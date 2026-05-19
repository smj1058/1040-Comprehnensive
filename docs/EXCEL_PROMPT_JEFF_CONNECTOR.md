# Prompt — Connect Master_Pivot_Framework to Jeff's Tax Plan Workbook

**Use with BOTH `Master_Pivot_Framework.xlsx` AND `Accruity_Tax_Plan_Asset_v1_8_7_1_Jeff.xlsx` open at the desktop.**

---

I have two workbooks I need to connect:

1. **`Master_Pivot_Framework.xlsx`** — the year-over-year compliance/historical record. Holds `tblMaster_Inputs` (all source-input rows year-tagged) plus pivots and named ranges (`AGI`, `TaxableIncome`, `W2_OWNER`, `BI_SE_SUBJECT`, `BI_PASSIVE`, `QBI_Income`, `CG_LT`, etc.).

2. **`Accruity_Tax_Plan_Asset_v1_8_7_1_Jeff.xlsx`** ("Jeff's workbook") — Jeff's forward-looking tax planning tool. **Tab 1 - Inputs** is a planner-facing data-entry surface that drives **Tab 2 - Engine** (computation modules) and **Tab 7 - Executive Summary** (deliverable).

**Goal**: when a planner opens Jeff's workbook for a client + plan year, Tab 1 Inputs should be pre-populated automatically from Master_Pivot_Framework for that client + year — instead of the planner typing them manually.

## Analysis of Jeff's Tab 1 - Inputs (what needs to populate)

Tab 1 has 6 sections of inputs. Below is the map of WHICH cell in Jeff's Tab 1 pulls FROM what in Master_Pivot_Framework. For cells without a Master source (planner judgment / strategy targets), leave them manual.

### Section 1 — Plan Status (mostly manual)

| Tab 1 cell | Field | Source |
| --- | --- | --- |
| C6 | Client Name | `Master_Inputs[ClientName]` for the active ClientID (use any row for that client; or store on a Settings tab) |
| C7 | Plan Year | Manual (or default to current year + 1) |
| C8 | Plan Maturity | Manual |
| C9 | Plan Reviewer | Manual |
| C10 | Last Refresh | `=TODAY()` |
| C11 | Engagement Leader | Manual |

### Section 2 — Tax Profile

| Tab 1 cell | Field | Source |
| --- | --- | --- |
| C14 | Filing Status | Master Settings (or CONTROL_PANEL!FilingStatus if it exists) |
| C15 | State of Residence | Master client metadata (add a `State` column to tblMaster_Inputs if not present, OR a separate Clients lookup sheet) |
| C16 | Taxpayer Age | Master client metadata (add `DateOfBirth` to Clients lookup, compute age) |
| C17 | Spouse Age | Same |
| C18 | Dependent Children | Manual or from Form_1040_Summary "Number of Dependents" if available |
| C19 | REPS Qualified | Manual (planner determines) |
| C20 | Entity Notes | Manual / free text |
| C21 | S-Corp Election in Place? | Derive: `=IF(SUMIFS(tblMaster_Inputs[Baseline_Amount], ..., Treatment_Profile, "K1_SCorp_Active") > 0, "Yes", "No")` |
| C22 | Business is SSTB? | From `QBI_Entities` sheet (if built) or manual |
| C23 | Active Business Type | Manual / planner judgment |

### Section 3 — Income Build-Up (THE BIG ONE — pulls heavily from Master)

| Tab 1 cell | Field | Master source / named range |
| --- | --- | --- |
| C26 | Active Business Net Income (pre-wage) | `=BI_SE_SUBJECT + BI_ACTIVE_NONSE` from Master_Pivot_Framework |
| C27 | RE Portfolio Net Income/(Loss) — PRE-cost-seg | `=BI_PASSIVE` (with sign adjustment) |
| C28 | Spouse W-2 Income | `=SUMIFS(tblMaster_Inputs[Baseline_Amount], ..., ClientName="<Spouse>", Treatment_Profile="W2_Employee")` — needs spouse identification |
| C29 | Other Active Income (not subject to FICA) | Manual or derived |
| C30 | Investment Income (Interest/Div/CG) | `=Line_2b_TaxInt + Line_3b_OrdDiv + Line_7_CapGain` |
| C31 | UBIA (RE basis for §199A) | From `QBI_Entities` sheet (if built) or manual |
| C32 | Charitable Contributions | `=SUMIFS(tblMaster_Inputs[Baseline_Amount], ..., Treatment_Profile, "Itm_Charity")` |
| C33 | RE Portfolio Annual Cash Flow | Manual (not derivable from tax data — needs separate cash flow tracking) |

### Section 4 — Core Strategy Drivers (mostly planner judgment)

These are strategy TARGETS, not historical values. Leave manual. Planner sets them based on tax plan recommendations:
- C37 Recommended Structure
- C38 S-Corp Effective Date
- C39 §199A Aggregation Election
- C40 §1.469-4 Grouping Election
- C43 Recommended Annual W-2 Wage
- C46 Plan Type
- C47 Employee Deferral
- C48 Employer Contribution
- C50 HSA Contribution
- C53 REPS Hours Documented
- C54 Cost Seg — Existing Properties
- C55 Cost Seg — New Acquisition
- C59 Accountable Plan Reimbursements
- C60 Augusta Rule Rent

### Section 5 onwards (mostly manual or planner judgment)

## What to build

Choose ONE of two integration patterns based on how Jeff wants to use this:

### Pattern A — Live link via external workbook reference

In Jeff's Tab 1, the source-able cells (Section 2 derive-ables and all of Section 3) become formulas referencing the open Master_Pivot_Framework.xlsx:

```
=[Master_Pivot_Framework.xlsx]Pivot_Helpers!BI_SE_SUBJECT
```

Requires both files open at the same time. If Master file is closed, cells show last cached values.

**Pros**: Always live; opens both files together → immediate refresh.
**Cons**: Workbook path becomes part of the formula; fragile if files move.

### Pattern B — Snapshot push via a button macro

Add a button on Jeff's Tab 1 Section 1 (e.g., near C5 header) labeled **"Pull from Master"**. Clicking it:

1. Prompts for ClientID (or reads it from C6 if already set) and Plan Year (C7).
2. Opens Master_Pivot_Framework.xlsx (or uses the active reference if open).
3. Reads the relevant named ranges and SUMIFS values **for that ClientID and Year** from Master.
4. Writes the values into the corresponding Tab 1 cells (C14, C15, C26, C27, C30, C32, etc.).
5. Stamps "Last pulled from Master: <datetime>" in C10.
6. Marks each pulled cell with a yellow fill so the planner sees what came from Master vs. what they typed.

**Pros**: Robust to file moves; planner sees a clean snapshot; manual overrides retain their formatting.
**Cons**: Doesn't auto-refresh if Master changes after the pull.

**My recommendation: Pattern B (snapshot push).** Jeff's workbook is a planning artifact for one client + year at a time; live linkage to a multi-year compliance file isn't necessary, and the snapshot makes the deliverable self-contained.

## Build steps (Pattern B)

1. **On Master_Pivot_Framework.xlsx, add a `Clients` sheet** if it doesn't exist:
   `ClientID | ClientName | State | TaxpayerName | TaxpayerDOB | SpouseName | SpouseDOB | DependentCount | Notes`

   One row per client. Used as the lookup for Jeff's Section 2 client-metadata fields.

2. **Add `Selected_ClientID` and `Selected_Year` named ranges on Master_Pivot_Framework** (Control cell on CONTROL_PANEL or just on Master_Inputs top-left).

3. **Make the existing helper named ranges parametric** so they respond to Selected_ClientID:
   - Update `W2_OWNER`, `BI_SE_SUBJECT`, `BI_PASSIVE`, etc. on `Pivot_Helpers` to include `, tblMaster_Inputs[ClientID], Selected_ClientID` in their SUMIFS, alongside the existing Year filter.

4. **In Jeff's workbook, add a `modPullFromMaster` VBA module** with `Sub PullFromMaster()`:
   - Path-find Master_Pivot_Framework.xlsx (prompt user to locate it first time, cache the path on a Settings cell).
   - Read the listed named ranges using `Workbooks(...).Names(...).RefersToRange.Value`.
   - Write into Tab 1 cells per the map above.
   - Color the pulled cells with a yellow fill (RGB(255, 242, 204)).
   - Update C10 "Last Refresh" with the current date/time.

5. **Add a button on Tab 1** near C5 labeled "↻ Pull from Master_Pivot_Framework". Assign the macro.

## Constraints

- **Do NOT change Master_Pivot_Framework column structure** — Jeff's pull depends on stable named ranges.
- **Do NOT overwrite a cell on Tab 1 if the planner has already typed in it** — check for yellow-fill = pulled; clear-fill or other-fill = manual override, leave alone.
- The Clients sheet should be the single source of client-level metadata (state, ages, dependents) so we don't duplicate it on every Master_Inputs row.

## Testing

1. Open both files.
2. On Master_Pivot_Framework, set Selected_ClientID="CEDILLO" (or whichever client) and Selected_Year=2024.
3. Confirm `W2_OWNER`, `BI_SE_SUBJECT`, etc. show the correct filtered values.
4. Open Jeff's workbook, click "Pull from Master" button.
5. Confirm Tab 1 Section 3 cells (C26, C27, C30, C32) populate with the right numbers.
6. Confirm Tab 1 Section 2 cells (C14 Filing Status, C15 State, C21 S-Corp election flag) populate.
7. Type something manually in C26 (override) and verify the yellow fill clears (or stays yellow with a different shade to mark "edited after pull").
8. Click pull button again — manual override should NOT be replaced.

## Future extension

Once this basic connector works, Jeff's **Tab 3 Deliverable** and **Tab 7 Executive Summary** outputs (the strategy savings figures, the take-home cash recommendations, the recommended W-2 wage, etc.) could be pushed BACK to Master_Pivot_Framework as `Activity_Type = "Strategy"` rows on `tblMaster_Inputs` for the plan year. That closes the loop: planning recommendations → committed strategy rows → next year's baseline. Build that as a separate macro later.
