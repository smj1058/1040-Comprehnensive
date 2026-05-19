# Audit Report — Master_Pivot_Framework_RealPivotv5.xlsx

**Audit date:** 2026-05-19
**File:** `Master_Pivot_Framework_RealPivotv5.xlsx` (30 sheets, 89 named ranges)
**Audit type:** Pass 1 (issue identification). Pass 2 (verification of fixes) pending direction on which fixes to apply.

---

## 🔴 CRITICAL — workflow/calc-breaking

### C1. Bucket value inconsistency on Master_Inputs

- **Where:** `Master_Inputs!E17` (the SAM|2025|Strategy|HSA|01 row)
- **What:** Row has `Bucket = "Adjustments"` (plural). Closed-set on `Dropdown_Lists!A4:A11` is `"Adjustment"` (singular).
- **Impact:** The cascade formula `INDIRECT(SUBSTITUTE($E," ","")&"_Profiles")` evaluates to `INDIRECT("Adjustments_Profiles")` — that named range does not exist. Profile dropdown breaks. Row is also excluded from any pivot filtered to `Bucket="Adjustment"`.
- **Fix:** Change R17 Bucket from `"Adjustments"` to `"Adjustment"`. One-cell edit.

### C2. Pivots and Dashboard do not filter `Activity_Type`

- **Where:** Every SUMIFS on `Pivot_Summary`, `Pivot_Medium`, `Pivot_Detailed`, `Pivot_Helpers`, and the Baseline columns on `Tax_Plan_Dashboard`.
- **What:** `SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], <year>, tblMaster_Inputs[Primary_Line], <line>)` has no `Activity_Type` clause. Strategy rows (R15-R18 on Master_Inputs) get summed into the Baseline columns.
- **Impact:** Baseline totals are silently overstated/understated by the net strategy impact. `Tax_Plan_Dashboard.Δ Savings = Baseline − Eff w/ Strat` produces wrong numbers because Baseline already includes Strategy.
- **Fix:** Add `, tblMaster_Inputs[Activity_Type], "Baseline"` to every Baseline SUMIFS. Add a parallel Strategy column to each pivot that filters `Activity_Type = "Strategy"`. Done correctly on the Y2025 year-sheet rollup (J=Baseline + M=Strategies separately) — the pivots need the same pattern.

### C3. Tax_Ref bracket data appears wrong for 2023 and 2024

- **Where:** `Tax_Ref!B8:G35` (tblBrackets_FIT)
- **What:** 2023 MFJ first bracket is shown as `$0–$23,850 @ 10%`. Real 2023 MFJ first bracket: `$0–$22,000 @ 10%`. The $23,850 figure is the 2025 MFJ first bracket cap. Same pattern across the 2023 and 2024 rows.
- **Impact:** Any LAMBDA reading bracket data for 2023 or 2024 returns wrong tax. PY_Recon for prior years would show false variances.
- **Fix:** Update Tax_Ref rows for 2023 and 2024 with actual IRS published brackets:
  - 2023 MFJ: 22000 / 89450 / 190750 / 364200 / 462500 / 693750
  - 2024 MFJ: 23200 / 94300 / 201050 / 383900 / 487450 / 731200
  - Singles for both years similarly. (Standard deductions, NIIT thresholds, SS wage base, also need year-correct values.)

### C4. STR-004 SEP-IRA / Solo 401(k) has wrong TargetLine

- **Where:** `Y2025!C9` (Strategies table)
- **What:** TargetLine = `8`. Should be `10` (adjustments to income).
- **Impact:** SEP/401(k) contribution flows to Line 8 (Other income from Sch 1) instead of reducing AGI via Line 10. Misses the deduction.
- **Fix:** Change TargetLine to `10`.

### C5. STR-013 R&D Credit § 41 has wrong TargetLine

- **Where:** `Y2025!C18`
- **What:** TargetLine = `13` (QBI deduction). R&D Credit is a non-refundable credit on Schedule 3 line 6, flowing to 1040 Line 20.
- **Impact:** Credit applied to QBI line instead of as a credit.
- **Fix:** Change TargetLine to `20` (or whatever line code is used for Sch 3 credits) — and verify a credits-bucket line exists in the rollup.

### C6. Multi-impact strategies have CounterLine only on STR-001

- **Where:** `Y2025!G6:G20` (Strategies table CounterLine column)
- **What:** STR-001 Wage Optimization correctly specifies CounterLine = 8 (so the macro/formula creates the offset). STR-009 Hire Children, STR-010 Entity Restructuring, STR-007 Augusta Rule, and others that should fan out have blank CounterLine.
- **Impact:** Strategies fire only one leg of their impact. Same bug pattern we've been flagging.
- **Fix:** Populate CounterLine for each multi-impact strategy. Better long-term: move to the Master_Strategies catalog with one-row-per-impact (eliminates the CounterLine field — each impact is its own row). For now, populate CounterLine to unblock.

---

## 🟡 INCONSISTENCY — works but confusing

### I1. Strategy ID convention mismatch

- **Where:** `Y2025!A6:A20` uses `STR-001..STR-015`. Jeff's framework uses `STD-001..STD-014` + `ADV-001..ADV-006`.
- **Impact:** Cross-reference between this workbook and Jeff's catalog is manual. No clear mapping.
- **Fix:** Pick one convention. Either: (a) rename `STR-*` to align with Jeff's `STD-*` / `ADV-*`, or (b) add a `Jeff_Ref_ID` column on the Strategies table for cross-reference. (a) is cleaner if the strategies match 1:1; (b) is necessary if your STR list diverges from Jeff's intentionally.

### I2. 246 hardcoded year literals in pivot tabs

- **Where:** `Pivot_Summary` (48 cells), `Pivot_Medium` (78), `Pivot_Detailed` (60), `Pivot_Helpers` (60)
- **What:** Every cell has `, tblMaster_Inputs[Year], 2024` style hardcoded. Years 2023-2028 are baked into formulas.
- **Impact:** When 2029 brackets / pivot column needs adding, requires editing 246+ cells across 4 tabs.
- **Fix:** Two options:
  - (a) **Column-header-driven**: replace `, 2024` with `, <col-header-cell>` (e.g., `D$3` where the header row has the year). Pivot data fills the cell based on the column header value. Multi-year columns work via copy-right.
  - (b) **Leave it**: hardcoded years are only annoying when adding years. If you're committed to 2023-2028 forever, this is fine.
  Tax_Plan_Dashboard already uses `INDIRECT(Active_Year)` and is clean — pivots should match.

### I3. Master_Inputs missing data validations on Year, Helper_Treatment, Primary_Line

- **Where:** Master_Inputs columns B (Year), M (Helper_Treatment), Q (Primary_Line)
- **What:** No dropdown — free text. Bucket, Treatment_Profile, Source_Document, Activity_Type, Provenance, NIIT_Class, SE_Subject, QBI_Eligible all have proper dropdowns. The three above don't.
- **Impact:** Typos in closed-set columns break downstream lookups. e.g., a Primary_Line typed as `"1Z"` (uppercase Z) vs the expected `"1z"` (lowercase) wouldn't aggregate.
- **Fix:** Add list-validations: Year → `=TaxYears`, Helper_Treatment → `=Helper_Treatments`, Primary_Line → `=TaxLines`. Named ranges need to exist (probably do, given the framework includes them — verify on Dropdown_Lists).

### I4. STR-006 Roth Conversion and STR-008 Accountable Plan have placeholder rows

- **Where:** `Y2025!D11` (STR-006), `Y2025!D13` and `E13` (STR-008)
- **What:** Strategy Name and TargetLine populated, but Amount blank for STR-006 and STR-008; Status blank for STR-008. They look like real rows but are not committed.
- **Impact:** Confusing during planning. Reader doesn't know if these are "available but not used" or "should be filled in."
- **Fix:** Either fill them in with sample amounts/statuses for the SAMPLE client, or move them to a `Strategies_Catalog` reference sheet listing all available strategies (zero-amounted) and only put committed ones on the year sheet.

### I5. Control_Panel mixes year-specific and workbook-wide settings

- **Where:** `Control_Panel!B14:C21` — Filing Status, State, Taxpayer Age, Spouse Age, Dependent Children, REPS Qualified, Business is SSTB all on the same surface as `Plan Year` and `Active Client`.
- **What:** If client ages year-over-year, divorces (FS change), moves states, the Control_Panel values can't track that. They're snapshot values.
- **Impact:** Multi-year planning can't accurately reflect client-level changes year by year.
- **Fix:** Long-term: create a `Clients` sheet keyed by `(ClientID, Year)` with FS, ages, state, dependents. Control_Panel reads via `XLOOKUP(Active_Client & Active_Year, …)`. Short-term: leave it; document that these are "as of the active year" and update manually when year changes.

### I6. Master_Inputs column order changed (Helper_Treatment moved)

- **Where:** Column M now = Helper_Treatment (was at Q in my earlier framework).
- **What:** Order now: Helper_Amount (L), Helper_Treatment (M), SE_Subject (N), NIIT_Class (O), QBI_Eligible (P), Primary_Line (Q).
- **Impact:** Earlier prompts I wrote (EXCEL_PROMPT_ADD_QBI_COLUMNS.md, etc.) assume the old column positions. Need to harmonize.
- **Fix:** Two options: (a) Accept the new order as the canonical, update old prompts. (b) Move Helper_Treatment back to position Q for consistency. (a) is less work and the new order is defensible (helper amount → helper treatment naturally pair).

---

## 🟢 WHAT'S RIGHT — don't break these

- Real Excel PivotTables on all 4 Visual_Pivot tabs (Income, BusinessIncome, ByPayor, HelperCarveOuts)
- Tax_Plan_Dashboard uses GETPIVOTDATA with `INDIRECT($C$4)` to switch years cleanly
- All 6 year sheets (Y2023-Y2028) present, identical 136×16 structure
- Color-coded tabs (green inputs, gold visual, blue years, gray internal pivots, purple visual pivots, red reference/dev)
- 89 workbook-level named ranges, most using `INDIRECT("Y"&Active_Year&"!$X$Y")` for dynamic year-switching
- Helper named ranges (W2_OWNER, BI_SE_SUBJECT, MAGI, NII, OrdIncome, etc.) properly defined
- Reference / dev tabs in place: Tax_Ref, Glossary, Carryovers, Framework_Ref, Questionnaire, Connections, Projection_History, Change_Log, Setup_Guide
- AsFiled tab as parallel data store for filed amounts (tblAsFiled) — clean two-table model
- PY_Recon tab implements the Computed-vs-Filed variance comparison (Option B snapshot reconciliation)
- Pivot_GPD aggregates via GETPIVOTDATA from Visual_Pivot tabs, parameterized on Active_Year
- STR-001 Wage Optimization correctly fans out into 2 Master_Inputs rows (R15 -$25K Wages + R16 +$25K K-1) — the multi-line strategy bug is FIXED for this one strategy at least
- Year-sheet rollup has clean separation: J (Baseline from Master_Inputs) + M (Strategies from tblY2025_Strategies)

---

## 🟠 ARCHITECTURE OBSERVATIONS (not bugs, design decisions to lock in)

- **Two-source-of-truth pattern (intentional):** Master_Inputs for source-input rows, AsFiled for filed amounts. PY_Recon compares them. Cleaner than the snapshot-archive approach I proposed earlier.
- **Strategy data lives in two places:** Master_Inputs (with Activity_Type=Strategy) AND on year sheet (`tblY2025_Strategies`). Year-sheet rollup pulls from the year-sheet table, but the Master_Inputs Strategy rows ALSO exist (R15-R18). Pivots over Master_Inputs see them. So depending on which view (year sheet rollup vs cross-year pivot), strategies show differently. This needs reconciliation — pick one canonical source.
- **STR-006/STR-008 placeholder rows** suggest a hybrid model where the year-sheet strategy table is doubling as both "available strategies" catalog AND "committed strategies for this year." That's the dual-purpose tension we discussed — better to split into a catalog (Master_Strategies) and per-year commits.

---

## Recommended Pass 2 priority order (when you're ready)

1. **Quick critical fixes (no architectural change):**
   - C1 Bucket "Adjustments" → "Adjustment" (1 cell)
   - C4 STR-004 TargetLine 8 → 10 (1 cell)
   - C5 STR-013 TargetLine 13 → 20 (1 cell)
   - C3 Tax_Ref bracket data refresh for 2023, 2024 (~30 rows of corrections)

2. **Slightly bigger:**
   - C6 Populate CounterLine for multi-impact strategies on Y2025
   - I3 Add missing dropdown validations to Master_Inputs B, M, Q

3. **Architectural (needs decision):**
   - C2 Add `Activity_Type = "Baseline"` filter to all pivot Baseline SUMIFS + add parallel Strategy column. **Affects 246+ cells across 4 pivot tabs.** Choose to either (a) inline the filter or (b) restructure to read from a "Master_Inputs filtered to Baseline" view.
   - I2 Convert hardcoded year literals to column-header-driven references. Affects same 246+ cells.
   - I1 Strategy ID alignment with Jeff's naming convention.
   - I5 Control_Panel year-specific vs workbook-wide design — decide on Clients sheet pattern.

4. **Style/documentation:**
   - I4 Clean up placeholder strategy rows
   - I6 Document the new Master_Inputs column order in Column_Definitions
