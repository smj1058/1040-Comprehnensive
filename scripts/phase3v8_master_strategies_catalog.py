"""Phase 3v8 — Master_Strategies catalog (additive, doesn't touch year sheets).

Creates a new Master_Strategies sheet with one row per IMPACT (a strategy
that touches N 1040 lines has N rows). Schema:

  Strategy_ID | Impact_Num | Strategy_Name | Bucket | Framework_Ref |
  TargetLine | HelperTreatment | Sign | Cap_Rule | Plan_Maturity_Min |
  Description

Scope this build:
  - 15 STR-* numbered strategies (Core 5 expanded + Supplemental 7 + 3 extra)
  - Each strategy expanded to its actual impact rows (some are 1, some 3)
  - Reference-only — year sheets remain unchanged
  - Bucket legend section
  - Sign convention legend section

Future build (separate phase):
  - Year sheet refactor to FILTER/INDEX from this catalog
  - Cap-rule enforcement formulas
  - Plan Maturity gating
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v7_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v8_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# Remove existing sheet if rebuilding
if 'Master_Strategies' in wb.sheetnames:
    del wb['Master_Strategies']

ws = wb.create_sheet('Master_Strategies')

# Position right after Framework_Ref
target_idx = wb.sheetnames.index('Framework_Ref') + 1
current_idx = wb.sheetnames.index('Master_Strategies')
if current_idx != target_idx:
    wb.move_sheet('Master_Strategies', offset=target_idx - current_idx)

ws.sheet_properties.tabColor = 'C00000'  # red — reference

# Styles
title_font     = Font(name='Calibri', size=18, bold=True, color='1F4E79')
subtitle_font  = Font(name='Calibri', size=10, italic=True, color='7F7F7F')
section_font   = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill   = PatternFill('solid', fgColor='1F4E79')
hdr_font       = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill       = PatternFill('solid', fgColor='4472C4')
label_font     = Font(name='Calibri', size=10)
mono_font      = Font(name='Consolas', size=9)
center         = Alignment(horizontal='center', vertical='center')
left           = Alignment(horizontal='left',   vertical='center', wrap_text=True)
right          = Alignment(horizontal='right',  vertical='center')
thin           = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)

# ----------------------------------------------------------------------
# Header block
# ----------------------------------------------------------------------
ws['B2'] = 'MASTER STRATEGIES CATALOG'
ws['B2'].font = title_font
ws['B3'] = ('Source of truth for all tax strategies. One row per impact — '
            'a strategy that touches N 1040 lines has N rows here. Year sheets '
            'currently reference this manually; future build will auto-populate.')
ws['B3'].font = subtitle_font

# ----------------------------------------------------------------------
# SECTION A — Strategy Catalog (the main table)
# ----------------------------------------------------------------------
ws.merge_cells('B5:L5')
ws['B5'] = '▸ SECTION A — STRATEGY CATALOG (one row per impact)'
ws['B5'].font = section_font
ws['B5'].fill = section_fill
ws['B5'].alignment = left

# Table headers at row 7
headers = [
    'Strategy_ID', 'Impact_Num', 'Strategy_Name', 'Bucket', 'Framework_Ref',
    'TargetLine', 'HelperTreatment', 'Sign', 'Cap_Rule', 'Plan_Maturity_Min', 'Description'
]
for i, h in enumerate(headers):
    cell = ws.cell(row=7, column=2+i, value=h)
    cell.font = hdr_font
    cell.fill = hdr_fill
    cell.alignment = center
    cell.border = thin

# Strategy impact data
# (strategy_id, impact_num, name, bucket, framework_ref, target_line, helper_treatment,
#  sign, cap_rule, plan_maturity_min, description)
rows = [
    # STR-001 S-Corp Wage Optimization — 2 impacts (FAN OUT)
    ('STR-001', 1, 'S-Corp Wage Optimization', 'Core',    '#2', '1z', 'OWNER_PAY',         -1, 'Reasonable comp test (RCReports/avg)', 'Standard', 'Reduce W-2 wages to reasonable comp; surplus moves to K-1 active'),
    ('STR-001', 2, 'S-Corp Wage Optimization', 'Core',    '#2', '8',  'K1_SCorp_Active',   +1, 'Mirrors Impact 1 amount',              'Standard', 'Surplus from W-2 reduction lands as K-1 active income'),

    # STR-002 Entity Structuring — 1 impact (foundational, often 0-impact on 1040 directly)
    ('STR-002', 1, 'Entity Structuring',       'Core',    '#1', '—',  'STRUCTURAL',         0, 'Form 2553 timing / QBI grouping',     'Verified', 'Foundation. Enables wage opt + QBI. No direct $ impact on 1040 in year-of-election'),

    # STR-003 Retirement Contributions — 3 impacts (employee deferral hits 1z, employer match hits 8, IRA hits 10/12a)
    ('STR-003', 1, '401(k) Employee Deferral', 'Core',    '#3', '1z', 'RETIREMENT',        -1, '$23K + $7.5K catch-up (2024)',         'Standard', 'Pre-tax 401(k) elective deferral reduces W-2 wages'),
    ('STR-003', 2, '401(k) Employer Match',    'Core',    '#3', '8',  'RETIREMENT',        -1, '25% of comp, $66K combined (2024)',    'Standard', 'Employer side reduces S-Corp K-1 income'),
    ('STR-003', 3, 'Traditional IRA',          'Core',    '#3', '10', 'RETIREMENT',        -1, '$7K + $1K catch-up (2024); MAGI cap', 'Standard', 'Above-line deduction Line 20 (Sch 1 line 20)'),

    # STR-004 SEP-IRA — 1 impact (defaults to Line 8 per user pref; technically Line 10 for sole prop)
    ('STR-004', 1, 'SEP-IRA',                  'Core',    '#3', '8',  'RETIREMENT',        -1, '25% of comp, $66K cap (2024)',         'Standard', 'Defaults to Line 8 (S-Corp owner context); change TargetLine→10 for sole-prop'),

    # STR-005 Cost Seg + Bonus Depreciation — 1 impact (E rental)
    ('STR-005', 1, 'Cost Seg + Bonus Depr.',   'Core',    '#4', '8',  'SchE_Rental',       -1, '25% Y1 accel of building basis (default)', 'Verified', 'Cost seg study reclassifies 5/7/15-yr property; bonus depr accelerates'),

    # STR-006 Augusta Rule — 1 impact (deduction to business)
    ('STR-006', 1, 'Augusta Rule (§280A)',     'Core',    '#5 LHF', '8', 'AUGUSTA',       -1, '≤14 days/yr at FMV',                   'Standard', 'S-Corp rents owner residence ≤14 days; deduction to business, tax-free to owner'),

    # STR-007 Accountable Plan — 1 impact
    ('STR-007', 1, 'Accountable Plan',         'Core',    '#5 LHF', '8', 'ACCT_PLAN',     -1, 'Substantiated expenses only',          'Standard', 'Written plan reimburses owner-employee for business use of home/vehicle'),

    # STR-008 MERP/HRA — 1 impact
    ('STR-008', 1, 'MERP / HRA',               'Core',    '#5 LHF', '8', 'MEDICAL_HRA',   -1, 'Per §105/106 limits',                  'Verified', 'Medical Expense Reimbursement Plan — deductible to S-Corp, tax-free to employee'),

    # STR-009 Hire Children — 3 impacts (-8 business, +1z child wages, info Roth)
    ('STR-009', 1, 'Hire Children',            'Core',    '#5 LHF', '8',  'CHILD_WAGES',  -1, 'Reasonable wages for age/work',        'Standard', 'Wages deductible to business'),
    ('STR-009', 2, 'Hire Children',            'Core',    '#5 LHF', '1z', 'CHILD_WAGES',  +1, "Child's standard deduction = $14,600 (2024)", 'Standard', "Wages reportable on child's return; up to std ded = 0 tax"),
    ('STR-009', 3, 'Hire Children',            'Core',    '#5 LHF', '—',  'CHILD_ROTH',    0, 'Up to lesser of earned income or $7K', 'Standard', 'Informational — child can fund Roth IRA with earned wages (no 1040 impact)'),

    # STR-010 Entity Restructure — multi-impact (potentially)
    ('STR-010', 1, 'Entity Restructure',       'Advanced', '#1', '—',  'STRUCTURAL',        0, 'Case-by-case',                         'Confirmed', 'HoldCo over OpCo, F-reorg, etc. Foundation move'),

    # STR-011 PTET Election — 1 impact (Bucket B Supplemental)
    ('STR-011', 1, 'PTET Election',            'Supp.',   'B1', '8',  'PTET',              -1, '100% of state tax via entity',         'Verified', 'Pass-Through Entity Tax — entity pays state, federal deduction at entity level'),

    # STR-012 Tax Loss Harvesting — 1 impact
    ('STR-012', 1, 'Tax Loss Harvesting',      'Supp.',   'B2', '7',  'CG_HARVEST',        -1, '$3K ord loss; CL carryforward',        'Standard', 'Realize losses to offset realized gains; wash-sale 30-day rule'),

    # STR-013 R&D Credit — 1 impact (offsets Line 20 tax, not income)
    ('STR-013', 1, 'R&D Tax Credit',           'Advanced','—',  '20', 'CREDIT_RD',         -1, 'Qualifying research expenses',         'Verified', 'Section 41 credit — offsets tax on Line 20 (was Line 13 in older 1040)'),

    # STR-014 Roth Conversion — 1 impact
    ('STR-014', 1, 'Roth Conversion',          'Supp.',   'B4', '4b', 'ROTH_CONV',        +1, 'Bracket-management strategy',          'Standard', 'Move trad IRA dollars to Roth; current-year income hit for future tax-free growth'),

    # STR-015 DAF (Donor-Advised Fund) — 1 impact
    ('STR-015', 1, 'Donor-Advised Fund',       'Supp.',   'B5', '12a', 'CHARITY_DAF',     -1, '30%/60% of AGI limits',                'Standard', 'Bunch multiple years of giving into one DAF contribution'),
]

start_row = 8
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        cell = ws.cell(row=start_row + i, column=2 + j, value=v)
        cell.font = label_font
        cell.alignment = left
        cell.border = thin
        # Right-align numeric impact/sign columns
        if headers[j] in ('Impact_Num', 'Sign'):
            cell.alignment = center

# Make it an Excel table for easy filtering
end_row = start_row + len(rows) - 1
table_ref = f'B7:L{end_row}'
table = Table(displayName='tblMasterStrategies', ref=table_ref)
table.tableStyleInfo = TableStyleInfo(
    name='TableStyleMedium2',
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False,
)
ws.add_table(table)
print(f"  Section A built: {len(rows)} impact rows, table tblMasterStrategies at {table_ref}")

# Named range for the table
if 'MasterStrategies' in wb.defined_names:
    del wb.defined_names['MasterStrategies']
wb.defined_names['MasterStrategies'] = DefinedName(
    name='MasterStrategies',
    attr_text=f"Master_Strategies!${table_ref.replace(':', ':$')}"
)

# ----------------------------------------------------------------------
# SECTION B — Bucket legend
# ----------------------------------------------------------------------
bucket_row = end_row + 3
ws.merge_cells(f'B{bucket_row}:L{bucket_row}')
ws.cell(row=bucket_row, column=2, value='▸ SECTION B — BUCKET LEGEND').font = section_font
ws.cell(row=bucket_row, column=2).fill = section_fill
ws.cell(row=bucket_row, column=2).alignment = left

buckets = [
    ('Core',     'Bucket A — 5 dependency-ordered foundational strategies. Entity → Wage → Retirement → Bonus Depr → LHF'),
    ('Supp.',    'Bucket B — 7 supplemental strategies (B1-B7). PTET, TaxLoss, IncShift, Roth, DAF, 1031, OppZone'),
    ('Advanced', 'Bucket C — case-by-case heavy machinery. Entity restructure, R&D credit, conservation easements'),
]
for i, (b, desc) in enumerate(buckets):
    r = bucket_row + 2 + i
    ws.cell(row=r, column=2, value=b).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=2).alignment = center
    ws.cell(row=r, column=2).border = thin
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=12)
    ws.cell(row=r, column=3, value=desc).font = label_font
    ws.cell(row=r, column=3).alignment = left
    ws.cell(row=r, column=3).border = thin

# ----------------------------------------------------------------------
# SECTION C — Sign convention legend
# ----------------------------------------------------------------------
sign_row = bucket_row + 2 + len(buckets) + 2
ws.merge_cells(f'B{sign_row}:L{sign_row}')
ws.cell(row=sign_row, column=2, value='▸ SECTION C — SIGN CONVENTION').font = section_font
ws.cell(row=sign_row, column=2).fill = section_fill
ws.cell(row=sign_row, column=2).alignment = left

signs = [
    ('-1', 'REDUCES target line', 'e.g., 401(k) employee deferral reduces W-2 wages (Line 1z by -$X)'),
    ('+1', 'INCREASES target line', 'e.g., S-Corp wage reduction shifts dollars to K-1 (Line 8 by +$X)'),
    ('0',  'NO 1040 IMPACT (info)', 'e.g., entity structure or Roth-via-child wages — tracked but no direct line move'),
]
for i, (s, label, ex) in enumerate(signs):
    r = sign_row + 2 + i
    ws.cell(row=r, column=2, value=s).font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
    ws.cell(row=r, column=2).alignment = center
    ws.cell(row=r, column=2).border = thin
    ws.cell(row=r, column=3, value=label).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=3).alignment = left
    ws.cell(row=r, column=3).border = thin
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=12)
    ws.cell(row=r, column=4, value=ex).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws.cell(row=r, column=4).alignment = left
    ws.cell(row=r, column=4).border = thin

# ----------------------------------------------------------------------
# SECTION D — STRATEGY BUILDER (live tool)
# ----------------------------------------------------------------------
builder_row = sign_row + 2 + len(signs) + 2
ws.merge_cells(f'B{builder_row}:L{builder_row}')
ws.cell(row=builder_row, column=2, value='▸ SECTION D — STRATEGY BUILDER (live tool — pick + size a strategy)').font = section_font
ws.cell(row=builder_row, column=2).fill = section_fill
ws.cell(row=builder_row, column=2).alignment = left

# Builder inputs at row builder_row+2
br_input = builder_row + 2
input_yellow = PatternFill('solid', fgColor='FFF2CC')

# Pick STR-ID
ws.cell(row=br_input, column=2, value='Strategy:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=2).alignment = right
ws.cell(row=br_input, column=3, value='STR-001').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=3).fill = input_yellow
ws.cell(row=br_input, column=3).alignment = center
ws.cell(row=br_input, column=3).border = thin

# STR-ID dropdown
str_ids = sorted({r[0] for r in rows})
dv_str = DataValidation(type='list', formula1=f'"{",".join(str_ids)}"', allow_blank=False)
dv_str.add(f'C{br_input}')
ws.add_data_validation(dv_str)

# Amount input
ws.cell(row=br_input, column=4, value='Amount:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=4).alignment = right
ws.cell(row=br_input, column=5, value=25000).font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=5).fill = input_yellow
ws.cell(row=br_input, column=5).alignment = center
ws.cell(row=br_input, column=5).border = thin
ws.cell(row=br_input, column=5).number_format = '"$"#,##0'

# For year (informational)
ws.cell(row=br_input, column=6, value='For Year:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=6).alignment = right
ws.cell(row=br_input, column=7, value='=Active_Year').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=7).fill = input_yellow
ws.cell(row=br_input, column=7).alignment = center
ws.cell(row=br_input, column=7).border = thin

# Status pick
ws.cell(row=br_input, column=8, value='Status:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=8).alignment = right
ws.cell(row=br_input, column=9, value='Proposed').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=9).fill = input_yellow
ws.cell(row=br_input, column=9).alignment = center
ws.cell(row=br_input, column=9).border = thin

dv_status = DataValidation(type='list',
    formula1='"Proposed,Approved,Committed,Implemented"', allow_blank=False)
dv_status.add(f'I{br_input}')
ws.add_data_validation(dv_status)

# Cap warning (compares C{br_input} amount vs Cap_Rule)
ws.cell(row=br_input, column=10, value='Cap check:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=10).alignment = right
cap_formula = (
    f'=IFERROR(IF(ISNUMBER(SEARCH("$",VLOOKUP($C${br_input},$B$8:$L${end_row},9,FALSE))),'
    f'IF($E${br_input}>VALUE(MID(VLOOKUP($C${br_input},$B$8:$L${end_row},9,FALSE),'
    f'FIND("$",VLOOKUP($C${br_input},$B$8:$L${end_row},9,FALSE))+1,10)),'
    f'"⚠ Over cap","OK"),"manual"),"see cap rule")'
)
# Simpler: just display the Cap_Rule text for reference
ws.cell(row=br_input, column=11, value=f'=VLOOKUP($C${br_input},$B$8:$L${end_row},9,FALSE)').font = Font(name='Calibri', size=9, italic=True, color='C00000')
ws.cell(row=br_input, column=11).alignment = left
ws.cell(row=br_input, column=11).border = thin

# Impact table header
hdr_b_row = br_input + 2
ws.merge_cells(start_row=hdr_b_row, start_column=2, end_row=hdr_b_row, end_column=12)
ws.cell(row=hdr_b_row, column=2, value=f'▾ All impacts for the selected strategy (paste these rows into Y[year] sheet)').font = Font(name='Calibri', size=10, italic=True, color='3F3F3F')

hdr2_row = hdr_b_row + 1
builder_headers = ['#', 'Strategy_ID', 'Strategy_Name', 'TargetLine', 'HelperTreatment',
                   'Sign', 'Amount (signed)', 'Status', 'Cap_Rule', 'Description']
for i, h in enumerate(builder_headers):
    c = ws.cell(row=hdr2_row, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin

# Spill rows — up to 5 impact slots (no strategy fans out further than 3 today; 5 gives headroom)
# Using INDEX/SMALL pattern (works without dynamic arrays) to filter impacts for picked Strategy_ID
table_range_rows = f'$B$8:$L${end_row}'
for i in range(5):
    r = hdr2_row + 1 + i
    impact_num = i + 1
    # Row appears only if a matching impact exists
    # Using INDEX/MATCH via Strategy_ID + Impact_Num composite
    match_formula = (
        f'IFERROR(INDEX($B$8:$L${end_row},'
        f'MATCH(1,($B$8:$B${end_row}=$C${br_input})*($C$8:$C${end_row}={impact_num}),0),'
    )
    ws.cell(row=r, column=2, value=impact_num).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=2).alignment = center
    ws.cell(row=r, column=2).border = thin

    # Strategy_ID
    ws.cell(row=r, column=3, value=f'={match_formula}1),"")').font = label_font
    ws.cell(row=r, column=3).alignment = center
    ws.cell(row=r, column=3).border = thin
    # Strategy_Name
    ws.cell(row=r, column=4, value=f'={match_formula}3),"")').font = label_font
    ws.cell(row=r, column=4).alignment = left
    ws.cell(row=r, column=4).border = thin
    # TargetLine
    ws.cell(row=r, column=5, value=f'={match_formula}6),"")').font = label_font
    ws.cell(row=r, column=5).alignment = center
    ws.cell(row=r, column=5).border = thin
    # HelperTreatment
    ws.cell(row=r, column=6, value=f'={match_formula}7),"")').font = label_font
    ws.cell(row=r, column=6).alignment = center
    ws.cell(row=r, column=6).border = thin
    # Sign
    ws.cell(row=r, column=7, value=f'={match_formula}8),"")').font = label_font
    ws.cell(row=r, column=7).alignment = center
    ws.cell(row=r, column=7).border = thin
    # Amount (signed) = $E$br_input * Sign  (only if impact exists)
    amt_formula = (
        f'=IFERROR(IF({match_formula}8),""),'
        f'$E${br_input}*{match_formula}8),"")),"")'
    )
    ws.cell(row=r, column=8, value=amt_formula).font = Font(name='Calibri', size=10, bold=True, color='1F4E79')
    ws.cell(row=r, column=8).alignment = right
    ws.cell(row=r, column=8).border = thin
    ws.cell(row=r, column=8).number_format = '"$"#,##0;("$"#,##0);"-"'
    # Status (copies from input)
    ws.cell(row=r, column=9, value=f'=IF({match_formula}1),"")="","",$I${br_input})').font = label_font
    ws.cell(row=r, column=9).alignment = center
    ws.cell(row=r, column=9).border = thin
    # Cap_Rule
    ws.cell(row=r, column=10, value=f'={match_formula}9),"")').font = Font(name='Calibri', size=9, italic=True)
    ws.cell(row=r, column=10).alignment = left
    ws.cell(row=r, column=10).border = thin
    # Description (merge across rest)
    ws.merge_cells(start_row=r, start_column=11, end_row=r, end_column=12)
    ws.cell(row=r, column=11, value=f'={match_formula}11),"")').font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws.cell(row=r, column=11).alignment = left
    ws.cell(row=r, column=11).border = thin

# Helper note
note_row = hdr2_row + 7
ws.merge_cells(start_row=note_row, start_column=2, end_row=note_row, end_column=12)
ws.cell(row=note_row, column=2, value='Tip: change C{br}, E{br}, I{br} above to size a different strategy. Blank rows mean the strategy has fewer impacts than the slot. Paste signed amounts into Y[year]!A6:F20 columns matching: Name → B, TargetLine → C, HelperTreatment (none today), Amount → D, Status → E.'.format(br=br_input)).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
ws.cell(row=note_row, column=2).alignment = left
ws.row_dimensions[note_row].height = 30

# ----------------------------------------------------------------------
# SECTION E — How to use this catalog
# ----------------------------------------------------------------------
howto_row = note_row + 3
ws.merge_cells(f'B{howto_row}:L{howto_row}')
ws.cell(row=howto_row, column=2, value='▸ SECTION E — HOW TO USE THIS CATALOG').font = section_font
ws.cell(row=howto_row, column=2).fill = section_fill
ws.cell(row=howto_row, column=2).alignment = left

howto = [
    ('Today (Strategy Builder above):', 'Pick STR-ID + Amount + Status above. Impact rows spill below with signed amounts. Copy to a year sheet.'),
    ('Today (search):', 'Filter the catalog table by Strategy_ID to see every strategy\'s impacts.'),
    ('Today (validator on year sheets):', 'Each year sheet now has columns M-O at the right showing what the catalog says about the strategy you typed. If it doesn\'t match, the catalog probably needs updating.'),
    ('Next phase (auto-populate):', 'Year sheet picks STR-ID from dropdown → FILTER returns impacts and amounts auto-spill into rows 6-20. Cap_Rule auto-enforces. Plan_Maturity blocks below-threshold commits.'),
    ('Adding a new strategy:', 'Add rows here first. Each impact = one row. Assign next available STR-NNN. Update Framework_Ref to reference it.'),
]
for i, (label, desc) in enumerate(howto):
    r = howto_row + 2 + i
    ws.cell(row=r, column=2, value=label).font = Font(name='Calibri', size=10, bold=True, color='1F4E79')
    ws.cell(row=r, column=2).alignment = left
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=12)
    ws.cell(row=r, column=3, value=desc).font = label_font
    ws.cell(row=r, column=3).alignment = left
    ws.row_dimensions[r].height = 30

# ----------------------------------------------------------------------
# Column widths
# ----------------------------------------------------------------------
widths = [3, 13, 11, 28, 10, 14, 12, 22, 6, 28, 18, 50]
for i, w in enumerate(widths):
    ws.column_dimensions[get_column_letter(i+1)].width = w

# Row 2 title height
ws.row_dimensions[2].height = 26

# ----------------------------------------------------------------------
# Save
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Master_Strategies']
print(f"\nVerification:")
print(f"  B2 title: {ws2['B2'].value!r}")
print(f"  Header row count (B7:L7): {[ws2.cell(row=7, column=c).value for c in range(2,13)]}")
print(f"  Total impact rows: {len(rows)}")
print(f"  STR-001 row count (should be 2): {sum(1 for r in rows if r[0]=='STR-001')}")
print(f"  STR-003 row count (should be 3): {sum(1 for r in rows if r[0]=='STR-003')}")
print(f"  STR-009 row count (should be 3): {sum(1 for r in rows if r[0]=='STR-009')}")
print(f"  Sheet position: index {wb2.sheetnames.index('Master_Strategies')}")
print(f"  Named range MasterStrategies: {wb2.defined_names.get('MasterStrategies').value if 'MasterStrategies' in wb2.defined_names else 'MISSING'}")
print(f"  Sheets: {wb2.sheetnames}")
