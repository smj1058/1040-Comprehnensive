# Prompt — Import a Tax Return Extraction File into Master_Inputs

**Use with `Master_Pivot_Framework.xlsx` open at the desktop.**

---

I have a tax return extraction file with a known structure (sample: `MOCK_SAMPLE__tax_return_extraction.xlsx`). I need a VBA macro that **reads the extraction file and appends rows to `tblMaster_Inputs`** in `Master_Pivot_Framework.xlsx`, with each extraction line correctly mapped to my framework's schema. Don't replace existing rows — append, and skip duplicates.

## Extraction file structure (7 tabs)

| Tab | What it contains | Maps to |
| --- | --- | --- |
| `Form_1040_Summary` | Line-item rows: `Line_Item` (text like "Line 1z: Total Wages") and `Amount` | Most income/deduction/adjustment lines — one Master_Inputs row each |
| `Activity_Detail` | One row per business activity: `Property_Business_Name | Source | Type | Entity_Type | Passive_Active | Income | Depreciation | W2_Wages | K1_Cap_Account | K1_Owner_Distribution | etc.` | Per-entity Master_Inputs rows (Schedule C, Schedule E rentals, K-1s) |
| `Deductions_and_Adjustments` | Schedule A and Schedule 1 line-by-line: `Line_Number | Deduction_Category | Description | Amount` | Itemized and Adjustment Master_Inputs rows |
| `Form_Inventory` | List of forms/schedules in the return with counts | Reference only — not imported as Master rows |
| `PBC_Checklist` | Prior-year amounts + required docs | Reference (could populate a PBC sheet later, not for this import) |
| `Document_Log` | Document tracking | Reference only |
| `PBC_Summary` | Status rollup | Reference only |

## Master_Inputs target schema

Each row added must populate:
```
InputID | Year | ClientID | ClientName | Bucket | Treatment_Profile |
Source_Document | Activity_Type | Provenance | Payor |
Baseline_Amount | Helper_Amount |
SE_Subject | NIIT_Class | QBI_Eligible | Primary_Line | Helper_Treatment |
Consider | Notes
```

The first few columns come from extraction context; the SE/NIIT/QBI/Primary_Line/Helper_Treatment columns are *derived* via the `Treatment_Profile_Map` sheet (look up Treatment_Profile, copy those flags into the row).

## Mapping rules — Form_1040_Summary tab

For each row in Form_1040_Summary that has a numeric Amount > 0 (or ≠ 0):

| Source row text contains | Bucket | Treatment_Profile | Primary_Line | Helper_Treatment | Source_Document | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| "Line 1z: Total Wages" or "Line 1a: W-2 Wages" | Wages | W2_Employee or W2_SCorpOwner* | 1z | NONE or OWNER_PAY* | W-2 | * If client has S-Corp election (from Activity_Detail), tag as W2_SCorpOwner / OWNER_PAY |
| "Line 2a: Tax-Exempt Interest" | Investment Income | Int_Exempt | 2a | NONE | 1099-INT | This is INFORMATIONAL — also creates a Helper_Amount carve-out |
| "Line 2b: Taxable Interest" | Investment Income | Int_Taxable | 2b | TAX_EXEMPT | 1099-INT | If 2a exists, Helper_Amount = 2a value on this row |
| "Line 3a: Qualified Dividends" | (skip — captured as Helper) | | | | | Use as Helper_Amount on the 3b row |
| "Line 3b: Ordinary Dividends" | Investment Income | Div_Ordinary | 3b | QUAL_DIV | 1099-DIV | Helper_Amount = 3a value |
| "Line 7: Capital Gain or (Loss)" | Capital Gains | LTCG_Stock (default) | 7 | LTCG_SPLIT | 1099-B | Split into LT/ST/§1250 if Activity_Detail or 8949 breakouts available |
| "Line 8: Additional Income from Schedule 1" | (skip — handled via Activity_Detail) | | | | | |
| "Line 10: Adjustments to Income" | (skip — handled via Deductions_and_Adjustments Section 2) | | | | | |
| "Line 12: Standard / Itemized Deduction" | (skip — handled via Deductions_and_Adjustments Section 1, OR if standard, write one row Itm_StandardDeduction) | | | | | |
| "Line 13: QBI Deduction" | (skip for now — computed downstream by LAMBDA) | | | | | |

Skip aggregator lines: Line 9 (Total Income), Line 11 (AGI), Line 15 (Taxable Income), Line 16-38 (tax/credits/payments — for now). They're recomputed by the pivot.

## Mapping rules — Activity_Detail tab

For each row in Activity_Detail (one row per business entity):

| Source row | Bucket | Treatment_Profile | Primary_Line | Helper_Treatment | Payor | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Source="Schedule C" | Business Income | SchC_Active | 8 | SE_INCOME | Property_Business_Name | Income column → Baseline_Amount |
| Source="Schedule E Part I", Passive_Active="Passive" | Business Income | SchE_Rental | 8 | PASSIVE | Property_Business_Name | Income column → Baseline_Amount; Depreciation column → optional separate Strategy row if it represents Cost Seg |
| Source="Schedule E Part I", Passive_Active="Active" | Business Income | SchE_REPro | 8 | ACTIVE_RE | Property_Business_Name | Active (RE Pro election) |
| Source="Schedule K-1", Entity_Type="S", Passive_Active="Active" | Business Income | K1_SCorp_Active | 8 | K1_SPLIT | Property_Business_Name | Income column → Baseline_Amount; W2_Wages column → separate row with Treatment_Profile=W2_SCorpOwner |
| Source="Schedule K-1", Entity_Type="P", Passive_Active="Active" | Business Income | K1_PTP_Active | 8 | K1_SPLIT | Property_Business_Name | |
| Source="Schedule K-1", Entity_Type="P", Passive_Active="Passive" | Business Income | K1_PTP_Passive | 8 | K1_SPLIT | Property_Business_Name | |

For each Activity_Detail row that has a non-zero `W2_Wages` value AND `Entity_Type="S"` with `Passive_Active="Active"`: create a SECOND Master_Inputs row for the owner W-2 wages (Bucket=Wages, Treatment_Profile=W2_SCorpOwner, Primary_Line=1z, Source_Document=W-2, Helper_Treatment=OWNER_PAY, Baseline_Amount AND Helper_Amount both = W2_Wages).

## Mapping rules — Deductions_and_Adjustments tab

**Section 1 (Schedule A Itemized)** — for each line where Deduction_Category is one of {Medical & Dental, State & Local..., Mortgage..., Charitable...} AND Amount > 0:

| Deduction_Category contains | Treatment_Profile | Helper_Treatment |
| --- | --- | --- |
| "Medical" | Itm_Medical | MEDICAL |
| "State" or "Local" or "SALT" | Itm_SALT | SALT |
| "Mortgage" | Itm_Mortgage | MORTGAGE |
| "Charitable" | Itm_Charity | CHARITY |

Bucket=Itemized, Primary_Line=12, Source_Document=(Charity Receipts | 1098 Mortgage | Property Tax Receipt | Medical Receipts as appropriate).

**Section 2 (Schedule 1 Adjustments)** — for each line:

| Adjustment_Category contains | Treatment_Profile | Helper_Treatment | Source_Document |
| --- | --- | --- | --- |
| "HSA" | Adj_HSA | HSA | HSA Stmt |
| "IRA" | Adj_IRA | IRA | IRA Receipt |
| "Solo 401(k)" or "SEP" or "Retirement" | Adj_Retirement | RETIREMENT | Retirement Plan Stmt |
| "SE Health" or "Self-Employed Health" | Adj_SEHealth | SE_HEALTH | SE Health Premium |
| "Student Loan" | Adj_StudentLoan | STUDENT_LOAN | 1098-E |

Bucket=Adjustment, Primary_Line=10. Baseline_Amount = negative of the Amount (adjustments reduce income, so they're stored as negative in this schema).

## Field population on every row

- **InputID**: composite key `<ClientID>|<Year>|<Bucket short>|<Payor short or Treatment_Profile>|01`
- **Year**: from `Form_1040_Summary` "Line 10: Tax Year" or whatever year cell the extraction has
- **ClientID** / **ClientName**: from `Form_1040_Summary` "Line 4: Taxpayer Name" (use surname uppercase as ClientID)
- **Activity_Type**: always "Baseline" for imported rows
- **Provenance**: always "Extraction - Imported"
- **Helper_Amount**: 0 unless the mapping rule above specifies a value
- **SE_Subject / NIIT_Class / QBI_Eligible / Primary_Line / Helper_Treatment**: do not type these — let the VBA do an XLOOKUP against Treatment_Profile_Map after writing Treatment_Profile, and populate from there (or leave blank if Treatment_Profile_Map doesn't contain that profile)
- **Notes**: copy any extraction context (the raw "Line_Item" text, or Activity_Detail Type field) for traceability

## Duplicate handling

Before appending a row, check if `tblMaster_Inputs` already has a row with the same `InputID`. If yes, skip (or prompt for overwrite — preparer choice).

## Constraints

- **Append rows to `tblMaster_Inputs`** — do not modify column structure, do not insert columns.
- **Do not modify any other sheet** (Pivot tabs, Y2025, Treatment_Profile_Map, Dropdown_Lists).
- Use `ListObjects("tblMaster_Inputs").ListRows.Add` to extend the table cleanly.
- Show a summary at the end: "Imported X rows, skipped Y duplicates, flagged Z rows for review (missing Treatment_Profile_Map entry)."

## Testing

After importing the sample extraction file:
1. Confirm Master_Inputs has ~30-40 new rows for the sample taxpayer.
2. Confirm Pivot_Summary's 2024 column now shows non-zero values for Line 1z, 2b, 3b, 7, 8, 10, 12.
3. Confirm the helper amounts populate — Pivot_Helpers should show non-zero TAX_EXEMPT, QUAL_DIV, OWNER_PAY values for 2024.
4. Use the drill panel on Pivot_Detailed to verify the contributing rows are correctly populated and tagged.
