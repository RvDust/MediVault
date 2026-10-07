const { DatabaseSync } = require('node:sqlite');
const path = require('path');
const crypto = require('crypto');

const dbPath = path.join(__dirname, 'medivault.db');
const db = new DatabaseSync(dbPath);

// Enable WAL mode and foreign keys for high-performance ACID compliance
db.exec('PRAGMA journal_mode = WAL;');
db.exec('PRAGMA foreign_keys = ON;');

function computeHash(dataString) {
    return '0x' + crypto.createHash('sha256').update(dataString + Date.now().toString()).digest('hex').substring(0, 16);
}

function initDatabase() {
    // 1. Users & RBAC
    db.exec(`
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL,
            role_title TEXT NOT NULL,
            department TEXT NOT NULL,
            badge_id TEXT UNIQUE NOT NULL,
            security_tier TEXT NOT NULL,
            dispensing_level TEXT NOT NULL,
            mfa_required INTEGER DEFAULT 0,
            status TEXT DEFAULT 'Active',
            pager_ext TEXT DEFAULT 'Ext. 4092 (ICU Desk 3)',
            alert_pref TEXT DEFAULT 'Real-Time Push & Email Digest',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 2. Master Inventory Items
    db.exec(`
        CREATE TABLE IF NOT EXISTS inventory_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ndc_code TEXT UNIQUE NOT NULL,
            barcode TEXT UNIQUE NOT NULL,
            item_name TEXT NOT NULL,
            generic_name TEXT NOT NULL,
            category TEXT NOT NULL,
            dosage_form TEXT NOT NULL,
            unit_cost REAL NOT NULL,
            total_vault_stock INTEGER NOT NULL DEFAULT 0,
            min_reorder_level INTEGER NOT NULL DEFAULT 15,
            is_controlled INTEGER DEFAULT 0,
            schedule_class TEXT DEFAULT 'Non-Controlled',
            turnover_rate TEXT DEFAULT 'Steady (2.5x)',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 3. Batches / Lots (Lot tracking, ward locations, expiration dates)
    db.exec(`
        CREATE TABLE IF NOT EXISTS inventory_batches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER NOT NULL,
            lot_number TEXT NOT NULL,
            ward TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            expiration_date DATE NOT NULL,
            status TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (item_id) REFERENCES inventory_items(id) ON DELETE CASCADE
        );
    `);

    // 4. Clinical Medication Alternatives (for Doctors/Nurses when stock is low/out)
    db.exec(`
        CREATE TABLE IF NOT EXISTS medication_alternatives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            primary_item_id INTEGER NOT NULL,
            alternative_name TEXT NOT NULL,
            ndc_code TEXT NOT NULL,
            dosage_info TEXT NOT NULL,
            clinical_indication TEXT NOT NULL,
            stock_status TEXT NOT NULL,
            FOREIGN KEY (primary_item_id) REFERENCES inventory_items(id) ON DELETE CASCADE
        );
    `);

    // 5. Dispensing Ledger
    db.exec(`
        CREATE TABLE IF NOT EXISTS dispensing_ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            lot_number TEXT,
            quantity INTEGER NOT NULL,
            ward TEXT NOT NULL,
            authorizing_staff TEXT NOT NULL,
            authorizing_badge TEXT,
            patient_mrn TEXT,
            notes TEXT,
            verification_hash TEXT NOT NULL,
            is_controlled INTEGER DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (item_id) REFERENCES inventory_items(id)
        );
    `);

    // 6. Ward Requisitions
    db.exec(`
        CREATE TABLE IF NOT EXISTS ward_requisitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            ward TEXT NOT NULL,
            priority TEXT DEFAULT 'Normal',
            requested_by TEXT NOT NULL,
            status TEXT DEFAULT 'Pending Review',
            requested_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            fulfilled_at DATETIME
        );
    `);

    // 7. Vendors & Distributors
    db.exec(`
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT UNIQUE NOT NULL,
            contact_person TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            rating REAL DEFAULT 4.9,
            active_status TEXT DEFAULT 'Active'
        );
    `);

    // 8. Procurement Purchase Orders
    db.exec(`
        CREATE TABLE IF NOT EXISTS procurement_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            po_number TEXT UNIQUE NOT NULL,
            vendor_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_cost REAL NOT NULL,
            status TEXT DEFAULT 'Pending Approval',
            expected_delivery DATE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 9. Tamper-Evident Audit & Compliance Logs (DOH / PhilHealth Compliance)
    db.exec(`
        CREATE TABLE IF NOT EXISTS audit_compliance_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            item_name TEXT NOT NULL,
            authorizing_staff TEXT NOT NULL,
            role TEXT NOT NULL,
            ward_or_dept TEXT NOT NULL,
            details TEXT NOT NULL,
            verification_hash TEXT NOT NULL,
            is_controlled_substance INTEGER DEFAULT 0,
            philhealth_compliant INTEGER DEFAULT 1,
            doh_flagged INTEGER DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 10. Digitized Prescriptions (Medical Staff Interface)
    db.exec(`
        CREATE TABLE IF NOT EXISTS prescriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rx_number TEXT UNIQUE NOT NULL,
            patient_name TEXT NOT NULL,
            mrn TEXT NOT NULL,
            philhealth_no TEXT,
            prescribing_doctor TEXT NOT NULL,
            item_name TEXT NOT NULL,
            dosage TEXT NOT NULL,
            dispense_qty INTEGER NOT NULL,
            instructions TEXT NOT NULL,
            status TEXT DEFAULT 'Pending Dispense',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 11. Clinical Appointments
    db.exec(`
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            mrn TEXT NOT NULL,
            consulting_physician TEXT NOT NULL,
            appointment_date DATE NOT NULL,
            time_slot TEXT NOT NULL,
            priority TEXT DEFAULT 'Standard',
            notes TEXT,
            status TEXT DEFAULT 'Confirmed',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 12. Equipment & Operating Suite Bookings
    db.exec(`
        CREATE TABLE IF NOT EXISTS equipment_bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment_name TEXT NOT NULL,
            reservation_start DATETIME NOT NULL,
            reservation_end DATETIME NOT NULL,
            requesting_ward TEXT NOT NULL,
            lead_nurse TEXT NOT NULL,
            status TEXT DEFAULT 'Confirmed',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 13. System Announcements
    db.exec(`
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            badge TEXT NOT NULL,
            badge_color TEXT DEFAULT 'medical',
            pinned INTEGER DEFAULT 0,
            posted_by TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    // 14. Financial Reports (Makati LGU & Hospital Admin)
    db.exec(`
        CREATE TABLE IF NOT EXISTS financial_ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            billing_month TEXT UNIQUE NOT NULL,
            pharmaceutical_spend REAL NOT NULL,
            surgical_spend REAL NOT NULL,
            equipment_amortization REAL NOT NULL,
            total_expenditure REAL NOT NULL,
            growth_pct REAL DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    `);

    seedDataIfEmpty();
}

function seedDataIfEmpty() {
    const userCount = db.prepare('SELECT COUNT(*) as count FROM users').get().count;
    if (userCount > 0) return;

    console.log('Seeding initial MediVault Makati enterprise data...');

    // Seed Users
    const insertUser = db.prepare(`
        INSERT INTO users (username, password_hash, full_name, email, role, role_title, department, badge_id, security_tier, dispensing_level, mfa_required, status, pager_ext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertUser.run(
        'dr.elena.vance',
        'password123',
        'Dr. Elena Vance, MD, FACP',
        'elena.vance@mediavault-health.org',
        'doctor',
        'Senior Medical Officer',
        'ICU Critical Care',
        'STF-0192',
        'Tier 4 (Full Clinical Authorizer)',
        'Full Approval & Schedule II',
        0,
        'Active',
        'Ext. 4092 (ICU Desk 3)'
    );

    insertUser.run(
        'pharm.j.miller',
        'password123',
        'Pharm. Julian Miller, RPh',
        'julian.miller@mediavault-health.org',
        'pharmacist',
        'Lead Pharmacist',
        'Central Pharmacy Vault',
        'STF-0481',
        'Tier 4 (Pharmacy Master)',
        'Catalog Master Control & Procurement',
        0,
        'Active',
        'Ext. 5110 (Central Vault)'
    );

    insertUser.run(
        'nurse.clara.reyes',
        'password123',
        'Nurse Clara Reyes, RN',
        'clara.reyes@mediavault-health.org',
        'nurse',
        'ER Staff Nurse',
        'Emergency Room',
        'STF-0914',
        'Tier 2 (Ward Clinical)',
        'Ward Requisition Only',
        0,
        'Active',
        'Ext. 9112 (ER Triage)'
    );

    insertUser.run(
        'admin.root',
        'password123',
        'Roberto Cruz (Chief Information Officer)',
        'admin@mediavault-makati.gov.ph',
        'admin',
        'Hospital Administrator',
        'IT & Administrative Services',
        'ADM-001',
        'Tier 5 (Super Administrator)',
        'Full System Configuration & User Admin',
        1, // MFA Required
        'Active',
        'Ext. 1001 (HQ)'
    );

    insertUser.run(
        'finance.director',
        'password123',
        'Sofia Ramos, CPA (Finance Director)',
        'sofia.ramos@makati.gov.ph',
        'finance',
        'Finance Director & Makati LGU Auditor',
        'Hospital Finance & Makati LGU Oversight',
        'FIN-0082',
        'Tier 4 (Financial Oversight)',
        'Financial Audit & Analytics Only',
        1, // MFA Required
        'Active',
        'Ext. 2040 (Audit Hall)'
    );

    // Seed Master Inventory Items
    const insertItem = db.prepare(`
        INSERT INTO inventory_items (ndc_code, barcode, item_name, generic_name, category, dosage_form, unit_cost, total_vault_stock, min_reorder_level, is_controlled, schedule_class, turnover_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertItem.run('004-981-22', '00498122019', 'Epinephrine 1mg/mL Auto-Inj', 'Epinephrine', 'Emergency / Vasoactive', 'Auto-Injector 1mg/mL', 30.00, 48, 15, 0, 'Non-Controlled', 'Fast (3.8x)');
    insertItem.run('012-774-88', '01277488031', 'Propofol Emulsion 20mL Vial', 'Propofol', 'Anesthetics', 'Injectable Emulsion 10mg/mL', 38.33, 6, 12, 1, 'Schedule IV Sedative', 'Fast (4.2x)');
    insertItem.run('008-312-09', '00831209044', 'Surgical N95 Respirators (Box 20)', 'N95 Particulate Respirator', 'PPE / Safety', 'Box of 20 units', 65.00, 114, 30, 0, 'Non-Controlled', 'Steady (2.9x)');
    insertItem.run('019-442-12', '01944212055', 'Heparin Sodium 5,000 U/mL', 'Heparin Sodium', 'Anticoagulants', 'Vial 5,000 USP Units/mL', 24.50, 3, 10, 0, 'Non-Controlled', 'High Velocity');
    insertItem.run('040-911-33', '04091133066', 'Morphine Sulfate 10mg/mL', 'Morphine Sulfate', 'Analgesics / Narcotics', 'Ampule 10mg/mL', 18.75, 24, 10, 1, 'Schedule II Narcotic', 'Controlled Steady');
    insertItem.run('025-441-19', '02544119077', 'Midazolam 5mg/mL Inj', 'Midazolam', 'Sedatives / Hypnotics', 'Vial 5mg/mL (2mL)', 14.20, 32, 12, 1, 'Schedule IV Controlled', 'Moderate');
    insertItem.run('078-112-90', '07811290088', 'Cefuroxime 750mg Vial', 'Cefuroxime Axetil', 'Antibiotics', 'IV Powder for Injection', 8.50, 85, 25, 0, 'Non-Controlled', 'High Velocity');
    insertItem.run('033-882-14', '03388214099', 'Norepinephrine 4mg/4mL', 'Norepinephrine Bitartrate', 'Emergency / Vasoactive', 'Ampule 4mg/4mL', 28.00, 35, 10, 0, 'Non-Controlled', 'Fast (3.5x)');
    insertItem.run('062-990-41', '06299041011', 'Etomidate 20mg/10mL', 'Etomidate', 'Anesthetics', 'Vial 2mg/mL', 42.00, 18, 8, 0, 'Non-Controlled', 'Alternative Anesthetic');
    insertItem.run('051-772-23', '05177223022', 'Enoxaparin Sodium 40mg/0.4mL', 'Enoxaparin Sodium (LMWH)', 'Anticoagulants', 'Prefilled Syringe', 32.50, 40, 15, 0, 'Non-Controlled', 'Steady (3.1x)');

    // Seed Batches / Lots
    const insertBatch = db.prepare(`
        INSERT INTO inventory_batches (item_id, lot_number, ward, quantity, expiration_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    `);

    insertBatch.run(1, 'EP-9941', 'ICU Critical Care', 48, '2027-08-14', 'Optimal');
    insertBatch.run(2, 'PR-3012', 'Operating Rooms', 6, '2026-10-30', 'Low Stock Alert');
    insertBatch.run(3, 'N95-4421', 'Emergency Room', 114, '2028-11-01', 'Optimal');
    insertBatch.run(4, 'HEP-8810', 'ICU Critical Care', 3, '2026-09-28', 'Expiring Soon');
    insertBatch.run(5, 'MS-2026A', 'Central Pharmacy Vault', 24, '2027-05-20', 'Optimal');
    insertBatch.run(6, 'MDZ-901', 'Operating Rooms', 32, '2027-03-15', 'Optimal');
    insertBatch.run(7, 'CEF-882', 'Pediatric & Outpatient', 85, '2027-12-01', 'Optimal');
    insertBatch.run(8, 'NE-4491', 'ICU Critical Care', 35, '2027-06-30', 'Optimal');
    insertBatch.run(9, 'ETO-319', 'Operating Rooms', 18, '2027-04-12', 'Optimal');
    insertBatch.run(10, 'ENO-771', 'ICU Critical Care', 40, '2027-09-18', 'Optimal');

    // Seed Medication Alternatives (Essential for Medical Staff Interface as per Section 1)
    const insertAlt = db.prepare(`
        INSERT INTO medication_alternatives (primary_item_id, alternative_name, ndc_code, dosage_info, clinical_indication, stock_status)
        VALUES (?, ?, ?, ?, ?, ?)
    `);

    insertAlt.run(2, 'Etomidate 20mg/10mL', '062-990-41', '0.2 - 0.3 mg/kg IV', 'Rapid Sequence Intubation & Induction (Cardiovascular Stable)', 'In Stock (18 units)');
    insertAlt.run(2, 'Midazolam 5mg/mL Inj', '025-441-19', '0.05 - 0.1 mg/kg IV', 'Procedural Sedation & Anxiolysis', 'In Stock (32 units)');
    insertAlt.run(4, 'Enoxaparin Sodium 40mg/0.4mL', '051-772-23', '40mg SC once daily', 'DVT/PE Prophylaxis & Therapeutic Anticoagulation', 'In Stock (40 units)');
    insertAlt.run(1, 'Norepinephrine 4mg/4mL', '033-882-14', '0.01 - 3 mcg/kg/min IV Titrate', 'First-line Vasopressor for Septic & Cardiogenic Shock', 'In Stock (35 units)');

    // Seed Dispensing History
    const insertDispense = db.prepare(`
        INSERT INTO dispensing_ledger (item_id, item_name, lot_number, quantity, ward, authorizing_staff, authorizing_badge, patient_mrn, notes, verification_hash, is_controlled, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertDispense.run(1, 'Epinephrine 1mg/mL Auto-Inj', 'EP-9941', 2, 'ICU Critical Care', 'Dr. Elena Vance', 'STF-0192', 'MRN-8812', 'Emergency anaphylaxis stabilization', '0x8f9a4c1231b2e9a0', 0, '2026-10-07 14:12:08');
    insertDispense.run(3, 'Surgical N95 Respirators (Box 20)', 'N95-4421', 5, 'Emergency Room', 'Nurse Clara Reyes', 'STF-0914', 'MRN-9021', 'ER isolation precaution replenishment', '0xa41b7f830d12e441', 0, '2026-10-07 11:04:22');
    insertDispense.run(2, 'Propofol Emulsion 20mL Vial', 'PR-3012', 1, 'Operating Rooms', 'Dr. Elena Vance', 'STF-0192', 'MRN-7740', 'General anesthesia induction OR Suite 3', '0x4c2e881090a1bc34', 1, '2026-10-06 09:30:15');

    // Seed Requisitions
    const insertReq = db.prepare(`
        INSERT INTO ward_requisitions (item_name, quantity, ward, priority, requested_by, status, requested_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    `);

    insertReq.run('Epinephrine 1mg/mL Auto-Inj', 6, 'ICU Critical Care', 'Urgent', 'Nurse Clara Reyes', 'Approved & Dispatched', '2026-10-07 08:15:00');
    insertReq.run('Propofol Emulsion 20mL Vial', 10, 'Operating Rooms', 'High', 'Dr. Elena Vance', 'Pending Pharmacist Release', '2026-10-07 10:20:00');
    insertReq.run('Surgical N95 Respirators (Box 20)', 15, 'Emergency Room', 'Normal', 'Nurse Clara Reyes', 'Pending Review', '2026-10-07 12:45:00');

    // Seed Vendors (Section 1 Integration Layer: Vendor & Distributor Systems)
    const insertVendor = db.prepare(`
        INSERT INTO vendors (name, code, contact_person, email, phone, address, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    `);

    insertVendor.run('Zuellig Pharma Philippines', 'VND-ZUELLIG', 'Ramon Valdez', 'orders@zuelligpharma.com.ph', '+63 2 8982 7700', 'KM 14 West Service Rd, Parañaque, Metro Manila', 4.9);
    insertVendor.run('Metro Drug Inc.', 'VND-METRO', 'Patricia Santos', 'hospital.sales@metrodrug.com.ph', '+63 2 8837 0122', 'Mañalac Ave, Bicutan, Taguig City', 4.8);
    insertVendor.run('PhilPharma LGU Supply Alliance', 'VND-PHILPHARMA', 'Engr. Dan Navarro', 'makati.depot@philpharma.gov.ph', '+63 2 8870 1400', 'Chino Roces Ave, Makati City', 4.9);
    insertVendor.run('Unilab Hospital Solutions', 'VND-UNILAB', 'Beatriz Mendoza', 'institutional@unilab.com.ph', '+63 2 8858 1000', '66 United St, Mandaluyong City', 4.9);

    // Seed Procurement Orders
    const insertPO = db.prepare(`
        INSERT INTO procurement_orders (po_number, vendor_name, item_name, quantity, unit_price, total_cost, status, expected_delivery)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertPO.run('PO-2026-0891', 'Zuellig Pharma Philippines', 'Propofol Emulsion 20mL Vial', 50, 38.33, 1916.50, 'Dispatched / In-Transit', '2026-10-10');
    insertPO.run('PO-2026-0892', 'Metro Drug Inc.', 'Heparin Sodium 5,000 U/mL', 40, 24.50, 980.00, 'Approved by LGU Finance', '2026-10-11');
    insertPO.run('PO-2026-0888', 'PhilPharma LGU Supply Alliance', 'Surgical N95 Respirators (Box 20)', 100, 65.00, 6500.00, 'Delivered & Vaulted', '2026-10-05');

    // Seed Audit Compliance Logs (DOH & PhilHealth compliance as per Section 1 & 4)
    const insertAudit = db.prepare(`
        INSERT INTO audit_compliance_logs (event_type, item_name, authorizing_staff, role, ward_or_dept, details, verification_hash, is_controlled_substance, philhealth_compliant, doh_flagged, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertAudit.run('Stock Dispensed', 'Epinephrine 1mg/mL Auto-Inj (-2)', 'Dr. Elena Vance', 'Senior Medical Officer', 'ICU Critical Care', 'Dispensed to Patient #MRN-8812 under ICU Protocol Beta', '0x8f9a2b1331b2e911', 0, 1, 0, '2026-10-07 14:12:08');
    insertAudit.run('GS1 Scan Verified', 'Propofol Emulsion 20mL Vial', 'Pharm. Julian Miller', 'Lead Pharmacist', 'Central Pharmacy Vault', 'GS1 DataMatrix Verified: Lot PR-3012 Exp 2026-10-30', '0x4c2e910490a1bc34', 1, 1, 0, '2026-10-07 11:04:22');
    insertAudit.run('Controlled Substance Signoff', 'Morphine Sulfate 10mg/mL', 'Dr. Elena Vance', 'Senior Medical Officer', 'ICU Critical Care', 'Dual Sign-Off with Nurse Clara Reyes. DOH Form 34 logged.', '0x99a01f42e3157b88', 1, 1, 0, '2026-10-06 18:22:40');
    insertAudit.run('Automated Reorder Trigger', 'Heparin Sodium 5,000 U/mL', 'System Daemon (Auto-Procure)', 'System', 'Procurement Service', 'Stock below safety threshold (3 <= 10). Generated PO-2026-0892.', '0x71b288c3a9010ef5', 0, 1, 0, '2026-10-06 08:00:00');

    // Seed Prescriptions (Digitized Prescriptions as per Section 1)
    const insertRx = db.prepare(`
        INSERT INTO prescriptions (rx_number, patient_name, mrn, philhealth_no, prescribing_doctor, item_name, dosage, dispense_qty, instructions, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertRx.run('RX-2026-0041', 'Arthur Pendelton', 'MRN-8812', 'PH-19-00284711-2', 'Dr. Elena Vance', 'Epinephrine 1mg/mL Auto-Inj', '1mg IM stat', 2, 'Administer immediately upon bronchospasm', 'Dispensed');
    insertRx.run('RX-2026-0042', 'Maria Teresa Santos', 'MRN-9021', 'PH-19-09482711-9', 'Dr. Elena Vance', 'Cefuroxime 750mg Vial', '750mg IV q8h', 6, 'Post-operative antibiotic prophylaxis', 'Pending Dispense');
    insertRx.run('RX-2026-0043', 'Eduardo Dimaculangan', 'MRN-7740', 'PH-19-03829104-5', 'Dr. Elena Vance', 'Heparin Sodium 5,000 U/mL', '5000 units SC q12h', 4, 'Monitor aPTT every 6 hours', 'Verified');

    // Seed Appointments
    const insertAppt = db.prepare(`
        INSERT INTO appointments (patient_name, mrn, consulting_physician, appointment_date, time_slot, priority, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    `);

    insertAppt.run('Arthur Pendelton', 'MRN-8812', 'Dr. Elena Vance (ICU Critical Care)', '2026-10-14', '09:00 AM - 09:30 AM', 'Urgent', 'Post-ICU discharge cardiac follow-up and airway re-evaluation');
    insertAppt.run('Carmen Valenzuela', 'MRN-4491', 'Dr. Marcus Sterling (Cardiothoracic Surgery)', '2026-10-14', '10:30 AM - 11:00 AM', 'Standard', 'Pre-operative valve repair clearance');
    insertAppt.run('Benedicto Cruz', 'MRN-2108', 'Dr. Sarah Lin (Pulmonology)', '2026-10-15', '02:00 PM - 02:45 PM', 'Standard', 'Chronic asthma and spirometry assessment');

    // Seed Equipment & Operating Suite Bookings
    const insertBooking = db.prepare(`
        INSERT INTO equipment_bookings (equipment_name, reservation_start, reservation_end, requesting_ward, lead_nurse, status)
        VALUES (?, ?, ?, ?, ?, ?)
    `);

    insertBooking.run('Hamilton-C6 ICU Mobile Ventilator (#EQ-VNT-04)', '2026-10-15T08:00', '2026-10-15T12:00', 'ICU Wing B', 'Nurse Clara Reyes', 'Confirmed');
    insertBooking.run('Operating Suite #3 (Cardiac Catheterization)', '2026-10-16T07:30', '2026-10-16T14:00', 'Surgical Pavilion', 'Nurse J. De Leon', 'Confirmed');
    insertBooking.run('Philips Practix Mobile Digital X-Ray (#EQ-XRY-02)', '2026-10-15T13:00', '2026-10-15T16:30', 'Emergency Room Triage', 'Nurse Clara Reyes', 'Confirmed');

    // Seed Announcements
    const insertAnnounce = db.prepare(`
        INSERT INTO announcements (title, content, category, badge, badge_color, pinned, posted_by)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    `);

    insertAnnounce.run(
        'Mandatory Quarterly GS1 Barcode Audit (All Wards)',
        'All ICU and ER charge nurses are required to complete handheld barcode spot-audits before Friday shift change. Expiring vials (Lot #HEP-8810) have been flagged for centralized return.',
        'Pharmacy Operations',
        'Pinned • Pharmacy Operations',
        'medical',
        1,
        'Pharm. Julian Miller'
    );

    insertAnnounce.run(
        'Mediavault v4.8 Cloud Vault Synchronization Window',
        'The inventory synchronization engine will undergo a 15-minute optimization cycle this Saturday at 02:00 AM UTC. Offline barcode scanning will buffer locally without clinical interruption.',
        'System Maintenance',
        'Scheduled Maintenance',
        'amber',
        0,
        'Roberto Cruz (IT Admin)'
    );

    insertAnnounce.run(
        'DOH Dangerous Drugs Board Compliance Circular #2026-09',
        'Mandatory dual-practitioner signoff is now active for all Schedule II dispensations (Morphine, Propofol). Verifiable blockchain SHA-256 hashes are automatically generated upon deduction.',
        'Regulatory & PhilHealth',
        'Regulatory Advisory',
        'emerald',
        1,
        'Hospital Administration'
    );

    // Seed Financial Ledger (Makati LGU & Hospital Admin as per Wireframe & Section 1)
    const insertFinance = db.prepare(`
        INSERT INTO financial_ledger (billing_month, pharmaceutical_spend, surgical_spend, equipment_amortization, total_expenditure, growth_pct)
        VALUES (?, ?, ?, ?, ?, ?)
    `);

    insertFinance.run('September 2026', 82400.00, 41200.00, 19290.00, 142890.00, -3.2);
    insertFinance.run('August 2026', 85120.00, 43100.00, 19290.00, 147510.00, 6.5);
    insertFinance.run('July 2026', 79800.00, 39400.00, 19290.00, 138490.00, 1.8);
    insertFinance.run('June 2026', 81200.00, 40100.00, 19290.00, 140590.00, 0.4);

    console.log('MediVault Makati enterprise database initialization and seed complete.');
}

// Initialize on module load
initDatabase();

module.exports = {
    db,
    computeHash
};
