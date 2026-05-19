"""Phase 3v10 — State tax stack.

Adds multistate allocation capability to Master_Inputs and a state rate
reference table to Tax_Ref. Three new columns on Master_Inputs:

  T: Primary_State        — main state for sourcing (UT, CA, NY, ...)
  U: State_Mix            — text override for multi-state allocations
                           (e.g., "UT 70 CA 30"; blank = 100% Primary)
  V: PTET_Routed          — Yes/No: is this row part of a PTET election?

Plus:
  - States dropdown list added to Dropdown_Lists (column I)
  - Data validation on Master_Inputs!T5:T503 (states list)
  - Data validation on Master_Inputs!V5:V503 (Yes/No)
  - Named ranges: States, PTET_States
  - Tax_Ref new section "STATE TAX RATES + PTET" at row 615+
    (15 common states with top marginal rates 2024 + PTET flags)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v9_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v10_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

# Styles
hdr_font   = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill   = PatternFill('solid', fgColor='4472C4')
label_font = Font(name='Calibri', size=10)
section_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill = PatternFill('solid', fgColor='1F4E79')
input_fill = PatternFill('solid', fgColor='FFF2CC')
center = Alignment(horizontal='center', vertical='center')
left   = Alignment(horizontal='left',   vertical='center')
right  = Alignment(horizontal='right',  vertical='center')
thin   = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)

# ======================================================================
# PART 1 — Master_Inputs: add 3 columns at T, U, V
# ======================================================================
ws = wb['Master_Inputs']
print(f"\n--- Part 1: Master_Inputs columns T, U, V ---")

# Headers at row 4
ws.cell(row=4, column=20, value='Primary_State').font = hdr_font
ws.cell(row=4, column=20).fill = hdr_fill
ws.cell(row=4, column=20).alignment = center
ws.cell(row=4, column=20).border = thin

ws.cell(row=4, column=21, value='State_Mix').font = hdr_font
ws.cell(row=4, column=21).fill = hdr_fill
ws.cell(row=4, column=21).alignment = center
ws.cell(row=4, column=21).border = thin

ws.cell(row=4, column=22, value='PTET_Routed').font = hdr_font
ws.cell(row=4, column=22).fill = hdr_fill
ws.cell(row=4, column=22).alignment = center
ws.cell(row=4, column=22).border = thin

# Default values for existing rows (5-18): Primary_State = State of Residence from Control_Panel
# Use Control_Panel's State of Residence (currently at C16 — need to verify)
cp = wb['Control_Panel']
state_residence_row = None
for r in range(10, 50):
    if cp.cell(row=r, column=2).value == 'State of Residence':
        state_residence_row = r
        break
print(f"  Control_Panel 'State of Residence' at row {state_residence_row}, value={cp.cell(row=state_residence_row, column=3).value!r}")

# Seed defaults for existing data rows
for r in range(5, 19):
    if ws.cell(row=r, column=1).value is not None:  # only rows with data
        ws.cell(row=r, column=20, value=f'=Control_Panel!$C${state_residence_row}').font = label_font
        ws.cell(row=r, column=20).alignment = center
        ws.cell(row=r, column=20).border = thin
        ws.cell(row=r, column=20).fill = input_fill
        # State_Mix left blank (= 100% Primary)
        ws.cell(row=r, column=21).font = label_font
        ws.cell(row=r, column=21).alignment = center
        ws.cell(row=r, column=21).border = thin
        ws.cell(row=r, column=21).fill = input_fill
        # PTET_Routed default No
        ws.cell(row=r, column=22, value='No').font = label_font
        ws.cell(row=r, column=22).alignment = center
        ws.cell(row=r, column=22).border = thin
        ws.cell(row=r, column=22).fill = input_fill

# Column widths
ws.column_dimensions['T'].width = 14
ws.column_dimensions['U'].width = 20
ws.column_dimensions['V'].width = 12

# Try to extend the Master_Inputs table to include the new columns
print(f"  Master_Inputs tables: {[t.name for t in ws.tables.values()] if hasattr(ws, 'tables') else 'none'}")
for tbl in ws.tables.values():
    print(f"    table {tbl.name}: ref={tbl.ref}")
    # Existing ref is e.g. A4:S503 — extend to V503
    old_ref = tbl.ref
    # Parse end cell column letter
    import re
    m = re.match(r'^([A-Z]+)(\d+):([A-Z]+)(\d+)$', old_ref)
    if m:
        start_col, start_row, end_col, end_row = m.groups()
        new_ref = f"{start_col}{start_row}:V{end_row}"
        tbl.ref = new_ref
        print(f"    extended to {new_ref}")

# ======================================================================
# PART 2 — Dropdown_Lists: add States column at column I
# ======================================================================
ws_dd = wb['Dropdown_Lists']
print(f"\n--- Part 2: Dropdown_Lists States column ---")

# Header row 3
ws_dd.cell(row=3, column=9, value='States').font = hdr_font
ws_dd.cell(row=3, column=9).fill = hdr_fill
ws_dd.cell(row=3, column=9).alignment = center

# Full US state list + DC + PR (51 entries)
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS',
          'KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
          'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
for i, st in enumerate(states):
    ws_dd.cell(row=4+i, column=9, value=st).font = label_font
    ws_dd.cell(row=4+i, column=9).alignment = center

# Named range States (col I, rows 4-54)
if 'States' in wb.defined_names:
    del wb.defined_names['States']
wb.defined_names['States'] = DefinedName(
    name='States',
    attr_text=f'Dropdown_Lists!$I$4:$I${4+len(states)-1}'
)
print(f"  Added {len(states)} states; named range States = Dropdown_Lists!$I$4:$I${4+len(states)-1}")

# ======================================================================
# PART 3 — Add data validation to Master_Inputs T column (states) + V (Yes/No)
# ======================================================================
print(f"\n--- Part 3: Master_Inputs data validations ---")
dv_states = DataValidation(type='list', formula1='=States', allow_blank=True)
dv_states.add('T5:T503')
ws.add_data_validation(dv_states)

dv_yn = DataValidation(type='list', formula1='"Yes,No"', allow_blank=False)
dv_yn.add('V5:V503')
ws.add_data_validation(dv_yn)
print("  Added State dropdown on T5:T503, Yes/No on V5:V503")

# ======================================================================
# PART 4 — Tax_Ref: new STATE TAX RATES + PTET section
# ======================================================================
ws_tr = wb['Tax_Ref']
print(f"\n--- Part 4: Tax_Ref state rate reference ---")

# Find end of existing Tax_Ref content
start_row = ws_tr.max_row + 3
print(f"  Adding section at row {start_row}")

# Section header
ws_tr.merge_cells(start_row=start_row, start_column=2, end_row=start_row, end_column=9)
ws_tr.cell(row=start_row, column=2, value='STATE TAX RATES + PTET ELIGIBILITY (2024)').font = section_font
ws_tr.cell(row=start_row, column=2).fill = section_fill
ws_tr.cell(row=start_row, column=2).alignment = left

# Subtitle
ws_tr.cell(row=start_row+1, column=2,
    value='Top marginal rate by state + whether PTET (pass-through entity tax) election is available. '
          'Update annually as PTET landscape changes.').font = Font(name='Calibri', size=9, italic=True, color='7F7F7F')
ws_tr.merge_cells(start_row=start_row+1, start_column=2, end_row=start_row+1, end_column=9)

# Headers
hdr_row = start_row + 3
state_headers = ['State', 'Top_Marginal_Rate', 'Has_PTET', 'PTET_Rate', 'Notes']
for i, h in enumerate(state_headers):
    c = ws_tr.cell(row=hdr_row, column=2+i, value=h)
    c.font = hdr_font
    c.fill = hdr_fill
    c.alignment = center
    c.border = thin

# State data (2024 top marginal rates + PTET eligibility — illustrative; update annually)
state_data = [
    # (state, top_rate, has_ptet, ptet_rate, notes)
    ('AL', 0.0500, 'Yes', 0.0500, 'PTET election available'),
    ('AK', 0.0000, 'No',  None,   'No state income tax'),
    ('AZ', 0.0250, 'Yes', 0.0250, 'Flat 2.5%; PTET election available'),
    ('AR', 0.0440, 'Yes', 0.0440, 'PTET election available'),
    ('CA', 0.1330, 'Yes', 0.0930, '13.3% top rate (12.3% + 1% mental health surtax over $1M); PTET 9.3%'),
    ('CO', 0.0440, 'Yes', 0.0440, 'Flat 4.4%; PTET election available'),
    ('CT', 0.0699, 'Yes', 0.0699, 'PTET mandatory; election to opt out as of 2024'),
    ('DE', 0.0660, 'Yes', 0.0660, 'PTET election available'),
    ('DC', 0.1075, 'No',  None,   'No PTET as of 2024'),
    ('FL', 0.0000, 'No',  None,   'No state personal income tax'),
    ('GA', 0.0539, 'Yes', 0.0539, 'PTET election available'),
    ('HI', 0.1100, 'Yes', 0.1100, 'PTET election available'),
    ('ID', 0.0580, 'Yes', 0.0580, 'Flat 5.8%; PTET election available'),
    ('IL', 0.0495, 'Yes', 0.0495, 'PTET election available'),
    ('IN', 0.0315, 'Yes', 0.0315, 'PTET election available'),
    ('IA', 0.0590, 'Yes', 0.0590, 'PTET election available'),
    ('KS', 0.0570, 'Yes', 0.0570, 'PTET election available'),
    ('KY', 0.0400, 'Yes', 0.0400, 'PTET election available'),
    ('LA', 0.0425, 'Yes', 0.0425, 'PTET election available'),
    ('ME', 0.0715, 'No',  None,   'No PTET as of 2024'),
    ('MD', 0.0575, 'Yes', 0.0800, 'PTET 8% (includes county add-back)'),
    ('MA', 0.0900, 'Yes', 0.0500, 'Top rate 9% (5% + 4% millionaires tax); PTET 5%'),
    ('MI', 0.0425, 'Yes', 0.0425, 'PTET election available'),
    ('MN', 0.0985, 'Yes', 0.0985, 'PTET election available'),
    ('MS', 0.0440, 'Yes', 0.0500, 'PTET election available'),
    ('MO', 0.0480, 'Yes', 0.0480, 'PTET election available'),
    ('MT', 0.0590, 'Yes', 0.0590, 'PTET election available'),
    ('NE', 0.0524, 'Yes', 0.0524, 'PTET election available'),
    ('NV', 0.0000, 'No',  None,   'No state personal income tax'),
    ('NH', 0.0000, 'No',  None,   'No income tax on wages (interest/dividends only — repealed 2025)'),
    ('NJ', 0.1075, 'Yes', 0.1075, 'PTET (BAIT) election available'),
    ('NM', 0.0590, 'Yes', 0.0590, 'PTET election available'),
    ('NY', 0.1090, 'Yes', 0.0685, 'PTET 6.85% on income up to $2M; higher above'),
    ('NC', 0.0450, 'Yes', 0.0450, 'PTET election available'),
    ('ND', 0.0250, 'No',  None,   'Top 2.5%; no PTET'),
    ('OH', 0.0399, 'Yes', 0.0399, 'PTET election available'),
    ('OK', 0.0475, 'Yes', 0.0475, 'PTET election available'),
    ('OR', 0.0990, 'Yes', 0.0990, 'PTET election available'),
    ('PA', 0.0307, 'No',  None,   'Flat 3.07%; no PTET'),
    ('RI', 0.0599, 'Yes', 0.0599, 'PTET election available'),
    ('SC', 0.0640, 'Yes', 0.0300, 'PTET 3%'),
    ('SD', 0.0000, 'No',  None,   'No state personal income tax'),
    ('TN', 0.0000, 'No',  None,   'No state income tax (Hall tax repealed 2021)'),
    ('TX', 0.0000, 'No',  None,   'No state personal income tax'),
    ('UT', 0.0465, 'Yes', 0.0465, 'Flat 4.65%; PTET election available'),
    ('VT', 0.0875, 'No',  None,   'No PTET'),
    ('VA', 0.0575, 'Yes', 0.0575, 'PTET election available'),
    ('WA', 0.0000, 'No',  None,   'No state personal income tax (7% capital gains tax)'),
    ('WV', 0.0512, 'Yes', 0.0512, 'PTET election available'),
    ('WI', 0.0765, 'Yes', 0.0790, 'PTET 7.9%'),
    ('WY', 0.0000, 'No',  None,   'No state personal income tax'),
]

for i, (st, tr, ptet, ptet_r, notes) in enumerate(state_data):
    r = hdr_row + 1 + i
    ws_tr.cell(row=r, column=2, value=st).font = label_font
    ws_tr.cell(row=r, column=2).alignment = center
    ws_tr.cell(row=r, column=2).border = thin

    ws_tr.cell(row=r, column=3, value=tr).font = label_font
    ws_tr.cell(row=r, column=3).alignment = right
    ws_tr.cell(row=r, column=3).border = thin
    ws_tr.cell(row=r, column=3).number_format = '0.00%'

    ws_tr.cell(row=r, column=4, value=ptet).font = label_font
    ws_tr.cell(row=r, column=4).alignment = center
    ws_tr.cell(row=r, column=4).border = thin

    if ptet_r is not None:
        ws_tr.cell(row=r, column=5, value=ptet_r)
        ws_tr.cell(row=r, column=5).number_format = '0.00%'
    ws_tr.cell(row=r, column=5).font = label_font
    ws_tr.cell(row=r, column=5).alignment = right
    ws_tr.cell(row=r, column=5).border = thin

    ws_tr.cell(row=r, column=6, value=notes).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws_tr.cell(row=r, column=6).alignment = left
    ws_tr.cell(row=r, column=6).border = thin

state_table_end_row = hdr_row + len(state_data)
print(f"  Wrote {len(state_data)} states (rows {hdr_row+1}-{state_table_end_row})")

# Set column widths
ws_tr.column_dimensions['F'].width = 50

# Named ranges for state lookup
if 'tblStateRates' in wb.defined_names:
    del wb.defined_names['tblStateRates']
wb.defined_names['tblStateRates'] = DefinedName(
    name='tblStateRates',
    attr_text=f'Tax_Ref!$B${hdr_row+1}:$F${state_table_end_row}'
)

if 'PTET_States' in wb.defined_names:
    del wb.defined_names['PTET_States']
# PTET_States = filter where Has_PTET=Yes — store as a static name (used by formulas)
wb.defined_names['PTET_States'] = DefinedName(
    name='PTET_States',
    attr_text=f'Tax_Ref!$B${hdr_row+1}:$D${state_table_end_row}'
)
print(f"  Named ranges: tblStateRates, PTET_States")

# ======================================================================
# Save
# ======================================================================
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")

# Verify
wb2 = openpyxl.load_workbook(OUT_FILE)
ws2 = wb2['Master_Inputs']
print(f"\nVerification:")
print(f"  Master_Inputs T4: {ws2.cell(row=4, column=20).value!r}")
print(f"  Master_Inputs U4: {ws2.cell(row=4, column=21).value!r}")
print(f"  Master_Inputs V4: {ws2.cell(row=4, column=22).value!r}")
print(f"  Master_Inputs T5 (seeded): {ws2.cell(row=5, column=20).value!r}")
print(f"  Master_Inputs V5 (seeded): {ws2.cell(row=5, column=22).value!r}")
ws2 = wb2['Dropdown_Lists']
print(f"  Dropdown_Lists I3: {ws2.cell(row=3, column=9).value!r}")
print(f"  Dropdown_Lists I4-I7: {[ws2.cell(row=r, column=9).value for r in range(4, 8)]}")
ws2 = wb2['Tax_Ref']
print(f"  Tax_Ref state section ends at row {state_table_end_row}")
print(f"  Sample state row: {[ws2.cell(row=hdr_row+1, column=c).value for c in range(2, 7)]}")
print(f"  States named range: {wb2.defined_names['States'].value}")
print(f"  tblStateRates: {wb2.defined_names['tblStateRates'].value}")
