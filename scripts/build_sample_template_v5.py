"""Build v5 sample — master-first, minimal.

  Master_Inputs    — single-entry committed baseline rows (year-tagged).
  Y2025            — year sheet with a strategies schedule and a rollup:
                     Line | Desc | Baseline (from Master) | S1 (manual override)
                     | Strategies (from year-sheet table) | Effective | Drill
                     Plus Helper / Tax-Calc Inputs section (reference values
                     for future LAMBDAs that don't aggregate into income).
                     Plus FILTER-driven drill panel.
  Treatment_Profile_Map — lookup reference
  Dropdown_Lists   — closed sets + per-bucket cascade named ranges

Output: docs/Tax_Workbook_Sample_Template_v5.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.workbook.properties import CalcProperties

OUT = '/home/user/1040-Comprehnensive/docs/Tax_Workbook_Sample_Template_v5.xlsx'

wb = Workbook()
wb.remove(wb.active)
wb.calculation = CalcProperties(fullCalcOnLoad=True)

HDR_FONT = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
HDR_FILL = PatternFill('solid', fgColor='305496')
SUB_FONT = Font(name='Calibri', size=10, bold=True, color='305496')
TITLE_FONT = Font(name='Calibri', size=14, bold=True, color='305496')
NOTE_FONT = Font(name='Calibri', size=9, italic=True, color='595959')
INPUT_FILL = PatternFill('solid', fgColor='FFF2CC')
KEY_FILL = PatternFill('solid', fgColor='DDEBF7')

def hdr(ws, row, cols, start_col=1):
    for i, c in enumerate(cols):
        cell = ws.cell(row=row, column=start_col + i, value=c)
        cell.font = HDR_FONT
        cell.fill = HDR_FILL
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def add_dv(ws, letter, formula, start=5, end=500):
    dv = DataValidation(type='list', formula1=formula, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f'{letter}{start}:{letter}{end}')

# ============================================================
# Dropdown_Lists
# ============================================================
ws = wb.create_sheet('Dropdown_Lists')
ws['A1'] = 'DROPDOWN LISTS — top-level + per-bucket cascade named ranges'
ws['A1'].font = TITLE_FONT

top_lists = {
    'Bucket':       ['Business Income', 'Wages', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment'],
    'Yes_No':       ['Yes', 'No'],
    'NIIT_Class':   ['Active', 'Passive', 'Portfolio', 'N/A'],
    'Provenance':   ['PY Rolled Forward', 'PY Actuals', 'Estimate - Preparer', 'Estimate - Client',
                     'PBC - Requested', 'PBC - Received', 'PBC - Reviewed',
                     'Extraction - Imported', 'Extraction - Tied', 'System Calculated'],
    'Status':       ['Proposed', 'Approved', 'Committed', 'Implemented', 'Rejected'],
    'TaxLines':     ['1z', '2a', '2b', '3a', '3b', '7', '8', '10', '12', '13'],
}
col = 1
for header, items in top_lists.items():
    ws.cell(row=3, column=col, value=header).font = HDR_FONT
    ws.cell(row=3, column=col).fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=4 + i, column=col, value=v)
    last_row = 3 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$4:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

ws.cell(row=17, column=1, value='▸ PER-BUCKET TREATMENT_PROFILE LISTS').font = SUB_FONT
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
    ws.cell(row=18, column=col, value=header).font = HDR_FONT
    ws.cell(row=18, column=col).fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=19 + i, column=col, value=v)
    last_row = 18 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$19:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

ws.cell(row=33, column=1, value='▸ PER-BUCKET SOURCE_DOCUMENT LISTS').font = SUB_FONT
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
    ws.cell(row=34, column=col, value=header).font = HDR_FONT
    ws.cell(row=34, column=col).fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=35 + i, column=col, value=v)
    last_row = 34 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$35:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

widths(ws, [22] * 12)

# ============================================================
# Treatment_Profile_Map
# ============================================================
ws = wb.create_sheet('Treatment_Profile_Map')
ws['A1'] = 'TREATMENT PROFILE MAP — reference for the VBA hook that fills SE/NIIT/QBI/Primary_Line/Helper_Treatment'
ws['A1'].font = TITLE_FONT
tpm_cols = ['Profile', 'Bucket', 'SE_Subject', 'NIIT_Class', 'QBI_Eligible',
            'Primary_Line', 'Helper_Treatment', 'Consider_Prompt', 'Notes']
hdr(ws, 4, tpm_cols)
profiles = [
    ('SchC_Active',       'Business Income',  'Yes','Active',    'Yes','10', 'SE_INCOME',   'SE earnings?',                                 'Sole prop active SE'),
    ('SchE_Rental',       'Business Income',  'No', 'Passive',   'No', '10', 'PASSIVE',     'short-term rental? RE Pro election?',          'Rental real estate default passive'),
    ('SchE_REPro',        'Business Income',  'No', 'Active',    'No', '10', 'ACTIVE_RE',   'meets 750hr / >50% test?',                     'RE Pro election'),
    ('SchF_Active',       'Business Income',  'Yes','Active',    'Yes','10', 'SE_INCOME',   'farm income averaging?',                       'Farm income'),
    ('K1_PTP_Active',     'Business Income',  'Yes','Active',    'Yes','10', 'K1_SPLIT',    'active vs passive?',                           'Active partnership K-1'),
    ('K1_PTP_Passive',    'Business Income',  'No', 'Passive',   'Yes','10', 'K1_SPLIT',    'PAL limits?',                                  'Passive partnership K-1'),
    ('K1_SCorp_Active',   'Business Income',  'No', 'Active',    'Yes','10', 'K1_SPLIT',    'active vs passive?',                           'Active S-Corp K-1'),
    ('K1_SCorp_Passive',  'Business Income',  'No', 'Passive',   'Yes','10', 'K1_SPLIT',    'rare — confirm',                               'Passive S-Corp K-1'),
    ('Trust_K1',          'Business Income',  'No', 'Portfolio', 'No', '10', 'TRUST_DIST',  'character of distribution?',                   'Trust K-1'),
    ('W2_Employee',       'Wages',            'No', 'Active',    'No', '1z', 'NONE',        '(n/a)',                                        'Standard W-2 wages'),
    ('W2_SCorpOwner',     'Wages',            'No', 'Active',    'No', '1z', 'OWNER_PAY',   'owner pay portion?',                           'S-Corp owner reasonable comp'),
    ('Int_Taxable',       'Investment Income','No', 'Portfolio', 'No', '2b', 'TAX_EXEMPT',  'tax-exempt portion?',                          'Taxable interest'),
    ('Int_Exempt',        'Investment Income','No', 'N/A',       'No', '2a', 'NONE',        '(all exempt)',                                 'Tax-exempt interest'),
    ('Div_Qualified',     'Investment Income','No', 'Portfolio', 'No', '3b', 'QUAL_DIV',    'qualified portion?',                           'Qualified dividends'),
    ('Div_Ordinary',      'Investment Income','No', 'Portfolio', 'No', '3b', 'QUAL_DIV',    'qualified portion?',                           'Ordinary dividends'),
    ('LTCG_Stock',        'Capital Gains',    'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'wash sales? carryover?',                       'LT cap gains'),
    ('STCG_Stock',        'Capital Gains',    'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'wash sales? carryover?',                       'ST cap gains'),
    ('LTCG_RE',           'Capital Gains',    'No', 'Passive',   'No', '7',  'LTCG_SPLIT',  '§1250 portion? §1031?',                        'LT cap gain on RE'),
    ('Sec1250_Recap',     'Capital Gains',    'No', 'Passive',   'No', '7',  'SEC1250',     'capped at 25%',                                '§1250 recapture'),
    ('LTCG_K1_Passthrough','Capital Gains',   'No', 'Portfolio', 'No', '7',  'LTCG_SPLIT',  'character per K-1 box?',                       'K-1 passthrough'),
    ('Adj_HSA',           'Adjustment',       'No', 'N/A',       'No', '10', 'HSA',         'family vs self?',                              'HSA'),
    ('Adj_IRA',           'Adjustment',       'No', 'N/A',       'No', '10', 'IRA',         'deductible portion?',                          'IRA'),
    ('Adj_Retirement',    'Adjustment',       'No', 'N/A',       'No', '10', 'RETIREMENT',  'plan type / limit?',                           'Retirement plan'),
    ('Adj_SEHealth',      'Adjustment',       'No', 'N/A',       'No', '10', 'SE_HEALTH',   'SE earnings cap?',                             'SE health insurance'),
    ('Adj_StudentLoan',   'Adjustment',       'No', 'N/A',       'No', '10', 'STUDENT_LOAN','MAGI phase-out?',                              'Student loan interest'),
    ('Itm_Medical',       'Itemized',         'No', 'N/A',       'No', '12', 'MEDICAL',     '7.5% AGI floor',                               'Medical'),
    ('Itm_SALT',          'Itemized',         'No', 'N/A',       'No', '12', 'SALT',        '$10K cap',                                     'SALT'),
    ('Itm_Mortgage',      'Itemized',         'No', 'N/A',       'No', '12', 'MORTGAGE',    'principal cap by date',                        'Mortgage int'),
    ('Itm_Charity',       'Itemized',         'No', 'N/A',       'No', '12', 'CHARITY',     '60% AGI cap',                                  'Charity'),
    ('Cr_CTC',            'Credit',           'No', 'N/A',       'No', '19', 'CTC',         'children under 17?',                           'CTC'),
    ('Cr_Education',      'Credit',           'No', 'N/A',       'No', '20', 'EDUCATION',   'AOTC vs LLC?',                                 'Education credits'),
    ('Cr_FTC',            'Credit',           'No', 'N/A',       'No', '20', 'FTC',         'Form 1116 required?',                          'FTC'),
    ('Pmt_Withholding',   'Payment',          'No', 'N/A',       'No', '25', 'NONE',        '(n/a)',                                        'Withholding'),
    ('Pmt_EstTax',        'Payment',          'No', 'N/A',       'No', '26', 'NONE',        'safe harbor met?',                             'Estimated tax'),
]
for i, row in enumerate(profiles):
    for j, v in enumerate(row):
        ws.cell(row=5 + i, column=1 + j, value=v)
tbl = Table(displayName='tblTreatmentProfileMap', ref=f'A4:{get_column_letter(len(tpm_cols))}{4+len(profiles)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)
widths(ws, [22, 18, 11, 12, 13, 11, 18, 50, 35])

# ============================================================
# Master_Inputs — single-entry committed baseline items, year-tagged
# ============================================================
ws = wb.create_sheet('Master_Inputs')
ws['A1'] = 'MASTER INPUTS — committed baseline source-input items (one row per source document per year)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Adjustments and strategies live on the year sheet. Master is just where baseline data lives.'
ws['A2'].font = NOTE_FONT

mi_cols = [
    'InputID',                                                       # A
    'Year',                                                          # B
    'ClientID', 'ClientName',                                        # C-D
    'Bucket', 'Treatment_Profile', 'Source_Document',                # E-G (cascading dropdowns)
    'Provenance',                                                    # H
    'Payor',                                                         # I
    'Baseline_Amount', 'Helper_Amount',                              # J-K
    'SE_Subject', 'NIIT_Class', 'QBI_Eligible',                      # L-N (stored; VBA auto-fills)
    'Primary_Line', 'Helper_Treatment',                              # O-P (stored; VBA auto-fills)
    'Consider', 'Notes',                                             # Q-R
]
hdr(ws, 4, mi_cols)

mi_sample = [
    # 2024 — Cedillo tie-out validation case
    ['CED|2024|Wages|01',  2024, 'CEDILLO', 'Ron Cedillo',
     'Wages',             'W2_SCorpOwner',  'W-2',       'PBC - Reviewed', 'Acme S-Corp',
     153648, 0,
     'No', 'Active',    'No',  '1z', 'OWNER_PAY',   'Owner reasonable comp', ''],
    ['CED|2024|BI|01',     2024, 'CEDILLO', 'Ron Cedillo',
     'Business Income',   'K1_PTP_Passive', 'K-1',       'PBC - Reviewed', 'Cedillo Partnership',
     -100766, 0,
     'No', 'Passive',   'Yes', '10', 'K1_SPLIT',    'Passive loss', ''],
    ['CED|2024|II|01',     2024, 'CEDILLO', 'Ron Cedillo',
     'Investment Income', 'Div_Ordinary',   '1099-DIV',  'PBC - Reviewed', 'Brokerage',
     25922, 0,
     'No', 'Portfolio', 'No',  '3b', 'QUAL_DIV',    'All non-qualified', ''],
    ['CED|2024|CG|01',     2024, 'CEDILLO', 'Ron Cedillo',
     'Capital Gains',     'LTCG_Stock',     '1099-B',    'PBC - Reviewed', 'Brokerage',
     14487, 0,
     'No', 'Portfolio', 'No',  '7',  'LTCG_SPLIT',  'All long-term', ''],
    # 2025 — sample client baseline
    ['SAM|2025|Wages|01',  2025, 'SAMPLE', 'Sample Client',
     'Wages',             'W2_SCorpOwner',  'W-2',       'Estimate - Preparer', 'SampleCo S-Corp',
     100000, 100000,
     'No', 'Active',    'No',  '1z', 'OWNER_PAY',   'Owner reasonable comp', ''],
    ['SAM|2025|BI|01',     2025, 'SAMPLE', 'Sample Client',
     'Business Income',   'K1_SCorp_Active','K-1',       'PY Rolled Forward', 'SampleCo S-Corp K-1',
     200000, 0,
     'No', 'Active',    'Yes', '10', 'K1_SPLIT',    'Active S-corp K-1', ''],
    ['SAM|2025|II_Div|01', 2025, 'SAMPLE', 'Sample Client',
     'Investment Income', 'Div_Qualified',  '1099-DIV',  'PBC - Received', 'Brokerage',
     10000, 7000,
     'No', 'Portfolio', 'No',  '3b', 'QUAL_DIV',    '$7K qualified', ''],
    ['SAM|2025|II_Int|01', 2025, 'SAMPLE', 'Sample Client',
     'Investment Income', 'Int_Taxable',    '1099-INT',  'PBC - Received', 'Brokerage',
     500, 0,
     'No', 'Portfolio', 'No',  '2b', 'TAX_EXEMPT',  'All taxable', ''],
    ['SAM|2025|CG|01',     2025, 'SAMPLE', 'Sample Client',
     'Capital Gains',     'LTCG_Stock',     '1099-B',    'PBC - Requested', 'Brokerage',
     25000, 0,
     'No', 'Portfolio', 'No',  '7',  'LTCG_SPLIT',  'All long-term', ''],
    ['SAM|2025|Itm|01',    2025, 'SAMPLE', 'Sample Client',
     'Itemized',          'Itm_SALT',       'Property Tax Receipt', 'PBC - Received', '',
     10000, 0,
     'No', 'N/A',       'No',  '12', 'SALT',        'SALT cap', ''],
]
for i, row in enumerate(mi_sample):
    r = 5 + i
    for j, v in enumerate(row):
        c = ws.cell(row=r, column=1 + j, value=v); c.fill = INPUT_FILL

tbl = Table(displayName='tblMaster_Inputs', ref=f'A4:{get_column_letter(len(mi_cols))}{4+len(mi_sample)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

# Cascading dropdowns
add_dv(ws, 'E', '=Bucket')
add_dv(ws, 'F', '=INDIRECT(SUBSTITUTE($E5," ","")&"_Profiles")')
add_dv(ws, 'G', '=INDIRECT(SUBSTITUTE($E5," ","")&"_Docs")')
add_dv(ws, 'H', '=Provenance')
add_dv(ws, 'L', '=Yes_No')
add_dv(ws, 'M', '=NIIT_Class')
add_dv(ws, 'N', '=Yes_No')

widths(ws, [22, 7, 11, 18, 18, 22, 22, 18, 22, 14, 14, 11, 12, 13, 11, 18, 30, 30])
ws.freeze_panes = 'A5'

# ============================================================
# Y2025 — strategies schedule + rollup with S1 manual override
# ============================================================
ws = wb.create_sheet('Y2025')
ws['A1'] = 'Y2025 — strategies schedule + rollup (master baseline + S1 manual override + strategies)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Strategies entered here flow into the Strategies column of the rollup (committed-tier status only).'
ws['A2'].font = NOTE_FONT

# ----- STRATEGIES SCHEDULE -----
ws['A4'] = '▸ STRATEGIES — tblY2025_Strategies'
ws['A4'].font = SUB_FONT
strat_cols = ['StrategyID', 'Strategy Name', 'TargetLine', 'Amount', 'Status', 'Notes']
hdr(ws, 5, strat_cols)
strat_rows = [
    ['STR-001', 'S-Corp Wage Optimization (STD-008)',   '1z', -25000, 'Committed',  'Reduce W-2 by $25K'],
    ['STR-002', 'HSA Family Max (Retirement-adjacent)', '10', -8550,  'Committed',  'Family HSA contribution'],
    ['STR-003', 'DAF Stack (ADV-002 Charitable)',       '12',  15000, 'Proposed',   'Bunching strategy — pending decision'],
    ['STR-004', 'SEP-IRA Contribution (STD-001)',       '10', -7000,  'Approved',   'Pending commitment'],
    ['STR-005', 'Cost Seg Study (STD-012)',             '10', -80000, 'Proposed',   'Real estate accelerated depreciation'],
]
for i, row in enumerate(strat_rows):
    r = 6 + i
    for j, v in enumerate(row):
        c = ws.cell(row=r, column=1 + j, value=v); c.fill = INPUT_FILL

tbl = Table(displayName='tblY2025_Strategies', ref=f'A5:{get_column_letter(len(strat_cols))}{5+len(strat_rows)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)
add_dv(ws, 'C', '=TaxLines', start=6, end=200)
add_dv(ws, 'E', '=Status', start=6, end=200)

# ----- ROLLUP at column H (col 8) — gap G -----
ROLLUP_COL = 8  # H
RC = lambda offset: get_column_letter(ROLLUP_COL + offset)

ws.cell(row=4, column=ROLLUP_COL, value='▸ 2025 ROLLUP — 1040 LINES').font = SUB_FONT
hdr(ws, 5, ['Line', 'Description', 'Baseline (Master)', 'S1 Override (manual)', 'Strategies', 'Effective', 'Drill'], start_col=ROLLUP_COL)

# Section 1: 1040 LINES — aggregate to taxable income
ru_lines = [
    ('1z', 'Wages'),
    ('2b', 'Taxable interest'),
    ('3b', 'Ordinary dividends (total — incl qualified)'),
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
    r = 6 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=line)
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    # Baseline from Master (Year=2025 + Primary_Line)
    ws.cell(row=r, column=ROLLUP_COL + 2,
            value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Primary_Line], ${RC(0)}{r})')
    # S1 Override — manual entry by preparer; blank means no override
    s1_cell = ws.cell(row=r, column=ROLLUP_COL + 3)
    s1_cell.fill = INPUT_FILL
    # Strategies — SUMIFS from year-sheet strategies table, committed-tier only
    ws.cell(row=r, column=ROLLUP_COL + 4,
            value=f'=SUMIFS(tblY2025_Strategies[Amount], tblY2025_Strategies[TargetLine], ${RC(0)}{r}, tblY2025_Strategies[Status], "Committed") '
                  f'+ SUMIFS(tblY2025_Strategies[Amount], tblY2025_Strategies[TargetLine], ${RC(0)}{r}, tblY2025_Strategies[Status], "Implemented")')
    # Effective = IF(Override blank, Baseline, Override) + Strategies
    # — S1 column is a TRUE OVERRIDE: blank = use baseline; non-blank = replace baseline
    ws.cell(row=r, column=ROLLUP_COL + 5,
            value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})+{RC(4)}{r}')
    # Drill hyperlink — jumps to Drill_Line cell
    ws.cell(row=r, column=ROLLUP_COL + 6,
            value=f'=HYPERLINK("#Y2025!{RC(1)}33", "↗ drill")')
    ws.cell(row=r, column=ROLLUP_COL + 6).font = Font(color='0563C1', underline='single')

# ----- Section 2: HELPER / TAX-CALC INPUTS -----
HELPER_ROW = 19
ws.cell(row=HELPER_ROW, column=ROLLUP_COL,
        value='▸ HELPER / TAX-CALC INPUTS — does NOT add to income; reference values for future LAMBDAs').font = SUB_FONT
hdr(ws, HELPER_ROW + 1, ['Helper Label', 'Description', 'Amount', 'Used by'], start_col=ROLLUP_COL)
helper_items = [
    ('TAX_EXEMPT', 'Tax-exempt interest (Line 2a; reported but not taxed)',  'NIIT_FN (MAGI base)'),
    ('QUAL_DIV',   'Qualified dividends (carve-out of Line 3b; LTCG stack)', 'Calc_CapGainsTax stacking'),
    ('OWNER_PAY',  'Owner W-2 wages (S-Corp reasonable comp)',               'FICA_Employer/Employee — True Tax Burden box'),
    ('SEC1250',    '§1250 unrecaptured gain (capped at 25% rate)',           'Calc_1250Tax'),
    ('SE_INCOME',  'Total SE-subject income (Sch C/F + active K-1 helper)',  'Calc_SE_Tax · AddlMedicareTax_FN'),
    ('PASSIVE',    'Passive income/loss (Sch E baseline; PAL limits)',       'PassiveLossAllowed_FN'),
    ('TAX_W2',     'Total W-2 wages (any source)',                           'Calc_SE_Tax · AddlMedicareTax_FN'),
]
for i, (label, desc, used_by) in enumerate(helper_items):
    r = HELPER_ROW + 2 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=label).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    if label == 'TAX_W2':
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], "Wages")')
    elif label == 'SE_INCOME':
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblMaster_Inputs[Helper_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Helper_Treatment], "SE_INCOME") '
                      f'+ SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "SchC_Active") '
                      f'+ SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "SchF_Active")')
    elif label == 'PASSIVE':
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[NIIT_Class], "Passive")')
    else:
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblMaster_Inputs[Helper_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Helper_Treatment], "{label}")')
    ws.cell(row=r, column=ROLLUP_COL + 3, value=used_by).font = NOTE_FONT

# ----- DRILL PANEL -----
DRILL_HDR = 32
ws.cell(row=DRILL_HDR, column=ROLLUP_COL,
        value='▸ DRILL DETAIL — pick a line; FILTER below shows the contributing Master_Inputs rows').font = SUB_FONT
ws.cell(row=DRILL_HDR + 1, column=ROLLUP_COL, value='Drill into line:').font = Font(bold=True)
ws.cell(row=DRILL_HDR + 1, column=ROLLUP_COL).alignment = Alignment(horizontal='right')
drill_cell = ws.cell(row=DRILL_HDR + 1, column=ROLLUP_COL + 1, value='1z')
drill_cell.fill = KEY_FILL
drill_cell.font = Font(bold=True, color='305496')
drill_cell.alignment = Alignment(horizontal='center')

wb.defined_names['Drill_Line'] = DefinedName('Drill_Line', attr_text=f"'Y2025'!${RC(1)}${DRILL_HDR + 1}")
ws.cell(row=DRILL_HDR + 1, column=ROLLUP_COL + 3,
        value=f'=HYPERLINK("#Master_Inputs!A1", "✏ open Master_Inputs to edit")').font = Font(color='0563C1', underline='single')

drill_lines = [l for (l, _) in ru_lines]
dv_drill = DataValidation(type='list', formula1=f'"{",".join(drill_lines)}"', allow_blank=False)
ws.add_data_validation(dv_drill)
dv_drill.add(f'{RC(1)}{DRILL_HDR + 1}')

FILTER_HDR = DRILL_HDR + 3
hdr(ws, FILTER_HDR, ['InputID', 'Bucket', 'Treatment_Profile', 'Payor', 'Baseline_Amount', 'Helper_Amount', 'Notes'], start_col=ROLLUP_COL)
hstack_formula = (
    '=IFERROR('
    'HSTACK('
    'FILTER(tblMaster_Inputs[InputID],          (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Bucket],           (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Treatment_Profile],(tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Payor],            (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Baseline_Amount],  (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Helper_Amount],    (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line)),'
    'FILTER(tblMaster_Inputs[Notes],            (tblMaster_Inputs[Year]=2025)*(tblMaster_Inputs[Primary_Line]=Drill_Line))'
    '), "(no rows matching this line / year)")'
)
ws.cell(row=FILTER_HDR + 1, column=ROLLUP_COL, value=hstack_formula)

ws.cell(row=FILTER_HDR + 12, column=ROLLUP_COL,
        value='FILTER output is live — change Drill_Line and the rows update. Use the hyperlink to edit in Master_Inputs.').font = NOTE_FONT

# Column widths
# A:F strategies table (6 cols), G gap (1), H-N rollup (7 cols)
strat_widths = [12, 36, 12, 14, 14, 32]   # A-F
gap_widths = [3]                            # G
rollup_widths = [8, 36, 16, 16, 14, 16, 9] # H-N
widths(ws, strat_widths + gap_widths + rollup_widths)
ws.freeze_panes = 'A6'

# Order sheets
order = ['Master_Inputs', 'Y2025', 'Treatment_Profile_Map', 'Dropdown_Lists']
wb._sheets = [wb[name] for name in order]

wb.save(OUT)
print(f'Saved: {OUT}')
print(f'Sheets: {wb.sheetnames}')
print(f'Named ranges: {len(list(wb.defined_names))}')
