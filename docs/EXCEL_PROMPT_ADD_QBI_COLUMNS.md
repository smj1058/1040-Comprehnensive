# Prompt — Add QBI Columns to Master_Inputs

**Use with `Master_Pivot_Framework.xlsx` open at the desktop.**

---

I need to add **five QBI-related columns to `tblMaster_Inputs`** on the `Master_Inputs` sheet. These hold per-business-entity §199A data on each row so the QBI LAMBDA can read them directly without a JOIN to another sheet.

## Current Master_Inputs column layout

Current order (19 columns):
```
A: InputID
B: Year
C: ClientID
D: ClientName
E: Bucket
F: Treatment_Profile
G: Source_Document
H: Activity_Type
I: Provenance
J: Payor
K: Baseline_Amount
L: Helper_Amount
M: SE_Subject
N: NIIT_Class
O: QBI_Eligible       ← new columns go right after this
P: Primary_Line
Q: Helper_Treatment
R: Consider
S: Notes
```

## What to do

Insert **five new columns between O (QBI_Eligible) and the current P (Primary_Line)**. After insertion, the existing P–S columns shift right to U–X.

New columns and their data:

| New position | Column header | Data type / dropdown | Default for blank rows | Notes |
| --- | --- | --- | --- | --- |
| P | `QBI_W2_Wages_Paid_by_Business` | Currency | blank | W-2 wages paid by THIS business entity (for the §199A 50%-of-W-2 limit or 25%+2.5%-of-UBIA limit) |
| Q | `QBI_UBIA` | Currency | blank | Unadjusted Basis Immediately after Acquisition of qualified property held by this business |
| R | `QBI_IsSSTB` | Yes / No dropdown | blank | Specified Service Trade or Business flag — phases out the deduction at high income |
| S | `QBI_Aggregation_Group` | Text (free or dropdown of group labels) | blank | §1.199A-4 aggregation election grouping label (e.g., "RE Portfolio", "Operating Cos"). Multiple rows with the same label aggregate together for the W-2/UBIA test. |
| T | `QBI_Loss_Carryover` | Currency | 0 or blank | QBI losses carried in from prior year (net against future QBI separately from regular NOL) |

## Constraints

- **Do NOT modify column order before O** — the named ranges and pivots reference columns by structured table reference (e.g., `tblMaster_Inputs[Baseline_Amount]`), so adding columns is fine but reordering existing ones breaks everything.
- **Existing structured-reference formulas continue to work** because they reference by column NAME, not position. After insertion, the SUMIFS formulas in Pivot_Summary/Medium/Detailed/Helpers should auto-update.
- **The new columns are typically BLANK** for non-Business-Income rows (Wages, Investment Income, Capital Gains, Itemized, Adjustments, Credits, Payments). Blank = N/A. Only populate them on rows where `Bucket = "Business Income"` AND `QBI_Eligible = "Yes"`.
- **Use Insert Cells, not Append** — the new columns must go between O and the current P, not at the right end of the table. The right-edge columns (Primary_Line, Helper_Treatment, Consider, Notes) MUST remain immediately to the right of the QBI cluster for visual cohesion.

## Add data validation

- Column R `QBI_IsSSTB`: dropdown `=Yes_No` (existing named range on Dropdown_Lists)
- Column S `QBI_Aggregation_Group`: free text for now (later, we may add a dropdown sourced from a `QBI_Aggregation_Groups` list — leave as free text for v1)

## Sample population

For the existing sample rows on Master_Inputs that are business-income rows, populate the QBI columns with reasonable sample data:

| InputID | QBI_W2_Wages_Paid_by_Business | QBI_UBIA | QBI_IsSSTB | QBI_Aggregation_Group |
| --- | --- | --- | --- | --- |
| CED\|2024\|BI\|01 (K1_PTP_Passive) | 0 | 0 | No | (blank) |
| SAM\|2025\|BI\|01 (K1_SCorp_Active) | 80000 | 250000 | No | OpCo |
| SAM\|2025\|Strategy\|CostSeg\|01 (SchE_Rental Strategy) | 0 | 2500000 | No | RE Portfolio |

Leave all other (non-business-income) rows blank for these columns.

## Add new named ranges that consume these columns

Add to the `Pivot_Helpers` sheet (in the existing helper section pattern), four new helper aggregations + named ranges:

| Named range | Formula | Purpose |
| --- | --- | --- |
| `QBI_W2_Wages_Total` | `=SUMIFS(tblMaster_Inputs[QBI_W2_Wages_Paid_by_Business], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[QBI_Eligible], "Yes")` | Total W-2 wages across all QBI-eligible entities, for the 50%-of-W-2 limit |
| `QBI_UBIA_Total` | `=SUMIFS(tblMaster_Inputs[QBI_UBIA], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[QBI_Eligible], "Yes")` | Total UBIA, for the 25%+2.5%-of-UBIA limit |
| `QBI_SSTB_Income` | `=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[QBI_IsSSTB], "Yes", tblMaster_Inputs[QBI_Eligible], "Yes")` | Income from SSTB businesses (phases out at threshold) |
| `QBI_NonSSTB_Income` | `=SUMIFS(tblMaster_Inputs[Baseline_Amount], tblMaster_Inputs[Year], 2025, tblMaster_Inputs[QBI_IsSSTB], "No", tblMaster_Inputs[QBI_Eligible], "Yes")` | Income from non-SSTB businesses (full deduction at any income) |

Each becomes a workbook-level named range pointing at its cell on Pivot_Helpers, just like the existing helpers (W2_OWNER, BI_SE_SUBJECT, etc.).

## Test after insertion

1. Open `Master_Inputs` → confirm five new columns at P-T with the right headers.
2. Confirm column R has the Yes/No data validation dropdown.
3. Open `Pivot_Helpers` → confirm new helper rows added and named ranges exist (`QBI_W2_Wages_Total`, `QBI_UBIA_Total`, `QBI_SSTB_Income`, `QBI_NonSSTB_Income`).
4. Open `Pivot_Summary`, `Pivot_Medium`, `Pivot_Detailed` → confirm the existing pivot numbers haven't changed (these don't depend on the new QBI columns).
5. Type a test value in column P for a business-income row and confirm `QBI_W2_Wages_Total` on Pivot_Helpers updates.
6. Confirm Y2025 sheet (active-year manipulation) is undisturbed.

## What this enables (downstream)

Once these columns exist, the QBI LAMBDA call becomes:

```
=QBI_FN(QBI_Income, QBI_W2_Wages_Total, QBI_UBIA_Total, TaxableIncome, FilingStatus, IsSSTB_AnyEntity)
```

(Or the LAMBDA can take more granular inputs once you decide whether to compute aggregation per-group or in total.)

The full QBI LAMBDA install lives in `EXCEL_PROMPT_KISS_LAMBDAS.md` — these columns are the missing inputs for that calc.
