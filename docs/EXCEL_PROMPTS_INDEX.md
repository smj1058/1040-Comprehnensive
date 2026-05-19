# Excel Prompts Index

Each `EXCEL_PROMPT_*.md` is a self-contained prompt to paste into **Claude-in-Excel** (or Shortcut) with `Master_Pivot_Framework.xlsx` open at the desktop. Run them in the order they're listed if you're building out the workbook from scratch.

| # | Prompt file | What it does |
| --- | --- | --- |
| 1 | `REAL_PIVOT_DESKTOP_PROMPT.md` | Adds four `Visual_Pivot_*` tabs with real Excel PivotTables (slicers, drill-down) sourced from `tblMaster_Inputs` |
| 2 | `EXCEL_PROMPT_DRILL_LINKS.md` | Extends or modifies the existing drill panels / hyperlinks on the SUMIFS pivot tabs |
| 3 | `EXCEL_PROMPT_KISS_LAMBDAS.md` | Installs the 7 KISS LAMBDAs (Calc_OrdinaryTax, Calc_CapGainsTax, etc.) in Name Manager so the named ranges feed into actual tax computation |
| 4 | `EXCEL_PROMPT_QBI_ENTITIES.md` | Adds a `QBI_Entities` sheet for per-business QBI data (W-2 wages paid, UBIA, IsSSTB, aggregation group) |
| 5 | `EXCEL_PROMPT_CARRYOVERS.md` | Adds a `Carryovers` sheet for NOL, capital loss, passive loss, QBI loss, etc. — long-format per-client per-year |
| 6 | `EXCEL_PROMPT_EXTRACTION_IMPORT.md` | Builds the macro to import a tax-software extraction file (CSV/XLSX) and append rows into `tblMaster_Inputs` with field mapping |
| 7 | `EXCEL_PROMPT_ROLLFORWARD.md` | Year-end roll-forward macro — committed strategies absorbed as next-year baseline + carryover updates |
| 8 | `EXCEL_PROMPT_SNAPSHOT.md` | Snapshot / PROJECTION_HISTORY macro — captures current state at extension, S1, As-Filed |
| 9 | `EXCEL_PROMPT_DASHBOARD_EXPORT.md` | Builds `Dashboard_Export` tab — stable named-range block that Jeff's workbook can pull from |

## How to run any prompt

1. Open `Master_Pivot_Framework.xlsx` in Excel at the desktop.
2. Open Claude-in-Excel (sidebar/task pane — look for the Claude icon in the ribbon).
3. Open the relevant `EXCEL_PROMPT_*.md` file in a text editor.
4. Copy everything between the two `---` rulers.
5. Paste into the Claude-in-Excel chat.
6. Review what it proposes before letting it execute.

## Hard rule for every prompt

**Never modify `tblMaster_Inputs` column structure or rename it.** Every downstream consumer depends on its current schema:
- Column order
- Column names (`Baseline_Amount`, `Helper_Amount`, `Treatment_Profile`, etc.)
- Table name `tblMaster_Inputs`

Adding rows is fine. Adding new sheets is fine. Renaming/reordering columns or the table breaks the pivots, named ranges, and (eventually) the LAMBDAs and Jeff's workbook.
