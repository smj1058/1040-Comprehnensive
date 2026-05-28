# Finatical / Flash Reports — Strategic Enhancement Memo

> **Project**: Enhancing Flash Reports for accounting firms, large family offices, and tax practitioners
> **Author**: Seth Johnson (seth@accruity.com)
> **Status**: Strategic vision + product concept memo
> **Companion docs**: `FLASHTAX_HANDOFF.md` (technical handoff for prototype build)

---

## EXECUTIVE SUMMARY

Flash Reports is an excellent live query layer for QuickBooks Online data in Excel. It solves the "get the data into a workbook" problem cleanly. But for the high-value users — multi-client accounting firms, multi-entity family offices, tax practitioners — that's only the first step.

This memo describes what an enhanced Flash Reports platform looks like, the use cases it unlocks, and the architecture that makes it possible. The thesis: **Flash Reports becomes the foundation for a family of advisory-grade add-ons, not just a reporting tool.**

The four enhancements that matter most:

1. **Multi-client aggregation** — see across a firm's entire book of business
2. **Live computed metrics** — hard calculations like LTV, CAC, customer profitability, cohort retention, computed continuously rather than rebuilt manually each quarter
3. **External data integration** — connect to non-QBO sources (Plaid for personal banking, payroll systems, CRM, brokerage feeds) so the platform reflects total household / business reality
4. **Tax integration** — book-to-tax reconciliation, K-1 distribution to individual returns, year-round tax projection rather than annual cleanup

All four ride on a single thin platform layer that, critically, **does not store the GL** — it stores only metadata, configuration, and milestone snapshots. The data lives in QBO. Flash Reports queries it live. The platform layer adds the multi-client, multi-period, multi-source coherence that turns "a reporting tool" into "a practice operating system."

---

## THE OPPORTUNITY

### Who has the problem

| Segment | Pain |
|---|---|
| **Accounting firms** (250K+ in the US) | One workbook per client. No firm-wide view. Manual roll-ups every month. Can't see across clients to find anomalies, opportunities, or risks. |
| **Tax practitioners** | Financial reports stop at the P&L. Tax adjustments (M-1, depreciation differences, accrued comp, meals, etc.) are hand-rolled in separate Excel files. Filing-time scramble. No year-round position tracking. |
| **Family offices** | Multiple entities owned by the same family with varying ownership percentages. True consolidation requires manual labor every quarter. Individual + business tax interaction is siloed. |
| **Advisory firms (CFO, fractional CFO, wealth)** | Hard calculations (LTV, CAC, cohort retention, gross margin by customer) require building one-off models per client. Models don't update automatically. Insight isn't repeatable. |

### What Flash Reports does well today

- Live QBO data in Excel via formulas
- Drill-down to source transactions
- Multi-entity consolidation at the company level
- Reporting Pack with branded multi-section workbooks
- Claude in Excel integration for AI-assisted analysis (March 2026 release)

### Where it falls short for advisory-grade use

- **Single-client at a time**: each workbook handles one client. No cross-client visibility.
- **No standardized chart of accounts across clients**: each client's QBO is bespoke; comparison is hard.
- **Snapshots are workbook-wide only**: can't freeze Q1 while keeping Q2-Q4 live; can't have As-Filed and Working coexist in one file.
- **No tax integration**: financial reports don't bridge to taxable income.
- **No external data sources**: personal banking, payroll, brokerage, CRM — none of it is in Flash Reports' scope today.
- **No advanced computed metrics**: LTV, CAC, cohort retention, customer profitability with allocated overhead — practitioners build these themselves, every time.

These are the gaps the enhancement program fills.

---

## THE VISION — Flash Reports as a platform

Today Flash Reports is a **product**. The enhancement vision turns it into a **platform** — a foundation that other capabilities sit on top of.

```
┌─────────────────────────────────────────────────────────────────┐
│                  PLATFORM (FlashCore)                            │
│   Metadata service + snapshot vault + cross-source connectors    │
│   Small, Excel-native, no GL storage                             │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
                  ┌──────────┴──────────┐
                  ↓                     ↓
          ┌──────────────┐      ┌──────────────────┐
          │ DATA SOURCES │      │   APPLICATIONS    │
          │ ──────────── │      │   ─────────────   │
          │ • QBO via    │      │ • Tax bridge      │
          │   Flash      │      │ • Health score    │
          │   Reports    │      │ • Practice roll-up│
          │ • Plaid      │      │ • Consolidation   │
          │   (personal) │      │ • LTV/CAC engine  │
          │ • Payroll    │      │ • Snapshot/audit  │
          │ • Brokerage  │      │ • Template library│
          │ • CRM        │      │ • + more          │
          └──────────────┘      └──────────────────┘
```

**The single most important architectural insight**: the platform does NOT store the GL. Live data flows through Flash Reports formulas on demand. The platform stores only:

1. **Metadata** — who the clients are, what entities they own, ownership percentages, period definitions, account mappings
2. **Aggregate snapshots** — frozen values at milestone moments (As-Filed, Extension, S1, Amended, Reviewed)
3. **Selective deep snapshots** — transaction-level capture only for high-consequence accounts (Fixed Assets, Loans always; Inventory / WIP / Equity / specific Revenue configurable per client)
4. **Templates** — workbook layouts with formulas, zero data

Total storage for a 30-client firm over 5 years: comfortably under 100,000 rows. Fits in one Excel file. No SQL Server, no data warehouse, no ETL pipelines, no batch refresh maintenance.

---

## WHAT IT ENABLES

### 1. Multi-client aggregation

A firm with 30+ clients currently has 30+ workbooks that don't talk to each other. The platform watches a `/clients/` folder of refreshed Flash Reports outputs and rolls them up:

- **Firm-wide dashboard**: total revenue, total clients, top concentration risks, AR aging across the book
- **Anomaly flagging**: "which clients had revenue drops >15% this month? which have AR aging >60 days?"
- **Benchmarking**: compare clients in the same industry (NAICS-coded), surface outliers
- **Practice KPIs**: realization, utilization, average fee per client, client retention curves

Workflow magnet: instead of "open each workbook and check," the firm opens one dashboard and sees the whole book at a glance.

### 2. Live computed metrics — the hard calculations

This is where Flash Reports today falls short. Practitioners and CFOs constantly want metrics that require sustained customer-level tracking across time:

| Metric | What it requires | Why it's hard today |
|---|---|---|
| **Customer Lifetime Value (LTV)** | Revenue per customer per period × margin × retention curve | Requires customer-level history across years, joined with cost data |
| **Customer Acquisition Cost (CAC)** | Sales + marketing spend ÷ new customers acquired | Requires segmenting cost data + attribution logic |
| **LTV:CAC ratio** | LTV / CAC, trended | Requires both above, plus cohort definitions |
| **Cohort retention** | % of customers retained from month-1 to month-N by cohort | Requires longitudinal customer tracking |
| **Customer profitability** | Revenue × margin per customer, with allocated overhead | Requires customer-level cost allocation rules |
| **Gross margin by product line** | Revenue × COGS allocation by SKU/line | Requires standardized SKU mapping |
| **Project / job profitability** | Per-project labor + materials + indirect | Requires project tagging and time tracking integration |
| **Vendor concentration risk** | % spend with top 5 / 10 vendors | Requires standardized vendor categorization |

With the platform layer, each of these becomes a **template that consumes the standardized data + snapshot vault**. Build it once, every client gets it. Refresh automatically. No more one-off models.

This is the **enterprise-grade computation** Flash Reports is missing — and it's exactly what high-value firms need.

### 3. External data integration

QBO is one source. The platform adds connectors so users can pull in:

| Source | What it adds |
|---|---|
| **Plaid (banks, brokerages)** | Personal banking data for individuals; cash position across accounts; investment holdings |
| **Payroll systems (Gusto, ADP, QB Payroll)** | Owner W-2, employee comp detail, FICA wage base tracking |
| **CRM (HubSpot, Salesforce)** | Customer attribution, sales pipeline, deal close detail |
| **E-commerce / billing (Stripe, Shopify, Recurly)** | Granular subscription metrics, churn detection, plan-level revenue |
| **Time tracking (Harvest, Toggl)** | Billable utilization, project profitability |
| **Bank feeds direct** | Transaction-level cash flow for individuals not on Quicken |

This is where the platform serves **individuals and households**, not just businesses. For a tax practitioner serving an owner-operator, the client's tax picture = business activities + personal activities. Both need to flow into the unified view.

### 4. Tax integration

The biggest gap for tax practitioners. Today's workflow:

1. Flash Reports gives you the P&L
2. You export to Excel
3. You hand-compute book-to-tax adjustments (Schedule M-1)
4. You determine taxable income
5. You manually transfer K-1 distributions to each owner's 1040 file
6. At year-end you scramble

The enhanced platform adds an app — **FlashTax** — that:

- Reads the Flash Reports P&L and BS cells directly
- Computes M-1 reconciliation per entity type (1120S / 1120 / 1065 / Sch C)
- Tracks every category that needs adjustment (depreciation difference, §263A, meals 50%, entertainment 100%, fines, tax-exempt interest, §179, bonus depreciation, accrued comp not paid in 2.5 months, bad debt reserve, charitable >10% AGI, NOL carryforward, R&D credit)
- Outputs entity taxable income
- For pass-through entities, bridges K-1 distributions to each owner's individual 1040 framework
- All live, all in the same workbook, all citation-traceable via Claude in Excel

The downstream effect: **year-round tax tracking**. Instead of seeing the client once at filing, the practitioner sees current tax position every month. Quarterly estimated tax math is automatic. Strategy decisions are made when they have impact, not after the fact.

---

## ARCHITECTURE — three storage tiers, each with one job

For the technically curious. Most readers can skim.

### Tier 1 — Master DB (the refined layer)
- Excel file, lives at the firm level
- Contains: clients, entities, ownership percentages with effective dates, standardized chart of accounts, per-entity account mappings, period registry
- Contains: aggregate snapshots (account × entity × period × value × snapshot date × milestone)
- Contains: configuration (which clients want which deep-snapshot categories)
- **Size**: ~5-10K rows for a 30-client firm. Tiny.

### Tier 2 — Live client workbooks (the live layer)
- One Excel file per client
- Pure Flash Reports formulas — no data stored
- Change ClientID / Year / Period cells → entire workbook recalcs with that client's current data
- Drill-down via Flash Reports' native feature → live QBO transactions
- **Storage**: zero data, just formulas. KB per file.

### Tier 3 — Deep snapshot vault (the audit-grade layer)
- Excel file or Power Pivot model
- Contains: transaction-level captures for high-consequence categories only
- **Always-on categories**: Fixed Assets, Loans (basis + multi-year tax positions can't be reconstructed otherwise)
- **Configurable per client**: WIP, Inventory, Equity, specific Revenue codes
- **Drift detection without storing transactions**: for everything else, compare each live transaction's Modified Date against the snapshot date — flag transactions modified after snapshot
- **Size**: ~200-600 transactions per client per year. Bounded. ~18K transactions/year for a 30-client firm.

### What's NOT stored
- The full GL — never duplicated, never warehoused
- Routine AR / AP / payroll / expense transactions — flowed through Flash Reports live
- Per-client per-year archive files — not needed; live drill is sufficient with drift detection

This is the architecture's elegance: a typical "build a multi-client financial system" project is 6-12 months and requires SQL Server. This is 4-6 weeks of Excel work because Flash Reports already owns the hard part (the QBO data pipeline).

---

## SPECIFIC PRODUCT FEEDBACK FOR FLASH REPORTS

Beyond the platform vision, one concrete Flash Reports feature ask:

**Granular snapshots.** Current snapshot feature converts the entire workbook from formulas to values. Too coarse for actual workflow:

- **Rolling quarter close** — at Q1 close, freeze Q1 column but keep Q2-Q4 live. Currently impossible.
- **As-Filed vs Working** — one tab snapshotted at filing, another stays live. Currently impossible.
- **Projection vs Actual** — snapshot the "Q1 projection" tab in February, leave "Q1 actual" tab live, variance tab compares. Currently impossible.
- **Audit defense** — multiple "as of" snapshots in one file (Extension / S1 / As-Filed / Amended). Currently requires four separate files.

**Recommended granularity levels**: Workbook (current), Sheet, Column, Row, Named Range, Cell list.

**Most impactful additions**: Column-level (handles rolling close) and Named Range-level (handles everything else flexibly). Implementation is straightforward — selective formula → value conversion within a chosen scope, with a hidden marker preserving the original formula for "un-snapshot."

This single feature dramatically expands workflow possibilities and is achievable in 2-3 weeks of engineering. Long-term answer is the centralized snapshot vault described above, but granular snapshot is the immediate win.

---

## ROADMAP

Sketched as phases, each delivering standalone value:

### Phase 0 — Foundations (Finatical's existing product)
Live formulas, drill-down, multi-entity consolidation, Reporting Pack, Claude in Excel. **Done.**

### Phase 1 — Granular snapshot
Workbook → Sheet / Column / Named Range scope. Immediate workflow unlock. 2-3 weeks engineering.

### Phase 2 — FlashCore (the platform layer)
Metadata service + aggregate snapshot vault + standardized CoA + per-client account mappings. The thin layer that turns Flash Reports into a platform. 4-6 weeks engineering.

### Phase 2.5 — FlashOnboard (the wizard that populates the platform)
The user-facing front door to FlashCore. Without this, the platform is a database with no UX. See "FlashOnboard" section below for detail.

### Phase 2.7 — FlashStandardize (write-back to QBO for data hygiene)
**Potentially the highest-value feature in the entire family.** Pushes standardized vendor categories, missing accounts, bookkeeping rules, class lists back into client QBOs. Eliminates the bookkeeper labor that's the #1 cost in every accounting firm. Creates strong lock-in via standardization. Requires QBO API write scope + approval workflows. Detailed below.

### Phase 3 — FlashTax (the first app)
Book-to-tax M-1 reconciliation, taxable income output, K-1 bridge to individual 1040. Proves the platform architecture and opens the tax practitioner segment. Co-developed with tax SME (Seth).

### Phase 4 — FlashPractice (multi-client roll-up)
Firm-wide dashboards, anomaly flagging, industry benchmarking, practice KPIs. Removes the single-client sales constraint.

### Phase 5 — FlashMetrics (computed metrics engine)
LTV, CAC, cohort retention, customer profitability, project profitability, vendor analysis. Advisory-grade calculations as out-of-the-box templates.

### Phase 6 — External data connectors
Plaid for personal banking, payroll integrations, CRM connectors, e-commerce / billing systems. Brings individuals + cross-source data into the platform.

### Phase 7 — FlashConsolidate (ownership-weighted multi-entity)
True consolidated P&L and BS for clients with multiple entities. Walks ownership tree, applies full / equity / cost method, eliminates intercompany. Family office wedge.

### Phase 8 — FlashSnapshot (audit-grade)
User-facing interface to the snapshot vault. Milestone capture, diff reports, workpaper-ready PDF export. Opens audit firm market.

### Phase 9 — FlashLibrary (template marketplace)
Practitioner-contributed templates (construction WIP, SaaS metrics, law firm trust accounting, etc.) — install with one click. Network effects play.

---

## DETAILED ADD-ON DESCRIPTIONS

### FlashOnboard — the wizard that populates the platform

The user-facing entry point to FlashCore. Without it, the platform is a database with no front door. What it does:

- **Client intake**: collect firm, client name, EIN, NAICS code, fiscal year-end, ownership structure
- **CoA mapping assistant**: pull client's QBO chart of accounts, AI-suggests mappings to the firm's standardized CoA, queue uncertain matches for reviewer approval, audit log every mapping decision
- **Historical backfill**: pull 1-3 prior years of QBO data, apply mappings, generate baseline aggregate snapshots
- **Period setup**: define which periods to track (monthly / quarterly), schedule snapshot triggers (manual, milestone-driven, scheduled)
- **Snapshot configuration**: which deep-snapshot categories for this client (Fixed Assets + Loans always on; WIP / Inventory / Equity / specific Revenue configurable)
- **Stakeholder setup**: identify owners with effective-dated percentages, individuals who own entities, roles (preparer, reviewer, partner) and access
- **Engagement letter automation**: generate from client metadata, track scope changes, capture signatures
- **Data quality scan**: initial review of client's QBO for red flags — broken accounts, unclassified transactions, gaps in periods, prior-period adjustments

Onboarding is the highest-friction moment in any client relationship. A wizard that turns a 4-hour manual process into a 30-minute guided flow is itself a feature firms will pay for.

### FlashStandardize — bidirectional write-back to QBO

The platform's standardization layer doesn't just sit in Excel — it pushes back into QBO so the source data becomes uniform. What it does:

- **Vendor standardization across the firm's client base**: identifies vendors across all clients, AI-suggests firm-standard category (e.g., "Materials" / "Subcontractor"), on approval pushes the category back to each client's QBO vendor record. Every client's "Acme Hardware" becomes consistently categorized.
- **Account additions**: scans each client's CoA against the firm's standard, suggests missing accounts ("Add 'Tools & Equipment'?"), creates them in QBO with proper parent/type on approval. Additive only — doesn't modify existing accounts.
- **Bookkeeping rules push**: define a rule once ("Memo contains 'Stripe' → Merchant Fees"), push as a native QBO Rule to all relevant clients. Future transactions auto-categorize.
- **Class / Tag / Custom Field standardization**: firm decides on standard classes (e.g., for construction: "Direct / Indirect / Overhead"), push class lists into all relevant client QBOs.
- **Historical reclassification (optional, high-care)**: with reviewer approval and audit log, retroactively recategorize historical transactions to match the standard. Most firms won't do this by default; some will at engagement start.

**Why this is the strategic crown jewel**:

1. **Hard-dollar value**: eliminates the #1 cost in every accounting firm — bookkeeper time spent on categorization cleanup. Easy ROI math.
2. **Improves source data quality**: instead of the platform abstracting over messy QBO data, the data IN QBO gets cleaner. Every other tool benefits, not just Flash Reports.
3. **Creates a moat via standardization lock-in**: once a firm has standardized 30 clients via Flash Reports, switching to a competitor means restandardizing. High switch cost = customer retention.

**Engineering requirements**:

- QBO API write scope (different from read scope — user re-authorizes on first connect)
- Approval workflows: every push has a reviewer queue, dry-run preview, rollback option
- Audit log: every write captured (who, what, when, before/after) with permissions to query
- Per-client opt-in: some clients permit write-back, others don't
- Test mode: show exactly what would change before doing anything

**Risk mitigation**:

- Additive-only by default — only ADD new things (categories, accounts, rules, classes). Don't modify or delete existing without explicit per-action approval.
- All changes logged + reversible.
- Permission gates: only specific firm roles can authorize pushes.
- QBO native audit log captures all changes too — provides independent verification.

Estimated engineering: 4-6 weeks for core write infrastructure, plus 1-2 weeks per new push type (vendors, accounts, rules, classes, etc.). Total ~8-12 weeks for the full FlashStandardize app.

### FlashTax — book-to-tax bridge (already detailed)

See `FLASHTAX_HANDOFF.md` for the full technical specification. Summary: M-1 reconciliation per entity type, taxable income output, K-1 bridge to individual 1040.

### FlashPractice — multi-client roll-up

Practice-level dashboard watching a `/clients/` folder of Flash Reports outputs (or querying the platform's metadata layer directly). Power Query aggregates. Anomaly flags (revenue down >15% MoM, AR aging >60 days). Industry benchmarking via NAICS-coded entities. Practice KPIs (realization, utilization, fee/client). Workflow: "open one dashboard, see the whole book."

### FlashMetrics — computed metrics engine

Templates for advisory-grade calculations: LTV, CAC, LTV:CAC ratio, cohort retention, customer profitability with allocated overhead, gross margin by product line, project/job profitability, vendor concentration risk. Each one becomes a template that runs against the standardized data + snapshot vault. Build once, every client gets it. Refreshes automatically.

### FlashConsolidate — ownership-weighted multi-entity consolidation

Walks the ownership tree, applies full / equity / cost method based on ownership %, eliminates intercompany transactions, produces one consolidated P&L + BS for the entire client. Critical for family offices. Effective-dated ownership records so historical reports use period-correct percentages.

### FlashHealth — composite business health scorecard

Pulls every QBO dimension into one 0-100 health score with subscores (Liquidity, Profitability, Efficiency, Solvency, Growth, Customer Concentration, Vendor Concentration, AR Aging). Red/yellow/green flags. Refresh on Flash Reports recalc. "Which clients need attention this week?" workflow magnet.

### FlashSnapshot — milestone audit trail

User-facing interface to the platform's snapshot vault. Capture at workflow milestones (Extension, S1, As-Filed, Amended, Reviewed). Diff reports between snapshots. Workpaper-ready PDF export. PCAOB / SSARS-compliant. Opens audit firm market for Finatical.

### FlashDimensions — analytical layers beyond raw pull

Customer profitability, vendor analysis, project profitability, class/department trending, cohort retention, employee productivity, inventory turns + ABC classification. Flash Reports shows the P&L. FlashDimensions shows *what to do with it*.

### FlashLibrary — practitioner template marketplace

Practitioners publish custom analyses (construction WIP, SaaS ARR, law firm trust, cannabis 280E). Other practitioners install with one click. Models: free / paid (creator price + platform fee) / firm-private. Network effects play.

### FlashConnect — cross-system drill (longer horizon)

Drill from P&L line all the way to QBO transaction → customer card → CRM → email thread → meeting transcript → next scheduled call. Cross-system context aggregation. Long-term partnership play with CRM / communication tool vendors.

### FlashPersonal — individual financial dashboard (for HNW practitioner segment)

For tax practitioners serving owner-operators: connect to Plaid for personal bank/brokerage, track W-2 income, categorize personal transactions for Schedule A, track 1099 income through the year, year-round 1040 projection. Unifies the personal + business sides of the same household.

### FlashHousehold — unified business + personal view

Combines all entities a client owns + their individual accounts into one household view. Total income, total tax exposure, projected 1040. "If the S-Corp distributes $200K in November, what's the family tax impact?" live.

---

## WHO WINS

### Finatical wins
- Higher ARPU per practitioner (tax + advisory tiers above bookkeeping)
- Larger TAM (family offices, audit firms, wealth advisors — not just bookkeepers)
- Defensible moat (mapping data + practitioner templates + tax IP)
- Platform economics (apps from third parties = network effect)
- Sticky workflow (once a firm has standardized on the platform, they don't switch)

### Practitioners win
- 3-5 hours saved per client per month (already Finatical's tagline; the platform multiplies this)
- Cross-client visibility they don't have today
- Year-round tax tracking instead of filing-time scramble
- Advanced metrics (LTV, CAC, etc.) without one-off model building
- Audit defense built in

### Clients win (indirectly)
- Better-informed advisor → better business decisions
- More frequent touchpoints (monthly tax position vs. annual)
- Lower fees (advisor's time is spent on insight, not data wrangling)

---

## THE PITCH FRAME

For a meeting where the founder didn't get it the first time, the three-sentence version:

> **Flash Reports today is a great reporting tool — one workbook per client. The next product is the same tool turned into a platform: a thin metadata + snapshot service that lets a family of advisory-grade add-ons sit on top of one source of truth. That platform doesn't store any GL data — QBO already does, Flash Reports already queries it — but it adds the multi-client, multi-period, multi-source coherence that turns Finatical from a reporting tool into a practice operating system.**

Followed by the specific applications: tax bridge, multi-client roll-up, LTV/CAC engine, ownership-weighted consolidation, audit trail, template marketplace.

If the conversation can hold one more idea, the immediate-value ask: **granular snapshots** in Flash Reports as a 2-3 week engineering effort that unlocks half the workflows above.

---

## WHAT THIS MEMO IS NOT

- Not a feature request list. The platform IS the feature.
- Not a tactical roadmap with deadlines. Phases are sketched for direction, not committed.
- Not a finished technical spec. Architecture is described at the right level for a strategic conversation; implementation details would follow if there's alignment.
- Not asking Finatical to build everything. Some apps are co-developable with domain experts (Seth for tax). Some are marketplace candidates. Finatical's core build is the platform layer.

---

## NEXT ACTIONS

1. **For Finatical**: read this memo. If the platform vision resonates, talk about Phase 1 (granular snapshots) as the immediate win and Phase 2 (FlashCore platform layer) as the strategic bet.
2. **For Seth**: the FlashTax prototype (Phase 3, first app on the platform) is in build. It demonstrates the architecture works and opens the tax practitioner segment.
3. **For the broader conversation**: this is a 12-18 month strategic vision, not a quarter's roadmap. Pacing depends on Finatical's team capacity and appetite.

---

## RELATED REPO DOCUMENTS

- `docs/FLASHTAX_HANDOFF.md` — technical handoff for the FlashTax prototype build (Phase 3 app)
- `docs/REMAINING_EXCEL_WORK.md` — punch list for the 1040 framework that FlashTax connects to
- `Master_Pivot_Framework_v5_phase3v24_CC.xlsx` — the existing 1040 calc engine that FlashTax bridges into for K-1 → individual tax flow

---

**END OF MEMO**

*Comprehensive: covers the full architecture brainstorm. Designed to be re-readable by a non-technical reader who needs to grasp the strategic vision, and detail-complete enough that a technical reader can follow up with implementation questions.*
