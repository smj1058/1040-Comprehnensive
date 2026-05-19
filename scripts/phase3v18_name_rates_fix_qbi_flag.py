"""Phase 3v18 — Name the 96 hardcoded rates from audit findings.

Six distinct rate values across the calc engine on Y2023-Y2028. Naming:

  Rate_FICA_SS_Employee     = 0.062   (J84/K84  — 12 cells)
  Rate_FICA_Medicare_Employee = 0.0145 (J85/K85  — 12 cells)
  Rate_Sec1250_Recap        = 0.25    (J106/K106 — 12 cells)
  Rate_QBI_Deduction        = 0.20    (J118/K118 — 12 cells)
  Rate_QBI_W2_Limit         = 0.25    (J120/K120 first arg — 12 cells)
  Rate_QBI_UBIA_Limit       = 0.025   (J120/K120 third arg — 12 cells)
  Rate_QBI_BenefitApprox    = 0.24    (J131/K131 — 12 cells)

  (Also adds Rate_QBI_W2_50pct = 0.50 for J120's inner MAX first arg)

BUG FLAGGED (not auto-fixed): J119/K119 on every year sheet labels
"50% of W-2 Wages" but multiplies by 0.2. Under-computes QBI deduction
when this limit binds (e.g., $20K instead of $50K for a $100K W-2
business). Documented in Audit_Report; user decides whether to fix.

Also patches fn_StrategyMarginal to use Rate_FICA_Combined named range
instead of embedded 0.153 (consistency).
"""

import openpyxl
import re
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

IN  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v17_CC.xlsx'
OUT = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v18_CC.xlsx'

wb = openpyxl.load_workbook(IN)

# ---------------------------------------------------------------
# Define named rates (point to cells holding the rate value)
# Best practice: rates live in Tax_Ref as cells, named ranges point at them
# Simpler approach: defined names with the literal value as the formula
# ---------------------------------------------------------------
named_rates = [
    ('Rate_FICA_SS_Employee',       0.062),
    ('Rate_FICA_Medicare_Employee', 0.0145),
    ('Rate_FICA_Combined',          0.153),    # SS 6.2% + 6.2% + Medicare 1.45% + 1.45% = 15.3%
    ('Rate_Sec1250_Recap',          0.25),
    ('Rate_QBI_Deduction',          0.20),
    ('Rate_QBI_W2_50pct',           0.50),
    ('Rate_QBI_W2_25pct',           0.25),
    ('Rate_QBI_UBIA_2_5pct',        0.025),
    ('Rate_QBI_BenefitApprox',      0.24),
    ('Rate_NIIT',                   0.038),
    ('Rate_SE_Deduction',           0.9235),
]

for name, val in named_rates:
    if name in wb.defined_names:
        del wb.defined_names[name]
    wb.defined_names[name] = DefinedName(name=name, attr_text=str(val))

print(f"Defined {len(named_rates)} rate names")

# ---------------------------------------------------------------
# Substitute literals in year-sheet cells with named references
# ---------------------------------------------------------------
year_sheets = ['Y2023', 'Y2024', 'Y2025', 'Y2026', 'Y2027', 'Y2028']

# Substitutions by cell location → (old text in formula, new text)
# Apply across both J and K columns
substitutions = [
    (84,  '*0.062',  '*Rate_FICA_SS_Employee'),       # SS payroll
    (85,  '*0.0145', '*Rate_FICA_Medicare_Employee'), # Medicare payroll
    (106, '*0.25',   '*Rate_Sec1250_Recap'),           # §1250 recap
    (118, '*0.2',    '*Rate_QBI_Deduction'),           # 20% QBI
    # Row 119 is the bug — leave untouched, flag separately
    (120, 'J23*0.5', 'J23*Rate_QBI_W2_50pct'),         # 50% W-2 in MAX
    (120, 'K23*0.5', 'K23*Rate_QBI_W2_50pct'),
    (120, 'J23*0.25','J23*Rate_QBI_W2_25pct'),         # 25% W-2 in MAX
    (120, 'K23*0.25','K23*Rate_QBI_W2_25pct'),
    (120, 'J44*0.025','J44*Rate_QBI_UBIA_2_5pct'),     # 2.5% UBIA in MAX
    (120, 'K44*0.025','K44*Rate_QBI_UBIA_2_5pct'),
    (131, '*0.24',   '*Rate_QBI_BenefitApprox'),       # QBI tax benefit approx
]

# Some rows like 120 use both J/K with different ref prefixes, handle carefully per cell
# Simplified approach: do per-cell text replacement on J and K columns separately
total_subs = 0
for sn in year_sheets:
    ws = wb[sn]
    for row_num in [84, 85, 106, 118, 120, 131]:
        for col in [10, 11]:  # J, K
            cell = ws.cell(row=row_num, column=col)
            v = cell.value
            if not isinstance(v, str) or not v.startswith('='):
                continue
            new_v = v
            for r_target, old, new in substitutions:
                if row_num != r_target:
                    continue
                if old in new_v:
                    new_v = new_v.replace(old, new)
            if new_v != v:
                cell.value = new_v
                total_subs += 1

print(f"Replaced {total_subs} cells with named-rate references")

# ---------------------------------------------------------------
# Update fn_StrategyMarginal to use Rate_FICA_Combined instead of 0.153
# ---------------------------------------------------------------
if 'fn_StrategyMarginal' in wb.defined_names:
    fn = wb.defined_names['fn_StrategyMarginal'].value
    new_fn = fn.replace('*0.153', '*Rate_FICA_Combined')
    if new_fn != fn:
        del wb.defined_names['fn_StrategyMarginal']
        wb.defined_names['fn_StrategyMarginal'] = DefinedName(
            name='fn_StrategyMarginal', attr_text=new_fn
        )
        print("Updated fn_StrategyMarginal: 0.153 → Rate_FICA_Combined")

# Same for TAX_NIIT (uses 0.038)
if 'TAX_NIIT' in wb.defined_names:
    fn = wb.defined_names['TAX_NIIT'].value
    new_fn = fn.replace('0.038', 'Rate_NIIT')
    if new_fn != fn:
        del wb.defined_names['TAX_NIIT']
        wb.defined_names['TAX_NIIT'] = DefinedName(name='TAX_NIIT', attr_text=new_fn)
        print("Updated TAX_NIIT: 0.038 → Rate_NIIT")

# TAX_SE uses 0.9235, 0.124, 0.029
if 'TAX_SE' in wb.defined_names:
    fn = wb.defined_names['TAX_SE'].value
    new_fn = fn.replace('0.9235', 'Rate_SE_Deduction')
    if new_fn != fn:
        del wb.defined_names['TAX_SE']
        wb.defined_names['TAX_SE'] = DefinedName(name='TAX_SE', attr_text=new_fn)
        print("Updated TAX_SE: 0.9235 → Rate_SE_Deduction")

# ---------------------------------------------------------------
# Add a QBI BUG flag to Audit_Report
# ---------------------------------------------------------------
ws_aud = wb['Audit_Report']
# Find a clean place at top to insert "KNOWN BUGS" callout
# Insert a row at row 5 (before Section A)
ws_aud.insert_rows(idx=5, amount=4)

ws_aud.merge_cells('B5:G5')
ws_aud['B5'] = '🔴 KNOWN BUG FLAGGED (Phase 3v18 finding — NOT auto-fixed)'
ws_aud['B5'].font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
ws_aud['B5'].fill = PatternFill('solid', fgColor='C00000')
ws_aud['B5'].alignment = Alignment(horizontal='left', vertical='center')

ws_aud.merge_cells('B6:G6')
ws_aud['B6'] = ('Y2023-Y2028 row 119 (J119/K119): cell label says "50% of W-2 Wages" '
                'but formula multiplies by 0.2, not 0.5. UNDER-COMPUTES QBI deduction '
                'when this limit binds. Example: $100K W-2 → $20K limit (current) vs $50K limit (correct).')
ws_aud['B6'].font = Font(name='Calibri', size=10, color='C00000')
ws_aud['B6'].alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
ws_aud.row_dimensions[6].height = 36

ws_aud.merge_cells('B7:G7')
ws_aud['B7'] = ('TO FIX: open Y[year] sheet, change J119 and K119 formulas from "MAX(0,J41)*0.2" to '
                '"MAX(0,J41)*Rate_QBI_W2_50pct" on each of the 6 year sheets. '
                'WARNING: this will change every client\'s QBI deduction calc — verify before applying.')
ws_aud['B7'].font = Font(name='Calibri', size=10, italic=True, color='3F3F3F')
ws_aud['B7'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
ws_aud.row_dimensions[7].height = 36

print("Added QBI bug callout to Audit_Report rows 5-7")

# ---------------------------------------------------------------
# Save + audit verification
# ---------------------------------------------------------------
wb.save(OUT)
print(f"\nSaved: {OUT}")

# Verify
wb2 = openpyxl.load_workbook(OUT)
ws = wb2['Y2025']
print("\nVerification — Y2025 rates after substitution:")
for r in [84, 85, 106, 118, 119, 120, 131]:
    print(f"  J{r}: {ws.cell(row=r, column=10).value}")

print("\nNamed rates in Name Manager:")
for name, val in named_rates:
    if name in wb2.defined_names:
        print(f"  {name} = {wb2.defined_names[name].value}")
