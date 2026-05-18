# Desktop Handoff Prompt — Tax Workbook Rework

**Use this on the desktop Claude Code session (or whichever assistant
has filesystem access to `C:\...\Tax production three.xlsx`).**

Copy everything between the rulers below into the desktop session as a
single message, after pointing it at the workbook.

---

I'm reworking `Tax production three.xlsx` (path:
`C:\...\Tax production three.xlsx` — please open and inspect first).
We've done the design work in a separate cloud session; the full
architecture write-up is in `docs/TAX_WORKBOOK_PIVOT_ARCHITECTURE.md`
on the `claude/pivot-tax-calculations-q4NyZ` branch of the
`1040-Comprehnensive` repo. **Read that file end-to-end before doing
anything else** — it contains the final decisions, the schema, the
tab layout, and the open items.

Once you've read the design notes, do the following, in order:

## Step 1 — Inventory the current workbook

For each existing tab, report:

- Tab name and (if obvious) intended role
- Approximate row/column count of any data tables on it
- Whether it's a data sheet, calc sheet, presentation sheet, or
  control/UI sheet
- Any defined names that reference this tab (search Name Manager)
- Any pivot tables on this tab (count + source range)
- Any LAMBDAs defined that this tab participates in

I want a clear "here's what's currently in the file" snapshot before
we start moving things.

## Step 2 — Map current → target

For each existing tab, classify against the target architecture
(§11 of the design notes):

- **Keep as-is** — already fits the target architecture
- **Reshape** — content is right but layout / structure needs to
  change (e.g. wide → long, per-year → year-as-column)
- **Merge** — content overlaps with another tab's role and should be
  combined
- **Retire** — no role in the target architecture, content can be
  deleted (or archived if there's history worth preserving)

Produce this as a table. For "Reshape" and "Merge" rows, write a
one-sentence description of the transformation.

## Step 3 — Identify the gaps

What target tabs (`_Master`, `_Calc`, `Control`, `Strategies`,
`Projection`, `PBC Inventory`, `Snapshots`, `Dashboard_Export`) do
**not** yet exist? Which need to be created from scratch vs.
extracted from existing content?

## Step 4 — Resolve open items by inspection

Several open items in §12 of the design notes can be answered by
looking at the file:

- **Excel version / `GROUPBY` availability** — check via formula bar
  (`=GROUPBY(...)` in a scratch cell; if it autocompletes, you're on
  365 current channel)
- **What "S1" actually means in the existing Filing Stage usage** —
  search the workbook for "S1", "Scenario 1", "Stage 1", "Estimate 1"
  to see how it's currently used
- **Existing LAMBDAs** — list every name in Name Manager whose
  `RefersTo` starts with `=LAMBDA(`. For each, write one sentence on
  what it does and whether the target architecture (pivot-fed inputs)
  will need it rewritten

Report findings.

## Step 5 — Produce the migration plan

Given the inventory + gap analysis + open-item resolutions, propose
an ordered migration plan. Expected shape:

1. Create `_Master` tab with the target schema (empty)
2. Migrate data from `<existing tab>` into `_Master` (with a brief
   description of the transformation)
3. Repeat for each data source
4. Create `_Calc` tab and wire up pivots / `GROUPBY` aggregates
5. Create / refactor LAMBDAs to consume `_Calc` named ranges
6. Build `Projection` view with `SUMIFS` against `_Master`
7. ...etc

Order matters — flag any dependencies (e.g. "step N requires step M
to be complete before formulas will resolve"). Flag any steps that
need user input or judgment calls before they can proceed.

## Step 6 — STOP and wait for confirmation

Do not start executing the migration. Present the inventory, map,
gap analysis, open-item findings, and proposed plan, and wait for
me to confirm or adjust before any structural changes are made to
the workbook.

If during inventory you find anything that makes you think the
target architecture itself needs adjustment (e.g. existing complexity
that the design notes didn't account for), flag it explicitly — don't
silently work around it.

## Constraints

- **No destructive changes** until the plan is confirmed. Read-only
  inspection only for Steps 1–4.
- **Preserve existing LAMBDAs** until their replacements are wired
  up and verified. Don't delete defined names without checking
  downstream references.
- **If the file is open in Excel**, ask me to close it before doing
  anything that requires write access.
- **Keep a working copy.** Before any destructive change in Step 5+,
  save a timestamped backup (`Tax production three_backup_YYYY-MM-DD.xlsx`).

---

## Additional context for the desktop session

The full architecture write-up lives at:
`docs/TAX_WORKBOOK_PIVOT_ARCHITECTURE.md` (this same repo, branch
`claude/pivot-tax-calculations-q4NyZ`).

Key decisions already made (don't re-litigate; see §13 of the design
notes):

- Long-format master, no per-year input sheets
- Component columns on the view (`Baseline | Σ Adj | Σ Strat | Total`),
  not filing-stage columns
- `Source` ∈ {Baseline, Adjustment, Tax Strategy}
- `Status` flag on strategies drives include/exclude
- `Source Document` column on master drives PBC inventory generation
- Master and Control are separate tabs
- Pivots / `GROUPBY` isolated to `_Calc` to avoid adjacent-cell
  encroachment
- Snapshots are filtered copies of `_Master` tagged by Filing Stage +
  date, not copies of the wide view
- Roll-forward carries Baseline only (pivot-net from prior year As Filed)
