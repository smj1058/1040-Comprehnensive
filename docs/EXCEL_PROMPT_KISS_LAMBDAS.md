# Prompt — Install the 7 KISS LAMBDAs in Name Manager

**Use with `Master_Pivot_Framework.xlsx` open.**

---

I have a tax workbook `Master_Pivot_Framework.xlsx` with named ranges already wired (`TaxableIncome`, `AGI`, `MAGI`, `NII`, `OrdIncome`, `QBI_Income`, `W2_OWNER`, `W2_TOTAL`, `BI_SE_SUBJECT`, `BI_PASSIVE`, `CG_LT`, `CG_ST`, `QUAL_DIV`, `TAX_EXEMPT`, `SEC1250`, `FilingStatus`, etc.). I want to install **7 KISS LAMBDAs** in Name Manager so I can call them directly: `=Calc_OrdinaryTax(TaxableIncome, FilingStatus)`.

## What to do

Open `Formulas → Name Manager → New` and add each of the following as a new defined name. The "Refers to" formula is on the right.

The LAMBDA definitions reference some bracket and constant named ranges that I need to add first (or you can leave them as inline literals — I'll tell you which I prefer).

### Prerequisites — add these named ranges first if they don't exist

| Name | Refers to | Notes |
| --- | --- | --- |
| `FIT_BRACKETS_2025_MFJ` | (range with rows of `Rate / Low / High` for MFJ 2025 brackets — see Tax_Brackets sheet if it exists, otherwise create it) | Federal ordinary brackets |
| `FIT_BRACKETS_2025_S` | (Single brackets) | |
| `LTCG_BRACKETS_2025_MFJ` | (LTCG brackets MFJ) | |
| `LTCG_BRACKETS_2025_S` | (LTCG brackets Single) | |
| `SS_WAGE_BASE_2025` | 176100 | Social Security wage base |
| `SE_BASE_MULT` | 0.9235 | SE net earnings multiplier |
| `SE_SS_RATE` | 0.124 | SE SS rate |
| `SE_MED_RATE` | 0.029 | SE Medicare rate |
| `NIIT_RATE` | 0.038 | NIIT 3.8% |
| `NIIT_THRESH_MFJ` | 250000 | |
| `NIIT_THRESH_S` | 200000 | |
| `ADDL_MED_RATE` | 0.009 | Additional Medicare tax 0.9% |

### The 7 KISS LAMBDAs

```
Calc_OrdinaryTax = LAMBDA(income, fs,
    IF(income<=0, 0,
      LET(br, IF(fs="MFJ", FIT_BRACKETS_2025_MFJ, FIT_BRACKETS_2025_S),
          rates, INDEX(br, , 1),
          lows,  INDEX(br, , 2),
          highs, INDEX(br, , 3),
          inBracket, (income > lows) * (income > 0),
          taxable, IF(inBracket, MIN(income, highs) - lows, 0),
          SUMPRODUCT(taxable * rates))))

Calc_CapGainsTax = LAMBDA(cap_gain, ord_inc, fs,
    LET(thresh0, IF(fs="MFJ", 96700, 48350),
        thresh15, IF(fs="MFJ", 600050, 533400),
        stack_base, MAX(0, ord_inc),
        in_0_zone, MAX(0, MIN(cap_gain, thresh0 - stack_base)),
        remaining, cap_gain - in_0_zone,
        in_15_zone, MAX(0, MIN(remaining, thresh15 - MAX(stack_base, thresh0))),
        in_20_zone, MAX(0, remaining - in_15_zone),
        in_15_zone * 0.15 + in_20_zone * 0.20))

Calc_1250Tax = LAMBDA(unrecap_1250, ord_rate,
    MAX(0, MIN(unrecap_1250 * 0.25, unrecap_1250 * ord_rate)))

Calc_SE_Tax = LAMBDA(se_inc, w2_wages, fs,
    IF(se_inc<=0, 0,
      LET(net_se, se_inc * SE_BASE_MULT,
          ss_avail, MAX(0, SS_WAGE_BASE_2025 - MAX(0, w2_wages)),
          ss_taxable, MIN(net_se, ss_avail),
          ss_taxable * SE_SS_RATE + net_se * SE_MED_RATE)))

Calc_NIIT = LAMBDA(magi, nii, fs,
    IF(nii<=0, 0,
      LET(thresh, IF(fs="MFJ", NIIT_THRESH_MFJ, NIIT_THRESH_S),
          excess, MAX(0, magi - thresh),
          MIN(nii, excess) * NIIT_RATE)))

Calc_QBI_Simple = LAMBDA(qbi_inc, taxable_before_qbi, fs,
    MIN(MAX(qbi_inc * 0.2, 0), MAX(taxable_before_qbi * 0.2, 0)))

Get_TreatmentDefault = LAMBDA(profile, field,
    IFERROR(INDEX(Treatment_Profile_Map!$B$5:$F$38,
                  MATCH(profile, Treatment_Profile_Map!$A$5:$A$38, 0),
                  MATCH(field, Treatment_Profile_Map!$B$4:$F$4, 0)),
           ""))
```

## After installation — test

Create a test cell anywhere and verify each works:

```
=Calc_OrdinaryTax(TaxableIncome, FilingStatus)
=Calc_CapGainsTax(CG_LT, OrdIncome, FilingStatus)
=Calc_SE_Tax(BI_SE_SUBJECT, W2_TOTAL, FilingStatus)
=Calc_NIIT(NII, MAGI, FilingStatus)
=Calc_QBI_Simple(QBI_Income, TaxableIncome_BeforeQBI, FilingStatus)
```

Each should return a number. If any returns `#NAME?` or `#REF!`, check that the prerequisite bracket / constant named ranges resolve correctly.

## Constraint

These are LAMBDAs in Name Manager — not VBA. They work in any Excel 365 version. Do not delete or rename existing named ranges (`TaxableIncome`, `AGI`, `MAGI`, etc.) — they're consumed as arguments to these LAMBDAs.
