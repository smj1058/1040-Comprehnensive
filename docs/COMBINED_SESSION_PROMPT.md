# Combined Session Prompt — Tax Workbook Production v3 (KISS)

**Use this in a fresh Claude Code session at the desktop with filesystem
access to the workbook.** Self-contained — does not depend on any
earlier conversation or file in any other repo.

---

I'm working on a 1040 tax planning workbook with a "KISS"
architecture. I need you to read this prompt end-to-end before
touching anything, then give me a plan and wait for confirmation.

## Project identity

- **Workbook:** `Tax_Workbook_Production_v3.xlsm`
- **Location:** `G:\Shared drives\_SMJ\___Product Development\1040 - Template Review\Tax_Workbook_Production_v3.xlsm`
- **Pre-merge backup:** `archive\Tax_Workbook_Production_v3_pre_KISS_merge_2026-05-15.xlsm`
- **Build scripts:** `C:\Users\SethJohnson\MCP_Projects\tax-workbook-production\scripts\v3_kiss_merge_phase{1-7}.py`
- **VBA module source:** `C:\Users\SethJohnson\MCP_Projects\tax-workbook-production\scripts\modKissSync.bas`
- **Excel version:** 365 current channel (`GROUPBY` / `PIVOTBY` confirmed available)

## The architecture in one paragraph

KISS is **year-sheet-primary, master-downstream**. Year sheets
(`Y2023`, `Y2024`, `Y2025`, `Y2026`) are the preparer's working
surface — bucket-pattern input table on the left, tax rollup +
LAMBDA-driven calc on the right, planning adjustments table
underneath the rollup. The calc engine reads same-sheet ranges from
the active year sheet, so calc updates immediately as data is
entered. On every Ctrl+S, a `Workbook_BeforeSave` handler
auto-syncs every year sheet into two parent tables on `Master_Inputs`
and `Planning_Adjustments` for cross-year reporting. **Master is the
aggregate, not the calc source.** Going the other way
(`RefreshInputsFromMaster`) is a manual macro and intentionally not
automatic — overwriting in-progress work is dangerous.

## Scenario dimensions (5 levels, not 3)

Each line carries: `Baseline | Override | S1 | S2 | AsFiled`.
- **Baseline** — extracted / starting facts
- **Override** — preparer hardcodes over the baseline
- **S1** — Scenario 1 / Extension Estimate
- **S2** — Scenario 2 / second planning view
- **AsFiled** — what actually got filed

Each planning adjustment row carries both `S1_Amount` and `S2_Amount`
and a `Status` (`Proposed → Approved → Committed → Converted_To_Input`).
The rollup's `S1_Adj` and `S2_Adj` columns are SUMIFS over the
year-sheet planning table, filtered by status:
- S1 sum includes Proposed/Approved/Committed
- S2 sum includes Approved/Committed
- Converted_To_Input rows are excluded (they're now real inputs)

## Validation case (regression check — must remain green)

**Cedillo Y2024 must tie to $7,213.92 federal tax.**

Source data on Y2024:
- Wages $153,648 (W2-Self Pay, profile W2_SCorpOwner)
- K-1 Business Income -$100,766 (Partnership K-1, passive loss, profile K1_PTP_Passive)
- NonQual Dividends $25,922 (1099-DIV, profile Div_Ordinary)
- LTCG $14,487 (1099-B, profile LTCG_Stock)

Computed: Total Income $93,291 → AGI $93,291 → Std Deduction $29,200 →
QBI $0 (clamped from negative) → Taxable Income $64,091 →
Ord Tax $7,213.92 → LTCG Tax $0 (stacks below MFJ 0% threshold of $96,700) →
**Total Fed Tax $7,213.92**.

Any change you make must leave this tie-out intact.

## What's complete (DO NOT REBUILD)

1. **Bucket-pattern input table** on `Y2024` and `Y2025` — Excel
   Tables `tblY2024_Inputs` and `tblY2025_Inputs`, banded rows,
   header filters, auto-extend
2. **Cascading dropdowns** — Bucket (col B) → Input_Type (col C) via
   INDIRECT named ranges, Source_Type (col D), Treatment_Profile (col J)
3. **Treatment_Profile_Map auto-fill** — 18 profiles drive K/L/M/N
   columns (SE_Subject, NIIT_Class, QBI_Eligible, Char_Type) via
   `Get_TreatmentDefault` LAMBDA. Type a value over the formula to
   hardcode an override.
4. **Tax rollup right-side block** (W:AG rows 5-18) — 13 lines (1z..15)
   with cols: Line | Description | Baseline | Override | Effective |
   S1_Adj | S1_Total | S2_Adj | S2_Total | AsFiled | Variance.
   Aggregator lines (9, 11, 13, 15) cascade per scenario.
5. **Tax computation block** (W:AG rows 21-27) — Ord Tax | LTCG Tax |
   SE Tax | NIIT, TOTAL FED TAX at row 27, using 7 KISS LAMBDAs
6. **Planning Adjustments table on each year sheet** (W:AE rows 29-60)
   — preparer edits here; S1/S2 amounts feed back into rollup via
   SUMIFS by TargetLine + Status
7. **Quick Override Sandbox** on year sheets (A:D rows 47+) for
   what-if scratch that doesn't save
8. **`Master_Inputs` parent table** — 25 cols, InputID composite key,
   auto-populated on Save
9. **`Planning_Adjustments` parent table** — 14 cols, AdjustmentID,
   auto-populated on Save
10. **7 KISS sync macros** in `modKissSync`:
    - `PushInputsToMaster` (manual)
    - `PushPlanningToMaster` (manual)
    - `PushAllYearsToMaster` (auto on Ctrl+S, quiet mode)
    - `RefreshInputsFromMaster` (manual; overwrites year sheet!)
    - `CommitPlanningRow` (Approved → Committed, stamps date)
    - `ConvertPlanningToInput` (planning row → new input row)
    - `InstallKissLambdas` (one-time / re-install)
11. **7 KISS LAMBDAs** in Name Manager:
    - `Calc_OrdinaryTax(income, fs)`
    - `Calc_CapGainsTax(cap_gain, ord_inc, fs)` [simplified — see Known Limitations]
    - `Calc_1250Tax(unrecap_1250, ord_rate)`
    - `Calc_SE_Tax(se_inc, w2_wages, fs)`
    - `Calc_NIIT(magi, nii, fs)`
    - `Calc_QBI_Simple(qbi_inc, taxable_before_qbi, fs)`
    - `Get_TreatmentDefault(profile, field)`
12. **14 v3-original LAMBDAs** still installed alongside the KISS ones:
    `OrdTax_FN`, `CapGainsTax_FN`, `SETax_FN`, `NIIT_FN`, `QBI_FN`,
    `AddlMedicareTax_FN`, `FICA_EmployeeTax_FN`, `FICA_EmployerTax_FN`,
    `ExcessBusinessLossLimit_FN`, `NOLDeductionAllowed_FN`,
    `PassiveLossAllowed_FN`, `IncomeClassifier_FN`, `GetFITBrackets_FN`,
    `GetLTCGBrackets_FN`
13. **Bracket / threshold named ranges** restored after openpyxl
    dropped them: `FIT_BRACKETS_2025_*`, `LTCG_BRACKETS_2025_*`,
    `NIIT_THRESH_TABLE`, `SS_WAGE_BASE_2025`, `ADDL_MED_*`,
    `SE_BASE_MULT`, `SE_SS_RATE`, `SE_MED_RATE`, etc.
14. **`Treatment_Profile_Map`** — 18 profiles × (Profile | SE_Subject
    | NIIT_Class | QBI_Eligible | Char_Type | Default_Bucket | Notes)
15. **`PROJECTION_HISTORY`** — year-end rollover archive
    (Year | Line | Projected | Filed | Variance | Accuracy Grade) —
    also serves as the tie-out workpaper

## Sheet inventory (34 sheets)

| Sheet | Status / role |
| --- | --- |
| `CONTROL_PANEL` | Entry point. `C6=TaxYear`, `C7=FilingStatus`, macro shortcuts |
| `Y2023` | **Placeholder** — needs Phases 3-6 |
| `Y2024` | DONE — Cedillo data, $7,213.92 tie-out |
| `Y2025` | DONE — empty template + 4 seeded planning rows |
| `Y2026` | **Placeholder** — needs Phases 3-6 |
| `Master_Inputs` | Parent aggregate; Cedillo 2024 seeded |
| `Planning_Adjustments` | Parent aggregate; populated by auto-sync |
| `Treatment_Profile_Map` | 18-profile lookup driving auto-fill |
| `CONNECTIONS` | Extraction file paths per year; `PullExtractions` reads (stub) |
| `CLIENT_DASHBOARD` | **Needs repoint** — formulas reference old year-sheet positions |
| `DELIVERABLE` | **Needs repoint** — same issue |
| `QUESTIONNAIRE` | **Needs repoint** — 26 questions with conditional logic |
| `Tax_Brackets` | Reference data |
| `Tax_Limitations` | Reference data |
| `Tax_Line_Map` | Bucket+Input_Type → 1040 line + helper treatment |
| `Tax_Pecking_Order` | Calc sequence definition |
| `Carryovers` | Separate concern; leave alone |
| `Strategies` | **Strategy LIBRARY / catalog** of 20 standard plays. Preparers draw FROM this into year-sheet planning tables. Not per-year selections. |
| `Dropdown_Lists` | Closed sets; has a "REQUIRES MANUAL SETUP" block to clean up |
| `Field_Mapping` | Required / optional matrix per Input_Type+Source_Type |
| `PROJECTION_HISTORY` | Tie-out workpaper / rollover archive |
| `Tax_Summary` | **Broken — `#REF!` errors**. Rebuild as cross-year GROUPBY view. |
| `PBC_List` | Hardcoded; rebuild as GROUPBY-driven from Master_Inputs |
| `PBC_2026` | **Delete** — year scoping is a filter parameter, not a sheet |
| `Change_Log` | Audit trail |
| `Review_Summary` | Workflow tracking |
| `Input_Table_Mods` | Likely scratch — peek inside, may retire |
| `LAMBDA_Functions` | Documentation reference (real LAMBDAs are in Name Manager) |
| `VBA_Macros` | Documentation reference (real code in `vbaProject.bin`) |
| `User_Instructions` / `INSTRUCTIONS` / `SETUP_GUIDE` | Consolidate into one |
| `GLOSSARY`, `FRAMEWORK_REF` | Reference content |

## What's broken / incomplete

1. **`Tax_Summary` is full of `#REF!`** — references died
2. **7 external workbook links** on `CONNECTIONS`:
   `Activity_Detail`, `Deductions_and_Adjustments1`,
   `Form_1040_Summary`, `2025`, `Y2022`, `STRATEGY_INPUTS`,
   `TAX_CALCULATIONS`. Some LAMBDAs depend on them
   (`EntityCount`, `RentalCount`, `LookupDed`, `LookupLine`) and
   currently return errors.
3. **`PullExtractionsToAsFiled`** is a stub — needs wiring to the
   `CONNECTIONS` file paths
4. **Roll-forward macro** doesn't exist yet — needed: copy PY input
   rows (no amounts, Baseline only) to CY as a starting template
5. **`CLIENT_DASHBOARD` / `DELIVERABLE` / `QUESTIONNAIRE`** still
   reference old year-sheet cell positions (e.g. `'2025'!$AU$40` for
   AGI; AGI now lives at `Y2025!$AA$15`). Named ranges fixed for
   TaxYear/FilingStatus/AGI/TaxableIncome/TotalFederalTax in Phase 1
   but the dashboard sheets themselves likely still have hardcoded
   refs.
6. **`Year_Lookup_Summary`** not built — cross-year roll-up using
   `CHOOSE` (not `INDIRECT`) per resilience standards
7. **`Calc_CapGainsTax` simplified** — 2-bracket (0% / 15%) instead
   of 3-bracket. Slight under-tax for cap gains above the 15%
   threshold ($600,050 MFJ). Fixable via VBA install or manual Name
   Manager entry.
8. **`Y2023` and `Y2026`** are KISS-skeleton placeholders — no
   Tables, dropdowns, auto-fill, or planning section. Need Phases 3-6
   applied.
9. **Stale `Module1-4` VBA modules** — harmless v8.6 leftovers
10. **Jeff's dashboard workbook** has not been merged in (location TBD)
11. **Two LAMBDA libraries coexist** — 7 KISS + 14 v3 originals.
    Some v3 ones (`ExcessBusinessLossLimit_FN`, `PassiveLossAllowed_FN`,
    `NOLDeductionAllowed_FN`) look load-bearing without KISS
    equivalents; some are likely retire-able duplicates.

## Priority order

### Unblock first (no design needed)

1. **Triage the 7 external workbook links.** For each: locate, embed,
   or rewrite the dependent LAMBDAs to read from `Master_Inputs`.
   Report findings before deleting anything.
2. **Reconcile the two LAMBDA libraries.** Produce a keep/retire
   table for the 14 v3 LAMBDAs based on (a) whether referenced and
   (b) whether KISS covers the same math. Don't retire yet.

### Finish the KISS backlog

3. Fine-tune Y2025 input UX (column widths, label clarity, dropdowns)
4. Apply Phases 3-6 to `Y2023` and `Y2026` for layout consistency
   (use the existing `v3_kiss_merge_phase{3,4,5,6}.py` scripts as
   reference)
5. Build the Roll-forward macro in `modKissSync` — copy `Source =
   Baseline` rows from prior year into next year sheet, blank Amounts
6. Wire `PullExtractionsToAsFiled` to read `CONNECTIONS` paths and
   populate the `AsFiled` column on year sheets
7. Clean up stale `Module1-4` VBA modules

### Add the new view layer on top of Master_Inputs (additive, doesn't disturb KISS)

8. **Rebuild `Tax_Summary` as a `GROUPBY`-driven cross-year view**
   reading from `Master_Inputs`. Fixes the `#REF!` and creates the
   first piece of the new view layer.
9. **Build `Year_Lookup_Summary`** — CHOOSE-based, `GROUPBY`-driven
   cross-year roll-up (resilience standard says CHOOSE over INDIRECT
   for cross-year refs)
10. **Build a `Dashboard_Export` tab** — stable named-range block,
    `GROUPBY`-driven from `Master_Inputs`. Output is the dashboards'
    three-number headline (plus whatever else they need) at known
    cell addresses. This is the contract layer that future-proofs
    consumers against year-sheet layout changes.
11. **Rebuild `PBC_List`** as `GROUPBY`-driven from `Master_Inputs`,
    filtered to `Source = Baseline` and active year. Delete
    `PBC_2026` — year scoping becomes a parameter.
12. **Repoint `CLIENT_DASHBOARD` / `DELIVERABLE` / `QUESTIONNAIRE`**
    to read from `Dashboard_Export` named ranges instead of hardcoded
    year-sheet cells.
13. **Merge Jeff's dashboard workbook** into the file alongside (or
    replacing) `CLIENT_DASHBOARD` / `DELIVERABLE`, pointed at
    `Dashboard_Export`.

### Documentation

14. Consolidate `User_Instructions` / `INSTRUCTIONS` / `SETUP_GUIDE`
    into one instructions tab.

## Hard constraints

- **DO NOT modify the KISS calc engine** — the 7 KISS LAMBDAs, the
  same-sheet rollup on year sheets, the auto-sync, the
  `Treatment_Profile_Map` auto-fill, the bucket-pattern input table.
  These work and tie out.
- **DO NOT change directionality** — year sheets remain the primary
  work surface; master remains the downstream aggregate. New views
  read FROM master; they don't replace year sheets.
- **DO NOT touch `Y2024` data** — it's the regression case.
- **Save a timestamped backup** before any structural change.
- **No destructive operations** without confirmation — that includes
  retiring v3 LAMBDAs, deleting external links, deleting `PBC_2026`,
  removing stale modules, or repointing dashboards.
- **For each step, report before/after** — what changed, where, and
  what was verified. Always verify Cedillo Y2024 still ties to
  $7,213.92 after any change that could touch the calc path.

## Workflow

1. Read this entire prompt.
2. Confirm you can see the workbook and the build-script directory.
3. Propose an ordered plan covering items 1-14 with rough effort
   estimates and dependencies. Flag anything that needs my decision
   before you can start.
4. Wait for me to confirm before making any change.

## Open questions you may need to ask

- Where is Jeff's dashboard workbook?
- Are the 7 external link targets obsolete or are they real workbooks
  that need to be relocated and rewired?
- Is `Input_Table_Mods` still in active use or is it scratch?
- Are there v3 LAMBDAs in the keep/retire table I should investigate
  before retiring?

---

*Generated as a combined handoff merging the KISS Merge handoff
(2026-05-16) and the pivot-architecture reconciliation chat
(2026-05-18). Both source docs concluded with the same recommendation:
keep KISS, add view layer on top — don't rebuild the calc engine.*
