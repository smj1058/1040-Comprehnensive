"""Phase 3v11 — Year-sheet catalog validator (Path A — safe additive).

For each of Y2023..Y2028, add:

  1. Data validation on A6:A20 (StrategyID) — dropdown of catalog STR-IDs
  2. Five new columns R-V (outside tblY*_Strategies, no table extension):
       R: Catalog Name      (VLOOKUP from Master_Strategies)
       S: Catalog TargetLine (Impact 1)
       T: Catalog CounterLine (Impact 2 TargetLine, if multi-impact)
       U: Catalog Sign       (Impact 1 sign)
       V: Drift Check        ("OK" / "Name drift" / "Line drift" / "Counter drift")

Existing tblY*_Strategies (A5:H20) is NOT modified. The 96 downstream
SUMIFS keep working unchanged. Users get a picker + side-by-side comparison
of what the catalog says vs. what they typed.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v10_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v11_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# Catalog STR-IDs (15 from year sheets, but pull from catalog at runtime to stay in sync)
ws_cat = wb['Master_Strategies']
catalog_ids = []
for r in range(8, 30):
    v = ws_cat.cell(row=r, column=2).value
    if v and v not in catalog_ids:
        catalog_ids.append(v)
print(f"  Catalog STR-IDs in use: {len(catalog_ids)} → {catalog_ids[:5]}...")

# Styles
hdr_font   = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill   = PatternFill('solid', fgColor='C00000')   # red header to signal "validator"
label_font = Font(name='Calibri', size=10)
warn_font  = Font(name='Calibri', size=10, bold=True, color='C00000')
ok_font    = Font(name='Calibri', size=10, color='548235')
center     = Alignment(horizontal='center', vertical='center')
left       = Alignment(horizontal='left',   vertical='center')
thin       = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)
warn_fill = PatternFill('solid', fgColor='FCE4D6')   # light red for drift
ok_fill   = PatternFill('solid', fgColor='E2EFDA')   # light green for OK

year_sheets = ['Y2023', 'Y2024', 'Y2025', 'Y2026', 'Y2027', 'Y2028']

for sn in year_sheets:
    ws = wb[sn]
    print(f"\n--- {sn} ---")

    # 1. Data validation on A6:A20 — STR-ID dropdown
    str_id_list = ','.join(catalog_ids)
    dv = DataValidation(type='list', formula1=f'"{str_id_list}"', allow_blank=True)
    dv.add('A6:A20')
    ws.add_data_validation(dv)
    print(f"  Added STR-ID dropdown on A6:A20")

    # 2. Headers at row 5, columns R-V
    headers = [
        ('R', 'Catalog Name'),
        ('S', 'Catalog Line'),
        ('T', 'Catalog Counter'),
        ('U', 'Catalog Sign'),
        ('V', 'Drift Check'),
    ]
    for col_letter, hdr in headers:
        cell = ws[f'{col_letter}5']
        cell.value = hdr
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = center
        cell.border = thin

    # 3. Formulas in R6:V20
    # Catalog at Master_Strategies!$B$8:$L$26 (sorted by Strategy_ID then Impact_Num)
    cat_range = 'Master_Strategies!$B$8:$L$26'
    cat_id_col  = 'Master_Strategies!$B$8:$B$26'
    cat_imp_col = 'Master_Strategies!$C$8:$C$26'
    cat_name_col = 'Master_Strategies!$D$8:$D$26'
    cat_line_col = 'Master_Strategies!$G$8:$G$26'
    cat_sign_col = 'Master_Strategies!$I$8:$I$26'

    for r in range(6, 21):
        # R: Catalog Name — VLOOKUP first match (which is Impact_Num=1 since catalog is sorted)
        ws.cell(row=r, column=18,
            value=f'=IFERROR(VLOOKUP($A{r},{cat_range},3,FALSE),"")').font = label_font
        ws.cell(row=r, column=18).alignment = left
        ws.cell(row=r, column=18).border = thin

        # S: Catalog TargetLine (Impact 1) — VLOOKUP col 6 (G is the 6th column from B)
        ws.cell(row=r, column=19,
            value=f'=IFERROR(VLOOKUP($A{r},{cat_range},6,FALSE),"")').font = label_font
        ws.cell(row=r, column=19).alignment = center
        ws.cell(row=r, column=19).border = thin

        # T: Catalog CounterLine (Impact 2 TargetLine if multi-impact)
        #    Find next row after first match; check it's same STR-ID; return its TargetLine
        ws.cell(row=r, column=20,
            value=(
                f'=IF($A{r}="","",IF(COUNTIF({cat_id_col},$A{r})>1,'
                f'INDEX({cat_line_col},MATCH($A{r},{cat_id_col},0)+1),""))'
            )).font = label_font
        ws.cell(row=r, column=20).alignment = center
        ws.cell(row=r, column=20).border = thin

        # U: Catalog Sign (Impact 1) — VLOOKUP col 8 (I is the 8th column from B)
        ws.cell(row=r, column=21,
            value=f'=IFERROR(VLOOKUP($A{r},{cat_range},8,FALSE),"")').font = label_font
        ws.cell(row=r, column=21).alignment = center
        ws.cell(row=r, column=21).border = thin

        # V: Drift Check — compare B, C, G against catalog values
        #    If A blank: "" (nothing to check)
        #    If catalog Name doesn't match B: "Name drift"
        #    If catalog Line doesn't match C: "Line drift"
        #    If catalog Counter doesn't match G (when both present): "Counter drift"
        #    Else: "OK"
        ws.cell(row=r, column=22,
            value=(
                f'=IF($A{r}="","",'
                f'IF($R{r}="","Unknown ID",'
                f'IF($B{r}<>$R{r},"Name drift",'
                f'IF($C{r}<>$S{r},"Line drift",'
                f'IF(AND($T{r}<>"",$G{r}<>"",$G{r}<>$T{r}),"Counter drift","OK")))))'
            )).font = label_font
        ws.cell(row=r, column=22).alignment = center
        ws.cell(row=r, column=22).border = thin

    # 4. Conditional formatting on V6:V20 — green for OK, red for drift/unknown
    ws.conditional_formatting.add(
        f'V6:V20',
        CellIsRule(operator='equal', formula=['"OK"'], fill=ok_fill, font=ok_font)
    )
    ws.conditional_formatting.add(
        f'V6:V20',
        CellIsRule(operator='notEqual', formula=['"OK"'], fill=warn_fill, font=warn_font)
    )
    # But that 2nd rule fires for blanks too. Refine: only color non-blank drift rows.
    # Add a higher-priority rule for blank → no formatting.
    ws.conditional_formatting.add(
        f'V6:V20',
        CellIsRule(operator='equal', formula=['""'], fill=PatternFill(), font=Font())
    )

    # 5. Column widths
    for col_letter, width in [('R', 26), ('S', 12), ('T', 14), ('U', 10), ('V', 16)]:
        ws.column_dimensions[col_letter].width = width

    print(f"  Wrote R-V validator columns on rows 6-20 (15 strategy rows)")

# Save
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify against Y2025
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Y2025']
print(f"\nVerification — Y2025 sample (row 6, STR-001):")
print(f"  A6 (typed): {ws2['A6'].value!r}")
print(f"  B6 (typed name): {ws2['B6'].value!r}")
print(f"  C6 (typed line): {ws2['C6'].value!r}")
print(f"  G6 (typed counter): {ws2['G6'].value!r}")
print(f"  R6 (catalog name formula): {ws2['R6'].value!r}")
print(f"  S6 (catalog line formula): {ws2['S6'].value!r}")
print(f"  T6 (catalog counter formula): {ws2['T6'].value!r}")
print(f"  U6 (catalog sign formula): {ws2['U6'].value!r}")
print(f"  V6 (drift check): {ws2['V6'].value!r}")
print()
print(f"\nVerification — Y2025 row 14 (STR-009 Hire Children — multi-impact):")
print(f"  A14: {ws2['A14'].value!r}")
print(f"  G14 (typed counter): {ws2['G14'].value!r}")
print(f"  T14 (catalog counter formula): {ws2['T14'].value!r}")

# Confirm table NOT modified
print()
print(f"tblY2025_Strategies ref (should still be A5:H20): "
      f"{[t.ref for t in ws2.tables.values() if 'Strategies' in t.name][0]}")
