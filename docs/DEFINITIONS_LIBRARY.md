# Definitions Library — Headers, Naming & Database Framing

**The single lookup reference for the ExecSumm-Dossiers pipeline.** When you're
building or reading a dossier, an executive summary, a correspondence/email
record, a meeting record, a tax-planning workbook, or a tax-planning strategy
table — *this* file defines every header, every property, every status symbol,
and every source tag you'll encounter, plus how files should be named and how
everything is wired into the Notion databases so it can be searched and looked
up later.

> **TL;DR on your core question — "does it matter how the files are saved, as
> long as the headers are there?"**
> Both matter, but they do *different jobs*. Two things make the system
> searchable: (1) the **structured headers/sections inside each file** (the
> `## §N` skeleton + inline source tags) and (2) the **Notion database row +
> its properties** that points at the file. The **filename** is the third,
> weakest axis — it matters for human/Drive browsing and for the dated
> living-document rule, but it is **not** what the system searches on. So:
> *get the headers and the DB properties right first; the filename is a
> convenience layer on top.* See §1 for the full model.

---

## §1. The findability model — three lookup axes

Everything in this project is findable along three independent axes. Get all
three consistent and a fact is retrievable from any direction.

| Axis | What it is | What it's good for | Authority |
| --- | --- | --- | --- |
| **A — Headers & sections** (inside the `.md`) | The `## §0`–`## §13` skeleton + sub-headers + inline `[source]` tags | Full-text search, jumping to a section anchor, machine parsing, provenance | **Primary.** This is the real index. A fact lives under a known header with a known tag. |
| **B — Notion DB row + properties** | The Executive Summaries row + its `📄/📧/🎙/⚡/📁/🤖` URL properties + `Summary`, `Summary Type`, `Tax Engagement Type`, `Last Synthesized`, etc. | Filtering, sorting, dashboards, "show me all clients with X engagement type", cross-linking to Accounts/Meetings/EL/F&L | **Pointer-of-record.** The row is how a human or automation *finds* the file; it does not duplicate the body. |
| **C — Filename + folder path** | `<Client>_Client_Intelligence_<YYYY-MM-DD>.md` in `dossiers/<ClientFolderNoSpaces>/` and on Drive | Human browsing, the dated living-document trail, offline fallback | **Convenience.** Reconstructable from Axis B. Helpful, not load-bearing for search. |

### What this means in practice

- **If you only fix one thing, fix the headers (Axis A).** A file with the
  correct `## §N` headers and source tags is fully searchable even if the
  filename is wrong, because search hits the section text and the Notion row
  points at it.
- **The filename is not how the system looks things up** — but it *is* how the
  dated history is preserved (`..._2026-04-22.md`, `..._2026-06-01.md` side by
  side) and how a human scanning Drive recognizes a file. Keep the convention
  (§2) so the trail stays legible, but don't treat a perfect filename as a
  substitute for correct headers.
- **The Notion row (Axis B) is the bridge.** It carries the `📄 Dossier` URL
  that resolves a client to the current file, and its properties are what
  dashboards/filters key off. The body of the dossier is *never* copied into
  the Notion row — pointer-only (see Hard Rule #7 in `CLAUDE.md`).

**Rule of thumb:** structured headers + DB properties = how it's *found*;
filename = how it's *recognized and dated*. Optimize the first two; keep the
third tidy.

---

## §2. File naming & folder conventions

### 2.1 Canonical filenames

| Artifact | Canonical name | Where |
| --- | --- | --- |
| **Dossier — Drive deliverable** | `<ClientNameNoSpaces>_Client_Intelligence_<YYYY-MM-DD>.md` | `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\` |
| **Dossier — repo mirror** | `dossier.md` | `dossiers/<ClientFolderNoSpaces>/` |
| **Dossier — HTML render** | `dossier.html` | `dossiers/<ClientFolderNoSpaces>/` |
| **Per-client state** | `state.json` | `dossiers/<ClientFolderNoSpaces>/` |
| **Run-level handoff** | `HANDOFF_<YYYY-MM-DD>.md` | `docs/` |

### 2.2 The rules behind the names

- **`<ClientNameNoSpaces>`** — strip spaces and punctuation; join joint
  households with both names (e.g. `MattAndChelseaIannaccio`,
  `ReneeMuellerJeffCohn`, `DavidMichelleSaward`). The repo folder uses the same
  token: `dossiers/MattAndChelseaIannaccio/`.
- **`<YYYY-MM-DD>`** = the refresh date, ISO 8601. Always sortable, always
  unambiguous.
- **Prior dated files are retained forever.** Each refresh writes a *new* dated
  file on Drive; the old ones stay. That dated trail is the visible history of
  how the narrative evolved — never overwrite or delete a prior dated file.
- **The repo mirror keeps a single rolling `dossier.md`** (the living document);
  git history is its version trail. Drive keeps the dated snapshots.
- One client = one folder = disjoint paths, so parallel agents never collide.

### 2.3 Why the date is in the filename but not the search key

The date suffix exists so the Drive folder reads as a chronological stack. The
*current* version is always resolvable through the Notion row's `📄 Dossier`
property (Axis B) or by taking the newest date in the folder — you never search
*for* a file by guessing its name. So a missing or slightly-off date in a
filename degrades the human trail but does not break lookup.

---

## §3. Dossier header taxonomy (§0–§13)

Every dossier follows one skeleton. The headers are the contract — same `## §N`
markers, same order, every client. Sparse-mode dossiers compress empty sections
to a one-line gap flag; full-depth dossiers expand each with tables and
narrative. **The headers are present even when the section is thin** — that's
what keeps every dossier searchable the same way.

### 3.1 §0 — Header block (the file's "front matter")

The top of every dossier is a two-column `| Item | Detail |` table. These are
the fields, defined:

| Field | Definition |
| --- | --- |
| **Client** | Display name(s) + filing posture, e.g. `Spring Bengtzen + Brian Charlesworth (MFJ household)`. |
| **Client #** | Accruity client number from the Accounts record (e.g. `19070214-01`). |
| **Mango Client ID** | The numeric ID in Mango practice-management (e.g. `937753`); also the ImagineTime workspace key. |
| **Prepared by** | Always `Accruity Tax Advisory`. |
| **Date** | Refresh date (matches the filename date). |
| **Prior Refresh** | `first run` or the previous refresh's date. |
| **Planning Year(s)** | Tax years in scope (e.g. `2024 / 2025 / 2026`). |
| **Engagement Stage** | Where the client sits in the service lifecycle (e.g. `Tax Ascend — Planning + Compliance + Advisory`). |
| **Temperature** | Relationship/risk read (e.g. `Active & engaged (High risk on compliance track)`). |
| **Relationship Manager** | The Accruity RM (from the Account). |
| **Primary Contact** | Name(s) + email(s). |
| **Data Sources (this refresh)** | The Notion DBs / subpages consulted this run. |
| **Files Read This Refresh** | Concrete records opened (with short page-ID tails). |
| **Files NOT Accessible This Refresh** | Workbooks/links that were missing or unlinked — the gap list that drives next-refresh backfill. |

Two footer lines under the table set the legend used everywhere below:
- **`Confidence:` `✓ Confirmed · ~ Estimated · ? Pending`**
- **`Attribution:` every non-obvious fact carries an inline source tag → §12.**

### 3.2 §1–§13 — Section definitions

| § | Header | What goes here | Update rule |
| --- | --- | --- | --- |
| **§1** | Executive Overview | The TL;DR narrative; the `Summary` property in Notion is pulled from here | **Amended** (dated block above prior) |
| **§2** | Client Profile | Principals at a glance · Entity stack · Third parties in the file | **In-place** (annotate `(was…→…)`) |
| **§3** | Email Intelligence | 3.1 Active Threads · 3.2 Noise (filtered) · 3.3 Thread Rollup · 3.4 Gaps | **Append-only** |
| **§4** | Meeting History | 4.1 Chronological log · 4.2 Meeting-by-meeting detail · 4.3 Referenced-but-not-tracked · 4.4 Rollup · 4.5 Gaps | **Append-only** |
| **§5** | Document Inventory | 5.1 Engagement Letters · 5.2 Files & Links rows · 5.3 External platforms · 5.4 Files still missing · 5.5 Rollup | **In-place** |
| **§6** | Claude Work Product | 6.1 Prior sessions tied to account · 6.2 Passing mentions · 6.3 This refresh log row · 6.4 Cross-stream notes · 6.5 Gaps | **Append-only** |
| **§7** | Action Items — Rolled Up | 7.1 Master table · 7.2 Owner rollup · 7.3 Source count · 7.4 Gaps. Rolled up across email + Advisory issues + Meeting Action Items + Engagement Inquiries + Service/Intake Requests + dossier-gen flags | **In-place** |
| **§8** | Tax Strategies & Projected Savings | 8.1 Strategy table · 8.2 Projected savings rollup · 8.3 Gaps | **In-place** |
| **§9** | Opportunity Flags (auto-detected) | 9.1 Cost Segregation Candidates · 9.2 S-Corp Election Candidates · 9.3 Classifier coverage · 9.4 Gaps. Rule-based from `execsumm_emails/opportunity_flags.py` | **In-place** |
| **§10** | Operations Analysis | Per-principal operating footprint · joint/household ops · referral/brand context | **Amended** |
| **§11** | Individual Profile(s) | One `### 11.x <Name>` sub-block per principal | **Amended** |
| **§12** | Provenance Index | Every inline source tag → its canonical URL (see §6 of this library) | Rebuilt each refresh |
| **§13** | Changed Since Last Refresh | Dated delta block at top · carry-over summary · "what to look at first next time" | **Append** (new dated block above prior) |

The four update rules (Append-only / In-place / Amended / Rebuilt) are the
living-document mechanics — full detail in `CLAUDE.md` "Hard rules" and
`docs/PROJECT_OVERVIEW.md` §4.

---

## §4. Database & artifact property dictionaries

This is the header set for each *non-dossier* artifact — the Notion DB rows and
the trackers. These are the properties you filter, sort, and look up on.

### 4.1 Executive Summaries DB (the pointer-of-record)

DB `20f69b74-b140-4c3c-8041-ba71e7792478` · data source
`collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b`. One row per client; the
**body stays empty** (pointer-only model). Properties populated on Turn 11:

| Property | Definition |
| --- | --- |
| **Summary** | TL;DR pulled from dossier §1 (≤3000 chars). |
| **Summary Type** | The lens of the row: `General` · `Advisory` · `Tax Planning` · `Tax Planning Memo` (some clients have multiple rows, one per lens — amend, don't duplicate). |
| **Tax Engagement Type** | The engagement classification (e.g. Planning / Compliance / Advisory). |
| **Reporting Entity** | Relation to the Reporting Entities DB. |
| **Last Synthesized** (date) | `start` = the refresh date. The freshness signal. |
| **📄 Dossier** | URL → the dossier file (Drive deliverable, or repo blob). **The canonical pointer.** |
| **📧** | URL → §3 Email Intelligence (same file, section anchor where supported). |
| **🎙** | URL → §4 Meeting History. |
| **⚡** | URL → §7/§8 Action Items / Strategies. |
| **📁** | URL → §5 Document Inventory. |
| **🤖** | URL → §6 Claude Work Product. |

> The five emoji URL properties all resolve to the *same* dossier file, each
> with the section anchor for its stream where the host supports anchors. They
> are convenience deep-links, not separate documents.

### 4.2 Correspondence — Client Email Log DB

DB `collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945`. Populated by the user's
Make.com scenarios (**do not touch those scenarios**). The dossier reads these
rows + the `📧 Email Intelligence` subpage into §3.

Thread headers inside §3 follow this shape:

```
#### 🔴 **Re: <Subject>** · HIGH risk · ACTIVE      ← active thread
#### ⚪ <Subject> · Noise                            ← filtered noise
```

| Element | Definition |
| --- | --- |
| **Risk dot** | `🔴 HIGH` · `🟡 MED` · `🟢 LOW` · `⚪ Noise`. |
| **State** | `ACTIVE` / resolved / `Noise`. |
| **Per-message tag** | `[Email <date> <from>→<to> "<subject-stub>"]` — the source-tag form (see §6). |

### 4.3 Meeting trackers

- **Meetings Tracker** DB `collection://2fb49172-8751-80df-b73d-000b4a81281e` —
  one row per meeting, with recap URLs (Fathom / Fellow / Granola).
- **Meeting Action Items** DB `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3`.
- **Meeting Transcripts** DB `collection://b80239b8-8216-4e27-8492-c8a5b66c177d`.

Meeting block headers inside §4.2:

```
#### 🎙 **<YYYY-MM-DD> · <Meeting Type>** · <Status>
```

| Element | Definition |
| --- | --- |
| **🎙** | Meeting marker. |
| **Meeting Type** | e.g. `Tax Strategy / Structure`, `Ad Hoc`. |
| **Status** | `Done` · `Pending ⚠️` (recap/transcript missing). |
| **`Restricted`** | A Meetings Tracker column — restricted meetings are excluded from synthesis and noted in the status line count. |
| **Tag form** | `[Meeting <date> <Type>]` → resolves in §12.6 with the recap URL. |

### 4.4 Tax-planning workbooks

These are the source spreadsheets/memos the strategy sections depend on. They
live on SharePoint/Drive and are *linked from the Account record* via named URL
properties. The reader stubs live in `execsumm_emails/readers/`.

| Workbook | Account property it should be linked under | Reader stub | Feeds |
| --- | --- | --- | --- |
| **PBC Workbook** (Prepared-By-Client) | `PBC Workbook` | `pbc_workbook.py` | §2 entity stack · §9 Cost Seg property schedule |
| **Insights Delivery Workbook** | `Tax Extraction` | `insights_workbook.py` | prior-year baseline (AGI, tax, SE) |
| **Tax Analysis Workbook** | (Account link) | `tax_analysis.py` | §8 projected-savings numerics |
| **Tax Planning Memo** | `Tax Planning Memo` | `tax_memo.py` | §8 strategy narrative |
| **Tax Meeting Prep** | `Meeting Prep Notes` | `tax_meeting_prep.py` | §4 prep context |

> **Naming for workbooks is the user's existing SharePoint convention — the
> dossier doesn't rename them.** What matters for *this* pipeline is that the
> Account record carries the **URL property** pointing at each one. If the
> property is empty, the dossier writes `? Pending workbook ingestion` and adds
> the file to §0 "Files NOT Accessible" and the §-x.4/.5 gap lists. So again:
> the **link/property is the lookup key**, not the workbook's filename.

### 4.5 Tax-planning strategies — table column dictionaries

**§8.1 Strategy table columns:**

| Column | Definition |
| --- | --- |
| **Strategy** | The named planning move (Cost seg, PTET election, S-Corp election, QSBS diligence, accountable plan, REPS, STR material participation, …). |
| **Entity/Property** | Which entity or property it attaches to. |
| **Est. Impact** | Dollar/again estimate, or `? Pending <source>` if the number isn't in a linked file. |
| **Status** | Current state / what it's gated on. |
| **Year** | Applicable tax year(s). |
| **Priority** | `🔴 HIGH` · `🟡 MED` · `🟢 LOW` · `mixed`. |
| **Source** | Inline source tag (see §6). |

**§9.1 Cost Segregation Candidates columns:** Property · Entity Owner · Basis ·
Placed in Service · Study Status · Est. Bonus Dep · Priority · Basis of Flag ·
Source.

**§9.2 S-Corp Election Candidates columns:** Entity · Current Classification ·
Net SE Earnings · Reasonable Salary · Est. SE Savings · Priority · Basis of
Flag · Source.

> §9 is **rule-based** (`opportunity_flags.py`). Any `HIGH` flag auto-promotes
> into §7 Critical Open Items. `NOT APPLICABLE` = ruled out by the classifier
> (e.g. already an S-corp, passive rental holding, disregarded entity).

---

## §5. Notion database catalog

The full set of DBs the pipeline reads/writes, with IDs. (Mirrors the table in
`CLAUDE.md`; reproduced here so this library stands alone.)

| Database | ID / collection | Role |
| --- | --- | --- |
| Executive Summaries DB | `20f69b74-b140-4c3c-8041-ba71e7792478` | Pointer-of-record (one row/client) |
| Executive Summaries data source | `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b` | Query target for the above |
| Accounts | `collection://8668d5ca-6472-4b62-914d-0da55334c72a` | Canonical client record + workbook URL properties |
| Reporting Entities | `collection://9c91286b-e233-45f2-98b0-f065544fb89c` | Per-entity records (federal form, classification) |
| Meetings Tracker | `collection://2fb49172-8751-80df-b73d-000b4a81281e` | Meeting rows + recap URLs |
| Meeting Action Items | `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3` | Action items from meetings → §7 |
| Meeting Transcripts | `collection://b80239b8-8216-4e27-8492-c8a5b66c177d` | Transcript records |
| Claude Summaries | `collection://86dca8a4-3522-40c4-a568-b99bc98fc756` | One row per refresh (audit) → §6 |
| Claude Activity Log | `collection://f9cc7d05-26b0-4c77-b29c-af974a234b77` | Per-action audit |
| Engagement Inquiries | `collection://7d71d896-b9de-4658-a02d-4caca8b0cc02` | Client inquiries → §7 |
| Engagement Letters | `collection://2ef49172-8751-8056-99e0-000ba1b5dd54` | EL tracker rows → §5.1 |
| Files & Links | `collection://4432a66e-8f29-480b-8bae-9b88525ae841` | Document inventory rows → §5.2 |
| Client Email Log | `collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945` | Correspondence (Make-fed) → §3 |
| Tax Ascend | `collection://2f049172-8751-80f7-bcad-000b63a307fe` | Engagement-stage tracker |

---

## §6. Source-tag (provenance) grammar

Every non-obvious fact carries an inline tag in backticks; §12 of each dossier
resolves every tag to a URL. **This is the heart of Axis A search** — a tag is a
searchable, resolvable key. The vocabulary:

| Tag form | Resolves to |
| --- | --- |
| `[Accounts:<Client>]` | The Account record. |
| `[Accounts:<Client>.<Property>]` | A specific Account property (e.g. `.Client #`, `.PBC Workbook = empty`). |
| `[AdvExec §<Issue/Section>]` | A section of the Advisory Exec Summary page. |
| `[ThinExec §<Section>]` | A section of the thin Exec Summary child page. |
| `[EISub:<Client>]` | The `📧 Email Intelligence` subpage. |
| `[Email <date> <from>→<to> "<subj>"]` | A message within a Client Email Log thread. |
| `[EI:<Subject> §<part>]` | A sub-section of a Client Email Log page. |
| `[EL:<who> <id-tail>]` / `[EL:<who> §<Property>]` | An Engagement Letters tracker row / property. |
| `[FL:<who> <id-tail>]` / `[FL:<who> §<Property>]` | A Files & Links row / property. |
| `[Meeting <date> <Type>]` | A Meetings Tracker row (recap URL in §12.6). |
| `[Inquiry #INQ-<n>]` | An Engagement Inquiries row. |
| `[Tax Ascend:<id>]` | The Tax Ascend row. |
| `[Claude <date> <thread title>]` | A Claude Summaries/Activity Log row. |
| `[Entity Stack §2]`, `[§3.1 …]`, `[§4.4 …]` | In-dossier back-references. |
| `[Gap: <desc>]` | **Not a real source** — a carry-forward reminder for next refresh. |
| `[SharedInbox:<inbox> <date> "<subj>"]` | Template form reserved for the live Outlook scan (not yet active). |

§12 buckets these into: 12.1 Account · 12.2 exec-summary pages · 12.3 Email Log
· 12.4 Engagement Letters · 12.5 Files & Links · 12.6 Meetings · 12.7 Inquiries
& adjacent DBs · 12.8 SharePoint/Drive/Portals · 12.9 in-dossier
back-references · 12.10 gap markers.

---

## §7. Status, confidence & symbol glossary

One legend for every symbol used across the artifacts:

| Symbol | Meaning |
| --- | --- |
| `✓` | **Confirmed** — fact verified against a source. |
| `~` | **Estimated** — approximate / derived. |
| `?` | **Pending** — depends on a file/number not yet ingested. |
| `🔴` | **HIGH** priority / risk. |
| `🟡` | **MED** priority / risk. |
| `🟢` | **LOW** priority / risk. |
| `⚪` | **Noise** (filtered email/thread). |
| `🎙` | Meeting / recap. |
| `📧` | Email / correspondence stream. |
| `📁` | Document inventory stream. |
| `⚡` | Action items / strategies stream. |
| `🤖` | Claude work-product stream. |
| `📄` | The dossier file (pointer property). |
| `📋` | An Advisory exec-summary page. |
| `⚠️` | Pending / attention (e.g. meeting with no recap). |
| `🗑️` | Duplicate row flagged for cleanup — **log, never auto-delete.** |
| `NOT APPLICABLE` | A §9 flag ruled out by the classifier. |
| `? Pending workbook ingestion` / `? Pending memo ingestion` | Standard gap markers when a $ figure's source isn't linked. |

---

## §8. Domain glossary

Plain-language definitions of the recurring tax/ops terms so a header makes
sense at a glance.

| Term | Meaning |
| --- | --- |
| **Dossier** | The comprehensive per-client Client Intelligence markdown file (§0–§13). |
| **PBC Workbook** | "Prepared By Client" workbook — client-supplied entity/financial data; seeds the entity stack and property schedule. |
| **EL / Engagement Letter** | The signed scope-of-work agreement; tracked per client/entity in the Engagement Letters DB. |
| **F&L / Files & Links** | The Notion DB row(s) holding document URLs for a client → §5.2. |
| **Cost Seg(regation)** | Accelerating depreciation on a building by reclassifying components; flagged per property in §9.1. |
| **S-Corp election** | Form 2553 election to be taxed as an S-corporation (reduces SE tax via reasonable salary); flagged per entity in §9.2. |
| **PTET** | Pass-Through Entity Tax — a state-level election (e.g. Utah PTET) that works around the SALT cap. |
| **QSBS (§1202)** | Qualified Small Business Stock — potential gain exclusion on eligible C-corp stock at exit. |
| **REPS** | Real Estate Professional Status — unlocks non-passive treatment of rental losses given an hours test. |
| **STR** | Short-Term Rental — material-participation rules can make losses non-passive. |
| **Accountable plan** | A reimbursement arrangement that keeps reimbursements out of taxable wages. |
| **Mango** | The firm's practice-management system; `Mango Client ID` doubles as the ImagineTime workspace key. |
| **Tax Ascend** | The engagement-stage program/tracker (Planning + Compliance + Advisory). |
| **Reporting Entity** | A taxable entity (1040/1065/1120S/1120) tied to the Account in the Reporting Entities DB. |
| **Sidecar** | Any Notion record fetched to build a dossier (Account, EL, F&L, Meeting, Email, Inquiry, Tax Ascend, etc.). |
| **MFJ** | Married Filing Jointly — household managed as one combined client. |
| **Make.com** | The automation piping emails into the Client Email Log — **read-only / do not touch.** |

---

## §9. Lookup recipes — "I want to find X"

| You want to find… | Look here |
| --- | --- |
| The current dossier for a client | Notion Exec Summary row → `📄 Dossier` URL (Axis B). Or newest dated file in the Drive folder. |
| Every client with a given engagement type | Filter the Exec Summaries DB on `Tax Engagement Type` / `Summary Type`. |
| What changed since last time | Dossier §13 (top dated block). |
| Who owns an open action | Dossier §7.2 owner rollup. |
| Whether a workbook is linked yet | Dossier §0 "Files NOT Accessible" + the Account record's URL properties. |
| The source behind a claim | The inline `[tag]` → resolve in §12. |
| All correspondence on a thread | Client Email Log DB row / §3 thread block. |
| A meeting recap | §4.2 block → §12.6 tag → Fathom/Fellow/Granola URL. |
| Which cost-seg / S-corp opportunities are live | §9.1 / §9.2 (HIGH flags also appear in §7). |
| What a symbol means | §7 of this library. |
| What a term means | §8 of this library. |

---

## §10. The one-paragraph answer to "does the filename matter?"

The system finds things by **headers + source tags inside the file (Axis A)**
and by **the Notion row's properties that point at the file (Axis B)**. The
**filename (Axis C)** is a human-and-Drive convenience and the carrier of the
dated history trail — it is reconstructable from the Notion row and is *not*
what search keys on. So: keep the `<Client>_Client_Intelligence_<YYYY-MM-DD>.md`
convention so the dated trail stays legible and Drive stays browsable, but spend
your real effort making sure every section header is present and every fact
carries a resolvable source tag, and that the Exec Summary row's properties +
`📄 Dossier` pointer are populated. Get those right and the file is fully
findable regardless of how it's named.

---

*Definitions Library v1 — 2026-06-01. Companion to `CLAUDE.md` (session rules),
`docs/PROJECT_OVERVIEW.md` (architecture), and `docs/BATCH_REFRESH_PROMPT.md`
(invocation contract). Reference dossier: `dossiers/SpringBengtzen/dossier.md`.*
