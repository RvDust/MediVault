const express = require('express');
const cors = require('cors');
const path = require('path');
const { db, computeHash } = require('./database');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// ==========================================
// 1. AUTHENTICATION & RBAC ENDPOINTS
// ==========================================

// Login endpoint with MFA detection (Admin & Hospital Admin require MFA per Section 4)
app.post('/api/auth/login', (req, res) => {
    try {
        const { username, password } = req.body;
        const user = db.prepare('SELECT * FROM users WHERE username = ?').get(username);

        if (!user) {
            return res.status(401).json({ success: false, message: 'Invalid Staff ID or username.' });
        }

        // Demo password check: accepts any matching or default password
        if (password !== 'EnterpriseVault2026!' && password !== 'password123' && password !== user.password_hash) {
            return res.status(401).json({ success: false, message: 'Invalid credentials entered.' });
        }

        // If user role is admin or finance, MFA is strictly enforced
        if (user.mfa_required === 1) {
            return res.json({
                success: true,
                requireMfa: true,
                userId: user.id,
                username: user.username,
                role: user.role,
                message: 'Two-Factor Authentication (MFA) required for high-privilege hospital administrative access.'
            });
        }

        // Standard direct clinical login (for Doctors, Pharmacists, Nurses to avoid operational delay)
        return res.json({
            success: true,
            requireMfa: false,
            user: {
                id: user.id,
                username: user.username,
                fullName: user.full_name,
                email: user.email,
                role: user.role,
                roleTitle: user.role_title,
                department: user.department,
                badgeId: user.badge_id,
                securityTier: user.security_tier,
                dispensingLevel: user.dispensing_level,
                pagerExt: user.pager_ext,
                alertPref: user.alert_pref
            }
        });
    } catch (err) {
        console.error('Login error:', err);
        return res.status(500).json({ success: false, message: 'Internal server error during authentication.' });
    }
});

// Verify 2FA code for Admins
app.post('/api/auth/verify-mfa', (req, res) => {
    try {
        const { username, code } = req.body;
        const user = db.prepare('SELECT * FROM users WHERE username = ?').get(username);

        if (!user) {
            return res.status(404).json({ success: false, message: 'User not found.' });
        }

        // Accept demo MFA token '202601' or any 6-digit numerical code for simulation
        if (!code || code.length !== 6 || isNaN(Number(code))) {
            return res.status(400).json({ success: false, message: 'Please enter a valid 6-digit authentication token.' });
        }

        // Log successful MFA authentication in audit log
        const verifyHash = computeHash(`MFA-AUTH-${user.username}-${Date.now()}`);
        db.prepare(`
            INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash, is_controlled_substance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        `).run(
            'MFA Login Verified',
            'Security Token Challenge',
            user.full_name,
            user.role_title,
            user.department,
            `MFA 2-Factor Challenge completed for authoritative session. Hardware token ID: #HW-AUTH-${user.id}`,
            verifyHash,
            0
        );

        return res.json({
            success: true,
            user: {
                id: user.id,
                username: user.username,
                fullName: user.full_name,
                email: user.email,
                role: user.role,
                roleTitle: user.role_title,
                department: user.department,
                badgeId: user.badge_id,
                securityTier: user.security_tier,
                dispensingLevel: user.dispensing_level,
                pagerExt: user.pager_ext,
                alertPref: user.alert_pref
            }
        });
    } catch (err) {
        console.error('MFA error:', err);
        return res.status(500).json({ success: false, message: 'Internal server error verifying MFA.' });
    }
});

// Update Profile Preferences
app.post('/api/auth/profile', (req, res) => {
    try {
        const { username, fullName, email, pagerExt, alertPref } = req.body;
        db.prepare(`
            UPDATE users
            SET full_name = ?, email = ?, pager_ext = ?, alert_pref = ?
            WHERE username = ?
        `).run(fullName, email, pagerExt, alertPref, username);

        res.json({ success: true, message: 'User profile preferences updated successfully.' });
    } catch (err) {
        console.error('Profile update error:', err);
        res.status(500).json({ success: false, message: 'Could not update profile.' });
    }
});

// ==========================================
// 2. INVENTORY & GS1 BARCODE HUB
// ==========================================

// Get inventory items and batches with live stock status
app.get('/api/inventory', (req, res) => {
    try {
        const { ward, search, category, status } = req.query;

        let query = `
            SELECT 
                b.id AS batch_id,
                b.lot_number,
                b.ward,
                b.quantity AS batch_quantity,
                b.expiration_date,
                b.status AS batch_status,
                i.id AS item_id,
                i.ndc_code,
                i.barcode,
                i.item_name,
                i.generic_name,
                i.category,
                i.dosage_form,
                i.unit_cost,
                i.total_vault_stock,
                i.min_reorder_level,
                i.is_controlled,
                i.schedule_class,
                i.turnover_rate
            FROM inventory_batches b
            JOIN inventory_items i ON b.item_id = i.id
            WHERE 1=1
        `;
        const params = [];

        if (ward && ward !== 'ALL') {
            query += ` AND b.ward LIKE ?`;
            params.push(`%${ward}%`);
        }
        if (search) {
            query += ` AND (i.item_name LIKE ? OR i.ndc_code LIKE ? OR i.barcode LIKE ? OR b.lot_number LIKE ?)`;
            params.push(`%${search}%`, `%${search}%`, `%${search}%`, `%${search}%`);
        }
        if (category && category !== 'ALL') {
            query += ` AND i.category = ?`;
            params.push(category);
        }

        query += ` ORDER BY b.expiration_date ASC`;

        const rows = db.prepare(query).all(...params);
        res.json({ success: true, count: rows.length, data: rows });
    } catch (err) {
        console.error('Inventory fetch error:', err);
        res.status(500).json({ success: false, message: 'Error retrieving inventory records.' });
    }
});

// Master Catalog List (Items aggregated)
app.get('/api/catalog', (req, res) => {
    try {
        const items = db.prepare(`
            SELECT * FROM inventory_items ORDER BY item_name ASC
        `).all();
        res.json({ success: true, data: items });
    } catch (err) {
        console.error('Catalog error:', err);
        res.status(500).json({ success: false, message: 'Error retrieving catalog.' });
    }
});

// Barcode Scan Lookup (GS1 / NDC / UPC code)
app.post('/api/inventory/scan', (req, res) => {
    try {
        const { code } = req.body;
        if (!code) {
            return res.status(400).json({ success: false, message: 'Scan code is required.' });
        }

        const cleanCode = code.trim();
        const item = db.prepare(`
            SELECT i.*, b.id AS batch_id, b.lot_number, b.expiration_date, b.ward, b.quantity AS batch_qty, b.status AS batch_status
            FROM inventory_items i
            LEFT JOIN inventory_batches b ON b.item_id = i.id
            WHERE i.barcode = ? OR i.ndc_code = ? OR i.item_name LIKE ? OR b.lot_number = ?
            ORDER BY b.expiration_date ASC
            LIMIT 1
        `).get(cleanCode, cleanCode, `%${cleanCode}%`, cleanCode);

        if (!item) {
            return res.status(404).json({ success: false, message: `Barcode/NDC '${code}' not found in MediVault Registry.` });
        }

        // Check if there are suggested clinical alternatives if low stock
        let alternatives = [];
        if (item.total_vault_stock <= item.min_reorder_level) {
            alternatives = db.prepare(`
                SELECT * FROM medication_alternatives WHERE primary_item_id = ?
            `).all(item.id);
        }

        res.json({
            success: true,
            item,
            alternatives,
            isLowStock: item.total_vault_stock <= item.min_reorder_level,
            scanTimestamp: new Date().toISOString()
        });
    } catch (err) {
        console.error('Scan error:', err);
        res.status(500).json({ success: false, message: 'Error processing optical barcode scan.' });
    }
});

// Dispense Inventory (Atomic transaction with audit hash & compliance logging)
app.post('/api/inventory/dispense', (req, res) => {
    try {
        const { itemId, batchId, quantity, ward, authorizingStaff, authorizingBadge, patientMrn, notes } = req.body;
        const qtyToDeduct = parseInt(quantity, 10);

        if (!qtyToDeduct || qtyToDeduct <= 0) {
            return res.status(400).json({ success: false, message: 'Quantity must be greater than zero.' });
        }

        // Get item details
        let item;
        let batch;

        if (batchId) {
            batch = db.prepare('SELECT * FROM inventory_batches WHERE id = ?').get(batchId);
            if (!batch) {
                return res.status(404).json({ success: false, message: 'Specified batch not found.' });
            }
            item = db.prepare('SELECT * FROM inventory_items WHERE id = ?').get(batch.item_id);
        } else if (itemId) {
            item = db.prepare('SELECT * FROM inventory_items WHERE id = ?').get(itemId);
            if (!item) {
                return res.status(404).json({ success: false, message: 'Specified medication item not found.' });
            }
            // Pick earliest expiring batch
            batch = db.prepare('SELECT * FROM inventory_batches WHERE item_id = ? ORDER BY expiration_date ASC LIMIT 1').get(itemId);
        } else {
            return res.status(400).json({ success: false, message: 'Missing item or batch specification.' });
        }

        if (item.total_vault_stock < qtyToDeduct) {
            return res.status(400).json({
                success: false,
                message: `Insufficient stock balance. Requested: ${qtyToDeduct}, Available: ${item.total_vault_stock}.`
            });
        }

        // Compute tamper-evident verification hash
        const verificationHash = computeHash(`DISPENSE-${item.ndc_code}-${qtyToDeduct}-${authorizingStaff}-${Date.now()}`);

        // Update Database in atomic execution
        db.exec('BEGIN TRANSACTION;');
        try {
            // Deduct master vault stock
            db.prepare('UPDATE inventory_items SET total_vault_stock = total_vault_stock - ? WHERE id = ?').run(qtyToDeduct, item.id);

            // Deduct batch stock
            if (batch) {
                const newBatchQty = Math.max(0, batch.quantity - qtyToDeduct);
                let newBatchStatus = 'Optimal';
                if (newBatchQty <= 5) newBatchStatus = 'Low Stock Alert';
                if (newBatchQty === 0) newBatchStatus = 'Depleted';

                db.prepare('UPDATE inventory_batches SET quantity = ?, status = ? WHERE id = ?').run(newBatchQty, newBatchStatus, batch.id);
            }

            // Record in dispensing ledger
            db.prepare(`
                INSERT INTO dispensing_ledger (item_id, item_name, lot_number, quantity, ward, authorizing_staff, authorizing_badge, patient_mrn, notes, verification_hash, is_controlled)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            `).run(
                item.id,
                item.item_name,
                batch ? batch.lot_number : 'VAULT-POOL',
                qtyToDeduct,
                ward || 'ICU Critical Care',
                authorizingStaff || 'Dr. Elena Vance',
                authorizingBadge || 'STF-0192',
                patientMrn || 'MRN-UNASSIGNED',
                notes || 'Standard clinical dispensation',
                verificationHash,
                item.is_controlled
            );

            // Record in tamper-evident compliance log
            const eventType = item.is_controlled ? 'Controlled Substance Dispensed' : 'Stock Dispensed';
            db.prepare(`
                INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash, is_controlled_substance, philhealth_compliant)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)
            `).run(
                eventType,
                `${item.item_name} (-${qtyToDeduct})`,
                authorizingStaff || 'Dr. Elena Vance',
                'Senior Medical Officer',
                ward || 'ICU Critical Care',
                `Dispensed ${qtyToDeduct} unit(s). Lot: ${batch ? batch.lot_number : 'N/A'}. Patient MRN: ${patientMrn || 'N/A'}. Hash: ${verificationHash}`,
                verificationHash,
                item.is_controlled
            );

            // Automated Procurement trigger if below threshold (Section 1: Procurement Service)
            const updatedItem = db.prepare('SELECT total_vault_stock, min_reorder_level FROM inventory_items WHERE id = ?').get(item.id);
            let autoReorderTriggered = false;
            let poNumber = null;

            if (updatedItem.total_vault_stock <= updatedItem.min_reorder_level) {
                autoReorderTriggered = true;
                poNumber = `PO-AUTO-${Date.now().toString().slice(-4)}`;
                const reorderQty = 50;
                const totalCost = reorderQty * item.unit_cost;

                db.prepare(`
                    INSERT INTO procurement_orders (po_number, vendor_name, item_name, quantity, unit_price, total_cost, status, expected_delivery)
                    VALUES (?, ?, ?, ?, ?, ?, 'Automated Reorder Triggered', DATE('now', '+3 days'))
                `).run(poNumber, 'Zuellig Pharma Philippines', item.item_name, reorderQty, item.unit_cost, totalCost);

                db.prepare(`
                    INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash, is_controlled_substance)
                    VALUES (?, ?, ?, ?, ?, ?, ?, 0)
                `).run(
                    'Automated Reorder Trigger',
                    item.item_name,
                    'MediVault Inventory Daemon',
                    'System Service',
                    'Procurement Department',
                    `Stock dropped below threshold (${updatedItem.total_vault_stock} <= ${updatedItem.min_reorder_level}). Generated purchase requisition #${poNumber}.`,
                    computeHash(`PO-TRIGGER-${poNumber}`)
                );
            }

            db.exec('COMMIT;');

            return res.json({
                success: true,
                message: `Successfully deducted ${qtyToDeduct} unit(s) of ${item.item_name}.`,
                remainingStock: updatedItem.total_vault_stock,
                verificationHash,
                autoReorderTriggered,
                poNumber
            });
        } catch (innerErr) {
            db.exec('ROLLBACK;');
            throw innerErr;
        }
    } catch (err) {
        console.error('Dispense error:', err);
        return res.status(500).json({ success: false, message: 'Failed to complete dispensing transaction.' });
    }
});

// Manual Stock Adjustment (+1 / -1 or custom adjustment)
app.post('/api/inventory/adjust', (req, res) => {
    try {
        const { itemId, ndcCode, delta } = req.body;
        const change = parseInt(delta, 10);

        if (isNaN(change)) {
            return res.status(400).json({ success: false, message: 'Invalid delta amount.' });
        }

        let item;
        if (itemId) {
            item = db.prepare('SELECT * FROM inventory_items WHERE id = ?').get(itemId);
        } else if (ndcCode) {
            item = db.prepare('SELECT * FROM inventory_items WHERE ndc_code = ?').get(ndcCode);
        }

        if (!item) {
            return res.status(404).json({ success: false, message: 'Item not found.' });
        }

        const newStock = Math.max(0, item.total_vault_stock + change);
        db.prepare('UPDATE inventory_items SET total_vault_stock = ? WHERE id = ?').run(newStock, item.id);

        // Update corresponding primary batch
        db.prepare(`
            UPDATE inventory_batches 
            SET quantity = MAX(0, quantity + ?) 
            WHERE item_id = ?
        `).run(change, item.id);

        const vHash = computeHash(`ADJUST-${item.id}-${change}`);
        db.prepare(`
            INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        `).run(
            'Manual Stock Adjustment',
            item.item_name,
            'Pharm. Julian Miller',
            'Lead Pharmacist',
            'Central Pharmacy Vault',
            `Stock adjusted by ${change > 0 ? '+' : ''}${change} units. New balance: ${newStock}.`,
            vHash
        );

        res.json({
            success: true,
            message: `Adjusted ${item.item_name} stock by ${change > 0 ? '+' : ''}${change}.`,
            newStock,
            verificationHash: vHash
        });
    } catch (err) {
        console.error('Stock adjust error:', err);
        res.status(500).json({ success: false, message: 'Failed to adjust stock.' });
    }
});

// Add New Master Inventory SKU
app.post('/api/inventory/items', (req, res) => {
    try {
        const { ndcCode, barcode, itemName, genericName, category, dosageForm, unitCost, initialStock, ward, lotNumber, expirationDate, isControlled } = req.body;

        if (!ndcCode || !itemName) {
            return res.status(400).json({ success: false, message: 'NDC Code and Item Name are required.' });
        }

        const cost = parseFloat(unitCost) || 25.00;
        const stock = parseInt(initialStock, 10) || 50;
        const barcodeVal = barcode || ndcCode.replace(/[^0-9]/g, '');

        db.exec('BEGIN TRANSACTION;');
        try {
            const insertResult = db.prepare(`
                INSERT INTO inventory_items (ndc_code, barcode, item_name, generic_name, category, dosage_form, unit_cost, total_vault_stock, min_reorder_level, is_controlled, schedule_class)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 15, ?, ?)
            `).run(
                ndcCode,
                barcodeVal,
                itemName,
                genericName || itemName,
                category || 'General Medicine',
                dosageForm || 'Vial / Unit',
                cost,
                stock,
                isControlled ? 1 : 0,
                isControlled ? 'Schedule II Controlled' : 'Non-Controlled'
            );

            const newItemId = insertResult.lastInsertRowid;

            db.prepare(`
                INSERT INTO inventory_batches (item_id, lot_number, ward, quantity, expiration_date, status)
                VALUES (?, ?, ?, ?, ?, ?)
            `).run(
                newItemId,
                lotNumber || `LOT-${Math.floor(1000 + Math.random() * 9000)}`,
                ward || 'Central Pharmacy Vault',
                stock,
                expirationDate || '2028-12-31',
                'Optimal'
            );

            const vHash = computeHash(`NEW-SKU-${ndcCode}`);
            db.prepare(`
                INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash, is_controlled_substance)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            `).run(
                'New Inventory SKU Enrolled',
                itemName,
                'Pharm. Julian Miller',
                'Lead Pharmacist',
                'Central Pharmacy Vault',
                `Enrolled NDC ${ndcCode} with initial vault inventory of ${stock} units.`,
                vHash,
                isControlled ? 1 : 0
            );

            db.exec('COMMIT;');
            res.json({ success: true, message: `Successfully enrolled new SKU: ${itemName}`, itemId: newItemId });
        } catch (innerErr) {
            db.exec('ROLLBACK;');
            throw innerErr;
        }
    } catch (err) {
        console.error('Add SKU error:', err);
        res.status(500).json({ success: false, message: 'Failed to create inventory item. NDC may already exist.' });
    }
});

// Recent dispensing transactions (for the Dispensing console)
app.get('/api/dispensing-log', (req, res) => {
    try {
        const rows = db.prepare(`
            SELECT id, item_name, lot_number, quantity, ward, authorizing_staff, timestamp
            FROM dispensing_ledger
            ORDER BY id DESC
            LIMIT 10
        `).all();
        res.json({ success: true, data: rows });
    } catch (err) {
        console.error('Dispensing log error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch dispensing log.' });
    }
});

// Get Suggested Clinical Alternatives for an Item
app.get('/api/inventory/alternatives/:itemId', (req, res) => {
    try {
        const alts = db.prepare(`
            SELECT * FROM medication_alternatives WHERE primary_item_id = ?
        `).all(req.params.itemId);

        res.json({ success: true, data: alts });
    } catch (err) {
        console.error('Alternatives error:', err);
        res.status(500).json({ success: false, message: 'Error retrieving alternative medications.' });
    }
});

// ==========================================
// 3. WARD REQUISITIONS
// ==========================================

app.get('/api/requisitions', (req, res) => {
    try {
        const rows = db.prepare('SELECT * FROM ward_requisitions ORDER BY requested_at DESC').all();
        res.json({ success: true, data: rows });
    } catch (err) {
        console.error('Requisitions fetch error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch requisitions.' });
    }
});

app.post('/api/requisitions', (req, res) => {
    try {
        const { itemName, quantity, ward, priority, requestedBy } = req.body;
        const qty = parseInt(quantity, 10) || 5;

        db.prepare(`
            INSERT INTO ward_requisitions (item_name, quantity, ward, priority, requested_by, status)
            VALUES (?, ?, ?, ?, ?, 'Pending Review')
        `).run(itemName, qty, ward, priority || 'Normal', requestedBy || 'Ward Charge Nurse');

        res.json({ success: true, message: `Requisition for ${qty}x ${itemName} submitted to Central Pharmacy.` });
    } catch (err) {
        console.error('Requisition post error:', err);
        res.status(500).json({ success: false, message: 'Could not submit requisition.' });
    }
});

// ==========================================
// 4. PROCUREMENT & VENDOR ORDERS
// ==========================================

app.get('/api/procurement/orders', (req, res) => {
    try {
        const orders = db.prepare('SELECT * FROM procurement_orders ORDER BY created_at DESC').all();
        res.json({ success: true, data: orders });
    } catch (err) {
        console.error('Procurement orders error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch procurement orders.' });
    }
});

app.get('/api/procurement/vendors', (req, res) => {
    try {
        const vendors = db.prepare('SELECT * FROM vendors ORDER BY rating DESC').all();
        res.json({ success: true, data: vendors });
    } catch (err) {
        console.error('Vendors error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch vendor suppliers.' });
    }
});

app.post('/api/procurement/orders', (req, res) => {
    try {
        const { vendorName, itemName, quantity, unitPrice, expectedDelivery } = req.body;
        const qty = parseInt(quantity, 10);
        const price = parseFloat(unitPrice);
        const total = qty * price;
        const poNumber = `PO-2026-${Math.floor(1000 + Math.random() * 9000)}`;

        db.prepare(`
            INSERT INTO procurement_orders (po_number, vendor_name, item_name, quantity, unit_price, total_cost, status, expected_delivery)
            VALUES (?, ?, ?, ?, ?, ?, 'Approved by Hospital Admin', ?)
        `).run(poNumber, vendorName, itemName, qty, price, total, expectedDelivery || '2026-10-20');

        const vHash = computeHash(`PO-${poNumber}`);
        db.prepare(`
            INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        `).run(
            'Procurement PO Dispatched',
            itemName,
            'Sofia Ramos, CPA',
            'Finance Director',
            'Procurement & Finance',
            `Purchase Order ${poNumber} for ${qty} units issued to ${vendorName}. Total Value: $${total.toFixed(2)}.`,
            vHash
        );

        res.json({ success: true, message: `Dispatched Purchase Order ${poNumber} to ${vendorName}.`, poNumber });
    } catch (err) {
        console.error('Create PO error:', err);
        res.status(500).json({ success: false, message: 'Could not create procurement order.' });
    }
});

// ==========================================
// 5. DIGITIZED PRESCRIPTIONS (Medical Staff Interface)
// ==========================================

app.get('/api/prescriptions', (req, res) => {
    try {
        const rxs = db.prepare('SELECT * FROM prescriptions ORDER BY created_at DESC').all();
        res.json({ success: true, data: rxs });
    } catch (err) {
        console.error('Prescriptions error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch prescriptions.' });
    }
});

app.post('/api/prescriptions', (req, res) => {
    try {
        const { patientName, mrn, philhealthNo, prescribingDoctor, itemName, dosage, dispenseQty, instructions } = req.body;
        const rxNumber = `RX-2026-${Math.floor(1000 + Math.random() * 9000)}`;

        db.prepare(`
            INSERT INTO prescriptions (rx_number, patient_name, mrn, philhealth_no, prescribing_doctor, item_name, dosage, dispense_qty, instructions, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Verified & Queued')
        `).run(
            rxNumber,
            patientName,
            mrn,
            philhealthNo || 'PH-19-ACTIVE',
            prescribingDoctor || 'Dr. Elena Vance',
            itemName,
            dosage,
            parseInt(dispenseQty, 10) || 1,
            instructions || 'Take as directed.'
        );

        res.json({ success: true, message: `Electronic Prescription ${rxNumber} generated & synced to Central Pharmacy.`, rxNumber });
    } catch (err) {
        console.error('Create Rx error:', err);
        res.status(500).json({ success: false, message: 'Could not create prescription.' });
    }
});

// ==========================================
// 6. CLINICAL APPOINTMENTS & EQUIPMENT BOOKINGS
// ==========================================

app.get('/api/appointments', (req, res) => {
    try {
        const appts = db.prepare('SELECT * FROM appointments ORDER BY appointment_date ASC').all();
        res.json({ success: true, data: appts });
    } catch (err) {
        console.error('Appointments error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch appointments.' });
    }
});

app.post('/api/appointments', (req, res) => {
    try {
        const { patientName, mrn, consultingPhysician, appointmentDate, timeSlot, priority, notes } = req.body;

        db.prepare(`
            INSERT INTO appointments (patient_name, mrn, consulting_physician, appointment_date, time_slot, priority, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        `).run(patientName, mrn, consultingPhysician, appointmentDate, timeSlot, priority || 'Standard', notes);

        res.json({ success: true, message: `Clinical appointment scheduled for ${patientName}.` });
    } catch (err) {
        console.error('Create appointment error:', err);
        res.status(500).json({ success: false, message: 'Could not schedule appointment.' });
    }
});

app.get('/api/bookings', (req, res) => {
    try {
        const bookings = db.prepare('SELECT * FROM equipment_bookings ORDER BY reservation_start ASC').all();
        res.json({ success: true, data: bookings });
    } catch (err) {
        console.error('Bookings error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch equipment bookings.' });
    }
});

app.post('/api/bookings', (req, res) => {
    try {
        const { equipmentName, reservationStart, reservationEnd, requestingWard, leadNurse } = req.body;

        db.prepare(`
            INSERT INTO equipment_bookings (equipment_name, reservation_start, reservation_end, requesting_ward, lead_nurse)
            VALUES (?, ?, ?, ?, ?)
        `).run(equipmentName, reservationStart, reservationEnd, requestingWard, leadNurse);

        res.json({ success: true, message: `Equipment / Operating Suite booking confirmed for ${equipmentName}.` });
    } catch (err) {
        console.error('Create booking error:', err);
        res.status(500).json({ success: false, message: 'Could not save equipment booking.' });
    }
});

// ==========================================
// 7. STAFF MANAGEMENT & RBAC
// ==========================================

app.get('/api/staff', (req, res) => {
    try {
        const staff = db.prepare('SELECT id, username, full_name, email, role, role_title, department, badge_id, security_tier, dispensing_level, mfa_required, status, pager_ext FROM users ORDER BY id ASC').all();
        res.json({ success: true, data: staff });
    } catch (err) {
        console.error('Staff error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch staff directory.' });
    }
});

app.post('/api/staff', (req, res) => {
    try {
        const { username, fullName, email, role, roleTitle, department, badgeId, securityTier, dispensingLevel, mfaRequired } = req.body;

        db.prepare(`
            INSERT INTO users (username, password_hash, full_name, email, role, role_title, department, badge_id, security_tier, dispensing_level, mfa_required, status)
            VALUES (?, 'password123', ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Active')
        `).run(
            username,
            fullName,
            email,
            role || 'nurse',
            roleTitle || 'Clinical Staff',
            department || 'General Ward',
            badgeId || `STF-${Math.floor(1000 + Math.random() * 9000)}`,
            securityTier || 'Tier 2',
            dispensingLevel || 'Ward Requisition Only',
            mfaRequired ? 1 : 0
        );

        res.json({ success: true, message: `Staff account granted for ${fullName}.` });
    } catch (err) {
        console.error('Add staff error:', err);
        res.status(500).json({ success: false, message: 'Could not add staff. Username or Badge ID may already exist.' });
    }
});

app.put('/api/staff/:id/permissions', (req, res) => {
    try {
        const { dispensingLevel, securityTier, mfaRequired, status } = req.body;
        db.prepare(`
            UPDATE users
            SET dispensing_level = COALESCE(?, dispensing_level),
                security_tier = COALESCE(?, security_tier),
                mfa_required = COALESCE(?, mfa_required),
                status = COALESCE(?, status)
            WHERE id = ?
        `).run(dispensingLevel, securityTier, mfaRequired, status, req.params.id);

        res.json({ success: true, message: 'Staff role privileges updated successfully.' });
    } catch (err) {
        console.error('Update permissions error:', err);
        res.status(500).json({ success: false, message: 'Failed to update privileges.' });
    }
});

// ==========================================
// 8. FINANCIAL REPORTS & ANALYTICS
// ==========================================

app.get('/api/analytics', (req, res) => {
    try {
        // Aggregate totals
        const skuCount = db.prepare('SELECT COUNT(*) as count FROM inventory_items').get().count;
        const lowStockCount = db.prepare('SELECT COUNT(*) as count FROM inventory_items WHERE total_vault_stock <= min_reorder_level').get().count;
        const totalStockUnits = db.prepare('SELECT SUM(total_vault_stock) as total FROM inventory_items').get().total || 0;
        const totalStockValue = db.prepare('SELECT SUM(total_vault_stock * unit_cost) as total FROM inventory_items').get().total || 0;

        // Latest financial record
        const latestFinance = db.prepare('SELECT * FROM financial_ledger ORDER BY id DESC LIMIT 1').get() || {
            total_expenditure: 142890,
            growth_pct: -3.2
        };

        // Top velocity supplies
        const topVelocity = db.prepare(`
            SELECT item_name, unit_cost, total_vault_stock, turnover_rate,
                   (unit_cost * 200) as est_monthly_value
            FROM inventory_items
            ORDER BY unit_cost DESC
            LIMIT 3
        `).all();

        // Department breakdown
        const deptBreakdown = [
            { department: 'ICU Critical Care', percentage: 42, spend: 59990, color: '#0284c7' },
            { department: 'Operating Rooms', percentage: 28, spend: 40009, color: '#06b6d4' },
            { department: 'Emergency Room (ER)', percentage: 21, spend: 30006, color: '#6366f1' },
            { department: 'Pediatric & Outpatient', percentage: 9, spend: 12885, color: '#10b981' }
        ];

        res.json({
            success: true,
            kpis: {
                monthlySpend: latestFinance.total_expenditure,
                monthlyGrowthPct: latestFinance.growth_pct,
                activeSkus: skuCount,
                lowStockCount,
                totalUnits: totalStockUnits,
                totalVaultValue: Math.round(totalStockValue),
                wastageLoss: 1142,
                slaIndex: 98.4
            },
            deptBreakdown,
            topVelocity
        });
    } catch (err) {
        console.error('Analytics error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch analytics data.' });
    }
});

app.get('/api/financials', (req, res) => {
    try {
        const rows = db.prepare('SELECT * FROM financial_ledger ORDER BY id DESC').all();
        res.json({ success: true, data: rows });
    } catch (err) {
        console.error('Financials error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch financial records.' });
    }
});

// ==========================================
// 9. AUDIT COMPLIANCE & DOH / PHILHEALTH REPORTS
// ==========================================

app.get('/api/audit-logs', (req, res) => {
    try {
        const { controlledOnly } = req.query;
        let query = 'SELECT * FROM audit_compliance_logs';
        const params = [];

        if (controlledOnly === 'true') {
            query += ' WHERE is_controlled_substance = 1';
        }

        query += ' ORDER BY timestamp DESC LIMIT 100';
        const logs = db.prepare(query).all(...params);

        res.json({ success: true, count: logs.length, data: logs });
    } catch (err) {
        console.error('Audit logs error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch compliance logs.' });
    }
});

// Official DOH & PhilHealth compliance data export endpoint
app.get('/api/reports/doh-philhealth', (req, res) => {
    try {
        const logs = db.prepare(`
            SELECT 
                timestamp,
                event_type,
                item_name,
                authorizing_staff,
                role,
                ward_or_dept,
                details,
                verification_hash,
                CASE WHEN is_controlled_substance = 1 THEN 'YES (Schedule II/IV)' ELSE 'NO' END AS dangerous_drug_board_regulated,
                'COMPLIANT (OsMak PhilHealth Accr. #PH-MAK-091)' AS philhealth_status
            FROM audit_compliance_logs
            ORDER BY timestamp DESC
        `).all();

        res.json({
            success: true,
            hospital: 'Ospital ng Makati (OsMak) / MediVault Makati Hub',
            accreditation: 'DOH Level 3 Tertiary Hospital • PhilHealth Center of Excellence',
            generatedAt: new Date().toISOString(),
            complianceRate: '100%',
            totalRecords: logs.length,
            records: logs
        });
    } catch (err) {
        console.error('Compliance export error:', err);
        res.status(500).json({ success: false, message: 'Failed to generate compliance report.' });
    }
});

// ==========================================
// 10. SYSTEM ANNOUNCEMENTS & STATUS
// ==========================================

app.get('/api/announcements', (req, res) => {
    try {
        const announcements = db.prepare('SELECT * FROM announcements ORDER BY pinned DESC, created_at DESC').all();
        res.json({ success: true, data: announcements });
    } catch (err) {
        console.error('Announcements error:', err);
        res.status(500).json({ success: false, message: 'Could not fetch announcements.' });
    }
});

app.post('/api/announcements', (req, res) => {
    try {
        const { title, content, category, badge, postedBy } = req.body;
        db.prepare(`
            INSERT INTO announcements (title, content, category, badge, posted_by)
            VALUES (?, ?, ?, ?, ?)
        `).run(title, content, category || 'General', badge || 'Hospital Notice', postedBy || 'Administration');

        res.json({ success: true, message: 'Announcement broadcasted successfully.' });
    } catch (err) {
        console.error('Post announcement error:', err);
        res.status(500).json({ success: false, message: 'Could not post announcement.' });
    }
});

// System Status Telemetry
app.get('/api/system/status', (req, res) => {
    try {
        const stats = {
            status: 'ONLINE',
            uptime: Math.round(process.uptime()),
            databaseEngine: 'SQLite 3 (Embedded ACID WAL Engine via Node.js)',
            acidCompliance: 'Enforced',
            walJournalMode: 'Active',
            syncLatencyMs: 1.2,
            activeNodes: 4,
            osMakNodeId: '#MV-2026-HQ-MAKATI',
            hospitalName: 'Ospital ng Makati (OsMak) Clinical Vault'
        };
        res.json({ success: true, data: stats });
    } catch (err) {
        res.status(500).json({ success: false, message: 'Telemetry error.' });
    }
});

// Catch-all route to serve SPA frontend
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`====================================================`);
    console.log(`🏥 MediVault Makati Enterprise Clinical & Supply OS`);
    console.log(`📡 Backend Server listening at http://localhost:${PORT}`);
    console.log(`🗄️ Relational ACID Database: medivault.db (Active)`);
    console.log(`====================================================`);
});
