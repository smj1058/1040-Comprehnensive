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

OUT = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework.xlsx'

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
    # Business income flows to Sch 1 → 1040 Line 8 (NOT Line 10 — that's adjustments)
    ('SchC_Active',       'Business Income',  'Yes','Active',    'Yes','8',  'SE_INCOME',   'SE earnings?',                                 'Sole prop active SE'),
    ('SchE_Rental',       'Business Income',  'No', 'Passive',   'No', '8',  'PASSIVE',     'short-term rental? RE Pro election?',          'Rental real estate default passive'),
    ('SchE_REPro',        'Business Income',  'No', 'Active',    'No', '8',  'ACTIVE_RE',   'meets 750hr / >50% test?',                     'RE Pro election'),
    ('SchF_Active',       'Business Income',  'Yes','Active',    'Yes','8',  'SE_INCOME',   'farm income averaging?',                       'Farm income'),
    ('K1_PTP_Active',     'Business Income',  'Yes','Active',    'Yes','8',  'K1_SPLIT',    'active vs passive?',                           'Active partnership K-1'),
    ('K1_PTP_Passive',    'Business Income',  'No', 'Passive',   'Yes','8',  'K1_SPLIT',    'PAL limits?',                                  'Passive partnership K-1'),
    ('K1_SCorp_Active',   'Business Income',  'No', 'Active',    'Yes','8',  'K1_SPLIT',    'active vs passive?',                           'Active S-Corp K-1'),
    ('K1_SCorp_Passive',  'Business Income',  'No', 'Passive',   'Yes','8',  'K1_SPLIT',    'rare — confirm',                               'Passive S-Corp K-1'),
    ('Trust_K1',          'Business Income',  'No', 'Portfolio', 'No', '8',  'TRUST_DIST',  'character of distribution?',                   'Trust K-1'),
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
     'No', 'Passive',   'Yes', '8',  'K1_SPLIT',    'Passive loss', ''],
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
     'No', 'Active',    'Yes', '8',  'K1_SPLIT',    'Active S-corp K-1', ''],
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

# Rollup lines in 1040 page-1 order. 'kind' = 'data' (SUMIFS) | 'agg' (aggregator) | 'info' (informational, doesn't add to Total Income)
ru_lines = [
    ('1z', 'Wages',                                            'data'),
    ('2a', 'Tax-exempt interest (informational — Helper)',     'info'),
    ('2b', 'Taxable interest',                                 'data'),
    ('3a', 'Qualified dividends (informational — Helper)',     'info'),
    ('3b', 'Ordinary dividends (total — incl qualified)',      'data'),
    ('7',  'Capital gain or (loss)',                           'data'),
    ('8',  'Other income (incl business income via Sch 1)',    'data'),
    ('9',  'TOTAL INCOME',                                     'agg_total_income'),
    ('10', 'Adjustments to income',                            'data'),
    ('11', 'AGI',                                              'agg_agi'),
    ('12', 'Std/Itemized deduction',                           'data'),
    ('13', 'QBI deduction',                                    'data'),
    ('15', 'TAXABLE INCOME',                                   'agg_taxable_income'),
]
# Pre-compute row map (line → row number) for aggregator formulas
row_map = {line: 6 + i for i, (line, _, _) in enumerate(ru_lines)}
EFF = lambda line: f'{RC(5)}{row_map[line]}'

for i, (line, desc, kind) in enumerate(ru_lines):
    r = 6 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=line)
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)

    if kind == 'info':
        # Informational lines (2a tax-exempt, 3a qualified div) pull from helper section, don't add to income
        if line == '2a':
            ws.cell(row=r, column=ROLLUP_COL + 2, value='=TAX_EXEMPT')
        elif line == '3a':
            ws.cell(row=r, column=ROLLUP_COL + 2, value='=QUAL_DIV')
        ws.cell(row=r, column=ROLLUP_COL + 3).fill = INPUT_FILL  # Override (still allowed)
        ws.cell(row=r, column=ROLLUP_COL + 4, value=0)  # No strategies on info lines
        # Effective: same as Baseline (or Override) — doesn't aggregate into anything
        ws.cell(row=r, column=ROLLUP_COL + 5,
                value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})')
    elif kind == 'agg_total_income':
        # Line 9 = sum of 1z, 2b, 3b, 7, 8 (the data-bearing income lines)
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'={EFF("1z")}+{EFF("2b")}+{EFF("3b")}+{EFF("7")}+{EFF("8")}')
        ws.cell(row=r, column=ROLLUP_COL + 3).fill = INPUT_FILL
        ws.cell(row=r, column=ROLLUP_COL + 4, value=0)
        ws.cell(row=r, column=ROLLUP_COL + 5,
                value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})')
    elif kind == 'agg_agi':
        # Line 11 = Line 9 (Total Income) - Line 10 (Adjustments to income)
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'={EFF("9")}+{EFF("10")}')   # Line 10 typically negative (deductions)
        ws.cell(row=r, column=ROLLUP_COL + 3).fill = INPUT_FILL
        ws.cell(row=r, column=ROLLUP_COL + 4, value=0)
        ws.cell(row=r, column=ROLLUP_COL + 5,
                value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})')
    elif kind == 'agg_taxable_income':
        # Line 15 = Line 11 (AGI) - Line 12 (Std/Itm Ded) - Line 13 (QBI Ded)
        # Line 12 and 13 are typically negative deductions in the data model
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'={EFF("11")}+{EFF("12")}+{EFF("13")}')
        ws.cell(row=r, column=ROLLUP_COL + 3).fill = INPUT_FILL
        ws.cell(row=r, column=ROLLUP_COL + 4, value=0)
        ws.cell(row=r, column=ROLLUP_COL + 5,
                value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})')
    else:
        # Standard data line — SUMIFS from Master, plus S1 Override and Strategies
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Primary_Line], ${RC(0)}{r})')
        ws.cell(row=r, column=ROLLUP_COL + 3).fill = INPUT_FILL  # S1 Override
        ws.cell(row=r, column=ROLLUP_COL + 4,
                value=f'=SUMIFS(tblY2025_Strategies[Amount], tblY2025_Strategies[TargetLine], ${RC(0)}{r}, tblY2025_Strategies[Status], "Committed") '
                      f'+ SUMIFS(tblY2025_Strategies[Amount], tblY2025_Strategies[TargetLine], ${RC(0)}{r}, tblY2025_Strategies[Status], "Implemented")')
        # Effective = IF(Override blank, Baseline, Override) + Strategies
        ws.cell(row=r, column=ROLLUP_COL + 5,
                value=f'=IF(ISBLANK({RC(3)}{r}),{RC(2)}{r},{RC(3)}{r})+{RC(4)}{r}')
    # Drill hyperlink — jumps to Drill_Line cell
    ws.cell(row=r, column=ROLLUP_COL + 6,
            value=f'=HYPERLINK("#Y2025!{RC(1)}49", "↗ drill")')  # drill cell at DRILL_HDR+1 = 49
    ws.cell(row=r, column=ROLLUP_COL + 6).font = Font(color='0563C1', underline='single')

# ----- Section 2: HELPER / TAX-CALC INPUTS -----
HELPER_ROW = 21  # rollup now ends at row 18 (added 2a, 3a)
ws.cell(row=HELPER_ROW, column=ROLLUP_COL,
        value='▸ HELPER / TAX-CALC INPUTS — does NOT add to income; reference values for future LAMBDAs').font = SUB_FONT
hdr(ws, HELPER_ROW + 1, ['Helper Label', 'Description', 'Amount', 'Used by'], start_col=ROLLUP_COL)
# Each entry: (label, description, used_by_LAMBDA, formula_template)
# Formulas use Year=2025 and tblMaster_Inputs columns; SUMIFS aggregations.
ROLLUP_REF_COL = ROLLUP_COL  # for f-string interpolation
helper_items = [
    # --- WAGES BREAKOUT ---
    ('W2_OWNER',        'Owner W-2 wages (S-Corp reasonable comp; Treatment_Profile=W2_SCorpOwner)',
        'FICA_Employer/Employee — True Tax Burden box',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "W2_SCorpOwner")'),
    ('W2_THIRD_PARTY',  'Third-party W-2 wages (Treatment_Profile=W2_Employee)',
        'Calc_SE_Tax (SS-base sharing) · AddlMedicareTax_FN',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "W2_Employee")'),
    ('W2_TOTAL',        'Total W-2 wages (owner + third-party)',
        'Calc_SE_Tax (SS-base sharing) · AddlMedicareTax_FN',
        '=W2_OWNER+W2_THIRD_PARTY'),
    # --- BUSINESS INCOME BREAKOUT (three tiers) ---
    ('BI_SE_SUBJECT',   'Business income subject to SE tax (Sch C, Sch F, active K-1 PTP)',
        'Calc_SE_Tax base · AddlMedicareTax_FN',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], "Business Income", tblMaster_Inputs[SE_Subject], "Yes")'),
    ('BI_ACTIVE_NONSE', 'Active business income NOT subject to SE (active S-Corp K-1, etc.)',
        'NIIT exclusion (active) · QBI eligible',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], "Business Income", tblMaster_Inputs[SE_Subject], "No", tblMaster_Inputs[NIIT_Class], "Active")'),
    ('BI_PASSIVE',      'Passive business income / loss (passive K-1s, Sch E rental)',
        'PassiveLossAllowed_FN · NIIT inclusion',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Bucket], "Business Income", tblMaster_Inputs[NIIT_Class], "Passive")'),
    # --- INVESTMENT INCOME CARVE-OUTS ---
    ('TAX_EXEMPT',      'Tax-exempt interest (Line 2a; reported but not taxed)',
        'NIIT_FN (MAGI base)',
        '=SUMIFS(tblMaster_Inputs[Helper_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Helper_Treatment], "TAX_EXEMPT")'),
    ('QUAL_DIV',        'Qualified dividends (carve-out of Line 3b; LTCG stack)',
        'Calc_CapGainsTax stacking',
        '=SUMIFS(tblMaster_Inputs[Helper_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Helper_Treatment], "QUAL_DIV")'),
    # --- CAPITAL GAINS BREAKOUT (1040 Line 7 nets ST+LT; LAMBDAs need them split) ---
    ('CG_LT',           'Long-term capital gains (LT preferential rate; stacks with qualified div)',
        'Calc_CapGainsTax',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "LTCG_Stock") '
        '+ SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "LTCG_RE") '
        '+ SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "LTCG_K1_Passthrough") '
        '+ SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "Sec1250_Recap")'),
    ('CG_ST',           'Short-term capital gains (taxed as ordinary income)',
        'Calc_OrdinaryTax (ST folded into ordinary income)',
        '=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Treatment_Profile], "STCG_Stock")'),
    ('SEC1250',         '§1250 unrecaptured gain (sub-carve of CG_LT; capped at 25% rate)',
        'Calc_1250Tax',
        '=SUMIFS(tblMaster_Inputs[Helper_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[Helper_Treatment], "SEC1250")'),
]
for i, (label, desc, used_by, formula) in enumerate(helper_items):
    r = HELPER_ROW + 2 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=label).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    amt_cell = ws.cell(row=r, column=ROLLUP_COL + 2, value=formula)
    ws.cell(row=r, column=ROLLUP_COL + 3, value=used_by).font = NOTE_FONT
    # Workbook-level named range for this helper amount — ready to feed LAMBDAs / summary page
    helper_ref = f"'Y2025'!${get_column_letter(ROLLUP_COL + 2)}${r}"
    wb.defined_names[label] = DefinedName(label, attr_text=helper_ref)

# Named ranges for the key rollup totals (Effective column = ROLLUP_COL+5)
# Updated row numbers — added 2a (row 7) and 3a (row 9) informational lines shifted everything down
eff_col_letter = get_column_letter(ROLLUP_COL + 5)
rollup_totals_named = {
    'Line_1z_Wages':       6,
    'Line_2a_TaxExempt':   7,   # informational (= TAX_EXEMPT)
    'Line_2b_TaxInt':      8,
    'Line_3a_QualDiv':     9,   # informational (= QUAL_DIV)
    'Line_3b_OrdDiv':      10,
    'Line_7_CapGain':      11,
    'Line_8_OtherInc':     12,  # business income flows here via Sch 1
    'TotalIncome':         13,  # Line 9
    'AdjToIncome':         14,  # Line 10
    'AGI':                 15,  # Line 11
    'StdItemDed':          16,  # Line 12
    'QBI_Deduction':       17,  # Line 13
    'TaxableIncome':       18,  # Line 15
}
for name, row in rollup_totals_named.items():
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Y2025'!${eff_col_letter}${row}")

# ============================================================
# TAX CALC INPUTS — derived values future LAMBDAs consume directly
# (named so each LAMBDA call can read =OrdIncome, =MAGI, =NII, etc.)
# ============================================================
TAX_INPUTS_ROW = 35  # helper section ends at row 33; gap at 34; tax inputs header at 35
ws.cell(row=TAX_INPUTS_ROW, column=ROLLUP_COL,
        value='▸ TAX CALC INPUTS — derived; each row is a workbook-level named range for LAMBDAs to consume').font = SUB_FONT
hdr(ws, TAX_INPUTS_ROW + 1, ['Named Range', 'Description', 'Formula / Value', 'Used by LAMBDA'], start_col=ROLLUP_COL)

tax_inputs = [
    ('OrdIncome',                'Ordinary income (TaxableIncome - CG_LT - QUAL_DIV - SEC1250)',
                                 '=TaxableIncome-CG_LT-QUAL_DIV-SEC1250',
                                 'Calc_CapGainsTax stacking base · Calc_OrdinaryTax (after carve-outs)'),
    ('MAGI',                     'Modified AGI = AGI + tax-exempt interest',
                                 '=AGI+TAX_EXEMPT',
                                 'Calc_NIIT · PassiveLossAllowed_FN'),
    ('NII',                      'Net Investment Income = taxable int + div + cap gain + passive',
                                 '=Line_2b_TaxInt+Line_3b_OrdDiv+Line_7_CapGain+BI_PASSIVE',
                                 'Calc_NIIT'),
    ('QBI_Income',               'QBI-eligible business income (active business)',
                                 '=BI_SE_SUBJECT+BI_ACTIVE_NONSE',
                                 'Calc_QBI_Simple · QBI_FN'),
    ('TaxableIncome_BeforeQBI',  'Taxable Income BEFORE QBI deduction (= AGI - StdItemDed)',
                                 '=AGI+StdItemDed',  # StdItemDed is negative by convention
                                 'Calc_QBI_Simple (cap reference)'),
    ('BusinessLoss',             'Net business loss (only when negative; for EBL limit)',
                                 '=MIN(0,BI_SE_SUBJECT+BI_ACTIVE_NONSE+BI_PASSIVE)',
                                 'ExcessBusinessLossLimit_FN'),
    ('NetSEIncome',              'Net SE income (alias of BI_SE_SUBJECT for LAMBDA clarity)',
                                 '=BI_SE_SUBJECT',
                                 'Calc_SE_Tax · AddlMedicareTax_FN · SETax_FN'),
]

# Manual / placeholder inputs (preparer or another sheet supplies these)
tax_inputs_manual = [
    ('UBIA',                'Unadjusted Basis Immediately After Acquisition (QBI W-2/UBIA test)',
                            0,  # placeholder
                            'QBI_FN'),
    ('IsSSTB',              'Is Specified Service Trade or Business? (TRUE/FALSE)',
                            False,
                            'QBI_FN'),
    ('NOL_Carryforward',    'NOL carryforward available (from prior-year Carryovers; populate manually for now)',
                            0,
                            'NOLDeductionAllowed_FN'),
]

ti_start_row = TAX_INPUTS_ROW + 2
for i, (name, desc, formula, used_by) in enumerate(tax_inputs):
    r = ti_start_row + i
    ws.cell(row=r, column=ROLLUP_COL,     value=name).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    ws.cell(row=r, column=ROLLUP_COL + 2, value=formula)
    ws.cell(row=r, column=ROLLUP_COL + 3, value=used_by).font = NOTE_FONT
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Y2025'!${get_column_letter(ROLLUP_COL + 2)}${r}")

ti_manual_start = ti_start_row + len(tax_inputs)
for i, (name, desc, value, used_by) in enumerate(tax_inputs_manual):
    r = ti_manual_start + i
    ws.cell(row=r, column=ROLLUP_COL,     value=name).font = Font(bold=True, color='305496')
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    c = ws.cell(row=r, column=ROLLUP_COL + 2, value=value)
    c.fill = INPUT_FILL  # manual entry
    ws.cell(row=r, column=ROLLUP_COL + 3, value=used_by).font = NOTE_FONT
    wb.defined_names[name] = DefinedName(name, attr_text=f"'Y2025'!${get_column_letter(ROLLUP_COL + 2)}${r}")

# ----- DRILL PANEL -----
DRILL_HDR = 48  # after rollup (6-18), helper (21-33), tax inputs (35-46), gap at 47
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

drill_lines = [l for (l, _, _) in ru_lines]
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
