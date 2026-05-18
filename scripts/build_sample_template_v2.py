"""Build v2 sample .xlsx — final schema with cascading dropdowns, derived columns,
adjustment column on input table, separate strategies table with commit gating,
True Tax Burden box for owner FICA, and year-sheet ↔ pivot integrity check.

Output: docs/Tax_Workbook_Sample_Template_v2.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

OUT = '/home/user/1040-Comprehnensive/docs/Tax_Workbook_Sample_Template_v2.xlsx'

wb = Workbook()
wb.remove(wb.active)

# ---------- styling ----------
HDR_FONT = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
HDR_FILL = PatternFill('solid', fgColor='305496')
SUB_FONT = Font(name='Calibri', size=10, bold=True, color='305496')
TITLE_FONT = Font(name='Calibri', size=14, bold=True, color='305496')
NOTE_FONT = Font(name='Calibri', size=9, italic=True, color='595959')
DERIVED_FILL = PatternFill('solid', fgColor='E7E6E6')  # gray = derived (formula)
INPUT_FILL = PatternFill('solid', fgColor='FFF2CC')    # yellow = preparer input
KEY_FILL = PatternFill('solid', fgColor='DDEBF7')      # blue = key/dropdown

def hdr(ws, row, cols, start_col=1):
    for i, c in enumerate(cols):
        cell = ws.cell(row=row, column=start_col + i, value=c)
        cell.font = HDR_FONT
        cell.fill = HDR_FILL
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ============================================================
# README
# ============================================================
ws = wb.create_sheet('README')
ws['A1'] = 'TAX WORKBOOK — SAMPLE TEMPLATE v2 (final schema)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'KISS architecture: year sheets primary, Master_Inputs aggregate, pivots feed downstream views.'
ws['A2'].font = NOTE_FONT

readme = [
    ('FINAL SCHEMA (Master_Inputs and year-sheet input table)', [
        'INPUT (preparer types these — yellow cells):',
        '  Year, Scenario, ClientID, Bucket, Treatment_Profile, Source_Document,',
        '  Source_Layer, Status, Provenance, Payor, Baseline_Amount, Helper_Amount,',
        '  Adjustment_Amount, Consider, Notes',
        '',
        'DERIVED (formula-populated — gray cells, available for pivots):',
        '  SE_Subject, NIIT_Class, QBI_Eligible, Primary_Line, Helper_Treatment,',
        '  Consider_Prompt — all looked up via Treatment_Profile_Map and Tax_Line_Map',
    ]),
    ('CASCADING DROPDOWNS (pick Bucket → narrows Profile and Source_Document)', [
        'Bucket drives both:',
        '  Treatment_Profile dropdown → INDIRECT(SUBSTITUTE(Bucket," ","")&"_Profiles")',
        '  Source_Document dropdown   → INDIRECT(SUBSTITUTE(Bucket," ","")&"_Docs")',
        'Per-bucket named ranges live in Dropdown_Lists.',
    ]),
    ('ADJUSTMENTS vs. STRATEGIES — different conceptual roles', [
        'ADJUSTMENT = revision to an existing source-input row.',
        '  Lives as a column (Adjustment_Amount) on the same input row.',
        '  Pushed to Master_Inputs as a separate row with Source_Layer = "Adjustment".',
        '',
        'STRATEGY = new tax position (Cost Seg, Augusta Rule, S-Corp Election, etc.).',
        '  Lives in a separate Strategies_Y2025 planning table on the year sheet.',
        '  Pushed to Master_Inputs only when Status IN ("Committed", "Implemented").',
        '  Once Status = "Converted_To_Input", strategy becomes next-year baseline row.',
    ]),
    ('PROVENANCE — orthogonal to Scenario; tracks where the number came from', [
        'PY Rolled Forward · PY Actuals · Estimate - Preparer · Estimate - Client',
        'PBC - Requested · PBC - Received · PBC - Reviewed',
        'Extraction - Imported · Extraction - Tied · System Calculated',
    ]),
    ('INTEGRITY CHECK — year-sheet calc = pivot-over-master calc', [
        'For any (Year, Scenario): year-sheet TOTAL FED TAX must equal',
        'pivot-over-Master_Inputs TOTAL FED TAX.',
        'Y2025_Sample sheet shows both side-by-side at the bottom of the rollup.',
    ]),
    ('TRUE TAX BURDEN BOX — separate from 1040 federal tax', [
        'Owner W-2 wages trigger BOTH employer-side and employee-side FICA.',
        'Total Fed Tax = 1040 federal tax (the standard computation).',
        'True Tax Burden = Total Fed Tax + FICA on owner W-2 (employer + employee).',
        'Computed via existing FICA_EmployerTax_FN / FICA_EmployeeTax_FN LAMBDAs.',
    ]),
    ('NOT INCLUDED (require VBA install in real workbook)', [
        '7 KISS LAMBDAs (Calc_OrdinaryTax, Calc_QBI_Simple, FICA_*_FN, etc.)',
        'Workbook_BeforeSave auto-sync handler',
        'modKissSync macros (PushAllYearsToMaster, CommitPlanningRow, etc.)',
        'All tax-computation cells show "=0  (placeholder — wire to LAMBDA)"',
    ]),
    ('TAB MAP', [
        'README',
        'CONTROL_PANEL',
        'Y2025_Sample           — bucket-pattern input table + rollup + strategies table + True Tax Burden box',
        'Master_Inputs          — long-format parent store (Cedillo Y2024 sample data)',
        'Strategies_Library     — 20 standard strategies with Buckets_Impacted',
        'Tax_Summary            — GROUPBY-driven cross-year view',
        'PBC_List               — GROUPBY-driven document inventory',
        'Dashboard_Export       — stable named-range block for Jeff',
        'PROJECTION_HISTORY     — snapshot archive / tie-out workpaper',
        'Treatment_Profile_Map  — 18 profiles × (Bucket | SE | NIIT | QBI | Primary_Line | Helper_Treatment | Consider_Prompt)',
        'Tax_Brackets           — 2024/2025 brackets, NIIT/SE/FICA constants',
        'Dropdown_Lists         — closed sets + per-bucket named ranges for cascading',
    ]),
]
r = 4
for title, lines in readme:
    ws.cell(row=r, column=1, value=title).font = SUB_FONT
    r += 1
    for line in lines:
        ws.cell(row=r, column=1, value='  ' + line if line else '')
        r += 1
    r += 1
widths(ws, [120])

# ============================================================
# CONTROL_PANEL
# ============================================================
ws = wb.create_sheet('CONTROL_PANEL')
ws['B2'] = 'TAX WORKBOOK — CONTROL PANEL'
ws['B2'].font = TITLE_FONT
ws['B3'] = 'Settings driving the rest of the workbook via named ranges'
ws['B3'].font = NOTE_FONT

ws['B5'] = '▸ SETTINGS'
ws['B5'].font = SUB_FONT
settings = [
    ('Tax Year Being Analyzed', 2025, 'TaxYear — drives bracket/limit lookups'),
    ('Filing Status', 'MFJ', 'FilingStatus — Single | MFJ | MFS | HOH'),
    ('Client ID', 'SAMPLE', 'ClientID — Master_Inputs filtering key'),
    ('Active Scenario', 'S1', 'Baseline | Override | S1 | S2 | AsFiled'),
    ('Include Strategies', True, 'Include_Strategies — toggles strategy layer in rollup'),
    ('Include Adjustments', True, 'Include_Adjustments — toggles adjustment layer'),
]
for i, (label, val, note) in enumerate(settings):
    r = 6 + i
    ws.cell(row=r, column=2, value=label).font = Font(bold=True)
    c = ws.cell(row=r, column=3, value=val)
    c.font = Font(bold=True, color='305496')
    c.fill = KEY_FILL
    c.alignment = Alignment(horizontal='center')
    ws.cell(row=r, column=5, value=note).font = NOTE_FONT

ws['B14'] = '▸ MACRO SHORTCUTS (real workbook only — placeholders)'
ws['B14'].font = SUB_FONT
macros = [
    ('PushAllYearsToMaster', 'Auto on Ctrl+S — pushes year sheets to Master_Inputs'),
    ('PushCommittedStrategies', 'Push only strategies with Status IN (Committed, Implemented)'),
    ('RefreshInputsFromMaster', 'Manual: master → active year sheet (overwrites!)'),
    ('CommitPlanningRow', 'Approved → Committed; stamps date; triggers master push'),
    ('ConvertStrategyToInput', 'Strategy → new Baseline row in next year'),
    ('SnapshotProjection', 'Captures current state to PROJECTION_HISTORY'),
    ('RunRollover', 'Year-end: snapshot, increment year, build next-year skeleton'),
    ('InstallKissLambdas', 'One-time: register 7+ KISS LAMBDAs'),
    ('PullExtractionsToAsFiled', 'Pull extraction file → AsFiled column'),
]
for i, (n, d) in enumerate(macros):
    r = 15 + i
    ws.cell(row=r, column=2, value=n).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=3, value=d).font = NOTE_FONT

widths(ws, [3, 30, 22, 3, 80])

wb.defined_names['TaxYear'] = DefinedName('TaxYear', attr_text="'CONTROL_PANEL'!$C$6")
wb.defined_names['FilingStatus'] = DefinedName('FilingStatus', attr_text="'CONTROL_PANEL'!$C$7")
wb.defined_names['ClientID'] = DefinedName('ClientID', attr_text="'CONTROL_PANEL'!$C$8")
wb.defined_names['ActiveScenario'] = DefinedName('ActiveScenario', attr_text="'CONTROL_PANEL'!$C$9")
wb.defined_names['Include_Strategies'] = DefinedName('Include_Strategies', attr_text="'CONTROL_PANEL'!$C$10")
wb.defined_names['Include_Adjustments'] = DefinedName('Include_Adjustments', attr_text="'CONTROL_PANEL'!$C$11")

# ============================================================
# Dropdown_Lists — with per-bucket named ranges for cascade
# ============================================================
ws = wb.create_sheet('Dropdown_Lists')
ws['A1'] = 'DROPDOWN LISTS — closed sets + per-bucket cascade named ranges'
ws['A1'].font = TITLE_FONT

# Top-level dropdowns (single column each)
top_lists = {
    'Bucket':              ['Business Income', 'Wages', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment'],
    'Source_Layer':        ['Baseline', 'Adjustment', 'Tax Strategy'],
    'Scenario':            ['Baseline', 'Override', 'S1', 'S2', 'AsFiled'],
    'Status':              ['Proposed', 'Approved', 'Committed', 'Implemented', 'Converted_To_Input', 'Rejected'],
    'FilingStatusOptions': ['Single', 'MFJ', 'MFS', 'HOH', 'QW'],
    'Yes_No':              ['Yes', 'No'],
    'NIIT_Class':          ['Active', 'Passive', 'Portfolio', 'N/A'],
    'Provenance':          [
        'PY Rolled Forward', 'PY Actuals',
        'Estimate - Preparer', 'Estimate - Client',
        'PBC - Requested', 'PBC - Received', 'PBC - Reviewed',
        'Extraction - Imported', 'Extraction - Tied',
        'System Calculated',
    ],
}
col = 1
for header, items in top_lists.items():
    c = ws.cell(row=3, column=col, value=header)
    c.font = HDR_FONT; c.fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=4 + i, column=col, value=v)
    last_row = 3 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$4:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

# Per-bucket Treatment_Profile lists (cascade target)
ws.cell(row=15, column=1, value='▸ PER-BUCKET TREATMENT_PROFILE LISTS  (named ranges keyed to bucket name with spaces removed)').font = SUB_FONT
bucket_profiles = {
    'BusinessIncome_Profiles': ['SchC_Active', 'SchE_Rental', 'SchE_REPro', 'SchF_Active',
                                'K1_PTP_Active', 'K1_PTP_Passive', 'K1_SCorp_Active', 'K1_SCorp_Passive', 'Trust_K1'],
    'Wages_Profiles':          ['W2_Employee', 'W2_SCorpOwner'],
    'InvestmentIncome_Profiles': ['Int_Taxable', 'Int_Exempt', 'Div_Qualified', 'Div_Ordinary'],
    'CapitalGains_Profiles':   ['LTCG_Stock', 'STCG_Stock', 'LTCG_RE', 'Sec1250_Recap', 'LTCG_K1_Passthrough'],
    'Adjustment_Profiles':     ['Adj_HSA', 'Adj_IRA', 'Adj_Retirement', 'Adj_SEHealth', 'Adj_StudentLoan'],
    'Itemized_Profiles':       ['Itm_Medical', 'Itm_SALT', 'Itm_Mortgage', 'Itm_Charity'],
    'Credit_Profiles':         ['Cr_CTC', 'Cr_Education', 'Cr_FTC'],
    'Payment_Profiles':        ['Pmt_Withholding', 'Pmt_EstTax'],
}
col = 1
for header, items in bucket_profiles.items():
    c = ws.cell(row=16, column=col, value=header)
    c.font = HDR_FONT; c.fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=17 + i, column=col, value=v)
    last_row = 16 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$17:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

# Per-bucket Source_Document lists
ws.cell(row=30, column=1, value='▸ PER-BUCKET SOURCE_DOCUMENT LISTS').font = SUB_FONT
bucket_docs = {
    'BusinessIncome_Docs': ['K-1', 'P&L Statement', 'QuickBooks Export', 'Sch C Workpaper', 'Sch E Workpaper', 'Sch F Workpaper', 'PY Return'],
    'Wages_Docs':          ['W-2', 'Paystub Summary', 'S-Corp Officer Comp Wkpr'],
    'InvestmentIncome_Docs': ['1099-INT', '1099-DIV', 'Broker Year-End Stmt'],
    'CapitalGains_Docs':   ['1099-B', 'Settlement Statement', 'K-1 (passthrough)', '8949 detail'],
    'Adjustment_Docs':     ['HSA Stmt', 'IRA Receipt', 'Retirement Plan Stmt', '1098-E', 'SE Health Premium'],
    'Itemized_Docs':       ['Charity Receipts', '1098 Mortgage', 'Property Tax Receipt', 'Medical Receipts'],
    'Credit_Docs':         ['CTC Verification', '1098-T', 'FTC Workpaper'],
    'Payment_Docs':        ['Withholding Stmt', 'Est Tax Vouchers'],
}
col = 1
for header, items in bucket_docs.items():
    c = ws.cell(row=31, column=col, value=header)
    c.font = HDR_FONT; c.fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=32 + i, column=col, value=v)
    last_row = 31 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$32:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

widths(ws, [22] * 12)

# ============================================================
# Treatment_Profile_Map — folds Bucket + Tax_Line_Map into one lookup
# ============================================================
ws = wb.create_sheet('Treatment_Profile_Map')
ws['A1'] = 'TREATMENT PROFILE MAP — single source for derived columns'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Profile selection on input rows drives auto-fill of SE/NIIT/QBI/Primary_Line/Helper_Treatment/Consider_Prompt.'
ws['A2'].font = NOTE_FONT

cols = ['Profile', 'Bucket', 'SE_Subject', 'NIIT_Class', 'QBI_Eligible',
        'Primary_Line', 'Helper_Treatment', 'Consider_Prompt', 'Notes']
hdr(ws, 4, cols)

profiles = [
    # Profile,           Bucket,             SE,   NIIT,        QBI,  Line, Helper,        Consider_Prompt,                                Notes
    ('SchC_Active',       'Business Income',  'Yes','Active',    'Yes','10', 'SE_INCOME',   'SE earnings? owner draws separately tracked?', 'Sole prop active SE'),
    ('SchE_Rental',       'Business Income',  'No', 'Passive',   'No', '10', 'PASSIVE',     'short-term rental treatment? RE Pro election?','Rental real estate default passive'),
    ('SchE_REPro',        'Business Income',  'No', 'Active',    'No', '10', 'ACTIVE_RE',   'meets 750 hr / >50% test?',                    'RE Pro election makes rental active'),
    ('SchF_Active',       'Business Income',  'Yes','Active',    'Yes','10', 'SE_INCOME',   'SE earnings? farm income averaging?',          'Farm income SE subject'),
    ('K1_PTP_Active',     'Business Income',  'Yes','Active',    'Yes','10', 'K1_SPLIT',    'active vs passive? SE adjustments?',           'Active partnership K-1 (SE subject)'),
    ('K1_PTP_Passive',    'Business Income',  'No', 'Passive',   'Yes','10', 'K1_SPLIT',    'PAL limits? grouping election?',               'Passive partnership K-1'),
    ('K1_SCorp_Active',   'Business Income',  'No', 'Active',    'Yes','10', 'K1_SPLIT',    'active vs passive?',                           'Active S-Corp K-1 box 1'),
    ('K1_SCorp_Passive',  'Business Income',  'No', 'Passive',   'Yes','10', 'K1_SPLIT',    'rare — confirm',                               'Passive S-Corp K-1 (uncommon)'),
    ('Trust_K1',          'Business Income',  'No', 'Portfolio', 'No', '10', 'TRUST_DIST',  'character of distribution? DNI components?',   'Trust K-1'),
    ('W2_Employee',       'Wages',            'No', 'Active',    'No', '1z', 'NONE',        '(n/a)',                                        'Standard W-2 wages'),
    ('W2_SCorpOwner',     'Wages',            'No', 'Active',    'No', '1z', 'OWNER_PAY',   'owner pay portion (S-corp owner)?',           'S-Corp owner reasonable comp — drives FICA double-burden box'),
    ('Int_Taxable',       'Investment Income','No', 'Portfolio', 'No', '2b', 'TAX_EXEMPT',  'tax-exempt portion?',                          'Taxable interest income'),
    ('Int_Exempt',        'Investment Income','No', 'N/A',       'No', '2a', 'NONE',        '(all exempt)',                                 'Tax-exempt interest (muni)'),
    ('Div_Qualified',     'Investment Income','No', 'Portfolio', 'No', '3b', 'QUAL_DIV',    'qualified dividend portion?',                  'Qualified dividends — stack with LTCG'),
    ('Div_Ordinary',      'Investment Income','No', 'Portfolio', 'No', '3b', 'QUAL_DIV',    'qualified dividend portion?',                  'Ordinary (non-qualified) dividends'),
    ('LTCG_Stock',        'Capital Gains',    'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'wash sales? carryover loss available?',        'Long-term capital gains on equities'),
    ('STCG_Stock',        'Capital Gains',    'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'wash sales? carryover loss available?',        'Short-term capital gains'),
    ('LTCG_RE',           'Capital Gains',    'No', 'Passive',   'No', '7',  'LTCG_SPLIT',  '§1250 unrecaptured portion? §1031 deferred?',  'Long-term cap gain on real estate'),
    ('Sec1250_Recap',     'Capital Gains',    'No', 'Passive',   'No', '7',  'SEC1250',     '(unrecaptured §1250 — capped at 25%)',         '§1250 unrecaptured depreciation recapture'),
    ('LTCG_K1_Passthrough','Capital Gains',   'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'character per K-1 box?',                       'Cap gain passed through K-1'),
    ('Adj_HSA',           'Adjustment',       'No', 'N/A',       'No', '10', 'HSA',         'family vs self limit? catch-up age?',          'HSA contribution adjustment'),
    ('Adj_IRA',           'Adjustment',       'No', 'N/A',       'No', '10', 'IRA',         'deductible portion? Roth conversion?',         'IRA contribution adjustment'),
    ('Adj_Retirement',    'Adjustment',       'No', 'N/A',       'No', '10', 'RETIREMENT',  'plan type? employer limit?',                   'Retirement plan contribution'),
    ('Adj_SEHealth',      'Adjustment',       'No', 'N/A',       'No', '10', 'SE_HEALTH',   'SE earnings cap? spouse plan available?',      'SE health insurance deduction'),
    ('Adj_StudentLoan',   'Adjustment',       'No', 'N/A',       'No', '10', 'STUDENT_LOAN','MAGI phase-out check?',                        'Student loan interest deduction'),
    ('Itm_Medical',       'Itemized',         'No', 'N/A',       'No', '12', 'MEDICAL',     '7.5% AGI floor',                               'Medical expenses (Sch A)'),
    ('Itm_SALT',          'Itemized',         'No', 'N/A',       'No', '12', 'SALT',        '$10K cap (current law)',                       'State and local taxes (Sch A)'),
    ('Itm_Mortgage',      'Itemized',         'No', 'N/A',       'No', '12', 'MORTGAGE',    'principal cap by date',                        'Mortgage interest (Sch A)'),
    ('Itm_Charity',       'Itemized',         'No', 'N/A',       'No', '12', 'CHARITY',     '60% AGI cap; DAF bunching?',                   'Charitable contributions (Sch A)'),
    ('Cr_CTC',            'Credit',           'No', 'N/A',       'No', '19', 'CTC',         'children under 17? phase-out by AGI?',         'Child Tax Credit'),
    ('Cr_Education',      'Credit',           'No', 'N/A',       'No', '20', 'EDUCATION',   'AOTC vs LLC? phase-out?',                      'Education credits'),
    ('Cr_FTC',            'Credit',           'No', 'N/A',       'No', '20', 'FTC',         'Form 1116 required?',                          'Foreign tax credit'),
    ('Pmt_Withholding',   'Payment',          'No', 'N/A',       'No', '25', 'NONE',        '(n/a)',                                        'W-2/1099 withholding'),
    ('Pmt_EstTax',        'Payment',          'No', 'N/A',       'No', '26', 'NONE',        'safe harbor met?',                             'Quarterly estimated tax'),
]
for i, row in enumerate(profiles):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)
tbl_ref = f'A4:{get_column_letter(len(cols))}{4+len(profiles)}'
tbl = Table(displayName='tblTreatmentProfileMap', ref=tbl_ref)
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)
widths(ws, [22, 18, 11, 12, 13, 11, 18, 50, 45])

# ============================================================
# Tax_Brackets
# ============================================================
ws = wb.create_sheet('Tax_Brackets')
ws['A1'] = 'TAX BRACKETS & CONSTANTS — 2024 & 2025'
ws['A1'].font = TITLE_FONT

ws['A3'] = '2025 ORDINARY — Single'; ws['A3'].font = SUB_FONT
ws['G3'] = '2025 ORDINARY — MFJ';    ws['G3'].font = SUB_FONT
hdr(ws, 4, ['Rate', 'Low', 'High'])
hdr(ws, 4, ['Rate', 'Low', 'High'], start_col=7)
ord_s = [(0.10,0,11925),(0.12,11925,48475),(0.22,48475,103350),(0.24,103350,197300),(0.32,197300,250525),(0.35,250525,626350),(0.37,626350,99999999)]
ord_m = [(0.10,0,23850),(0.12,23850,96950),(0.22,96950,206700),(0.24,206700,394600),(0.32,394600,501050),(0.35,501050,751600),(0.37,751600,99999999)]
for i,(rt,lo,hi) in enumerate(ord_s):
    ws.cell(row=5+i, column=1, value=rt).number_format = '0.00%'
    ws.cell(row=5+i, column=2, value=lo); ws.cell(row=5+i, column=3, value=hi)
for i,(rt,lo,hi) in enumerate(ord_m):
    ws.cell(row=5+i, column=7, value=rt).number_format = '0.00%'
    ws.cell(row=5+i, column=8, value=lo); ws.cell(row=5+i, column=9, value=hi)

ws['A16'] = '2025 LTCG — Single'; ws['A16'].font = SUB_FONT
ws['E16'] = '2025 LTCG — MFJ';    ws['E16'].font = SUB_FONT
hdr(ws, 17, ['Rate', 'Low', 'High'])
hdr(ws, 17, ['Rate', 'Low', 'High'], start_col=5)
ltcg_s = [(0.00,0,48350),(0.15,48350,533400),(0.20,533400,99999999)]
ltcg_m = [(0.00,0,96700),(0.15,96700,600050),(0.20,600050,99999999)]
for i,(rt,lo,hi) in enumerate(ltcg_s):
    ws.cell(row=18+i, column=1, value=rt).number_format = '0.00%'
    ws.cell(row=18+i, column=2, value=lo); ws.cell(row=18+i, column=3, value=hi)
for i,(rt,lo,hi) in enumerate(ltcg_m):
    ws.cell(row=18+i, column=5, value=rt).number_format = '0.00%'
    ws.cell(row=18+i, column=6, value=lo); ws.cell(row=18+i, column=7, value=hi)

ws['A23'] = 'STANDARD DEDUCTIONS'; ws['A23'].font = SUB_FONT
hdr(ws, 24, ['Year', 'Single', 'MFJ', 'MFS', 'HOH'])
ws['A25'], ws['B25'], ws['C25'], ws['D25'], ws['E25'] = 2024, 14600, 29200, 14600, 21900
ws['A26'], ws['B26'], ws['C26'], ws['D26'], ws['E26'] = 2025, 15000, 30000, 15000, 22500

ws['A29'] = 'NIIT / SE / FICA CONSTANTS (2025)'; ws['A29'].font = SUB_FONT
consts = [
    ('NIIT_THRESH_MFJ', 250000, 'NIIT $250K threshold (MFJ)'),
    ('NIIT_THRESH_S', 200000, 'NIIT $200K threshold (Single/HOH)'),
    ('NIIT_THRESH_MFS', 125000, 'NIIT $125K threshold (MFS)'),
    ('NIIT_RATE', 0.038, '3.8% NIIT rate'),
    ('SS_WAGE_BASE_2025', 176100, 'Social Security wage base 2025'),
    ('SE_BASE_MULT', 0.9235, 'SE base multiplier'),
    ('SE_SS_RATE', 0.124, 'SE SS rate 12.4%'),
    ('SE_MED_RATE', 0.029, 'SE Medicare rate 2.9%'),
    ('FICA_SS_RATE_EE', 0.062, 'Employee SS rate'),
    ('FICA_SS_RATE_ER', 0.062, 'Employer SS rate'),
    ('FICA_MED_RATE_EE', 0.0145, 'Employee Medicare rate'),
    ('FICA_MED_RATE_ER', 0.0145, 'Employer Medicare rate'),
    ('ADDL_MED_RATE', 0.009, 'Additional Medicare 0.9%'),
    ('ADDL_MED_THRESH_MFJ', 250000, 'Addl Medicare MFJ threshold'),
    ('ADDL_MED_THRESH_S', 200000, 'Addl Medicare Single threshold'),
    ('EBL_LIMIT_MFJ', 626000, 'Excess Business Loss MFJ'),
    ('EBL_LIMIT_S', 313000, 'Excess Business Loss Single'),
]
for i, (name, val, note) in enumerate(consts):
    r = 30 + i
    ws.cell(row=r, column=1, value=name).font = Font(bold=True)
    ws.cell(row=r, column=2, value=val)
    ws.cell(row=r, column=3, value=note).font = NOTE_FONT
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Tax_Brackets'!$B${r}")

widths(ws, [22, 14, 12, 3, 22, 14, 12, 22, 14, 12])

# ============================================================
# Master_Inputs — long-format store with Cedillo Y2024 sample data
# ============================================================
ws = wb.create_sheet('Master_Inputs')
ws['A1'] = 'MASTER INPUTS — long-format store (auto-synced from year sheets)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Yellow cells = preparer input.  Gray cells = derived (formula).  Cedillo Y2024 sample rows tie to $7,213.92 federal tax.'
ws['A2'].font = NOTE_FONT

input_cols = ['InputID', 'Year', 'Scenario', 'ClientID', 'ClientName',
              'Bucket', 'Treatment_Profile', 'Source_Document',
              'Source_Layer', 'Status', 'Provenance',
              'Payor', 'Baseline_Amount', 'Helper_Amount', 'Adjustment_Amount',
              'Consider', 'Notes']
derived_cols = ['SE_Subject', 'NIIT_Class', 'QBI_Eligible',
                'Primary_Line', 'Helper_Treatment', 'Consider_Prompt']
audit_cols = ['LastUpdated', 'UpdatedBy', 'ReviewStatus']
all_cols = input_cols + derived_cols + audit_cols

hdr(ws, 4, all_cols)

# Color-code the header strip: input=yellow, derived=gray, audit=blue
for i, c in enumerate(all_cols):
    cell = ws.cell(row=3, column=1 + i)
    if c in input_cols:
        cell.value = 'INPUT'
        cell.fill = INPUT_FILL
    elif c in derived_cols:
        cell.value = 'DERIVED'
        cell.fill = DERIVED_FILL
    else:
        cell.value = 'AUDIT'
        cell.fill = KEY_FILL
    cell.font = Font(size=8, italic=True, color='595959')
    cell.alignment = Alignment(horizontal='center')

sample = [
    # Cedillo 2024 baseline rows
    ['CEDILLO|2024|Wages|W2_SCorpOwner|01', 2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Wages', 'W2_SCorpOwner', 'W-2',
     'Baseline', 'Approved', 'PBC - Reviewed',
     'Acme S-Corp', 153648, 0, 0,
     'Owner reasonable comp — full $153,648 treated as OWNER_PAY for FICA box', ''],
    ['CEDILLO|2024|BI|K1_PTP_Passive|01', 2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Business Income', 'K1_PTP_Passive', 'K-1',
     'Baseline', 'Approved', 'PBC - Reviewed',
     'Cedillo Partnership', -100766, 0, 0,
     'Passive loss', ''],
    ['CEDILLO|2024|II|Div_Ordinary|01', 2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Investment Income', 'Div_Ordinary', '1099-DIV',
     'Baseline', 'Approved', 'PBC - Reviewed',
     'Brokerage', 25922, 0, 0,
     'All non-qualified', ''],
    ['CEDILLO|2024|CG|LTCG_Stock|01', 2024, 'AsFiled', 'CEDILLO', 'Ron Cedillo',
     'Capital Gains', 'LTCG_Stock', '1099-B',
     'Baseline', 'Approved', 'PBC - Reviewed',
     'Brokerage', 14487, 0, 0,
     'Long-term, stacks below MFJ 0% threshold', ''],
    # Y2025 sample rows for SAMPLE client
    ['SAMPLE|2025|Wages|W2_SCorpOwner|01', 2025, 'S1', 'SAMPLE', 'Sample Client',
     'Wages', 'W2_SCorpOwner', 'W-2',
     'Baseline', 'Approved', 'Estimate - Preparer',
     'SampleCo S-Corp', 100000, 0, -25000,
     'Adjustment -$25K from S-Corp salary reduction strategy', ''],
    ['SAMPLE|2025|II|Div_Ordinary|01', 2025, 'S1', 'SAMPLE', 'Sample Client',
     'Investment Income', 'Div_Ordinary', '1099-DIV',
     'Baseline', 'Approved', 'Estimate - Preparer',
     'Brokerage', 10000, 7000, 0,
     'Helper = $7K qualified portion (Box 1b)', ''],
    # Strategy row that has been Committed (Source_Layer = Tax Strategy)
    ['SAMPLE|2025|Strategy|HSA-Family-Max|S1', 2025, 'S1', 'SAMPLE', 'Sample Client',
     'Adjustment', 'Adj_HSA', 'HSA Stmt',
     'Tax Strategy', 'Committed', 'Estimate - Preparer',
     '', -8550, 0, 0,
     'Family HSA max for 2025', ''],
]

for i, row_inputs in enumerate(sample):
    r = 5 + i
    # Write input columns
    for j, v in enumerate(row_inputs):
        cell = ws.cell(row=r, column=1 + j, value=v)
        if j > 0:  # InputID is computed in real workbook but stored here for the sample
            cell.fill = INPUT_FILL if all_cols[j] in input_cols else cell.fill

# Add DERIVED formula columns (looked up against Treatment_Profile_Map)
# Treatment_Profile is column G (index 7). Year=2024, Bucket=F, Treatment_Profile=G.
n_input = len(input_cols)
for i in range(len(sample)):
    r = 5 + i
    profile_cell = f'G{r}'  # Treatment_Profile column
    # SE_Subject
    ws.cell(row=r, column=n_input+1, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[SE_Subject]), "")').fill = DERIVED_FILL
    # NIIT_Class
    ws.cell(row=r, column=n_input+2, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[NIIT_Class]), "")').fill = DERIVED_FILL
    # QBI_Eligible
    ws.cell(row=r, column=n_input+3, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[QBI_Eligible]), "")').fill = DERIVED_FILL
    # Primary_Line
    ws.cell(row=r, column=n_input+4, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Primary_Line]), "")').fill = DERIVED_FILL
    # Helper_Treatment
    ws.cell(row=r, column=n_input+5, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Helper_Treatment]), "")').fill = DERIVED_FILL
    # Consider_Prompt
    ws.cell(row=r, column=n_input+6, value=f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Consider_Prompt]), "")').fill = DERIVED_FILL
    # Audit cols
    ws.cell(row=r, column=n_input+7, value='2026-05-18').fill = KEY_FILL
    ws.cell(row=r, column=n_input+8, value='SMJ').fill = KEY_FILL
    ws.cell(row=r, column=n_input+9, value='Approved').fill = KEY_FILL

# Convert to Excel Table
last_row = 4 + len(sample)
last_col = get_column_letter(len(all_cols))
tbl = Table(displayName='tblMaster_Inputs', ref=f'A4:{last_col}{last_row}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

# Data validation — cascading dropdowns via INDIRECT
# Bucket dropdown
dv_bucket = DataValidation(type='list', formula1='=Bucket', allow_blank=True); ws.add_data_validation(dv_bucket); dv_bucket.add('F5:F1000')
# Treatment_Profile dropdown — cascading based on Bucket
dv_profile = DataValidation(type='list', formula1='=INDIRECT(SUBSTITUTE($F5," ","")&"_Profiles")', allow_blank=True); ws.add_data_validation(dv_profile); dv_profile.add('G5:G1000')
# Source_Document dropdown — cascading based on Bucket
dv_doc = DataValidation(type='list', formula1='=INDIRECT(SUBSTITUTE($F5," ","")&"_Docs")', allow_blank=True); ws.add_data_validation(dv_doc); dv_doc.add('H5:H1000')
# Source_Layer
dv_layer = DataValidation(type='list', formula1='=Source_Layer', allow_blank=True); ws.add_data_validation(dv_layer); dv_layer.add('I5:I1000')
# Status
dv_status = DataValidation(type='list', formula1='=Status', allow_blank=True); ws.add_data_validation(dv_status); dv_status.add('J5:J1000')
# Scenario
dv_scen = DataValidation(type='list', formula1='=Scenario', allow_blank=True); ws.add_data_validation(dv_scen); dv_scen.add('C5:C1000')
# Provenance
dv_prov = DataValidation(type='list', formula1='=Provenance', allow_blank=True); ws.add_data_validation(dv_prov); dv_prov.add('K5:K1000')

widths(ws, [40, 7, 11, 11, 18, 18, 22, 18, 14, 14, 18, 18, 14, 14, 14, 30, 22,
            11, 12, 13, 11, 18, 50, 12, 12, 14])

# ============================================================
# Strategies_Library — with Buckets_Impacted
# ============================================================
ws = wb.create_sheet('Strategies_Library')
ws['A1'] = 'TAX PLANNING STRATEGIES — library / catalog'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Year-sheet strategies tables draw from this list. Buckets_Impacted column drives "which strategies apply to this client" filtering.'
ws['A2'].font = NOTE_FONT

hdr(ws, 4, ['ID', 'Group', 'Strategy Name', 'Description', 'Buckets_Impacted', 'Impact Type', 'Complexity', 'Tax Lines Affected', 'Est. Savings', 'Notes'])
strategies = [
    ('STD-001', 'Low Hanging Fruit', 'Retirement Plan Contributions', 'Solo 401k, SEP IRA, or Cash Balance contributions', 'Adjustment', 'Single', 'Low',    'Line 10 (Non-SE) ↓', None, ''),
    ('STD-002', 'Low Hanging Fruit', 'Augusta Rule',                  'Business rents owner home ≤14 days; IRC §280A(g) excludes rental from owner income — business gets deduction, owner reports nothing', 'Business Income', 'Single', 'Low', 'Line 10 (Non-SE) ↓', None, 'Pure business-side deduction; owner side has no income recognition'),
    ('STD-003', 'Low Hanging Fruit', 'Accountable Plan',              'Reimburse business expenses tax-free',             'Business Income', 'Single', 'Low', 'Line 10 (Non-SE) ↑', None, ''),
    ('STD-004', 'Low Hanging Fruit', 'Employee Health/Fringe Benefits','Health/fringe benefits through business',         'Business Income, Adjustment', 'Single', 'Low', 'Line 10 ↑', None, ''),
    ('STD-005', 'Low Hanging Fruit', 'Hiring Children',               'Pay children for legitimate work in business',     'Wages, Business Income', 'Single', 'Medium', 'Line 1 ↑, Line 10 ↑', None, ''),
    ('STD-006', 'Low Hanging Fruit', 'Income Timing',                 'Defer/accelerate income between tax years',        'Various', 'Single', 'Low', 'Various', None, ''),
    ('STD-007', 'SE Tax',            'Entity Restructure (S-Corp)',   'Convert Sch C to S-Corp for wage/distribution split','Wages, Business Income', 'Multi', 'High', 'Line 1 ↑, Line 10 ↑, SE ↓', None, ''),
    ('STD-008', 'SE Tax',            'Wage Optimization',             'Optimize S-Corp salary for SE tax vs QBI',         'Wages, Business Income', 'Multi', 'Medium', 'Line 1, Line 10', None, 'S-Corp owner wage box impact'),
    ('STD-009', 'Cap Gain',          '1031 Exchange',                 'Defer gains on real estate sale',                  'Capital Gains', 'Single', 'High', 'Line 7 (LTCG) ↓', None, ''),
    ('STD-010', 'Cap Gain',          'Opportunity Zone',              'Invest gains in OZ for deferral/exclusion',        'Capital Gains', 'Single', 'High', 'Line 7 (LTCG) ↓', None, ''),
    ('STD-011', 'Cap Gain',          'Tax Loss Harvesting',           'Sell losers to offset gains',                      'Capital Gains', 'Single', 'Medium', 'Line 7 ↓', None, ''),
    ('STD-012', 'CRE',               'Cost Segregation',              'Accelerate depreciation via cost seg study',       'Business Income', 'Single', 'High', 'Line 10 ↓', None, ''),
    ('STD-013', 'CRE',               'RE Professional Election',      'Convert passive to active for loss utilization',   'Business Income', 'Multi', 'High', 'Line 14 → Line 10', None, ''),
    ('STD-014', 'CRE',               'Section 179 Expensing',         'Immediate expense vs depreciation',                'Business Income', 'Single', 'Medium', 'Line 10 ↓', None, ''),
    ('ADV-001', 'Advanced',          'Cash Balance Plan',             'Defined benefit plan for high earners',            'Adjustment', 'Single', 'High', 'Line 10 ↓', None, ''),
    ('ADV-002', 'Advanced',          'Charitable Strategies',         'CRUT, CRAT, DAF for charitable deductions',        'Itemized', 'Single', 'High', 'Line 12 ↑', None, ''),
    ('ADV-003', 'Advanced',          'QBI Optimization',              'Grouping and aggregation elections',               'Business Income', 'Computed', 'High', 'QBI Deduction', None, ''),
    ('ADV-004', 'Advanced',          'Roth Conversion',               'Convert traditional IRA → Roth at lower bracket',  'Investment Income, Adjustment', 'Multi', 'High', 'Line 4b ↑, future Roth tax-free', None, ''),
    ('ADV-005', 'Advanced',          'NOL Planning',                  'Time / utilize Net Operating Losses',              'Business Income', 'Multi', 'High', 'Line 10', None, ''),
    ('ADV-006', 'Advanced',          'Installment Sale',              'Spread gain across multiple years',                'Capital Gains', 'Multi', 'Medium', 'Line 7 over years', None, ''),
]
for i, s in enumerate(strategies):
    for j, v in enumerate(s):
        ws.cell(row=5 + i, column=1 + j, value=v)
tbl = Table(displayName='tblStrategies_Library', ref=f'A4:J{4+len(strategies)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)
widths(ws, [10, 18, 32, 50, 32, 12, 12, 30, 12, 28])

# ============================================================
# Y2025_Sample — KISS year sheet (full pattern)
# ============================================================
ws = wb.create_sheet('Y2025_Sample')
ws['A1'] = 'Y2025 — sample year sheet (KISS pattern)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'LEFT (A:Q) = bucket-pattern input table.  RIGHT (S:AG) = rollup + LAMBDA calc + planning strategies + True Tax Burden.'
ws['A2'].font = NOTE_FONT
ws['A3'] = 'Yellow = preparer input; Gray = derived formula; Blue = key/dropdown.'
ws['A3'].font = NOTE_FONT

# LEFT: input table — ALL rows (Baseline, Adjustment, Tax Strategy) in one table
ws['A5'] = 'INPUTS — tblY2025_Inputs  (one table for Baseline + Adjustment + Tax Strategy; distinguished by Source_Layer + Status)'
ws['A5'].font = SUB_FONT
yi_input_cols = ['Source_ID', 'Bucket', 'Treatment_Profile', 'Source_Document',
                 'Source_Layer', 'Status', 'Payor',
                 'Baseline_Amount', 'Helper_Amount', 'Adjustment_Amount', 'Consider',
                 'Provenance', 'Notes']
yi_derived_cols = ['SE_Subject', 'NIIT_Class', 'QBI_Eligible', 'Primary_Line', 'Helper_Treatment', 'Consider_Prompt']
all_yi = yi_input_cols + yi_derived_cols
hdr(ws, 6, all_yi)

# Sample rows — mix of Baseline + Tax Strategy at various Status levels
yi_data = [
    # Baseline source rows
    ['Y25-001', 'Wages',             'W2_SCorpOwner',  'W-2',      'Baseline',     'Approved',  'SampleCo S-Corp',     100000, 100000, 0, 'Owner reasonable comp',     'Estimate - Preparer',  ''],
    ['Y25-002', 'Business Income',   'K1_SCorp_Active','K-1',      'Baseline',     'Approved',  'SampleCo S-Corp K-1', 200000, 0, 0, 'Active S-corp K-1',           'PY Rolled Forward',    ''],
    ['Y25-003', 'Investment Income', 'Div_Qualified',  '1099-DIV', 'Baseline',     'Approved',  'Brokerage',           10000,  7000, 0, '$7K qualified portion',       'PBC - Received',       ''],
    ['Y25-004', 'Capital Gains',     'LTCG_Stock',     '1099-B',   'Baseline',     'Approved',  'Brokerage',           25000,  0,    0, 'All long-term',               'PBC - Requested',      ''],
    # Tax Strategy rows — only Committed/Implemented flow into Σ Strat
    ['STR-001', 'Wages',             'W2_SCorpOwner',  '',         'Tax Strategy', 'Committed', 'SampleCo S-Corp',     -25000, -25000, 0, 'S-Corp salary reduction',    'Estimate - Preparer',  'STD-008 Wage Optimization'],
    ['STR-002', 'Adjustment',        'Adj_HSA',        'HSA Stmt', 'Tax Strategy', 'Committed', '',                    -8550,  0,    0, 'Family HSA max for 2025',     'Estimate - Preparer',  'STD-001 Retirement (HSA)'],
    ['STR-003', 'Itemized',          'Itm_Charity',    '',         'Tax Strategy', 'Proposed',  '',                    15000,  0,    0, 'DAF stack for bunching',      'Estimate - Preparer',  'ADV-002 — excluded from Σ Strat (Proposed)'],
    ['STR-004', 'Business Income',   'SchE_Rental',    '',         'Tax Strategy', 'Approved',  '',                    -80000, 0,    0, 'Cost Seg study',              'Estimate - Preparer',  'STD-012 — excluded from Σ Strat (Approved, not Committed)'],
]
for i, row in enumerate(yi_data):
    r = 7 + i
    for j, v in enumerate(row):
        c = ws.cell(row=r, column=1 + j, value=v)
        c.fill = INPUT_FILL
    # Derived columns
    profile_cell = f'C{r}'
    base = len(yi_input_cols)
    formulas = [
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[SE_Subject]), "")',
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[NIIT_Class]), "")',
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[QBI_Eligible]), "")',
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Primary_Line]), "")',
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Helper_Treatment]), "")',
        f'=IFERROR(XLOOKUP({profile_cell}, tblTreatmentProfileMap[Profile], tblTreatmentProfileMap[Consider_Prompt]), "")',
    ]
    for k, f in enumerate(formulas):
        cc = ws.cell(row=r, column=base + 1 + k, value=f)
        cc.fill = DERIVED_FILL

# Convert to Excel Table
tbl = Table(displayName='tblY2025_Inputs', ref=f'A6:{get_column_letter(len(all_yi))}{6+len(yi_data)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

# Cascading dropdowns on year-sheet table
dv1 = DataValidation(type='list', formula1='=Bucket', allow_blank=True); ws.add_data_validation(dv1); dv1.add('B7:B200')
dv2 = DataValidation(type='list', formula1='=INDIRECT(SUBSTITUTE($B7," ","")&"_Profiles")', allow_blank=True); ws.add_data_validation(dv2); dv2.add('C7:C200')
dv3 = DataValidation(type='list', formula1='=INDIRECT(SUBSTITUTE($B7," ","")&"_Docs")', allow_blank=True); ws.add_data_validation(dv3); dv3.add('D7:D200')
dv_layer = DataValidation(type='list', formula1='=Source_Layer', allow_blank=True); ws.add_data_validation(dv_layer); dv_layer.add('E7:E200')
dv_status = DataValidation(type='list', formula1='=Status', allow_blank=True); ws.add_data_validation(dv_status); dv_status.add('F7:F200')
dv4 = DataValidation(type='list', formula1='=Provenance', allow_blank=True); ws.add_data_validation(dv4); dv4.add('L7:L200')

# RIGHT side: TAX ROLLUP (col S onwards)
ws.cell(row=5, column=19, value='TAX ROLLUP (S:AC)').font = SUB_FONT
ru_cols = ['Line', 'Description', 'Baseline', 'Σ Adj', 'Σ Strat', 'Total (Effective)']
hdr(ws, 6, ru_cols, start_col=19)
ru_lines = [
    ('1z', 'Wages'),
    ('2a', 'Tax-exempt interest'),
    ('2b', 'Taxable interest'),
    ('3a', 'Qualified dividends'),
    ('3b', 'Ordinary dividends (total)'),
    ('7',  'Capital gain or (loss)'),
    ('8',  'Other income (Sch 1)'),
    ('9',  'TOTAL INCOME'),
    ('10', 'Adjustments to income'),
    ('11', 'AGI'),
    ('12', 'Std/Itemized deduction'),
    ('13', 'QBI deduction'),
    ('15', 'TAXABLE INCOME'),
]
for i, (line, desc) in enumerate(ru_lines):
    r = 7 + i
    ws.cell(row=r, column=19, value=line)
    ws.cell(row=r, column=20, value=desc)
    # Baseline = SUMIFS of input table Baseline_Amount, filtered to Source_Layer="Baseline" + Primary_Line=line
    ws.cell(row=r, column=21, value=f'=SUMIFS(tblY2025_Inputs[Baseline_Amount], tblY2025_Inputs[Primary_Line], $S{r}, tblY2025_Inputs[Source_Layer], "Baseline")')
    # Σ Adj = SUMIFS of Adjustment_Amount where Primary_Line = line (revisions live ON baseline rows)
    ws.cell(row=r, column=22, value=f'=SUMIFS(tblY2025_Inputs[Adjustment_Amount], tblY2025_Inputs[Primary_Line], $S{r})')
    # Σ Strat = SUMIFS of Baseline_Amount where Source_Layer="Tax Strategy" + Status IN (Committed, Implemented) + Primary_Line=line
    ws.cell(row=r, column=23, value=f'=SUMIFS(tblY2025_Inputs[Baseline_Amount], tblY2025_Inputs[Primary_Line], $S{r}, tblY2025_Inputs[Source_Layer], "Tax Strategy", tblY2025_Inputs[Status], "Committed") + SUMIFS(tblY2025_Inputs[Baseline_Amount], tblY2025_Inputs[Primary_Line], $S{r}, tblY2025_Inputs[Source_Layer], "Tax Strategy", tblY2025_Inputs[Status], "Implemented")')
    # Total
    ws.cell(row=r, column=24, value=f'=U{r}+V{r}+IF(Include_Strategies, W{r}, 0)')

# TAX COMPUTATION block
ws.cell(row=21, column=19, value='TAX COMPUTATION (1040)').font = SUB_FONT
ws.cell(row=22, column=19, value='Component').font = HDR_FONT; ws.cell(row=22, column=19).fill = HDR_FILL
ws.cell(row=22, column=20, value='LAMBDA signature').font = HDR_FONT; ws.cell(row=22, column=20).fill = HDR_FILL
ws.cell(row=22, column=21, value='Amount').font = HDR_FONT; ws.cell(row=22, column=21).fill = HDR_FILL

tax_calc = [
    ('Ord Tax',         'Calc_OrdinaryTax(Taxable_Income_S1, FilingStatus)',                '=0  (replace with LAMBDA)'),
    ('LTCG Tax',        'Calc_CapGainsTax(LTCG_S1, OrdIncome_S1, FilingStatus)',            '=0'),
    ('SE Tax',          'Calc_SE_Tax(SE_Income_S1, W2_S1, FilingStatus)',                   '=0'),
    ('NIIT',            'Calc_NIIT(MAGI_S1, NII_S1, FilingStatus)',                         '=0'),
    ('Addl Medicare',   'AddlMedicareTax_FN(W2_S1, SE_Income_S1, FilingStatus)',            '=0'),
    ('TOTAL FED TAX',   'SUM of above (Form 1040 line 24)',                                 '=SUM(U23:U27)'),
]
for i, (label, sig, val) in enumerate(tax_calc):
    r = 23 + i
    ws.cell(row=r, column=19, value=label).font = Font(bold='TOTAL' in label)
    ws.cell(row=r, column=20, value=sig).font = NOTE_FONT
    ws.cell(row=r, column=21, value=val)

# TRUE TAX BURDEN box — separate from 1040
ws.cell(row=30, column=19, value='▸ TRUE TAX BURDEN (1040 + FICA on owner W-2)').font = SUB_FONT
true_burden = [
    ('Owner W-2 Wages',     '=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "OWNER_PAY", tblY2025_Inputs[Source_Layer], "Baseline")',
                            '(Helper_Amount on Baseline rows where Helper_Treatment = OWNER_PAY)'),
    ('FICA Employer Share', '=0  (replace with =FICA_EmployerTax_FN(U31))',
                            'SS 6.2% + Medicare 1.45% on owner W-2'),
    ('FICA Employee Share', '=0  (replace with =FICA_EmployeeTax_FN(U31))',
                            'Same rates, employee side — already withheld on W-2 but reflects true cost'),
    ('TOTAL ADDITIONAL',    '=U32+U33',                                                          'Employer + Employee FICA on owner W-2'),
    ('TOTAL FED TAX (1040)','=U28',                                                              ''),
    ('TRUE TAX BURDEN',     '=U35+U34',                                                          '1040 tax + double FICA on owner pay'),
]
for i, (label, val, note) in enumerate(true_burden):
    r = 31 + i
    ws.cell(row=r, column=19, value=label).font = Font(bold='TRUE' in label or 'TOTAL' in label)
    ws.cell(row=r, column=21, value=val)
    ws.cell(row=r, column=22, value=note).font = NOTE_FONT

# Strategies are now rows in tblY2025_Inputs above (Source_Layer = "Tax Strategy").
# No separate table needed — Status column drives lifecycle, only Committed/Implemented flow into Σ Strat in the rollup.
ws.cell(row=40, column=19, value='▸ STRATEGIES ARE IN tblY2025_Inputs (Source_Layer = "Tax Strategy")').font = SUB_FONT
ws.cell(row=41, column=19, value='Filter the input table by Source_Layer = "Tax Strategy" to see only strategies.').font = NOTE_FONT
ws.cell(row=42, column=19, value='Status drives lifecycle: Proposed → Approved → Committed → Implemented → Converted_To_Input.').font = NOTE_FONT
ws.cell(row=43, column=19, value='Only Committed and Implemented rows flow into the Σ Strat column of the rollup.').font = NOTE_FONT
ws.cell(row=44, column=19, value='Once Converted_To_Input, the row is treated as a regular Baseline (it has become a fact).').font = NOTE_FONT

# INTEGRITY CHECK block
ws.cell(row=50, column=19, value='▸ INTEGRITY CHECK — year-sheet calc vs. master-pivot calc').font = SUB_FONT
ws.cell(row=51, column=19, value='Year-sheet TOTAL FED TAX').font = Font(bold=True)
ws.cell(row=51, column=21, value='=U28')
ws.cell(row=52, column=19, value='Master pivot for (Y=2025, Scenario=S1)').font = Font(bold=True)
ws.cell(row=52, column=21, value='= placeholder — see Tax_Summary for the GROUPBY')
ws.cell(row=53, column=19, value='Variance (must be 0)').font = Font(bold=True)
ws.cell(row=53, column=21, value='=U51-IFERROR(U52,0)')

# Column widths
for col_letter, w in zip(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
                          [12,18,22,18,18,14,14,14,18,18,30,11,12,13,11,18,50]):
    ws.column_dimensions[col_letter].width = w
for col_letter, w in zip(['S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG'],
                          [10,32,14,12,12,14,14,12,12,14,14,12,12,12,12]):
    ws.column_dimensions[col_letter].width = w

# ============================================================
# Tax_Summary — GROUPBY-driven cross-year view
# ============================================================
ws = wb.create_sheet('Tax_Summary')
ws['A1'] = 'TAX SUMMARY — cross-year, GROUPBY-driven from Master_Inputs'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Reproduces the year-sheet rollup by pivoting Master_Inputs. Integrity check: year-sheet total must = pivot total.'
ws['A2'].font = NOTE_FONT

ws['A4'] = 'PATTERN 1 — GROUPBY (Excel 365)'.upper(); ws['A4'].font = SUB_FONT
ws['A5'] = '=GROUPBY( tblMaster_Inputs[[Year]:[Bucket]], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0 )'
ws['A5'].font = Font(name='Consolas', size=10)

ws['A7'] = 'PATTERN 2 — PIVOTBY (rows × columns)'; ws['A7'].font = SUB_FONT
ws['A8'] = '=PIVOTBY( tblMaster_Inputs[Bucket], tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 2 )'
ws['A8'].font = Font(name='Consolas', size=10)

ws['A10'] = 'PATTERN 3 — SUMIFS fallback (per Source_Layer breakdown)'; ws['A10'].font = SUB_FONT
ws['A11'] = '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], "Wages", tblMaster_Inputs[Source_Layer], "Baseline")'
ws['A11'].font = Font(name='Consolas', size=10)

ws['A13'] = 'CROSS-YEAR ROLLUP — Baseline + Adjustments + Strategies per Bucket'; ws['A13'].font = SUB_FONT
hdr(ws, 14, ['Bucket', '2024 Base', '2024 Adj', '2024 Strat', '2025 Base', '2025 Adj', '2025 Strat'])
buckets = ['Wages', 'Business Income', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment']
for i, b in enumerate(buckets):
    r = 15 + i
    ws.cell(row=r, column=1, value=b)
    ws.cell(row=r, column=2, value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2024, tblMaster_Inputs[Bucket], A{r}, tblMaster_Inputs[Source_Layer], "Baseline")')
    ws.cell(row=r, column=3, value=f'=SUMIFS(tblMaster_Inputs[Adjustment_Amount], tblMaster_Inputs[Year], 2024, tblMaster_Inputs[Bucket], A{r})')
    ws.cell(row=r, column=4, value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2024, tblMaster_Inputs[Bucket], A{r}, tblMaster_Inputs[Source_Layer], "Tax Strategy")')
    ws.cell(row=r, column=5, value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], A{r}, tblMaster_Inputs[Source_Layer], "Baseline")')
    ws.cell(row=r, column=6, value=f'=SUMIFS(tblMaster_Inputs[Adjustment_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], A{r})')
    ws.cell(row=r, column=7, value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], A{r}, tblMaster_Inputs[Source_Layer], "Tax Strategy")')

widths(ws, [22, 14, 14, 14, 14, 14, 14])

# ============================================================
# PBC_List — GROUPBY-driven
# ============================================================
ws = wb.create_sheet('PBC_List')
ws['A1'] = 'PBC CHECKLIST — auto-generated from Master_Inputs by Provenance + Source_Document'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Filters: Source_Layer = "Baseline" AND Provenance IN ("PBC - Requested", "PBC - Received", "PBC - Reviewed").'
ws['A2'].font = NOTE_FONT

ws['A4'] = 'GROUPBY pattern'; ws['A4'].font = SUB_FONT
ws['A5'] = '=GROUPBY(CHOOSECOLS(FILTER(tblMaster_Inputs, (tblMaster_Inputs[Year]=TaxYear)*(tblMaster_Inputs[Source_Layer]="Baseline")), 6, 8, 12), 1, COUNTA, 3, 0)'
ws['A5'].font = Font(name='Consolas', size=10)

ws['A7'] = 'EXAMPLE OUTPUT (with Provenance flag for status)'; ws['A7'].font = SUB_FONT
hdr(ws, 8, ['Status', 'Bucket', 'Source_Document', 'Payor', 'Provenance'])
pbc_rows = [
    ('[ ]', 'Wages',             'W-2',      'SampleCo S-Corp', 'PBC - Requested'),
    ('[ ]', 'Business Income',   'K-1',      'SampleCo S-Corp K-1', 'PY Rolled Forward'),
    ('[✓]', 'Investment Income', '1099-DIV', 'Brokerage', 'PBC - Received'),
    ('[ ]', 'Capital Gains',     '1099-B',   'Brokerage', 'PBC - Requested'),
]
for i, row in enumerate(pbc_rows):
    for j, v in enumerate(row):
        ws.cell(row=9 + i, column=1 + j, value=v)

widths(ws, [10, 22, 22, 28, 22])

# ============================================================
# Dashboard_Export — stable named-range block
# ============================================================
ws = wb.create_sheet('Dashboard_Export')
ws['A1'] = 'DASHBOARD EXPORT — stable named-range contract for Jeff/downstream consumers'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Downstream dashboards pull from these named ranges. Layout is the CONTRACT.'
ws['A2'].font = NOTE_FONT

ws['B4'] = 'METRIC'; ws['B4'].font = HDR_FONT; ws['B4'].fill = HDR_FILL
ws['C4'] = 'VALUE';  ws['C4'].font = HDR_FONT; ws['C4'].fill = HDR_FILL
ws['D4'] = 'NAMED RANGE'; ws['D4'].font = HDR_FONT; ws['D4'].fill = HDR_FILL

dash = [
    ('Active Tax Year',       '=TaxYear', 'Dashboard_TaxYear'),
    ('Filing Status',         '=FilingStatus', 'Dashboard_FilingStatus'),
    ('Total Income',          '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], TaxYear, tblMaster_Inputs[Source_Layer], "Baseline")', 'Dashboard_TotalIncome'),
    ('Total Adjustments',     '=SUMIFS(tblMaster_Inputs[Adjustment_Amount], tblMaster_Inputs[Year], TaxYear)', 'Dashboard_TotalAdj'),
    ('Total Strategies (committed)', '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], TaxYear, tblMaster_Inputs[Source_Layer], "Tax Strategy")', 'Dashboard_TotalStrat'),
    ('Effective Total',       '=Dashboard_TotalIncome + Dashboard_TotalAdj + IF(Include_Strategies, Dashboard_TotalStrat, 0)', 'Dashboard_EffectiveTotal'),
    ('Total Federal Tax',     'placeholder — wire to year-sheet U28 in real workbook', 'Dashboard_TotalFedTax'),
    ('True Tax Burden',       'placeholder — wire to year-sheet U36 in real workbook', 'Dashboard_TrueTaxBurden'),
]
for i, (label, formula, name) in enumerate(dash):
    r = 5 + i
    ws.cell(row=r, column=2, value=label).font = Font(bold=True)
    ws.cell(row=r, column=3, value=formula)
    ws.cell(row=r, column=4, value=name).font = NOTE_FONT
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Dashboard_Export'!$C${r}")

widths(ws, [3, 30, 70, 30])

# ============================================================
# PROJECTION_HISTORY
# ============================================================
ws = wb.create_sheet('PROJECTION_HISTORY')
ws['A1'] = 'PROJECTION HISTORY — snapshot archive / tie-out workpaper'
ws['A1'].font = TITLE_FONT
hdr(ws, 4, ['Year', 'Scenario', 'Line', 'Description', 'Projected', 'Filed', 'Variance $', 'Variance %', 'Accuracy Grade', 'Snapshot Date', 'Notes'])
example = [
    (2023, 'AsFiled', '1z', 'Wages',           105000, 108500, 3500, 0.0333, 'A', '2024-04-15', ''),
    (2023, 'AsFiled', '2b', 'Taxable interest', 8500,   8200,  -300, -0.0353,'A', '2024-04-15', ''),
    (2024, 'S1 Extension', '1z', 'Wages',     112000, None,  None, None,   None,'2024-04-15', 'Projected at extension'),
    (2025, 'S1', '1z', 'Wages',                75000, None,  None, None,   None, '2025-09-01', 'Post S-Corp salary reduction strategy'),
]
for i, row in enumerate(example):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)
widths(ws, [7, 18, 7, 28, 14, 12, 12, 12, 14, 14, 40])

# ============================================================
# Reorder sheets
# ============================================================
order = ['README', 'CONTROL_PANEL', 'Y2025_Sample', 'Master_Inputs',
         'Strategies_Library', 'Tax_Summary', 'PBC_List', 'Dashboard_Export',
         'PROJECTION_HISTORY', 'Treatment_Profile_Map', 'Tax_Brackets', 'Dropdown_Lists']
wb._sheets = [wb[name] for name in order]

wb.save(OUT)
print(f'Saved: {OUT}')
print(f'Sheets ({len(wb.sheetnames)}):')
for n in wb.sheetnames:
    print(f'  - {n}')
print(f'\nNamed ranges: {len(list(wb.defined_names))}')
