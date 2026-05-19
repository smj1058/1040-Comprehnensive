# Prompt for Claude-in-Excel / Shortcut — Add or Modify Drill Links on Pivot Sheets

**Use this if you want to add more drill links, change where they jump to, or modify the FILTER drill panels on the pivot tabs of `Master_Pivot_Framework.xlsx`.**

---

I have a tax workbook `Master_Pivot_Framework.xlsx` with four pivot tabs that already have drill links and FILTER panels at the bottom. I want to [DESCRIBE WHAT YOU WANT — e.g., "add a hyperlink on every pivot value cell that jumps to the drill panel," or "add a second drill panel that filters by Year instead of by line"].

## Context — what's already in place

Every pivot tab (`Pivot_Summary`, `Pivot_Medium`, `Pivot_Detailed`, `Pivot_Helpers`) already has:

1. **Quick-jump hyperlink at cell `I2`**: `=HYPERLINK("#Master_Inputs!A1", "↗ Edit in Master_Inputs")` — clicks to Master_Inputs.

2. **Drill detail panel below the pivot data** with three parts:
   - A label `Drill into row:` at `A{drill_hdr_row + 1}` (e.g., A19 on Pivot_Summary)
   - A picker cell at `B{drill_hdr_row + 1}` with a data validation dropdown
   - A second hyperlink at `I{drill_hdr_row + 1}` to open Master_Inputs
   - A FILTER spill formula below the drill picker, columns InputID/Year/Bucket/Treatment_Profile/Payor/Baseline_Amount/Helper_Amount/Activity_Type/Notes

The FILTER formula matches by `Primary_Line` for the three line-based pivots (Summary/Medium/Detailed), and by `Helper_Treatment` for `Pivot_Helpers`.

## Source data table

- `tblMaster_Inputs` on `Master_Inputs` sheet
- Columns: `InputID | Year | ClientID | ClientName | Bucket | Treatment_Profile | Source_Document | Activity_Type | Provenance | Payor | Baseline_Amount | Helper_Amount | SE_Subject | NIIT_Class | QBI_Eligible | Primary_Line | Helper_Treatment | Consider | Notes`

## Common modifications you might want to make

### A. Make every pivot VALUE cell clickable to jump to its source rows

For each pivot tab, change the value cell formulas from raw `SUMIFS(...)` to something like:

```
=HYPERLINK("#"&CELL("address", $B$<drill_picker_row>), TEXT(SUMIFS(...), "$#,##0"))
```

Where the hyperlink target sets the drill picker to that row's label so the FILTER panel below auto-populates with those rows.

(Alternative: skip the value-cell hyperlink entirely. The existing per-row label dropdown + FILTER panel achieves the same end result with less clutter.)

### B. Add a YEAR-based drill instead of (or in addition to) the line-based drill

Add a second drill section below the existing one:

1. Cell with label `Drill into year:` and a year picker (dropdown of 2023-2028).
2. FILTER spill matching `tblMaster_Inputs[Year]=<picker>`.
3. Drill-by-year shows all rows for that year regardless of line.

### C. Change the FILTER columns shown in the drill panel

Edit the FILTER spill formula to include/exclude columns. The current set is: InputID, Year, Bucket, Treatment_Profile, Payor, Baseline_Amount, Helper_Amount, Activity_Type, Notes.

To add `Source_Document` and `Provenance`, append two more `FILTER(...)` calls inside the `HSTACK(...)`.

### D. Style improvements

- Bold the FILTER header row
- Apply currency formatting to the Baseline_Amount and Helper_Amount columns in the FILTER spill (use Conditional Formatting → Format only cells that contain → Number, or just select the columns and apply currency format)
- Freeze panes so the drill picker stays visible when scrolling the FILTER spill

## Constraints

- **Do NOT change cell addresses** of the pivot value cells (rows 5–18 in the data area). The named ranges on the workbook (`TaxableIncome`, `AGI`, `MAGI`, `W2_OWNER`, etc.) point at specific cells in the SUMIFS pivots that feed the LAMBDA layer. Moving cells breaks those.
- **Drill panel sits BELOW the pivot data** — it's safe to add/remove/restyle the drill panel since nothing references it.
- The pivot data area uses `SUMIFS` and the aggregators use sum-of-prior-rows formulas — leave those formulas alone.

## Test after each change

1. Click on `I2` of any pivot → should jump to Master_Inputs.
2. On any pivot, change the drill picker (`B<drill_row>`) to a different line/label → the FILTER spill below should update to show the matching rows.
3. Confirm `Pivot_Summary` totals haven't changed.
4. Confirm named ranges `TaxableIncome`, `AGI`, etc. still resolve to the correct cells (use Formulas → Name Manager to spot-check).
