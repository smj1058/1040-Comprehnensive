# Finatical / Flash Reports — Founder Meeting Handoff

> Comprehensive handoff covering the full brainstorm arc — from initial FlashTax concept through to the final platform architecture. Self-contained brief for any Claude Code session picking this up, OR for Seth's own reference walking into the founder meeting.
>
> **Repo**: `smj1058/1040-Comprehnensive`
> **Branch**: `claude/pivot-tax-calculations-q4NyZ`
> **User**: Seth Johnson (seth@accruity.com)
> **Context**: Seth has Flash Reports installed, is meeting with the founder, expected to come with ideas + a working prototype demonstrating value.

---

## 1. EXECUTIVE SUMMARY — what to walk into the meeting with

**The pitch in one sentence**:

> "Flash Reports is the live query layer for QBO. The missing piece is a thin metadata + snapshot service that turns Flash Reports into a multi-client, multi-period, audit-defensible **platform**. That service is small — it doesn't store any GL data — but it's the keystone that makes a whole family of add-ons possible. I've sketched the platform and built the first app (FlashTax) to prove the architecture."

**What Seth brings to the meeting**:

1. **A working FlashTax prototype** (the wedge — first app on the platform)
2. **A platform architecture sketch** (FlashCore — the layer Flash Reports needs next)
3. **A product family roadmap** (8 add-on concepts that ride on FlashCore)
4. **One specific Flash Reports product-feedback ask** — granular snapshots (covered in Section 6)

**Why this lands**: Seth isn't asking the founder to add a feature. He's showing the founder how Finatical becomes the iOS of accounting Excel — a platform other people build on.

---

## 2. WHAT FLASH REPORTS DOES (the host product)

### Core capabilities
- **Excel add-in for QuickBooks Online** — pulls live QBO data via formulas like `=FR.PL("Revenue", ClientID, Year, Period)` (exact syntax TBD when Seth shares examples)
- **Multi-entity** — connects to unlimited QBO subscriptions, consolidates at the entity level
- **Formula-driven refresh** — change a control cell (ClientID / Year / Period) → entire workbook recalcs → see different client's data. No manual refresh button.
- **Drill-down** — click a cell, see the underlying QBO transactions
- **Snapshot** — converts formulas to static values to freeze a point in time. Currently **workbook-wide only** (this is a limitation — see Section 6)
- **Reporting Pack** (March 2026 release) — branded multi-section workbooks with cover, index, narrative, multiple report tabs
- **Claude in Excel integration** (March 2026 release) — Claude can read cells, explain variances, with cell-level citations

### Why formula-driven is the foundation
Because formulas + drill-down already exist, **most of what we'd otherwise have to build for a multi-client database is already done by Flash Reports**. The hard parts (QBO auth, API client, ETL, account normalization, drill paths) are handled. What's left to build is much smaller than it first appeared.

### Sources
- https://quickbooks.intuit.com/app/apps/appdetails/flashreports/
- https://finaticalsoftware.com/
- https://www.prnewswire.com/news-releases/finatical-software-launches-reporting-pack-and-integrates-claude-in-excel-302712247.html
- https://support.claude.com/en/articles/12650343-use-claude-for-excel

---

## 3. THE BRAINSTORM ARC — how the thinking evolved

The discussion went through five reframes. Each one made the architecture simpler and the pitch stronger:

### Reframe 1: "Build FlashTax — a tax add-on"
First idea was a tax-specific add-on (book-to-tax M-1 bridge + K-1 to 1040 connection). Strong because tax is Seth's expertise and high-ARPU. But too narrow as a standalone pitch.

### Reframe 2: "FlashTax is one of several add-ons"
Brainstormed eight add-on concepts (Tax, Practice, Snapshot, Consolidate, Taxonomy, Health, Dimensions, Library, Connect). Each individually compelling. But still a feature pitch.

### Reframe 3: "Platform, not features"
The eight add-ons share a common need — they all want multi-client, multi-period, drill-down-preserving access to financial data. That's a **platform layer**, not a feature. Pitching the platform changes the conversation from "add this feature" to "build this category."

### Reframe 4: "Flash Reports does most of the platform already"
The formula-driven nature of Flash Reports means we don't need to build a transactional warehouse. Live data flows through `=FR.<func>(...)` calls on demand. The "database" we sketched shrinks from millions of rows to thousands.

### Reframe 5: "Templates + central snapshot vault — no GL storage at all"
Snapshots shouldn't live inside workbooks. They should live in a centralized vault, and templates query EITHER Flash Reports (live) OR the vault (frozen). This breakthrough means we don't store any GL data anywhere. Just metadata + a snapshot vault.

**Final architecture is the result of these five reframes.**

---

## 4. THE FINAL ARCHITECTURE — FlashCore + apps

```
┌──────────────────────────────────────────────────────────────────┐
│                            QBO                                    │
│              (system of record for transactions)                  │
└─────────────────────────────┬────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                       FLASH REPORTS                               │
│        (formula-driven live query layer to QBO in Excel)         │
│                Already exists. Owned by Finatical.                │
└─────────────────────────────┬────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                          FLASHCORE                                │
│             (the platform layer — what's missing today)          │
│                                                                   │
│  ┌────────────────────┐    ┌─────────────────────────────────┐   │
│  │ METADATA SERVICE   │    │ SNAPSHOT VAULT                  │   │
│  │ - Firms / Clients  │    │ - Frozen milestone states       │   │
│  │ - Entities         │    │ - As-Filed / Extension / S1 /   │   │
│  │ - Ownership %      │    │   Amended / Reviewed            │   │
│  │ - Standard CoA     │    │ - Queryable by date + scope     │   │
│  │ - Account mappings │    │ - One source of truth for       │   │
│  │ - Periods          │    │   "what we knew when"           │   │
│  │ - Tax line codings │    │                                 │   │
│  └────────────────────┘    └─────────────────────────────────┘   │
│                                                                   │
│  Total storage: thousands of rows of metadata + bounded growth   │
│  in snapshots. Fits in one Excel file for years.                 │
└─────────────────────────────┬────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                       APPLICATIONS                                │
│             (templates that consume FlashCore + Flash Reports)    │
│                                                                   │
│  FlashTax       — book-to-tax bridge, K-1 to 1040                │
│  FlashHealth    — composite business health scorecard            │
│  FlashPractice  — multi-client roll-up dashboards                │
│  FlashConsolidate — ownership-weighted multi-entity consolidation │
│  FlashSnapshot  — milestone audit trail UI                       │
│  FlashTaxonomy  — standardized CoA + mapping engine              │
│  FlashDimensions — customer / vendor / cohort analytics          │
│  FlashLibrary   — practitioner template marketplace              │
│  FlashConnect   — cross-system drill (CRM, email, meetings)      │
│                                                                   │
│  Each app = thin Excel workbook with templates that read from    │
│  FlashCore + Flash Reports. No app stores GL data.               │
└──────────────────────────────────────────────────────────────────┘
```

### The single biggest insight: no GL storage

**You do not store transactions. You do not store P&L history. You do not store BS history.** All of that lives in QBO. Flash Reports queries it on demand via formulas.

You ONLY store:

| What | Why | Approximate size |
|---|---|---|
| **Metadata** | Defines structure (clients, entities, ownership, mappings) | ~1,000 rows per 30-client firm |
| **Snapshots** | Frozen point-in-time captures at milestones | ~5-10K rows per client per year |
| **Templates** | Layout + formulas — zero data | KB, not MB |

The entire "Master DB" fits comfortably in **one Excel file** for years. No SQL Server. No data warehouse. No ETL pipelines.

### Template + snapshot vault pattern

Every cell in every template uses a routing formula:

```excel
=IF(SnapshotMode="Live",
    FR.PL("Revenue", ClientID, Year, Period),
    INDEX(tblSnapshots[Value], MATCH(...)))
```

Or wrapped in a custom function:

```excel
=GetValue("Revenue", ClientID, EntityID, Year, Period, SnapshotMode)
```

Where `SnapshotMode` is a control cell: `"Live"` / `"AsOf_2025-04-15"` / `"AsFiled_2024"` / etc.

**Same template. Different lens.** Change one cell → see live data, or any historical snapshot.

This eliminates the workbook-embedded-snapshot problem completely. All snapshots live in one queryable vault. Workbooks stay pure view layer.

---

## 5. THE APPS — what rides on FlashCore

### 5.1 FlashTax — book-to-tax bridge (the prototype)

**What it does**: Sits next to Flash Reports in the same workbook. Reads P&L / BS cells, computes Schedule M-1 reconciliation per entity type, outputs taxable income, bridges K-1s to individual 1040s.

**Why it's first**: Seth's expertise lives here. Tax IP is harder to replicate than reporting templates. High-ARPU practitioner segment. Demonstrates FlashCore architecture works.

**Sheet structure**:
- Cover (branded title page with selectors visible)
- Control_Panel (ClientID / EntityID / EntityType / Year / Period / SnapshotMode)
- PL_Live (cells calling Flash Reports formulas — placeholders until Seth pastes real syntax)
- BS_Live (same)
- M1_Reconciliation (book net income → adds → subs → taxable income; categories below)
- TaxableIncome_Output (entity taxable income per type — 1120S / 1120 / 1065 / Sch C)
- K1_Bridge (pass-through distribution to owner's 1040)
- Claude_Prompts (5-7 ready-to-paste prompts)
- TaxRef_M1 (citation reference)
- Settings (toggles)

**M-1 categories to include**: Federal tax expense, state tax expense (PTET-aware), depreciation difference (DDA), §263A, meals (50%), entertainment (100%), political contributions, fines & penalties, tax-exempt interest, life insurance proceeds, §179 depreciation, bonus §168(k), accrued comp not paid in 2.5mo, bad debt reserve, charitable >10% AGI (corp), NOL carryforward, tax credits.

**K-1 Bridge output**: For each owner of a pass-through entity — `(OwnerID, EntityID, Year, Share_Ordinary, Share_CG, Share_QBI, Share_§199A_W2, Share_UBIA)` ready to land in owner's 1040 Master_Inputs as new rows.

**The 1040 framework already in this repo** (`Master_Pivot_Framework_v5_phase3v24_CC.xlsx`) is the receiving system for K-1 outputs.

### 5.2 FlashHealth — composite business health scorecard

**What it does**: Pulls every dimension QBO tracks into one 0-100 health score with subscores across Liquidity, Profitability, Efficiency, Solvency, Growth, Customer Concentration, Vendor Concentration, Receivables Aging. Red/yellow/green sub-flags. Refresh on Flash Reports recalc.

**Why it matters**: Finagraph already does business health scoring as a separate product. Finatical adding it in-workbook removes a competitor. Workflow magnet — "which clients need attention this week?"

### 5.3 FlashPractice — multi-client roll-up

**What it does**: Practice-level dashboard watching a `/clients/` folder of Flash Reports outputs. Power Query aggregates. Anomaly flags (revenue down >15% MoM, AR aging >60 days, ratio thresholds). Industry benchmarking using NAICS-coded entities.

**Why it matters**: Removes the single-client constraint that limits Finatical's sales to mid-size firms. Practice-level views are the missing piece for firm-wide buyers.

### 5.4 FlashSnapshot — milestone audit trail

**What it does**: User-facing interface to the FlashCore snapshot vault. Captures snapshots at workflow milestones (Extension, S1, As-Filed, Amended, Reviewed). Diff reports between snapshots. Workpaper-ready PDF export. PCAOB / SSARS-compliant output.

**Why it matters**: Opens the audit firm market for Finatical (large TAM). Compliance + audit defense is a wedge into firms that don't currently care about reporting tools.

### 5.5 FlashConsolidate — ownership-weighted multi-entity consolidation

**What it does**: Walks the ownership tree, applies full/equity/cost method based on ownership %, eliminates intercompany transactions, produces one consolidated P&L + BS for the entire client.

**Why it matters**: Family offices and multi-entity clients currently pay separately for this. Automating it is a major revenue unlock for Finatical.

### 5.6 FlashTaxonomy — standardized CoA + mapping engine

**What it does**: Master standardized CoA (~200-400 normalized accounts). Per-entity mapping table (LocalAccountName → StandardAccountID). AI-assisted mapping suggestions on client onboarding. Multiple groupings (GAAP / Tax / Mgmt / Lender / Industry / Audit).

**Why it matters**: Highest-effort phase but deepest moat. Once mapped, every report / consolidation / benchmark just works. Mapping data is hard to replicate.

### 5.7 FlashDimensions — analytical layers beyond raw pull

**What it does**: Customer profitability (revenue × margin per customer with allocated overhead), vendor concentration risk, project / job profitability, class / department P&L over time, cohort retention, employee productivity, inventory turns + ABC classification.

**Why it matters**: Flash Reports today shows the P&L. FlashDimensions shows *what to do with it*. Different value prop, justifies higher price tier.

### 5.8 FlashLibrary — practitioner template marketplace

**What it does**: Practitioners build custom analyses (construction WIP, SaaS ARR waterfall, law firm trust accounting, cannabis 280E carve-out). Publish to marketplace. Other practitioners install with one click. Models: free / paid (creator price + Finatical platform fee) / firm-private.

**Why it matters**: Network effects. Once practitioners have built and shared, they don't switch tools. This is the moat play.

### 5.9 FlashConnect — cross-system drill

**What it does**: Drill from P&L line all the way to QBO transaction → customer card → CRM (HubSpot/Salesforce) → last email thread → last meeting transcript → next scheduled call.

**Why it matters**: Cross-system context aggregation. Same dollar of revenue, with the why and what's-next attached. Long-term partnership play.

---

## 6. PRODUCT FEEDBACK FOR THE FOUNDER — granular snapshots

Beyond the platform pitch, there's one concrete piece of feedback that's worth raising directly:

**Current Flash Reports snapshot is workbook-wide.** That's too coarse. It breaks every actual practitioner workflow:
- Rolling quarter close (Q1 freeze, Q2-Q4 stay live)
- As-Filed vs Working (one sheet frozen, others live)
- Projection vs Actual (Q1 projection snapshotted in February, Q1 actual stays live, variance sheet compares)
- Audit defense (multiple "as of" snapshots in one file)

**Recommended granularity levels**: Workbook (current), Sheet, Column, Row, Named Range, Cell list.

**Most impactful additions**: Column (handles rolling close) and Named Range (handles everything else cleanly).

**Implementation sketch**: User selects scope → snapshot converts formulas → values within that scope only → cells outside scope unchanged → hidden marker records the original formula for "un-snapshot" → Snapshot Manager pane shows all snapshots with timestamp, label, scope.

**This is great founder-meeting feedback** because it's specific, actionable, immediately understandable, and shows Seth has actually used the product in workflow.

**Better long-term answer**: implement FlashCore's central snapshot vault instead of (or in addition to) workbook-embedded granular snapshots. Templates query the vault. Workbooks stay pure view. That's the architectural fix; granular snapshot is the immediate fix.

---

## 7. WHAT'S ALREADY BUILT IN THIS REPO

The 1040 framework. `Master_Pivot_Framework_v5_phase3v24_CC.xlsx` (latest CC version) is the proof of concept for the long-format / pivot-driven architecture that FlashCore would generalize.

Already built and applicable to the FlashCore platform:

- **Long-format Master_Inputs schema** — the template for FlashCore's metadata + snapshot tables
- **Standardized account / treatment profile mapping** (Tax_Ref tblTreatmentProfileMap) — the template for FlashTaxonomy
- **Master_Strategies catalog with multi-impact fan-out** — the pattern for storing strategy/event impacts
- **Per-year calc engine** — the pattern for period-by-period calculation
- **State tax stack with PTET routing** — applicable to FlashTax M-1 PTET logic
- **6 LAMBDAs + fn_StrategyMarginal** — the calc engine (TAX_ORD / TAX_CG / TAX_NIIT / TAX_SE / STD_DED / TAX_STATE). FlashTax imports these directly.
- **QBI bug fix** — J119/K119 (50% W-2 limit, not 20%)

See `docs/REMAINING_EXCEL_WORK.md` for the punch-list to finish the 1040 workbook.

---

## 8. BUILD SEQUENCE FOR THE PROTOTYPE

Phase A — FlashTax MVP (what to build for the meeting):

1. **Scope confirm with Seth**:
   - Actual Flash Reports formula syntax (`=FR.PL`, `=FLASH.GET`, etc.)
   - Entity types to support (just 1120S or full set)
   - Sample client to demo with
   - Meeting timeline
2. **Build FlashTax_Prototype_v1_CC.xlsx**:
   - 10 sheets per Section 5.1 above
   - Yellow-fill placeholder cells for Flash Reports formulas (Seth pastes real syntax)
   - Working M-1 reconciliation logic
   - K-1 Bridge for single-owner case
   - 5-7 pre-loaded Claude prompts
3. **Cover sheet = one-page pitch** (pitch text in Section 1 of this doc)
4. **Optional**: build a tiny `FlashCore_Sketch.xlsx` showing the metadata + snapshot vault tables with sample data — visual aid for the platform conversation

Phase B onward (post-meeting, depending on founder response): K-1 bridge polish, FlashCore service, additional apps.

---

## 9. OPEN QUESTIONS FOR SETH BEFORE BUILDING

1. What's the actual Flash Reports function name? (`=FR.PL`, `=FRGET`, `=FLASH.GET`, other?)
2. Entity types for the prototype — just 1120S, or full set (1120 / 1120S / 1065 / SchC)?
3. Sample client to demo with — Cedillo or a real Flash Reports demo client?
4. K-1 Bridge output — to a file importing into `Master_Pivot_Framework_v5_phase3v24_CC.xlsx`, or just show what output would look like?
5. When is the founder meeting? (Affects polish vs. speed tradeoff.)
6. Want a separate `FlashCore_Sketch.xlsx` visual aid alongside FlashTax_Prototype?

---

## 10. PITCH FRAMING FOR THE FOUNDER

### Three-tier pitch structure

| Tier | Concepts | One-line pitch |
|---|---|---|
| **Wedge (today)** | FlashTax | "The prototype I brought today — the tax bridge that turns Flash Reports into a tax-ready close" |
| **Platform (the unlock)** | FlashCore (metadata + snapshot vault) | "The thin service layer that lets a family of add-ons share one source of truth — without storing any GL data" |
| **Apps (what becomes possible)** | Health / Practice / Snapshot / Consolidate / Taxonomy / Dimensions / Library / Connect | "Every one of these is an app on FlashCore. Build the platform; the apps come naturally" |

### The platform speech (one paragraph)

> "Flash Reports is the live query layer for QBO. That solves one problem. The next problems are: bridging that data to tax, seeing across all my clients at once, freezing history for audit defense, consolidating multi-entity families, and standardizing the chart so all of the above scale. I don't think you need to build all of these. But you DO need one thing — a thin metadata + snapshot service that turns Flash Reports into a multi-client, multi-period platform. That service is small — it doesn't store any GL data, just metadata and milestone snapshots — but it's the keystone every add-on needs. I've sketched it and built FlashTax to prove the architecture. Build the service, and you turn Finatical from a reporting tool into a platform that other people build apps on."

### The granular-snapshot ask (one paragraph)

> "Separately — one specific product ask. Your current snapshot is workbook-wide. In actual workflow that's too coarse. Quarter close needs column-level snapshot. Comparing projection-vs-actual needs sheet-level. Audit defense needs multiple "as of" states in one file. Long-term answer is the centralized snapshot vault I just described — but in the meantime, expanding snapshot to column/sheet/named-range scope is high-value with manageable engineering. Two to three weeks of work, opens a lot of workflows."

---

## 11. WHAT NOT TO DO

- **Don't modify** the 1040 workbook in this repo. FlashTax is a separate workbook.
- **Don't assume Flash Reports formula syntax** — use yellow-fill placeholders, Seth pastes real syntax during the meeting.
- **Don't build the full database**. The whole point of the brainstorm is that you DON'T need to. Build metadata + snapshot vault only when needed for the demo.
- **Don't bake LAMBDA syntax via openpyxl** — Excel rejected our openpyxl-written LAMBDAs in the 1040 workbook. Install LAMBDAs natively in Excel during the build, not programmatically.
- **Don't add macros that auto-run on open** — Excel security will fight you. Button-triggered only.
- **Don't claim the platform exists when it doesn't yet** — FlashCore is the proposed centerpiece, but FlashTax is the only actually-built piece. Be honest about which is which in the founder conversation.

---

## 12. REPO + NAMING CONVENTIONS

```
/home/user/1040-Comprehnensive/
├── docs/
│   ├── Master_Pivot_Framework_v5_phase3v24_CC.xlsx     ← 1040 workbook (latest CC)
│   ├── REMAINING_EXCEL_WORK.md                          ← Excel-side todo for 1040
│   ├── FLASHTAX_HANDOFF.md                              ← THIS FILE (comprehensive)
│   └── EXCEL_PROMPT_*.md                                ← misc handoff prompts
├── scripts/
│   └── phase3v*_*.py                                    ← openpyxl build scripts (1040)
└── CLAUDE.md                                            ← project instructions
```

### Naming convention

| Suffix | Meaning |
|---|---|
| `_CC` | File built by Claude via openpyxl |
| `_SJ` | File built / edited by Seth in Excel |
| `v{N}` | Iteration version |

Examples:
- `FlashTax_Prototype_v1_CC.xlsx` — Claude-built initial prototype
- `FlashTax_Prototype_v1_SJ.xlsx` — Seth's hand-edited polish
- `FlashCore_Sketch_v1_CC.xlsx` — optional platform visual aid

### Repo + GitHub scope

- GitHub: `smj1058/1040-Comprehnensive`
- Restricted scope: this repo only
- Working branch: `claude/pivot-tax-calculations-q4NyZ` or new branch per session

### Local MCP project folder (Seth's machine)

Seth maintains a local copy of all Flash Reports / FlashTax work at:

```
C:\Users\SethJohnson\MCP_Projects\flash-tax\
```

This is where the work lives between cloud sessions — Seth's working area, separate from the cloud container. If a Claude Code CLI session runs against this folder locally (not via the web), this is the path. Files travel between the repo and this folder by manual copy or git pull/push.

**Source-of-truth resolution**: when in doubt, the most recently updated location wins. If Seth edits locally after a session ends, that supersedes the repo. If a new cloud session updates the repo, that supersedes the local copy. Sync manually as needed.

---

## 13. QUICK-START PROMPT FOR THE NEW SESSION

> Paste this at the top of a fresh Claude Code session (in this repo or in your local MCP_Projects setup):

```
Read docs/FLASHTAX_HANDOFF.md fully. That's the brief. The architecture
arc and platform reframe in Sections 3-4 are the keystone — don't skip
them.

Then ask Seth the 6 open questions in Section 9 before building. Once
answered, work through the build sequence in Section 8.

Deliver as FlashTax_Prototype_v1_CC.xlsx on a new branch
claude/flashtax-prototype-{your-suffix}. Commit + push at the end.
Use SendUserFile to deliver the file inline.

If Seth wants a FlashCore visual aid alongside FlashTax, build
FlashCore_Sketch_v1_CC.xlsx — a small file showing the metadata +
snapshot vault schema with sample data. Not full-featured, just a
visualization for the founder conversation.

Do NOT modify Master_Pivot_Framework_v5_phase3v24_CC.xlsx or anything
else in this repo's existing 1040 workbook.

Section 5 lists 9 follow-on apps. Don't build them in this session,
but be aware so design choices in FlashTax don't paint into a corner.

Section 11 is the do-not-list. Read it before any build action.
```

---

## 14. STATE OF THE BRAINSTORM AS OF HANDOFF

What's been talked through and locked:

✓ Flash Reports is the live query layer (formula-driven, drill-down, multi-entity)
✓ Claude in Excel integration exists (March 2026 release)
✓ FlashTax is the wedge product (tax angle is Seth's expertise)
✓ Eight other add-on concepts identified (Health, Practice, Snapshot, Consolidate, Taxonomy, Dimensions, Library, Connect)
✓ The architecture is a **platform**, not a feature collection
✓ The platform layer (FlashCore) is **metadata + snapshot vault only** — no GL storage
✓ Templates query Flash Reports (live) OR snapshot vault (frozen) via routing function
✓ Granular snapshot is a specific Flash Reports product-feedback ask
✓ All of this fits in Excel — no SQL Server, no data warehouse needed

What's NOT yet locked:

- Exact Flash Reports formula syntax (Seth has, will share)
- Sample client / entity for the prototype demo
- Meeting timeline
- Whether to build FlashCore_Sketch alongside FlashTax_Prototype
- Pricing model thoughts (mentioned in passing for FlashTax — $50-100/month/practitioner — not validated)

What's deferred to post-meeting:

- Actually building any of the 8 follow-on apps
- The FlashCore service implementation beyond a sketch
- Power Query / VBA orchestration of the multi-client refresh + snapshot loop
- Practitioner template marketplace mechanics

---

## END OF HANDOFF

Total tokens of context captured: 30+ minutes of architecture brainstorm distilled into a self-contained reference document.

Next action: Seth confirms the open questions in Section 9, then a Claude Code session builds the FlashTax prototype + optional FlashCore sketch.
