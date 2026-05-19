"""Phase 3a — Control_Panel audit against Jeff Tab 1 §1-2 inputs.

Adds a new HOUSEHOLD DETAILS section between TAX PROFILE (ends row 21) and
ACTIVE YEAR SNAPSHOT (was row 23, becomes row 35). 12 new rows inserted at
row 22:

  Row 22: ▸ HOUSEHOLD DETAILS (section header)
  Row 23: Taxpayer Name
  Row 24: Spouse Name
  Row 25: Taxpayer 65+
  Row 26: Spouse 65+
  Row 27: Taxpayer Blind
  Row 28: Spouse Blind
  Row 29: Dependents — CTC Qualifying (under 17)
  Row 30: Dependents — ODC Qualifying (other)
  Row 31: Self-Employed Health Ins Eligible
  Row 32: Itemize Override
  Row 33: Prior Year Total Tax (safe harbor)

Also adds named ranges for the new fields so the calc engine can pick them
up by name.

Safe because:
- Only 3 named ranges hit Control_Panel and all are at rows 8, 11, 15
- Direct Control_Panel! refs from other sheets hit C19 (Dependent Children)
  and C21 (SSTB) — both above the insertion point
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v4_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v5_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)
ws = wb['Control_Panel']

# Pre-check: confirm we're at the right spot
assert ws['B21'].value == 'Business is SSTB?', f"Expected SSTB at B21, got {ws['B21'].value!r}"
assert ws['B23'].value == '▸ ACTIVE YEAR SNAPSHOT', f"Expected snapshot header at B23, got {ws['B23'].value!r}"
print("  Pre-check OK: SSTB at B21, ACTIVE YEAR SNAPSHOT at B23")

# Insert 12 rows at row 22. Existing row 22 (blank) → row 34. Existing row 23 (snapshot) → row 35.
ws.insert_rows(idx=22, amount=12)
print("  Inserted 12 rows at row 22")

# ----------------------------------------------------------------------
# Styles (match existing Control_Panel look)
# ----------------------------------------------------------------------
section_header_font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
field_label_font    = Font(name='Calibri', size=11, bold=False)
input_font          = Font(name='Calibri', size=11, bold=False, color='1F4E79')
input_fill          = PatternFill('solid', fgColor='FFF2CC')   # light yellow = user input
thin_border         = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)

# ----------------------------------------------------------------------
# Section header at row 22
# ----------------------------------------------------------------------
ws['B22'] = '▸ HOUSEHOLD DETAILS'
ws['B22'].font = section_header_font

# ----------------------------------------------------------------------
# 11 fields at rows 23-33: B = label, C = value, D = description
# ----------------------------------------------------------------------
fields = [
    # (row, label, default, description, named_range_name)
    (23, 'Taxpayer Name',                  'TAXPAYER',   'Used in Deliverable header',                   'Taxpayer_Name'),
    (24, 'Spouse Name',                    'SPOUSE',     'Only used if Filing_Status = MFJ',             'Spouse_Name'),
    (25, 'Taxpayer 65+',                   'No',         'Adds $1,550 to standard deduction (2024)',     'Taxpayer_65Plus'),
    (26, 'Spouse 65+',                     'No',         'Adds $1,550 to standard deduction (2024)',     'Spouse_65Plus'),
    (27, 'Taxpayer Blind',                 'No',         'Adds $1,550 to standard deduction (2024)',     'Taxpayer_Blind'),
    (28, 'Spouse Blind',                   'No',         'Adds $1,550 to standard deduction (2024)',     'Spouse_Blind'),
    (29, 'Dep — CTC Qualifying',           2,            'Children under 17 — $2,000 CTC each',          'Dep_CTC_Count'),
    (30, 'Dep — ODC Qualifying',           0,            'Other dependents — $500 ODC each',             'Dep_ODC_Count'),
    (31, 'Self-Employed Health Ins',       'No',         'Eligible to deduct SE health ins above-line',  'SE_Health_Ins_Eligible'),
    (32, 'Itemize Override',               'Auto',       'Auto / Force Itemize / Force Standard',        'Itemize_Override'),
    (33, 'Prior Year Total Tax',           0,            'For 110% safe harbor calc',                    'PY_Total_Tax'),
]

for row, label, default, desc, _ in fields:
    ws.cell(row=row, column=2, value=label).font = field_label_font
    cell = ws.cell(row=row, column=3, value=default)
    cell.font = input_font
    cell.fill = input_fill
    cell.border = thin_border
    if isinstance(default, (int, float)) and 'Tax' in label:
        cell.number_format = '"$"#,##0;("$"#,##0)'
    ws.cell(row=row, column=4, value=desc).font = Font(name='Calibri', size=10, italic=True, color='7F7F7F')

print(f"  Wrote 11 household fields rows 23-33")

# ----------------------------------------------------------------------
# Data validations for Y/N + Itemize Override dropdowns
# ----------------------------------------------------------------------
dv_yn = DataValidation(type='list', formula1='"Yes,No"', allow_blank=False)
dv_yn.add('C25:C28')   # T/S 65+, T/S Blind
dv_yn.add('C31')        # SE Health Ins
ws.add_data_validation(dv_yn)

dv_itemize = DataValidation(type='list', formula1='"Auto,Force Itemize,Force Standard"', allow_blank=False)
dv_itemize.add('C32')
ws.add_data_validation(dv_itemize)

print("  Added Y/N dropdowns on C25:C28, C31 and Itemize Override on C32")

# ----------------------------------------------------------------------
# Named ranges for the new fields
# ----------------------------------------------------------------------
for row, _, _, _, name in fields:
    if name in wb.defined_names:
        del wb.defined_names[name]
    dn = DefinedName(name=name, attr_text=f"Control_Panel!$C${row}")
    wb.defined_names[name] = dn

print(f"  Added {len(fields)} named ranges")

# ----------------------------------------------------------------------
# Save
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# ----------------------------------------------------------------------
# Verify
# ----------------------------------------------------------------------
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Control_Panel']
print("\nVerification:")
print(f"  B21 (should be SSTB): {ws2['B21'].value!r}")
print(f"  B22 (should be HOUSEHOLD header): {ws2['B22'].value!r}")
print(f"  B23 (should be Taxpayer Name): {ws2['B23'].value!r}")
print(f"  B33 (should be Prior Year Total Tax): {ws2['B33'].value!r}")
print(f"  B35 (should be ACTIVE YEAR SNAPSHOT - shifted): {ws2['B35'].value!r}")
print(f"  Named range Taxpayer_Name: {wb2.defined_names['Taxpayer_Name'].value!r}")
print(f"  Named range PY_Total_Tax: {wb2.defined_names['PY_Total_Tax'].value!r}")
print(f"  Named range Active_Year (should be unchanged C8): {wb2.defined_names['Active_Year'].value!r}")
