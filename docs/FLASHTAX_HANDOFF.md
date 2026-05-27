# FlashTax Handoff — Prototype Build + Database Architecture

> Handoff doc for a fresh Claude Code session. Self-contained: anyone reading this can pick up and build the prototype + understand the bigger vision.
>
> **Repo**: `smj1058/1040-Comprehnensive`
> **Branch**: `claude/pivot-tax-calculations-q4NyZ` (or whatever branch the new session designates)
> **User**: Seth Johnson (seth@accruity.com)

---

## 1. Context — what's already built and what we're building next

### Already built (this repo, this branch)

A **1040 tax planning workbook** (`Master_Pivot_Framework_v5_phase3v24_CC.xlsx` is the latest CC version) with:

- **Master_Inputs**: long-format table of tax facts (income, deductions, strategy impacts) with columns for Year, ClientID, Bucket, Treatment_Profile, Activity_Type (Baseline / Strategy), Provenance, Payor, Baseline_Amount, Helper_Amount, Helper_Treatment, Primary_Line, Primary_State, State_Mix, PTET_Routed, etc.
- **Year sheets Y2023-Y2028**: per-year sandboxes with 1040-line breakdown, calc engine (7 components: SE, payroll, ordinary, CG, NIIT, QBI, combined), and an At-a-Glance dashboard at rows 140-185.
- **Master_Strategies catalog**: 19 impact rows for 15 STR-* IDs, with multi-impact fan-out (S-Corp wage opt = -1z + +8, Hire Children = -8 + +1z + info-only Roth, etc.)
- **Tax_Plan_Dashboard**: 4-box layout following Active_Year
- **Deliverable sheet**: 7-section client-facing report
- **Property_Appendix, Framework_Ref, Tax_Ref** (rate tables, std ded, brackets, state rates, treatment profile map)
- **6 KISS LAMBDAs + fn_StrategyMarginal** (designed but pasted manually in Excel; openpyxl couldn't serialize them cleanly)
- **State tax stack** (multistate columns + state PTET routing on Master_Inputs)
- **QBI bug fix** (J119/K119 0.2 → 0.5 on year sheets)

See `docs/REMAINING_EXCEL_WORK.md` for full punch-list.

### Building next: FlashTax

A **separate workbook** (NOT modifying the 1040 workbook above) that:
1. Sits next to **Flash Reports by Finatical** in the same Excel session
2. Reads QBO data via Flash Reports' formula functions
3. Computes book-to-tax adjustments (Schedule M-1) per entity
4. Outputs **entity taxable income** per entity type (1120S / 1120 / 1065 / Sch C)
5. Bridges K-1 distributions to the 1040 framework

**Purpose**: prototype to walk into a meeting with the Finatical founder. Seth is positioning as a partner / feature-suggester / co-builder. FlashTax is the wedge — Finatical has financial data, we add the tax IP layer.

---

## 2. About Flash Reports / Finatical (the host product)

- **What it is**: Excel add-in for QuickBooks Online. Pulls live QBO data into Excel via **formulas** (function-based, like `=FR.PL("Revenue", ClientID, Year)` or similar — exact syntax TBD when Seth shares examples).
- **Multi-entity**: connects to unlimited QBO subscriptions; can consolidate.
- **Refresh model**: change a cell (ClientID / Year / Period) → all formulas recalc → new client's data appears. NO manual refresh button required for context switching.
- **Snapshots**: feature to convert formulas to static values, freezing a point in time.
- **New (March 2026)**: **Claude in Excel integration** — Claude lives in the same workbook, can read cells, explain variances, with cell-level citations.
- **Pricing page**: https://finaticalsoftware.com/pricing/
- **App listing**: https://quickbooks.intuit.com/app/apps/appdetails/flashreports/

**Implication for the prototype**: Build placeholders for Flash Reports formulas. Seth will paste the actual `=FR.<function>(...)` syntax during the meeting once he confirms the function names.

---

## 3. FlashTax — what to build

### Target file

`FlashTax_Prototype.xlsx` — standalone workbook, NOT merged into the 1040 framework. (Eventually FlashTax can pipe into the 1040 workbook via cross-workbook references for owner-level planning, but the prototype stands alone.)

### Sheet structure

| # | Sheet | Purpose |
|---|---|---|
| 1 | **Cover** | Branded title page — "FlashTax for [Client Name] — [Year]" with selectors visible |
| 2 | **Control_Panel** | ClientID, EntityID, EntityType, Year, Period selectors (drive everything) |
| 3 | **PL_Live** | P&L cells that call Flash Reports formulas (placeholders for now) |
| 4 | **BS_Live** | Balance Sheet cells calling Flash Reports formulas |
| 5 | **M1_Reconciliation** | Book net income → adds → subs → taxable income |
| 6 | **TaxableIncome_Output** | Entity taxable income summary by type (1120S / 1120 / 1065 / Sch C) |
| 7 | **K1_Bridge** | For pass-through entities: K-1 distribution by owner with ownership %, ready to land in owner's 1040 |
| 8 | **Claude_Prompts** | 5-7 ready-to-paste Claude-in-Excel prompts demonstrating value |
| 9 | **TaxRef_M1** | Reference table of M-1 categories with rules and citations |
| 10 | **Settings** | EntityType-specific rule toggles, override switches |

### Schemas

#### Control_Panel cells (named ranges)

```
ClientID         — text dropdown (sourced from a client list, hardcoded for prototype)
EntityID         — text dropdown
EntityType       — enum: 1120S / 1120 / 1065 / SchC / SchE / Trust
Year             — number (2023..2028)
Period           — enum: Q1 / Q2 / Q3 / Q4 / YTD / Annualized / Projected / Final
BookBasis        — enum: Accrual / Cash
TaxBasis         — enum: Accrual / Cash (often different from BookBasis)
```

Every formula on PL_Live, BS_Live, M1_Reconciliation references these via named ranges. Change `ClientID` cell → entire workbook recalcs.

#### M1_Reconciliation table (the heart of FlashTax)

Each row is one M-1 adjustment line. Suggested categories (with form citations):

| Category | Direction | Book vs Tax | Typical Source |
|---|---|---|---|
| Federal income tax expense | Add | Book deducts; tax doesn't | P&L `FedTaxExpense` |
| State income tax expense (entity-level) | Depends on PTET | Varies | P&L `StateTaxExpense` |
| Depreciation difference (DDA) | Add or Sub | Book SL vs tax MACRS/§168(k)/§179 | Computed from Fixed Asset module |
| §263A inventory capitalization | Add | Tax requires capitalizing more costs | Reasoned estimate |
| Meals (50%) | Add | Book 100%, tax 50% | P&L `Meals` × 0.5 |
| Entertainment (100%) | Add | Book deducts, tax doesn't (post-2017) | P&L `Entertainment` |
| Political contributions | Add | Book deducts, tax doesn't | P&L `PoliticalContrib` |
| Fines & penalties | Add | Book deducts, tax doesn't | P&L `Penalties` |
| Tax-exempt interest | Sub | Book includes, tax excludes | P&L `MuniInterest` |
| Life insurance proceeds | Sub | Book includes, tax excludes | P&L (rare) |
| §179 depreciation | Sub | Tax accelerates over book | Fixed Asset module |
| Bonus depreciation §168(k) | Sub | Tax accelerates over book | Fixed Asset module |
| Accrued compensation not paid in 2.5 mo | Add | Book accrues, tax requires payment | Payroll module |
| Bad debt reserve | Add | Book reserves, tax direct write-off only | AR aging |
| Charitable contributions over 10% AGI cap | Add (corp only) | C-Corp cap, S-Corp passes through | P&L `Charitable` |
| Net operating loss carryforward | Sub | Tax-specific | Prior year tax return |
| Tax credits (R&D, etc.) | Note | Reduces tax, not income | Separate calc |

#### Output: Taxable Income by entity type

For each entity type, the output formula is:

```
Net Income per Books (from Flash Reports P&L)
  + Σ M1 Adds
  − Σ M1 Subs
  = Taxable Income before special deductions
  − Special deductions (e.g., DRD for C-Corp, QBI for individuals)
  = Federal Taxable Income
```

#### K-1 Bridge (for pass-through entities only)

```
Per entity (1120S / 1065):
  Taxable Income → Total
  
Per owner:
  Ownership %  ← from a tblOwnership table (manually entered for prototype; production = from database)
  Owner's share = Total × Ownership %
  
Output: list of (OwnerID, EntityID, Year, Share_OrdinaryIncome, Share_CG, Share_QBI, Share_Section199A_W2, Share_UBIA)
  ↓
  ready to import into owner's 1040 Master_Inputs as new rows with Helper_Treatment = K1_SCorp_Active / K1_PTP_Passive / etc.
```

This is the **direct bridge** to the 1040 framework already in this repo.

### Flash Reports formula placeholders

Until Seth provides actual syntax, use these placeholder patterns:

```excel
=FR.PL(account_name, ClientID, Year, Period)             ← P&L cell
=FR.BS(account_name, ClientID, AsOfDate)                  ← BS cell
=FR.Drill(account_name, ClientID, Year, Period)           ← drill-down link
=FR.Snapshot(snapshot_id)                                 ← static historical value
```

Mark each placeholder cell with a yellow fill (`FFF2CC`) so Seth can find and paste real syntax during the meeting.

### Claude_Prompts sheet — 5-7 demonstrating value

Pre-load these prompts so the founder sees Claude is useful inside FlashTax:

1. **"Explain my Q3 M-1 variance"** — Claude reads M1_Reconciliation, identifies which lines moved the most QoQ, and writes 2-3 sentences of plain language.
2. **"What's the tax impact of accruing the $50K Q4 bonus on 12/31 vs paying it 3/1?"** — Tests the 2.5-month rule. Claude computes both scenarios.
3. **"Compare my book net income to taxable income for the last 3 years"** — Trend on the M-1 bridge.
4. **"Which M-1 category is growing fastest as a % of book income?"** — Anomaly / trend detection.
5. **"Estimate my §199A QBI deduction for this entity"** — Reads the entity-type, applies QBI rules from the Tax_Ref already built.
6. **"What's my effective tax rate by entity in 2025?"** — Multi-entity comparison.
7. **"If I take a $100K distribution from the S-Corp, what's my owner-level tax impact?"** — Cross-workbook to 1040 framework.

### VBA stubs (skeleton, not full implementation)

```vba
' mod_FlashTaxControl
Sub RefreshAllClients()
    ' Loop over tblClients, set ClientID cell, calc, save
End Sub

Sub SnapshotCurrent()
    ' Capture current PL/BS/M1 state to a versioned sheet
End Sub

Sub PushToOwner1040()
    ' For each pass-through entity in current view:
    '   Read K1_Bridge sheet
    '   Write rows into owner's Master_Pivot_Framework Master_Inputs
End Sub
```

### One-page pitch (for the meeting handout)

Print as PDF or include as the Cover sheet:

```
FLASHTAX — Tax-Ready Financial Close for Flash Reports

THE PROBLEM
Flash Reports stops at the financial statement. Tax practitioners then
spend hours hand-rolling M-1 adjustments in Excel, re-keying numbers,
and bridging K-1s to individual 1040s.

THE SOLUTION
FlashTax sits next to Flash Reports in the same workbook. Reads your
=FR.<func>() cells. Computes Schedule M-1 reconciliation per entity
type. Outputs taxable income. Bridges K-1s to owner returns.

WHY FINATICAL WINS
- Locks in the higher-ARPU tax practitioner segment (currently lost
  to ProConnect / Lacerte add-ons)
- Same workbook = Claude can analyze BOTH financial and tax in one
  conversation, with cell-level citations
- Defensible moat — tax IP is harder to replicate than report
  templates

WHO IT'S FOR
- Tax-focused CPA firms (250K+ in US)
- Family offices doing entity consolidation + tax planning
- Wealth advisors who need pre-tax projections for clients

PRICING IDEA
Add-on to Flash Reports — $50-100/month per practitioner. Justified
by 2-3 hours saved per client per quarter.

ROADMAP
- Phase 1 (this prototype): M-1 reconciliation, taxable income output
- Phase 2: K-1 bridge to 1040, owner-level planning
- Phase 3: Multi-entity consolidation with ownership-weighted M-1
- Phase 4: Industry benchmarking, year-over-year trend, AI commentary
```

---

## 4. The bigger Database vision (back-burner, for context)

FlashTax is the wedge product. The full architecture Seth has in mind is a **practice-level data system** for accounting firms. Knowing this context helps avoid building FlashTax in ways that conflict with later phases.

### Hierarchy

```
FIRM                              (the CPA practice — Seth's firm)
  └─ CLIENTS                      (households / engagement groups)
       └─ ENTITIES                (legal entities: S-Corps, LLCs, partnerships, trusts)
            └─ TRANSACTIONS       (GL data per entity, refreshed from QBO via Flash Reports)

Cross-cutting tables:
  INDIVIDUALS                     (people who own entities directly)
  OWNERSHIP_RELATIONSHIPS         (effective-dated %, by class, voting/non)
  STANDARD_COA                    (normalized chart of accounts — Seth's tax line coding)
  ACCOUNT_MAPPINGS                (per-entity QB CoA → Standard CoA)
  GROUPINGS                       (different lenses on standard accounts)
```

### Key tables

```sql
tblFirms          (FirmID, Name, Type, ContactInfo)
tblClients        (ClientID, FirmID, Name, PrimaryContact, Type)
tblEntities       (EntityID, ClientID, Name, EntityType, EIN, StartYear,
                   ClosedYear, NAICS, HomeState, FiscalYearEnd)
tblIndividuals    (IndividualID, FirstName, LastName, SSN_last4, DOB, Notes)
tblOwnership      (OwnershipID, EntityID, OwnerType, OwnerID, Percent,
                   Class, Voting, EffectiveStart, EffectiveEnd)
tblStandardCoA    (AccountID, AccountName, BalanceType, NAICS_Mapping,
                   TaxLine_1120, TaxLine_1120S, TaxLine_1065, TaxLine_SchC,
                   Sort_Order)
tblAccountMap     (MapID, EntityID, LocalAccountName, StandardAccountID,
                   ApprovedBy, ApprovedDate)
tblGroupings      (GroupingID, Name, Description, Purpose)
tblGroupingDetail (GroupingID, StandardAccountID, DisplayLabel, Sort_Order,
                   SignMultiplier, ParentLabel)
tblTransactions   (TxnID, EntityID, StandardAccountID, Year, Period, Amount,
                   Source, Provenance, IC_Flag, Notes)
tblConsolidationGroups (GroupID, RootClientID, IncludedEntityID,
                        Method [Full/Equity/Cost], EffectiveStart, EffectiveEnd)
tblIntercompany   (ICID, EntityID_A, EntityID_B, Description,
                   ExpectedConvention, MatchRule)
tblSnapshots      (SnapshotID, EntityID, Milestone [Extension/S1/AsFiled/Amended],
                   SnapshotDate, FrozenState_JSON_or_blob)
```

### The 4 layers that make this work

1. **Standardized CoA + mapping** — every QB account in every client maps to one StandardAccountID. This is the foundation; once mapped, everything else flows.
2. **Ownership graph + effective-dating** — supports consolidation, K-1 distribution, ownership-change scenarios.
3. **Consolidation engine** — given a `ClientID + Year + Period`, walks ownership tree, applies full/equity/cost method, eliminates intercompany, returns one consolidated set.
4. **Groupings** — same standard accounts viewed through different lenses (GAAP / Tax-by-entity-type / Mgmt / Lender / Industry / Audit workpaper).

### The hard problems

| Problem | Why hard | Where to focus |
|---|---|---|
| Account mapping at scale | Every QB file is a snowflake — ~200 accounts per client | AI-suggest + reviewer workflow + audit log |
| Ownership over time | Sales / restructures change %; historical reports must use period-correct % | Effective-dated records; point-in-time queries |
| Intercompany detection | Same dollar in two entities; manual ID is painful | Matching algorithm: amount + date proximity + opposite sign + 2 entities in same client |
| Period alignment | Different fiscal year-ends across entities | Periodization layer; stub periods if needed |
| Tax ≠ book at every level | Each entity has M-1; consolidated tax ≠ sum of consolidated book | Per-entity M-1, then consolidation, then top-level tax adjustments |
| Versioning | What CoA / mapping / ownership was in effect when this snapshot was taken? | Snapshot blobs (frozen) + mapping audit log (reproducible) |

### Phasing toward the full vision

| Phase | Scope |
|---|---|
| **A — FlashTax MVP** | Single entity, M-1 reconciliation, taxable income output. This handoff. |
| **B — K-1 Bridge** | Connect pass-through entities to owners' 1040 framework. |
| **C — Multi-Entity per Client** | Repeat A+B for each entity of a client; manual consolidation for now. |
| **D — Standard CoA** | Build the dictionary + mapping engine. Onboarding workflow. |
| **E — Ownership Graph** | tblOwnership + effective-dating. Consolidated K-1 distribution. |
| **F — Consolidation Engine** | Full/equity/cost method math + intercompany elimination. |
| **G — Groupings** | Multiple presentation lenses on the same data. |
| **H — Cross-Client Analytics** | Practice dashboard, industry benchmarking, anomaly detection. |
| **I — Snapshot / Audit Trail** | Versioning, milestone capture, workpaper export. |

FlashTax (Phase A) is the wedge. Phases B-I are the moat.

---

## 5. Existing assets in this repo to leverage

- `docs/Master_Pivot_Framework_v5_phase3v24_CC.xlsx` — the 1040 calc framework. K-1 outputs from FlashTax should land in this workbook's `Master_Inputs` via cross-workbook reference or VBA push.
- `docs/REMAINING_EXCEL_WORK.md` — punch list for finishing the 1040 workbook.
- `Tax_Ref` sheet inside the 1040 workbook — has bracket tables, std ded, NIIT thresholds, state rates, treatment profile map. Can be referenced or duplicated in FlashTax.
- `Master_Strategies` sheet — strategy catalog with multi-impact fan-out; may be useful for showing tax-planning hooks from financial data.
- The 7 KISS LAMBDAs (`TAX_ORD`, `TAX_CG`, `TAX_NIIT`, `TAX_SE`, `STD_DED`, `TAX_STATE`, `fn_StrategyMarginal`) — pasted into the 1040 workbook's Name Manager. FlashTax can import these LAMBDAs into its own Name Manager OR cross-reference.

---

## 6. Naming convention (this repo's standard)

| Suffix | Meaning |
|---|---|
| `_CC` | File built by Claude via openpyxl |
| `_SJ` | File built / edited by Seth in Excel |
| `v{N}` | Iteration version |

So your output should be: `FlashTax_Prototype_v1_CC.xlsx` (or higher iteration).

---

## 7. What NOT to do

- **Don't modify** `Master_Pivot_Framework_v5_phase3v*_CC.xlsx`. FlashTax is a separate workbook.
- **Don't assume Flash Reports formula syntax** — use placeholders (`=FR.PL(...)`) clearly marked. Seth has the actual syntax and will paste it during the meeting.
- **Don't build the full database** in this prototype. The hierarchy / consolidation / mapping engine is Phase D-F work. FlashTax MVP is single-entity only.
- **Don't repeat the LAMBDA syntax-error problem** from the 1040 workbook. If you install LAMBDAs in FlashTax, install them with proper `_xlpm.` parameter markers OR (preferred) write them as instructions for Seth to paste into Name Manager manually.
- **Don't add macros that auto-run on open** — Excel macro security will fight you. All macros should be button-triggered.

---

## 8. Suggested build sequence (for the new session)

1. **Scope confirm** — ask Seth for (a) the actual Flash Reports formula function name(s), (b) entity types to support in the prototype, (c) when the meeting is so urgency is calibrated.
2. **Build skeleton** — 10 sheets per Section 3 above, with named ranges defined on Control_Panel.
3. **M-1 reconciliation logic** — that's the demo centerpiece. Make it work with manual inputs first (PL_Live cells as placeholder yellow), then swap to Flash Reports formulas.
4. **K-1 Bridge** — single owner case for the prototype. Multi-owner is Phase C.
5. **Claude_Prompts sheet** — pre-load the 5-7 prompts so Seth can demo Claude live.
6. **Cover + one-page pitch** — Seth's handout.
7. **Test by manually setting Control_Panel ClientID and Year** — verify everything recalcs.
8. **Deliver via SendUserFile** + commit to repo on a new branch named `claude/flashtax-prototype-XYZ`.

---

## 9. Open questions for Seth before building

1. What's the actual Flash Reports function name? (`=FR.PL`, `=FRGET`, `=FLASH.GET`, other?)
2. What entity types for the prototype — just 1120S, or full set (1120 / 1120S / 1065 / SchC)?
3. Is there a sample client he wants used (Cedillo? a real Flash Reports demo client?) for the M-1 walkthrough?
4. Should K-1 Bridge output a file that imports into `Master_Pivot_Framework_v5_phase3v24_CC.xlsx`, or just show what the output would look like?
5. When is the founder meeting? (Affects polish vs. speed tradeoff.)

---

## 10. Repo context

```
/home/user/1040-Comprehnensive/
├── docs/
│   ├── Master_Pivot_Framework_v5_phase3v24_CC.xlsx     ← 1040 workbook (LATEST)
│   ├── REMAINING_EXCEL_WORK.md                          ← Excel-side todo for 1040
│   ├── FLASHTAX_HANDOFF.md                              ← THIS FILE
│   └── EXCEL_PROMPT_*.md                                ← misc Excel handoff prompts
├── scripts/
│   └── phase3v*_*.py                                    ← openpyxl build scripts (1040 workbook)
└── CLAUDE.md                                            ← project instructions (mostly for dossier work)
```

GitHub: `smj1058/1040-Comprehnensive`
Restricted scope: this repo only.

---

## 11. Other add-on concepts in the brainstorm pipeline

> FlashTax is the wedge. These are the broader product family Seth is sketching for Finatical. Mentioned here so a new session understands the bigger picture and avoids decisions that conflict with later ideas.

### FlashTax (Phase 1 — this prototype)
Book-to-tax bridge sitting next to Flash Reports. M-1 reconciliation, taxable income output, K-1 bridge to 1040.

### FlashPractice (Phase 2 — multi-client roll-up)
Practice-level Master DB.xlsx that watches a `/clients/` folder of Flash Reports outputs and auto-aggregates via Power Query.
- Cross-client KPI dashboards (revenue concentration, fee realization, client health)
- Anomaly flags (revenue ↓ >15% MoM, AR aging >60 days, ratio thresholds)
- "Across my portfolio, which 3 clients need attention this week?" Claude prompt
- Industry benchmarking using NAICS-coded entities
- Removes the single-client constraint that limits Finatical's sales to mid-size firms

### FlashSnapshot (Phase 3 — time-series audit trail)
Versioning layer on top of any Flash Reports workbook.
- Captures snapshots at workflow milestones (Extension, S1, As-Filed, Amended, Reviewed)
- Diff reports between snapshots — what changed, by whom, when
- Workpaper-ready PDF export
- Meets PCAOB / SSARS workpaper standards
- Opens the audit firm market for Finatical (large TAM)

### FlashConsolidate (Phase 4 — multi-entity consolidation)
Ownership-weighted consolidation for clients with multiple entities.
- tblOwnership with effective-dated %
- Full / equity / cost method math
- Intercompany elimination engine
- True consolidated P&L + BS for the entire client (vs single-entity reports)
- Eliminates the manual Excel consolidation work that family offices and multi-entity clients currently pay separately for

### FlashTaxonomy (Phase 5 — standardized chart of accounts)
The foundation layer that makes everything above scale.
- Master standardized CoA (~200-400 normalized accounts)
- Per-entity mapping table (LocalAccountName → StandardAccountID)
- AI-assisted mapping suggestions on client onboarding
- Multiple groupings (GAAP / Tax / Mgmt / Lender / Industry / Audit)
- Once mapped, every report / consolidation / benchmark just works
- This is the highest-effort phase but the deepest moat — mapping data is hard to replicate

### Connecting concepts

- **FlashTax + FlashPractice** = practice-level tax visibility ("which clients owe estimated tax in 3 weeks?")
- **FlashPractice + FlashSnapshot** = portfolio history ("show me every quarter-close variance across my book this year")
- **FlashConsolidate + FlashTaxonomy** = ground truth for multi-entity reporting ("here's the family's true consolidated P&L across all 6 entities")
- **All five + Claude in Excel** = a tax & advisory practice operating system, not just a reporting tool

### Pitch framing for the founder meeting

> "Flash Reports gives you live QBO data in Excel. That solves the report-generation problem. The next problems are: (1) bridging that to tax, (2) seeing across all my clients, (3) freezing history for audit defense, (4) consolidating multi-entity families, and (5) standardizing the CoA so all of the above scale. I've been thinking through what each of these looks like as a Flash Reports add-on. FlashTax is the prototype I brought today; the others are the roadmap."

This positions Seth not as a feature-suggester but as **product strategy**. The prototype proves he can execute.

---

## 12. Note on this handoff doc

This document lives at `docs/FLASHTAX_HANDOFF.md` in the `smj1058/1040-Comprehnensive` repo. Seth will also be adding a copy to his local `MCP_Projects` folder on his computer for reference / cross-context use. The repo version is the source of truth for any Claude Code session picking up this work.

If the doc gets updated in either location, the repo version should be re-sync'd to match.

---

## 13. Quick-start prompt for the new session

> Paste at the top of your new Claude Code session:

```
Read docs/FLASHTAX_HANDOFF.md fully. That's the brief. Then ask Seth the 5
open questions in Section 9 before building. Once answered, work through
the build sequence in Section 8.

Deliver as FlashTax_Prototype_v1_CC.xlsx on a new branch
claude/flashtax-prototype-{your-suffix}. Commit + push at the end.
Use SendUserFile to deliver the file inline.

Do NOT modify Master_Pivot_Framework_v5_phase3v24_CC.xlsx or anything
else in this repo's existing 1040 workbook.

Section 11 lists 4 follow-on concepts (FlashPractice, FlashSnapshot,
FlashConsolidate, FlashTaxonomy). Don't build them in this session,
but be aware of them so design choices in FlashTax don't paint us
into a corner for later phases.
```
