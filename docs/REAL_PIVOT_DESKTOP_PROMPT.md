# Prompt for Shortcut / Claude-in-Excel — Add Real PivotTables

**Use this prompt at your desktop with Shortcut or Claude-in-Excel, with `Master_Pivot_Framework.xlsx` open.**

---

I have a tax workbook (`Master_Pivot_Framework.xlsx`) with a long-format data table called **`tblMaster_Inputs`** on the `Master_Inputs` sheet. I want to **add real Excel PivotTables for visual analysis** alongside the existing SUMIFS-driven pivots that feed the LAMBDA layer.

## Context — what's already in the workbook

- **`Master_Inputs` sheet** holds `tblMaster_Inputs` — every committed baseline source-input row, year-tagged.
  Columns: `InputID | Year | ClientID | ClientName | Bucket | Treatment_Profile | Source_Document | Activity_Type | Provenance | Payor | Baseline_Amount | Helper_Amount | SE_Subject | NIIT_Class | QBI_Eligible | Primary_Line | Helper_Treatment | Consider | Notes`

- **Existing `Pivot_Summary`, `Pivot_Medium`, `Pivot_Detailed`, `Pivot_Helpers` sheets** are SUMIFS-driven aggregation tables. These feed named ranges (`TaxableIncome`, `AGI`, `MAGI`, `W2_OWNER`, `BI_SE_SUBJECT`, etc.) that feed LAMBDA tax calculations. **Do NOT modify these.** They need stable cell addresses for the named ranges.

- **`Y2025` sheet** is the active-year manual manipulation playground (S1 overrides + strategies table). Independent of the pivots.

## What I want you to add — real Excel PivotTables on new sheets

**Don't touch any existing sheet.** Add four NEW sheets, each with a real `Insert → PivotTable` PivotTable sourced from `tblMaster_Inputs`. These are for visual analysis (slicers, drill-down by double-click, drag-and-drop field rearrangement) — NOT for feeding the LAMBDAs.

### Sheet 1: `Visual_Pivot_Income`

- **Source**: `tblMaster_Inputs`
- **Rows**: `Primary_Line` (in this manual sort order: `1z, 2a, 2b, 3a, 3b, 7, 8, 9, 10, 12, 13, 15`)
  - Use Field Settings → Manual sort to enforce 1040 order
- **Columns**: `Year`
- **Values**: Sum of `Baseline_Amount`
- **Filter**: `Activity_Type` (allow filtering Baseline vs. Strategy vs. all)
- **Slicers** to add: `Activity_Type`, `ClientID`
- Pivot style: any "Medium" style with banded rows
- Show grand totals: rows and columns

### Sheet 2: `Visual_Pivot_BusinessIncome`

- **Source**: `tblMaster_Inputs`
- **Filter**: `Bucket = "Business Income"`
- **Rows**: `Treatment_Profile` (so you see SchC_Active, K1_PTP_Active, K1_PTP_Passive, K1_SCorp_Active, etc. broken out)
- **Columns**: `Year`
- **Values**: Sum of `Baseline_Amount`
- **Slicers**: `SE_Subject`, `NIIT_Class`, `QBI_Eligible`, `Activity_Type`
- Show grand totals

### Sheet 3: `Visual_Pivot_ByPayor`

- **Source**: `tblMaster_Inputs`
- **Rows**: `Payor`, then `Treatment_Profile` (nested)
- **Columns**: `Year`
- **Values**: Sum of `Baseline_Amount`
- **Slicers**: `ClientID`, `Bucket`, `Activity_Type`
- Show subtotals per Payor

### Sheet 4: `Visual_Pivot_HelperCarveOuts`

- **Source**: `tblMaster_Inputs`
- **Filter**: `Helper_Amount > 0` (so only rows with a helper carve-out)
- **Rows**: `Helper_Treatment`
- **Columns**: `Year`
- **Values**: Sum of `Helper_Amount`
- **Slicers**: `Bucket`, `Activity_Type`
- This shows the QUAL_DIV, OWNER_PAY, TAX_EXEMPT, SEC1250 amounts as the helper layer

## Constraints

- **Do NOT modify** existing sheets: `Master_Inputs`, `Pivot_Summary`, `Pivot_Medium`, `Pivot_Detailed`, `Pivot_Helpers`, `Y2025`, `Treatment_Profile_Map`, `Dropdown_Lists`.
- **Do NOT replace** the SUMIFS-driven pivots — those have named ranges (`TaxableIncome`, `AGI`, etc.) attached to specific cells that the LAMBDA layer depends on.
- The Real PivotTables are an **additive visual layer** for exploration.
- Set the workbook to refresh PivotTables on open (`File → Options → Save → check "Refresh data when opening the file"` — or set per-pivot via PivotTable Options).

## Optional follow-up (only if you want named ranges off the real pivots too)

If you want to use a real PivotTable as the *source* of a named range (not just for visual exploration), the trick is to wrap a `GETPIVOTDATA` formula in a cell, and put the named range on that cell:

```
=GETPIVOTDATA("Baseline_Amount", Visual_Pivot_Income!$A$3, "Year", 2025, "Primary_Line", "15")
```

Wrap that in a cell at a known address. Name the cell. That gives stable named ranges sourced from the real pivot.

But the existing SUMIFS pivots already do this job and don't need the intermediate PivotTable, so you'd only add `GETPIVOTDATA` if you specifically want the pivot's slicer state to influence the LAMBDA inputs (which is a more advanced workflow).

## Test after building

Once you've added the four visual pivots:
1. Click into `Visual_Pivot_Income`, double-click a value cell — Excel should drill through to a sheet showing the contributing rows from `tblMaster_Inputs`.
2. Use a slicer (e.g., set Activity_Type = "Strategy") — confirm the pivot updates to show only Strategy rows.
3. Right-click → Refresh on each pivot — confirm no errors, totals match the SUMIFS pivots on `Pivot_Summary`/`Pivot_Detailed`.
4. Save the file. Reopen it. Confirm pivots refresh on open (no stale data warning).
