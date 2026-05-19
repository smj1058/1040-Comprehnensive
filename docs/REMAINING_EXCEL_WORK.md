# Remaining Excel-Side Work — phase3v24 onward

> Tracking doc for everything left to do/verify in Excel after the openpyxl phase wrapped.
> Companion file: `Tax_Calculator_Library.xlsx` (standalone LAMBDA library + reference data).
> Primary workbook: `Master_Pivot_Framework_v5_phase3v24_CC.xlsx`.

---

## 🔴 1. CRITICAL — Table recovery & #REF cleanup (do first)

The v22-v23 files had a broken `tblMaster_Inputs` (ref `A4:V18` but only 19 of 22 column metadata entries). v24 patched it. On first open verify:

- [ ] Open `phase3v24_CC.xlsx`. **No "We found a problem" recovery dialog should appear.**
- [ ] Click any cell in `Master_Inputs!A4:V18` → Table Tools should show **tblMaster_Inputs** with range A4:V18.
- [ ] Open Name Manager (Ctrl+F3) → confirm `tblMaster_Inputs` listed under Tables.
- [ ] Press **F9** to force recalc. Use Ctrl+F → search `#REF!` workbook-wide. Should be **zero hits**.
- [ ] If recovery dialog still appears, follow the **Excel-side rescue prompt** at the bottom of this doc.

---

## 🟡 2. LAMBDA install via Name Manager

The 7 LAMBDAs power per-strategy marginal savings + standalone tax computation. openpyxl-written LAMBDAs may show `#NAME?` until pasted by hand (Excel writes proper internal `_xlpm.` parameter markers).

For each LAMBDA below: Name Manager (Ctrl+F3) → New (or edit existing) → paste body → OK.

### 2.1 `STD_DED` — standard deduction lookup

```excel
=LAMBDA(yr, fs,
  INDEX(tblStdDed[Amount],
    MATCH(1, (tblStdDed[Year]=yr)*(tblStdDed[FilingStatus]=fs), 0)))
```

Test: `=STD_DED(2025,"MFJ")` → **31,500**

### 2.2 `TAX_ORD` — federal ordinary income tax

```excel
=LAMBDA(ti, yr, fs,
  LET(
    r, MATCH(1, (tblBrackets_FIT[Year]=yr) * (tblBrackets_FIT[FilingStatus]=fs)
              * (tblBrackets_FIT[Lower]<=ti) * (tblBrackets_FIT[Upper]>ti), 0),
    MAX(0, (ti - INDEX(tblBrackets_FIT[Lower], r))
            * INDEX(tblBrackets_FIT[Rate], r)
            + INDEX(tblBrackets_FIT[Add_To], r))))
```

Test: `=TAX_ORD(100000, 2025, "MFJ")` → **~11,828**

### 2.3 `TAX_CG` — capital gains 0/15/20

```excel
=LAMBDA(cg, ti, yr, fs,
  LET(
    r, MATCH(1, (tblBrackets_LTCG[Year]=yr) * (tblBrackets_LTCG[FilingStatus]=fs)
              * (tblBrackets_LTCG[Lower]<=ti) * (tblBrackets_LTCG[Upper]>ti), 0),
    cg * INDEX(tblBrackets_LTCG[Rate], r)))
```

Test: `=TAX_CG(50000, 200000, 2025, "MFJ")` → **7,500**

### 2.4 `TAX_NIIT` — 3.8% NIIT above threshold

```excel
=LAMBDA(nii, magi, fs, yr,
  LET(
    th, INDEX(tblThresholds[Value],
          MATCH(1, (tblThresholds[Item]="NIIT_Threshold") * (tblThresholds[Year]=yr)
                  * (tblThresholds[FilingStatus]=fs), 0)),
    MAX(0, MIN(nii, magi - th)) * 0.038))
```

Test: `=TAX_NIIT(50000, 300000, "MFJ", 2025)` → **1,900**

### 2.5 `TAX_SE` — self-employment tax

```excel
=LAMBDA(se, yr,
  LET(
    b, se * 0.9235,
    c, INDEX(tblThresholds[Value],
         MATCH(1, (tblThresholds[Item]="SS_Wage_Base") * (tblThresholds[Year]=yr), 0)),
    MIN(b, c) * 0.124 + b * 0.029))
```

Test: `=TAX_SE(100000, 2025)` → **~14,130**

### 2.6 `TAX_STATE` — state top marginal rate

```excel
=LAMBDA(ti, st,
  ti * XLOOKUP(st, tblStateRates[State], tblStateRates[Top_Marginal_Rate], 0))
```

Test: `=TAX_STATE(200000, "UT")` → **9,300**

### 2.7 `fn_StrategyMarginal` — per-strategy marginal savings

```excel
=LAMBDA(tl, amt, cl, yr, fs, ti,
  LET(
    pd, -amt,
    pf, IF(OR(tl="—", tl=""), 0,
        IF(tl="20", pd,
        IF(tl="7", TAX_CG(pd, ti+pd, yr, fs),
          TAX_ORD(ti+pd, yr, fs) - TAX_ORD(ti, yr, fs)))),
    pfica, IF(tl="1z", pd*0.153, 0),
    hc, AND(cl<>"", cl<>0),
    cd, IF(hc, amt, 0),
    cf, IF(NOT(hc), 0,
        IF(cl="20", cd,
        IF(cl="7", TAX_CG(cd, ti+cd, yr, fs),
          TAX_ORD(ti+cd, yr, fs) - TAX_ORD(ti, yr, fs)))),
    cfica, IF(AND(hc, cl="1z"), cd*0.153, 0),
    pf + pfica + cf + cfica))
```

Test: `=fn_StrategyMarginal("1z", -25000, 8, 2025, "MFJ", 200000)` → **~3,825**

- [ ] All 7 tests return the expected value.

---

## 🟢 3. Wire LAMBDAs into Box 2 marginal savings

Once the 7 LAMBDAs work, replace the placeholder `× 0.32` formula:

### 3.1 Year-sheet At-a-Glance Box 2 (Y2023 through Y2028)

Cell range: `K144:K158` on each year sheet (15 strategy rows × 6 sheets = 90 cells).

Old: `=IF(OR(E{n}="Committed",E{n}="Implemented"), -D{n}*0.32, 0)`
New: `=IF(OR(E{n}="Committed",E{n}="Implemented"), fn_StrategyMarginal(C{n}, D{n}, G{n}, {year_literal}, Filing_Status, $K$94), 0)`

Replace `{n}` with row 6..20 to match `K144..K158`. Replace `{year_literal}` with 2023/2024/.../2028 per sheet.

- [ ] Y2023 K144:K158 updated
- [ ] Y2024 K144:K158 updated
- [ ] Y2025 K144:K158 updated
- [ ] Y2026 K144:K158 updated
- [ ] Y2027 K144:K158 updated
- [ ] Y2028 K144:K158 updated

### 3.2 Tax_Plan_Dashboard Box 2 (K8:K22)

Old: `=IF(OR(I{r}="Committed",I{r}="Implemented"), -J{r}*0.32, 0)`
New:

```excel
=IF(OR(I{r}="Committed",I{r}="Implemented"),
   fn_StrategyMarginal(
     INDIRECT("Y"&$C$4&"!C"&({r}-2)),
     J{r},
     INDIRECT("Y"&$C$4&"!G"&({r}-2)),
     $C$4, Filing_Status,
     INDIRECT("Y"&$C$4&"!$K$94")),
   0)
```

- [ ] K8:K22 updated.

### 3.3 Deliverable F50:F64

Same INDIRECT pattern but using `Active_Year` named range:

```excel
=IF(OR(INDIRECT("Y"&Active_Year&"!E{strat}")="Committed",
       INDIRECT("Y"&Active_Year&"!E{strat}")="Implemented"),
   fn_StrategyMarginal(
     INDIRECT("Y"&Active_Year&"!C{strat}"),
     INDIRECT("Y"&Active_Year&"!D{strat}"),
     INDIRECT("Y"&Active_Year&"!G{strat}"),
     Active_Year, Filing_Status,
     INDIRECT("Y"&Active_Year&"!$K$94")),
   0)
```

Where `{strat}` = `f_row - 44` (so F50 → row 6, F64 → row 20).

- [ ] F50:F64 updated.

---

## 🔵 4. Verification checks (no work — just confirm)

- [ ] Y2025 J119 reads `=MAX(0,J41)*0.5` or `*Rate_QBI_W2_50pct`, NOT `*0.2` (QBI bug fix)
- [ ] Y2025 row 11 (STR-006 Roth Conversion): C11 = "4b" (not "1z")
- [ ] Y2025 row 19 (STR-014 SALT PTE): C19 = 8 (not 12)
- [ ] Control_Panel HOUSEHOLD DETAILS section at B22:D33 has 11 fields
- [ ] Master_Strategies catalog has 19 impact rows for 15 STR-IDs
- [ ] Year-sheet column W (Catalog Bucket) on each year sheet shows Bucket from catalog
- [ ] STR-001 marginal savings on Y2025 K144 = **~$3,825** after LAMBDAs are wired (the FICA on the $25K wage shift)

---

## 🟣 5. Bigger Excel-side work (separate sessions)

### 5.1 Jeff PullFromMaster integration

Wire `Accruity_Tax_Plan_Asset_v1_8_7_1.xlsx` Tab 1 inputs to pull from this workbook's named ranges:

- `Active_Year`, `Filing_Status`, `Active_Client`
- `Taxpayer_Name`, `Spouse_Name`
- `Dep_CTC_Count`, `Dep_ODC_Count`
- `Taxpayer_65Plus`, `Spouse_65Plus`, `Taxpayer_Blind`, `Spouse_Blind`
- `SE_Health_Ins_Eligible`, `Itemize_Override`, `PY_Total_Tax`

STR-* → STD-* mapping lives in `Framework_Ref` columns F-H.

Add a button macro "Pull from Master" that:
1. Confirms both workbooks open
2. Force-recalculates
3. Reports any missing named range

- [ ] Jeff Tab 1 inputs cross-linked
- [ ] "Pull from Master" button macro built
- [ ] Tested with Jeff Tab 7 Executive Summary

### 5.2 VBA: `mod_RollForward`

Year-end carry-forward:
1. Find committed strategies in Y[active_year]
2. Copy them to Y[active_year+1]
3. Move implemented strategies' net impact into Master_Inputs baseline rows for next year
4. Set carried strategies to status "Proposed" in new year

- [ ] Module created and tested

### 5.3 VBA: `mod_Snapshot`

Capture year state at workflow milestones:
1. User picks milestone (Extension / S1 / As-Filed)
2. Copy Y[active_year] calc engine rows 80-135 into `Projection_History` with milestone label + date stamp
3. Compute variance vs prior snapshot

- [ ] Module created and tested

### 5.4 VBA: `mod_ExtractionImport`

Parse tax-software export file:
1. File path lives in `Connections` sheet (define schema first — sheet exists but empty)
2. Map extraction columns to `Master_Inputs` schema
3. Append parsed rows to `tblMaster_Inputs` with appropriate `Activity_Type` / `Provenance`

- [ ] Schema designed in Connections
- [ ] Module created and tested

### 5.5 PivotTable refresh settings

For each `Visual_Pivot_*` sheet:
1. Right-click PivotTable → PivotTable Options → Data tab
2. Check "Refresh data when opening file"
3. (Optional) "Enable show details"

- [ ] Visual_Pivot_Income
- [ ] Visual_Pivot_BusinessIncome
- [ ] Visual_Pivot_ByPayor
- [ ] Visual_Pivot_HelperCarveOuts

---

## ⚪ 6. Optional / deferred

- [ ] Audit_Report sheet rebuild (was stripped in v22 recovery)
- [ ] LAMBDA_Test verification harness sheet rebuild
- [ ] Path B full year-sheet refactor (formula-driven from catalog) — risky, 96 SUMIFS depend on existing structure
- [ ] 1,362 string-literal "warnings" from old audit (mostly noise — status icons like ✓ OK, sheet-ref fragments)
- [ ] Rate-naming completeness (most calc-engine literals named; some 2.5% UBIA / 6.2% SS variants could be further consolidated)

---

## 🛠 Excel-side rescue prompt — if v24 still shows recovery dialog

> Paste into Claude-in-Excel.

```
You are recovering Master_Pivot_Framework_v5_phase3v24_CC.xlsx after openpyxl
corrupted tblMaster_Inputs. Symptoms: #REF errors everywhere; Excel "recover"
dialog appeared and silently dropped the table.

STEP 1 — DIAGNOSE
Open Name Manager (Ctrl+F3). Confirm tblMaster_Inputs exists. If missing, go
to Step 2A. If present but column count != 22, go to Step 2B.

STEP 2A — TABLE MISSING (recreate from data)
1. Go to Master_Inputs. Data lives at A4:V18 (headers row 4, data 5-18).
2. Select A4:V18 → Insert → Table → "My table has headers" → OK.
3. Table Design → Name = "tblMaster_Inputs".
4. Confirm 22 columns: InputID, Year, ClientID, ClientName, Bucket,
   Treatment_Profile, Source_Document, Activity_Type, Provenance, Payor,
   Baseline_Amount, Helper_Amount, Helper_Treatment, SE_Subject, NIIT_Class,
   QBI_Eligible, Primary_Line, Consider, Notes, Primary_State, State_Mix,
   PTET_Routed.

STEP 2B — TABLE BROKEN
1. Click table → Design → Resize Table → A4:V18.
2. If column count wrong, Convert to Range → redo Step 2A.

STEP 3 — REPAIR #REFs
1. Press F9 (force recalc).
2. Ctrl+F → search "#REF!" workbook-wide. Hunt remaining cell by cell.

STEP 4 — SAVE AS
Save as "Master_Pivot_Framework_v5_phase3v25_SJ.xlsx" (_SJ suffix per
naming convention since you fixed it in Excel directly).

REPORT BACK: which tables were missing, how many #REFs remained, and
what STR-001 marginal savings shows on Y2025 At-a-Glance Box 2 after fix.
```

---

## Naming convention

- `_CC` suffix = Claude (openpyxl-built) file
- `_SJ` suffix = user-built in Excel
- Phase number `v{N}` tracks build iteration
- Latest framework version: v5
- Companion file: `Tax_Calculator_Library.xlsx` (no version suffix — single-purpose)
