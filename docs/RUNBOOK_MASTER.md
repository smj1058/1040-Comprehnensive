# MASTER RUNBOOK — Master_Pivot_Framework end-to-end

**Use this as the single source of truth for completing the workbook.** It bundles: what's already been fixed, what remains to fix, the run order for remaining work, the per-step Excel prompts, and the save checkpoints.

---

## File map (deliverables in `G:\...\Pivot Strategy\` folder)

```
Master_Pivot_Framework_RealPivotv5.xlsx              ← your uploaded version (baseline)
Master_Pivot_Framework_v5_audit-fixes.xlsx           ← post Phase 0 fixes (delivered)
Master_Pivot_Framework_v5_post-phase-N_<date>.xlsx   ← after each phase you run
```

Each Excel prompt below assumes the WORKING file is open. Save checkpoints between phases.

---

## What's been fixed already (Phase 0 — applied via openpyxl, file delivered)

The following were applied programmatically and saved in `Master_Pivot_Framework_v5_audit-fixes.xlsx`. **PivotTables verified preserved through the round-trip.**

| Fix | Where | What |
| --- | --- | --- |
| **C1** | `Master_Inputs!E17` | `Adjustments` (plural) → `Adjustment` (singular) — fixes broken cascade for HSA strategy row |
| **C4** | `Y2025!C9` | STR-004 SEP-IRA TargetLine: `8` → `10` (correct: adjustments to income) |
| **C5** | `Y2025!C18` | STR-013 R&D Credit TargetLine: `13` → `20` (correct: Sch 3 line 6 / 1040 Line 20) |
| **C3** | `Tax_Ref!B9:G36` | 2023 + 2024 MFJ + Single brackets refreshed with IRS-published values. Previously held 2025 values for all years. |
| **I3** | `Master_Inputs!B5:B503` | Year column → dropdown `2023,2024,2025,2026,2027,2028` |
| **I3** | `Master_Inputs!M5:M503` | Helper_Treatment column → 23-value closed-set dropdown |
| **I3** | `Master_Inputs!Q5:Q503` | Primary_Line column → `=TaxLines` named range dropdown |
| **C2** | All 4 pivot tabs | Added `, tblMaster_Inputs[Activity_Type], "Baseline"` to **246 SUMIFS** across Pivot_Summary (40), Pivot_Medium (~66), Pivot_Detailed (~80), Pivot_Helpers (~60). Baseline columns now correctly exclude Strategy rows. |

**Verify after opening `Master_Pivot_Framework_v5_audit-fixes.xlsx`:**

- [ ] Master_Inputs R17 Bucket = "Adjustment" (singular)
- [ ] Y2025 R9 TargetLine = 10; R18 TargetLine = 20
- [ ] Tax_Ref R9 = `2023 / MFJ / 0 / 22000 / 10%`, R23 = `2024 / MFJ / 0 / 23200 / 10%`
- [ ] Master_Inputs B (Year), M (Helper_Treatment), Q (Primary_Line) all have dropdowns when you click them
- [ ] Pivot_Summary D5 formula ends with `, tblMaster_Inputs[Activity_Type], "Baseline"`
- [ ] All 4 Visual_Pivot tabs still have working real PivotTables
- [ ] Tax_Plan_Dashboard KPIs still resolve (no #REF!)

If anything fails verification, open the BASELINE backup and let me know.

---

## What still needs to be done (Phase 1 → Phase 4, run in Excel)

### Phase 1 — Strategy ID alignment with Jeff + multi-impact fan-out

**Issue:** STR-001..STR-015 (firm internal) don't map to Jeff's STD-xxx/ADV-xxx catalog. Strategies that fan out (Hire Children, Entity Restructuring, etc.) have CounterLine blank instead of populated. Most strategies are correctly single-impact (Cost Seg, Augusta, etc.); only true multi-line strategies need CounterLine.

**Excel prompt to paste into Claude-in-Excel:**

```
Open Master_Pivot_Framework_v5_audit-fixes.xlsx. On Y2025 sheet, the Strategies
table (A5:G20) uses StrategyID values STR-001 through STR-015. I want to:

1. Add a new column H labeled "Jeff_Ref_ID" between G (CounterLine) and the
   existing H (Line) so we can cross-reference Jeff's catalog. Shift current
   columns H onwards one to the right.

2. Populate Jeff_Ref_ID per the mapping below. Some have multiple Jeff
   references separated by " + ":

   STR-001 S-Corp Wage Optimization     → STD-008
   STR-002 HSA Family Max               → STD-001 (Retirement-adjacent)
   STR-003 Charitable Bunching (DAF)    → ADV-002
   STR-004 SEP-IRA / Solo 401(k)        → STD-001
   STR-005 Cost Seg Study               → STD-012
   STR-006 Roth Conversion              → ADV-004
   STR-007 Augusta Rule (§280A)         → STD-002
   STR-008 Accountable Plan             → STD-003
   STR-009 Hire Children                → STD-005
   STR-010 Entity Restructuring         → STD-007
   STR-011 Installment Sale / 1031      → STD-009 + ADV-006
   STR-012 Bonus Depreciation §168(k)   → STD-012
   STR-013 R&D Credit § 41              → (not in Jeff's catalog — leave blank)
   STR-014 SALT PTE Election            → (not in Jeff's catalog — leave blank)
   STR-015 Timing / Deferral            → STD-006

3. Populate CounterLine (G column) only for the truly multi-impact strategies.
   Leave blank for single-impact:

   STR-001  CounterLine = 8     (S-Corp wage opt: -1z + +8 K-1 offset) — should already be set
   STR-009  CounterLine = 1z    (Hire children: -biz expense + +child wages, though child wages
                                 are on a separate return — note in F column)
   STR-010  CounterLine = 1z    (Entity Restructure: -biz income + +W-2 wages on owner)

   For all others, leave CounterLine blank (Augusta = business deduction only,
   Cost Seg = single impact, etc.)

4. Repeat steps 1-3 on Y2023, Y2024, Y2026, Y2027, Y2028 — the strategy table
   layout is identical across year sheets.

Two-pass review: (1) tell me what you plan to change before doing it,
(2) execute, (3) confirm rollup formulas in column M still resolve and
the Net Strategy Impact summary on row 28 of each year sheet still computes.

When complete, save as Master_Pivot_Framework_v5_post-phase-1_<today>.xlsx
```

### Phase 2 — Add a Strategy column to each pivot tab (parallel to Baseline)

**Issue:** Pivots now correctly filter Baseline (Phase 0 fix), but there's no parallel Strategy column showing what strategies contribute per line. Without it, Tax_Plan_Dashboard can't compute Δ Savings cleanly across years.

**Excel prompt to paste into Claude-in-Excel:**

```
Open Master_Pivot_Framework_v5_post-phase-1_<date>.xlsx. On each of these
4 pivot tabs:
  - Pivot_Summary
  - Pivot_Medium
  - Pivot_Detailed
  - Pivot_Helpers

Currently each has columns:
  A: Line/Label  B: Description  C-H: 2023-2028 Baseline values

I want to add 6 more columns (I-N) for Strategy values:
  I-N: 2023-2028 Strategy values, formula identical to C-H but with
       , tblMaster_Inputs[Activity_Type], "Strategy"
       instead of
       , tblMaster_Inputs[Activity_Type], "Baseline"

For Pivot_Helpers, the column header is "Strategy" but the SUMIFS source
column may be Helper_Amount (not Baseline_Amount) depending on the row —
preserve the existing column choice, just add the Activity_Type filter
with "Strategy" value.

After adding: optionally add a 3rd block of columns O-T for Effective
(= Baseline + Strategy), each cell = corresponding C+I, D+J, etc.

Two-pass review and save as Master_Pivot_Framework_v5_post-phase-2_<date>.xlsx
```

### Phase 3 — Jeff workbook integration ("Pull from Master")

**Issue:** Jeff's `Accruity_Tax_Plan_Asset_v1_8_7_1.xlsx` Tab 1 Inputs is manually filled. Should auto-populate from Master_Pivot_Framework named ranges.

**Excel prompt to paste into Claude-in-Excel:**

```
Open BOTH:
  - Master_Pivot_Framework_v5_post-phase-2_<date>.xlsx
  - Accruity_Tax_Plan_Asset_v1_8_7_1.xlsx

In Master_Pivot_Framework, create a Clients sheet (color-code red/reference)
with columns:
  ClientID | Year | ClientName | FilingStatus | State |
  TaxpayerAge | SpouseAge | DependentCount | REPS_Qualified |
  Active_Business_Type | EntityNotes | Notes

Pre-populate with at least one row each for the existing client IDs (CED
2024, SAMPLE 2025).

In Jeff's workbook, add a VBA macro module modPullFromMaster containing
Sub PullFromMaster() that:
1. Reads Tab 1 C6 (ClientID) and C7 (Plan Year)
2. Opens Master_Pivot_Framework if not already open (path prompted first time,
   cached on a Settings cell)
3. Sets Master_Pivot_Framework Control_Panel C11 (Active_Client) to the
   ClientID and C8 (Active_Year) to the Year
4. Reads these named ranges from Master_Pivot_Framework:
   - BI_SE_SUBJECT, BI_ACTIVE_NONSE, BI_PASSIVE (for biz income build-up)
   - W2_OWNER, W2_THIRD_PARTY, W2_TOTAL (for wages)
   - Line_2b_TaxInt, Line_3b_OrdDiv, Line_7_CapGain (for investment + cap gains)
   - QUAL_DIV, TAX_EXEMPT (helper carve-outs)
   - AGI, TaxableIncome, MAGI, QBI_Income (for engine inputs)
5. Maps and writes them to Jeff's Tab 1 Inputs cells per the table below
6. Reads from new Clients sheet for state, ages, FS:
   - XLOOKUP(Active_Client&Active_Year, Clients[ClientID]&Clients[Year], Clients[State])
   - similar for ages, FS, dependents
7. Writes those to Jeff's Tab 1 Section 2 (Tax Profile)
8. Stamps Tab 1 C10 (Last Refresh) with NOW()
9. Highlights pulled cells with yellow fill (RGB 255,242,204)

Map (Jeff Tab 1 cell ← Master named range):
  C6  (Client Name)                ← XLOOKUP from Clients[ClientName]
  C7  (Plan Year)                  ← preserve user-set
  C14 (Filing Status)              ← XLOOKUP from Clients[FilingStatus]
  C15 (State of Residence)         ← XLOOKUP from Clients[State]
  C16 (Taxpayer Age)               ← XLOOKUP from Clients[TaxpayerAge]
  C17 (Spouse Age)                 ← XLOOKUP from Clients[SpouseAge]
  C18 (Dependent Children)         ← XLOOKUP from Clients[DependentCount]
  C19 (REPS Qualified)             ← XLOOKUP from Clients[REPS_Qualified]
  C21 (S-Corp Election in Place?)  ← =IF(SUMIFS(Master[Baseline_Amount],
                                          ..., Treatment_Profile, "K1_SCorp_Active",
                                          ..., Year, Active_Year, ..., ClientID,
                                          Active_Client) > 0, "Yes", "No")
  C26 (Active Business Net Income) ← BI_SE_SUBJECT + BI_ACTIVE_NONSE
  C27 (RE Portfolio Net Income)    ← BI_PASSIVE
  C28 (Spouse W-2 Income)          ← manual (no reliable Master source yet)
  C30 (Investment Income)          ← Line_2b_TaxInt + Line_3b_OrdDiv + Line_7_CapGain
  C32 (Charitable Contributions)   ← SUMIFS Master where Treatment_Profile = "Itm_Charity"

Skip Section 4+ for now — those are planner strategy targets, not pulled values.

After Sub: add a Form Control button to Tab 1 near C5 labeled "↻ Pull from Master".
Assign PullFromMaster to it.

Save Jeff's as Accruity_Tax_Plan_Asset_v1_8_7_2_with-pull.xlsm (note xlsm
since adding VBA).

Save Master_Pivot_Framework as v5_with-clients-sheet_<date>.xlsx
```

### Phase 4 — Reference / dev tabs polish

**Issue:** Audit observations I5 (Control_Panel mixes year-wide + workbook-wide), I6 (column order change), placeholder strategy rows STR-006/STR-008. Lower priority.

**Excel prompt** (when ready):

```
Open Master_Pivot_Framework_v5_with-clients-sheet_<date>.xlsx.

1. Document the current Master_Inputs column order in a new sheet
   `Column_Definitions` (or update existing). Columns to document (in order):
   InputID, Year, ClientID, ClientName, Bucket, Treatment_Profile,
   Source_Document, Activity_Type, Provenance, Payor, Baseline_Amount,
   Helper_Amount, Helper_Treatment, SE_Subject, NIIT_Class, QBI_Eligible,
   Primary_Line, Consider, Notes.

2. For STR-006 Roth Conversion and STR-008 Accountable Plan (currently
   placeholders with no Amount): either populate them with sample
   amounts for the SAMPLE client, OR move them to a separate
   Strategies_Catalog reference sheet listing all available strategies
   with no per-client commits.

3. (Optional) Restructure Control_Panel to read year-specific fields
   (Filing Status, ages, etc.) from the new Clients sheet via XLOOKUP
   keyed on Active_Client + Active_Year. Section 2 (Tax Profile) cells
   become formulas that auto-update when Active_Year changes.

Save as Master_Pivot_Framework_v5_post-phase-4_<date>.xlsx
```

---

## What's NOT yet addressed (future phases)

- **Master_Strategies catalog** (one-row-per-impact) — would replace the current Y2025_Strategies table model entirely. Bigger architectural shift; defer until current strategy model is producing right numbers.
- **Roll-forward macro** — year-end strategy carryforward + Converted_To_Baseline absorption into next-year Master_Inputs.
- **Snapshot macro** — PROJECTION_HISTORY captures at Extension / S1 / As-Filed milestones.
- **KISS LAMBDAs install** — register the 7 KISS LAMBDAs (Calc_OrdinaryTax, Calc_NIIT, etc.) in Name Manager. Prompt already written in `EXCEL_PROMPT_KISS_LAMBDAS.md`.
- **Extraction file importer** — VBA macro to read tax-software extraction files and append rows to Master_Inputs. Prompt already written in `EXCEL_PROMPT_EXTRACTION_IMPORT.md`.
- **Per-strategy marginal savings calc** — Jeff's "Strategy #1 saved $X / #2 saved $Y / Plan Synergy / PLAN TOTAL" display. Needs LAMBDAs to be installed and ability to re-run calc with/without each strategy.
- **State tax stack** — Phase 5 in earlier sequencing. 3 state-allocation columns on Master_Inputs (Home_State/State_2/State_3 with percentages) + State_Brackets reference + state LAMBDAs.

---

## Rollback procedure

```
1. Close working file WITHOUT saving
2. Reopen the most recent successful checkpoint (highest-numbered post-phase-N file)
3. Diagnose what failed (Claude-in-Excel should have reported)
4. Either retry the prompt OR report back with the error
```

---

## Naming convention recap

```
Master_Pivot_Framework_RealPivotv5.xlsx                              ← original upload
Master_Pivot_Framework_v5_audit-fixes.xlsx                           ← Phase 0 (delivered)
Master_Pivot_Framework_v5_post-phase-1_<YYYY-MM-DD>.xlsx             ← after Phase 1
Master_Pivot_Framework_v5_post-phase-2_<YYYY-MM-DD>.xlsx             ← after Phase 2
Master_Pivot_Framework_v5_with-clients-sheet_<YYYY-MM-DD>.xlsx       ← after Phase 3 (Master side)
Accruity_Tax_Plan_Asset_v1_8_7_2_with-pull.xlsm                      ← after Phase 3 (Jeff side)
Master_Pivot_Framework_v5_post-phase-4_<YYYY-MM-DD>.xlsx             ← after Phase 4
```

---

## Audit reference

Full Pass 1 audit details in `AUDIT_REPORT_v5.md`. The runbook above resolves issues C1, C2, C3, C4, C5, I3 via Phase 0 and addresses C6, I1, I4, I5, I6 in Phases 1-4. I2 (hardcoded year literals) and the architectural items remain for future sessions if they prove painful in practice.
