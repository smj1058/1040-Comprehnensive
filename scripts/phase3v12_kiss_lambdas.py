"""Phase 3v12 — KISS LAMBDAs install.

Writes 6 named LAMBDAs to the workbook's defined names. Excel parses
them when the file opens; they become callable from any cell.

LAMBDAs installed:
  1. TAX_ORD     — federal ordinary income tax (progressive bracket)
  2. TAX_CG      — long-term cap gains / qualified div tax (0/15/20%)
  3. TAX_NIIT    — 3.8% net investment income tax
  4. TAX_SE      — self-employment tax (Social Security + Medicare)
  5. STD_DED     — standard deduction lookup
  6. TAX_STATE   — state tax via top marginal rate (KISS approximation)

Documentation added to Setup_Guide.

CAVEAT: openpyxl doesn't validate LAMBDA syntax. After opening, verify
each LAMBDA in Name Manager (Ctrl+F3) and spot-test with sample values.
"""

import openpyxl
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v11_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v12_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# ----------------------------------------------------------------------
# LAMBDAs — each as a single-line formula assigned to a defined name
# ----------------------------------------------------------------------

# 1. TAX_ORD(taxable_income, year, fs) — progressive federal income tax
#    Pull the bracket row matching (year, fs, lower<=ti<upper) and compute
#    (ti - lower) * rate + add_to
TAX_ORD = (
    'LAMBDA(taxable_income,year,fs,'
    'LET('
    'rows,FILTER(tblBrackets_FIT,'
    '(tblBrackets_FIT[Year]=year)*'
    '(tblBrackets_FIT[FilingStatus]=fs)*'
    '(tblBrackets_FIT[Lower]<=taxable_income)*'
    '(tblBrackets_FIT[Upper]>taxable_income)),'
    'lower,INDEX(rows,1,3),'
    'rate,INDEX(rows,1,5),'
    'add_to,INDEX(rows,1,6),'
    'MAX(0,(taxable_income-lower)*rate+add_to)))'
)

# 2. TAX_CG(cg_amount, taxable_income, year, fs)
#    LTCG bracket is by TAXABLE INCOME, but rate applies to cg_amount only
TAX_CG = (
    'LAMBDA(cg_amount,taxable_income,year,fs,'
    'LET('
    'rows,FILTER(tblBrackets_LTCG,'
    '(tblBrackets_LTCG[Year]=year)*'
    '(tblBrackets_LTCG[FilingStatus]=fs)*'
    '(tblBrackets_LTCG[Lower]<=taxable_income)*'
    '(tblBrackets_LTCG[Upper]>taxable_income)),'
    'rate,INDEX(rows,1,5),'
    'cg_amount*rate))'
)

# 3. TAX_NIIT(net_inv_income, magi, fs, year) — 3.8% on lesser of NII or MAGI-threshold
TAX_NIIT = (
    'LAMBDA(net_inv_income,magi,fs,year,'
    'LET('
    'threshold,INDEX(FILTER(tblThresholds[Value],'
    '(tblThresholds[Item]="NIIT_Threshold")*'
    '(tblThresholds[Year]=year)*'
    '(tblThresholds[FilingStatus]=fs)),1),'
    'rate,0.038,'
    'MAX(0,MIN(net_inv_income,magi-threshold))*rate))'
)

# 4. TAX_SE(se_net_earnings, year) — self-employment tax
#    Base = net_earnings * 0.9235 (deduction for employer-equivalent portion)
#    SS portion: 12.4% on base up to SS_Wage_Base
#    Medicare portion: 2.9% on full base
TAX_SE = (
    'LAMBDA(se_net_earnings,year,'
    'LET('
    'se_base,se_net_earnings*0.9235,'
    'ss_cap,INDEX(FILTER(tblThresholds[Value],'
    '(tblThresholds[Item]="SS_Wage_Base")*'
    '(tblThresholds[Year]=year)),1),'
    'ss_tax,MIN(se_base,ss_cap)*0.124,'
    'medi_tax,se_base*0.029,'
    'ss_tax+medi_tax))'
)

# 5. STD_DED(year, fs) — standard deduction lookup
STD_DED = (
    'LAMBDA(year,fs,'
    'INDEX(FILTER(tblStdDed[Amount],'
    '(tblStdDed[Year]=year)*(tblStdDed[FilingStatus]=fs)),1))'
)

# 6. TAX_STATE(taxable_income, state) — flat top-rate approximation
TAX_STATE = (
    'LAMBDA(taxable_income,state,'
    'taxable_income*XLOOKUP(state,tblStateRates[State],tblStateRates[Top_Marginal_Rate],0))'
)

lambdas = [
    ('TAX_ORD',   TAX_ORD,   'Federal ordinary income tax (progressive bracket)',
        'TAX_ORD(taxable_income, year, fs)',
        '=TAX_ORD(100000, 2025, "MFJ")  →  ~ $12,300'),
    ('TAX_CG',    TAX_CG,    'Long-term capital gains / qualified dividend tax (0/15/20%)',
        'TAX_CG(cg_amount, taxable_income, year, fs)',
        '=TAX_CG(50000, 200000, 2025, "MFJ")  →  $7,500'),
    ('TAX_NIIT',  TAX_NIIT,  '3.8% net investment income tax above MAGI threshold',
        'TAX_NIIT(net_inv_income, magi, fs, year)',
        '=TAX_NIIT(50000, 300000, "MFJ", 2025)  →  $1,900'),
    ('TAX_SE',    TAX_SE,    'Self-employment tax — SS + Medicare on net earnings × 0.9235',
        'TAX_SE(se_net_earnings, year)',
        '=TAX_SE(100000, 2025)  →  ~ $14,130'),
    ('STD_DED',   STD_DED,   'Standard deduction lookup by year + filing status',
        'STD_DED(year, fs)',
        '=STD_DED(2025, "MFJ")  →  $31,500'),
    ('TAX_STATE', TAX_STATE, 'State tax via top marginal rate (KISS approximation)',
        'TAX_STATE(taxable_income, state)',
        '=TAX_STATE(200000, "UT")  →  $9,300'),
]

# Install each as a defined name
print("\nInstalling LAMBDAs:")
for name, formula, _, _, _ in lambdas:
    if name in wb.defined_names:
        del wb.defined_names[name]
    wb.defined_names[name] = DefinedName(name=name, attr_text=formula)
    print(f"  {name}: {len(formula)} chars")

# ----------------------------------------------------------------------
# Documentation in Setup_Guide
# ----------------------------------------------------------------------
ws = wb['Setup_Guide']
print(f"\nSetup_Guide max_row before: {ws.max_row}")

# Add section at end of Setup_Guide
start_row = ws.max_row + 3

section_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill = PatternFill('solid', fgColor='1F4E79')
hdr_font     = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill     = PatternFill('solid', fgColor='4472C4')
label_font   = Font(name='Calibri', size=10)
mono_font    = Font(name='Consolas', size=9, color='1F4E79')
thin         = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)
center = Alignment(horizontal='center', vertical='center')
left   = Alignment(horizontal='left',   vertical='center', wrap_text=True)

# Section header
ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=6)
ws.cell(row=start_row, column=1, value='▸ KISS LAMBDAs — Installed by Phase 3v12').font = section_font
ws.cell(row=start_row, column=1).fill = section_fill
ws.cell(row=start_row, column=1).alignment = left

# Subtitle
ws.cell(row=start_row+1, column=1,
    value='Six LAMBDAs in Name Manager (Ctrl+F3 to view). Callable from any cell. CAVEAT: verify each in Name Manager after opening; spot-test with the example values shown.').font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
ws.merge_cells(start_row=start_row+1, start_column=1, end_row=start_row+1, end_column=6)

# Table headers
hdr_row = start_row + 3
for i, h in enumerate(['Name', 'Purpose', 'Signature', 'Example call', 'Returns']):
    c = ws.cell(row=hdr_row, column=1+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin

# LAMBDA documentation rows
for i, (name, formula, purpose, sig, example_full) in enumerate(lambdas):
    r = hdr_row + 1 + i
    # Split example into call and result
    if '→' in example_full:
        call_part, result_part = example_full.split('→', 1)
    else:
        call_part, result_part = example_full, ''
    cells = [
        (name, mono_font),
        (purpose, label_font),
        (sig, mono_font),
        (call_part.strip(), mono_font),
        (result_part.strip(), label_font),
    ]
    for j, (val, font) in enumerate(cells):
        c = ws.cell(row=r, column=1+j, value=val)
        c.font = font
        c.alignment = left
        c.border = thin
    ws.row_dimensions[r].height = 22

# Add a "Show formula" section showing the actual LAMBDA bodies
formula_start = hdr_row + len(lambdas) + 3
ws.merge_cells(start_row=formula_start, start_column=1, end_row=formula_start, end_column=6)
ws.cell(row=formula_start, column=1, value='▸ LAMBDA bodies (for reference/audit)').font = section_font
ws.cell(row=formula_start, column=1).fill = section_fill
ws.cell(row=formula_start, column=1).alignment = left

for i, (name, formula, _, _, _) in enumerate(lambdas):
    r = formula_start + 2 + i * 2
    ws.cell(row=r, column=1, value=name).font = Font(name='Consolas', size=10, bold=True, color='1F4E79')
    ws.cell(row=r, column=1).alignment = left
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    ws.cell(row=r, column=2, value=formula).font = Font(name='Consolas', size=8, color='3F3F3F')
    ws.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws.row_dimensions[r].height = 80

# Column widths
ws.column_dimensions['A'].width = 14
ws.column_dimensions['B'].width = 40
ws.column_dimensions['C'].width = 38
ws.column_dimensions['D'].width = 38
ws.column_dimensions['E'].width = 18

# ----------------------------------------------------------------------
# Save
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify
wb2 = openpyxl.load_workbook(OUT_FILE)
print(f"\nVerification — defined names installed:")
for name in ['TAX_ORD', 'TAX_CG', 'TAX_NIIT', 'TAX_SE', 'STD_DED', 'TAX_STATE']:
    if name in wb2.defined_names:
        v = wb2.defined_names[name].value
        print(f"  {name}: {v[:80]}...")
    else:
        print(f"  {name}: MISSING")
