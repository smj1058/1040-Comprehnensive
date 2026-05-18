# Tax Workbook — Pivot-Based Calculation Architecture (Design Notes)

**Status:** Design notes captured during a planning chat. Workbook
itself (`Tax production three.xlsx`) lives on Seth's C drive and was
not accessible from this cloud session — these notes are meant to be
carried into that workbook when back at the desktop.

**Context:** Rework of the comprehensive 1040 workbook. Going back and
forth between per-year input sheets and a master input sheet, with
tax calculations driven off pivots rather than direct cell references.
The premise: pivots → defined names → LAMBDAs is cleaner than chained
direct refs for the calc engine.

---

## 1. Source-of-truth model

- **Annual input sheets** = where data is entered. One per tax year.
- **Master sheet** = consolidated stacked table of every annual sheet's
  rows, with `Year` as a column. This is the input to the pivots.
- **Pivots on the master** = the source of truth for tax calculations.
- Annual sheets may carry **lightweight "quick & dirty" calcs locally**
  so a user doing a fast tax-planning estimate gets immediate feedback
  without round-tripping through the master. Those local calcs are
  **not authoritative** — the master pivots are.

Flow:

```
Annual sheet (YYYY)  ─┐
Annual sheet (YYYY-1)─┼──► Master (stacked) ──► Pivots ──► Defined names ──► LAMBDAs ──► Tax calcs
Annual sheet (YYYY-2)─┘
```

---

## 2. Amount-type dimension (multiple "versions" per year)

Each annual row carries an **Amount Type** so the same line item can
exist in several states within one tax year. Planned set:

| Amount Type | Meaning |
| --- | --- |
| **Extension** | Numbers used at extension filing (Form 4868 estimate basis) |
| **S1** | (To confirm — likely "Scenario 1" / first revision, or first estimate. Clarify before building.) |
| **Final / As Filed** | Numbers that match the return as ultimately filed |

> **Open question to resolve at desktop:** what exactly is "S1"?
> Candidates: Scenario 1, Q1 estimate, first amendment ("Superseded 1"),
> or first projection. The pivot's column/slicer behavior depends on
> this being a clean closed set.

**Recommendation:** make `Amount Type` a single column on every annual
row (not separate columns per type). That way the pivot can slice by
amount type without column-count explosion, and adding a new amount
type (e.g. an amended return) is one new value in the column, not a
schema change.

---

## 3. Two tables per annual sheet — Baseline vs. Tax Planning Adjustments

Each annual sheet has **two physical tables** that both get pushed into
the master:

1. **Baseline** — the "as-is" facts (W-2, 1099, K-1, Sch C activity,
   Sch E, deductions, credits, etc.).
2. **Tax Planning Adjustments** — proposed changes layered on top
   (Cost Seg acceleration, S-Corp election delta, retirement
   contribution bumps, Roth conversion blocks, QBI repositioning,
   etc.).

**Why two tables instead of one with a "type" column:**

- The adjustments are themselves baseline-ish (recurring playbook
  items, not free-form), so they have their own stable schema.
- Having them as a **separate pivot table** lets you toggle adjustments
  on/off cleanly — show baseline only, show baseline + adjustments,
  or show adjustments alone (delta view) — without dragging the
  baseline pivot around.
- Filtering one big pivot to "exclude adjustments" works but tends to
  get messy with `GETPIVOTDATA`. Two pivots = two clean named ranges.

**On the master:** both tables stack into the master as well, ideally
into the **same master table** with a column `Source = Baseline |
Adjustment`, OR as two parallel master tables (`Master_Baseline` and
`Master_Adjustments`). Either works; the column approach is more
flexible long-term, the two-table approach is what falls out
naturally if you push from the annual sheets table-by-table.

**Recommendation:** one master table with a `Source` column, then
build two pivots off the same master (filtered by Source). Single
source of truth, two slicing views.

---

## 4. Schema sketch — annual sheet rows

Minimum columns each row needs to support the pivot/LAMBDA layer:

| Column | Notes |
| --- | --- |
| `Year` | e.g. 2024 |
| `Amount Type` | Extension / S1 / Final (closed set, validated via data validation) |
| `Source` | Baseline / Adjustment |
| `Entity` | Taxpayer / Spouse / Joint / Entity name |
| `Category` | Wages, Sch C, Sch E, Sch D, IRA, Itemized, Credit, etc. |
| `Subcategory` | Specific line (e.g. "Sch C — gross receipts") |
| `Form / Line` | Optional but huge for traceability (e.g. `1040 line 1a`) |
| `Amount` | The number |
| `Memo` | Optional free text |

The pivot then has `Year` × `Amount Type` × `Category` (rows) crossed
with `Source` (columns or filter), summing `Amount`.

---

## 5. Pivot → defined names → LAMBDA

The mechanism that makes this calc-engine-friendly:

1. Pivot output (or `GROUPBY` spilled array in 365) sits in a known
   location on a `_Calc` tab.
2. Each meaningful aggregate gets a **defined name** that points at a
   `GETPIVOTDATA(...)` or `INDEX/XLOOKUP` against the spilled array.
   Wrap with `IFERROR(..., 0)` so empty categories don't `#REF!`.
3. LAMBDAs (named in Name Manager) take those names as inputs:
   - `TaxableIncome(year, amountType, source)` → number
   - `FederalTax(year, amountType, source)` → applies brackets
   - `QBIDeduction(...)`, `NIIT(...)`, `AMTDelta(...)`, etc.
4. The "Adjustment impact" view = `FederalTax(yr, type, "Baseline+Adj")
   − FederalTax(yr, type, "Baseline")`. Two pivots, one subtraction.

**Note on Excel version:** if Seth is on 365 current channel, prefer
`GROUPBY` / `PIVOTBY` over classic PivotTables — they spill, they're
formula-driven (recalc automatically with the rest of the workbook),
and they don't need a "Refresh All" step. Classic PivotTables require
manual or VBA-triggered refresh, which is the #1 reason pivot-based
calc engines get flaky.

---

## 6. Annual-sheet local "quick & dirty" calcs

Per Seth's note: the annual sheets should still let a user do a fast
tax-planning estimate without depending on the master being refreshed.

Approach:

- Keep a small calc block at the top/side of each annual sheet that
  references **the annual sheet's own tables directly** (no pivots).
- This produces a "preview" number — clearly labeled as preview, not
  authoritative.
- The master pivot result is what feeds the official deliverable
  (planning memo, projection, return reconciliation).

Visual rule: the local preview cell should show a delta vs. the master
pivot value when they disagree — that's the cue to refresh or
investigate.

---

## 7. Risks / things to watch

- **`GETPIVOTDATA` brittleness with missing categories.** Always
  `IFERROR(..., 0)` wrap. Or use `GROUPBY`/`PIVOTBY` to sidestep.
- **PivotTable refresh dependency.** If staying on classic pivots,
  consider a `Workbook_Open` or button-driven `RefreshAll` macro, or
  accept that calcs lag inputs until refresh. `GROUPBY` avoids this.
- **Amount Type closed-set discipline.** If users freetype "Ext.",
  "Extension ", "EXT" you'll get phantom pivot columns. Data
  validation dropdown is mandatory.
- **Source column on the master.** If annual sheets push two physical
  tables, make sure the push process tags each row's `Source`
  correctly before it lands on the master.
- **Year sheet proliferation vs. one stacked input.** Long-term, the
  cleanest move is to retire per-year sheets entirely and have one
  long stacked input table with `Year` as a column. But that's a
  bigger UX change — keeping per-year sheets as the input UI and
  stacking into the master is a reasonable middle ground.

---

## 8. Open items for the next desk session

- [ ] Confirm the exact closed set of `Amount Type` values (especially
      what "S1" means).
- [ ] Decide: one master table with `Source` column, or two parallel
      master tables (`Master_Baseline` / `Master_Adjustments`).
- [ ] Confirm Excel version — is `GROUPBY`/`PIVOTBY` available, or do
      we need to design around classic PivotTables?
- [ ] Inventory which LAMBDAs already exist in `Tax production three`
      and which need to be (re)written against the pivot outputs.
- [ ] Decide whether the annual-sheet local "quick & dirty" calcs
      should be deleted or kept once the master pivots are stable.
- [ ] Upload the workbook (or just the master tab as CSV) to this
      repo so the LAMBDA + pivot scaffolding can be sketched against
      real columns.
