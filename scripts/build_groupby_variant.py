"""GROUPBY/PIVOTBY variant of the framework.

Compares against the SUMIFS version. Each pivot tab uses a single
PIVOTBY (or GROUPBY) formula that spills.

NOTE: this requires Excel 365 current channel. Older Excel versions
will see #NAME? in those cells.

Output: docs/Master_Pivot_Framework_GROUPBY.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.workbook.properties import CalcProperties

OUT = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_GROUPBY.xlsx'

wb = Workbook()
wb.remove(wb.active)
wb.calculation = CalcProperties(fullCalcOnLoad=True)

HDR_FONT = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
HDR_FILL = PatternFill('solid', fgColor='305496')
SUB_FONT = Font(name='Calibri', size=10, bold=True, color='305496')
TITLE_FONT = Font(name='Calibri', size=14, bold=True, color='305496')
NOTE_FONT = Font(name='Calibri', size=9, italic=True, color='595959')
INPUT_FILL = PatternFill('solid', fgColor='FFF2CC')

def hdr(ws, row, cols, start_col=1):
    for i, c in enumerate(cols):
        cell = ws.cell(row=row, column=start_col + i, value=c)
        cell.font = HDR_FONT; cell.fill = HDR_FILL
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ==========================================
# README
# ==========================================
ws = wb.create_sheet('README')
ws['A1'] = 'PIVOT FRAMEWORK — GROUPBY / PIVOTBY variant'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Same Master_Inputs as the SUMIFS version. Pivots use ONE formula each that spills.'
ws['A2'].font = NOTE_FONT

notes = [
    '',
    'KEY DIFFERENCES FROM SUMIFS VERSION:',
    '  • Each pivot tab has ONE formula (in cell A5) that uses PIVOTBY or GROUPBY and spills.',
    '  • Auto-discovers unique values — no need to hardcode lines or years.',
    '  • Auto-handles new years / new lines / new entities added to Master_Inputs.',
    '  • Output cells DO NOT have stable addresses — they move as the spill resizes.',
    '',
    'LIMITATIONS YOU SHOULD KNOW BEFORE COMMITTING TO THIS:',
    '  1. ROW ORDER is alphabetical/numerical, NOT 1040 page-1 order. ',
    '     PIVOTBY sorts rows automatically and there is no easy way to force a',
    '     custom order like 1z → 2a → 2b → 3a → 3b → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 15.',
    '     Workarounds exist but require pre-sorting Master or post-processing.',
    '  2. NAMED RANGES on individual output cells are fragile. If a new year of data',
    '     is added, the spill grows and a named range pointing at cell M18 (which used',
    '     to be TaxableIncome) now points at the wrong number. ',
    '     This is the trade for getting auto-discovery.',
    '  3. EXCEL VERSION DEPENDENCY. PIVOTBY landed in Excel 365 in 2024. Users on',
    '     older Office versions will see #NAME? in the cells.',
    '',
    'BOTTOM LINE: This variant gives you "real pivot" behavior in formula form.',
    '  Great for exploration / cross-year reports.',
    '  Not great as the source for stable named-range LAMBDA inputs.',
    '',
    'RECOMMENDATION: Keep both files. Use SUMIFS version for the LAMBDA-feeding',
    '  named-range layer. Use this GROUPBY version for visual cross-year analysis.',
]
for i, n in enumerate(notes):
    ws.cell(row=4 + i, column=1, value=n)
widths(ws, [120])

# ==========================================
# Master_Inputs — same as the SUMIFS version (single canonical data source)
# ==========================================
ws = wb.create_sheet('Master_Inputs')
ws['A1'] = 'MASTER INPUTS — single canonical source (long-format, year-tagged)'
ws['A1'].font = TITLE_FONT

mi_cols = [
    'InputID', 'Year', 'ClientID', 'ClientName',
    'Bucket', 'Treatment_Profile', 'Source_Document', 'Activity_Type',
    'Provenance', 'Payor',
    'Baseline_Amount', 'Helper_Amount',
    'SE_Subject', 'NIIT_Class', 'QBI_Eligible',
    'Primary_Line', 'Helper_Treatment',
    'Consider', 'Notes',
]
hdr(ws, 4, mi_cols)

mi_sample = [
    ['CED|2024|Wages|01',  2024, 'CEDILLO', 'Ron Cedillo', 'Wages',             'W2_SCorpOwner',  'W-2',       'Baseline', 'PBC - Reviewed', 'Acme S-Corp', 153648, 0, 'No', 'Active', 'No', '1z', 'OWNER_PAY', '', ''],
    ['CED|2024|BI|01',     2024, 'CEDILLO', 'Ron Cedillo', 'Business Income',   'K1_PTP_Passive', 'K-1',       'Baseline', 'PBC - Reviewed', 'Cedillo Partnership', -100766, 0, 'No', 'Passive', 'Yes', '8', 'K1_SPLIT', '', ''],
    ['CED|2024|II|01',     2024, 'CEDILLO', 'Ron Cedillo', 'Investment Income', 'Div_Ordinary',   '1099-DIV',  'Baseline', 'PBC - Reviewed', 'Brokerage', 25922, 0, 'No', 'Portfolio', 'No', '3b', 'QUAL_DIV', '', ''],
    ['CED|2024|CG|01',     2024, 'CEDILLO', 'Ron Cedillo', 'Capital Gains',     'LTCG_Stock',     '1099-B',    'Baseline', 'PBC - Reviewed', 'Brokerage', 14487, 0, 'No', 'Portfolio', 'No', '7', 'LTCG_SPLIT', '', ''],
    ['SAM|2025|Wages|01',  2025, 'SAMPLE', 'Sample Client', 'Wages',             'W2_SCorpOwner',  'W-2',       'Baseline', 'Estimate - Preparer', 'SampleCo S-Corp', 100000, 100000, 'No', 'Active', 'No', '1z', 'OWNER_PAY', '', ''],
    ['SAM|2025|BI|01',     2025, 'SAMPLE', 'Sample Client', 'Business Income',   'K1_SCorp_Active','K-1',       'Baseline', 'PY Rolled Forward', 'SampleCo S-Corp K-1', 200000, 0, 'No', 'Active', 'Yes', '8', 'K1_SPLIT', '', ''],
    ['SAM|2025|II_Div|01', 2025, 'SAMPLE', 'Sample Client', 'Investment Income', 'Div_Qualified',  '1099-DIV',  'Baseline', 'PBC - Received', 'Brokerage', 10000, 7000, 'No', 'Portfolio', 'No', '3b', 'QUAL_DIV', '', ''],
    ['SAM|2025|CG|01',     2025, 'SAMPLE', 'Sample Client', 'Capital Gains',     'LTCG_Stock',     '1099-B',    'Baseline', 'PBC - Requested', 'Brokerage', 25000, 0, 'No', 'Portfolio', 'No', '7', 'LTCG_SPLIT', '', ''],
    ['SAM|2025|Itm|01',    2025, 'SAMPLE', 'Sample Client', 'Itemized',          'Itm_SALT',       'Property Tax Receipt', 'Baseline', 'PBC - Received', '', 10000, 0, 'No', 'N/A', 'No', '12', 'SALT', '', ''],
    ['SAM|2025|Strategy|CostSeg|01', 2025, 'SAMPLE', 'Sample Client', 'Business Income', 'SchE_Rental', '', 'Strategy', 'Estimate - Preparer', '', -80000, 0, 'No', 'Passive', 'No', '8', 'PASSIVE', '', 'Cost Seg STD-012'],
]
for i, row in enumerate(mi_sample):
    r = 5 + i
    for j, v in enumerate(row):
        c = ws.cell(row=r, column=1 + j, value=v); c.fill = INPUT_FILL

tbl = Table(displayName='tblMaster_Inputs', ref=f'A4:{get_column_letter(len(mi_cols))}{4+len(mi_sample)}')
tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
ws.add_table(tbl)
widths(ws, [22, 7, 11, 18, 18, 22, 22, 14, 18, 22, 14, 14, 11, 12, 13, 11, 18, 22, 22])
ws.freeze_panes = 'A5'

# ==========================================
# PIVOT — by Primary_Line × Year (PIVOTBY)
# ==========================================
ws = wb.create_sheet('Pivot_PIVOTBY')
ws['A1'] = 'PIVOTBY — Primary_Line × Year (one formula, auto-spills)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Single formula in A5. Auto-discovers all Primary_Line values and Year values present in Master.'
ws['A2'].font = NOTE_FONT
ws['A3'] = 'Notice: row order is automatic (alphabetical/numerical), not 1040 order. Years auto-discover as columns.'
ws['A3'].font = NOTE_FONT

# PIVOTBY syntax: PIVOTBY(row_fields, col_fields, values, function, [field_headers], [row_totals], [col_totals], [sort_order_row], [sort_order_col], [filter_array])
ws['A5'] = '=PIVOTBY(tblMaster_Inputs[Primary_Line], tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 0)'
widths(ws, [14] * 10)

# ==========================================
# PIVOT — by Bucket × Year
# ==========================================
ws = wb.create_sheet('Pivot_ByBucket')
ws['A1'] = 'PIVOTBY — Bucket × Year (one formula, auto-spills)'
ws['A1'].font = TITLE_FONT
ws['A5'] = '=PIVOTBY(tblMaster_Inputs[Bucket], tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 0)'
widths(ws, [22] + [14] * 9)

# ==========================================
# PIVOT — by Treatment_Profile × Year (detailed)
# ==========================================
ws = wb.create_sheet('Pivot_ByProfile')
ws['A1'] = 'PIVOTBY — Treatment_Profile × Year (one formula, auto-spills)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Most detailed — one row per Treatment_Profile present in Master.'
ws['A2'].font = NOTE_FONT
ws['A5'] = '=PIVOTBY(tblMaster_Inputs[Treatment_Profile], tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 0)'
widths(ws, [25] + [14] * 9)

# ==========================================
# PIVOT — Activity_Type × Year (Baseline vs. Strategy split)
# ==========================================
ws = wb.create_sheet('Pivot_ActivityType')
ws['A1'] = 'PIVOTBY — Activity_Type × Year (separates Baseline from Strategy)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'See the dollar impact of strategies year-over-year, separated from baseline.'
ws['A2'].font = NOTE_FONT
ws['A5'] = '=PIVOTBY(tblMaster_Inputs[Activity_Type], tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 0)'
widths(ws, [16] + [14] * 9)

# ==========================================
# PIVOT — Bucket + Activity_Type × Year (cross-cut)
# ==========================================
ws = wb.create_sheet('Pivot_BucketByType')
ws['A1'] = 'PIVOTBY — Bucket + Activity_Type × Year (cross-cut)'
ws['A1'].font = TITLE_FONT
ws['A2'] = 'Multi-field rows: see Baseline vs. Strategy within each bucket, across years.'
ws['A2'].font = NOTE_FONT
# Multi-field row dim: use a 2-column range
ws['A5'] = '=PIVOTBY(CHOOSECOLS(tblMaster_Inputs[#All], MATCH("Bucket", tblMaster_Inputs[#Headers], 0), MATCH("Activity_Type", tblMaster_Inputs[#Headers], 0)), tblMaster_Inputs[Year], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0, 0)'
widths(ws, [20, 16] + [14] * 8)

# ==========================================
# GROUPBY — single grouping by Primary_Line (all-year sum)
# ==========================================
ws = wb.create_sheet('GroupBy_TotalByLine')
ws['A1'] = 'GROUPBY — Primary_Line, all-year total (no year breakout)'
ws['A1'].font = TITLE_FONT
ws['A5'] = '=GROUPBY(tblMaster_Inputs[Primary_Line], tblMaster_Inputs[Baseline_Amount], SUM, 3, 0)'
widths(ws, [14, 20])

# Order sheets
order = ['README', 'Master_Inputs', 'Pivot_PIVOTBY', 'Pivot_ByBucket', 'Pivot_ByProfile',
         'Pivot_ActivityType', 'Pivot_BucketByType', 'GroupBy_TotalByLine']
wb._sheets = [wb[name] for name in order]

wb.save(OUT)
print(f'Saved: {OUT}')
print(f'Sheets: {wb.sheetnames}')
