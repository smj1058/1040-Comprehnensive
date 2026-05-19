"""Phase 3v7 — Dashboard selector fix + Phase 3e (Framework_Ref + Property Appendix).

Part A: Tax_Plan_Dashboard year selector
  - Change C4 from =Active_Year formula to a static value 2025
  - Keep the dropdown
  - Update subtitle so user knows they can pick any year freely
  - Add "Sync to Active_Year" cell next to it (manual: user types =Active_Year)

Part B: Phase 3e (Glossary merge dropped — keeping Glossary separate
        because text definitions and numeric rate tables are conceptually
        distinct and a merge would muddy both)
  - Framework_Ref: add column F "Jeff STD-ID" (placeholder mapping)
  - New "Property_Appendix" sheet for per-property reference data
    (cost basis, depreciation schedule, REPS hours)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v6_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v7_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# Styles used in multiple places
title_font     = Font(name='Calibri', size=18, bold=True, color='1F4E79')
subtitle_font  = Font(name='Calibri', size=10, italic=True, color='7F7F7F')
section_font   = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill   = PatternFill('solid', fgColor='1F4E79')
hdr_font       = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill       = PatternFill('solid', fgColor='4472C4')
label_font     = Font(name='Calibri', size=10)
value_font     = Font(name='Calibri', size=10, color='1F4E79')
input_fill     = PatternFill('solid', fgColor='FFF2CC')
thin_border    = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)
center = Alignment(horizontal='center', vertical='center')
left   = Alignment(horizontal='left',   vertical='center')

# =====================================================================
# PART A — Tax_Plan_Dashboard selector fix
# =====================================================================
ws = wb['Tax_Plan_Dashboard']
print("\n--- Part A: Tax_Plan_Dashboard selector fix ---")

# Update subtitle
ws['B3'] = 'Pick any year from the dropdown below — the entire dashboard updates. Type =Active_Year in C4 to sync with Control_Panel.'
ws['B3'].font = subtitle_font

# C4 currently = =Active_Year. Replace with static value.
ws['C4'] = 2025
ws['C4'].font = Font(name='Calibri', size=10, bold=True, color='1F4E79')
ws['C4'].fill = input_fill
ws['C4'].alignment = center
ws['C4'].border = thin_border
ws['C4'].number_format = '0'

# Add hint cell next to it: "Active_Year on Control_Panel: 2025"
ws['D4'] = '(Active_Year on Control_Panel:'
ws['D4'].font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
ws['D4'].alignment = Alignment(horizontal='right', vertical='center')
ws['E4'] = '=Active_Year'
ws['E4'].font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
ws['E4'].alignment = Alignment(horizontal='left', vertical='center')
ws['E4'].number_format = '0")"'

print("  C4: =Active_Year → 2025 (static, dropdown still active)")
print("  Subtitle updated, hint added at D4/E4 showing current Active_Year")

# =====================================================================
# PART B.1 — Framework_Ref: add Jeff STD-ID cross-ref column
# =====================================================================
ws = wb['Framework_Ref']
print("\n--- Part B.1: Framework_Ref Jeff STD-ID cross-ref ---")

# Look for the strategy table header at row 19 (we saw: A19='Strategy', B19='Why this...')
# Verify
hdr_row = None
for r in range(15, 30):
    if ws.cell(row=r, column=1).value == 'Strategy':
        hdr_row = r
        break
print(f"  Strategy header row: {hdr_row}")

# The existing strategy table at Framework_Ref!A19:E? — add new column F
# F19: "Our STR-ID" (links to STR-001..STR-015 numbering on year sheets)
# G19: "Jeff STD-ID" (placeholder for mapping)
# H19: "Notes"

# First find the last row of the strategy section (rows where col A is "#N — ...")
strategy_rows = []
for r in range(hdr_row + 1, ws.max_row + 1):
    val = ws.cell(row=r, column=1).value
    if isinstance(val, str) and val.startswith('#'):
        strategy_rows.append((r, val))

print(f"  Found {len(strategy_rows)} strategy rows")
for r, v in strategy_rows[:5]:
    print(f"    row {r}: {v[:60]}")

# Add new columns F (Our STR-ID), G (Jeff STD-ID), H (Notes)
hdr_cells = [
    (hdr_row, 6, 'Our STR-ID'),
    (hdr_row, 7, 'Jeff STD-ID'),
    (hdr_row, 8, 'Cross-Ref Notes'),
]
for r, c, val in hdr_cells:
    cell = ws.cell(row=r, column=c, value=val)
    cell.font = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    cell.fill = PatternFill('solid', fgColor='4472C4')
    cell.alignment = center
    cell.border = thin_border

# Populate STR-* and (placeholder) STD-* for each strategy row
# Our numbering = order in the strategy list, STR-001..STR-NNN
# Jeff's numbering is unknown until we can compare workbooks — leave blank with TBD
str_mapping = {
    '#1':  ('STR-001', 'STD-001?', 'Entity structuring — verify against Jeff Tab 1'),
    '#2':  ('STR-002', 'STD-002?', 'Wage optimization — likely Jeff #1 in his ordering'),
    '#3':  ('STR-003', 'STD-003?', 'Retirement contributions'),
    '#4':  ('STR-004', 'STD-004?', 'Cost segregation / bonus depreciation'),
    '#5':  ('STR-005', 'STD-005?', 'Low-hanging fruit (Augusta, accountable plan, MERP)'),
    '#6':  ('STR-006', '—',        'Placeholder row — clarify before mapping'),
    '#7':  ('STR-007', 'STD-007?', 'PTET election'),
    '#8':  ('STR-008', '—',        'Placeholder row — clarify before mapping'),
    '#9':  ('STR-009', 'STD-009?', 'Hire children'),
    '#10': ('STR-010', 'STD-010?', 'Entity restructure'),
    '#11': ('STR-011', 'STD-011?', 'TBD'),
    '#12': ('STR-012', 'STD-012?', 'TBD'),
    '#13': ('STR-013', 'STD-013?', 'R&D credit'),
    '#14': ('STR-014', 'STD-014?', 'TBD'),
    '#15': ('STR-015', 'STD-015?', 'TBD'),
}

mapped_count = 0
for r, v in strategy_rows:
    # Extract leading #N token
    token = v.split(' ')[0].split('—')[0].strip()
    mapping = str_mapping.get(token)
    if mapping:
        our_id, jeff_id, note = mapping
        ws.cell(row=r, column=6, value=our_id).font = label_font
        ws.cell(row=r, column=6).alignment = center
        ws.cell(row=r, column=6).border = thin_border
        ws.cell(row=r, column=7, value=jeff_id).font = label_font
        ws.cell(row=r, column=7).alignment = center
        ws.cell(row=r, column=7).border = thin_border
        ws.cell(row=r, column=8, value=note).font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
        ws.cell(row=r, column=8).alignment = left
        ws.cell(row=r, column=8).border = thin_border
        mapped_count += 1

print(f"  Populated {mapped_count} STR/STD cross-ref rows")

# Set column widths for new columns
ws.column_dimensions['F'].width = 12
ws.column_dimensions['G'].width = 12
ws.column_dimensions['H'].width = 50

# =====================================================================
# PART B.2 — New Property_Appendix sheet
# =====================================================================
print("\n--- Part B.2: Property_Appendix new sheet ---")

# Position: insert after Carryovers (which is the property/carryforward sheet)
if 'Property_Appendix' in wb.sheetnames:
    del wb['Property_Appendix']
ws = wb.create_sheet('Property_Appendix')

# Position right after Carryovers
target_idx = wb.sheetnames.index('Carryovers') + 1
current_idx = wb.sheetnames.index('Property_Appendix')
if current_idx != target_idx:
    wb.move_sheet('Property_Appendix', offset=target_idx - current_idx)
print(f"  Property_Appendix positioned at index {wb.sheetnames.index('Property_Appendix')} (after Carryovers)")

ws.sheet_properties.tabColor = 'C00000'  # red — reference / data input

# Title
ws['B2'] = 'PROPERTY APPENDIX'
ws['B2'].font = title_font
ws['B3'] = 'Per-property reference data: cost basis, placed-in-service, cost seg, REPS hours, REPS election. Drives Schedule E, depreciation, and material participation tests.'
ws['B3'].font = subtitle_font

# Section A: Property Master List
ws.merge_cells('B5:N5')
ws['B5'] = '▸ SECTION A — PROPERTY MASTER LIST'
ws['B5'].font = section_font
ws['B5'].fill = section_fill
ws['B5'].alignment = left

property_headers = [
    'Property #',
    'Address / Name',
    'Type',
    'Entity / Owner',
    'Acquisition Date',
    'Total Cost Basis',
    'Land Allocation',
    'Building Basis',
    'Cost Seg Done?',
    'Cost Seg Y1 %',
    'Placed-In-Service',
    'Disposition Date',
    'REPS Hours (TY)',
    'Notes',
]
for i, h in enumerate(property_headers):
    c = ws.cell(row=7, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin_border

# Data validation: Type dropdown
dv_type = DataValidation(type='list',
    formula1='"Long-Term Rental,Short-Term Rental,Commercial,Mixed-Use,Personal Residence,Land,Other"',
    allow_blank=True)
dv_type.add('D8:D100')
ws.add_data_validation(dv_type)

# Data validation: Cost Seg Done?
dv_yn = DataValidation(type='list', formula1='"Yes,No,In Progress"', allow_blank=True)
dv_yn.add('J8:J100')
ws.add_data_validation(dv_yn)

# Sample row showing what to enter (row 8 — sample property)
sample = [
    'P-001',
    '123 Main St, Salt Lake City UT',
    'Long-Term Rental',
    'Holding LLC',
    '2024-03-15',
    500000,
    100000,
    400000,
    'Yes',
    0.25,
    '2024-03-15',
    None,
    750,
    'Cost seg study by ABC Eng; 5/7/15-year reclass = 25%',
]
for i, v in enumerate(sample):
    cell = ws.cell(row=8, column=2+i, value=v)
    cell.font = Font(name='Calibri', size=9, italic=True, color='808080')
    cell.alignment = center
    cell.border = thin_border
    if i in (5, 6, 7):
        cell.number_format = '"$"#,##0'
    elif i == 9:
        cell.number_format = '0.00%'

# Input rows (rows 9-30) — empty, formatted
for r in range(9, 31):
    for c in range(2, 16):
        cell = ws.cell(row=r, column=c)
        cell.fill = input_fill
        cell.border = thin_border
        cell.font = label_font
        if c in (7, 8, 9):
            cell.number_format = '"$"#,##0'
        elif c == 11:
            cell.number_format = '0.00%'

# Column widths
widths = [4, 10, 35, 18, 16, 14, 14, 14, 14, 12, 12, 14, 14, 12, 30]
for i, w in enumerate(widths):
    ws.column_dimensions[get_column_letter(i+1)].width = w

# Section B: REPS Material Participation Tracker
ws.merge_cells('B33:N33')
ws['B33'] = '▸ SECTION B — REPS MATERIAL PARTICIPATION (per Reg §1.469-5T)'
ws['B33'].font = section_font
ws['B33'].fill = section_fill
ws['B33'].alignment = left

# REPS notes
ws['B35'] = 'REPS qualification requires:'
ws['B35'].font = Font(name='Calibri', size=10, bold=True)
ws['B36'] = '  (1) >50% of personal services across all trades/businesses in real property trades/businesses'
ws['B37'] = '  (2) >750 hours in real property trades/businesses in which taxpayer materially participates'
ws['B38'] = 'Material participation per §1.469-5T: 7 tests (500hr / substantially all / >100hr+nobody-more / etc.)'
ws['B39'] = 'Grouping election (§1.469-4): combine multiple rentals as a single activity for material participation test.'
for r in [36, 37, 38, 39]:
    ws.cell(row=r, column=2).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')

reps_headers = [
    'Activity Description',
    'Property #(s)',
    'Hours TY',
    'Hours PY',
    'Material Particip. Test',
    'Notes',
]
for i, h in enumerate(reps_headers):
    c = ws.cell(row=41, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin_border

dv_mp = DataValidation(type='list',
    formula1='"Test 1: 500+ hrs,Test 2: Substantially all,Test 3: >100 hrs & nobody-more,Test 4: Significant participation,Test 5: 5-of-10 prior yrs,Test 6: Personal service,Test 7: Facts & circumstances"',
    allow_blank=True)
dv_mp.add('F42:F60')
ws.add_data_validation(dv_mp)

for r in range(42, 61):
    for c in range(2, 8):
        cell = ws.cell(row=r, column=c)
        cell.fill = input_fill
        cell.border = thin_border
        cell.font = label_font
        if c in (4, 5):
            cell.number_format = '#,##0'

# Section C: §1.469-4 Grouping Election Tracker
ws.merge_cells('B63:N63')
ws['B63'] = '▸ SECTION C — §1.469-4 GROUPING ELECTION TRACKER'
ws['B63'].font = section_font
ws['B63'].fill = section_fill
ws['B63'].alignment = left

ws['B65'] = 'If election made: attach written statement to first return where grouping is reflected. Cannot revoke without IRS consent.'
ws['B65'].font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')

grouping_headers = [
    'Election Year',
    'Group Description',
    'Properties Included',
    'Filing Status (Single/Combined)',
    'Notes',
]
for i, h in enumerate(grouping_headers):
    c = ws.cell(row=67, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin_border

for r in range(68, 80):
    for c in range(2, 7):
        cell = ws.cell(row=r, column=c)
        cell.fill = input_fill
        cell.border = thin_border
        cell.font = label_font

print("  Property_Appendix built: 3 sections (Master List, REPS, Grouping)")

# =====================================================================
# Save
# =====================================================================
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Tax_Plan_Dashboard']
print(f"\nVerification — Tax_Plan_Dashboard C4 (year selector): {ws2['C4'].value!r}")
print(f"  E4 (Active_Year hint): {ws2['E4'].value!r}")

ws2 = wb2['Framework_Ref']
print(f"\nFramework_Ref column F header: {ws2.cell(row=19, column=6).value!r}")
print(f"  row 20 cross-ref: F={ws2.cell(row=20, column=6).value!r}  G={ws2.cell(row=20, column=7).value!r}")

ws2 = wb2['Property_Appendix']
print(f"\nProperty_Appendix B2 title: {ws2['B2'].value!r}")
print(f"  B5 section: {ws2['B5'].value!r}")
print(f"  B33 section: {ws2['B33'].value!r}")
print(f"  B63 section: {ws2['B63'].value!r}")
print(f"  Sheet position: index {wb2.sheetnames.index('Property_Appendix')}")
print(f"  Sheets: {wb2.sheetnames}")
