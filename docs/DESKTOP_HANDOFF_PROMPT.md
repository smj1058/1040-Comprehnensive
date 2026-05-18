# Desktop Handoff Prompt — Tax Workbook (REVISED, much smaller scope)

**Status:** Revised 2026-05-18 after receiving the existing KISS Merge
handoff doc. The earlier version of this prompt assumed we were
designing the architecture from scratch — we're not. KISS is built.
This prompt is now a targeted "what to add on top" instead.

**Use this on the desktop Claude Code session that has filesystem
access to `Tax_Workbook_Production_v3.xlsm`** (at
`G:\Shared drives\_SMJ\___Product Development\1040 - Template Review\`).

Copy the section between the rulers below into that session.

---

I'm continuing work on `Tax_Workbook_Production_v3.xlsm`. The KISS
merge (Phases 1–7) is complete and Cedillo Y2024 ties out to $7,213.92
federal tax. Don't touch the year-sheet calc engine or the
auto-sync — those work.

The architecture decisions and full context are in TWO files in the
`1040-Comprehnensive` repo on branch
`claude/pivot-tax-calculations-q4NyZ`:

- `docs/TAX_WORKBOOK_PIVOT_ARCHITECTURE.md` — reconciliation between
  what we explored in chat vs. what's actually built (KISS). **Read
  this first.** Section "Revised game plan" is the work to do.
- `docs/DESKTOP_HANDOFF_PROMPT.md` — this file
- (Also relevant on Seth's desktop:
  `C:\Users\SethJohnson\MCP_Projects\tax-workbook-production\HANDOFF_v3_KISS.md`)

The KISS daily flow stays. The work below is **additive view layer**
on top of `Master_Inputs`, plus the items already in the KISS backlog.

## Work items (in priority order)

### Cleanup / unblock (do first)

1. **Triage the 7 external workbook links** on `CONNECTIONS`.
   Targets are: `Activity_Detail`, `Deductions_and_Adjustments1`,
   `Form_1040_Summary`, `2025`, `Y2022`, `STRATEGY_INPUTS`,
   `TAX_CALCULATIONS`. Several LAMBDAs depend on these
   (`EntityCount`, `RentalCount`, `LookupDed`, `LookupLine`) and
   currently return errors. For each: resolve path, embed the
   referenced data into a new tab, or rewrite the LAMBDA to read from
   `Master_Inputs`. **Report back what you find before deleting any
   external link** — could be live referenced data.

2. **Reconcile the two LAMBDA libraries.** 7 KISS LAMBDAs +
   14 v3-original LAMBDAs are both installed. For each v3 LAMBDA
   (`OrdTax_FN`, `CapGainsTax_FN`, `SETax_FN`, `NIIT_FN`, `QBI_FN`,
   `AddlMedicareTax_FN`, `FICA_EmployeeTax_FN`, `FICA_EmployerTax_FN`,
   `ExcessBusinessLossLimit_FN`, `NOLDeductionAllowed_FN`,
   `PassiveLossAllowed_FN`, `IncomeClassifier_FN`, `GetFITBrackets_FN`,
   `GetLTCGBrackets_FN`), check (a) is it referenced anywhere in the
   workbook, and (b) does KISS have an equivalent. Report a
   keep/retire table. **Don't retire anything yet** — just produce
   the table.

### KISS backlog (already on the list in HANDOFF_v3_KISS.md)

3. Fine-tune Y2025 input UX (column widths, label clarity, dropdowns,
   validation).
4. Apply Phases 3–6 to Y2023 and Y2026 so all four year sheets are
   consistent. Use `scripts/v3_kiss_merge_phase{3,4,5,6}.py` as
   reference.
5. Build the Roll-forward macro — copy PY input rows (without amounts,
   `Source = Baseline` only) into the next year sheet as a starting
   template. Macro lives in `modKissSync`.
6. Wire up `PullExtractionsToAsFiled` to read `CONNECTIONS` file paths
   and populate the `AsFiled` column on year sheets. Currently a stub.
7. Clean up stale v8.6 `Module1–4` VBA modules (harmless leftovers).

### New view layer on top of Master_Inputs (additive — does not touch KISS)

8. **Rebuild `Tax_Summary` as a `GROUPBY`-driven cross-year view**
   reading from `Master_Inputs`. Currently `#REF!`'d out. Goal: a
   single tab where you can pick a year (or "all years") and see a
   pivoted summary of every line item across years, scenarios, and
   baseline/adjustment split. Use `GROUPBY` (Excel 365 — confirmed
   available).

9. **Build `Year_Lookup_Summary` — CHOOSE-based cross-year roll-up.**
   Already on the KISS backlog. Per the resilience standards, use
   `CHOOSE` for cross-year refs, not `INDIRECT`.

10. **Rebuild `PBC_List` as `GROUPBY`-driven from `Master_Inputs`.**
    Filter to `Source = Baseline` and `Year = SelectedYear`, group by
    `Bucket`/`Source_Type`/`Payor`. Replaces the hardcoded version.
    Also DELETE `PBC_2026` — year scoping should be a parameter, not
    a sheet per year.

11. **Build `Dashboard_Export` tab** — a stable named-range block,
    `GROUPBY`-driven from `Master_Inputs`. Output is the three-number
    headline (or whatever the dashboard needs) at known cell addresses
    so downstream consumers (Jeff's dashboard workbook, leadership
    Power BI, etc.) have a contract that doesn't break when year-sheet
    layouts change.

12. **Repoint `CLIENT_DASHBOARD` / `DELIVERABLE` / `QUESTIONNAIRE`**
    formulas to read from `Dashboard_Export` named ranges instead of
    hardcoded year-sheet cells. This is KISS backlog #4 but with the
    target redirected to the new export block.

13. **Merge Jeff's dashboard workbook.** KISS backlog #2. Locate the
    file (currently TBD per the handoff). Bring his dashboard sheets
    in alongside (or replacing) CLIENT_DASHBOARD/DELIVERABLE, pointed
    at `Dashboard_Export`.

### Documentation / hygiene

14. Consolidate `User_Instructions` / `INSTRUCTIONS` / `SETUP_GUIDE`
    into a single instructions tab.

## Constraints

- **Do NOT modify the KISS calc engine** (the 7 KISS LAMBDAs, the
  same-sheet rollup on year sheets, the auto-sync, the
  `Treatment_Profile_Map` auto-fill). These work. Cedillo Y2024 ties
  to $7,213.92 — that's the validation case.
- **Do NOT change directionality** — year sheet remains primary, master
  remains downstream aggregate. New views read FROM master; they
  don't replace year sheets.
- **Save a timestamped backup** before any structural change.
- **No destructive operations** without confirmation — that includes
  retiring v3 LAMBDAs (step 2), deleting external links (step 1),
  deleting `PBC_2026` (step 10), or removing stale modules (step 7).
- **For each step, report before/after.** Output should include:
  what changed, where, and what was verified (e.g. "Cedillo Y2024
  still ties to $7,213.92").

## Stop and confirm

Before starting, read both architecture files
(`TAX_WORKBOOK_PIVOT_ARCHITECTURE.md` and the local
`HANDOFF_v3_KISS.md`). Then present an ordered plan of what you'd
attack first, what you need clarified, and what's likely to be quick
vs. slow. Wait for confirmation before making changes.
