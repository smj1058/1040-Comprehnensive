"""Phase 3v9 — Reconcile Master_Strategies catalog with year-sheet STR-IDs.

In v8 I built the catalog with my own STR-* numbering. Turned out 8 of 15
IDs disagreed with what was already on the year sheets (e.g., catalog
STR-002 was "Entity Structuring" while year-sheet STR-002 was "HSA Family
Max"). Auto-populate refactor would have silently overwritten existing
year-sheet entries.

Fix: rebuild Section A of Master_Strategies using the YEAR SHEET as the
authoritative STR-ID source. Multi-impact fan-out is preserved where the
year sheet uses CounterLine (STR-001 and STR-010) or where the strategy
inherently has multiple impacts (STR-009 Hire Children: -8 business
deduction, +1z child wages, info-only Roth).

Strategy Builder formulas (Section D) updated to point at the new
catalog range (19 rows instead of 20).

Open question for later revisit:
  - Some year-sheet strategies (HSA, Roth Conversion at Line 1z,
    SALT PTE at Line 12) may have non-canonical TargetLines that warrant
    review. Logged as ITEM-RECONCILE-1 in this build.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v8_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v9_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# Drop existing Master_Strategies and rebuild from scratch
if 'Master_Strategies' in wb.sheetnames:
    del wb['Master_Strategies']
ws = wb.create_sheet('Master_Strategies')

# Position right after Framework_Ref
target_idx = wb.sheetnames.index('Framework_Ref') + 1
current_idx = wb.sheetnames.index('Master_Strategies')
if current_idx != target_idx:
    wb.move_sheet('Master_Strategies', offset=target_idx - current_idx)
ws.sheet_properties.tabColor = 'C00000'

# Styles
title_font     = Font(name='Calibri', size=18, bold=True, color='1F4E79')
subtitle_font  = Font(name='Calibri', size=10, italic=True, color='7F7F7F')
section_font   = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill   = PatternFill('solid', fgColor='1F4E79')
hdr_font       = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill       = PatternFill('solid', fgColor='4472C4')
label_font     = Font(name='Calibri', size=10)
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
# Header
# ----------------------------------------------------------------------
ws['B2'] = 'MASTER STRATEGIES CATALOG'
ws['B2'].font = title_font
ws['B3'] = ('Source of truth aligned with year-sheet STR-IDs. One row per impact. '
            'Use the Strategy Builder (Section D) to size a strategy and see its '
            'fan-out before pasting into a year sheet.')
ws['B3'].font = subtitle_font

# ----------------------------------------------------------------------
# SECTION A — Strategy Catalog (RECONCILED with year-sheet STR-IDs)
# ----------------------------------------------------------------------
ws.merge_cells('B5:L5')
ws['B5'] = '▸ SECTION A — STRATEGY CATALOG (aligned with year-sheet STR-IDs)'
ws['B5'].font = section_font
ws['B5'].fill = section_fill
ws['B5'].alignment = left

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

# Reconciled catalog — STR-IDs match Y2025!A6:A20 (and the other year sheets)
# Format: (id, impact, name, bucket, fw_ref, target_line, helper, sign, cap, maturity, desc)
rows = [
    # STR-001 S-Corp Wage Optimization — 2 impacts (matches year-sheet TargetLine=1z + CounterLine=8)
    ('STR-001', 1, 'S-Corp Wage Optimization',     'Core',    '#2',     '1z',  'OWNER_PAY',        -1, 'Reasonable comp (RCReports / industry avg)', 'Standard', 'Reduce W-2 wages to reasonable comp; surplus shifts to K-1'),
    ('STR-001', 2, 'S-Corp Wage Optimization',     'Core',    '#2',     '8',   'K1_SCorp_Active',  +1, 'Mirrors Impact 1 amount',                    'Standard', 'Surplus from W-2 reduction lands as K-1 active income'),

    # STR-002 HSA Family Max — single impact (above-line deduction Line 10)
    ('STR-002', 1, 'HSA Family Max',               'Supp.',   '—',      '10',  'HSA',              -1, '$8,300 family / $4,150 self (2024)',         'Standard', 'Health Savings Account above-line deduction'),

    # STR-003 Charitable Bunching (DAF) — itemized deduction (Line 12)
    ('STR-003', 1, 'Charitable Bunching (DAF)',    'Supp.',   'B5',     '12',  'CHARITY_DAF',      -1, '30%/60% AGI limits',                         'Standard', 'Bunch multi-year giving into one DAF year; itemize that year'),

    # STR-004 SEP-IRA / Solo 401(k) — defaults to Line 8 (user pref, S-Corp owner context)
    ('STR-004', 1, 'SEP-IRA / Solo 401(k)',        'Core',    '#3',     '8',   'RETIREMENT',       -1, '25% of comp; $66K combined (2024)',          'Standard', 'Retirement contribution defaults to Line 8 (S-Corp owner); change to 10 for sole-prop'),

    # STR-005 Cost Seg Study — Sch E rental
    ('STR-005', 1, 'Cost Seg Study',               'Core',    '#4',     '8',   'SchE_Rental',      -1, '25% Y1 accel of building basis (default)',   'Verified', 'Engineering reclass + bonus depr on rental property'),

    # STR-006 Roth Conversion — year sheet has TargetLine=1z; canonical is Line 4b but preserve user choice
    ('STR-006', 1, 'Roth Conversion',              'Supp.',   'B4',     '1z',  'ROTH_CONV',        +1, 'Bracket management',                         'Standard', 'Trad → Roth conversion (creates taxable income; revisit TargetLine — canonical is 4b)'),

    # STR-007 Augusta Rule §280A — business deduction
    ('STR-007', 1, 'Augusta Rule (§280A)',         'Core',    '#5 LHF', '8',   'AUGUSTA',          -1, '≤14 days/yr at FMV',                         'Standard', 'S-Corp rents owner residence ≤14 days; deduction to business, tax-free to owner'),

    # STR-008 Accountable Plan
    ('STR-008', 1, 'Accountable Plan',             'Core',    '#5 LHF', '8',   'ACCT_PLAN',        -1, 'Substantiated expenses only',                'Standard', 'Written plan reimburses owner-employee for business-use of home/vehicle'),

    # STR-009 Hire Children — 3 impacts (matches year-sheet TargetLine=8 + CounterLine=1z; + info-only Roth)
    ('STR-009', 1, 'Hire Children',                'Core',    '#5 LHF', '8',   'CHILD_WAGES',      -1, 'Reasonable wages for age/work',              'Standard', 'Wages deductible to business'),
    ('STR-009', 2, 'Hire Children',                'Core',    '#5 LHF', '1z',  'CHILD_WAGES',      +1, "Child's std ded $14,600 (2024)",             'Standard', "Wages reportable on child's return; offset by std ded"),
    ('STR-009', 3, 'Hire Children',                'Core',    '#5 LHF', '—',   'CHILD_ROTH',        0, 'Up to $7K Roth IRA cap',                     'Standard', 'Informational — child can fund Roth IRA from earned wages'),

    # STR-010 Entity Restructuring — 2 impacts (matches year-sheet TargetLine=8 + CounterLine=1z)
    ('STR-010', 1, 'Entity Restructuring',         'Advanced','#1',     '8',   'STRUCTURAL',       -1, 'Case-by-case',                               'Confirmed', 'Reshape entity (HoldCo over OpCo, F-reorg, P→S conv)'),
    ('STR-010', 2, 'Entity Restructuring',         'Advanced','#1',     '1z',  'STRUCTURAL',       +1, 'Case-by-case',                               'Confirmed', 'Reasonable comp adjustment after restructure'),

    # STR-011 Installment Sale / 1031 — capital gain deferral
    ('STR-011', 1, 'Installment Sale / 1031',      'Supp.',   'B6',     '7',   'CG_DEFER',         -1, 'Transaction-triggered',                      'Standard', 'Installment §453 or §1031 like-kind defers capital gain recognition'),

    # STR-012 Bonus Depreciation §168(k)
    ('STR-012', 1, 'Bonus Depreciation §168(k)',   'Core',    '#4',     '8',   'SchE_Rental',      -1, '60% (2024) → 40% (2025) phase-down',         'Verified', 'First-year bonus depreciation on qualifying property'),

    # STR-013 R&D Credit §41 — credit reduces tax (Line 20)
    ('STR-013', 1, 'R&D Credit §41',               'Advanced','—',      '20',  'CREDIT_RD',        -1, 'Qualifying research expenses',                'Verified', 'Section 41 research credit — offsets tax on Line 20'),

    # STR-014 SALT PTE Election — year sheet has TargetLine=12 (user choice); canonical is reduce K-1 income at entity level
    ('STR-014', 1, 'SALT PTE Election',            'Supp.',   'B1',     '12',  'PTET',             -1, '100% state tax via entity',                  'Verified', 'Pass-through entity pays state tax federally; revisit TargetLine — canonical reduces K-1 (8)'),

    # STR-015 Timing / Deferral — generic year-end lever
    ('STR-015', 1, 'Timing / Deferral',            'Supp.',   'B3',     '8',   'TIMING',           -1, 'Universal year-end lever',                   'Standard', 'Accelerate deductions / defer income (or reverse)'),
]

start_row = 8
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        cell = ws.cell(row=start_row + i, column=2 + j, value=v)
        cell.font = label_font
        cell.alignment = left
        cell.border = thin
        if headers[j] in ('Impact_Num', 'Sign'):
            cell.alignment = center

end_row = start_row + len(rows) - 1
table_ref = f'B7:L{end_row}'
table = Table(displayName='tblMasterStrategies', ref=table_ref)
table.tableStyleInfo = TableStyleInfo(
    name='TableStyleMedium2', showFirstColumn=False, showLastColumn=False,
    showRowStripes=True, showColumnStripes=False,
)
ws.add_table(table)
print(f"  Section A built: {len(rows)} impact rows (was 20, now {len(rows)})")

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
    ('Supp.',    'Bucket B — 7 supplemental strategies. PTET, TaxLoss, IncShift/Timing, Roth, DAF, 1031, OppZone'),
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
# SECTION C — Sign convention
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
# SECTION D — STRATEGY BUILDER
# ----------------------------------------------------------------------
builder_row = sign_row + 2 + len(signs) + 2
ws.merge_cells(f'B{builder_row}:L{builder_row}')
ws.cell(row=builder_row, column=2, value='▸ SECTION D — STRATEGY BUILDER (live tool — pick + size a strategy)').font = section_font
ws.cell(row=builder_row, column=2).fill = section_fill
ws.cell(row=builder_row, column=2).alignment = left

br_input = builder_row + 2
input_yellow = PatternFill('solid', fgColor='FFF2CC')

# Pick STR-ID
ws.cell(row=br_input, column=2, value='Strategy:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=2).alignment = right
ws.cell(row=br_input, column=3, value='STR-001').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=3).fill = input_yellow
ws.cell(row=br_input, column=3).alignment = center
ws.cell(row=br_input, column=3).border = thin

str_ids = sorted({r[0] for r in rows})
dv_str = DataValidation(type='list', formula1=f'"{",".join(str_ids)}"', allow_blank=False)
dv_str.add(f'C{br_input}')
ws.add_data_validation(dv_str)

ws.cell(row=br_input, column=4, value='Amount:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=4).alignment = right
ws.cell(row=br_input, column=5, value=25000).font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=5).fill = input_yellow
ws.cell(row=br_input, column=5).alignment = center
ws.cell(row=br_input, column=5).border = thin
ws.cell(row=br_input, column=5).number_format = '"$"#,##0'

ws.cell(row=br_input, column=6, value='For Year:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=6).alignment = right
ws.cell(row=br_input, column=7, value='=Active_Year').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=7).fill = input_yellow
ws.cell(row=br_input, column=7).alignment = center
ws.cell(row=br_input, column=7).border = thin

ws.cell(row=br_input, column=8, value='Status:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=8).alignment = right
ws.cell(row=br_input, column=9, value='Proposed').font = Font(name='Calibri', size=11, bold=True, color='1F4E79')
ws.cell(row=br_input, column=9).fill = input_yellow
ws.cell(row=br_input, column=9).alignment = center
ws.cell(row=br_input, column=9).border = thin

dv_status = DataValidation(type='list', formula1='"Proposed,Approved,Committed,Implemented"', allow_blank=False)
dv_status.add(f'I{br_input}')
ws.add_data_validation(dv_status)

ws.cell(row=br_input, column=10, value='Cap rule:').font = Font(name='Calibri', size=10, bold=True)
ws.cell(row=br_input, column=10).alignment = right
ws.cell(row=br_input, column=11, value=f'=VLOOKUP($C${br_input},$B$8:$L${end_row},9,FALSE)').font = Font(name='Calibri', size=9, italic=True, color='C00000')
ws.cell(row=br_input, column=11).alignment = left
ws.cell(row=br_input, column=11).border = thin

hdr_b_row = br_input + 2
ws.merge_cells(start_row=hdr_b_row, start_column=2, end_row=hdr_b_row, end_column=12)
ws.cell(row=hdr_b_row, column=2, value='▾ All impacts for the selected strategy (paste signed amounts into Y[year] sheet)').font = Font(name='Calibri', size=10, italic=True, color='3F3F3F')

hdr2_row = hdr_b_row + 1
builder_headers = ['#', 'Strategy_ID', 'Strategy_Name', 'TargetLine', 'HelperTreatment',
                   'Sign', 'Amount (signed)', 'Status', 'Cap_Rule', 'Description']
for i, h in enumerate(builder_headers):
    c = ws.cell(row=hdr2_row, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin

for i in range(5):
    r = hdr2_row + 1 + i
    impact_num = i + 1
    match_formula = (
        f'IFERROR(INDEX($B$8:$L${end_row},'
        f'MATCH(1,($B$8:$B${end_row}=$C${br_input})*($C$8:$C${end_row}={impact_num}),0),'
    )
    ws.cell(row=r, column=2, value=impact_num).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=2).alignment = center
    ws.cell(row=r, column=2).border = thin
    ws.cell(row=r, column=3, value=f'={match_formula}1),"")').font = label_font
    ws.cell(row=r, column=3).alignment = center
    ws.cell(row=r, column=3).border = thin
    ws.cell(row=r, column=4, value=f'={match_formula}3),"")').font = label_font
    ws.cell(row=r, column=4).alignment = left
    ws.cell(row=r, column=4).border = thin
    ws.cell(row=r, column=5, value=f'={match_formula}6),"")').font = label_font
    ws.cell(row=r, column=5).alignment = center
    ws.cell(row=r, column=5).border = thin
    ws.cell(row=r, column=6, value=f'={match_formula}7),"")').font = label_font
    ws.cell(row=r, column=6).alignment = center
    ws.cell(row=r, column=6).border = thin
    ws.cell(row=r, column=7, value=f'={match_formula}8),"")').font = label_font
    ws.cell(row=r, column=7).alignment = center
    ws.cell(row=r, column=7).border = thin
    amt_formula = (
        f'=IFERROR(IF({match_formula}8),""),'
        f'$E${br_input}*{match_formula}8),"")),"")'
    )
    ws.cell(row=r, column=8, value=amt_formula).font = Font(name='Calibri', size=10, bold=True, color='1F4E79')
    ws.cell(row=r, column=8).alignment = right
    ws.cell(row=r, column=8).border = thin
    ws.cell(row=r, column=8).number_format = '"$"#,##0;("$"#,##0);"-"'
    ws.cell(row=r, column=9, value=f'=IF({match_formula}1),"")="","",$I${br_input})').font = label_font
    ws.cell(row=r, column=9).alignment = center
    ws.cell(row=r, column=9).border = thin
    ws.cell(row=r, column=10, value=f'={match_formula}9),"")').font = Font(name='Calibri', size=9, italic=True)
    ws.cell(row=r, column=10).alignment = left
    ws.cell(row=r, column=10).border = thin
    ws.merge_cells(start_row=r, start_column=11, end_row=r, end_column=12)
    ws.cell(row=r, column=11, value=f'={match_formula}11),"")').font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws.cell(row=r, column=11).alignment = left
    ws.cell(row=r, column=11).border = thin

note_row = hdr2_row + 7
ws.merge_cells(start_row=note_row, start_column=2, end_row=note_row, end_column=12)
ws.cell(row=note_row, column=2, value=f'Tip: change C{br_input}, E{br_input}, I{br_input} above. Blank rows = strategy has fewer impacts than the slot. STR-IDs match year-sheet table at Y[year]!A6:A20.').font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
ws.cell(row=note_row, column=2).alignment = left
ws.row_dimensions[note_row].height = 28

# ----------------------------------------------------------------------
# SECTION E — Open Reconciliation Items (revisit later)
# ----------------------------------------------------------------------
recon_row = note_row + 3
ws.merge_cells(f'B{recon_row}:L{recon_row}')
ws.cell(row=recon_row, column=2, value='▸ SECTION E — OPEN RECONCILIATION ITEMS (REVISIT)').font = section_font
ws.cell(row=recon_row, column=2).fill = PatternFill('solid', fgColor='C00000')
ws.cell(row=recon_row, column=2).alignment = left

recon_items = [
    ('ITEM-RECON-1', 'STR-006 Roth Conversion',     'Year sheet has TargetLine=1z (wages). Canonical for Roth conversion is Line 4b (IRA distributions taxable). Confirm whether year-sheet choice is intentional or a placeholder.'),
    ('ITEM-RECON-2', 'STR-014 SALT PTE Election',   'Year sheet has TargetLine=12 (itemized ded). Federally, PTET reduces K-1 income at entity level (Line 8), not itemized. Confirm whether year-sheet choice reflects an alternative modeling approach.'),
    ('ITEM-RECON-3', 'STR-002 HSA Family Max',      'Year sheet has TargetLine=10 (above-line deductions, Schedule 1). HSA is correctly above-line. Confirm Helper_Treatment "HSA" maps to your Treatment_Profile_Map.'),
    ('ITEM-RECON-4', 'STR-009 Hire Children info',  'Catalog has 3rd row (Impact_Num=3) for child Roth contribution as info-only (Sign=0). Year sheet has 2-impact CounterLine model. Either add info row to year sheet or drop from catalog.'),
    ('ITEM-RECON-5', 'STR-010 Entity Restructure',  'Year sheet has TargetLine=8 + CounterLine=1z. Restructure mechanics vary by entity type. Confirm whether default fan-out captures intent or if it should be per-case.'),
    ('ITEM-RECON-6', 'Bucket alignment',            'Catalog buckets (Core/Supp./Advanced) come from Framework_Ref. Year sheet does not track Bucket. Not a blocker but useful to add to year sheet later.'),
]
hdr_recon = ['Item', 'Subject', 'Detail']
for i, h in enumerate(hdr_recon):
    c = ws.cell(row=recon_row+2, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin
ws.merge_cells(start_row=recon_row+2, start_column=4, end_row=recon_row+2, end_column=12)
for i, (item, subj, detail) in enumerate(recon_items):
    r = recon_row + 3 + i
    ws.cell(row=r, column=2, value=item).font = Font(name='Calibri', size=9, bold=True, color='C00000')
    ws.cell(row=r, column=2).alignment = center
    ws.cell(row=r, column=2).border = thin
    ws.cell(row=r, column=3, value=subj).font = label_font
    ws.cell(row=r, column=3).alignment = left
    ws.cell(row=r, column=3).border = thin
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=12)
    ws.cell(row=r, column=4, value=detail).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws.cell(row=r, column=4).alignment = left
    ws.cell(row=r, column=4).border = thin
    ws.row_dimensions[r].height = 30

# ----------------------------------------------------------------------
# Column widths + title height
# ----------------------------------------------------------------------
widths = [3, 13, 11, 28, 10, 14, 12, 22, 6, 28, 18, 50]
for i, w in enumerate(widths):
    ws.column_dimensions[get_column_letter(i+1)].width = w
ws.row_dimensions[2].height = 26

# ----------------------------------------------------------------------
# Save
# ----------------------------------------------------------------------
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Master_Strategies']
print(f"\nVerification:")
print(f"  Total impact rows: {len(rows)} (catalog range B8:L{end_row})")
# Compare with year sheet
ws_y = wb2['Y2025']
print(f"\nSTR-ID alignment check (year sheet vs catalog):")
yr_names = {ws_y.cell(row=r, column=1).value: ws_y.cell(row=r, column=2).value
            for r in range(6, 21) if ws_y.cell(row=r, column=1).value}
cat_names = {r[0]: r[2] for r in rows if r[1] == 1}  # first impact only
for sid in sorted(yr_names):
    match = '✓' if yr_names[sid] == cat_names.get(sid) else '✗'
    print(f"  {sid}: yr={yr_names[sid]!r:48} cat={cat_names.get(sid)!r:48} {match}")
