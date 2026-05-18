"""Build v3 sample — minimal, current-year focused.
One year sheet (Y2025), input table at A:Q, rollup at column T onwards.
All input columns are stored values (no formula-driven derived columns).
Strategies not in the input table for this iteration.

Output: docs/Tax_Workbook_Sample_Template_v3.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.workbook.properties import CalcProperties

OUT = '/home/user/1040-Comprehnensive/docs/Tax_Workbook_Sample_Template_v3.xlsx'

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

# ============================================================
# Dropdown_Lists (needed for the year sheet's data validation)
# ============================================================
ws = wb.create_sheet('Dropdown_Lists')
ws['A1'] = 'DROPDOWN LISTS (driving data validation on the year sheet)'
ws['A1'].font = TITLE_FONT

top_lists = {
    'Bucket':       ['Business Income', 'Wages', 'Investment Income', 'Capital Gains', 'Adjustment', 'Itemized', 'Credit', 'Payment'],
    'Yes_No':       ['Yes', 'No'],
    'NIIT_Class':   ['Active', 'Passive', 'Portfolio', 'N/A'],
    'Provenance':   ['PY Rolled Forward', 'PY Actuals', 'Estimate - Preparer', 'Estimate - Client',
                     'PBC - Requested', 'PBC - Received', 'PBC - Reviewed',
                     'Extraction - Imported', 'Extraction - Tied', 'System Calculated'],
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

ws.cell(row=16, column=1, value='▸ PER-BUCKET TREATMENT_PROFILE LISTS').font = SUB_FONT
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
    ws.cell(row=17, column=col, value=header).font = HDR_FONT
    ws.cell(row=17, column=col).fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=18 + i, column=col, value=v)
    last_row = 17 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$18:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

ws.cell(row=32, column=1, value='▸ PER-BUCKET SOURCE_DOCUMENT LISTS').font = SUB_FONT
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
    ws.cell(row=33, column=col, value=header).font = HDR_FONT
    ws.cell(row=33, column=col).fill = HDR_FILL
    for i, v in enumerate(items):
        ws.cell(row=34 + i, column=col, value=v)
    last_row = 33 + len(items)
    ref = f"'Dropdown_Lists'!${get_column_letter(col)}$34:${get_column_letter(col)}${last_row}"
    wb.defined_names[header] = DefinedName(header, attr_text=ref)
    col += 1

widths(ws, [22] * 12)

# Control panel cell for toggle
wb.defined_names['Include_Adjustments'] = DefinedName('Include_Adjustments', attr_text="'Y2025'!$T$3")

# ============================================================
# Y2025 — the only sheet that matters
# ============================================================
ws = wb.create_sheet('Y2025')
ws['A1'] = 'Y2025 — current-year tax workbook (sample)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'INPUT TABLE: A:Q  •  ROLLUP: T:Y  •  Yellow = preparer input.  Toggle Include_Adjustments at T3.'
ws['A2'].font = NOTE_FONT

# Toggle cell in plain sight
ws['T3'] = True
ws['T3'].fill = KEY_FILL
ws['T3'].font = Font(bold=True, color='305496')
ws['T3'].alignment = Alignment(horizontal='center')
ws['S3'] = 'Include_Adjustments →'
ws['S3'].font = Font(bold=True)
ws['S3'].alignment = Alignment(horizontal='right')

# Input table headers
input_cols = [
    'Source_ID',          # A
    'Bucket',             # B
    'Treatment_Profile',  # C
    'Source_Document',    # D
    'Payor',              # E
    'Baseline_Amount',    # F
    'Helper_Amount',      # G
    'Adjustment_Amount',  # H
    'Consider',           # I
    'Provenance',         # J
    'SE_Subject',         # K
    'NIIT_Class',         # L
    'QBI_Eligible',       # M
    'Primary_Line',       # N
    'Helper_Treatment',   # O
    'Notes',              # P
]
hdr(ws, 5, input_cols)

# Sample data — 2025 baseline rows only
yi_data = [
    ['Y25-001', 'Wages',             'W2_SCorpOwner',   'W-2',      'SampleCo S-Corp',     100000, 100000, -25000, 'Owner reasonable comp; planning adjustment -$25K', 'Estimate - Preparer', 'No', 'Active',    'No',  '1z', 'OWNER_PAY',   'S-Corp salary reduction planned'],
    ['Y25-002', 'Business Income',   'K1_SCorp_Active', 'K-1',      'SampleCo S-Corp K-1', 200000, 0,      0,      'Active S-corp K-1',                                'PY Rolled Forward',   'No', 'Active',    'Yes', '10', 'K1_SPLIT',    ''],
    ['Y25-003', 'Investment Income', 'Div_Qualified',   '1099-DIV', 'Brokerage',           10000,  7000,   0,      '$7K qualified',                                    'PBC - Received',      'No', 'Portfolio', 'No',  '3b', 'QUAL_DIV',    ''],
    ['Y25-004', 'Investment Income', 'Int_Taxable',     '1099-INT', 'Brokerage',           500,    0,      0,      'All taxable',                                      'PBC - Received',      'No', 'Portfolio', 'No',  '2b', 'TAX_EXEMPT',  ''],
    ['Y25-005', 'Capital Gains',     'LTCG_Stock',      '1099-B',   'Brokerage',           25000,  0,      0,      'All long-term',                                    'PBC - Requested',     'No', 'Portfolio', 'No',  '7',  'LTCG_SPLIT',  ''],
    ['Y25-006', 'Adjustment',        'Adj_HSA',         'HSA Stmt', '',                    -8550,  0,      0,      'Family HSA max',                                   'Estimate - Preparer', 'No', 'N/A',       'No',  '10', 'HSA',         ''],
    ['Y25-007', 'Itemized',          'Itm_SALT',        'Property Tax Receipt', '',         10000,  0,      0,      'SALT cap',                                         'PBC - Received',     'No', 'N/A',       'No',  '12', 'SALT',        ''],
]
for i, row in enumerate(yi_data):
    r = 6 + i
    for j, v in enumerate(row):
        c = ws.cell(row=r, column=1 + j, value=v)
        c.fill = INPUT_FILL

# Excel Table
n_cols = len(input_cols)
tbl = Table(displayName='tblY2025_Inputs', ref=f'A5:{get_column_letter(n_cols)}{5+len(yi_data)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)

# Data validation
def add_dv(letter, formula, end_row=200):
    dv = DataValidation(type='list', formula1=formula, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f'{letter}6:{letter}{end_row}')

add_dv('B', '=Bucket')
add_dv('C', '=INDIRECT(SUBSTITUTE($B6," ","")&"_Profiles")')
add_dv('D', '=INDIRECT(SUBSTITUTE($B6," ","")&"_Docs")')
add_dv('J', '=Provenance')
add_dv('K', '=Yes_No')
add_dv('L', '=NIIT_Class')
add_dv('M', '=Yes_No')
# Include_Adjustments toggle
dv_tog = DataValidation(type='list', formula1='=Yes_No', allow_blank=False)
ws.add_data_validation(dv_tog)
# Make toggle accept TRUE/FALSE or Yes/No — easier to use Yes/No drop
ws['T3'] = 'Yes'

# === ROLLUP at column T (col 20) ===
ROLLUP_COL = 20
RC = lambda offset: get_column_letter(ROLLUP_COL + offset)

ws.cell(row=4, column=ROLLUP_COL, value='2025 ROLLUP').font = SUB_FONT
hdr(ws, 5, ['Line', 'Description', 'Baseline', 'Adj', 'Effective'], start_col=ROLLUP_COL)

ru_lines = [
    ('1z', 'Wages'),
    ('2a', 'Tax-exempt interest'),
    ('2b', 'Taxable interest'),
    ('3a', 'Qualified dividends (helper)'),
    ('3b', 'Ordinary dividends (total)'),
    ('7',  'Capital gain or (loss)'),
    ('8',  'Other income (Sch 1)'),
    ('9',  'TOTAL INCOME (aggregator)'),
    ('10', 'Adjustments to income'),
    ('11', 'AGI (aggregator)'),
    ('12', 'Std/Itemized deduction'),
    ('13', 'QBI deduction'),
    ('15', 'TAXABLE INCOME (aggregator)'),
]
for i, (line, desc) in enumerate(ru_lines):
    r = 6 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=line)
    ws.cell(row=r, column=ROLLUP_COL + 1, value=desc)
    # Baseline (and Helper for line 3a — qualified dividends carve-out)
    if line == '3a':
        # Qualified dividends pulled from Helper_Amount where Helper_Treatment = QUAL_DIV
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "QUAL_DIV")')
    elif line == '2a':
        # Tax-exempt interest pulled from Helper_Amount where Helper_Treatment = TAX_EXEMPT
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "TAX_EXEMPT")')
    else:
        ws.cell(row=r, column=ROLLUP_COL + 2,
                value=f'=SUMIFS(tblY2025_Inputs[Baseline_Amount], tblY2025_Inputs[Primary_Line], ${RC(0)}{r})')
    # Adj
    ws.cell(row=r, column=ROLLUP_COL + 3,
            value=f'=SUMIFS(tblY2025_Inputs[Adjustment_Amount], tblY2025_Inputs[Primary_Line], ${RC(0)}{r})')
    # Effective = Baseline + IF(Include_Adjustments="Yes", Adj, 0)
    ws.cell(row=r, column=ROLLUP_COL + 4,
            value=f'={RC(2)}{r}+IF(Include_Adjustments="Yes", {RC(3)}{r}, 0)')

# TAX COMPUTATION
ws.cell(row=21, column=ROLLUP_COL, value='TAX COMPUTATION (1040)').font = SUB_FONT
hdr(ws, 22, ['Component', 'Note', 'Amount'], start_col=ROLLUP_COL)
tax_calc = [
    ('Ord Tax',         'Calc_OrdinaryTax(TI, FilingStatus)',                  '=0  (KISS LAMBDA)'),
    ('LTCG Tax',        'Calc_CapGainsTax(LTCG, OrdInc, FilingStatus)',        '=0'),
    ('SE Tax',          'Calc_SE_Tax(SE_inc, W2, FilingStatus)',               '=0'),
    ('NIIT',            'Calc_NIIT(MAGI, NII, FilingStatus)',                  '=0'),
    ('Addl Medicare',   'AddlMedicareTax_FN(W2, SE, FilingStatus)',            '=0'),
    ('TOTAL FED TAX',   'SUM',                                                 f'=SUM({RC(2)}23:{RC(2)}27)'),
]
for i, (label, sig, val) in enumerate(tax_calc):
    r = 23 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=label).font = Font(bold='TOTAL' in label)
    ws.cell(row=r, column=ROLLUP_COL + 1, value=sig).font = NOTE_FONT
    ws.cell(row=r, column=ROLLUP_COL + 2, value=val)

# True Tax Burden box
ws.cell(row=31, column=ROLLUP_COL, value='▸ TRUE TAX BURDEN (1040 + FICA on owner W-2)').font = SUB_FONT
tb = [
    ('Owner W-2 Wages',     f'=SUMIFS(tblY2025_Inputs[Helper_Amount], tblY2025_Inputs[Helper_Treatment], "OWNER_PAY")'),
    ('FICA Employer Share', '=0  (replace with =FICA_EmployerTax_FN(<above>))'),
    ('FICA Employee Share', '=0  (replace with =FICA_EmployeeTax_FN(<above>))'),
    ('TOTAL ADDITIONAL',    f'={RC(2)}33+{RC(2)}34'),
    ('TOTAL FED TAX (1040)',f'={RC(2)}28'),
    ('TRUE TAX BURDEN',     f'={RC(2)}36+{RC(2)}35'),
]
for i, (label, val) in enumerate(tb):
    r = 32 + i
    ws.cell(row=r, column=ROLLUP_COL,     value=label).font = Font(bold='TRUE' in label or 'TOTAL' in label)
    ws.cell(row=r, column=ROLLUP_COL + 2, value=val)

# Column widths
# A:P input (16 cols), Q:S gap (3 cols), T:X rollup (5 cols)
input_widths = [10, 18, 20, 18, 18, 14, 14, 14, 24, 18, 11, 12, 13, 11, 18, 30]  # 16
gap_widths = [3, 3, 22]                                                            # Q, R, S (S labeled "Include_Adjustments →")
rollup_widths = [8, 32, 13, 13, 14]                                                # T, U, V, W, X
all_w = input_widths + gap_widths + rollup_widths
widths(ws, all_w)
ws.freeze_panes = 'A6'

# ============================================================
# Order — Y2025 first
# ============================================================
order = ['Y2025', 'Dropdown_Lists']
wb._sheets = [wb[name] for name in order]

wb.save(OUT)
print(f'Saved: {OUT}')
print(f'Sheets: {wb.sheetnames}')
print(f'Named ranges: {len(list(wb.defined_names))}')
