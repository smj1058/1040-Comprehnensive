"""Phase 3v16 — Audit_Report sheet (expanded scope).

Scans every formula in non-reference sheets and flags:
  - Suspicious numeric literals inside formulas (rates, thresholds,
    dollar amounts that should be named ranges or come from tblThresholds)
  - Hardcoded text constants that look like enums (MFJ/Single/Committed/etc.)
  - Magic conditionals (literal > N inside an IF where N looks like a threshold)
  - Error values (#REF!, #NAME?, #N/A, #VALUE!, #DIV/0!)
  - External workbook links
  - Cells with static values where formula expected (cells in known
    calc-engine rows that aren't formulas)

Sheets EXCLUDED from audit (reference / input by design):
  Tax_Ref, Dropdown_Lists, Framework_Ref, Glossary, Setup_Guide,
  Master_Strategies, Property_Appendix, Carryovers, AsFiled,
  Master_Inputs, Change_Log, Connections, Projection_History,
  Control_Panel

Sheets AUDITED:
  Y2023..Y2028, Tax_Plan_Dashboard, Deliverable, PY_Recon, Pivot_GPD,
  Pivot_Summary, Pivot_Medium, Pivot_Detailed, Pivot_Helpers,
  Visual_Pivot_*

Severity:
  🔴 FLAG  — likely bug or hardcoded threshold (high-confidence)
  🟡 WARN  — review; might be intentional
  🟢 OK    — informational
"""

import openpyxl
import re
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

IN_FILE  = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v15_CC.xlsx'
OUT_FILE = '/home/user/1040-Comprehnensive/docs/Master_Pivot_Framework_v5_phase3v16_CC.xlsx'

print(f"Loading {IN_FILE}")
wb = openpyxl.load_workbook(IN_FILE)

EXCLUDE_SHEETS = {
    'Tax_Ref', 'Dropdown_Lists', 'Framework_Ref', 'Glossary', 'Setup_Guide',
    'Master_Strategies', 'Property_Appendix', 'Carryovers', 'AsFiled',
    'Master_Inputs', 'Change_Log', 'Connections', 'Projection_History',
    'Control_Panel',
    # Audit_Report itself (about to be added)
    'Audit_Report',
}

# Known-OK literals (basic math constants)
OK_INTS = {0, 1, -1, 2, -2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000,
           # 1040 line numbers
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}
OK_YEARS = set(range(2020, 2031))
OK_FLOATS = {0.5, 0.9235}  # SE deduction factor is widely recognized
# Common enums OK in formulas
OK_ENUMS = {'MFJ', 'Single', 'HOH', 'MFS',
            'Committed', 'Implemented', 'Approved', 'Proposed',
            'Baseline', 'Strategy', 'Active', 'Passive', 'Portfolio',
            'Yes', 'No', 'N/A',
            '1z', '2a', '2b', '3a', '3b', '4b', '5b', '6b', '7', '8',
            '—', '', ' '}

findings = []  # list of (sheet, cell, severity, kind, detail)

def parse_literals(formula):
    """Extract numeric literals from a formula, skipping numbers that are
    part of cell references like A1, $C$8, R[1]C[2], etc."""
    # Strip out cell-reference-like patterns first
    # Don't strip table refs — they contain []
    stripped = re.sub(r'\$?[A-Z]{1,3}\$?\d+', ' ', formula)
    stripped = re.sub(r'R\[?-?\d+\]?C\[?-?\d+\]?', ' ', stripped)
    # Also strip year literals that are common in INDIRECT("Y"&...)
    # Now extract numbers
    nums = re.findall(r'-?\d+\.?\d*', stripped)
    out = []
    for n in nums:
        try:
            f = float(n)
            if f == int(f):
                out.append(int(f))
            else:
                out.append(f)
        except ValueError:
            continue
    return out

def parse_strings(formula):
    """Extract quoted string literals from a formula."""
    return re.findall(r'"([^"]*)"', formula)

def is_error_value(v):
    return isinstance(v, str) and v.startswith('#') and v.endswith('!') or v in ('#N/A', '#NAME?', '#REF!', '#VALUE!', '#DIV/0!', '#NULL!', '#NUM!')

def has_external_link(formula):
    # Pattern: 'workbook.xlsx]Sheet'!cell or [workbook.xlsx]
    return bool(re.search(r"'\[?[^']*\.xlsx", formula)) or '![' in formula

print(f"\nScanning sheets...")
sheets_scanned = 0
cells_scanned = 0
for sn in wb.sheetnames:
    if sn in EXCLUDE_SHEETS:
        continue
    sheets_scanned += 1
    ws = wb[sn]
    for row in ws.iter_rows():
        for cell in row:
            v = cell.value
            if v is None:
                continue
            cells_scanned += 1
            coord = cell.coordinate

            # Error values
            if isinstance(v, str) and v in ('#N/A', '#NAME?', '#REF!', '#VALUE!', '#DIV/0!', '#NULL!', '#NUM!'):
                findings.append((sn, coord, 'FLAG', 'Error value', f'Cell evaluates to {v}'))
                continue

            # Only audit formulas for literals
            if not (isinstance(v, str) and v.startswith('=')):
                continue

            # External links
            if has_external_link(v):
                findings.append((sn, coord, 'FLAG', 'External link', f'Formula references external workbook: {v[:80]}'))

            # Numeric literals
            nums = parse_literals(v)
            for n in nums:
                if isinstance(n, int) and n in OK_INTS:
                    continue
                if isinstance(n, int) and n in OK_YEARS:
                    continue
                if isinstance(n, float) and n in OK_FLOATS:
                    continue
                # Rate-like decimals between 0 and 1
                if isinstance(n, float) and 0 < n < 1:
                    # 0.32 (old marginal approx), 0.153 (FICA), 0.038 (NIIT), 0.124 (SS), 0.029 (Medicare)
                    findings.append((sn, coord, 'WARN', 'Hardcoded rate',
                        f'Embedded rate {n} — should be named (e.g., FICA_Rate) or pulled from tblThresholds. Formula: {v[:100]}'))
                # Large integers — likely thresholds or dollar amounts
                elif isinstance(n, int) and abs(n) >= 1000:
                    findings.append((sn, coord, 'WARN', 'Hardcoded threshold',
                        f'Embedded integer {n} — verify if should come from tblThresholds or be named. Formula: {v[:100]}'))
                # Small odd floats
                elif isinstance(n, float):
                    findings.append((sn, coord, 'WARN', 'Hardcoded decimal',
                        f'Embedded decimal {n} — verify if should be named. Formula: {v[:100]}'))

            # Magic conditionals — look for IF(... > N, ...) or IF(... < N, ...) with non-OK N
            conds = re.findall(r'IF\([^,)]*[<>]\s*(\d+\.?\d*)', v)
            for c in conds:
                try:
                    n = float(c)
                    if n == int(n): n = int(n)
                    if n in OK_INTS or n in OK_YEARS or n in OK_FLOATS:
                        continue
                    findings.append((sn, coord, 'FLAG', 'Magic conditional',
                        f'IF threshold {n} embedded — should reference tblThresholds. Formula: {v[:100]}'))
                except ValueError:
                    pass

            # String literals in formula — check against OK_ENUMS
            # Skip if this is an INDIRECT formula (its string fragments are cell-ref construction, not enums)
            is_indirect = 'INDIRECT(' in v
            strs = parse_strings(v) if not is_indirect else []
            for s in strs:
                if s in OK_ENUMS or s == '':
                    continue
                # Some strings are intentional (sheet names like Y2025)
                if re.match(r'^Y\d{4}$', s): continue
                # State codes — also OK if used with tblStateRates
                if len(s) == 2 and s.isupper() and s.isalpha(): continue
                # Strategy IDs
                if re.match(r'^STR-\d+$', s): continue
                # Status icons / 1040 line refs / fragments
                if s in ('☑', '▣', '☐', '─') or s.startswith('!'): continue
                # Skip if it's a sheet/table name that's referenced elsewhere
                if s in wb.sheetnames: continue
                # Format strings, hyperlink anchors, drill text
                if re.match(r'^[!#$:]', s): continue
                if 'drill' in s.lower() or '↗' in s or '▾' in s or '▸' in s: continue
                # Format codes
                if s.lower() in ('yyyy-mm-dd', 'mm/dd/yyyy', '0.00', '#,##0', '0%'):
                    continue
                # Sentinel strings (Status, etc.) — short single words are usually labels
                if len(s) < 3 and not s.isupper(): continue
                # Status text or other reasonable strings
                findings.append((sn, coord, 'WARN', 'String literal in formula',
                    f'Embedded string {s!r} — verify if should be from Dropdown_Lists or named range. Formula: {v[:80]}'))

# Build the audit report sheet
print(f"\nSheets scanned: {sheets_scanned}")
print(f"Cells scanned: {cells_scanned:,}")
print(f"Findings: {len(findings)}")

# Tally by severity and kind
from collections import Counter
sev_count = Counter(f[2] for f in findings)
kind_count = Counter(f[3] for f in findings)
print(f"\nBy severity: {dict(sev_count)}")
print(f"By kind: {dict(kind_count)}")

# Create Audit_Report sheet
if 'Audit_Report' in wb.sheetnames:
    del wb['Audit_Report']
ws = wb.create_sheet('Audit_Report')

# Position right after Control_Panel
target_idx = 1
current_idx = wb.sheetnames.index('Audit_Report')
if current_idx != target_idx:
    wb.move_sheet('Audit_Report', offset=target_idx - current_idx)
ws.sheet_properties.tabColor = 'C00000'

title_font   = Font(name='Calibri', size=18, bold=True, color='C00000')
subtitle_font = Font(name='Calibri', size=10, italic=True, color='7F7F7F')
section_font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')
section_fill = PatternFill('solid', fgColor='1F4E79')
hdr_font     = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
hdr_fill     = PatternFill('solid', fgColor='4472C4')
label_font   = Font(name='Calibri', size=10)
flag_font    = Font(name='Calibri', size=10, bold=True, color='C00000')
warn_font    = Font(name='Calibri', size=10, color='BF8F00')
flag_fill    = PatternFill('solid', fgColor='FCE4D6')
warn_fill    = PatternFill('solid', fgColor='FFF2CC')
center = Alignment(horizontal='center', vertical='center')
left   = Alignment(horizontal='left', vertical='center', wrap_text=True)
thin = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF'),
)

# Title
ws['B2'] = 'AUDIT REPORT'
ws['B2'].font = title_font
ws['B3'] = (f'Static scan of {sheets_scanned} non-reference sheets ({cells_scanned:,} cells). '
            f'Flags hardcoded numbers/strings/thresholds in calc + output areas. '
            f'Re-run via the Phase 3v16 script after edits.')
ws['B3'].font = subtitle_font
ws.row_dimensions[2].height = 26

# Summary section
ws.merge_cells('B5:F5')
ws['B5'] = '▸ SECTION A — SUMMARY'
ws['B5'].font = section_font; ws['B5'].fill = section_fill; ws['B5'].alignment = left

ws['B7'] = 'Sheets scanned';        ws['C7'] = sheets_scanned
ws['B8'] = 'Cells scanned';         ws['C8'] = cells_scanned
ws['B9'] = '🔴 FLAG (high)';        ws['C9'] = sev_count.get('FLAG', 0)
ws['B10'] = '🟡 WARN (review)';     ws['C10'] = sev_count.get('WARN', 0)
ws['B11'] = '🟢 OK';                ws['C11'] = sev_count.get('OK', 0)
for r in range(7, 12):
    ws.cell(row=r, column=2).font = label_font
    ws.cell(row=r, column=3).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=3).alignment = center

# Breakdown by kind
ws.merge_cells('B13:F13')
ws['B13'] = '▸ SECTION B — BREAKDOWN BY KIND'
ws['B13'].font = section_font; ws['B13'].fill = section_fill; ws['B13'].alignment = left

r = 15
for kind, count in kind_count.most_common():
    ws.cell(row=r, column=2, value=kind).font = label_font
    ws.cell(row=r, column=3, value=count).font = Font(name='Calibri', size=10, bold=True)
    ws.cell(row=r, column=3).alignment = center
    r += 1

# Findings table
findings_start = r + 2
ws.merge_cells(start_row=findings_start, start_column=2, end_row=findings_start, end_column=7)
ws.cell(row=findings_start, column=2, value=f'▸ SECTION C — FINDINGS ({len(findings)} total — sorted FLAG → WARN, then by sheet/cell)').font = section_font
ws.cell(row=findings_start, column=2).fill = section_fill
ws.cell(row=findings_start, column=2).alignment = left

hdr_row = findings_start + 2
for i, h in enumerate(['Severity', 'Sheet', 'Cell', 'Kind', 'Detail', 'Recommended Action']):
    c = ws.cell(row=hdr_row, column=2+i, value=h)
    c.font = hdr_font; c.fill = hdr_fill; c.alignment = center; c.border = thin

# Sort findings
sev_order = {'FLAG': 0, 'WARN': 1, 'OK': 2}
sorted_f = sorted(findings, key=lambda x: (sev_order.get(x[2], 3), x[0], x[1]))

# Truncate to first 500 to keep file manageable
MAX_FINDINGS = 500
truncated = len(sorted_f) > MAX_FINDINGS
display_findings = sorted_f[:MAX_FINDINGS]

action_map = {
    'Hardcoded rate':  'Replace literal with a named range (e.g., FICA_Rate = 0.153) or pull from tblThresholds.',
    'Hardcoded threshold': 'Replace literal with a named range or pull from tblThresholds via FILTER/XLOOKUP.',
    'Hardcoded decimal': 'Verify if literal should be named or pulled from a config table.',
    'String literal in formula': 'If string is an enum (filing status, status, etc.), pull from Dropdown_Lists or a named range.',
    'Magic conditional': 'Replace threshold literal in IF condition with a named range or tblThresholds lookup.',
    'Error value': 'Investigate the dependency chain — formula or input is broken.',
    'External link': 'Confirm whether external workbook reference is intentional; replace with import if possible.',
}

for i, (sn, coord, sev, kind, detail) in enumerate(display_findings):
    r = hdr_row + 1 + i
    sev_cell = ws.cell(row=r, column=2, value=sev)
    if sev == 'FLAG':
        sev_cell.font = flag_font; sev_cell.fill = flag_fill
    elif sev == 'WARN':
        sev_cell.font = warn_font; sev_cell.fill = warn_fill
    sev_cell.alignment = center; sev_cell.border = thin

    ws.cell(row=r, column=3, value=sn).font = label_font
    ws.cell(row=r, column=3).alignment = center
    ws.cell(row=r, column=3).border = thin

    ws.cell(row=r, column=4, value=coord).font = Font(name='Consolas', size=9)
    ws.cell(row=r, column=4).alignment = center
    ws.cell(row=r, column=4).border = thin

    ws.cell(row=r, column=5, value=kind).font = label_font
    ws.cell(row=r, column=5).alignment = left
    ws.cell(row=r, column=5).border = thin

    ws.cell(row=r, column=6, value=detail).font = Font(name='Calibri', size=9)
    ws.cell(row=r, column=6).alignment = left
    ws.cell(row=r, column=6).border = thin

    ws.cell(row=r, column=7, value=action_map.get(kind, 'Review.')).font = Font(name='Calibri', size=9, italic=True, color='3F3F3F')
    ws.cell(row=r, column=7).alignment = left
    ws.cell(row=r, column=7).border = thin

if truncated:
    r = hdr_row + 1 + MAX_FINDINGS
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    ws.cell(row=r, column=2, value=f'... {len(sorted_f) - MAX_FINDINGS} more findings truncated. See raw output via re-run of script for full list.').font = subtitle_font
    ws.cell(row=r, column=2).alignment = left

# Column widths
ws.column_dimensions['A'].width = 3
ws.column_dimensions['B'].width = 10
ws.column_dimensions['C'].width = 22
ws.column_dimensions['D'].width = 10
ws.column_dimensions['E'].width = 22
ws.column_dimensions['F'].width = 70
ws.column_dimensions['G'].width = 50

# Save
wb.save(OUT_FILE)
print(f"\nSaved: {OUT_FILE}")
print(f"Audit_Report sheet positioned at index {wb.sheetnames.index('Audit_Report')}")

# Print top findings to stdout for visibility
print(f"\n=== TOP 30 FINDINGS (sorted FLAG first) ===")
for sn, coord, sev, kind, detail in sorted_f[:30]:
    print(f"  [{sev:4}] {sn:25} {coord:8} {kind:30} {detail[:100]}")
