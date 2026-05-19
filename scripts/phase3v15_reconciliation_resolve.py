"""Phase 3v15 — Resolve 6 reconciliation items from phase3v9 Section E.

Applied fixes:
  RECON-1: STR-006 Roth Conversion TargetLine 1z → 4b
           (Roth conversion taxable amount belongs on Form 1040 Line 4b)
           Fixed on Y2023-Y2028 row 11 and Master_Strategies STR-006 row
  RECON-2: STR-014 SALT PTE Election TargetLine 12 → 8
           (PTET federally reduces K-1 income at entity level, not
           itemized deduction)
           Fixed on Y2023-Y2028 row 19 and Master_Strategies STR-014 row
  RECON-3: HSA Helper_Treatment confirmed in tblTreatmentProfileMap (row 599)
           No action needed
  RECON-4: STR-009 child Roth info-only row kept in catalog; year sheet
           stays single-row (CounterLine handles primary 2 impacts).
           Asymmetry documented.
  RECON-5: STR-010 catalog Description updated to emphasize "case-by-case"
  RECON-6: Add Bucket lookup column W6:W20 on each year sheet, pulling
           from Master_Strategies catalog by Strategy_ID

Section E of Master_Strategies updated to show RESOLVED status for each.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v14_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v15_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# ----------------------------------------------------------------------
# RECON-1 & RECON-2: TargetLine fixes on year sheets
# ----------------------------------------------------------------------
year_sheets = ['Y2023', 'Y2024', 'Y2025', 'Y2026', 'Y2027', 'Y2028']
for sn in year_sheets:
    ws = wb[sn]
    # STR-006 at row 11: C11 from "1z" to "4b"
    if ws['C11'].value == '1z':
        ws['C11'] = '4b'
        print(f"  {sn} C11 (STR-006 Roth TargetLine): 1z → 4b ✓")
    # STR-014 at row 19: C19 from 12 to 8
    if ws['C19'].value == 12 or ws['C19'].value == '12':
        ws['C19'] = 8
        print(f"  {sn} C19 (STR-014 PTE TargetLine): 12 → 8 ✓")

# ----------------------------------------------------------------------
# RECON-1 & RECON-2: Catalog fixes
# ----------------------------------------------------------------------
ws_cat = wb['Master_Strategies']
# Catalog uses TargetLine in column G (offset 6 from B). Find STR-006 and STR-014 rows.
# Catalog layout: B=Strategy_ID, C=Impact_Num, D=Name, E=Bucket, F=FW_Ref, G=TargetLine, H=HelperTreatment, I=Sign, J=Cap, K=Maturity, L=Description
for r in range(8, 28):
    sid = ws_cat.cell(row=r, column=2).value
    if sid == 'STR-006' and ws_cat.cell(row=r, column=7).value == '1z':
        ws_cat.cell(row=r, column=7, value='4b')
        # Update description to remove the "revisit TargetLine" note
        desc_cell = ws_cat.cell(row=r, column=12)
        if isinstance(desc_cell.value, str) and 'revisit TargetLine' in desc_cell.value:
            desc_cell.value = 'Trad → Roth conversion (creates taxable income on Line 4b)'
        print(f"  Master_Strategies STR-006 (row {r}) TargetLine: 1z → 4b ✓")
    if sid == 'STR-014' and (ws_cat.cell(row=r, column=7).value == '12' or ws_cat.cell(row=r, column=7).value == 12):
        ws_cat.cell(row=r, column=7, value='8')
        desc_cell = ws_cat.cell(row=r, column=12)
        if isinstance(desc_cell.value, str) and 'revisit TargetLine' in desc_cell.value:
            desc_cell.value = 'Pass-through entity pays state tax federally; reduces K-1 pass-through income at entity level (Line 8)'
        print(f"  Master_Strategies STR-014 (row {r}) TargetLine: 12 → 8 ✓")

# ----------------------------------------------------------------------
# RECON-5: Update STR-010 Description in catalog to emphasize case-by-case
# ----------------------------------------------------------------------
for r in range(8, 28):
    sid = ws_cat.cell(row=r, column=2).value
    impact = ws_cat.cell(row=r, column=3).value
    if sid == 'STR-010' and impact == 1:
        ws_cat.cell(row=r, column=12,
            value='CASE-BY-CASE: Restructure mechanics vary by entity type (S-Corp election, HoldCo over OpCo, F-reorg, P→S). Default fan-out 8↔1z is illustrative only — adjust per scenario.')
        print(f"  Master_Strategies STR-010 (row {r}) Description: case-by-case note ✓")
    if sid == 'STR-010' and impact == 2:
        ws_cat.cell(row=r, column=12,
            value='CASE-BY-CASE: Reasonable comp adjustment varies by entity transition; default counter on Line 1z is illustrative.')
        print(f"  Master_Strategies STR-010 (row {r}) Impact 2 Description: case-by-case note ✓")

# ----------------------------------------------------------------------
# RECON-6: Add Bucket lookup column W to year-sheet validator
# ----------------------------------------------------------------------
hdr_font = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill = PatternFill('solid', fgColor='C00000')
label_font = Font(name='Calibri', size=10)
center = Alignment(horizontal='center', vertical='center')
thin = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)

# Bucket = catalog column E (offset 4 from B, = col 4 in VLOOKUP)
for sn in year_sheets:
    ws = wb[sn]
    # Header
    ws.cell(row=5, column=23, value='Catalog Bucket').font = hdr_font
    ws.cell(row=5, column=23).fill = hdr_fill
    ws.cell(row=5, column=23).alignment = center
    ws.cell(row=5, column=23).border = thin
    # Formulas at W6:W20
    for r in range(6, 21):
        ws.cell(row=r, column=23,
            value=f'=IFERROR(VLOOKUP($A{r},Master_Strategies!$B$8:$L$26,4,FALSE),"")').font = label_font
        ws.cell(row=r, column=23).alignment = center
        ws.cell(row=r, column=23).border = thin
    ws.column_dimensions['W'].width = 14

print(f"  Added Bucket lookup column W6:W20 on {len(year_sheets)} year sheets")

# ----------------------------------------------------------------------
# Update Section E in Master_Strategies to show RESOLVED status
# ----------------------------------------------------------------------
# Find Section E header
section_e_row = None
for r in range(40, 100):
    v = ws_cat.cell(row=r, column=2).value
    if isinstance(v, str) and 'SECTION E' in v and 'RECONCILIATION' in v:
        section_e_row = r
        break

if section_e_row:
    # Update section title
    ws_cat.cell(row=section_e_row, column=2,
        value='▸ SECTION E — RECONCILIATION ITEMS (5 of 6 RESOLVED in v15)')
    print(f"  Section E header updated at row {section_e_row}")

    # Mark each ITEM-RECON row with resolution status (column C)
    # Find each ITEM-RECON-N
    resolutions = {
        'ITEM-RECON-1': 'RESOLVED: TargetLine 1z → 4b (Roth conversion canonical)',
        'ITEM-RECON-2': 'RESOLVED: TargetLine 12 → 8 (PTET reduces K-1 federally)',
        'ITEM-RECON-3': 'RESOLVED: HSA confirmed in tblTreatmentProfileMap row 599',
        'ITEM-RECON-4': 'KEPT AS-IS: catalog 3 impacts (full doc); year sheet single-row (CounterLine)',
        'ITEM-RECON-5': 'RESOLVED: catalog Description updated to "case-by-case"',
        'ITEM-RECON-6': 'RESOLVED: Bucket lookup added at year-sheet column W',
    }
    for r in range(section_e_row, section_e_row + 20):
        item_cell = ws_cat.cell(row=r, column=2)
        if isinstance(item_cell.value, str) and item_cell.value in resolutions:
            # Append resolution to the detail column (column D, currently merged D:L)
            detail = ws_cat.cell(row=r, column=4).value or ''
            new_detail = f"[v15] {resolutions[item_cell.value]}  |  ORIGINAL: {detail}"
            ws_cat.cell(row=r, column=4, value=new_detail)
            # Tint with green to signal resolution (except item 4 which is "kept as-is")
            if 'RESOLVED' in resolutions[item_cell.value]:
                ws_cat.cell(row=r, column=2).fill = PatternFill('solid', fgColor='E2EFDA')

# ----------------------------------------------------------------------
# Save + verify
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

wb2 = openpyxl.load_workbook(OUT_FILE)
print(f"\nVerification:")
ws = wb2['Y2025']
print(f"  Y2025!C11 (STR-006 Roth line): {ws['C11'].value!r}")
print(f"  Y2025!C19 (STR-014 PTE line): {ws['C19'].value!r}")
print(f"  Y2025!W5 (header): {ws['W5'].value!r}")
print(f"  Y2025!W6 (STR-001 bucket): {ws['W6'].value!r}")
ws = wb2['Master_Strategies']
# Find STR-006 row and check TargetLine
for r in range(8, 28):
    if ws.cell(row=r, column=2).value == 'STR-006':
        print(f"  Master_Strategies STR-006 (row {r}) TargetLine: {ws.cell(row=r, column=7).value!r}")
        break
for r in range(8, 28):
    if ws.cell(row=r, column=2).value == 'STR-014':
        print(f"  Master_Strategies STR-014 (row {r}) TargetLine: {ws.cell(row=r, column=7).value!r}")
        break
