"""Phase 3v14 — Phase 3c-SE: add SE/FICA savings + CounterLine to fn_StrategyMarginal.

The v13 LAMBDA returned $0 for STR-001 net (Impact 1 -$25K Line 1z + Impact 2
+$25K Line 8 → ordinary tax nets out). The real STR-001 savings is the FICA
that's no longer owed on the moved wages: $25K × 15.3% ≈ $3,825.

This update:
  1. Adds counter_line parameter to fn_StrategyMarginal so a single call
     handles both primary impact and CounterLine (matches how year-sheet
     SUMIFS net the fan-out today)
  2. Adds FICA savings (15.3% × income change) when a wage line (1z) is
     affected on either primary or counter
  3. Updates Box 2 K-column formulas on all 6 year sheets + Tax_Plan_Dashboard
     to pass the CounterLine (column G on year sheet)

CAVEATS documented:
  - FICA flat 15.3% (no SS wage-base cap, no Medicare surtax)
  - Hire Children (STR-009 → counter on 1z) is treated as parent's
    income — actual child wages are on the child's separate return at
    child's bracket. UNDERSTATES STR-009 savings. Revisit later.
  - SE tax (sole-prop / partnership K-1) not modeled. S-Corp K-1 has
    no SE — correct for the default client context.
"""

import openpyxl
import re
from openpyxl.workbook.defined_name import DefinedName

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v13_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v14_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# ----------------------------------------------------------------------
# Updated fn_StrategyMarginal (now with counter_line)
# ----------------------------------------------------------------------
# Signature: (target_line, amount, counter_line, year, fs, ti_with_strats)
# Returns dollar savings (positive = savings, negative = added tax)

FN = (
    '_xlfn.LAMBDA(target_line,amount,counter_line,year,fs,ti_with_strats,'
    '_xlfn.LET('
    # PRIMARY impact on target_line
    'p_delta,-amount,'
    'p_credit,target_line="20",'
    'p_cg,target_line="7",'
    'p_info,OR(target_line="—",target_line=""),'
    'p_wages,target_line="1z",'
    'p_fed,'
        'IF(p_info,0,'
        'IF(p_credit,p_delta,'
        'IF(p_cg,'
            'TAX_CG(p_delta,ti_with_strats+p_delta,year,fs),'
            'TAX_ORD(ti_with_strats+p_delta,year,fs)-TAX_ORD(ti_with_strats,year,fs)))),'
    'p_fica,IF(p_wages,p_delta*0.153,0),'
    # COUNTER impact on counter_line (only if counter_line non-blank/non-zero)
    'has_c,AND(counter_line<>"",counter_line<>0),'
    'c_delta,IF(has_c,amount,0),'
    'c_wages,counter_line="1z",'
    'c_cg,counter_line="7",'
    'c_credit,counter_line="20",'
    'c_fed,'
        'IF(NOT(has_c),0,'
        'IF(c_credit,c_delta,'
        'IF(c_cg,'
            'TAX_CG(c_delta,ti_with_strats+c_delta,year,fs),'
            'TAX_ORD(ti_with_strats+c_delta,year,fs)-TAX_ORD(ti_with_strats,year,fs)))),'
    'c_fica,IF(AND(has_c,c_wages),c_delta*0.153,0),'
    'p_fed+p_fica+c_fed+c_fica))'
)

# Replace existing
if 'fn_StrategyMarginal' in wb.defined_names:
    del wb.defined_names['fn_StrategyMarginal']
wb.defined_names['fn_StrategyMarginal'] = DefinedName(
    name='fn_StrategyMarginal', attr_text=FN
)

opens = FN.count('(')
closes = FN.count(')')
print(f"  Installed fn_StrategyMarginal v2: {len(FN)} chars, parens {opens}={closes}  {'✓' if opens==closes else '✗'}")

# ----------------------------------------------------------------------
# Update At-a-Glance Box 2 on each year sheet to pass column G (CounterLine)
# ----------------------------------------------------------------------
year_sheets = [('Y2023', 2023), ('Y2024', 2024), ('Y2025', 2025),
               ('Y2026', 2026), ('Y2027', 2027), ('Y2028', 2028)]

for sn, yr in year_sheets:
    ws = wb[sn]
    for box_row in range(144, 159):
        strat_row = box_row - 138
        new = (
            f'=IF(OR(E{strat_row}="Committed",E{strat_row}="Implemented"),'
            f'fn_StrategyMarginal(C{strat_row},D{strat_row},G{strat_row},'
            f'{yr},Filing_Status,$K$94),0)'
        )
        ws.cell(row=box_row, column=11, value=new)
    # Update caveat at G162
    ws.cell(row=162, column=7,
        value='(Marginal Savings = fn_StrategyMarginal v2: federal ordinary + CG + credits + FICA on wage lines + CounterLine. Caveats in Setup_Guide.)'
    )

print(f"  Updated 90 year-sheet cells (Box 2 K-column rows 144-158 × 6 sheets)")

# ----------------------------------------------------------------------
# Update Tax_Plan_Dashboard Box 2 to also pull CounterLine from year sheet
# ----------------------------------------------------------------------
ws = wb['Tax_Plan_Dashboard']
for box_row in range(8, 23):
    strat_row = box_row - 2
    new = (
        f'=IF(OR(I{box_row}="Committed",I{box_row}="Implemented"),'
        f'fn_StrategyMarginal('
            f'INDIRECT("Y"&$C$4&"!C{strat_row}"),'
            f'J{box_row},'
            f'INDIRECT("Y"&$C$4&"!G{strat_row}"),'
            f'$C$4,Filing_Status,'
            f'INDIRECT("Y"&$C$4&"!$K$94")),'
        f'0)'
    )
    ws.cell(row=box_row, column=11, value=new)

# Update caveat
for r in range(25, 35):
    v = ws.cell(row=r, column=7).value
    if isinstance(v, str) and 'Marginal Δ' in v:
        ws.cell(row=r, column=7,
            value='Marginal Δ = fn_StrategyMarginal v2: federal ordinary + CG + credits + FICA on wage lines + CounterLine. Hire-Children child-wage offset is parent-rate (understates STR-009).'
        )
        break

print(f"  Updated 15 Tax_Plan_Dashboard cells (K8:K22)")

# ----------------------------------------------------------------------
# Append caveat block to Setup_Guide
# ----------------------------------------------------------------------
ws = wb['Setup_Guide']
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
start_row = ws.max_row + 3
section_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill = PatternFill('solid', fgColor='C00000')
label_font   = Font(name='Calibri', size=10)

ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=6)
ws.cell(row=start_row, column=1, value='▸ fn_StrategyMarginal v2 — CAVEATS').font = section_font
ws.cell(row=start_row, column=1).fill = section_fill
ws.cell(row=start_row, column=1).alignment = Alignment(horizontal='left', vertical='center')

caveats = [
    'FICA rate flat 15.3% — no SS wage-base cap, no extra 0.9% Medicare surtax above $250K MFJ.',
    'Only Line 1z is FICA-subject. Lines 8/10/11/12/13 are NOT FICA-subject (correct for S-Corp K-1; INCORRECT for sole-prop/partnership where SE applies).',
    'Hire Children (STR-009 → CounterLine 1z): child wages are taxed at PARENT'+chr(39)+'s rate in this model. Real child has separate return at lower bracket. UNDERSTATES STR-009 savings. Revisit when entity-type awareness is added.',
    'SE tax not modeled separately — would matter for sole-prop / partnership clients. Default client context is S-Corp owner so K-1 active has no SE.',
    'State tax savings not included in fn_StrategyMarginal. Use TAX_STATE separately for state-level marginal.',
    'NIIT impact not included. Strategies affecting investment income (Line 7 CG, 3b dividends) may have NIIT secondary effect.',
    'CounterLine handling assumes the catalog'+chr(39)+'s Sign convention: primary amount is "moved off" target_line; counter amount is "moved onto" counter_line (opposite sign).',
]

for i, c in enumerate(caveats):
    r = start_row + 2 + i
    ws.cell(row=r, column=1, value=f'•').font = Font(name='Calibri', size=10, bold=True, color='C00000')
    ws.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='top')
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    ws.cell(row=r, column=2, value=c).font = label_font
    ws.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws.row_dimensions[r].height = 30

print(f"  Caveats appended to Setup_Guide row {start_row}-{start_row+1+len(caveats)}")

# ----------------------------------------------------------------------
# Save + audit
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Audit pre-Excel-open
import zipfile
with zipfile.ZipFile(OUT_FILE) as z:
    with z.open('xl/workbook.xml') as f:
        xml = f.read().decode('utf-8')
m = re.search(r'<definedName name="fn_StrategyMarginal"[^>]*>([^<]+)</definedName>', xml)
if m:
    body = m.group(1)
    print(f"\nfn_StrategyMarginal post-save audit:")
    print(f"  Length: {len(body)} chars")
    print(f"  Parens: {body.count('(')} open / {body.count(')')} close")
    print(f"  _xlfn.LAMBDA present: {'_xlfn.LAMBDA' in body}")
    print(f"  _xlfn.LET present: {'_xlfn.LET' in body}")
    print(f"  No leading =: {not body.startswith('=')}")

print(f"\nSample formula (Y2025!K144):")
wb2 = openpyxl.load_workbook(OUT_FILE)
print(f"  {wb2['Y2025']['K144'].value}")
print(f"\nSample formula (Tax_Plan_Dashboard!K8):")
print(f"  {wb2['Tax_Plan_Dashboard']['K8'].value}")
