# Build MediVault with subtle, tasteful UI design enhancements
import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediVault | Enterprise Hospital Clinical & Supply OS</title>
    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Tailwind CSS with CDN Configuration -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        medical: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            200: '#bae6fd',
                            300: '#7dd3fc',
                            400: '#38bdf8',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            700: '#0369a1',
                            800: '#075985',
                            850: '#0c4a6e',
                            900: '#082f49',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { 
            font-family: 'Inter', sans-serif; 
            letter-spacing: -0.011em;
        }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f8fafc; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 9999px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        /* Clean, professional clinical background */
        .clinical-canvas {
            background-color: #f8fafc;
        }

        /* Refined glassmorphism header */
        .glass-header {
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }

        /* Elevated medical card */
        .med-card {
            background: #ffffff;
            border: 1px solid rgba(226, 232, 240, 0.88);
            border-radius: 1rem;
            box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.03), 0 4px 12px -2px rgba(15, 23, 42, 0.03);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .med-card:hover {
            box-shadow: 0 6px 20px -3px rgba(15, 23, 42, 0.06);
            border-color: rgba(186, 230, 253, 0.85);
        }

        /* Nav item active styling */
        .nav-item {
            transition: all 0.15s ease-in-out;
        }
        .nav-item.active {
            background-color: rgba(240, 249, 255, 0.9);
            color: #0369a1 !important;
            font-weight: 700;
            border-left: 3px solid #0284c7;
            padding-left: calc(0.75rem - 3px);
            box-shadow: 0 1px 2px 0 rgba(14, 165, 233, 0.05);
        }
        .nav-item.active i {
            color: #0284c7 !important;
        }

        /* Table micro-interactions */
        .med-table thead th {
            letter-spacing: 0.05em;
        }
        .med-table tbody tr {
            transition: background-color 0.15s ease;
        }
        .med-table tbody tr:hover {
            background-color: rgba(240, 249, 255, 0.6);
        }

        /* Input focus rings */
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #0284c7 !important;
            box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15) !important;
        }

        /* Clean status indicators */
        .sync-beacon {
            display: inline-block;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-medical-600 selection:text-white">

    <!-- Toast Notifications Container -->
    <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

    <!-- ======================================================== -->
    <!-- SCREEN 1: AUTHENTICATION & LOGIN (Wireframe Page 8)       -->
    <!-- ======================================================== -->
    <div id="screen-login" class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-950 via-medical-900 to-slate-900 p-4 relative overflow-hidden">
        <!-- Soft background aura -->
        <div class="absolute w-[500px] h-[500px] bg-cyan-500/10 rounded-full blur-3xl pointer-events-none -top-20 -left-20"></div>
        <div class="absolute w-[400px] h-[400px] bg-medical-600/10 rounded-full blur-3xl pointer-events-none -bottom-20 -right-20"></div>

        <div class="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-700/30 relative z-10">
            <!-- Left Clinical Brand Hero (Page 8 Wireframe) -->
            <div class="bg-gradient-to-br from-medical-900 via-medical-800 to-medical-900 p-8 md:p-12 text-white flex flex-col justify-between relative overflow-hidden">
                <div class="relative z-10">
                    <div class="flex items-center gap-3 mb-8">
                        <div class="w-11 h-11 rounded-2xl bg-cyan-500 text-slate-900 flex items-center justify-center font-bold text-xl shadow-lg shadow-cyan-500/20">
                            <i class="fa-solid fa-vault"></i>
                        </div>
                        <div>
                            <span class="text-2xl font-bold tracking-tight block leading-none">MediVault</span>
                            <span class="text-[10px] text-cyan-300 font-semibold uppercase tracking-wider">Clinical OS</span>
                        </div>
                    </div>
                    <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/20 text-cyan-300 border border-cyan-400/30 mb-4">
                        Enterprise Clinical & Supply OS
                    </span>
                    <h1 class="text-3xl font-bold leading-tight mb-4 tracking-tight">
                        Precision Hospital Inventory & Staff Portal
                    </h1>
                    <p class="text-slate-300 text-sm leading-relaxed mb-6 font-normal">
                        Streamlined medical stock dispensing, barcode verification, expiration intelligence, and role-segregated clinical workflows.
                    </p>
                    <div class="space-y-3.5 text-sm text-slate-300">
                        <div class="flex items-center gap-3">
                            <div class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">
                                <i class="fa-solid fa-check"></i>
                            </div>
                            <span>Real-time GS1 / Barcode Stock Tracking</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <div class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">
                                <i class="fa-solid fa-check"></i>
                            </div>
                            <span>Role-Based Access Control (RBAC)</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <div class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">
                                <i class="fa-solid fa-check"></i>
                            </div>
                            <span>Automated Expiration & Low-Stock Alerts</span>
                        </div>
                    </div>
                </div>
                <div class="pt-6 border-t border-slate-700/60 text-xs text-slate-400 flex items-center justify-between relative z-10">
                    <span>v4.8 Enterprise Build</span>
                    <span>Hospital ID: #MV-2026-HQ</span>
                </div>
            </div>

            <!-- Right Login Form Panel (Page 8 Wireframe) -->
            <div class="p-8 md:p-12 flex flex-col justify-center bg-white">
                <div id="login-primary-box">
                    <div class="mb-6">
                        <h2 class="text-2xl font-bold text-slate-900 tracking-tight">Sign in to MediVault</h2>
                        <p class="text-xs text-slate-500 mt-1">Enter your clinical or administrative credentials</p>
                    </div>

                    <form id="form-login" onsubmit="handleLogin(event)" class="space-y-4">
                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-slate-600 mb-1.5">USERNAME / STAFF ID</label>
                            <div class="relative">
                                <i class="fa-solid fa-user absolute left-3.5 top-3.5 text-slate-400 text-xs"></i>
                                <input id="login-user" type="text" required value="dr.elena.vance"
                                    class="w-full pl-9 pr-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 text-xs transition-all font-medium"
                                    placeholder="e.g. dr.elena.vance">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold uppercase tracking-wider text-slate-600 mb-1.5">PASSWORD</label>
                            <div class="relative">
                                <i class="fa-solid fa-lock absolute left-3.5 top-3.5 text-slate-400 text-xs"></i>
                                <input id="login-pass" type="password" required value="EnterpriseVault2026!"
                                    class="w-full pl-9 pr-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 text-xs transition-all font-medium"
                                    placeholder="••••••••">
                            </div>
                        </div>

                        <div class="flex items-center justify-between text-xs pt-1">
                            <label class="flex items-center gap-2 text-slate-600 cursor-pointer select-none">
                                <input type="checkbox" checked class="rounded border-slate-300 text-medical-600 focus:ring-medical-500">
                                <span class="text-xs">Remember session on terminal</span>
                            </label>
                            <a href="#" onclick="showToast('Password reset link sent to hospital email.', 'info'); return false;" class="text-medical-600 font-semibold hover:underline text-xs">Forgot password?</a>
                        </div>

                        <button id="btn-login-submit" type="submit"
                            class="w-full mt-2 bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold py-3 rounded-xl shadow-md shadow-medical-700/20 transition-all flex items-center justify-center gap-2 text-xs">
                            <span>Enter MediVault Workspace</span>
                            <i class="fa-solid fa-arrow-right text-xs"></i>
                        </button>
                    </form>

                    <!-- Quick Demo Accounts (Page 8 Wireframe) -->
                    <div class="mt-6 pt-5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                        <span class="font-medium">Quick Demo Accounts:</span>
                        <div class="flex gap-2">
                            <button type="button" onclick="fillDemoCreds('dr.elena.vance')" class="text-medical-600 font-semibold hover:underline">Doctor</button>
                            <button type="button" onclick="fillDemoCreds('pharm.j.miller')" class="text-medical-600 font-semibold hover:underline">Pharmacist</button>
                            <button type="button" onclick="fillDemoCreds('nurse.clara.reyes')" class="text-medical-600 font-semibold hover:underline">Nurse</button>
                            <button type="button" onclick="fillDemoCreds('admin.root')" class="text-medical-600 font-semibold hover:underline">Admin</button>
                            <button type="button" onclick="fillDemoCreds('finance.director')" class="text-medical-600 font-semibold hover:underline">Finance</button>
                        </div>
                    </div>
                </div>

                <!-- MFA Verification Box (Shown if role requires 2FA per Section 4 Security Architecture) -->
                <div id="login-mfa-box" class="hidden">
                    <div class="mb-5 text-center">
                        <div class="w-12 h-12 mx-auto mb-3 rounded-2xl bg-amber-50 border border-amber-200 flex items-center justify-center text-amber-600 text-xl shadow-xs">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <h2 class="text-xl font-bold text-slate-900 tracking-tight">Two-Factor Authentication</h2>
                        <p class="text-xs text-slate-500 mt-1">Administrator access requires hardware security token verification.</p>
                        <div id="mfa-user-tag" class="mt-2 inline-block px-3 py-1 bg-slate-100 text-slate-700 font-semibold text-xs rounded-full">admin.root</div>
                    </div>

                    <form onsubmit="handleMfaSubmit(event)" class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5 text-center">6-Digit Security Token</label>
                            <input id="mfa-code" type="text" maxlength="6" pattern="[0-9]{6}" required value="202601"
                                class="w-full text-center tracking-[0.5em] text-xl font-mono py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-medical-600 bg-slate-50 font-bold"
                                placeholder="000000">
                            <p class="text-[11px] text-slate-400 text-center mt-1.5">Enter token <code class="font-bold text-slate-700">202601</code> or any 6-digit code for simulation</p>
                        </div>

                        <button type="submit"
                            class="w-full bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold py-3 rounded-xl shadow-md shadow-medical-700/20 transition-all flex items-center justify-center gap-2 text-xs">
                            <span>Verify Token & Access Workspace</span>
                            <i class="fa-solid fa-check text-xs"></i>
                        </button>

                        <button type="button" onclick="cancelMfa()"
                            class="w-full text-xs text-slate-500 hover:text-slate-700 py-1 font-semibold text-center">
                            ← Return to sign in
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- ======================================================== -->
    <!-- SCREEN 2: MAIN DASHBOARD & OPERATIONAL WORKSPACE         -->
    <!-- ======================================================== -->
    <div id="screen-dashboard" class="hidden min-h-screen flex flex-col">
        <!-- Top Utility Header (Pages 9-15 Wireframe) -->
        <header class="glass-header border-b border-slate-200 sticky top-0 z-30 px-4 md:px-6 py-2.5 flex items-center justify-between shadow-xs">
            <div class="flex items-center gap-4">
                <button onclick="toggleMobileSidebar()" class="md:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100 transition-colors">
                    <i class="fa-solid fa-bars text-lg"></i>
                </button>
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-medical-700 via-sky-600 to-cyan-500 text-white flex items-center justify-center font-bold shadow-sm shadow-medical-900/10">
                        <i class="fa-solid fa-vault text-sm"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-extrabold text-slate-900 tracking-tight text-lg leading-none">MediVault</span>
                            <span class="text-[9px] font-bold uppercase tracking-wider px-1.5 py-0.5 rounded bg-sky-100/80 text-sky-800 border border-sky-200/50">v4.8</span>
                        </div>
                        <div class="text-[10px] text-slate-400 font-medium">Enterprise Clinical Platform</div>
                    </div>
                </div>
            </div>

            <!-- Quick Global Search & Action Switches -->
            <div class="flex items-center gap-3">
                <div class="hidden lg:flex items-center relative w-72">
                    <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
                    <input id="global-search-input" type="text" onkeyup="handleGlobalSearch(event)" placeholder="Search NDC, barcode, staff, or report..."
                        class="w-full pl-8 pr-4 py-1.5 rounded-xl border border-slate-200 bg-slate-50 text-xs focus:bg-white focus:outline-none focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all">
                </div>

                <button onclick="switchScreen('announcements')" class="relative p-2 rounded-xl text-slate-600 hover:bg-slate-100 transition-colors" title="Announcements">
                    <i class="fa-regular fa-bell text-sm"></i>
                    <span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500 ring-2 ring-white"></span>
                </button>

                <div class="h-6 w-px bg-slate-200"></div>

                <div class="flex items-center gap-3">
                    <div class="text-right hidden sm:block">
                        <div id="header-user-name" class="text-xs font-bold text-slate-800">dr.elena.vance</div>
                        <div id="header-user-role" class="text-[11px] text-slate-500 font-medium">Senior Medical Officer</div>
                    </div>
                    <button onclick="switchScreen('user-profile')" id="header-avatar"
                        class="w-8 h-8 rounded-full bg-gradient-to-tr from-medical-700 to-cyan-600 text-white font-bold text-xs flex items-center justify-center shadow-xs hover:scale-105 transition-transform" title="View Profile">
                        EV
                    </button>
                    <button onclick="handleLogout()" class="text-xs text-rose-600 hover:text-rose-700 font-semibold px-2.5 py-1.5 rounded-lg hover:bg-rose-50 transition-colors flex items-center gap-1">
                        <i class="fa-solid fa-right-from-bracket text-[11px]"></i>
                        <span class="hidden md:inline">Logout</span>
                    </button>
                </div>
            </div>
        </header>

        <!-- Body Layout: Sidebar + Main Content -->
        <div class="flex-1 flex overflow-hidden">
            <!-- Sidebar Navigation (Exact groups and labels from Pages 9-15) -->
            <aside id="app-sidebar" class="w-64 bg-white border-r border-slate-200 flex-shrink-0 flex flex-col justify-between hidden md:flex">
                <div class="p-3.5 space-y-5 overflow-y-auto">
                    <!-- Core Section: CLINICAL PORTAL -->
                    <div>
                        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 px-3 mb-1.5">Clinical Portal</div>
                        <nav class="space-y-0.5">
                            <button onclick="switchScreen('staff-portal')" data-nav="staff-portal"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-hospital-user w-4 text-medical-600 text-sm"></i>
                                <span>Hospital Staff Portal</span>
                            </button>
                            <button onclick="switchScreen('user-profile')" data-nav="user-profile"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-id-card w-4 text-medical-600 text-sm"></i>
                                <span>User Profile</span>
                            </button>
                            <button onclick="switchScreen('announcements')" data-nav="announcements"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-bullhorn w-4 text-medical-600 text-sm"></i>
                                <span>Announcements</span>
                                <span class="ml-auto bg-rose-100 text-rose-700 text-[10px] px-1.5 py-0.2 rounded-full font-bold">3</span>
                            </button>
                            <button onclick="switchScreen('quick-links')" data-nav="quick-links"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-bolt w-4 text-medical-600 text-sm"></i>
                                <span>Quick Links</span>
                            </button>
                        </nav>
                    </div>

                    <!-- Inventory & Core Modules: INVENTORY SYSTEM -->
                    <div>
                        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 px-3 mb-1.5">Inventory System</div>
                        <nav class="space-y-0.5">
                            <button onclick="switchScreen('inv-user-access')" data-nav="inv-user-access"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-shield-halved w-4 text-cyan-600 text-sm"></i>
                                <span>User Access Management</span>
                            </button>
                            <button onclick="switchScreen('inv-dispensing')" data-nav="inv-dispensing"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-capsules w-4 text-cyan-600 text-sm"></i>
                                <span>Dispensing & Stock Module</span>
                            </button>
                            <button onclick="switchScreen('inv-analytics')" data-nav="inv-analytics"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-chart-line w-4 text-cyan-600 text-sm"></i>
                                <span>Analytics & Reporting</span>
                            </button>
                            <button onclick="switchScreen('inventory-catalog')" data-nav="inventory-catalog"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-boxes-stacked w-4 text-cyan-600 text-sm"></i>
                                <span>Inventory Catalog</span>
                            </button>
                        </nav>
                    </div>

                    <!-- Scheduling & Admin: OPERATIONS & ADMIN -->
                    <div>
                        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 px-3 mb-1.5">Operations & Admin</div>
                        <nav class="space-y-0.5">
                            <button onclick="switchScreen('appointment-form')" data-nav="appointment-form"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-calendar-check w-4 text-indigo-600 text-sm"></i>
                                <span>Appointment Form</span>
                            </button>
                            <button onclick="switchScreen('booking-form')" data-nav="booking-form"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-bed-pulse w-4 text-indigo-600 text-sm"></i>
                                <span>Booking & Equipment Form</span>
                            </button>
                            <button onclick="switchScreen('employee-management')" data-nav="employee-management"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-users-gear w-4 text-indigo-600 text-sm"></i>
                                <span>Employee Management</span>
                            </button>
                            <button onclick="switchScreen('financial-reports')" data-nav="financial-reports"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-file-invoice-dollar w-4 text-indigo-600 text-sm"></i>
                                <span>Financial Reports</span>
                            </button>
                            <button onclick="switchScreen('inventory-reports')" data-nav="inventory-reports"
                                class="nav-item w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-all">
                                <i class="fa-solid fa-clipboard-list w-4 text-indigo-600 text-sm"></i>
                                <span>Inventory Reports</span>
                            </button>
                        </nav>
                    </div>
                </div>

            </aside>

            <!-- Main Scrollable Screen Content -->
            <main class="flex-1 clinical-canvas p-4 md:p-6 overflow-y-auto">

                <!-- ============================================== -->
                <!-- 1. VIEW: HOSPITAL STAFF PORTAL (Page 9 top)    -->
                <!-- ============================================== -->
                <section id="view-staff-portal" class="screen-view space-y-5">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Frontend Portal</span>
                            <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Hospital Staff Inventory & Requisition Portal</h2>
                            <p class="text-xs text-slate-500 mt-0.5">Scan clinical items, verify lot/expiration dates, and submit immediate ward requisitions.</p>
                        </div>
                        <button onclick="openModal('req-modal')" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white text-xs font-semibold px-4 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                            <i class="fa-solid fa-plus text-xs"></i>
                            <span>Process Ward Request</span>
                        </button>
                    </div>

                    <!-- Barcode & Item Verification (Wireframe Page 9) -->
                    <div class="med-card p-5">
                        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-medical-50 border border-medical-200 text-medical-700 flex items-center justify-center text-lg shrink-0">
                                    <i class="fa-solid fa-barcode"></i>
                                </div>
                                <div>
                                    <h3 class="text-sm font-bold text-slate-900">GS1 Barcode & Item Verification</h3>
                                    <p class="text-xs text-slate-500">Scan or select an NDC item to verify expiration, lot integrity, and stock levels.</p>
                                </div>
                            </div>

                            <div class="flex items-center gap-2.5 w-full md:w-auto">
                                <select id="scanner-preset" class="flex-1 md:w-72 px-3 py-2 rounded-xl border border-slate-300 text-xs bg-white text-slate-800 focus:outline-none focus:ring-2 focus:ring-medical-600/30">
                                    <option value="004-981-22">004-981-22 | Epinephrine 1mg/mL Auto-Inj</option>
                                    <option value="012-774-88">012-774-88 | Propofol Emulsion 20mL Vial</option>
                                    <option value="008-312-09">008-312-09 | Surgical N95 Respirators (Box 20)</option>
                                    <option value="019-442-12">019-442-12 | Heparin Sodium 5,000 U/mL</option>
                                    <option value="040-911-33">040-911-33 | Morphine Sulfate 10mg/mL</option>
                                </select>
                                <button type="button" onclick="simulateScanItem()" class="px-4 py-2 bg-slate-900 hover:bg-slate-800 active:scale-95 text-white text-xs font-semibold rounded-xl shadow-xs transition-all flex items-center gap-1.5 whitespace-nowrap">
                                    <i class="fa-solid fa-barcode text-xs"></i>
                                    <span>Scan Item</span>
                                </button>
                            </div>
                        </div>

                        <!-- Scan Feedback Display -->
                        <div id="scan-feedback-box" class="hidden mt-4 pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 border border-emerald-200 flex items-center justify-center shrink-0">
                                    <i class="fa-solid fa-check text-sm"></i>
                                </div>
                                <div>
                                    <div class="flex items-center gap-2">
                                        <span id="scan-item-title" class="font-bold text-slate-900 text-sm">--</span>
                                        <span id="scan-item-badge" class="px-2 py-0.2 rounded text-[10px] font-semibold bg-sky-50 text-sky-700 border border-sky-200">Verified</span>
                                    </div>
                                    <div class="text-slate-500 text-xs mt-0.5">
                                        <span id="scan-item-meta">NDC: --</span> • 
                                        <span id="scan-item-stock" class="font-semibold text-slate-700">Total Stock: -- units</span>
                                    </div>
                                </div>
                            </div>
                            <div id="scan-item-alternatives" class="hidden text-amber-800 bg-amber-50 px-3 py-1.5 rounded-lg text-xs border border-amber-200">
                                <i class="fa-solid fa-triangle-exclamation mr-1 text-amber-600"></i>Low Stock Suggestion Available
                            </div>
                            <button onclick="quickDeductFromScan()" class="bg-medical-700 hover:bg-medical-600 active:scale-95 text-white font-semibold py-2 px-3.5 rounded-xl text-xs transition-all flex items-center gap-1.5 self-start sm:self-auto shrink-0 shadow-xs">
                                <i class="fa-solid fa-minus text-xs"></i>
                                <span>Deduct 1 Unit</span>
                            </button>
                        </div>
                    </div>

                    <!-- Active Ward Inventory & Expiration Matrix Table (Wireframe Page 9) -->
                    <div class="med-card overflow-hidden">
                        <div class="p-4 border-b border-slate-100 bg-slate-50/70 flex items-center justify-between">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700">Active Ward Inventory & Expiration Matrix</h3>
                            <div class="flex items-center gap-2">
                                <label class="text-xs text-slate-600 font-semibold">Filter Ward:</label>
                                <select id="filter-ward-select" onchange="filterInventoryTable(this.value)" class="px-3 py-1.5 rounded-xl border border-slate-300 text-xs bg-white focus:ring-2 focus:ring-medical-600/30">
                                    <option value="ALL">All Wards / ICU</option>
                                    <option value="ICU Critical Care">ICU Critical Care</option>
                                    <option value="Operating Rooms">Operating Rooms</option>
                                    <option value="Emergency Room">Emergency Room</option>
                                    <option value="Central Pharmacy">Central Pharmacy Vault</option>
                                </select>
                            </div>
                        </div>

                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">ITEM & NDC CODE</th>
                                        <th class="py-3 px-4">CATEGORY</th>
                                        <th class="py-3 px-4">WARD</th>
                                        <th class="py-3 px-4">LOT #</th>
                                        <th class="py-3 px-4">EXPIRATION DATE</th>
                                        <th class="py-3 px-4">STOCK QTY</th>
                                        <th class="py-3 px-4">STATUS</th>
                                        <th class="py-3 px-4 text-center">ACTION</th>
                                    </tr>
                                </thead>
                                <tbody id="table-portal-inventory" class="divide-y divide-slate-100 font-medium">
                                    <tr><td colspan="8" class="py-6 text-center text-slate-400">Loading active ward inventory...</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 2. VIEW: USER PROFILE (Page 9 bottom)          -->
                <!-- ============================================== -->
                <section id="view-user-profile" class="screen-view hidden space-y-5">
                    <!-- Profile Header Banner (Page 9 Wireframe) -->
                    <div class="med-card p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="flex items-center gap-4">
                            <div id="profile-avatar-large" class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-medical-700 to-cyan-600 text-white font-extrabold text-2xl flex items-center justify-center shadow-md">
                                EV
                            </div>
                            <div>
                                <h2 id="profile-display-name" class="text-xl font-bold text-slate-900 tracking-tight">Dr. Elena Vance, MD, FACP</h2>
                                <p id="profile-display-meta" class="text-xs text-slate-500 mt-0.5">Badge ID: #MV-STF-0192 • Department: Critical Care & ICU</p>
                                <span id="profile-display-role" class="inline-block mt-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-medical-50 text-medical-700 border border-medical-200">
                                    Senior Medical Officer
                                </span>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="text-xs text-slate-400 block font-semibold uppercase tracking-wider">Medical Security Level</span>
                            <span id="profile-display-tier" class="text-sm font-bold text-slate-800">Tier 4 (Full Clinical Authorizer)</span>
                        </div>
                    </div>

                    <!-- Profile Form (Page 9 Wireframe) -->
                    <div class="med-card p-6">
                        <form onsubmit="handleProfileUpdate(event)" class="space-y-4">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1.5">Full Legal Name</label>
                                    <input id="profile-input-fullname" type="text" value="Dr. Elena Vance" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-xs focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1.5">Hospital Email Address</label>
                                    <input id="profile-input-email" type="email" value="elena.vance@medivault-health.org" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-xs focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                            </div>

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1.5">Direct Pager / Extension</label>
                                    <input id="profile-input-pager" type="text" value="Ext. 4092 (ICU Desk 3)"
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-xs focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1.5">Preferred Alert Frequency</label>
                                    <select id="profile-input-alerts" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-xs bg-white focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                        <option value="Real-Time Push & Email Digest">Real-Time Push & Email Digest</option>
                                        <option value="Daily Summary Only">Daily Summary Only</option>
                                        <option value="Critical Outages Only">Critical Outages Only</option>
                                    </select>
                                </div>
                            </div>

                            <div class="pt-2 flex justify-end">
                                <button type="submit" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold px-5 py-2.5 rounded-xl text-xs shadow-xs transition-all flex items-center gap-2">
                                    <i class="fa-solid fa-floppy-disk"></i>
                                    <span>Save Profile Preferences</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 3. VIEW: ANNOUNCEMENTS (Page 10 top)           -->
                <!-- ============================================== -->
                <section id="view-announcements" class="screen-view hidden space-y-5">
                    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                        <div>
                            <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Bulletin Board</span>
                            <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Hospital & MediVault System Announcements</h2>
                            <p class="text-xs text-slate-500 mt-0.5">Official clinical updates, supply chain maintenance windows, and policy revisions.</p>
                        </div>
                        <div id="announcement-admin-actions" class="hidden">
                            <button onclick="openAnnouncementModal()" class="bg-medical-700 hover:bg-medical-600 active:scale-95 text-white text-xs font-semibold px-4 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                                <i class="fa-solid fa-plus"></i>
                                <span>Post Announcement</span>
                            </button>
                        </div>
                    </div>

                    <div id="announcements-feed" class="space-y-3.5">
                        <!-- Populated dynamically via renderAnnouncements() -->
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 4. VIEW: QUICK LINKS (Page 10 bottom)          -->
                <!-- ============================================== -->
                <section id="view-quick-links" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Hospital Systems</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Quick Links & Clinical Launchpad</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Fast-action shortcuts to common hospital information systems and diagnostic panels.</p>
                    </div>

                    <!-- 3 Launch Cards (Wireframe Page 10) -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                        <div class="med-card p-6 hover:border-medical-500/80 cursor-pointer">
                            <div class="w-10 h-10 rounded-xl bg-cyan-50 text-cyan-600 flex items-center justify-center text-lg mb-4">
                                <i class="fa-solid fa-heart-pulse"></i>
                            </div>
                            <h3 class="font-bold text-sm text-slate-900">Electronic Health Record (EHR)</h3>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Patient vitals, medication charts, and clinical discharge summaries.</p>
                        </div>

                        <div class="med-card p-6 hover:border-medical-500/80 cursor-pointer">
                            <div class="w-10 h-10 rounded-xl bg-medical-50 text-medical-600 flex items-center justify-center text-lg mb-4">
                                <i class="fa-solid fa-flask-vial"></i>
                            </div>
                            <h3 class="font-bold text-sm text-slate-900">Lab & Radiology Results</h3>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Blood panel assay reports, CT scans, and toxicology lab queues.</p>
                        </div>

                        <div class="med-card p-6 hover:border-medical-500/80 cursor-pointer">
                            <div class="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-lg mb-4">
                                <i class="fa-solid fa-user-doctor"></i>
                            </div>
                            <h3 class="font-bold text-sm text-slate-900">On-Call Specialist Roster</h3>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Live pager links for anesthesiology, cardiology, and trauma surgeons.</p>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 5. VIEW: USER ACCESS MANAGEMENT (Page 11 top)  -->
                <!-- ============================================== -->
                <section id="view-inv-user-access" class="screen-view hidden space-y-5">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Inventory Module</span>
                            <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">User Access Management & Role-Based Permissions</h2>
                            <p class="text-xs text-slate-500 mt-0.5">Control role clearances, stock modification privileges, and sign-off compliance.</p>
                        </div>
                        <button onclick="openModal('add-access-modal')" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white text-xs font-semibold px-4 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                            <i class="fa-solid fa-user-plus text-xs"></i>
                            <span>Grant Staff Access</span>
                        </button>
                    </div>

                    <!-- 3 Stat Metrics (Wireframe Page 11) -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div class="med-card p-5 flex items-center justify-between">
                            <div>
                                <span class="text-xs font-semibold text-slate-400">Active Authorized Users</span>
                                <div id="access-stat-users" class="text-2xl font-bold text-slate-900 mt-1">142</div>
                            </div>
                            <div class="w-10 h-10 rounded-xl bg-cyan-50 text-cyan-600 flex items-center justify-center text-lg">
                                <i class="fa-solid fa-users"></i>
                            </div>
                        </div>

                        <div class="med-card p-5 flex items-center justify-between">
                            <div>
                                <span class="text-xs font-semibold text-slate-400">Restricted Schedule II Approvers</span>
                                <div id="access-stat-approvers" class="text-2xl font-bold text-slate-900 mt-1">19</div>
                            </div>
                            <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-lg">
                                <i class="fa-solid fa-key"></i>
                            </div>
                        </div>

                        <div class="med-card p-5 flex items-center justify-between">
                            <div>
                                <span class="text-xs font-semibold text-slate-400">Audit Compliance Status</span>
                                <div class="text-2xl font-bold text-emerald-600 mt-1">100% OK</div>
                            </div>
                            <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg">
                                <i class="fa-solid fa-shield-check"></i>
                            </div>
                        </div>
                    </div>

                    <!-- Staff Table (Wireframe Page 11) -->
                    <div class="med-card overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">STAFF MEMBER</th>
                                        <th class="py-3 px-4">ROLE TITLE</th>
                                        <th class="py-3 px-4">ASSIGNED DEPARTMENT</th>
                                        <th class="py-3 px-4">INVENTORY DISPENSING LEVEL</th>
                                        <th class="py-3 px-4">STATUS</th>
                                        <th class="py-3 px-4 text-center">ACCESS CONTROLS</th>
                                    </tr>
                                </thead>
                                <tbody id="table-access-staff" class="divide-y divide-slate-100 font-medium">
                                    <tr><td colspan="6" class="py-6 text-center text-slate-400">Loading staff permissions...</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 6. VIEW: DISPENSING & STOCK CONSOLE (Page 11)  -->
                <!-- ============================================== -->
                <section id="view-inv-dispensing" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Inventory Module</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Dispensing & Automated Stock Deduction Console</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Deduct medical inventory directly from vault balance with lot expiration ledger verification.</p>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                        <!-- Left: Process Live Dispensing Transaction (Wireframe Page 11) -->
                        <div class="med-card p-6">
                            <h3 class="text-sm font-bold text-slate-900 mb-4 tracking-tight">Process Live Dispensing Transaction</h3>
                            <form id="form-dispense" onsubmit="handleDispenseSubmit(event)" class="space-y-4 text-xs">
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Select Medical Supply / Medication</label>
                                    <select id="dispense-item" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 bg-white focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                        <option value="">-- Choose from Master Formulary --</option>
                                    </select>
                                </div>

                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block font-semibold text-slate-700 mb-1">Quantity to Deduct</label>
                                        <input id="dispense-qty" type="number" min="1" value="1" required
                                            class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                    </div>
                                    <div>
                                        <label class="block font-semibold text-slate-700 mb-1">Target Ward / Department</label>
                                        <input id="dispense-ward" type="text" value="ICU Critical Care" required
                                            class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                    </div>
                                </div>

                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Attending Physician / Staff Signature ID</label>
                                    <input id="dispense-authorizer" type="text" value="Dr. Elena Vance (#STF-0192)" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>

                                <button type="submit" class="w-full mt-2 bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold py-3 rounded-xl shadow-xs transition-all flex items-center justify-center gap-2">
                                    <i class="fa-solid fa-circle-check"></i>
                                    <span>Confirm Stock Dispensing & Deduct Ledger</span>
                                </button>
                            </form>
                        </div>

                        <!-- Right: Watchlist & Latest Transactions (Wireframe Page 11) -->
                        <div class="space-y-4">
                            <!-- Critical Expiration Watchlist -->
                            <div class="med-card p-5">
                                <div class="flex items-center justify-between mb-3">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700">Critical Expiration Watchlist</h3>
                                    <span class="text-[10px] font-bold text-rose-600 uppercase">Immediate Action Required</span>
                                </div>
                                <div class="space-y-2.5">
                                    <div class="p-3 rounded-xl bg-rose-50/70 border border-rose-100 flex items-center justify-between text-xs">
                                        <div>
                                            <div class="font-bold text-slate-900">Heparin Sodium 5,000 U/mL</div>
                                            <div class="text-[11px] text-slate-500">Lot: #HEP-8819 • Expires in 5 Days (2026-09-28)</div>
                                        </div>
                                        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-rose-200/80 text-rose-800">3 Left</span>
                                    </div>
                                    <div class="p-3 rounded-xl bg-amber-50/70 border border-amber-100 flex items-center justify-between text-xs">
                                        <div>
                                            <div class="font-bold text-slate-900">Propofol Emulsion 20mL Vial</div>
                                            <div class="text-[11px] text-slate-500">Lot: #PR-3912 • Expires 2026-10-30</div>
                                        </div>
                                        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-200/80 text-amber-800">6 Left (Low)</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Latest Dispensing Transactions -->
                            <div class="med-card p-5">
                                <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700 mb-3">Latest Dispensing Transactions</h3>
                                <div id="dispense-recent-list" class="space-y-2 text-xs">
                                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                                        <div>
                                            <div class="font-semibold text-slate-800">Epinephrine 1mg/mL Auto-Inj</div>
                                            <div class="text-[11px] text-slate-400 font-medium">ICU Critical Care Ward</div>
                                        </div>
                                        <span class="font-bold text-rose-600">-2 units</span>
                                    </div>
                                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                                        <div>
                                            <div class="font-semibold text-slate-800">Surgical N95 Respirators</div>
                                            <div class="text-[11px] text-slate-400 font-medium">Emergency Room Bay</div>
                                        </div>
                                        <span class="font-bold text-rose-600">-5 units</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 7. VIEW: ANALYTICS & REPORTING (Page 12 top)   -->
                <!-- ============================================== -->
                <section id="view-inv-analytics" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Inventory Module</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Analytics & Hospital Usage Intelligence</h2>
                        <p class="text-xs text-slate-500 mt-0.5">High-level financial cost breakdown, supply burn rate, and consumption charts.</p>
                    </div>

                    <!-- 4 KPI Cards (Wireframe Page 12) -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        <div class="med-card p-5">
                            <span class="text-xs font-medium text-slate-400 block">Monthly Supply Spend</span>
                            <div class="text-2xl font-bold text-slate-900 mt-1">$142,890</div>
                            <span class="text-[11px] text-emerald-600 font-medium mt-0.5 block">↓ 3.2% vs last month</span>
                        </div>
                        <div class="med-card p-5">
                            <span class="text-xs font-medium text-slate-400 block">Active Inventory SKUs</span>
                            <div class="text-2xl font-bold text-slate-900 mt-1">1,284</div>
                            <span class="text-[11px] text-medical-600 font-medium mt-0.5 block">100% Barcode Enrolled</span>
                        </div>
                        <div class="med-card p-5">
                            <span class="text-xs font-medium text-slate-400 block">Wastage / Expiry Loss</span>
                            <div class="text-2xl font-bold text-slate-900 mt-1">$1,142</div>
                            <span class="text-[11px] text-emerald-600 font-medium mt-0.5 block">&lt;1% efficiency improvement</span>
                        </div>
                        <div class="med-card p-5">
                            <span class="text-xs font-medium text-slate-400 block">Stockfill SLA Index</span>
                            <div class="text-2xl font-bold text-slate-900 mt-1">98.4%</div>
                            <span class="text-[11px] text-emerald-600 font-medium mt-0.5 block">Exceeds 95% target</span>
                        </div>
                    </div>

                    <!-- Department Consumption + Velocity Supplies (Wireframe Page 12) -->
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                        <div class="med-card p-5">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700 mb-4">Monthly Department Consumption Trend</h3>
                            <div class="space-y-4 text-xs">
                                <div>
                                    <div class="flex justify-between font-semibold mb-1">
                                        <span class="text-slate-800">ICU Critical Care</span>
                                        <span class="text-slate-500">42% ($59,990)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                                        <div class="h-full bg-sky-600 rounded-full w-[42%]"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between font-semibold mb-1">
                                        <span class="text-slate-800">Operating Rooms</span>
                                        <span class="text-slate-500">28% ($40,009)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                                        <div class="h-full bg-cyan-500 rounded-full w-[28%]"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between font-semibold mb-1">
                                        <span class="text-slate-800">Emergency Room (ER)</span>
                                        <span class="text-slate-500">21% ($30,006)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                                        <div class="h-full bg-indigo-500 rounded-full w-[21%]"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between font-semibold mb-1">
                                        <span class="text-slate-800">Pediatric & Outpatient</span>
                                        <span class="text-slate-500">9% ($12,885)</span>
                                    </div>
                                    <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                                        <div class="h-full bg-emerald-500 rounded-full w-[9%]"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="med-card p-5">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-700 mb-3">Highest Velocity Clinical Supplies</h3>
                            <div class="overflow-x-auto">
                                <table class="med-table w-full text-xs text-left">
                                    <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                        <tr>
                                            <th class="py-2.5 px-3">ITEM NAME</th>
                                            <th class="py-2.5 px-3">MONTHLY UNITS</th>
                                            <th class="py-2.5 px-3">TOTAL VALUE</th>
                                            <th class="py-2.5 px-3">TURNOVER RATE</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100 font-medium">
                                        <tr>
                                            <td class="py-2.5 px-3 font-semibold text-slate-800">Propofol Emulsion 20mL</td>
                                            <td class="py-2.5 px-3 text-slate-600">480 vials</td>
                                            <td class="py-2.5 px-3 text-slate-700">$18,400</td>
                                            <td class="py-2.5 px-3 text-medical-700 font-semibold">Fast (4.2x)</td>
                                        </tr>
                                        <tr>
                                            <td class="py-2.5 px-3 font-semibold text-slate-800">Epinephrine 1mg/mL Inj</td>
                                            <td class="py-2.5 px-3 text-slate-600">315 units</td>
                                            <td class="py-2.5 px-3 text-slate-700">$9,450</td>
                                            <td class="py-2.5 px-3 text-medical-700 font-semibold">Fast (3.8x)</td>
                                        </tr>
                                        <tr>
                                            <td class="py-2.5 px-3 font-semibold text-slate-800">Surgical N95 Respirator Pack</td>
                                            <td class="py-2.5 px-3 text-slate-600">220 boxes</td>
                                            <td class="py-2.5 px-3 text-slate-700">$14,300</td>
                                            <td class="py-2.5 px-3 text-slate-600 font-semibold">Steady (2.9x)</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 8. VIEW: INVENTORY CATALOG (Page 12 bottom)    -->
                <!-- ============================================== -->
                <section id="view-inventory-catalog" class="screen-view hidden space-y-5">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div>
                            <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Full Catalog</span>
                            <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Master Inventory Catalog & Stock Adjustment</h2>
                            <p class="text-xs text-slate-500 mt-0.5">Add new pharmaceutical items or manually adjust stock quantities.</p>
                        </div>
                        <button onclick="openModal('add-item-modal')" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white text-xs font-semibold px-4 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                            <i class="fa-solid fa-plus text-xs"></i>
                            <span>Add New Item SKU</span>
                        </button>
                    </div>

                    <!-- Catalog Table (Wireframe Page 12) -->
                    <div class="med-card overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">NDC CODE</th>
                                        <th class="py-3 px-4">ITEM NAME</th>
                                        <th class="py-3 px-4">CATEGORY</th>
                                        <th class="py-3 px-4">UNIT COST</th>
                                        <th class="py-3 px-4">TOTAL VAULT STOCK</th>
                                        <th class="py-3 px-4 text-center">STOCK ADJUSTMENT</th>
                                    </tr>
                                </thead>
                                <tbody id="table-catalog-items" class="divide-y divide-slate-100 font-medium">
                                    <tr><td colspan="6" class="py-6 text-center text-slate-400">Loading catalog items...</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 9. VIEW: APPOINTMENT FORM (Page 13 top)        -->
                <!-- ============================================== -->
                <section id="view-appointment-form" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Scheduling Portal</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Patient / Staff Clinical Appointment Form</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Schedule surgical consultations, follow-ups, or clinical peer reviews.</p>
                    </div>

                    <div class="max-w-2xl med-card p-6">
                        <form onsubmit="handleAppointmentSubmit(event)" class="space-y-4 text-xs">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Patient Full Name / MRN</label>
                                    <input id="appt-patient" type="text" placeholder="e.g. Arthur Pendelton (#MRN-4412)" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Consulting Physician</label>
                                    <input id="appt-doctor" type="text" value="Dr. Elena Vance (ICU Critical Care)" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                            </div>

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Appointment Date</label>
                                    <input id="appt-date" type="text" value="14/10/2026" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium">
                                </div>
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Time Slot</label>
                                    <select id="appt-time" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 bg-white font-medium">
                                        <option>09:00 AM - 09:30 AM</option>
                                        <option>10:30 AM - 11:00 AM</option>
                                        <option>01:00 PM - 01:30 PM</option>
                                        <option>03:30 PM - 04:00 PM</option>
                                    </select>
                                </div>
                            </div>

                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Clinical Notes / Priority</label>
                                <textarea id="appt-notes" rows="3" placeholder="Enter clinical reason for referral..."
                                    class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-medical-600/30 focus:border-medical-600 transition-all font-medium"></textarea>
                            </div>

                            <button type="submit" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold px-5 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                                <i class="fa-solid fa-calendar-check"></i>
                                <span>Confirm & Book Appointment</span>
                            </button>
                        </form>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 10. VIEW: BOOKING & EQUIPMENT FORM (Page 13)   -->
                <!-- ============================================== -->
                <section id="view-booking-form" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Resource Operations</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Medical Equipment & Operating Suite Booking Form</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Reserve mobile ICU ventilators, mobile X-ray units, or operating theatre rooms.</p>
                    </div>

                    <div class="max-w-2xl med-card p-6">
                        <form onsubmit="handleBookingSubmit(event)" class="space-y-4 text-xs">
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Select Equipment / Operating Suite</label>
                                <select id="book-equip" required class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 bg-white font-medium">
                                    <option>Hamilton-C6 ICU Mobile Ventilator (#EQ-VNT-04)</option>
                                    <option>Operating Suite B (Laparoscopic Tower)</option>
                                    <option>Portable C-Arm Fluoroscopy System</option>
                                </select>
                            </div>

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Reservation Start</label>
                                    <input id="book-start" type="text" value="15/10/2026 08:00 am" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-medium">
                                </div>
                                <div>
                                    <label class="block font-semibold text-slate-700 mb-1">Reservation End</label>
                                    <input id="book-end" type="text" value="15/10/2026 12:00 pm" required
                                        class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-medium">
                                </div>
                            </div>

                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Requesting Ward & Lead Nurse</label>
                                <input id="book-ward-lead" type="text" value="ICU Wing B • Nurse Clara Reyes" required
                                    class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-medium">
                            </div>

                            <button type="submit" class="bg-medical-700 hover:bg-medical-600 active:scale-[0.99] text-white font-semibold px-5 py-2.5 rounded-xl shadow-xs transition-all flex items-center gap-2">
                                <i class="fa-solid fa-circle-check"></i>
                                <span>Submit Equipment Booking</span>
                            </button>
                        </form>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 11. VIEW: EMPLOYEE MANAGEMENT (Page 14)        -->
                <!-- ============================================== -->
                <section id="view-employee-management" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Staff Administration</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Hospital Employee Directory & Shift Status</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Manage personnel roster, shift schedules, and department placement.</p>
                    </div>

                    <!-- Employee Directory Table (Wireframe Page 14) -->
                    <div class="med-card overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">EMPLOYEE</th>
                                        <th class="py-3 px-4">DEPARTMENT</th>
                                        <th class="py-3 px-4">SHIFT STATUS</th>
                                        <th class="py-3 px-4">ROLE DESIGNATION</th>
                                        <th class="py-3 px-4 text-center">ACTIONS</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100 font-medium">
                                    <tr>
                                        <td class="py-3 px-4">
                                            <div class="font-bold text-slate-900">Dr. Elena Vance</div>
                                            <div class="text-[10px] text-slate-400 font-mono">Badge #0192</div>
                                        </td>
                                        <td class="py-3 px-4 text-slate-700">ICU Critical Care</td>
                                        <td class="py-3 px-4">
                                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                                                On Shift (Day)
                                            </span>
                                        </td>
                                        <td class="py-3 px-4 text-slate-800 font-semibold">Senior Medical Officer</td>
                                        <td class="py-3 px-4 text-center">
                                            <button onclick="showToast('Employee profile editor opened.', 'info')" class="text-medical-600 hover:underline font-semibold">Edit</button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4">
                                            <div class="font-bold text-slate-900">Pharm. Julian Miller</div>
                                            <div class="text-[10px] text-slate-400 font-mono">Badge #0481</div>
                                        </td>
                                        <td class="py-3 px-4 text-slate-700">Central Pharmacy Vault</td>
                                        <td class="py-3 px-4">
                                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                                                On Shift (Day)
                                            </span>
                                        </td>
                                        <td class="py-3 px-4 text-slate-800 font-semibold">Lead Pharmacist</td>
                                        <td class="py-3 px-4 text-center">
                                            <button onclick="showToast('Employee profile editor opened.', 'info')" class="text-medical-600 hover:underline font-semibold">Edit</button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4">
                                            <div class="font-bold text-slate-900">Nurse Clara Reyes</div>
                                            <div class="text-[10px] text-slate-400 font-mono">Badge #0914</div>
                                        </td>
                                        <td class="py-3 px-4 text-slate-700">Emergency Room</td>
                                        <td class="py-3 px-4">
                                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-cyan-50 text-cyan-700 border border-cyan-200">
                                                On Call (Night)
                                            </span>
                                        </td>
                                        <td class="py-3 px-4 text-slate-800 font-semibold">ER Charge Nurse</td>
                                        <td class="py-3 px-4 text-center">
                                            <button onclick="showToast('Employee profile editor opened.', 'info')" class="text-medical-600 hover:underline font-semibold">Edit</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 12. VIEW: FINANCIAL REPORTS (Page 15 top)      -->
                <!-- ============================================== -->
                <section id="view-financial-reports" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Financial Ledger</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Hospital Monthly Financial Cost Breakdown</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Detailed monthly expenditure by pharmaceutical class and ward utilization.</p>
                    </div>

                    <!-- Financial Table (Wireframe Page 15) -->
                    <div class="med-card overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">BILLING MONTH</th>
                                        <th class="py-3 px-4">PHARMACEUTICAL SPEND</th>
                                        <th class="py-3 px-4">SURGICAL CONSUMABLES</th>
                                        <th class="py-3 px-4">EQUIPMENT AMORTIZATION</th>
                                        <th class="py-3 px-4">TOTAL MONTHLY EXPENDITURE</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100 font-medium">
                                    <tr>
                                        <td class="py-3 px-4 font-bold text-slate-900">September 2026</td>
                                        <td class="py-3 px-4 text-slate-700">$82,400</td>
                                        <td class="py-3 px-4 text-slate-700">$41,200</td>
                                        <td class="py-3 px-4 text-slate-700">$19,290</td>
                                        <td class="py-3 px-4 font-bold text-slate-900">$142,890</td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4 font-bold text-slate-900">August 2026</td>
                                        <td class="py-3 px-4 text-slate-700">$85,120</td>
                                        <td class="py-3 px-4 text-slate-700">$43,100</td>
                                        <td class="py-3 px-4 text-slate-700">$19,290</td>
                                        <td class="py-3 px-4 font-bold text-slate-900">$147,510</td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4 font-bold text-slate-900">July 2026</td>
                                        <td class="py-3 px-4 text-slate-700">$79,800</td>
                                        <td class="py-3 px-4 text-slate-700">$39,400</td>
                                        <td class="py-3 px-4 text-slate-700">$19,290</td>
                                        <td class="py-3 px-4 font-bold text-slate-900">$138,490</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- ============================================== -->
                <!-- 13. VIEW: INVENTORY & AUDIT LOGS (Page 15)     -->
                <!-- ============================================== -->
                <section id="view-inventory-reports" class="screen-view hidden space-y-5">
                    <div>
                        <span class="text-[11px] font-bold uppercase tracking-wider text-medical-600">Audit & Turnover</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Inventory Stock Turnover, Wastage & Audit Logs</h2>
                        <p class="text-xs text-slate-500 mt-0.5">Immutable blockchain-verifiable chain of custody audit trail.</p>
                    </div>

                    <!-- Audit Logs Table (Wireframe Page 15) -->
                    <div class="med-card overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="med-table w-full text-xs text-left">
                                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
                                    <tr>
                                        <th class="py-3 px-4">AUDIT TIMESTAMP</th>
                                        <th class="py-3 px-4">EVENT TYPE</th>
                                        <th class="py-3 px-4">ITEM / SKU</th>
                                        <th class="py-3 px-4">AUTHORIZING STAFF</th>
                                        <th class="py-3 px-4">VERIFICATION HASH</th>
                                    </tr>
                                </thead>
                                <tbody id="table-audit-logs" class="divide-y divide-slate-100 font-medium">
                                    <tr>
                                        <td class="py-3 px-4 font-mono text-slate-500 text-[11px]">2026-09-31 14:12:08</td>
                                        <td class="py-3 px-4">
                                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                                                Stock Dispensed
                                            </span>
                                        </td>
                                        <td class="py-3 px-4 font-bold text-slate-900">Epinephrine 1mg/mL Auto-Inj (-2)</td>
                                        <td class="py-3 px-4 text-slate-700">Dr. Elena Vance</td>
                                        <td class="py-3 px-4 font-mono text-[10px] text-slate-400">c9d11e...78e4</td>
                                    </tr>
                                    <tr>
                                        <td class="py-3 px-4 font-mono text-slate-500 text-[11px]">2026-09-30 11:04:22</td>
                                        <td class="py-3 px-4">
                                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-cyan-50 text-cyan-700 border border-cyan-200">
                                                GS1 Scan Verified
                                            </span>
                                        </td>
                                        <td class="py-3 px-4 font-bold text-slate-900">Propofol Emulsion 20mL Vial</td>
                                        <td class="py-3 px-4 text-slate-700">Pharm. Julian Miller</td>
                                        <td class="py-3 px-4 font-mono text-[10px] text-slate-400">0x4c2e...bc34</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    </div>

    <!-- ======================================================== -->
    <!-- MODALS SECTION                                           -->
    <!-- ======================================================== -->

    <!-- Ward Request Modal (req-modal) -->
    <div id="req-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
                <h3 class="font-bold text-slate-900 text-base">Ward Medical Stock Requisition</h3>
                <button onclick="closeModal('req-modal')" class="text-slate-400 hover:text-slate-600">
                    <i class="fa-solid fa-xmark text-base"></i>
                </button>
            </div>
            <form onsubmit="handleWardReqSubmit(event)" class="space-y-4 text-xs">
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Select Medication / Supply Item</label>
                    <select id="req-item-name" required class="w-full px-3 py-2.5 rounded-xl border border-slate-300 bg-white">
                        <option value="Epinephrine 1mg/mL Auto-Inj">Epinephrine 1mg/mL Auto-Inj</option>
                        <option value="Propofol Emulsion 20mL Vial">Propofol Emulsion 20mL Vial</option>
                        <option value="Surgical N95 Respirators (Box 20)">Surgical N95 Respirators (Box 20)</option>
                        <option value="Heparin Sodium 5,000 U/mL">Heparin Sodium 5,000 U/mL</option>
                    </select>
                </div>
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Quantity Requested</label>
                    <input id="req-quantity" type="number" min="1" value="5" required class="w-full px-3 py-2.5 rounded-xl border border-slate-300">
                </div>
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Ward Destination</label>
                    <input id="req-ward" type="text" value="ICU Critical Care Ward 4" required class="w-full px-3 py-2.5 rounded-xl border border-slate-300">
                </div>
                <div class="pt-2 flex justify-end gap-2">
                    <button type="button" onclick="closeModal('req-modal')" class="px-4 py-2 rounded-xl border border-slate-200 text-slate-600 font-semibold hover:bg-slate-50">Cancel</button>
                    <button type="submit" class="px-4 py-2 rounded-xl bg-medical-700 hover:bg-medical-600 text-white font-semibold transition-colors">Submit Requisition</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Grant Staff Access Modal (add-access-modal) -->
    <div id="add-access-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
                <h3 class="font-bold text-slate-900 text-base">Grant New Staff Access</h3>
                <button onclick="closeModal('add-access-modal')" class="text-slate-400 hover:text-slate-600">
                    <i class="fa-solid fa-xmark text-base"></i>
                </button>
            </div>
            <form onsubmit="handleAddStaffSubmit(event)" class="space-y-3.5 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Username</label>
                        <input id="staff-username" type="text" placeholder="e.g. dr.j.doe" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Full Name</label>
                        <input id="staff-fullname" type="text" placeholder="Dr. John Doe, MD" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                </div>
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Hospital Email</label>
                    <input id="staff-email" type="email" placeholder="j.doe@mediavault-health.org" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Role Type</label>
                        <select id="staff-role" class="w-full px-3 py-2 rounded-xl border border-slate-300 bg-white">
                            <option value="doctor">Doctor</option>
                            <option value="pharmacist">Pharmacist</option>
                            <option value="nurse">Nurse</option>
                            <option value="admin">Administrator</option>
                        </select>
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Department</label>
                        <input id="staff-dept" type="text" value="Emergency Department" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                </div>
                <div class="pt-2 flex justify-end gap-2">
                    <button type="button" onclick="closeModal('add-access-modal')" class="px-4 py-2 rounded-xl border border-slate-200 text-slate-600 font-semibold hover:bg-slate-50">Cancel</button>
                    <button type="submit" class="px-4 py-2 rounded-xl bg-medical-700 hover:bg-medical-600 text-white font-semibold transition-colors">Grant Access</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Add Item SKU Modal (add-item-modal) -->
    <div id="add-item-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
                <h3 class="font-bold text-slate-900 text-base">Add New Item SKU to Master Catalog</h3>
                <button onclick="closeModal('add-item-modal')" class="text-slate-400 hover:text-slate-600">
                    <i class="fa-solid fa-xmark text-base"></i>
                </button>
            </div>
            <form onsubmit="handleAddSkuSubmit(event)" class="space-y-3.5 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Item Name</label>
                        <input id="sku-name" type="text" placeholder="e.g. Cefepime 2g IV" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">NDC Code</label>
                        <input id="sku-ndc" type="text" placeholder="004-881-99" required class="w-full px-3 py-2 rounded-xl border border-slate-300 font-mono">
                    </div>
                </div>
                <div class="grid grid-cols-3 gap-3">
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Category</label>
                        <input id="sku-category" type="text" value="Emergency / Vasoactive" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Unit Cost ($)</label>
                        <input id="sku-cost" type="number" step="0.01" value="30.00" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Initial Stock</label>
                        <input id="sku-stock" type="number" min="1" value="48" required class="w-full px-3 py-2 rounded-xl border border-slate-300">
                    </div>
                </div>
                <div class="pt-2 flex justify-end gap-2">
                    <button type="button" onclick="closeModal('add-item-modal')" class="px-4 py-2 rounded-xl border border-slate-200 text-slate-600 font-semibold hover:bg-slate-50">Cancel</button>
                    <button type="submit" class="px-4 py-2 rounded-xl bg-medical-700 hover:bg-medical-600 text-white font-semibold transition-colors">Add SKU</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Announcement Add / Edit Modal (announcement-modal) -->
    <div id="announcement-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-medical-50 text-medical-600 flex items-center justify-center text-xs">
                        <i class="fa-solid fa-bullhorn"></i>
                    </div>
                    <h3 id="announcement-modal-title" class="font-bold text-slate-900 text-base">New System Announcement</h3>
                </div>
                <button onclick="closeModal('announcement-modal')" class="text-slate-400 hover:text-slate-600">
                    <i class="fa-solid fa-xmark text-base"></i>
                </button>
            </div>
            <form id="form-announcement" onsubmit="handleAnnouncementSubmit(event)" class="space-y-3.5 text-xs">
                <input type="hidden" id="announce-edit-id" value="">
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Announcement Title</label>
                    <input id="announce-title" type="text" placeholder="e.g. Mandatory Quarterly GS1 Barcode Audit" required class="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-medical-500">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Category</label>
                        <select id="announce-category" class="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-medical-500 bg-white">
                            <option value="Pharmacy Operations">Pharmacy Operations</option>
                            <option value="System Maintenance">System Maintenance</option>
                            <option value="Regulatory & PhilHealth">Regulatory & PhilHealth</option>
                            <option value="Clinical Policy">Clinical Policy</option>
                            <option value="Emergency Alert">Emergency Alert</option>
                            <option value="General Notice">General Notice</option>
                        </select>
                    </div>
                    <div>
                        <label class="block font-semibold text-slate-700 mb-1">Badge Color Tone</label>
                        <select id="announce-badge-color" class="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-medical-500 bg-white">
                            <option value="medical">Medical Blue (Primary)</option>
                            <option value="rose">Rose (Urgent/Critical)</option>
                            <option value="amber">Amber (Maintenance/Warning)</option>
                            <option value="emerald">Emerald (Regulatory/Approved)</option>
                        </select>
                    </div>
                </div>
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Content / Advisory Message</label>
                    <textarea id="announce-content" rows="4" placeholder="Detail the clinical or administrative advisory directive..." required class="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-medical-500"></textarea>
                </div>
                <div class="flex items-center gap-2 pt-1">
                    <input type="checkbox" id="announce-pinned" class="rounded border-slate-300 text-medical-600 focus:ring-medical-500">
                    <label for="announce-pinned" class="font-medium text-slate-700 cursor-pointer">Pin to top of hospital bulletin feed</label>
                </div>
                <div class="pt-2 flex justify-end gap-2 border-t border-slate-100">
                    <button type="button" onclick="closeModal('announcement-modal')" class="px-4 py-2 rounded-xl border border-slate-200 text-slate-600 font-semibold hover:bg-slate-50 transition-colors">Cancel</button>
                    <button type="submit" id="announce-submit-btn" class="px-4 py-2 rounded-xl bg-medical-700 hover:bg-medical-600 text-white font-semibold transition-colors flex items-center gap-1.5">
                        <i class="fa-solid fa-floppy-disk"></i>
                        <span>Save Announcement</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- ======================================================== -->
    <!-- DYNAMIC JAVASCRIPT APPLICATION LOGIC                     -->
    <!-- Supports both live Node.js server AND static GitHub Pages-->
    <!-- ======================================================== -->
    <script>
        // Static Seed Database (Ensures 100% functionality on static GitHub Pages deployment)
        const STATIC_USERS = {
            'dr.elena.vance': {
                id: 1, username: 'dr.elena.vance', fullName: 'Dr. Elena Vance, MD, FACP',
                email: 'elena.vance@mediavault-health.org', role: 'doctor', roleTitle: 'Senior Medical Officer',
                department: 'ICU Critical Care', badgeId: 'STF-0192', securityTier: 'Tier 4 (Full Clinical Authorizer)',
                dispensingLevel: 'Full Approval & Schedule II', mfaRequired: false, pagerExt: 'Ext. 4092 (ICU Desk 3)'
            },
            'pharm.j.miller': {
                id: 2, username: 'pharm.j.miller', fullName: 'Pharm. Julian Miller, RPh',
                email: 'julian.miller@mediavault-health.org', role: 'pharmacist', roleTitle: 'Lead Pharmacist',
                department: 'Central Pharmacy Vault', badgeId: 'STF-0481', securityTier: 'Tier 4 (Pharmacy Master)',
                dispensingLevel: 'Catalog Master Control & Procurement', mfaRequired: false, pagerExt: 'Ext. 5110 (Central Vault)'
            },
            'nurse.clara.reyes': {
                id: 3, username: 'nurse.clara.reyes', fullName: 'Nurse Clara Reyes, RN',
                email: 'clara.reyes@mediavault-health.org', role: 'nurse', roleTitle: 'ER Staff Nurse',
                department: 'Emergency Room', badgeId: 'STF-0914', securityTier: 'Tier 2 (Ward Clinical)',
                dispensingLevel: 'Ward Requisition Only', mfaRequired: false, pagerExt: 'Ext. 9112 (ER Triage)'
            },
            'admin.root': {
                id: 4, username: 'admin.root', fullName: 'Roberto Cruz (Chief Information Officer)',
                email: 'admin@mediavault-makati.gov.ph', role: 'admin', roleTitle: 'Hospital Administrator',
                department: 'IT & Administrative Services', badgeId: 'ADM-001', securityTier: 'Tier 5 (Super Administrator)',
                dispensingLevel: 'Full System Configuration & User Admin', mfaRequired: true, pagerExt: 'Ext. 1001 (HQ)'
            },
            'finance.director': {
                id: 5, username: 'finance.director', fullName: 'Sofia Ramos, CPA (Finance Director)',
                email: 'sofia.ramos@makati.gov.ph', role: 'finance', roleTitle: 'Finance Director & Makati LGU Auditor',
                department: 'Hospital Finance & Makati LGU Oversight', badgeId: 'FIN-0082', securityTier: 'Tier 4 (Financial Oversight)',
                dispensingLevel: 'Financial Audit & Analytics Only', mfaRequired: true, pagerExt: 'Ext. 2040 (Audit Hall)'
            }
        };

        const STATIC_INVENTORY = [
            { batch_id: 1, item_id: 1, item_name: 'Epinephrine 1mg/mL Auto-Inj', generic_name: 'Epinephrine', ndc_code: '004-981-22', category: 'Emergency / Vasoactive', ward: 'ICU Critical Care', lot_number: 'EP-9941', expiration_date: '2027-08-14', batch_quantity: 48, total_vault_stock: 48, min_reorder_level: 15, batch_status: 'Optimal' },
            { batch_id: 2, item_id: 2, item_name: 'Propofol Emulsion 20mL Vial', generic_name: 'Propofol', ndc_code: '012-774-88', category: 'Anesthetics', ward: 'Operating Rooms', lot_number: 'PR-3012', expiration_date: '2026-10-30', batch_quantity: 6, total_vault_stock: 6, min_reorder_level: 12, batch_status: 'Low Stock Alert' },
            { batch_id: 3, item_id: 3, item_name: 'Surgical N95 Respirators (Box 20)', generic_name: 'N95 Particulate Respirator', ndc_code: '008-312-09', category: 'PPE / Safety', ward: 'Emergency Room', lot_number: 'N95-4421', expiration_date: '2028-11-01', batch_quantity: 114, total_vault_stock: 114, min_reorder_level: 30, batch_status: 'Optimal' },
            { batch_id: 4, item_id: 4, item_name: 'Heparin Sodium 5,000 U/mL', generic_name: 'Heparin Sodium', ndc_code: '019-442-12', category: 'Anticoagulants', ward: 'ICU Critical Care', lot_number: 'HEP-8810', expiration_date: '2026-09-28', batch_quantity: 3, total_vault_stock: 3, min_reorder_level: 10, batch_status: 'Expiring Soon' },
            { batch_id: 5, item_id: 5, item_name: 'Morphine Sulfate 10mg/mL', generic_name: 'Morphine Sulfate', ndc_code: '040-911-33', category: 'Analgesics / Narcotics', ward: 'Central Pharmacy Vault', lot_number: 'MS-2026A', expiration_date: '2027-05-20', batch_quantity: 24, total_vault_stock: 24, min_reorder_level: 10, batch_status: 'Optimal' }
        ];

        const STATIC_ANNOUNCEMENTS = [
            {
                id: 1,
                title: 'Mandatory Quarterly GS1 Barcode Audit (All Wards)',
                content: 'All ICU and ER charge nurses are required to complete handheld barcode spot-audits before Friday shift change. Expiring vials (Lot #HEP-8810) have been flagged for centralized return.',
                category: 'Pharmacy Operations',
                badge: 'Pinned • Pharmacy Operations',
                badge_color: 'rose',
                pinned: 1,
                posted_by: 'Pharm. Julian Miller',
                created_at: 'Today, 07:15 AM'
            },
            {
                id: 2,
                title: 'MediVault v4.8 Cloud Vault Synchronization Window',
                content: 'The inventory synchronization engine will undergo a 15-minute optimization cycle this Saturday at 02:00 AM UTC. Offline barcode scanning will buffer locally without clinical interruption.',
                category: 'System Maintenance',
                badge: 'Scheduled Maintenance',
                badge_color: 'amber',
                pinned: 0,
                posted_by: 'Roberto Cruz (IT Admin)',
                created_at: 'Yesterday'
            },
            {
                id: 3,
                title: 'DOH Dangerous Drugs Board Compliance Circular #2026-09',
                content: 'Mandatory dual-practitioner signoff is now active for all Schedule II dispensations (Morphine, Propofol). Verifiable blockchain SHA-256 hashes are automatically generated upon deduction.',
                category: 'Regulatory & PhilHealth',
                badge: 'Regulatory Advisory',
                badge_color: 'emerald',
                pinned: 1,
                posted_by: 'Hospital Administration',
                created_at: '2 days ago'
            }
        ];

        const STATIC_CATALOG = [
            { id: 1, ndc_code: '004-981-22', item_name: 'Epinephrine 1mg/mL Auto-Inj', category: 'Emergency / Vasoactive', unit_cost: 30.00, total_vault_stock: 48, min_reorder_level: 15 },
            { id: 2, ndc_code: '012-774-88', item_name: 'Propofol Emulsion 20mL Vial', category: 'Anesthetics', unit_cost: 38.33, total_vault_stock: 6, min_reorder_level: 12 },
            { id: 3, ndc_code: '008-312-09', item_name: 'Surgical N95 Respirators (Box 20)', category: 'PPE / Safety', unit_cost: 65.00, total_vault_stock: 114, min_reorder_level: 30 },
            { id: 4, ndc_code: '019-442-12', item_name: 'Heparin Sodium 5,000 U/mL', category: 'Anticoagulants', unit_cost: 24.50, total_vault_stock: 3, min_reorder_level: 10 },
            { id: 5, ndc_code: '040-911-33', item_name: 'Morphine Sulfate 10mg/mL', category: 'Analgesics / Narcotics', unit_cost: 18.75, total_vault_stock: 24, min_reorder_level: 10 }
        ];

        const STATIC_STAFF = Object.values(STATIC_USERS);

        const STATIC_ALTERNATIVES = {
            '012-774-88': { alternative_name: 'Etomidate 20mg/10mL', dosage_info: '0.2 - 0.3 mg/kg IV (In Stock: 18 units)' },
            '019-442-12': { alternative_name: 'Enoxaparin Sodium 40mg/0.4mL', dosage_info: '40mg SC once daily (In Stock: 40 units)' }
        };

        let currentUser = null;
        let pendingMfaUser = null;
        let cachedInventory = [...STATIC_INVENTORY];
        let cachedCatalog = [...STATIC_CATALOG];
        let cachedAnnouncements = [...STATIC_ANNOUNCEMENTS];
        let lastScannedItem = null;

        // Demo Credentials Loader matching Wireframe Page 8
        function fillDemoCreds(username) {
            document.getElementById('login-user').value = username;
            document.getElementById('login-pass').value = 'EnterpriseVault2026!';
            showToast('Loaded demo credentials for ' + username, 'info');
        }

        function isBackendAvailable() {
            return (window.location.protocol === 'http:' || window.location.protocol === 'https:') && !window.location.hostname.includes('github.io');
        }

        async function quickFetch(url, options = {}, timeoutMs = 800) {
            if (!isBackendAvailable()) return null;
            try {
                const controller = new AbortController();
                const timer = setTimeout(() => controller.abort(), timeoutMs);
                const res = await fetch(url, { ...options, signal: controller.signal });
                clearTimeout(timer);
                return res;
            } catch (err) {
                return null;
            }
        }

        async function handleLogin(e) {
            e.preventDefault();
            const username = document.getElementById('login-user').value.trim();
            const password = document.getElementById('login-pass').value;
            const btn = document.getElementById('btn-login-submit');

            btn.disabled = true;
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin mr-1.5"></i> Authenticating...`;

            const fallbackUser = STATIC_USERS[username];

            // 1. Try Node backend if running on an active web server (with strict 800ms timeout)
            if (isBackendAvailable()) {
                const res = await quickFetch('/api/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                }, 800);

                if (res && res.ok) {
                    const data = await res.json();
                    if (data.requireMfa) {
                        pendingMfaUser = data.username;
                        document.getElementById('login-primary-box').classList.add('hidden');
                        document.getElementById('login-mfa-box').classList.remove('hidden');
                        document.getElementById('mfa-user-tag').textContent = `${data.username} (${data.role})`;
                        document.getElementById('mfa-code').focus();
                        showToast('MFA Hardware Challenge Required', 'info');
                        btn.disabled = false;
                        btn.innerHTML = `<span>Enter MediVault Workspace</span> <i class="fa-solid fa-arrow-right"></i>`;
                        return;
                    }
                    establishSession(data.user);
                    return;
                }
            }

            // 2. Instant static authentication (file://, GitHub Pages, or fast-fallback)
            if (fallbackUser && (password === 'EnterpriseVault2026!' || password === 'password123' || !password)) {
                if (fallbackUser.mfaRequired) {
                    pendingMfaUser = username;
                    document.getElementById('login-primary-box').classList.add('hidden');
                    document.getElementById('login-mfa-box').classList.remove('hidden');
                    document.getElementById('mfa-user-tag').textContent = `${username} (${fallbackUser.role})`;
                    document.getElementById('mfa-code').focus();
                    showToast('MFA Hardware Challenge Required', 'info');
                    btn.disabled = false;
                    btn.innerHTML = `<span>Enter MediVault Workspace</span> <i class="fa-solid fa-arrow-right"></i>`;
                    return;
                }
                establishSession(fallbackUser);
                return;
            }

            showToast('Invalid credentials entered.', 'error');
            btn.disabled = false;
            btn.innerHTML = `<span>Enter MediVault Workspace</span> <i class="fa-solid fa-arrow-right"></i>`;
        }

        async function handleMfaSubmit(e) {
            e.preventDefault();
            const code = document.getElementById('mfa-code').value.trim();

            if (isBackendAvailable()) {
                const res = await quickFetch('/api/auth/verify-mfa', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: pendingMfaUser, code })
                }, 800);

                if (res && res.ok) {
                    const data = await res.json();
                    if (data.success) {
                        showToast('MFA verification successful!', 'success');
                        establishSession(data.user);
                        return;
                    }
                }
            }

            if (code && code.length === 6 && STATIC_USERS[pendingMfaUser]) {
                showToast('MFA verification successful!', 'success');
                establishSession(STATIC_USERS[pendingMfaUser]);
                return;
            }

            showToast('Invalid 6-digit MFA token.', 'error');
        }

        function cancelMfa() {
            pendingMfaUser = null;
            document.getElementById('login-mfa-box').classList.add('hidden');
            document.getElementById('login-primary-box').classList.remove('hidden');
        }

        const SCREEN_NAMES = {
            'staff-portal': 'Hospital Staff Portal',
            'user-profile': 'User Profile',
            'announcements': 'Announcements',
            'quick-links': 'Quick Links',
            'inv-user-access': 'User Access Management',
            'inv-dispensing': 'Dispensing & Stock Module',
            'inv-analytics': 'Analytics & Reporting',
            'inventory-catalog': 'Inventory Catalog',
            'appointment-form': 'Appointment Form',
            'booking-form': 'Booking & Equipment Form',
            'employee-management': 'Employee Management',
            'financial-reports': 'Financial Reports',
            'inventory-reports': 'Inventory Reports'
        };

        const ROLE_PERMISSIONS = {
            nurse: {
                name: 'ER Staff Nurse',
                tier: 'Tier 2 (Ward Clinical)',
                clearanceTitle: 'Ward Clinical Access',
                scopeText: 'Authorized for ward requisitions, bedside scanning, patient appointments, and bed booking.',
                defaultScreen: 'staff-portal',
                allowedScreens: [
                    'staff-portal',
                    'user-profile',
                    'announcements',
                    'quick-links',
                    'appointment-form',
                    'booking-form'
                ],
                deniedReason: 'Pharmacy vault management, formulary modification, and administrative controls require Tier 4+ license.'
            },
            doctor: {
                name: 'Senior Medical Officer',
                tier: 'Tier 4 (Full Clinical Authorizer)',
                clearanceTitle: 'Clinical Authorizer Access',
                scopeText: 'Full clinical authorization for medications, Schedule II narcotics authorizer, surgical bookings, and clinical audits.',
                defaultScreen: 'staff-portal',
                allowedScreens: [
                    'staff-portal',
                    'user-profile',
                    'announcements',
                    'quick-links',
                    'inv-dispensing',
                    'inventory-catalog',
                    'appointment-form',
                    'booking-form',
                    'inventory-reports'
                ],
                deniedReason: 'IT user provisioning, HR employee files, and fiscal ledger require Administrator or Finance Director clearance.'
            },
            pharmacist: {
                name: 'Lead Pharmacist',
                tier: 'Tier 4 (Pharmacy Master)',
                clearanceTitle: 'Pharmacy Master Vault Access',
                scopeText: 'Full central pharmacy vault control, formulary catalog, dispensing, and inventory reports.',
                defaultScreen: 'inv-dispensing',
                allowedScreens: [
                    'staff-portal',
                    'user-profile',
                    'announcements',
                    'quick-links',
                    'inv-dispensing',
                    'inventory-catalog',
                    'inv-analytics',
                    'inventory-reports'
                ],
                deniedReason: 'Clinical ward appointment schedules, executive accounting, and IT user security require respective department clearance.'
            },
            finance: {
                name: 'Director of Hospital Financial Operations',
                tier: 'Tier 4 (Financial Oversight)',
                clearanceTitle: 'Financial & Audit Access',
                scopeText: 'Full oversight over medication expenditure, hospital procurement budgets, inventory valuation, and cost analytics.',
                defaultScreen: 'financial-reports',
                allowedScreens: [
                    'financial-reports',
                    'inv-analytics',
                    'inventory-reports',
                    'inventory-catalog',
                    'user-profile',
                    'announcements',
                    'quick-links'
                ],
                deniedReason: 'Bedside ward care, clinical patient triage, and medication dispensing require licensed clinical credentials.'
            },
            admin: {
                name: 'Hospital Operations Administrator',
                tier: 'Tier 5 (Super Administrator)',
                clearanceTitle: 'Super Administrator Access',
                scopeText: 'Unrestricted full access across all clinical, inventory, financial, security, and staff systems.',
                defaultScreen: 'inv-user-access',
                allowedScreens: [
                    'staff-portal',
                    'user-profile',
                    'announcements',
                    'quick-links',
                    'inv-user-access',
                    'inv-dispensing',
                    'inv-analytics',
                    'inventory-catalog',
                    'appointment-form',
                    'booking-form',
                    'employee-management',
                    'financial-reports',
                    'inventory-reports'
                ],
                deniedReason: ''
            }
        };

        function applyRolePermissions(user) {
            const role = (user && user.role) ? user.role : 'doctor';
            const perms = ROLE_PERMISSIONS[role] || ROLE_PERMISSIONS.doctor;

            // 1. Header Role Text (clean staff position title without extra labels)
            const headerRole = document.getElementById('header-user-role');
            if (headerRole) {
                headerRole.textContent = user.roleTitle || perms.name;
            }

            // 2. Announcements Admin Action Controls (Admin-only add/edit/delete)
            const announceAdminBtn = document.getElementById('announcement-admin-actions');
            if (announceAdminBtn) {
                if (role === 'admin') {
                    announceAdminBtn.classList.remove('hidden');
                } else {
                    announceAdminBtn.classList.add('hidden');
                }
            }
            renderAnnouncements(cachedAnnouncements);

            // 3. Update all sidebar nav items
            document.querySelectorAll('.nav-item').forEach(btn => {
                const screenId = btn.getAttribute('data-nav');
                if (!screenId) return;

                const isAllowed = perms.allowedScreens.includes(screenId);
                const oldLock = btn.querySelector('.nav-lock-badge');
                if (oldLock) oldLock.remove();

                if (isAllowed) {
                    btn.classList.remove('opacity-40');
                    btn.classList.add('cursor-pointer');
                    btn.removeAttribute('data-restricted');
                } else {
                    btn.classList.add('opacity-40');
                    btn.setAttribute('data-restricted', 'true');
                    const lockBadge = document.createElement('span');
                    lockBadge.className = 'nav-lock-badge ml-auto flex items-center text-[9px] text-slate-400 font-bold';
                    lockBadge.innerHTML = `<i class="fa-solid fa-lock text-[8px] mr-1"></i>`;
                    btn.appendChild(lockBadge);
                }
            });
        }

        // Cross-Tab Live Synchronization
        window.addEventListener('storage', (e) => {
            if (e.key === 'medivault_live_stock_sync' && e.newValue) {
                try {
                    const data = JSON.parse(e.newValue);
                    if (data.catalog && Array.isArray(data.catalog)) {
                        cachedCatalog = data.catalog;
                        renderCatalog(cachedCatalog);
                    }
                    if (data.inventory && Array.isArray(data.inventory)) {
                        cachedInventory = data.inventory;
                        renderPortalInventory(cachedInventory);
                        populateDispensingDropdown(cachedInventory);
                    }
                } catch (err) {}
            }
        });

        // Background Live Polling Heartbeat (Detects backend and multi-client changes)
        let liveSyncInterval = null;
        function startLiveSyncHeartbeat() {
            if (liveSyncInterval) clearInterval(liveSyncInterval);
            liveSyncInterval = setInterval(async () => {
                if (!currentUser || !isBackendAvailable()) return;
                try {
                    const res = await quickFetch('/api/inventory', {}, 600);
                    if (res && res.ok) {
                        const json = await res.json();
                        if (json.success && Array.isArray(json.data)) {
                            const curHash = cachedInventory.map(b => `${b.batch_id}:${b.batch_quantity}`).join('|');
                            const newHash = json.data.map(b => `${b.batch_id}:${b.batch_quantity}`).join('|');
                            if (curHash !== newHash) {
                                cachedInventory = json.data;
                                renderPortalInventory(cachedInventory);
                                populateDispensingDropdown(cachedInventory);
                            }
                        }
                    }
                    const catRes = await quickFetch('/api/catalog', {}, 600);
                    if (catRes && catRes.ok) {
                        const catJson = await catRes.json();
                        if (catJson.success && Array.isArray(catJson.data)) {
                            const curCatHash = cachedCatalog.map(c => `${c.id}:${c.total_vault_stock}`).join('|');
                            const newCatHash = catJson.data.map(c => `${c.id}:${c.total_vault_stock}`).join('|');
                            if (curCatHash !== newCatHash) {
                                cachedCatalog = catJson.data;
                                renderCatalog(cachedCatalog);
                            }
                        }
                    }
                } catch (e) {}
            }, 3000);
        }

        function establishSession(user) {
            currentUser = user;

            // Update Header (Pages 9-15 Wireframe)
            document.getElementById('header-user-name').textContent = user.username;

            const initials = (user.fullName || user.username).split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase();
            document.getElementById('header-avatar').textContent = initials;
            document.getElementById('profile-avatar-large').textContent = initials;

            // Update Profile Screen (Page 9 Wireframe)
            document.getElementById('profile-display-name').textContent = user.fullName;
            document.getElementById('profile-display-meta').textContent = `Badge ID: #${user.badgeId} • Department: ${user.department}`;
            document.getElementById('profile-display-role').textContent = user.roleTitle;
            document.getElementById('profile-display-tier').textContent = user.securityTier;
            document.getElementById('profile-input-fullname').value = user.fullName;
            document.getElementById('profile-input-email').value = user.email;
            document.getElementById('profile-input-pager').value = user.pagerExt || 'Ext. 4092 (ICU Desk 3)';

            // Update Dispensing default authorizer
            const dispAuth = document.getElementById('dispense-authorizer');
            if (dispAuth) dispAuth.value = `${user.fullName} (#${user.badgeId})`;

            // Apply Role-Based Access Control and adjust sidebar
            applyRolePermissions(user);

            // Transition Screen
            document.getElementById('screen-login').classList.add('hidden');
            document.getElementById('screen-dashboard').classList.remove('hidden');

            const perms = ROLE_PERMISSIONS[user.role] || ROLE_PERMISSIONS.doctor;
            switchScreen(perms.defaultScreen);

            showToast(`Signed in: ${user.fullName} (${perms.name})`, 'info');

            loadDynamicData();
            startLiveSyncHeartbeat();
        }

        function handleLogout() {
            if (liveSyncInterval) clearInterval(liveSyncInterval);
            currentUser = null;
            pendingMfaUser = null;
            document.getElementById('screen-dashboard').classList.add('hidden');
            document.getElementById('screen-login').classList.remove('hidden');
            cancelMfa();
            showToast('Session terminated safely.', 'info');
        }

        // Screen Switching with Strict RBAC Guard
        function switchScreen(screenId) {
            const role = (currentUser && currentUser.role) ? currentUser.role : 'doctor';
            const perms = ROLE_PERMISSIONS[role] || ROLE_PERMISSIONS.doctor;

            if (!perms.allowedScreens.includes(screenId)) {
                const screenTitle = SCREEN_NAMES[screenId] || screenId;
                showToast(`Access Restricted: ${perms.name} (${perms.tier}) cannot access "${screenTitle}". ${perms.deniedReason}`, 'warning');
                return;
            }

            document.querySelectorAll('.screen-view').forEach(el => el.classList.add('hidden'));
            const target = document.getElementById('view-' + screenId);
            if (target) {
                target.classList.remove('hidden');
            }

            document.querySelectorAll('.nav-item').forEach(btn => {
                if (btn.getAttribute('data-nav') === screenId) {
                    btn.classList.add('active');
                    btn.classList.remove('text-slate-600');
                } else {
                    btn.classList.remove('active');
                    btn.classList.add('text-slate-600');
                }
            });
        }

        function toggleMobileSidebar() {
            const sidebar = document.getElementById('app-sidebar');
            sidebar.classList.toggle('hidden');
            sidebar.classList.toggle('fixed');
            sidebar.classList.toggle('inset-y-0');
            sidebar.classList.toggle('left-0');
            sidebar.classList.toggle('z-40');
            sidebar.classList.toggle('shadow-2xl');
        }

        // Dynamic Data Fetching with static fallback
        async function loadDynamicData() {
            fetchInventory();
            fetchCatalog();
            fetchStaff();
            loadAuditLogs();
            fetchAnnouncements();
        }

        async function fetchInventory(wardFilter = 'ALL') {
            let url = '/api/inventory';
            if (wardFilter && wardFilter !== 'ALL') {
                url += `?ward=${encodeURIComponent(wardFilter)}`;
            }
            const res = await quickFetch(url, {}, 800);
            if (res && res.ok) {
                try {
                    const json = await res.json();
                    if (json.success) {
                        cachedInventory = json.data;
                        renderPortalInventory(cachedInventory);
                        populateDispensingDropdown(cachedInventory);
                        return;
                    }
                } catch (e) {}
            }

            let list = [...STATIC_INVENTORY];
            if (wardFilter && wardFilter !== 'ALL') {
                list = list.filter(b => b.ward.includes(wardFilter));
            }
            cachedInventory = list;
            renderPortalInventory(cachedInventory);
            populateDispensingDropdown(cachedInventory);
        }

        function renderPortalInventory(batches) {
            const tbody = document.getElementById('table-portal-inventory');
            if (!tbody) return;

            if (!batches || batches.length === 0) {
                tbody.innerHTML = `<tr><td colspan="8" class="py-6 text-center text-slate-400">No inventory batches found.</td></tr>`;
                return;
            }

            tbody.innerHTML = batches.map(b => {
                const statusDot = b.batch_status === 'Optimal' ? 'bg-emerald-500' : b.batch_status === 'Low Stock Alert' ? 'bg-amber-500' : 'bg-rose-500';
                const statusBadge = b.batch_status === 'Optimal' ? 'bg-emerald-50 text-emerald-700 border-emerald-200/80' :
                                    b.batch_status === 'Low Stock Alert' ? 'bg-amber-50 text-amber-700 border-amber-200/80' :
                                    'bg-rose-50 text-rose-700 border-rose-200/80';
                return `
                <tr class="hover:bg-sky-50/40 transition-colors">
                    <td class="py-3 px-4 font-bold text-slate-900">
                        ${b.item_name}
                        <div class="text-[10px] text-slate-400 font-normal font-mono">NDC: ${b.ndc_code}</div>
                    </td>
                    <td class="py-3 px-4 text-slate-600">${b.category}</td>
                    <td class="py-3 px-4 text-slate-700">${b.ward}</td>
                    <td class="py-3 px-4 font-mono text-[11px] text-slate-600">${b.lot_number}</td>
                    <td class="py-3 px-4 font-mono text-[11px] text-slate-500">${b.expiration_date}</td>
                    <td class="py-3 px-4 font-bold ${b.batch_quantity <= 5 ? 'text-amber-600' : 'text-slate-800'}">${b.batch_quantity}</td>
                    <td class="py-3 px-4">
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-bold border ${statusBadge}">
                            <span class="w-1.5 h-1.5 rounded-full ${statusDot}"></span>
                            <span>${b.batch_status}</span>
                        </span>
                    </td>
                    <td class="py-3 px-4 text-center">
                        <button onclick="quickDeductRow(this, ${b.batch_id}, ${b.item_id}, 1)"
                            class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-medical-700 bg-sky-50/80 hover:bg-medical-600 hover:text-white border border-sky-100 font-bold text-xs transition-all active:scale-[0.96]">
                            <i class="fa-solid fa-capsules text-[10px]"></i>
                            <span>Dispense</span>
                        </button>
                    </td>
                </tr>`;
            }).join('');
        }

        function populateDispensingDropdown(batches) {
            const select = document.getElementById('dispense-item');
            if (!select) return;

            const seen = new Set();
            const items = [];
            batches.forEach(b => {
                if (!seen.has(b.item_id)) {
                    seen.add(b.item_id);
                    items.push(b);
                }
            });

            select.innerHTML = `<option value="">-- Choose from Master Formulary --</option>` +
                items.map(i => `<option value="${i.item_id}">${i.item_name} (Lot #${i.lot_number})</option>`).join('');
        }

        function filterInventoryTable(ward) {
            fetchInventory(ward);
            showToast('Filtered ward view: ' + ward, 'info');
        }

        async function fetchCatalog() {
            const res = await quickFetch('/api/catalog', {}, 800);
            if (res && res.ok) {
                try {
                    const json = await res.json();
                    if (json.success) {
                        cachedCatalog = json.data;
                        renderCatalog(cachedCatalog);
                        return;
                    }
                } catch (e) {}
            }
            cachedCatalog = [...STATIC_CATALOG];
            renderCatalog(cachedCatalog);
        }

        function renderCatalog(items) {
            const tbody = document.getElementById('table-catalog-items');
            if (!tbody) return;

            tbody.innerHTML = items.map(item => `
                <tr class="hover:bg-sky-50/40 transition-colors">
                    <td class="py-3 px-4 font-mono text-[11px] text-slate-500">${item.ndc_code}</td>
                    <td class="py-3 px-4 font-bold text-slate-900">${item.item_name}</td>
                    <td class="py-3 px-4 text-slate-600">${item.category}</td>
                    <td class="py-3 px-4 font-semibold text-slate-800">$${item.unit_cost.toFixed(2)}</td>
                    <td class="py-3 px-4 font-bold ${item.total_vault_stock <= item.min_reorder_level ? 'text-amber-600' : 'text-slate-900'}">${item.total_vault_stock} units</td>
                    <td class="py-3 px-4 text-center">
                        <div class="inline-flex items-center gap-2">
                            <button onclick="adjustCatalogStock(${item.id}, 1)" class="w-6 h-6 rounded-md bg-slate-100 hover:bg-emerald-100 hover:text-emerald-700 active:scale-[0.95] text-slate-700 font-bold text-xs transition-colors">+1</button>
                            <button onclick="adjustCatalogStock(${item.id}, -1)" class="w-6 h-6 rounded-md bg-slate-100 hover:bg-rose-100 hover:text-rose-700 active:scale-[0.95] text-slate-700 font-bold text-xs transition-colors">-1</button>
                        </div>
                    </td>
                </tr>
            `).join('');
        }

        // ==========================================
        // UNIFIED LIVE STOCK SYNCHRONIZATION ENGINE
        // ==========================================

        function applyStockDelta(itemId, batchId, delta, options = {}) {
            itemId = Number(itemId);
            if (batchId) batchId = Number(batchId);

            // 1. Locate items in both cached lists
            let item = cachedCatalog.find(c => c.id === itemId);
            let batch = cachedInventory.find(b => (batchId && b.batch_id === batchId) || b.item_id === itemId);

            if (!item && batch) {
                item = cachedCatalog.find(c => c.id === batch.item_id);
            }

            // 2. Optimistic Mutation in Catalog (Immediate 0ms)
            if (item) {
                item.total_vault_stock = Math.max(0, (Number(item.total_vault_stock) || 0) + delta);
            }

            // 3. Optimistic Mutation in Inventory Batches (Immediate 0ms)
            if (batch) {
                batch.batch_quantity = Math.max(0, (Number(batch.batch_quantity) || 0) + delta);
                batch.total_vault_stock = item ? item.total_vault_stock : batch.batch_quantity;
                if (batch.batch_quantity <= 0) {
                    batch.batch_status = 'Depleted';
                } else if (batch.batch_quantity <= (batch.min_reorder_level || 5)) {
                    batch.batch_status = 'Low Stock Alert';
                } else {
                    batch.batch_status = 'Optimal';
                }
            } else if (item) {
                // Adjust matching batch by item_id if batchId wasn't specific
                const matchingBatches = cachedInventory.filter(b => b.item_id === item.id);
                if (matchingBatches.length > 0) {
                    matchingBatches[0].batch_quantity = Math.max(0, (Number(matchingBatches[0].batch_quantity) || 0) + delta);
                    matchingBatches[0].total_vault_stock = item.total_vault_stock;
                    if (matchingBatches[0].batch_quantity <= 0) matchingBatches[0].batch_status = 'Depleted';
                    else if (matchingBatches[0].batch_quantity <= (matchingBatches[0].min_reorder_level || 5)) matchingBatches[0].batch_status = 'Low Stock Alert';
                    else matchingBatches[0].batch_status = 'Optimal';
                }
            }

            // 4. Update Optical Barcode Scanner View live if current item is scanned
            if (lastScannedItem && (lastScannedItem.id === itemId || lastScannedItem.item_id === itemId || (batch && lastScannedItem.batch_id === batch.batch_id))) {
                const updatedQty = batch ? batch.batch_quantity : (item ? item.total_vault_stock : 0);
                lastScannedItem.batch_quantity = updatedQty;
                lastScannedItem.total_vault_stock = item ? item.total_vault_stock : updatedQty;
                const stockEl = document.getElementById('scan-item-stock');
                if (stockEl) {
                    stockEl.textContent = `Total Vault Stock: ${updatedQty} units (${lastScannedItem.ward || 'ICU Critical Care'})`;
                }
                const altBox = document.getElementById('scan-item-alternatives');
                if (altBox) {
                    if (updatedQty <= (lastScannedItem.min_reorder_level || 5)) {
                        altBox.classList.remove('hidden');
                    } else {
                        altBox.classList.add('hidden');
                    }
                }
            }

            // 5. Instant Synchronous UI Re-render across all views
            renderPortalInventory(cachedInventory);
            renderCatalog(cachedCatalog);
            populateDispensingDropdown(cachedInventory);

            // 6. Multi-tab synchronization broadcast
            try {
                localStorage.setItem('medivault_live_stock_sync', JSON.stringify({
                    timestamp: Date.now(),
                    itemId,
                    batchId,
                    delta,
                    catalog: cachedCatalog,
                    inventory: cachedInventory
                }));
            } catch (err) {}

            return { item, batch };
        }

        async function adjustCatalogStock(itemId, delta) {
            if (currentUser && !['admin', 'pharmacist'].includes(currentUser.role)) {
                showToast('Action Denied: Master catalog stock adjustments require Licensed Pharmacist clearance.', 'warning');
                return;
            }

            // 1. Instant optimistic update (0ms UI latency)
            const { item } = applyStockDelta(itemId, null, delta);
            const itemName = item ? item.item_name : `Item #${itemId}`;
            showToast(`${itemName} stock ${delta > 0 ? '+'+delta : delta} (Balance: ${item ? item.total_vault_stock : ''} units)`, 'info');

            // 2. Background server synchronization
            if (isBackendAvailable()) {
                try {
                    const res = await quickFetch('/api/inventory/adjust', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ itemId, delta })
                    }, 1000);
                    if (res && res.ok) {
                        const data = await res.json();
                        if (data.newStock !== undefined && item && item.total_vault_stock !== data.newStock) {
                            item.total_vault_stock = data.newStock;
                            renderCatalog(cachedCatalog);
                        }
                    }
                } catch (e) {}
            }
        }

        async function fetchStaff() {
            const res = await quickFetch('/api/staff', {}, 800);
            if (res && res.ok) {
                try {
                    const json = await res.json();
                    if (json.success) {
                        renderStaff(json.data);
                        return;
                    }
                } catch (e) {}
            }
            renderStaff(STATIC_STAFF);
        }

        function renderStaff(staffList) {
            const tbody = document.getElementById('table-access-staff');
            if (!tbody) return;

            tbody.innerHTML = staffList.map(s => `
                <tr class="hover:bg-sky-50/40 transition-colors">
                    <td class="py-3 px-4 font-bold text-slate-900">
                        ${s.full_name || s.fullName}
                        <div class="text-[10px] text-slate-400 font-normal font-mono">(ID: #${s.badge_id || s.badgeId})</div>
                    </td>
                    <td class="py-3 px-4 text-slate-700">${s.role_title || s.roleTitle}</td>
                    <td class="py-3 px-4 text-slate-600">${s.department}</td>
                    <td class="py-3 px-4 font-semibold text-medical-800">${s.dispensing_level || s.dispensingLevel}</td>
                    <td class="py-3 px-4">
                        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                            ${s.status || 'Active'}
                        </span>
                    </td>
                    <td class="py-3 px-4 text-center">
                        <button onclick="toggleRoleBadge(this)" class="text-medical-600 hover:underline font-semibold">
                            Edit Permissions
                        </button>
                    </td>
                </tr>
            `).join('');
        }

        async function loadAuditLogs() {
            const res = await quickFetch('/api/audit-logs', {}, 800);
            if (res && res.ok) {
                try {
                    const json = await res.json();
                    if (json.success) {
                        const tbody = document.getElementById('table-audit-logs');
                        if (!tbody) return;

                        tbody.innerHTML = json.data.slice(0, 10).map(l => `
                            <tr class="hover:bg-sky-50/40 transition-colors">
                                <td class="py-3 px-4 font-mono text-[11px] text-slate-500">${l.timestamp}</td>
                                <td class="py-3 px-4">
                                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold ${l.is_controlled_substance ? 'bg-rose-50 text-rose-700 border border-rose-200' : 'bg-emerald-50 text-emerald-700 border border-emerald-200'}">
                                        ${l.event_type}
                                    </span>
                                </td>
                                <td class="py-3 px-4 font-bold text-slate-900">${l.item_name}</td>
                                <td class="py-3 px-4 text-slate-700">${l.authorizing_staff}</td>
                                <td class="py-3 px-4 font-mono text-[10px] text-slate-400">${(l.verification_hash || 'c9d11e...78e4').slice(0, 12)}...</td>
                            </tr>
                        `).join('');
                    }
                } catch (e) {}
            }
        }

        // Optical Barcode Scanner Simulator (Wireframe Page 9)
        async function simulateScanItem() {
            const code = document.getElementById('scanner-preset').value;
            try {
                const res = await fetch('/api/inventory/scan', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ code })
                });

                if (res.ok) {
                    const data = await res.json();
                    if (data.success) {
                        lastScannedItem = data.item;
                        renderScanResult(data.item, data.isLowStock, data.alternatives);
                        showToast('Barcode scanned: ' + data.item.item_name, 'info');
                        return;
                    }
                }
            } catch (err) {}

            // Static fallback
            const item = cachedInventory.find(b => b.ndc_code === code) || cachedInventory[0];
            lastScannedItem = item;
            const isLowStock = item.batch_quantity <= item.min_reorder_level;
            const alts = STATIC_ALTERNATIVES[item.ndc_code] ? [STATIC_ALTERNATIVES[item.ndc_code]] : [];
            renderScanResult(item, isLowStock, alts);
            showToast('Barcode scanned: ' + item.item_name, 'info');
        }

        function renderScanResult(item, isLowStock, alternatives) {
            const box = document.getElementById('scan-feedback-box');
            box.classList.remove('hidden');

            document.getElementById('scan-item-title').textContent = 'Scanned: ' + item.item_name;
            document.getElementById('scan-item-meta').textContent = `NDC: ${item.ndc_code} • Verified Authenticated GS1 Vial • Lot: ${item.lot_number || 'EP-9941'}`;
            document.getElementById('scan-item-stock').textContent = `Total Vault Stock: ${item.batch_quantity || item.total_vault_stock} units (${item.ward || 'ICU Critical Care'})`;

            const altBox = document.getElementById('scan-item-alternatives');
            if (isLowStock) {
                altBox.classList.remove('hidden');
                if (alternatives && alternatives.length > 0) {
                    const alt = alternatives[0];
                    altBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation mr-1.5 text-amber-600"></i>Low Stock Suggestion: Suggested alternative <strong>${alt.alternative_name}</strong> (${alt.dosage_info}) is available.`;
                }
            } else {
                altBox.classList.add('hidden');
            }
        }

        async function quickDeductFromScan() {
            if (!lastScannedItem) {
                showToast('Please scan an item first.', 'error');
                return;
            }
            await quickDeductRow(null, lastScannedItem.batch_id, lastScannedItem.item_id || lastScannedItem.id, 1);
        }

        async function quickDeductRow(btn, batchId, itemId, count) {
            if (currentUser && currentUser.role === 'finance') {
                showToast('Action Denied: Financial personnel do not hold clinical dispensing clearance.', 'warning');
                return;
            }

            // 1. Instant optimistic update (0ms UI latency)
            const { item, batch } = applyStockDelta(itemId, batchId, -count);
            const itemName = (batch && batch.item_name) || (item && item.item_name) || 'Medication';
            const remaining = batch ? batch.batch_quantity : (item ? item.total_vault_stock : 0);
            showToast(`Dispensed ${count} unit of ${itemName} (Remaining: ${remaining} units)`, 'success');

            // 2. Background server synchronization
            if (isBackendAvailable()) {
                try {
                    await quickFetch('/api/inventory/dispense', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            itemId,
                            batchId,
                            quantity: count,
                            ward: batch ? batch.ward : 'ICU Critical Care',
                            authorizingStaff: currentUser ? currentUser.fullName : 'Dr. Elena Vance',
                            authorizingBadge: currentUser ? currentUser.badgeId : 'STF-0192'
                        })
                    }, 1000);
                    loadAuditLogs();
                } catch (e) {}
            }
        }

        // Form Submit Handlers
        async function handleDispenseSubmit(e) {
            e.preventDefault();
            if (currentUser && !['doctor', 'pharmacist', 'admin'].includes(currentUser.role)) {
                showToast('Action Denied: Direct Schedule II dispensation requires Attending Physician or Licensed Pharmacist sign-off.', 'warning');
                return;
            }
            const itemId = parseInt(document.getElementById('dispense-item').value, 10);
            const quantity = parseInt(document.getElementById('dispense-qty').value, 10) || 1;
            const ward = document.getElementById('dispense-ward').value;

            if (!itemId) {
                showToast('Please choose a medication item.', 'error');
                return;
            }

            // 1. Instant optimistic update (0ms UI latency)
            const { item } = applyStockDelta(itemId, null, -quantity);
            const itemName = item ? item.item_name : 'Medication';
            closeModal('dispense-modal');
            showToast(`Dispensed ${quantity} unit(s) of ${itemName} to ${ward}.`, 'success');

            // 2. Background server synchronization
            if (isBackendAvailable()) {
                try {
                    await quickFetch('/api/inventory/dispense', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            itemId,
                            quantity,
                            ward,
                            authorizingStaff: currentUser ? currentUser.fullName : 'Dr. Elena Vance'
                        })
                    }, 1000);
                    loadAuditLogs();
                } catch (e) {}
            }
        }

        async function handleWardReqSubmit(e) {
            e.preventDefault();
            const itemName = document.getElementById('req-item-name').value;
            const quantity = document.getElementById('req-quantity').value;
            const ward = document.getElementById('req-ward').value;

            try {
                await fetch('/api/requisitions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        itemName,
                        quantity,
                        ward,
                        requestedBy: currentUser ? currentUser.fullName : 'Ward Charge Nurse'
                    })
                });
            } catch (err) {}

            closeModal('req-modal');
            showToast('Ward requisition submitted to Lead Pharmacist.', 'info');
        }

        async function handleAddStaffSubmit(e) {
            e.preventDefault();
            const username = document.getElementById('staff-username').value.trim();
            const fullName = document.getElementById('staff-fullname').value.trim();
            const email = document.getElementById('staff-email').value.trim();
            const role = document.getElementById('staff-role').value;
            const department = document.getElementById('staff-dept').value.trim();

            try {
                await fetch('/api/staff', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, fullName, email, role, department })
                });
            } catch (err) {}

            closeModal('add-access-modal');
            showToast('Staff access granted successfully.', 'info');
            fetchStaff();
        }

        async function handleAddSkuSubmit(e) {
            e.preventDefault();
            const itemName = document.getElementById('sku-name').value.trim();
            const ndcCode = document.getElementById('sku-ndc').value.trim();
            const category = document.getElementById('sku-category').value.trim();
            const unitCost = parseFloat(document.getElementById('sku-cost').value);
            const initialStock = parseInt(document.getElementById('sku-stock').value, 10);

            try {
                await fetch('/api/inventory/items', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ itemName, ndcCode, category, unitCost, initialStock })
                });
            } catch (err) {}

            const newId = cachedCatalog.length + 1;
            cachedCatalog.push({
                id: newId,
                ndc_code: ndcCode,
                item_name: itemName,
                category: category,
                unit_cost: unitCost,
                total_vault_stock: initialStock,
                min_reorder_level: 15
            });
            cachedInventory.push({
                batch_id: cachedInventory.length + 1,
                item_id: newId,
                item_name: itemName,
                generic_name: itemName,
                ndc_code: ndcCode,
                category: category,
                ward: 'Central Pharmacy Vault',
                lot_number: 'LOT-' + Math.floor(1000 + Math.random() * 9000),
                expiration_date: '2028-12-31',
                batch_quantity: initialStock,
                total_vault_stock: initialStock,
                min_reorder_level: 15,
                batch_status: 'Optimal'
            });
            renderCatalog(cachedCatalog);
            renderPortalInventory(cachedInventory);
            populateDispensingDropdown(cachedInventory);

            closeModal('add-item-modal');
            showToast('Successfully enrolled new SKU: ' + itemName, 'info');
        }

        async function handleProfileUpdate(e) {
            e.preventDefault();
            if (!currentUser) {
                showToast('User profile preferences saved successfully.', 'info');
                return;
            }
            const fullName = document.getElementById('profile-input-fullname').value.trim();
            const email = document.getElementById('profile-input-email').value.trim();
            const pagerExt = document.getElementById('profile-input-pager').value.trim();
            const alertPref = document.getElementById('profile-input-alerts').value;

            try {
                await fetch('/api/auth/profile', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        username: currentUser.username,
                        fullName,
                        email,
                        pagerExt,
                        alertPref
                    })
                });
            } catch (err) {}

            currentUser.fullName = fullName;
            currentUser.email = email;
            document.getElementById('profile-display-name').textContent = fullName;
            showToast('User profile preferences saved successfully.', 'info');
        }

        async function handleAppointmentSubmit(e) {
            e.preventDefault();
            const patientName = document.getElementById('appt-patient').value.trim();
            const consultingPhysician = document.getElementById('appt-doctor').value.trim();
            const appointmentDate = document.getElementById('appt-date').value;
            const timeSlot = document.getElementById('appt-time').value;
            const notes = document.getElementById('appt-notes').value.trim();

            try {
                await fetch('/api/appointments', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        patientName,
                        mrn: patientName.includes('#') ? patientName.split('#')[1].replace(')', '') : 'MRN-4412',
                        consultingPhysician,
                        appointmentDate,
                        timeSlot,
                        priority: 'Standard',
                        notes
                    })
                });
            } catch (err) {}
            showToast('Patient clinical appointment scheduled.', 'info');
        }

        async function handleBookingSubmit(e) {
            e.preventDefault();
            const equipmentName = document.getElementById('book-equip').value;
            const reservationStart = document.getElementById('book-start').value;
            const reservationEnd = document.getElementById('book-end').value;
            const wardLead = document.getElementById('book-ward-lead').value;
            const parts = wardLead.split('•').map(s => s.trim());

            try {
                await fetch('/api/bookings', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        equipmentName,
                        reservationStart,
                        reservationEnd,
                        requestingWard: parts[0] || 'ICU Wing B',
                        leadNurse: parts[1] || 'Nurse Clara Reyes'
                    })
                });
            } catch (err) {}
            showToast('Equipment reservation confirmed.', 'info');
        }

        function toggleRoleBadge(btn) {
            showToast('Role permissions window updated.', 'info');
        }

        // ==========================================
        // ANNOUNCEMENTS CRUD ENGINE (Admin Authorized)
        // ==========================================
        async function fetchAnnouncements() {
            const res = await quickFetch('/api/announcements', {}, 800);
            if (res && res.ok) {
                try {
                    const json = await res.json();
                    if (json.success && Array.isArray(json.data)) {
                        cachedAnnouncements = json.data;
                        renderAnnouncements(cachedAnnouncements);
                        return;
                    }
                } catch (e) {}
            }
            renderAnnouncements(cachedAnnouncements);
        }

        function renderAnnouncements(items) {
            const feed = document.getElementById('announcements-feed');
            if (!feed) return;

            if (!items || items.length === 0) {
                feed.innerHTML = `
                    <div class="med-card p-8 text-center text-slate-400">
                        <i class="fa-solid fa-bullhorn text-2xl mb-2 opacity-50"></i>
                        <p class="text-xs font-medium">No announcements published at this time.</p>
                    </div>
                `;
                return;
            }

            const isAdmin = currentUser && currentUser.role === 'admin';

            // Badge color helper
            const colorClasses = {
                rose: { border: 'border-rose-200/90', badgeBg: 'bg-rose-50 text-rose-700 border-rose-200' },
                amber: { border: 'border-amber-200/90', badgeBg: 'bg-amber-50 text-amber-700 border-amber-200' },
                emerald: { border: 'border-emerald-200/90', badgeBg: 'bg-emerald-50 text-emerald-700 border-emerald-200' },
                medical: { border: 'border-medical-200/90', badgeBg: 'bg-medical-50 text-medical-700 border-medical-200' }
            };

            feed.innerHTML = items.map(a => {
                const colorTone = colorClasses[a.badge_color || a.badgeColor] || colorClasses.medical;
                const isPinned = a.pinned == 1 || a.pinned === true;
                const badgeLabel = a.badge || (isPinned ? `Pinned • ${a.category}` : a.category);
                const safeDate = a.created_at || 'Just now';
                const safeAuthor = a.posted_by || a.postedBy || 'Administration';

                return `
                    <div class="med-card ${colorTone.border} p-5 transition-all relative group" id="announce-card-${a.id}">
                        <div class="flex items-start justify-between gap-3 mb-2">
                            <div class="flex items-center gap-2 flex-wrap">
                                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold ${colorTone.badgeBg} border">
                                    ${isPinned ? '<i class="fa-solid fa-thumbtack text-[9px] mr-1"></i>' : ''}${badgeLabel}
                                </span>
                                <span class="text-[11px] text-slate-400 font-normal">
                                    By <span class="font-medium text-slate-600">${safeAuthor}</span> • ${safeDate}
                                </span>
                            </div>

                            ${isAdmin ? `
                                <div class="flex items-center gap-1.5 opacity-90 group-hover:opacity-100 transition-opacity">
                                    <button onclick="editAnnouncementModal(${a.id})" class="px-2 py-1 rounded-lg border border-slate-200 text-slate-600 hover:text-medical-700 hover:border-medical-300 hover:bg-medical-50/50 text-[11px] font-semibold transition-colors flex items-center gap-1" title="Edit Announcement">
                                        <i class="fa-solid fa-pen text-[10px]"></i>
                                        <span>Edit</span>
                                    </button>
                                    <button onclick="deleteAnnouncement(${a.id})" class="px-2 py-1 rounded-lg border border-rose-200 text-rose-600 hover:text-white hover:bg-rose-600 text-[11px] font-semibold transition-colors flex items-center gap-1" title="Delete Announcement">
                                        <i class="fa-solid fa-trash-can text-[10px]"></i>
                                        <span>Delete</span>
                                    </button>
                                </div>
                            ` : ''}
                        </div>
                        <h3 class="font-bold text-slate-900 text-sm mb-1">${a.title}</h3>
                        <p class="text-xs text-slate-600 leading-relaxed font-normal whitespace-pre-line">${a.content}</p>
                    </div>
                `;
            }).join('');
        }

        function openAnnouncementModal(editId = null) {
            if (!currentUser || currentUser.role !== 'admin') {
                showToast('Action Denied: Publishing or editing announcements requires Administrator privileges.', 'error');
                return;
            }

            const modalTitle = document.getElementById('announcement-modal-title');
            const editIdInput = document.getElementById('announce-edit-id');
            const titleInput = document.getElementById('announce-title');
            const categorySelect = document.getElementById('announce-category');
            const badgeColorSelect = document.getElementById('announce-badge-color');
            const contentTextarea = document.getElementById('announce-content');
            const pinnedCheckbox = document.getElementById('announce-pinned');
            const submitBtnText = document.querySelector('#announce-submit-btn span');

            if (editId) {
                const item = cachedAnnouncements.find(a => String(a.id) === String(editId));
                if (!item) return;

                modalTitle.textContent = 'Edit System Announcement';
                editIdInput.value = item.id;
                titleInput.value = item.title;
                categorySelect.value = item.category || 'General Notice';
                badgeColorSelect.value = item.badge_color || item.badgeColor || 'medical';
                contentTextarea.value = item.content;
                pinnedCheckbox.checked = item.pinned == 1 || item.pinned === true;
                if (submitBtnText) submitBtnText.textContent = 'Save Changes';
            } else {
                modalTitle.textContent = 'New System Announcement';
                editIdInput.value = '';
                document.getElementById('form-announcement').reset();
                if (submitBtnText) submitBtnText.textContent = 'Broadcast Announcement';
            }

            const modal = document.getElementById('announcement-modal');
            if (modal) modal.classList.remove('hidden');
        }

        function editAnnouncementModal(id) {
            openAnnouncementModal(id);
        }

        async function handleAnnouncementSubmit(e) {
            e.preventDefault();
            if (!currentUser || currentUser.role !== 'admin') {
                showToast('Unauthorized: Administrator authorization required.', 'error');
                return;
            }

            const editId = document.getElementById('announce-edit-id').value;
            const title = document.getElementById('announce-title').value.trim();
            const category = document.getElementById('announce-category').value;
            const badgeColor = document.getElementById('announce-badge-color').value;
            const content = document.getElementById('announce-content').value.trim();
            const pinned = document.getElementById('announce-pinned').checked ? 1 : 0;
            const postedBy = currentUser.fullName || 'Hospital Administration';
            const badge = pinned ? `Pinned • ${category}` : category;

            const payload = {
                title,
                category,
                badgeColor,
                badge,
                content,
                pinned,
                postedBy
            };

            if (editId) {
                // UPDATE (PUT)
                const targetId = parseInt(editId, 10) || editId;
                const idx = cachedAnnouncements.findIndex(a => String(a.id) === String(targetId));
                if (idx !== -1) {
                    cachedAnnouncements[idx] = {
                        ...cachedAnnouncements[idx],
                        ...payload,
                        badge_color: badgeColor,
                        posted_by: postedBy
                    };
                }

                closeModal('announcement-modal');
                renderAnnouncements(cachedAnnouncements);

                try {
                    await quickFetch(`/api/announcements/${targetId}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                } catch (err) {}

                showToast('Announcement updated successfully.', 'success');
            } else {
                // CREATE (POST)
                const newId = Date.now();
                const newRecord = {
                    id: newId,
                    ...payload,
                    badge_color: badgeColor,
                    posted_by: postedBy,
                    created_at: 'Today, Just now'
                };

                if (pinned) {
                    cachedAnnouncements.unshift(newRecord);
                } else {
                    cachedAnnouncements.push(newRecord);
                }

                closeModal('announcement-modal');
                renderAnnouncements(cachedAnnouncements);

                try {
                    const res = await quickFetch('/api/announcements', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    if (res && res.ok) {
                        const json = await res.json();
                        if (json.id) {
                            newRecord.id = json.id;
                        }
                    }
                } catch (err) {}

                showToast('Announcement broadcasted to bulletin board.', 'success');
            }
        }

        async function deleteAnnouncement(id) {
            if (!currentUser || currentUser.role !== 'admin') {
                showToast('Action Denied: Only Hospital Administrators can delete announcements.', 'error');
                return;
            }

            const item = cachedAnnouncements.find(a => String(a.id) === String(id));
            const confirmTitle = item ? `"${item.title.slice(0, 35)}..."` : 'this announcement';

            if (!confirm(`Are you sure you want to delete ${confirmTitle}? This action cannot be undone.`)) {
                return;
            }

            // Optimistic update
            cachedAnnouncements = cachedAnnouncements.filter(a => String(a.id) !== String(id));
            renderAnnouncements(cachedAnnouncements);

            try {
                await quickFetch(`/api/announcements/${id}`, {
                    method: 'DELETE'
                });
            } catch (err) {}

            showToast('Announcement removed from bulletin board.', 'info');
        }

        function handleGlobalSearch(e) {
            const q = e.target.value.toLowerCase().trim();
            if (!q) {
                renderPortalInventory(cachedInventory);
                renderCatalog(cachedCatalog);
                return;
            }
            renderPortalInventory(cachedInventory.filter(b =>
                b.item_name.toLowerCase().includes(q) ||
                b.ndc_code.toLowerCase().includes(q) ||
                b.lot_number.toLowerCase().includes(q)
            ));
            renderCatalog(cachedCatalog.filter(c =>
                c.item_name.toLowerCase().includes(q) ||
                c.ndc_code.toLowerCase().includes(q)
            ));
        }

        // Modals & Toasts
        function openModal(id) {
            if (id === 'add-access-modal' && currentUser && currentUser.role !== 'admin') {
                showToast('Action Denied: Granting staff credentials requires Super Administrator (Tier 5) privileges.', 'error');
                return;
            }
            if (id === 'add-employee-modal' && currentUser && currentUser.role !== 'admin') {
                showToast('Action Denied: Registering staff records requires Administrator privileges.', 'error');
                return;
            }
            if (id === 'add-sku-modal' && currentUser && !['admin', 'pharmacist'].includes(currentUser.role)) {
                showToast('Action Denied: Creating formulary items requires Central Pharmacy Vault authorization.', 'error');
                return;
            }
            const el = document.getElementById(id);
            if (el) el.classList.remove('hidden');
        }

        function closeModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        }

        function showToast(message, type = 'info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'pointer-events-auto bg-slate-900/95 backdrop-blur-md text-white text-xs px-4 py-3 rounded-2xl shadow-xl flex items-center gap-3 border border-slate-700/80 transition-all';
            
            let iconHtml = '<i class="fa-solid fa-circle-info text-cyan-400"></i>';
            if (type === 'error') {
                iconHtml = '<i class="fa-solid fa-triangle-exclamation text-rose-400"></i>';
            } else if (type === 'warning') {
                iconHtml = '<i class="fa-solid fa-shield-halved text-amber-400"></i>';
            } else if (type === 'success') {
                iconHtml = '<i class="fa-solid fa-circle-check text-emerald-400"></i>';
            }

            toast.innerHTML = `
                ${iconHtml}
                <span class="font-medium">${message}</span>
            `;
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 300);
            }, 3500);
        }
    </script>
</body>
</html>
'''

# 1. Write to public/index.html (for local Node.js server)
pub_path = os.path.join(os.path.dirname(__file__), 'public', 'index.html')
os.makedirs(os.path.dirname(pub_path), exist_ok=True)
with open(pub_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

# 2. Write to repository root ./index.html (for GitHub Pages deployment)
root_path = os.path.join(os.path.dirname(__file__), 'index.html')
with open(root_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Generated BOTH public/index.html and root index.html with refined UI styling ({len(HTML_CONTENT)} characters)")
