# Tax Workbook — Final Architecture (Design Notes)

**Status:** Consolidated final verdict from a multi-turn design chat
(2026-05-18). Workbook itself (`Tax production three.xlsx`) lives on
Seth's C drive and was not accessible from this cloud session — these
notes are the handoff to the desktop session that *can* see the file.

**Context:** Rework of the comprehensive 1040 workbook. Started from
"per-year input sheets pushing into a master with pivots driving
LAMBDA calcs," iterated through wide-vs-long format and component-vs-
filing-stage column structures, and landed on the architecture below.

---

## TL;DR — the one-line summary

**One long-format master data store; everything else — projection view,
tax calc engine, PBC inventory, leadership dashboard, snapshots, tie-out
— is a derived view on top of it.**

---

## 1. Data store — `_Master` tab (the source of truth)

Long-format structured table. Hidden in production. One row per
financial entry; rows grow over time.

### Schema

| Column | Type | Notes |
| --- | --- | --- |
| `Year` | Integer | 2024, 2025, etc. |
| `Filing Stage` | Closed set | Extension / S1 / As Filed (compliance lifecycle dimension — open question on exact S1 meaning) |
| `Source` | Closed set | Baseline / Adjustment / Tax Strategy (layer dimension) |
| `Status` | Closed set | Proposed / Selected / Implemented / Rejected (only meaningful when `Source = Tax Strategy`; drives include/exclude) |
| `Entity` | Text | Taxpayer / Spouse / Joint / Entity name |
| `Category` | Closed set | Wages, Sch C, Sch E, Sch D, IRA, Itemized, Credit, etc. |
| `Subcategory` | Closed set | Specific line (e.g. "Sch C — gross receipts") |
| `Form / Line` | Text | Optional but high-value for traceability (e.g. `1040 line 1a`) |
| `Source Document` | Text | Underlying doc (K-1 Entity X, W-2 Employer Y, 1099-B Broker Z) — **drives PBC inventory generation** |
| `Amount` | Currency | The number |
| `Memo` | Text | Optional free notes |

### Hard rules

- All closed-set columns enforced via **data validation dropdowns**.
  No freetype — one typo creates a phantom pivot row.
- `Filing Stage`, `Source`, `Status` are dimensional. `Amount` is the
  only measure. Everything else describes the row.
- **Component model, not filing-stage columns.** Filing stage is a
  *row property* (captured at snapshot time), not a column on the
  visible view.

---

## 2. View layer — `Projection` tab (the daily UI)

Wide-format, year-scoped, one row per line item. Reads from `_Master`
via `SUMIFS`. This is what the team works in daily, what the client
sees in the presentation, and what feeds the leadership dashboard.

### Columns

| Column | Source |
| --- | --- |
| `Line` (Entity + Category + Subcategory) | Derived / lookup |
| `Baseline` | `=SUMIFS(_Master[Amount], _Master[Year], Selected_Year, _Master[Line], [@Line], _Master[Source], "Baseline")` |
| `Σ Adjustments` | Same `SUMIFS` filtered to `Source = "Adjustment"` |
| `Σ Strategies` | Same `SUMIFS` filtered to `Source = "Tax Strategy"` AND `Status IN ("Selected", "Implemented")` |
| `Total` | `=Baseline + Σ Adjustments + IF(Include_Strategies, Σ Strategies, 0)` |

### Control cells (driven from `Control` tab)

- `Selected_Year` — dropdown, drives which year the view shows
- `Include_Strategies` — TRUE/FALSE toggle for the Total formula
- (Optional) `Strategy_Status_Filter` — e.g. "Selected only" vs.
  "Selected + Proposed" for what-if views

### Why this structure wins

- Drill-down for free: wide view shows the sum, `_Master` shows the
  itemized why.
- Scenario flexibility via one toggle, not by maintaining parallel views.
- Multiple adjustments and strategies per line are preserved in the
  store but presented as clean sums in the view.

---

## 3. Calc layer — `_Calc` tab (the math engine)

**Isolated tab** so pivots / spilled arrays can't trample any
presentation-formatted content. Three layers:

1. **Aggregation** — `GROUPBY` / `PIVOTBY` spilled arrays (preferred,
   if on 365 current channel), or classic PivotTables (fallback).
   Aggregate `_Master` by Year × Category × Subcategory × Filing Stage,
   summing Amount, filtered by Status as needed.
2. **Defined names** — point at the aggregate output via
   `IFERROR(GETPIVOTDATA(...), 0)` (classic) or `IFERROR(INDEX/XLOOKUP
   on the spilled array, 0)` (`GROUPBY`).
3. **LAMBDA library** — named LAMBDAs in Name Manager consume the
   defined names: `TaxableIncome(year, stage)`, `FederalTax(...)`,
   `QBIDeduction(...)`, `NIIT(...)`, `AMTDelta(...)`, etc.

### Excel version is the pivotal decision

- **365 current channel:** use `GROUPBY` / `PIVOTBY`. Spills as
  formulas, recalcs with the workbook, no Refresh All needed, no
  adjacent-cell encroachment. "Presentable pivot" becomes free.
- **Classic Excel:** use PivotTables with discipline — PivotTable
  Options → Preserve cell formatting ON + Autofit column widths OFF;
  Design → Show in Tabular Form + Repeat All Item Labels; Value Field
  Settings → Number Format (not cell formatting). Isolate to `_Calc`
  to avoid encroachment.

**Action item:** confirm Excel version at the desktop session before
committing to either path.

---

## 4. Control layer — `Control` tab (the UI surface)

Separate from `_Master`. Named cells with labels, dropdowns, and
toggle buttons. Drives the rest of the workbook via named ranges.

- `Selected_Year` (dropdown of available years from `_Master`)
- `Include_Strategies` (TRUE/FALSE toggle)
- `Active_Filing_Stage` (used by Snapshot button — Extension / S1 / As Filed)
- `Strategy_Status_Filter` (optional)
- Snapshot button (runs the snapshot macro)
- Year roll-forward button (runs the roll-forward macro)

**Why not combine `Control` and `_Master`:** the master is a
structured table that needs to grow rows freely; the control sheet is
a fixed UI layout with named cells. Combining them creates layout
conflicts and visually buries the controls.

---

## 5. Strategies layer — `Strategies` tab

Year-scoped strategies table. Filtered view of `_Master` where
`Source = "Tax Strategy"` and `Year = Selected_Year`. `Status` column
is a dropdown (Proposed / Selected / Implemented / Rejected) — editing
the dropdown here writes back to `_Master`.

This is the surface where the team toggles which strategies are
"in" vs. "considered but not adopted." Changes here immediately
update the `Σ Strategies` column on `Projection` and the LAMBDAs
downstream.

---

## 6. PBC inventory — `PBC Inventory` tab

`GROUPBY(_Master, [Year, Entity, Source Document])` filtered to
`Source = "Baseline"`. Generates the prepared-by-client document
inventory automatically from the same data that feeds the tax calc.

One data store, third use case. Worth pointing out explicitly because
it justifies the `Source Document` column on `_Master`.

---

## 7. Leadership dashboard export

Stable named-range block on a `Dashboard_Export` tab (or hidden
flat table). The leadership dashboard pulls from here — Power Query,
linked workbook refs, or Power BI connection — and the export block
shields the dashboard from any layout changes on the human-facing
sheets.

**Open question:** confirm with leadership what they pull, at what
grain, on what cadence — that determines whether the export is a
named-range block, a flat table, or a Power Query feed.

---

## 8. Snapshot mechanism — VBA macro #1

Button on `Control`. Reads `Active_Filing_Stage`. Copies *the current
state of `_Master`*, filtered to that stage, into the `Snapshots`
archive (long-format, preserves all metadata, timestamped + stage-tagged).

Snapshots are how filing stages get captured as point-in-time
artifacts. The Projection view at snapshot time becomes "the Extension
package" or "the As Filed work paper" — the snapshot is the source
of truth for that frozen view.

Snapshots are themselves long-format, so analytics across snapshots
(e.g. "show me how projected federal tax moved from Extension → S1 →
As Filed for client X") remain trivial — same store shape, just
multiple time slices.

---

## 9. Year roll-forward — VBA macro #2

Button on `Control`. Two modes:

1. **Categories only** — copies the structure (rows + line items) from
   prior year, blank Amounts. For when this year's numbers will be
   fully replaced by extraction.
2. **Carry net forward** — reads pivot-net per line from prior year's
   `As Filed` snapshot (Baseline + Adjustments + Implemented Strategies)
   and writes a single new Baseline row per line for the new year.
   Strategies and Adjustments do NOT carry forward — they get absorbed
   into next-year Baseline because once implemented they're facts.

Macro only writes rows with `Source = "Baseline"` in the new year.

---

## 10. Tie-out / variance workpaper — separate workbook

Loads the extracted as-filed return data (long-format from a data
extraction tool). Diffs against the most recent `As Filed` snapshot
via `XLOOKUP` or Power Query merge. Variances → rework queue.

Because both sides are long-format, the diff is one operation, not
a manual reconciliation. This is the standard CPA "tie-out workpaper"
practice, automated.

---

## 11. Tab layout — recap

| Tab | Role | Visibility |
| --- | --- | --- |
| `_Master` | Long-format data store | Hidden in production |
| `_Calc` | Pivots / GROUPBY + named ranges + LAMBDAs | Hidden in production |
| `Control` | Year selector, toggles, macro buttons | Visible |
| `Strategies` | Current-year strategy table with Status dropdowns | Visible |
| `Projection` | Wide-format daily view (presentation grade) | Visible |
| `PBC Inventory` | Auto-generated document checklist | Visible |
| `Snapshots` | Archive of point-in-time master extracts | Visible (or hidden) |
| `Dashboard_Export` | Stable named-range block for leadership pull | Hidden |

---

## 12. Open items for the desktop session

- [ ] Confirm Excel version (365 current channel → `GROUPBY`; older → classic pivots)
- [ ] Confirm exact closed set for `Filing Stage` (especially what "S1" stands for)
- [ ] Audit the existing workbook against this target architecture:
  - Which tabs map to which target role?
  - What stays as-is?
  - What needs reshaping (e.g. wide tabs → long master)?
  - What gets deleted entirely?
- [ ] Inventory existing LAMBDAs in `Tax production three` and decide
      which to rewrite against pivot/`GROUPBY` outputs.
- [ ] Confirm leadership dashboard pull mechanism.
- [ ] Decide whether per-year input sheets are fully retired (current
      verdict: yes — collapse to master only) or kept as a transitional
      UX layer.
- [ ] Decide where the workbook ultimately lives (firm shared drive
      vs. per-client copy) — affects snapshot archive strategy.

---

## 13. Decisions made (so they don't get re-litigated)

1. **Long-format master, not per-year sheets.** Per-year sheets are
   retired. Master holds all years with `Year` as a column.
2. **Component columns on the view, not filing-stage columns.**
   `Baseline | Σ Adj | Σ Strat | Total`. Filing stage is captured by
   snapshotting, not by adding columns.
3. **`Source` has three values, not two.** Baseline / Adjustment /
   Tax Strategy.
4. **`Status` flag on strategies.** Proposed / Selected / Implemented /
   Rejected. Drives the include/exclude in `Σ Strategies`.
5. **`Source Document` column on master.** Drives PBC inventory.
6. **Master and Control are separate tabs.** Different layout
   pressures; combining them hurts both jobs.
7. **Pivots / GROUPBY isolated to `_Calc` tab.** Avoids the "pivot
   ate my adjacent column" problem.
8. **One data store, multiple views.** Projection, PBC inventory,
   dashboard export, tie-out — all derived from `_Master`.
9. **Snapshot = filtered copy of master tagged by Filing Stage + date.**
   Not a copy of the wide view.
10. **Roll-forward carries Baseline only.** Pulls pivot-net from prior
    year As Filed, writes as new-year Baseline. Adjustments and
    Strategies never carry forward.
