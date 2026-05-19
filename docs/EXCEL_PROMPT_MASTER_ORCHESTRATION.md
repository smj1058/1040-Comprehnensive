# Master Orchestration Prompt — Master_Pivot_Framework Rebuild Sequence

**For each step below: open the indicated prompt file, paste into Claude-in-Excel (with the workbook open), let it execute, save as the indicated checkpoint, then move to the next.**

The two-pass review rule applies at every step: Claude-in-Excel should (1) report what it plans to change, (2) execute, (3) verify the change took correctly. If anything fails or returns unexpected, STOP and ask.

---

## Pre-flight

1. Open `Master_Pivot_Framework_RealPivotv5.xlsx` in Excel
2. Confirm Claude-in-Excel can read the workbook
3. Save a baseline backup: `File → Save As → Master_Pivot_Framework_BASELINE_2026-05-19.xlsx`
4. Have these prompt files accessible in a text editor: `EXCEL_PROMPT_AUDIT_FIXES_v5.md`, `EXCEL_PROMPT_JEFF_INTEGRATION.md`, `EXCEL_PROMPT_PIVOT_FILTER_FIX.md`

---

## Phase 1 — Quick audit fixes (no-risk, single-cell + small batches)

**Prompt:** `EXCEL_PROMPT_AUDIT_FIXES_v5.md`

Covers:
- C1: `Master_Inputs!E17` Bucket "Adjustments" → "Adjustment"
- C4: `Y2025!C9` STR-004 TargetLine 8 → 10
- C5: `Y2025!C18` STR-013 TargetLine 13 → 20
- C3: Tax_Ref 2023 + 2024 bracket data refresh with correct IRS published values
- C6 (partial): Populate CounterLine column on Y2025 strategies that fan out
- I3: Add data validation dropdowns to Master_Inputs Year (B), Helper_Treatment (M), Primary_Line (Q)
- I4: Clean up STR-006, STR-008 placeholder rows (decide: delete or move to catalog)
- I6: Document Master_Inputs new column order in Column_Definitions sheet (create the sheet if missing)

**Save as:** `Master_Pivot_Framework_post-audit-fixes_2026-05-19.xlsx`

**Verify before continuing:**
- Re-run a few SUMIFS spot-checks to confirm nothing downstream broke
- Open Tax_Plan_Dashboard and confirm headline KPIs still resolve (no #REF!)
- Cedillo Y2024 numbers unchanged

---

## Phase 2 — Pivot Activity_Type filter + year-reference fix (architectural, big rewrite)

**Prompt:** `EXCEL_PROMPT_PIVOT_FILTER_FIX.md`

Covers:
- C2: Add `, tblMaster_Inputs[Activity_Type], "Baseline"` to all 246+ Baseline SUMIFS across Pivot_Summary, Pivot_Medium, Pivot_Detailed, Pivot_Helpers, Tax_Plan_Dashboard
- C2: Add a parallel "Strategy" set of columns to each pivot that filters `Activity_Type = "Strategy"` (so you can see both side-by-side)
- I2: Convert hardcoded year literals (`2024`, `2025`, etc.) to column-header-driven references (`D$3`, `E$3`, etc.) so adding 2029 doesn't require 246 edits

**Save as:** `Master_Pivot_Framework_post-pivot-rebuild_2026-05-19.xlsx`

**Verify before continuing:**
- Pivot_Summary 2024 Baseline for Wages Line 1z should now be $153,648 only (the Cedillo W-2 baseline), NOT $153,648 + any strategy
- Pivot Strategy column should show -$25,000 + $25,000 = $0 net for Wages+Biz combined (the STR-001 fan-out cancels out at the Total Income level)
- Tax_Plan_Dashboard Δ Savings should now compute meaningfully (Baseline − Eff w/ Strat)

---

## Phase 3 — Jeff workbook integration

**Prompt:** `EXCEL_PROMPT_JEFF_INTEGRATION.md`

Covers:
- Build a `Clients` sheet (per-client per-year metadata: FilingStatus, State, ages, etc.)
- Add the "Pull from Master" button macro to Jeff's `Accruity_Tax_Plan_Asset_v1_8_7_1.xlsx`
- Map every Jeff Tab 1 Input cell to its source in Master_Pivot_Framework named ranges
- Align strategy IDs between the two workbooks (STR-xxx → STD-xxx mapping if needed)

**Save as:** `Master_Pivot_Framework_with-Jeff_2026-05-19.xlsx` AND `Accruity_Tax_Plan_Asset_v1_8_7_2_with-pull-from-master.xlsx`

**Verify:**
- Open Jeff's workbook
- Set Tab 1 C6=SAMPLE, C7=2025
- Click "Pull from Master" button
- Confirm Tab 1 Section 3 fields auto-populate from Master_Pivot_Framework values
- Confirm Jeff's Tab 7 Executive Summary updates with the pulled data

---

## Phase 4 — Future (don't run yet, just sequence)

Deferred to later sessions:
- Master_Strategies catalog (one-row-per-impact) — replaces ad-hoc Y2025 strategies tables
- Roll-forward macro (year-end strategy carryforward + baseline absorption)
- Snapshot macro (PROJECTION_HISTORY captures at Extension / S1 / As-Filed)
- KISS LAMBDAs install (already documented separately in `EXCEL_PROMPT_KISS_LAMBDAS.md`)
- Real Excel PivotTable refresh-on-open setting
- Extraction file importer (already documented in `EXCEL_PROMPT_EXTRACTION_IMPORT.md`)
- Strategy ID alignment with Jeff (I1) — bundled in Jeff integration
- Per-strategy marginal savings calc (the "Strategy #1 saved $X" Jeff list)

---

## Rollback procedure if anything goes wrong

1. Close the working file WITHOUT saving
2. Reopen the most recent checkpoint backup
3. Diagnose what failed (Claude-in-Excel should have reported)
4. Either retry the prompt, or report back here for adjustment

## Naming convention summary

```
Master_Pivot_Framework_BASELINE_<date>.xlsx              ← before any changes
Master_Pivot_Framework_post-audit-fixes_<date>.xlsx      ← after Phase 1
Master_Pivot_Framework_post-pivot-rebuild_<date>.xlsx    ← after Phase 2
Master_Pivot_Framework_with-Jeff_<date>.xlsx             ← after Phase 3
Master_Pivot_Framework.xlsx                              ← working / current
```
