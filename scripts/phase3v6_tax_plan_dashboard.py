"""Phase 3b — Tax_Plan_Dashboard restructure to Jeff 4-box pattern.

Strategy: full rebuild. The existing dashboard mixed headline-metrics
columns (B-E rows 5-13), business breakdown (B-E rows 15-19), and chart
data (H-K rows 6-19) along with strategy summary (B-F rows 37-49). Two
bar charts ("Income by 1040 Line", "Business Income by Treatment") pulled
from the H-K block.

New layout — mirrors year-sheet At-a-Glance via INDIRECT('Y'&Active_Year&'!...'):

  B2:  Title
  B3:  Subtitle
  B4:  Year (=Active_Year, override allowed)

  BOX 1 — THE HEADLINE              (B6:E15,  4 cols)
  BOX 2 — STRATEGY MARGINAL SAVINGS (G6:K28,  5 cols)
  BOX 3 — TAX PLAN EXECUTION        (B18:E22, 4 cols)
  BOX 4 — CHECKLIST + TAKE-HOME     (G31:K52, 5 cols)

All numeric pulls go through INDIRECT so the dashboard follows
Active_Year on Control_Panel.

Charts are NOT restored. Visual_Pivot_* sheets already cover that need
and the bar charts here were tied to the old chart-data block, which is
gone now. User can re-add charts on top of the new boxes if desired.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from copy import copy

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v5_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v6_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)
ws = wb['Tax_Plan_Dashboard']

# ----------------------------------------------------------------------
# Wipe the slate
# ----------------------------------------------------------------------
for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
    for cell in row:
        cell.value = None
        cell.font = Font()
        cell.fill = PatternFill()
        cell.border = Border()
        cell.alignment = Alignment()
        cell.number_format = 'General'

# Drop existing charts
ws._charts = []
# Drop existing data validations (we'll re-add)
ws.data_validations.dataValidation = []

print("  Cleared all cells, charts, and data validations")

# ----------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------
title_font     = Font(name='Calibri', size=18, bold=True, color='1F4E79')
subtitle_font  = Font(name='Calibri', size=10, italic=True, color='7F7F7F')
box_title_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
box_title_fill = PatternFill('solid', fgColor='1F4E79')
hdr_font       = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill       = PatternFill('solid', fgColor='4472C4')
label_font     = Font(name='Calibri', size=10)
value_font     = Font(name='Calibri', size=10, color='1F4E79')
total_font     = Font(name='Calibri', size=10, bold=True, color='1F4E79')
total_fill     = PatternFill('solid', fgColor='DDEBF7')
input_fill     = PatternFill('solid', fgColor='FFF2CC')
thin_border    = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)
center = Alignment(horizontal='center', vertical='center')
right  = Alignment(horizontal='right',  vertical='center')
left   = Alignment(horizontal='left',   vertical='center')

dollar_fmt = '"$"#,##0;("$"#,##0);"-"'
pct_fmt    = '0.00%'

def style_box_title(cell):
    cell.font = box_title_font
    cell.fill = box_title_fill
    cell.alignment = left

def style_header(cell):
    cell.font = hdr_font
    cell.fill = hdr_fill
    cell.alignment = center
    cell.border = thin_border

def style_label(cell):
    cell.font = label_font
    cell.alignment = left
    cell.border = thin_border

def style_value(cell, fmt=dollar_fmt):
    cell.font = value_font
    cell.alignment = right
    cell.border = thin_border
    cell.number_format = fmt

def style_total(cell, fmt=dollar_fmt):
    cell.font = total_font
    cell.fill = total_fill
    cell.alignment = right
    cell.border = thin_border
    cell.number_format = fmt

# ----------------------------------------------------------------------
# Title block
# ----------------------------------------------------------------------
ws['B2'] = 'TAX PLAN DASHBOARD'
ws['B2'].font = title_font
ws['B3'] = 'Multi-year practitioner view. Follows Active_Year on Control_Panel. Override the year selector below if needed.'
ws['B3'].font = subtitle_font
ws['B4'] = 'Year:'
ws['B4'].font = label_font
ws['B4'].alignment = right
ws['C4'] = '=Active_Year'
ws['C4'].font = total_font
ws['C4'].fill = input_fill
ws['C4'].alignment = center
ws['C4'].border = thin_border

dv_year = DataValidation(type='list', formula1='"2023,2024,2025,2026,2027,2028"', allow_blank=False)
dv_year.add('C4')
ws.add_data_validation(dv_year)

# Helper: build the INDIRECT formula referencing the year currently in C4
def Y(cell):
    """Generate INDIRECT formula pulling from Y[C4]!cell."""
    return f'=INDIRECT("Y"&$C$4&"!{cell}")'

# ----------------------------------------------------------------------
# BOX 1 — THE HEADLINE (B6:E15)
# ----------------------------------------------------------------------
ws.merge_cells('B6:E6')
ws['B6'] = '▸ BOX 1 — THE HEADLINE'
style_box_title(ws['B6'])

headers_b1 = ['Metric', 'Without Planning', 'With Planning', 'Δ Savings']
for i, h in enumerate(headers_b1):
    c = ws.cell(row=7, column=2+i, value=h)
    style_header(c)

# Row → (label, without_formula, with_formula, delta_formula, format)
box1_rows = [
    ('Total Income',             Y('J125'),     Y('K125'),     '=C8-D8',   dollar_fmt),
    ('Taxable Income',           Y('J94'),      Y('K94'),      '=C9-D9',   dollar_fmt),
    ('Federal Income Tax',       f'=INDIRECT("Y"&$C$4&"!J97")+INDIRECT("Y"&$C$4&"!J107")',
                                 f'=INDIRECT("Y"&$C$4&"!K97")+INDIRECT("Y"&$C$4&"!K107")',
                                 '=C10-D10', dollar_fmt),
    ('Payroll & SE Taxes',       f'=INDIRECT("Y"&$C$4&"!J80")+INDIRECT("Y"&$C$4&"!J91")',
                                 f'=INDIRECT("Y"&$C$4&"!K80")+INDIRECT("Y"&$C$4&"!K91")',
                                 '=C11-D11', dollar_fmt),
    ('NIIT',                     Y('J114'),     Y('K114'),     '=C12-D12', dollar_fmt),
    ('Total Tax',                Y('J133'),     Y('K133'),     '=C13-D13', dollar_fmt),
    ('Effective Rate',           Y('J134'),     Y('K134'),     '=C14-D14', pct_fmt),
    ('After-Tax Cash',           '=C8-C13',     '=D8-D13',     '=D15-C15', dollar_fmt),
]
for i, (label, without_f, with_f, delta_f, fmt) in enumerate(box1_rows):
    r = 8 + i
    style_label(ws.cell(row=r, column=2, value=label))
    style_value(ws.cell(row=r, column=3, value=without_f), fmt)
    style_value(ws.cell(row=r, column=4, value=with_f), fmt)
    style_value(ws.cell(row=r, column=5, value=delta_f), fmt)

print("  Built Box 1 (B6:E15)")

# ----------------------------------------------------------------------
# BOX 2 — STRATEGY-BY-STRATEGY MARGINAL SAVINGS (G6:K28)
# ----------------------------------------------------------------------
ws.merge_cells('G6:K6')
ws['G6'] = '▸ BOX 2 — STRATEGY-BY-STRATEGY MARGINAL SAVINGS'
style_box_title(ws['G6'])

headers_b2 = ['#', 'Strategy', 'Status', 'Amount', 'Marginal Δ']
for i, h in enumerate(headers_b2):
    c = ws.cell(row=7, column=7+i, value=h)
    style_header(c)

# Strategy table on year sheets lives at rows 6-20, columns B (name), D (amount), E (status)
# Pull each row via INDIRECT
for i in range(15):
    src_row = 6 + i             # rows 6..20 on year sheet
    r = 8 + i                   # rows 8..22 on dashboard
    style_label(ws.cell(row=r, column=7, value=f'#{i+1}'))
    style_label(ws.cell(row=r, column=8, value=f'=INDIRECT("Y"&$C$4&"!B{src_row}")'))
    style_label(ws.cell(row=r, column=9, value=f'=INDIRECT("Y"&$C$4&"!E{src_row}")'))
    style_value(ws.cell(row=r, column=10, value=f'=IFERROR(INDIRECT("Y"&$C$4&"!D{src_row}"),0)'), dollar_fmt)
    # Marginal Δ = -Amount × 0.32 IF status is Committed/Implemented, else 0
    style_value(ws.cell(row=r, column=11,
        value=f'=IF(OR(I{r}="Committed",I{r}="Implemented"),-J{r}*0.32,0)'), dollar_fmt)

# Subtotal / Synergy / Plan Total rows
style_label(ws.cell(row=23, column=7, value=''))
ws.cell(row=23, column=8, value='Subtotal — Direct Strategy Savings').font = total_font
ws.cell(row=23, column=8).alignment = left
ws.cell(row=23, column=8).fill = total_fill
ws.cell(row=23, column=8).border = thin_border
style_total(ws.cell(row=23, column=11, value='=SUM(K8:K22)'), dollar_fmt)

ws.cell(row=24, column=8, value='Plan Synergy Adjustment (Canon v1.4 est.)').font = label_font
ws.cell(row=24, column=8).alignment = left
ws.cell(row=24, column=8).border = thin_border
style_value(ws.cell(row=24, column=11, value=0), dollar_fmt)
ws.cell(row=24, column=11).fill = input_fill

ws.cell(row=25, column=8, value='PLAN TOTAL').font = total_font
ws.cell(row=25, column=8).alignment = left
ws.cell(row=25, column=8).fill = total_fill
ws.cell(row=25, column=8).border = thin_border
style_total(ws.cell(row=25, column=11, value='=K23+K24'), dollar_fmt)

# Caveat
ws.merge_cells('G27:K27')
caveat = ws.cell(row=27, column=7,
    value='Marginal Δ = -Amount × 32% approx. Replace with KISS LAMBDA exact recalc when LAMBDAs install (Phase 3c).')
caveat.font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
caveat.alignment = left

print("  Built Box 2 (G6:K27)")

# ----------------------------------------------------------------------
# BOX 3 — TAX PLAN EXECUTION (B18:E23)
# ----------------------------------------------------------------------
ws.merge_cells('B17:E17')
ws['B17'] = '▸ BOX 3 — TAX PLAN EXECUTION'
style_box_title(ws['B17'])

headers_b3 = ['Metric', 'Without', 'With', 'Δ']
for i, h in enumerate(headers_b3):
    c = ws.cell(row=18, column=2+i, value=h)
    style_header(c)

style_label(ws.cell(row=19, column=2, value='Federal Income Tax'))
style_value(ws.cell(row=19, column=3, value='=C10'), dollar_fmt)
style_value(ws.cell(row=19, column=4, value='=D10'), dollar_fmt)
style_value(ws.cell(row=19, column=5, value='=C19-D19'), dollar_fmt)

style_label(ws.cell(row=20, column=2, value='Total Tax (all components)'))
style_value(ws.cell(row=20, column=3, value='=C13'), dollar_fmt)
style_value(ws.cell(row=20, column=4, value='=D13'), dollar_fmt)
style_value(ws.cell(row=20, column=5, value='=C20-D20'), dollar_fmt)

style_label(ws.cell(row=21, column=2, value='Effective Rate'))
style_value(ws.cell(row=21, column=3, value='=C14'), pct_fmt)
style_value(ws.cell(row=21, column=4, value='=D14'), pct_fmt)
style_value(ws.cell(row=21, column=5, value='=C21-D21'), pct_fmt)

style_total(ws.cell(row=22, column=2, value='TOTAL TAX SAVED'), 'General')
ws.cell(row=22, column=2).alignment = left
style_total(ws.cell(row=22, column=5, value='=E20'), dollar_fmt)

print("  Built Box 3 (B17:E22)")

# ----------------------------------------------------------------------
# BOX 4 — CHECKLIST + TAKE-HOME CASH (G30:K52)
# ----------------------------------------------------------------------
ws.merge_cells('G30:K30')
ws['G30'] = '▸ BOX 4 — STRATEGY CHECKLIST + TAKE-HOME CASH'
style_box_title(ws['G30'])

# Take-Home block (rows 31-34)
style_label(ws.cell(row=31, column=8, value='Take-Home Cash (Without)'))
style_value(ws.cell(row=31, column=11, value='=C15'), dollar_fmt)
style_label(ws.cell(row=32, column=8, value='Take-Home Cash (With)'))
style_value(ws.cell(row=32, column=11, value='=D15'), dollar_fmt)
style_total(ws.cell(row=33, column=8, value='Δ Take-Home (annual)'), 'General')
ws.cell(row=33, column=8).alignment = left
style_total(ws.cell(row=33, column=11, value='=E15'), dollar_fmt)
style_label(ws.cell(row=34, column=8, value='Effective Tax %'))
style_value(ws.cell(row=34, column=11, value='=D14'), pct_fmt)

# Checklist header
headers_b4 = ['Status', '#', 'Strategy', '', 'Status Text']
for i, h in enumerate(headers_b4):
    c = ws.cell(row=36, column=7+i, value=h)
    style_header(c)

# 15 checklist rows
for i in range(15):
    src_row = 6 + i
    r = 37 + i
    # Status icon
    icon_formula = (
        f'=IF(INDIRECT("Y"&$C$4&"!E{src_row}")="Implemented","☑",'
        f'IF(INDIRECT("Y"&$C$4&"!E{src_row}")="Committed","☑",'
        f'IF(INDIRECT("Y"&$C$4&"!E{src_row}")="Approved","▣",'
        f'IF(INDIRECT("Y"&$C$4&"!E{src_row}")="Proposed","☐","─"))))'
    )
    cell = ws.cell(row=r, column=7, value=icon_formula)
    cell.font = Font(name='Calibri', size=14, bold=True, color='1F4E79')
    cell.alignment = center
    cell.border = thin_border

    style_label(ws.cell(row=r, column=8, value=f'#{i+1}'))
    style_label(ws.cell(row=r, column=9, value=f'=INDIRECT("Y"&$C$4&"!B{src_row}")'))
    style_label(ws.cell(row=r, column=10, value=''))
    style_label(ws.cell(row=r, column=11, value=f'=INDIRECT("Y"&$C$4&"!E{src_row}")'))

# Legend
ws.merge_cells('G53:K53')
legend = ws.cell(row=53, column=7,
    value='Legend:  ☑ Implemented/Committed   ▣ Approved   ☐ Proposed   ─ Not selected')
legend.font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
legend.alignment = left

print("  Built Box 4 (G30:K53)")

# ----------------------------------------------------------------------
# Column widths
# ----------------------------------------------------------------------
ws.column_dimensions['A'].width = 2
ws.column_dimensions['B'].width = 30
ws.column_dimensions['C'].width = 16
ws.column_dimensions['D'].width = 16
ws.column_dimensions['E'].width = 16
ws.column_dimensions['F'].width = 3
ws.column_dimensions['G'].width = 10
ws.column_dimensions['H'].width = 26
ws.column_dimensions['I'].width = 14
ws.column_dimensions['J'].width = 14
ws.column_dimensions['K'].width = 16

ws.row_dimensions[2].height = 26
ws.row_dimensions[6].height = 22
ws.row_dimensions[17].height = 22
ws.row_dimensions[30].height = 22

# ----------------------------------------------------------------------
# Save
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Tax_Plan_Dashboard']
print("\nVerification — key cells:")
for coord in ['B2', 'C4', 'B6', 'G6', 'B17', 'G30', 'B8', 'C8', 'K8', 'G37', 'I37']:
    print(f"  {coord}: {ws2[coord].value!r}")
print(f"  Charts on sheet: {len(ws2._charts)}")
print(f"  Data validations: {len(ws2.data_validations.dataValidation)}")
