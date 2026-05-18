"""Build a sample .xlsx demonstrating the Tax Workbook KISS+Views architecture.

Output: docs/Tax_Workbook_Sample_Template.xlsx

Scope:
- Demonstrates the schemas, closed-set dropdowns, reference data, and
  formula patterns from the architecture notes.
- NOT included (require VBA / Phase 2 install in the real workbook):
  - The 7 KISS LAMBDAs (Calc_OrdinaryTax, Calc_QBI_Simple, etc.)
  - Workbook_BeforeSave auto-sync handler
  - The 7 modKissSync macros
  - Get_TreatmentDefault LAMBDA (placeholder INDEX/MATCH used instead)
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.workbook.properties import CalcProperties

OUT = '/home/user/1040-Comprehnensive/docs/Tax_Workbook_Sample_Template_v4.xlsx'

wb = Workbook()
wb.remove(wb.active)
wb.calculation = CalcProperties(fullCalcOnLoad=True)  # force Excel recalc on open

# -------- styling helpers --------
HDR_FONT = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
HDR_FILL = PatternFill('solid', fgColor='305496')
SUB_FONT = Font(name='Calibri', size=10, bold=True, color='305496')
TITLE_FONT = Font(name='Calibri', size=14, bold=True, color='305496')
NOTE_FONT = Font(name='Calibri', size=9, italic=True, color='595959')
BORDER_THIN = Border(*[Side(style='thin', color='BFBFBF')]*4)

def write_header(ws, row, cols, start_col=1):
    for i, c in enumerate(cols):
        cell = ws.cell(row=row, column=start_col + i, value=c)
        cell.font = HDR_FONT
        cell.fill = HDR_FILL
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = BORDER_THIN

def autosize(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ============================================================
# 1. README
# ============================================================
ws = wb.create_sheet('README')
ws['A1'] = 'TAX WORKBOOK — SAMPLE TEMPLATE'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Architecture: KISS (year-sheet primary, master downstream) + GROUPBY view layer on top'
ws['A2'].font = NOTE_FONT

readme_blocks = [
    ('What this file demonstrates', [
        'Schema decisions for Master_Inputs, Planning_Adjustments, Strategies',
        '18-profile Treatment_Profile_Map (drives SE/NIIT/QBI/Char_Type auto-fill)',
        'Closed-set Dropdown_Lists with data validation wired',
        'Tax_Brackets 2024 + 2025 reference data',
        'Sample year sheet (Y2025_Sample) showing the KISS bucket-pattern input table + rollup',
        'GROUPBY-driven view layer examples (Tax_Summary, PBC_List, Dashboard_Export)',
        '5-tier scenario model: Baseline | Override | S1 | S2 | AsFiled',
        'Source dimension: Baseline | Adjustment | Tax Strategy (in Master_Inputs)',
    ]),
    ('What this file does NOT include (require VBA installation in real workbook)', [
        'The 7 KISS LAMBDAs (Calc_OrdinaryTax, Calc_CapGainsTax, Calc_1250Tax, Calc_SE_Tax, Calc_NIIT, Calc_QBI_Simple, Get_TreatmentDefault)',
        'The 14 v3-original LAMBDAs (OrdTax_FN, QBI_FN, etc.)',
        'Workbook_BeforeSave handler (auto-sync year sheet → Master_Inputs on Ctrl+S)',
        'modKissSync macros (PushAllYearsToMaster, RefreshInputsFromMaster, CommitPlanningRow, etc.)',
        'Calc engine on year sheets — placeholder SUMIFS used; real workbook uses LAMBDAs',
    ]),
    ('Tab map', [
        'CONTROL_PANEL    — TaxYear, FilingStatus, settings, named-range anchors',
        'Dropdown_Lists   — closed sets for Bucket, Input_Type, Source_Type, Treatment_Profile, etc.',
        'Treatment_Profile_Map — 18 profiles × (SE_Subject | NIIT_Class | QBI_Eligible | Char_Type)',
        'Tax_Brackets     — 2024 + 2025 federal brackets, LTCG brackets, NIIT/SE constants',
        'Tax_Line_Map     — Bucket + Input_Type → 1040 line + helper treatment',
        'Master_Inputs    — long-format parent table (sample row included)',
        'Planning_Adjustments — adjustments + strategies layer (sample row included)',
        'Strategies       — strategy library / catalog (20 standard plays)',
        'Y2025_Sample     — example year sheet (KISS pattern; bucket inputs + rollup + planning)',
        'Tax_Summary      — GROUPBY-driven cross-year view (placeholder formulas)',
        'PBC_List         — GROUPBY-driven document inventory from Master_Inputs',
        'Dashboard_Export — stable named-range export block for downstream consumers',
        'PROJECTION_HISTORY — snapshot archive / tie-out workpaper structure',
    ]),
    ('When you bring this into the real workbook', [
        '1. Install the 7 KISS LAMBDAs via VBA (use v3_kiss_merge_phase2.py as reference)',
        '2. Install modKissSync VBA module (re-import modKissSync.bas)',
        '3. Wire the Workbook_BeforeSave handler in ThisWorkbook',
        '4. Replace placeholder SUMIFS on Y2025_Sample rollup with the real LAMBDA calls',
        '5. Validation: confirm Cedillo Y2024 still ties to $7,213.92 federal tax',
    ]),
]

r = 4
for block_title, items in readme_blocks:
    ws.cell(row=r, column=1, value=block_title).font = SUB_FONT
    r += 1
    for item in items:
        ws.cell(row=r, column=1, value='  • ' + item)
        r += 1
    r += 1

autosize(ws, [120])

# ============================================================
# 2. CONTROL_PANEL
# ============================================================
ws = wb.create_sheet('CONTROL_PANEL')
ws['B2'] = 'TAX WORKBOOK — CONTROL PANEL'
ws['B2'].font = TITLE_FONT
ws['B3'] = 'Settings driving the rest of the workbook via named ranges'
ws['B3'].font = NOTE_FONT

ws['B5'] = '▸ SETTINGS'
ws['B5'].font = SUB_FONT

settings = [
    ('Tax Year Being Analyzed', 2025, 'Named: TaxYear — drives column lookups in brackets/limits'),
    ('Filing Status', 'MFJ', 'Named: FilingStatus — Single | MFJ | MFS | HOH'),
    ('Client ID', 'SAMPLE', 'Named: ClientID — used for Master_Inputs filtering'),
    ('Active Scenario', 'S1', 'Baseline | Override | S1 | S2 | AsFiled — drives Projection view'),
    ('Include Strategies', 'TRUE', 'Named: Include_Strategies — TRUE/FALSE toggles strategy layer'),
    ('Include Adjustments', 'TRUE', 'Named: Include_Adjustments — TRUE/FALSE toggles adjustment layer'),
]
for i, (label, val, note) in enumerate(settings):
    r = 6 + i
    ws.cell(row=r, column=2, value=label).font = Font(bold=True)
    ws.cell(row=r, column=3, value=val).alignment = Alignment(horizontal='center')
    ws.cell(row=r, column=3, value=val).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=5, value=note).font = NOTE_FONT

ws['B14'] = '▸ MACRO SHORTCUTS (real workbook — placeholders here)'
ws['B14'].font = SUB_FONT
macros = [
    ('PushAllYearsToMaster', 'Auto on every Ctrl+S — pushes all year-sheet data into Master_Inputs'),
    ('RefreshInputsFromMaster', 'Manual: master → active year sheet (overwrites!)'),
    ('CommitPlanningRow', 'On Planning_Adjustments: Approved → Committed, stamps date'),
    ('ConvertPlanningToInput', 'Planning row becomes a new Master_Inputs row'),
    ('SnapshotProjection', 'Captures current state to PROJECTION_HISTORY at active scenario'),
    ('RunRollover', 'Year-end: snapshot, increment year, build next-year skeleton'),
    ('InstallKissLambdas', 'One-time: register 7 KISS LAMBDAs in Name Manager'),
    ('PullExtractionsToAsFiled', 'Pull tie-out data from extraction file → AsFiled column'),
]
for i, (name, desc) in enumerate(macros):
    r = 15 + i
    ws.cell(row=r, column=2, value=name).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=3, value=desc).font = NOTE_FONT

autosize(ws, [3, 30, 20, 3, 80])

# Defined names — point to control panel cells
wb.defined_names['TaxYear'] = DefinedName('TaxYear', attr_text="'CONTROL_PANEL'!$C$6")
wb.defined_names['FilingStatus'] = DefinedName('FilingStatus', attr_text="'CONTROL_PANEL'!$C$7")
wb.defined_names['ClientID'] = DefinedName('ClientID', attr_text="'CONTROL_PANEL'!$C$8")
wb.defined_names['ActiveScenario'] = DefinedName('ActiveScenario', attr_text="'CONTROL_PANEL'!$C$9")
wb.defined_names['Include_Strategies'] = DefinedName('Include_Strategies', attr_text="'CONTROL_PANEL'!$C$10")
wb.defined_names['Include_Adjustments'] = DefinedName('Include_Adjustments', attr_text="'CONTROL_PANEL'!$C$11")

# ============================================================
# 3. Dropdown_Lists
# ============================================================
ws = wb.create_sheet('Dropdown_Lists')
ws['A1'] = 'CLOSED-SET LISTS — drive data validation across the workbook'
ws['A1'].font = TITLE_FONT

cols = {
    'Bucket': ['Business Income', 'Wages', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment', 'Other Income'],
    'Source_Layer': ['Baseline', 'Adjustment', 'Tax Strategy'],
    'Scenario': ['Baseline', 'Override', 'S1', 'S2', 'AsFiled'],
    'Status': ['Proposed', 'Approved', 'Committed', 'Implemented', 'Converted_To_Input', 'Rejected'],
    'FilingStatusOptions': ['Single', 'MFJ', 'MFS', 'HOH', 'QW'],
    'Provenance': ['PY Rolled Forward', 'PY Actuals', 'Estimate - Preparer', 'Estimate - Client',
                   'PBC - Requested', 'PBC - Received', 'PBC - Reviewed',
                   'Extraction - Imported', 'Extraction - Tied', 'System Calculated'],
    'Yes_No': ['Yes', 'No'],
    'NIIT_Class': ['Active', 'Passive', 'Portfolio', 'N/A'],
    # PER-BUCKET TREATMENT_PROFILE LISTS (drive cascading dropdown via INDIRECT)
    'BusinessIncome_Profiles': ['SchC_Active', 'SchE_Rental', 'SchE_REPro', 'SchF_Active',
                                'K1_PTP_Active', 'K1_PTP_Passive', 'K1_SCorp_Active', 'K1_SCorp_Passive', 'Trust_K1'],
    'Wages_Profiles':          ['W2_Employee', 'W2_SCorpOwner'],
    'InvestmentIncome_Profiles': ['Int_Taxable', 'Int_Exempt', 'Div_Qualified', 'Div_Ordinary'],
    'CapitalGains_Profiles':   ['LTCG_Stock', 'STCG_Stock', 'LTCG_RE', 'Sec1250_Recap', 'LTCG_K1_Passthrough'],
    'Adjustment_Profiles':     ['Adj_HSA', 'Adj_IRA', 'Adj_Retirement', 'Adj_SEHealth', 'Adj_StudentLoan'],
    'Itemized_Profiles':       ['Itm_Medical', 'Itm_SALT', 'Itm_Mortgage', 'Itm_Charity'],
    'Credit_Profiles':         ['Cr_CTC', 'Cr_Education', 'Cr_FTC'],
    'Payment_Profiles':        ['Pmt_Withholding', 'Pmt_EstTax'],
    'OtherIncome_Profiles':    ['Other_Generic'],
    # PER-BUCKET SOURCE_DOCUMENT LISTS (drive cascading dropdown via INDIRECT)
    'BusinessIncome_Docs': ['K-1', 'P&L Statement', 'QuickBooks Export', 'Sch C Workpaper', 'Sch E Workpaper', 'Sch F Workpaper', 'PY Return'],
    'Wages_Docs':          ['W-2', 'Paystub Summary', 'S-Corp Officer Comp Wkpr'],
    'InvestmentIncome_Docs': ['1099-INT', '1099-DIV', 'Broker Year-End Stmt'],
    'CapitalGains_Docs':   ['1099-B', 'Settlement Statement', 'K-1 (passthrough)', '8949 detail'],
    'Adjustment_Docs':     ['HSA Stmt', 'IRA Receipt', 'Retirement Plan Stmt', '1098-E', 'SE Health Premium'],
    'Itemized_Docs':       ['Charity Receipts', '1098 Mortgage', 'Property Tax Receipt', 'Medical Receipts'],
    'Credit_Docs':         ['CTC Verification', '1098-T', 'FTC Workpaper'],
    'Payment_Docs':        ['Withholding Stmt', 'Est Tax Vouchers'],
    'OtherIncome_Docs':    ['Other Doc'],
}

# Lay out the lists side-by-side
col_idx = 1
for header, items in cols.items():
    cell = ws.cell(row=2, column=col_idx, value=header)
    cell.font = HDR_FONT
    cell.fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=3 + i, column=col_idx, value=v)
    col_idx += 1

# Workbook-scope named ranges for each list
list_refs = {}
col_idx = 1
for header, items in cols.items():
    last_row = 2 + len(items)
    col_letter = get_column_letter(col_idx)
    ref = f"'Dropdown_Lists'!${col_letter}$3:${col_letter}${last_row}"
    list_refs[header] = ref
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col_idx += 1

autosize(ws, [22] * (col_idx))

# ============================================================
# 4. Treatment_Profile_Map
# ============================================================
ws = wb.create_sheet('Treatment_Profile_Map')
ws['A1'] = 'TREATMENT PROFILE MAP'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Selecting a Treatment_Profile auto-fills SE_Subject / NIIT_Class / QBI_Eligible / Char_Type. Real workbook uses Get_TreatmentDefault LAMBDA; here we expose the source table directly.'
ws['A2'].font = NOTE_FONT

cols = ['Profile', 'SE_Subject', 'NIIT_Class', 'QBI_Eligible', 'Char_Type', 'Default_Bucket', 'Notes']
write_header(ws, 4, cols)

profiles = [
    ('W2_Employee',       'No',  'Active',    'No',  'Ordinary',    'Wages',             'Standard W-2 wages'),
    ('W2_SCorpOwner',     'No',  'Active',    'No',  'Ordinary',    'Wages',             'S-Corp owner reasonable comp on W-2'),
    ('K1_SCorp_Active',   'No',  'Active',    'Yes', 'Ordinary',    'Business Income',   'Active S-Corp K-1 box 1'),
    ('K1_SCorp_Passive',  'No',  'Passive',   'Yes', 'Ordinary',    'Business Income',   'Passive S-Corp K-1 (rare)'),
    ('K1_PTP_Active',     'Yes', 'Active',    'Yes', 'Ordinary',    'Business Income',   'Active partnership K-1 (SE subject)'),
    ('K1_PTP_Passive',    'No',  'Passive',   'Yes', 'Ordinary',    'Business Income',   'Passive partnership K-1'),
    ('SchC_Active',       'Yes', 'Active',    'Yes', 'Ordinary',    'Business Income',   'Sole prop active SE'),
    ('SchE_Rental',       'No',  'Passive',   'No',  'Ordinary',    'Business Income',   'Rental real estate default passive'),
    ('Trust_K1',          'No',  'Portfolio', 'No',  'Ordinary',    'Business Income',   'Trust K-1'),
    ('Int_Taxable',       'No',  'Portfolio', 'No',  'Ordinary',    'Investment Income', 'Taxable interest income'),
    ('Int_Exempt',        'No',  'N/A',       'No',  'Ordinary',    'Investment Income', 'Tax-exempt interest'),
    ('Div_Qualified',     'No',  'Portfolio', 'No',  'QD/NonQD',    'Investment Income', 'Qualified dividends'),
    ('Div_Ordinary',      'No',  'Portfolio', 'No',  'QD/NonQD',    'Investment Income', 'Ordinary (non-qualified) dividends'),
    ('LTCG_Stock',        'No',  'Portfolio', 'No',  'LTCG/STCG',   'Capital Gains',     'Long-term capital gains, equities'),
    ('STCG_Stock',        'No',  'Portfolio', 'No',  'LTCG/STCG',   'Capital Gains',     'Short-term capital gains'),
    ('LTCG_RE',           'No',  'Passive',   'No',  'LTCG/STCG',   'Capital Gains',     'Long-term cap gain on real estate'),
    ('Sec1250_Recap',     'No',  'Passive',   'No',  'LTCG/1250',   'Capital Gains',     'Unrecaptured §1250 gain'),
    ('Adjustment_Generic','No',  'N/A',       'No',  'Deduction',   'Adjustment',        'Generic adjustment (HSA, IRA, etc.)'),
]
for i, row in enumerate(profiles):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)

autosize(ws, [22, 12, 12, 14, 14, 22, 45])

# ============================================================
# 5. Tax_Brackets
# ============================================================
ws = wb.create_sheet('Tax_Brackets')
ws['A1'] = 'TAX BRACKETS & CONSTANTS — 2024 & 2025'
ws['A1'].font = TITLE_FONT

ws['A3'] = '2025 ORDINARY — Single'
ws['A3'].font = SUB_FONT
ws['G3'] = '2025 ORDINARY — MFJ'
ws['G3'].font = SUB_FONT

write_header(ws, 4, ['Rate', 'Low', 'High'])
write_header(ws, 4, ['Rate', 'Low', 'High'], start_col=7)

ord_single_2025 = [
    (0.10,      0,    11925),
    (0.12,  11925,    48475),
    (0.22,  48475,   103350),
    (0.24, 103350,   197300),
    (0.32, 197300,   250525),
    (0.35, 250525,   626350),
    (0.37, 626350, 99999999),
]
ord_mfj_2025 = [
    (0.10,      0,    23850),
    (0.12,  23850,    96950),
    (0.22,  96950,   206700),
    (0.24, 206700,   394600),
    (0.32, 394600,   501050),
    (0.35, 501050,   751600),
    (0.37, 751600, 99999999),
]
for i, (rate, lo, hi) in enumerate(ord_single_2025):
    ws.cell(row=5+i, column=1, value=rate).number_format = '0.00%'
    ws.cell(row=5+i, column=2, value=lo)
    ws.cell(row=5+i, column=3, value=hi)
for i, (rate, lo, hi) in enumerate(ord_mfj_2025):
    ws.cell(row=5+i, column=7, value=rate).number_format = '0.00%'
    ws.cell(row=5+i, column=8, value=lo)
    ws.cell(row=5+i, column=9, value=hi)

ws['A16'] = '2025 LTCG — Single'
ws['A16'].font = SUB_FONT
ws['E16'] = '2025 LTCG — MFJ'
ws['E16'].font = SUB_FONT
write_header(ws, 17, ['Rate', 'Low', 'High'])
write_header(ws, 17, ['Rate', 'Low', 'High'], start_col=5)
ltcg_single = [(0.00, 0, 48350), (0.15, 48350, 533400), (0.20, 533400, 99999999)]
ltcg_mfj    = [(0.00, 0, 96700), (0.15, 96700, 600050), (0.20, 600050, 99999999)]
for i, (r, lo, hi) in enumerate(ltcg_single):
    ws.cell(row=18+i, column=1, value=r).number_format = '0.00%'
    ws.cell(row=18+i, column=2, value=lo)
    ws.cell(row=18+i, column=3, value=hi)
for i, (r, lo, hi) in enumerate(ltcg_mfj):
    ws.cell(row=18+i, column=5, value=r).number_format = '0.00%'
    ws.cell(row=18+i, column=6, value=lo)
    ws.cell(row=18+i, column=7, value=hi)

ws['A23'] = 'STANDARD DEDUCTIONS'
ws['A23'].font = SUB_FONT
write_header(ws, 24, ['Year', 'Single', 'MFJ', 'MFS', 'HOH'])
ws['A25'], ws['B25'], ws['C25'], ws['D25'], ws['E25'] = 2024, 14600, 29200, 14600, 21900
ws['A26'], ws['B26'], ws['C26'], ws['D26'], ws['E26'] = 2025, 15000, 30000, 15000, 22500

ws['A29'] = 'NIIT / SE / FICA CONSTANTS (2025)'
ws['A29'].font = SUB_FONT
constants = [
    ('NIIT_THRESH_MFJ', 250000, 'NIIT $250K threshold (MFJ)'),
    ('NIIT_THRESH_S', 200000, 'NIIT $200K threshold (Single/HOH)'),
    ('NIIT_THRESH_MFS', 125000, 'NIIT $125K threshold (MFS)'),
    ('NIIT_RATE', 0.038, '3.8% NIIT rate'),
    ('SS_WAGE_BASE_2025', 176100, 'Social Security wage base 2025'),
    ('SE_BASE_MULT', 0.9235, 'SE base multiplier (92.35%)'),
    ('SE_SS_RATE', 0.124, 'SE SS rate (12.4%)'),
    ('SE_MED_RATE', 0.029, 'SE Medicare rate (2.9%)'),
    ('ADDL_MED_RATE', 0.009, 'Additional Medicare tax 0.9%'),
    ('ADDL_MED_THRESH_MFJ', 250000, 'Addl Medicare threshold MFJ'),
    ('ADDL_MED_THRESH_S', 200000, 'Addl Medicare threshold Single'),
    ('EBL_LIMIT_MFJ', 626000, 'Excess Business Loss limit MFJ 2025'),
    ('EBL_LIMIT_S', 313000, 'Excess Business Loss limit Single 2025'),
]
for i, (name, val, note) in enumerate(constants):
    r = 30 + i
    ws.cell(row=r, column=1, value=name).font = Font(bold=True)
    ws.cell(row=r, column=2, value=val)
    ws.cell(row=r, column=3, value=note).font = NOTE_FONT
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Tax_Brackets'!$B${r}")

autosize(ws, [22, 12, 12, 3, 22, 12, 12, 22, 12, 12])

# ============================================================
# 6. Tax_Line_Map
# ============================================================
ws = wb.create_sheet('Tax_Line_Map')
ws['A1'] = 'TAX LINE MAP — Bucket + Input_Type → 1040 line + helper treatment'
ws['A1'].font = TITLE_FONT

write_header(ws, 3, ['Bucket', 'Input_Type', 'Consider_Prompt', 'Primary_Line', 'Helper_Treatment'])
lines = [
    ('Wages',             'W-2',                  'owner pay portion (S-corp owner)?', '1z', 'OWNER_PAY'),
    ('Wages',             'W2 - Self Pay',        'owner pay portion (S-corp owner)?', '1z', 'OWNER_PAY'),
    ('Wages',             'W2 - 3rd Party',       '(n/a)',                              '1z', 'NONE'),
    ('Investment Income', 'Interest',             'tax-exempt portion?',                '2b', 'TAX_EXEMPT'),
    ('Investment Income', '1099-INT',             'tax-exempt portion?',                '2b', 'TAX_EXEMPT'),
    ('Investment Income', 'Dividend',             'qualified dividend portion?',        '3b', 'QUAL_DIV'),
    ('Investment Income', '1099-DIV',             'qualified dividend portion?',        '3b', 'QUAL_DIV'),
    ('Capital Gains',     'Brokerage',            'LT/ST split + §1250?',               '7',  'LTCG_SPLIT'),
    ('Capital Gains',     'Real Estate',          'LT/ST split + §1250?',               '7',  'LTCG_SPLIT'),
    ('Capital Gains',     '1099-B',               'LT/ST split + §1250?',               '7',  'LTCG_SPLIT'),
    ('Business Income',   'Schedule C - Activity','SE earnings?',                       '10', 'SE_INCOME'),
    ('Business Income',   'Schedule E - Rental',  'rental passive treatment?',          '10', 'PASSIVE'),
    ('Business Income',   'Partnership K-1',      'active vs passive?',                 '10', 'K1_SPLIT'),
    ('Business Income',   'S-Corp K-1',           'active vs passive?',                 '10', 'K1_SPLIT'),
    ('Business Income',   'Trust K-1',            'character of distribution?',         '10', 'TRUST_DIST'),
    ('Adjustment',        'HSA',                  'family vs self limit?',              '10', 'HSA'),
    ('Adjustment',        'IRA',                  'deductible portion?',                '10', 'IRA'),
    ('Adjustment',        'Retirement',           'plan type / limit?',                 '10', 'RETIREMENT'),
    ('Adjustment',        'SE Health',            'subject to SE earnings limit?',      '10', 'SE_HEALTH'),
    ('Adjustment',        'Student Loan',         'phase-out by MAGI?',                 '10', 'STUDENT_LOAN'),
    ('Itemized',          'Medical',              '7.5% AGI floor',                     '12', 'MEDICAL'),
    ('Itemized',          'SALT',                 '$10K cap',                           '12', 'SALT'),
    ('Itemized',          'Mortgage',             'principal cap by date',              '12', 'MORTGAGE'),
    ('Itemized',          'Charity',              '60% AGI cap',                        '12', 'CHARITY'),
]
for i, row in enumerate(lines):
    for j, v in enumerate(row):
        ws.cell(row=4 + i, column=1 + j, value=v)
autosize(ws, [20, 25, 35, 14, 18])

# ============================================================
# 7. Master_Inputs (the long-format store)
# ============================================================
ws = wb.create_sheet('Master_Inputs')
ws['A1'] = 'MASTER INPUTS — long-format parent store. Auto-synced from year sheets in real workbook.'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Schema: one row per (Client, Year, Bucket, Input_Type, Source_Layer, Scenario) entry.'
ws['A2'].font = NOTE_FONT

# Column priority order:
# 1. Identifier  2-3. Time/Scenario  4-5. Client  6-8. Category cascade (Bucket → Treatment_Profile → Source_Document)
# 9-10. Layer/Status  11. Provenance  12-13. Payor  14-16. Amounts (Baseline / Helper / Adjustment)
# 17-19. Capital equity helper fields  20-24. Derived stored flags  25-26. Notes  27-29. Audit
cols = [
    'InputID',                                                            # A
    'Year', 'Scenario',                                                   # B-C
    'ClientID', 'ClientName',                                             # D-E
    'Bucket', 'Treatment_Profile', 'Source_Document',                     # F-H  (cascading dropdowns)
    'Source_Layer', 'Status',                                             # I-J
    'Provenance',                                                         # K  (new — PY/Estimate/PBC/etc.)
    'Payor', 'EIN',                                                       # L-M
    'Baseline_Amount', 'Helper_Amount', 'Adjustment_Amount',              # N-P
    'CE_Basis', 'CE_Proceeds', 'CE_AcqDate', 'CE_LT_ST',                  # Q-T (cap equity helper)
    'SE_Subject', 'NIIT_Class', 'QBI_Eligible',                           # U-W (stored; VBA auto-fills from Treatment_Profile_Map)
    'Primary_Line', 'Helper_Treatment',                                   # X-Y (stored; same)
    'Consider', 'Notes',                                                  # Z-AA
    'LastUpdated', 'UpdatedBy', 'ReviewStatus',                           # AB-AD
]
write_header(ws, 4, cols)

sample_rows = [
    # Cedillo Y2024 — tie-out validation case ($7,213.92 federal tax)
    ['CEDILLO|2024|Wages|01',           2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Wages',             'W2_SCorpOwner',   'W-2',       'Baseline', 'Approved',
     'PBC - Reviewed',    'Acme S-Corp', '00-0000000',
     153648, 0, 0,
     None, None, None, None,
     'No', 'Active', 'No', '1z', 'OWNER_PAY',
     'Owner reasonable comp', 'Cedillo validation case',
     '2026-05-15', 'SMJ', 'Approved'],
    ['CEDILLO|2024|BI|01',              2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Business Income',   'K1_PTP_Passive',  'K-1',       'Baseline', 'Approved',
     'PBC - Reviewed',    'Cedillo Partnership', '00-0000000',
     -100766, 0, 0,
     None, None, None, None,
     'No', 'Passive', 'Yes', '10', 'K1_SPLIT',
     'Passive loss', '',
     '2026-05-15', 'SMJ', 'Approved'],
    ['CEDILLO|2024|II|01',              2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Investment Income', 'Div_Ordinary',    '1099-DIV',  'Baseline', 'Approved',
     'PBC - Reviewed',    'Brokerage', '00-0000000',
     25922, 0, 0,
     None, None, None, None,
     'No', 'Portfolio', 'No', '3b', 'QUAL_DIV',
     'All non-qualified', '',
     '2026-05-15', 'SMJ', 'Approved'],
    ['CEDILLO|2024|CG|01',              2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Capital Gains',     'LTCG_Stock',      '1099-B',    'Baseline', 'Approved',
     'PBC - Reviewed',    'Brokerage', '00-0000000',
     14487, 0, 0,
     None, None, None, 'LT',
     'No', 'Portfolio', 'No', '7', 'LTCG_SPLIT',
     'Below MFJ 0% threshold', '',
     '2026-05-15', 'SMJ', 'Approved'],
    # Sample Y2025 entries demonstrating Adjustment_Amount + Provenance
    ['SAMPLE|2025|Wages|01',            2025, 'S1', 'SAMPLE', 'Sample Client',
     'Wages',             'W2_SCorpOwner',   'W-2',       'Baseline', 'Approved',
     'Estimate - Preparer','SampleCo S-Corp', '',
     100000, 100000, -25000,
     None, None, None, None,
     'No', 'Active', 'No', '1z', 'OWNER_PAY',
     'Adj -$25K from salary reduction', '',
     '2026-05-15', 'SMJ', 'Approved'],
    ['SAMPLE|2025|II|01',               2025, 'S1', 'SAMPLE', 'Sample Client',
     'Investment Income', 'Div_Qualified',   '1099-DIV',  'Baseline', 'Approved',
     'PBC - Received',    'Brokerage', '',
     10000, 7000, 0,
     None, None, None, None,
     'No', 'Portfolio', 'No', '3b', 'QUAL_DIV',
     'Helper = $7K qualified portion (Box 1b)', '',
     '2026-05-15', 'SMJ', 'Approved'],
    ['SAMPLE|2025|Adj_HSA|01',          2025, 'S1', 'SAMPLE', 'Sample Client',
     'Adjustment',        'Adj_HSA',         'HSA Stmt',  'Baseline', 'Approved',
     'Estimate - Preparer','', '',
     -8550, 0, 0,
     None, None, None, None,
     'No', 'N/A', 'No', '10', 'HSA',
     'Family HSA max', '',
     '2026-05-15', 'SMJ', 'Approved'],
]
for i, row in enumerate(sample_rows):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)

# Excel Table
last_row = 4 + len(sample_rows)
last_col_letter = get_column_letter(len(cols))
tbl = Table(displayName='tblMaster_Inputs', ref=f'A4:{last_col_letter}{last_row}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showFirstColumn=False,
                                     showLastColumn=False, showRowStripes=True, showColumnStripes=False)
ws.add_table(tbl)

# Widths (matches column order above)
autosize(ws, [28, 7, 11, 11, 18,                                   # A-E
              18, 22, 22, 14, 14,                                  # F-J (cascade columns wider)
              18, 18, 14,                                          # K-M
              14, 14, 14,                                          # N-P (amounts)
              12, 12, 12, 8,                                       # Q-T (CE)
              11, 12, 13, 11, 18,                                  # U-Y (derived)
              30, 30,                                              # Z-AA (consider/notes)
              14, 12, 14])                                         # AB-AD (audit)

# Data validation — CASCADING for Treatment_Profile and Source_Document based on Bucket
def add_dv(ws, col_letter, formula1, start=5, end=1000):
    dv = DataValidation(type='list', formula1=formula1, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f'{col_letter}{start}:{col_letter}{end}')

add_dv(ws, 'C', '=Scenario')                                                       # Scenario
add_dv(ws, 'F', '=Bucket')                                                         # Bucket (drives cascade)
add_dv(ws, 'G', '=INDIRECT(SUBSTITUTE($F5," ","")&"_Profiles")')                   # Treatment_Profile — CASCADED
add_dv(ws, 'H', '=INDIRECT(SUBSTITUTE($F5," ","")&"_Docs")')                       # Source_Document  — CASCADED
add_dv(ws, 'I', '=Source_Layer')                                                   # Source_Layer
add_dv(ws, 'J', '=Status')                                                         # Status
add_dv(ws, 'K', '=Provenance')                                                     # Provenance
add_dv(ws, 'U', '=Yes_No')                                                         # SE_Subject
add_dv(ws, 'V', '=NIIT_Class')                                                     # NIIT_Class
add_dv(ws, 'W', '=Yes_No')                                                         # QBI_Eligible

# ============================================================
# 8. Planning_Adjustments (separate sheet kept for readability)
# ============================================================
ws = wb.create_sheet('Planning_Adjustments')
ws['A1'] = 'PLANNING ADJUSTMENTS — current year strategy table'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Status workflow: Proposed → Approved → Committed → Converted_To_Input.'
ws['A2'].font = NOTE_FONT

cols = ['AdjID', 'ClientID', 'TaxYear', 'TargetLine', 'TargetInputID',
        'Strategy', 'Status', 'S1_Amount', 'S2_Amount',
        'Description', 'ProposedBy', 'ProposedDate', 'CommittedDate', 'ConvertedInputID']
write_header(ws, 4, cols)

adj_rows = [
    ['ADJ-2025-001', 'SAMPLE', 2025, '10', None,
     'SEP-IRA contribution', 'Approved', 0, -7000,
     '$7K SEP-IRA Y2025', 'SMJ', '2025-09-01', None, None],
    ['ADJ-2025-002', 'SAMPLE', 2025, '12', None,
     'DAF stack (Itemized)', 'Proposed', 15000, 15000,
     'DAF stack to bunch itemized', 'SMJ', '2025-10-15', None, None],
    ['ADJ-2025-003', 'SAMPLE', 2025, '1z', None,
     'S-Corp salary reduction', 'Committed', -25000, -25000,
     'Reduce W-2 by $25K', 'SMJ', '2025-08-01', '2025-08-15', None],
    ['ADJ-2025-004', 'SAMPLE', 2025, '10', None,
     'HSA family max', 'Converted_To_Input', -8550, -8550,
     'Family HSA max — converted to baseline', 'SMJ', '2025-07-01', '2025-07-15', 'SAMPLE|2025|Adjustment|HSA|Adjustment|S1|01'],
]
for i, row in enumerate(adj_rows):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)

table_ref = f'A4:{get_column_letter(len(cols))}{4+len(adj_rows)}'
tbl = Table(displayName='tblPlanning_Adjustments', ref=table_ref)
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

autosize(ws, [16, 12, 9, 11, 38, 28, 18, 12, 12, 35, 12, 14, 14, 38])

add_dv(ws, 'G', '=Status')

# ============================================================
# 9. Strategies (catalog)
# ============================================================
ws = wb.create_sheet('Strategies')
ws['A1'] = 'TAX PLANNING STRATEGIES — library / catalog'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Preparers draw FROM this catalog into Planning_Adjustments for a specific year/client.'
ws['A2'].font = NOTE_FONT

cols = ['ID', 'Group', 'Strategy Name', 'Description', 'Impact Type', 'Complexity', 'Tax Lines Affected', 'Est. Savings', 'Notes']
write_header(ws, 4, cols)

strategies = [
    ('STD-001', 'Low Hanging Fruit', 'Retirement Plan Contributions', 'Solo 401k, SEP IRA, or Cash Balance plan contributions', 'Single', 'Low', 'Line 10 (Non-SE) ↓', None, ''),
    ('STD-002', 'Low Hanging Fruit', 'Augusta Rule', 'Rent home to business up to 14 days tax-free', 'Single', 'Low', 'Line 10 (Non-SE) ↑', None, ''),
    ('STD-003', 'Low Hanging Fruit', 'Accountable Plan', 'Reimburse business expenses tax-free', 'Single', 'Low', 'Line 10 (Non-SE) ↑', None, ''),
    ('STD-004', 'Low Hanging Fruit', 'Employee Health/Fringe Benefits', 'Health insurance and fringe benefits through business', 'Single', 'Low', 'Line 10 (Non-SE) ↑', None, ''),
    ('STD-005', 'Low Hanging Fruit', 'Hiring Children', 'Pay children for legitimate work in business', 'Single', 'Medium', 'Line 10 (Non-SE) ↑, Line 1 ↑', None, ''),
    ('STD-006', 'Low Hanging Fruit', 'Income Timing', 'Defer/accelerate income between tax years', 'Single', 'Low', 'Various', None, ''),
    ('STD-007', 'SE Tax', 'Entity Restructure (S-Corp)', 'Convert Schedule C to S-Corp for wage/distribution split', 'Multi', 'High', 'Line 9 ↓, Line 10 ↑, Line 1 ↑', None, ''),
    ('STD-008', 'SE Tax', 'Wage Optimization', 'Optimize S-Corp salary for SE tax vs QBI', 'Multi', 'Medium', 'Line 1, Line 10', None, ''),
    ('STD-009', 'Cap Gain', '1031 Exchange', 'Defer gains on real estate sale', 'Single', 'High', 'Line 7 (LTCG) ↓', None, ''),
    ('STD-010', 'Cap Gain', 'Opportunity Zone', 'Invest gains in OZ for deferral/exclusion', 'Single', 'High', 'Line 7 (LTCG) ↓', None, ''),
    ('STD-011', 'Cap Gain', 'Tax Loss Harvesting', 'Sell losers to offset gains', 'Single', 'Medium', 'Line 7 ↓', None, ''),
    ('STD-012', 'CRE', 'Cost Segregation', 'Accelerate depreciation via cost seg study', 'Single', 'High', 'Line 10 (Non-SE) ↓', None, ''),
    ('STD-013', 'CRE', 'RE Professional Election', 'Convert passive to active for loss utilization', 'Multi', 'High', 'Line 14 → Line 10', None, ''),
    ('STD-014', 'CRE', 'Section 179 Expensing', 'Immediate expense vs depreciation', 'Single', 'Medium', 'Line 10 (Non-SE) ↓', None, ''),
    ('ADV-001', 'Advanced', 'Cash Balance Plan', 'Defined benefit plan for high earners', 'Single', 'High', 'Line 10 (Non-SE) ↓', None, ''),
    ('ADV-002', 'Advanced', 'Charitable Strategies', 'CRUT, CRAT, DAF for charitable deductions', 'Single', 'High', 'Line 12 (Itemized) ↑', None, ''),
    ('ADV-003', 'Advanced', 'QBI Optimization', 'Grouping and aggregation elections', 'Computed', 'High', 'QBI Deduction', None, ''),
]
for i, s in enumerate(strategies):
    for j, v in enumerate(s):
        ws.cell(row=5 + i, column=1 + j, value=v)
table_ref = f'A4:{get_column_letter(len(cols))}{4+len(strategies)}'
tbl = Table(displayName='tblStrategies', ref=table_ref)
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

autosize(ws, [10, 18, 32, 50, 12, 12, 30, 12, 25])

# ============================================================
# 10. Y2025_Sample — KISS year sheet pattern
# ============================================================
ws = wb.create_sheet('Y2025_Sample')
ws['A1'] = 'Y2025 — sample year sheet (KISS pattern)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'LEFT: bucket-pattern input table.  RIGHT: tax rollup + planning (W:AG).  Real workbook also has LAMBDA-driven calc block at W21:AG27.'
ws['A2'].font = NOTE_FONT

# Left side: input Table
ws['A4'] = 'SOURCE INPUTS — tblY2025_Inputs'
ws['A4'].font = SUB_FONT
# Column priority order:
# 1. Identifier  2-4. Category cascade (Bucket → Treatment_Profile → Source_Document)
# 5. Payor  6-8. Amounts (Baseline / Helper / Adjustment)  9. Provenance
# 10-14. Derived stored flags  15-16. Consider / Notes
input_cols = [
    'Source_ID',                                                                   # A
    'Bucket', 'Treatment_Profile', 'Source_Document',                              # B-D  (cascading dropdowns)
    'Payor',                                                                       # E
    'Baseline_Amount', 'Helper_Amount', 'Adjustment_Amount',                       # F-H
    'Provenance',                                                                  # I  (new — PY/Estimate/PBC/etc.)
    'SE_Subject', 'NIIT_Class', 'QBI_Eligible',                                    # J-L  (stored; VBA auto-fills from Treatment_Profile_Map)
    'Primary_Line', 'Helper_Treatment',                                            # M-N  (stored; same)
    'Consider', 'Notes',                                                           # O-P
]
write_header(ws, 5, input_cols)

starter_rows = [
    ['Y25-001', 'Wages',             'W2_SCorpOwner',   'W-2',       'SampleCo S-Corp',     100000, 100000, -25000, 'Estimate - Preparer', 'No', 'Active',    'No',  '1z', 'OWNER_PAY',   'Owner reasonable comp; -$25K planning adj', ''],
    ['Y25-002', 'Business Income',   'K1_SCorp_Active', 'K-1',       'SampleCo S-Corp K-1', 200000, 0,      0,      'PY Rolled Forward',   'No', 'Active',    'Yes', '10', 'K1_SPLIT',    'Active S-corp K-1', ''],
    ['Y25-003', 'Investment Income', 'Div_Qualified',   '1099-DIV',  'Brokerage',           10000,  7000,   0,      'PBC - Received',      'No', 'Portfolio', 'No',  '3b', 'QUAL_DIV',    '$7K qualified', ''],
    ['Y25-004', 'Investment Income', 'Int_Taxable',     '1099-INT',  'Brokerage',           500,    0,      0,      'PBC - Received',      'No', 'Portfolio', 'No',  '2b', 'TAX_EXEMPT',  'All taxable', ''],
    ['Y25-005', 'Capital Gains',     'LTCG_Stock',      '1099-B',    'Brokerage',           25000,  0,      0,      'PBC - Requested',     'No', 'Portfolio', 'No',  '7',  'LTCG_SPLIT',  'All long-term', ''],
    ['Y25-006', 'Adjustment',        'Adj_HSA',         'HSA Stmt',  '',                    -8550,  0,      0,      'Estimate - Preparer', 'No', 'N/A',       'No',  '10', 'HSA',         'Family HSA max', ''],
    ['Y25-007', 'Itemized',          'Itm_SALT',        'Property Tax Receipt', '',         10000,  0,      0,      'PBC - Received',      'No', 'N/A',       'No',  '12', 'SALT',        'SALT cap', ''],
]
for i, row in enumerate(starter_rows):
    for j, v in enumerate(row):
        ws.cell(row=6 + i, column=1 + j, value=v)

table_ref = f'A5:{get_column_letter(len(input_cols))}{5+len(starter_rows)}'
tbl = Table(displayName='tblY2025_Inputs', ref=table_ref)
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

# CASCADING data validation
add_dv(ws, 'B', '=Bucket', start=6, end=200)                                              # Bucket (drives cascade)
add_dv(ws, 'C', '=INDIRECT(SUBSTITUTE($B6," ","")&"_Profiles")', start=6, end=200)         # Treatment_Profile — CASCADED
add_dv(ws, 'D', '=INDIRECT(SUBSTITUTE($B6," ","")&"_Docs")', start=6, end=200)             # Source_Document  — CASCADED
add_dv(ws, 'I', '=Provenance', start=6, end=200)                                           # Provenance
add_dv(ws, 'J', '=Yes_No', start=6, end=200)                                               # SE_Subject
add_dv(ws, 'K', '=NIIT_Class', start=6, end=200)                                           # NIIT_Class
add_dv(ws, 'L', '=Yes_No', start=6, end=200)                                               # QBI_Eligible

# Right side rollup
ws['W4'] = 'TAX ROLLUP'
ws['W4'].font = SUB_FONT
rollup_cols = ['Line', 'Description', 'Baseline', 'Override', 'Effective',
               'S1_Adj', 'S1_Total', 'S2_Adj', 'S2_Total', 'AsFiled', 'Variance']
write_header(ws, 5, rollup_cols, start_col=23)  # column W is 23

rollup_lines = [
    ('1z',  'Wages'),
    ('2a',  'Tax-exempt interest'),
    ('2b',  'Taxable interest'),
    ('3a',  'Qualified dividends'),
    ('3b',  'Ordinary dividends (total)'),
    ('7',   'Capital gain or (loss)'),
    ('8',   'Other income (Sch 1)'),
    ('9',   'TOTAL INCOME (aggregator)'),
    ('10',  'Adjustments to income'),
    ('11',  'AGI (aggregator)'),
    ('12',  'Std/Itemized deduction'),
    ('13',  'QBI deduction'),
    ('15',  'TAXABLE INCOME (aggregator)'),
]
for i, (line, desc) in enumerate(rollup_lines):
    r = 6 + i
    ws.cell(row=r, column=23, value=line)
    ws.cell(row=r, column=24, value=desc)
    # Baseline: SUMIFS by Primary_Line; special-case helpers for line 2a (tax-exempt) and 3a (qualified div)
    if line == '2a':
        ws.cell(row=r, column=25, value=f'=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "TAX_EXEMPT")')
    elif line == '3a':
        ws.cell(row=r, column=25, value=f'=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "QUAL_DIV")')
    else:
        ws.cell(row=r, column=25, value=f'=SUMIFS(tblY2025_Inputs[Baseline_Amount], tblY2025_Inputs[Primary_Line], $W{r})')
    # S1_Adj: SUMIFS Adjustment_Amount by Primary_Line
    ws.cell(row=r, column=28, value=f'=SUMIFS(tblY2025_Inputs[Adjustment_Amount], tblY2025_Inputs[Primary_Line], $W{r})')
    # Effective = Baseline + (Override if set)
    ws.cell(row=r, column=27, value=f'=Y{r}+IF(ISNUMBER(Z{r}),Z{r},0)')
    # S1_Total = Effective + S1_Adj
    ws.cell(row=r, column=29, value=f'=IFERROR(AA{r}+AB{r},0)')
    # S2_Total = Effective + S2_Adj (placeholder — same as S1 until S2 differs)
    ws.cell(row=r, column=31, value=f'=IFERROR(AA{r}+AD{r},0)')

ws['W21'] = 'TAX COMPUTATION (real workbook uses 7 KISS LAMBDAs — placeholders shown)'
ws['W21'].font = SUB_FONT
calc_lines = [
    ('Ord Tax',   'Calc_OrdinaryTax(TI, FS)',  '=0  (replace with =Calc_OrdinaryTax(TI, FilingStatus))'),
    ('LTCG Tax',  'Calc_CapGainsTax(LTCG, ord, FS)', '=0  (replace with LAMBDA call)'),
    ('SE Tax',    'Calc_SE_Tax(SE_inc, W2, FS)','=0'),
    ('NIIT',      'Calc_NIIT(MAGI, NII, FS)',  '=0'),
    ('Addl Medicare', 'AddlMedicareTax_FN(W2, SE, FS)', '=0'),
    ('TOTAL FED TAX', 'sum of above', '=0'),
]
for i, (label, sig, placeholder) in enumerate(calc_lines):
    r = 22 + i
    ws.cell(row=r, column=23, value=label).font = Font(bold=True if 'TOTAL' in label else False)
    ws.cell(row=r, column=24, value=sig).font = NOTE_FONT
    ws.cell(row=r, column=25, value=placeholder).font = NOTE_FONT

# Planning Adjustments table on year sheet (the KISS pattern)
ws['W30'] = 'PLANNING ADJUSTMENTS — edit here; flows back into rollup via SUMIFS'
ws['W30'].font = SUB_FONT
plan_cols = ['AdjID', 'Strategy', 'Status', 'TargetLine', 'Description', 'S1_Amount', 'S2_Amount', 'ProposedDate', 'Notes']
write_header(ws, 31, plan_cols, start_col=23)

# Set some column widths for both sides
for col_letter, w in zip(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
                          [12,18,22,14,16,8,14,14,12,22,11,12,13,13,12,12,22]):
    ws.column_dimensions[col_letter].width = w
for col_letter, w in zip(['W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG'],
                          [8,30,12,12,12,12,12,12,12,12,12]):
    ws.column_dimensions[col_letter].width = w

# ============================================================
# 11. Tax_Summary — GROUPBY-driven cross-year view
# ============================================================
ws = wb.create_sheet('Tax_Summary')
ws['A1'] = 'TAX SUMMARY — cross-year view, GROUPBY-driven from Master_Inputs'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'In real workbook, this uses Excel 365 GROUPBY/PIVOTBY to aggregate Master_Inputs by Year/Scenario/Bucket. Below shows the formula pattern.'
ws['A2'].font = NOTE_FONT

ws['A4'] = 'PATTERN — GROUPBY example'
ws['A4'].font = SUB_FONT
ws['A5'] = "Type into a cell on a 365 build:"
ws['A5'].font = Font(italic=True)
ws['A6'] = "=GROUPBY( tblMaster_Inputs[[TaxYear]:[Bucket]], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0 )"
ws['A6'].font = Font(name='Consolas', size=10)

ws['A8'] = 'PATTERN — PIVOTBY example (rows × columns)'
ws['A8'].font = SUB_FONT
ws['A9'] = "=PIVOTBY( tblMaster_Inputs[Bucket], tblMaster_Inputs[TaxYear], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 2 )"
ws['A9'].font = Font(name='Consolas', size=10)

ws['A11'] = 'PATTERN — SUMIFS fallback (works on any Excel version)'
ws['A11'].font = SUB_FONT
ws['A12'] = 'Wages 2024 baseline = SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[TaxYear], 2024, tblMaster_Inputs[Bucket], "Wages", tblMaster_Inputs[Source_Layer], "Baseline")'
ws['A12'].font = Font(name='Consolas', size=10)

ws['A14'] = 'EXAMPLE CROSS-YEAR ROLLUP (using SUMIFS)'
ws['A14'].font = SUB_FONT
write_header(ws, 15, ['Bucket', '2023', '2024', '2025', '2026'])
buckets_for_summary = ['Wages', 'Business Income', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment']
for i, b in enumerate(buckets_for_summary):
    r = 16 + i
    ws.cell(row=r, column=1, value=b)
    for j, yr in enumerate([2023, 2024, 2025, 2026]):
        col_letter = get_column_letter(2 + j)
        ws.cell(row=r, column=2 + j, value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[TaxYear], {yr}, tblMaster_Inputs[Bucket], A{r}, tblMaster_Inputs[Source_Layer], "Baseline")')

autosize(ws, [22, 14, 14, 14, 14])

# ============================================================
# 12. PBC_List — GROUPBY-driven document inventory
# ============================================================
ws = wb.create_sheet('PBC_List')
ws['A1'] = 'PBC CHECKLIST — auto-generated from Master_Inputs'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Filtered to Source_Layer = "Baseline" and TaxYear = active. Real workbook uses GROUPBY; below shows the pattern.'
ws['A2'].font = NOTE_FONT

ws['A4'] = 'GROUPBY pattern (Excel 365)'
ws['A4'].font = SUB_FONT
ws['A5'] = '=GROUPBY( CHOOSECOLS(FILTER(tblMaster_Inputs, (tblMaster_Inputs[TaxYear]=TaxYear)*(tblMaster_Inputs[Source_Layer]="Baseline")), MATCH("Bucket",tblMaster_Inputs[#Headers],0), MATCH("Source_Type",tblMaster_Inputs[#Headers],0), MATCH("Payor",tblMaster_Inputs[#Headers],0), MATCH("Source_Document",tblMaster_Inputs[#Headers],0)), 1, COUNTA, 3, 0 )'
ws['A5'].font = Font(name='Consolas', size=9)

ws['A7'] = 'EXAMPLE OUTPUT'
ws['A7'].font = SUB_FONT
write_header(ws, 8, ['Received', 'Bucket', 'Source_Type', 'Payor', 'Source_Document'])

# Hardcoded sample — will be replaced by GROUPBY result in real workbook
pbc_rows = [
    ('[ ]', 'Wages', 'W2 - Self Pay', 'Acme S-Corp', 'W-2'),
    ('[ ]', 'Business Income', 'Partnership K-1', 'Cedillo Partnership', 'K-1 form'),
    ('[ ]', 'Investment Income', 'Dividend', 'Brokerage', '1099-DIV'),
    ('[ ]', 'Capital Gains', 'Brokerage', 'Brokerage', '1099-B'),
]
for i, row in enumerate(pbc_rows):
    for j, v in enumerate(row):
        ws.cell(row=9 + i, column=1 + j, value=v)

autosize(ws, [10, 22, 22, 28, 22])

# ============================================================
# 13. Dashboard_Export — stable named-range contract
# ============================================================
ws = wb.create_sheet('Dashboard_Export')
ws['A1'] = 'DASHBOARD EXPORT — stable named-range block for downstream consumers'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Downstream dashboards (Jeff, leadership, Power BI) pull from these named ranges. Layout below is the CONTRACT — do not move cells.'
ws['A2'].font = NOTE_FONT

ws['B4'] = 'METRIC'
ws['B4'].font = HDR_FONT
ws['B4'].fill = HDR_FILL
ws['C4'] = 'VALUE'
ws['C4'].font = HDR_FONT
ws['C4'].fill = HDR_FILL
ws['D4'] = 'NAMED RANGE'
ws['D4'].font = HDR_FONT
ws['D4'].fill = HDR_FILL

metrics = [
    ('Active Tax Year',       '=TaxYear', 'Dashboard_TaxYear'),
    ('Filing Status',         '=FilingStatus', 'Dashboard_FilingStatus'),
    ('Total Income',          '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[TaxYear], TaxYear, tblMaster_Inputs[Source_Layer], "Baseline")', 'Dashboard_TotalIncome'),
    ('AGI',                   '=Dashboard_TotalIncome - SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[TaxYear], TaxYear, tblMaster_Inputs[Bucket], "Adjustment")', 'Dashboard_AGI'),
    ('Std Deduction (lookup)','=INDEX(Tax_Brackets!$B$25:$E$26, MATCH(TaxYear, Tax_Brackets!$A$25:$A$26, 0), MATCH(FilingStatus, {"Single","MFJ","MFS","HOH"}, 0))', 'Dashboard_StdDed'),
    ('Taxable Income (est)',  '=Dashboard_AGI - Dashboard_StdDed', 'Dashboard_TaxableIncome'),
    ('Total Federal Tax',     'placeholder — wire to year-sheet rollup in real workbook', 'Dashboard_TotalFedTax'),
]
for i, (label, formula, name) in enumerate(metrics):
    r = 5 + i
    ws.cell(row=r, column=2, value=label).font = Font(bold=True)
    ws.cell(row=r, column=3, value=formula)
    ws.cell(row=r, column=4, value=name).font = NOTE_FONT
    # Register the named range pointing at column C
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Dashboard_Export'!$C${r}")

autosize(ws, [3, 30, 70, 28])

# ============================================================
# 14. PROJECTION_HISTORY — snapshot archive
# ============================================================
ws = wb.create_sheet('PROJECTION_HISTORY')
ws['A1'] = 'PROJECTION HISTORY — snapshot archive and tie-out workpaper'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Year-end rollover macro appends a row per line per scenario. Accuracy_Grade = how close the projection came to actual filed.'
ws['A2'].font = NOTE_FONT

write_header(ws, 4, ['Year', 'Scenario', 'Line', 'Description', 'Projected (when made)', 'Filed (actual)', 'Variance $', 'Variance %', 'Accuracy Grade', 'Snapshot Date', 'Notes'])

# Example rows
example = [
    (2023, 'AsFiled', '1z', 'Wages',           105000, 108500, 3500, 0.0333, 'A', '2024-04-15', 'Minor variance'),
    (2023, 'AsFiled', '2b', 'Taxable interest', 8500,   8200,  -300, -0.0353,'A', '2024-04-15', ''),
    (2024, 'S1 (Extension)', '1z', 'Wages',    112000, None,  None, None,   None,'2024-04-15', 'Projected at extension; actual not yet filed at snapshot'),
]
for i, row in enumerate(example):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)

autosize(ws, [8, 18, 8, 28, 16, 14, 12, 12, 14, 14, 40])

# ============================================================
# Reorder sheets — README first, then logical flow
# ============================================================
order = ['README', 'CONTROL_PANEL', 'Y2025_Sample', 'Master_Inputs',
         'Planning_Adjustments', 'Strategies', 'Tax_Summary', 'PBC_List',
         'Dashboard_Export', 'PROJECTION_HISTORY',
         'Treatment_Profile_Map', 'Tax_Brackets', 'Tax_Line_Map', 'Dropdown_Lists']
wb._sheets = [wb[name] for name in order]

# Save
wb.save(OUT)
print(f'Saved: {OUT}')
print(f'Sheets ({len(wb.sheetnames)}):')
for n in wb.sheetnames:
    print(f'  - {n}')
