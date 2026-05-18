# Tax Workbook — Architecture Reconciliation Notes

**Status:** Revised 2026-05-18 after receiving the KISS Merge handoff
doc (`HANDOFF_v3_KISS.md`, dated 2026-05-16). The architecture
exploration in the earlier version of this file was largely
re-inventing what's *already in the workbook* under the name "KISS."
This version reconciles the two and recommends a much smaller scope
of additional work.

---

## Headline

You have already built the architecture. Phases 1–7 of the KISS merge
implemented:

- The 5-tier scenario model (`Baseline | Override | S1 | S2 | AsFiled`)
- `Treatment_Profile_Map` driving SE/NIIT/QBI/Char_Type auto-fill
- Year-sheet bucket-pattern input table with cascading dropdowns
- Per-year planning adjustments table (`AdjID | Status | TargetLine |
  S1_Amount | S2_Amount | ...`) with status workflow
  (Proposed → Approved → Committed → Converted_To_Input)
- 7 KISS LAMBDAs for the tax calc (`Calc_OrdinaryTax`,
  `Calc_CapGainsTax`, `Calc_1250Tax`, `Calc_SE_Tax`, `Calc_NIIT`,
  `Calc_QBI_Simple`, `Get_TreatmentDefault`) plus 14 v3 originals
- Auto-sync from year sheet → `Master_Inputs` / `Planning_Adjustments`
  on every Ctrl+S (`Workbook_BeforeSave` → `PushAllYearsToMaster`)
- Cedillo Y2024 ties out to $7,213.92 federal tax

The KISS architecture is **the inverse** of the pivot-driven model the
earlier notes were exploring:

| Concern | Earlier notes (pivot-first) | KISS (already built) |
| --- | --- | --- |
| Source of truth | `Master_Inputs` | Year sheet (`Y####`) |
| Calc engine reads from | Pivots over master | Same-sheet ranges on active year |
| Master role | Primary store | Downstream aggregate |
| Year sheet role | Derived view | Primary work surface |
| Sync direction | Manual or push from sheets | Auto on Save (year → master) |

Both are defensible. KISS is what's built and what ties out. Don't
rebuild the calc layer just to change the directionality.

---

## What KISS does well

- **Immediate feedback during data entry** — change a number, calc
  updates same-tab, no master refresh round-trip
- **One year's calc is self-contained** — easy to audit, easy to
  diff against an actual return
- **Auto-sync prevents drift** — the "two sources of truth" problem
  that motivated the pivot-first design is solved by Ctrl+S
- **Per-year planning scenarios are local** — S1/S2 SUMIFS over the
  year's planning table happens on the same sheet; no cross-sheet
  fragility

## What KISS doesn't natively cover (and the pivot layer should)

These are the gaps the upcoming work should fill — without disturbing
KISS daily flow:

- **Cross-year reporting** — "wages by year 2022–2026 across all
  clients/this client" doesn't have a home today; year sheets are
  single-year, master is unaggregated rows
- **Auto-generated PBC inventory** — `PBC_List` is currently
  hardcoded; should derive from `Master_Inputs` rows where
  `Source = Baseline` for the active year
- **Leadership / Jeff dashboard feed** — needs a stable export block
  reading from master, not from year-sheet cell addresses
- **Year_Lookup_Summary** (already in the KISS backlog) —
  CHOOSE-based cross-year roll-up per the resilience standards

The pattern for all four: **a new `GROUPBY` view tab reading from
`Master_Inputs` after auto-sync has populated it.** This is additive,
not replacement.

---

## Tab-by-tab verdict (final, reconciled)

| Tab | Verdict | Notes |
| --- | --- | --- |
| `CONTROL_PANEL` | KEEP | TaxYear, FilingStatus, macro shortcuts — already wired |
| `Y2024` | KEEP — daily work surface | Cedillo ties out; don't touch |
| `Y2025` | KEEP — daily work surface | Active year template; don't touch |
| `Y2023` | UPGRADE — apply Phases 3-6 | Already in KISS backlog |
| `Y2026` | UPGRADE — apply Phases 3-6 | Already in KISS backlog |
| `Master_Inputs` | KEEP as aggregate; ADD pivot views on top | Don't change directionality |
| `Planning_Adjustments` | KEEP | Auto-synced; status workflow works |
| `Treatment_Profile_Map` | KEEP — this is gold | 18 profiles drive auto-fill; massive freetype-risk reducer |
| `Tax_Brackets` | KEEP | Bracket/limit reference; LAMBDAs already consume |
| `Tax_Limitations` | KEEP | Same role for limits/thresholds |
| `Tax_Line_Map` | KEEP | Bucket+Input_Type → 1040 line; drives helper treatment |
| `Tax_Pecking_Order` | KEEP | Calc sequence reference |
| `Carryovers` | KEEP | Separate concern from main flow |
| `Strategies` | KEEP — clarify it's a strategy LIBRARY/CATALOG | 20 standard plays; preparers draw FROM this into Planning_Adjustments |
| `Dropdown_Lists` | KEEP — clean up the "manual setup needed" block | Closed-set reference; mostly wired |
| `Field_Mapping` | KEEP | Required/optional matrix |
| `PROJECTION_HISTORY` | KEEP — this is your tie-out workpaper | Year/Line/Projected/Filed/Variance/Accuracy Grade |
| `Tax_Summary` | REBUILD as GROUPBY-driven cross-year view | Currently `#REF!`'d out; perfect target for the new view layer |
| `PBC_List` | REBUILD as GROUPBY-driven from Master_Inputs | Auto-generate from Baseline rows + Source_Document |
| `PBC_2026` | DELETE — year scoping is a filter, not a sheet per year | Superseded by the rebuilt PBC_List |
| `CLIENT_DASHBOARD` | REPOINT (KISS backlog #2/#4) — point at new export block | Currently hardcoded year-sheet refs |
| `DELIVERABLE` | REPOINT — same as above | |
| `QUESTIONNAIRE` | REPOINT — same as above | |
| `CONNECTIONS` | KEEP — triage the 7 external workbook links | Some LAMBDAs (`EntityCount`, `RentalCount`, `LookupDed`, `LookupLine`) depend on these and return errors |
| `Change_Log` | KEEP | Audit trail |
| `Review_Summary` | KEEP | Workflow tracking |
| `Input_Table_Mods` | EVALUATE — likely transient scratch tab | Peek inside; may retire |
| `LAMBDA_Functions` | KEEP — documentation reference | Real LAMBDAs live in Name Manager |
| `VBA_Macros` | KEEP — documentation reference | Real code in vbaProject.bin |
| `SETUP_GUIDE` / `INSTRUCTIONS` / `User_Instructions` | CONSOLIDATE into one | Three overlapping doc tabs |
| `GLOSSARY` | KEEP | New-user reference |
| `FRAMEWORK_REF` | KEEP | Reference content |
| `Stale v8.6 Module1-4` (VBA) | DELETE | Handoff confirms harmless leftovers |

---

## Revised game plan

In priority order. Items 1–8 are the existing KISS backlog; items 9–12
are the additive pivot-view layer.

1. Fine-tune Y2025 input UX (KISS backlog #1)
2. Merge Jeff's dashboard workbook into CLIENT_DASHBOARD/DELIVERABLE
3. Apply Phases 3–6 to Y2023 and Y2026
4. Repoint CLIENT_DASHBOARD / DELIVERABLE / QUESTIONNAIRE — and when
   you do, point them at the NEW Master_Inputs-driven export block
   (item 11 below), not at year-sheet cells
5. Build Roll-forward macro — copy PY input rows (no amounts) into
   next year as starting template
6. Wire up PullExtractions for KISS layout — read CONNECTIONS file
   paths, populate AsFiled
7. Build Year_Lookup_Summary — CHOOSE-based, GROUPBY-driven
8. Clean up stale Module1–4 VBA
9. **NEW: Triage the 7 external workbook links** on `CONNECTIONS` —
   resolve, embed, or rewrite the dependent LAMBDAs. Until done you
   have silent ghost errors in `EntityCount`, `RentalCount`,
   `LookupDed`, `LookupLine`.
10. **NEW: Rebuild `Tax_Summary` as a GROUPBY-driven cross-year view**
    reading from `Master_Inputs`. Fixes the `#REF!` and creates the
    first piece of the pivot view layer.
11. **NEW: Build a `Dashboard_Export` named-range block** —
    GROUPBY-driven, reads from `Master_Inputs`, stable cell addresses
    for the dashboards to pull from. Repoint step #4 targets this.
12. **NEW: Rebuild `PBC_List` as GROUPBY-driven** from `Master_Inputs`
    rows where `Source = Baseline`, grouped by Year/Bucket/Source_Type/
    Payor.
13. **NEW: Reconcile the two LAMBDA libraries** — 7 KISS + 14 v3
    coexist. Check for v3 LAMBDAs that have no KISS equivalent
    (`ExcessBusinessLossLimit_FN`, `PassiveLossAllowed_FN`,
    `NOLDeductionAllowed_FN` look load-bearing); keep those, retire the
    duplicates once KISS coverage is verified.

---

## What I'm explicitly NOT recommending

These were in the earlier version of this file. They're wrong given
what's actually built. Strike them:

- ~~"Rebuild the calc layer to read from Master_Inputs via GROUPBY"~~
  — would tear down working KISS LAMBDAs anchored to year sheets.
  The calc layer is fine where it is.
- ~~"Retire the Y#### sheets as input surfaces; collapse to master
  only"~~ — year sheets ARE the input surface in KISS. They stay.
- ~~"Make the master the source of truth, year sheets are derived
  views"~~ — KISS does the opposite, deliberately, and it works.
- ~~"Filing Stage = Extension / S1 / As Filed"~~ — actual scenario
  dimension is 5 levels: `Baseline | Override | S1 | S2 | AsFiled`.
  The `Override` and `S2` levels are real and used.

---

## Open items (genuinely still open)

- [ ] What "v8.6" was — referenced in the handoff as the base before
      KISS merge. Likely the workbook lineage before the v3 / KISS
      rewrite. Doesn't affect anything going forward but worth
      knowing for context.
- [ ] Where Jeff's dashboard workbook lives — handoff lists this as
      TBD; needs to be located before backlog item #2 can start.
- [ ] Whether the 7 external link targets (`Activity_Detail`,
      `Deductions_and_Adjustments1`, `Form_1040_Summary`, `2025`,
      `Y2022`, `STRATEGY_INPUTS`, `TAX_CALCULATIONS`) are obsolete
      paths or workbooks that need to be relocated and rewired.
- [ ] Whether `Input_Table_Mods` is still in use or transient.
