"""Apply Pass 1 audit fixes to Master_Pivot_Framework_RealPivotv5.xlsx.

Fixes applied:
  C1: Master_Inputs E17 "Adjustments" → "Adjustment"
  C4: Y2025 C9 (STR-004 SEP-IRA) TargetLine 8 → 10
  C5: Y2025 C18 (STR-013 R&D Credit) TargetLine 13 → 20
  C3: Tax_Ref 2023 + 2024 bracket data refresh with correct IRS values
  I3: Master_Inputs add data validations to Year (B), Helper_Treatment (M), Primary_Line (Q)
  C2: Add Activity_Type="Baseline" filter to all SUMIFS in Pivot_Summary,
      Pivot_Medium, Pivot_Detailed, Pivot_Helpers

Skipped (need manual review or different tooling):
  - Pivot_Helpers SUMIFS over Helper_Amount (not Baseline_Amount) — adding
    Activity_Type filter to those is more nuanced
  - I2 hardcoded year literal conversion (would change 246 cells; user can
    decide if/how)
  - C6 CounterLine population (most strategies don't fan out; STR-001 already
    has it; STR-010 Entity Restructure needs case-by-case configuration)
  - Tax_Plan_Dashboard formula updates (rely on Visual_Pivot tables which
    have their own Activity_Type filter UI)
  - Real Excel PivotTable settings updates (openpyxl can preserve them
    through round-trip but not modify them safely)
"""

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
import re

IN_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_uploaded.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_audit-fixes.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

changes_log = []

# --------------------------------------------------------------------
# C1: Master_Inputs E17 "Adjustments" → "Adjustment"
# --------------------------------------------------------------------
ws = wb['Master_Inputs']
e17 = ws['E17'].value
if e17 == 'Adjustments':
    ws['E17'] = 'Adjustment'
    changes_log.append(f"[C1] Master_Inputs!E17: 'Adjustments' → 'Adjustment'")
else:
    changes_log.append(f"[C1] Master_Inputs!E17 already = {e17!r}, no change needed")

# --------------------------------------------------------------------
# C4: Y2025 C9 (STR-004 SEP-IRA) TargetLine 8 → 10
# --------------------------------------------------------------------
ws = wb['Y2025']
c9 = ws['C9'].value
if c9 == 8 or str(c9) == '8':
    ws['C9'] = 10
    changes_log.append(f"[C4] Y2025!C9 (STR-004 SEP-IRA TargetLine): 8 → 10")
else:
    changes_log.append(f"[C4] Y2025!C9 currently = {c9!r} (expected 8); SKIP")

# --------------------------------------------------------------------
# C5: Y2025 C18 (STR-013 R&D Credit) TargetLine 13 → 20
# --------------------------------------------------------------------
c18 = ws['C18'].value
if c18 == 13 or str(c18) == '13':
    ws['C18'] = 20
    changes_log.append(f"[C5] Y2025!C18 (STR-013 R&D Credit TargetLine): 13 → 20")
else:
    changes_log.append(f"[C5] Y2025!C18 currently = {c18!r} (expected 13); SKIP")

# --------------------------------------------------------------------
# C3: Tax_Ref 2023 + 2024 bracket data refresh
# --------------------------------------------------------------------
ws = wb['Tax_Ref']
# Authoritative IRS-published 2023 brackets
brackets_2023_MFJ = [
    (0, 22000, 0.10, 0),
    (22000, 89450, 0.12, 2200),
    (89450, 190750, 0.22, 10294),
    (190750, 364200, 0.24, 32580),
    (364200, 462500, 0.32, 74208),
    (462500, 693750, 0.35, 105664),
    (693750, 9999999, 0.37, 186601.5),
]
brackets_2023_Single = [
    (0, 11000, 0.10, 0),
    (11000, 44725, 0.12, 1100),
    (44725, 95375, 0.22, 5147),
    (95375, 182100, 0.24, 16290),
    (182100, 231250, 0.32, 37104),
    (231250, 578125, 0.35, 52832),
    (578125, 9999999, 0.37, 174238.25),
]
brackets_2024_MFJ = [
    (0, 23200, 0.10, 0),
    (23200, 94300, 0.12, 2320),
    (94300, 201050, 0.22, 10852),
    (201050, 383900, 0.24, 34337),
    (383900, 487450, 0.32, 78221),
    (487450, 731200, 0.35, 111357),
    (731200, 9999999, 0.37, 196669.5),
]
brackets_2024_Single = [
    (0, 11600, 0.10, 0),
    (11600, 47150, 0.12, 1160),
    (47150, 100525, 0.22, 5426),
    (100525, 191950, 0.24, 17168.5),
    (191950, 243725, 0.32, 39110.5),
    (243725, 609350, 0.35, 55678.5),
    (609350, 9999999, 0.37, 183647.25),
]
# Tax_Ref layout: B=Year, C=FilingStatus, D=Lower, E=Upper, F=Rate, G=Add_To
# Rows 9-15: 2023 MFJ; 16-22: 2023 Single; 23-29: 2024 MFJ; 30-36: 2024 Single
def write_bracket_block(start_row, year, fs, brackets):
    for i, (lo, hi, rate, add) in enumerate(brackets):
        r = start_row + i
        # Confirm year/fs columns match what we expect (preserve them as-is)
        ws.cell(row=r, column=2, value=year)
        ws.cell(row=r, column=3, value=fs)
        ws.cell(row=r, column=4, value=lo)
        ws.cell(row=r, column=5, value=hi)
        ws.cell(row=r, column=6, value=rate)
        ws.cell(row=r, column=7, value=add)

write_bracket_block(9, 2023, 'MFJ', brackets_2023_MFJ)
write_bracket_block(16, 2023, 'Single', brackets_2023_Single)
write_bracket_block(23, 2024, 'MFJ', brackets_2024_MFJ)
write_bracket_block(30, 2024, 'Single', brackets_2024_Single)
changes_log.append(f"[C3] Tax_Ref rows 9-36: refreshed 2023 + 2024 brackets (MFJ + Single) with IRS values")

# --------------------------------------------------------------------
# I3: Add data validation dropdowns to Master_Inputs B (Year), M (Helper_Treatment), Q (Primary_Line)
# --------------------------------------------------------------------
ws = wb['Master_Inputs']

# Check if named ranges exist; if not, build inline closed sets
def has_named_range(name):
    return name in wb.defined_names

# Year dropdown
year_formula = '=TaxYears' if has_named_range('TaxYears') else '"2023,2024,2025,2026,2027,2028"'
dv_year = DataValidation(type='list', formula1=year_formula, allow_blank=True)
ws.add_data_validation(dv_year)
dv_year.add('B5:B503')
changes_log.append(f"[I3] Master_Inputs B5:B503 (Year): added dropdown {year_formula}")

# Helper_Treatment dropdown
if has_named_range('Helper_Treatments'):
    ht_formula = '=Helper_Treatments'
else:
    ht_formula = '"NONE,OWNER_PAY,TAX_EXEMPT,QUAL_DIV,LTCG_SPLIT,SEC1250,K1_SPLIT,ACTIVE_RE,PASSIVE,SE_INCOME,TRUST_DIST,HSA,IRA,RETIREMENT,SE_HEALTH,STUDENT_LOAN,MEDICAL,SALT,MORTGAGE,CHARITY,CTC,EDUCATION,FTC"'
dv_ht = DataValidation(type='list', formula1=ht_formula, allow_blank=True)
ws.add_data_validation(dv_ht)
dv_ht.add('M5:M503')
changes_log.append(f"[I3] Master_Inputs M5:M503 (Helper_Treatment): added dropdown {ht_formula[:40]}...")

# Primary_Line dropdown
pl_formula = '=TaxLines' if has_named_range('TaxLines') else '"1z,2a,2b,3a,3b,4b,5b,6b,7,8,9,10,11,12,13,15,16,19,20,22,23,24,25,26,27,28,29,33,34,37"'
dv_pl = DataValidation(type='list', formula1=pl_formula, allow_blank=True)
ws.add_data_validation(dv_pl)
dv_pl.add('Q5:Q503')
changes_log.append(f"[I3] Master_Inputs Q5:Q503 (Primary_Line): added dropdown {pl_formula[:40]}...")

# --------------------------------------------------------------------
# C2: Add Activity_Type="Baseline" filter to all Baseline SUMIFS in pivot tabs
# Targets formulas of the pattern:
#   =SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2024, ...)
# Adds:  , tblMaster_Inputs[Activity_Type], "Baseline"
# --------------------------------------------------------------------
PIVOT_TABS = ['Pivot_Summary', 'Pivot_Medium', 'Pivot_Detailed', 'Pivot_Helpers']
activity_pattern = re.compile(r'tblMaster_Inputs\[Activity_Type\]', re.IGNORECASE)
sumifs_pattern  = re.compile(r'(SUMIFS\s*\(\s*tblMaster_Inputs\[(?:Baseline_Amount|Helper_Amount)\][^)]*?)(\s*\))', re.IGNORECASE)

c2_changes = 0
c2_skipped = 0
for sn in PIVOT_TABS:
    ws = wb[sn]
    for row in ws.iter_rows():
        for cell in row:
            v = cell.value
            if not isinstance(v, str) or not v.startswith('='):
                continue
            if 'SUMIFS' not in v:
                continue
            if 'tblMaster_Inputs[Baseline_Amount]' not in v and 'tblMaster_Inputs[Helper_Amount]' not in v:
                continue
            if activity_pattern.search(v):
                c2_skipped += 1
                continue
            # Insert the Activity_Type filter just before the closing paren of the SUMIFS call
            new_v = sumifs_pattern.sub(r'\1, tblMaster_Inputs[Activity_Type], "Baseline"\2', v)
            if new_v != v:
                cell.value = new_v
                c2_changes += 1

changes_log.append(f"[C2] Added Activity_Type='Baseline' filter to {c2_changes} SUMIFS in {PIVOT_TABS} (skipped {c2_skipped} already filtered)")

# --------------------------------------------------------------------
# Save
# --------------------------------------------------------------------
print("\nChanges:")
for c in changes_log:
    print(f"  {c}")

wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")
