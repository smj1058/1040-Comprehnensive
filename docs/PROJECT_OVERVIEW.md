# Project Overview — ExecSumm-Dossiers Pipeline

A complete, project-level explanation of what this is, how it runs, where everything is saved, and what tools/memory/execution model it relies on. Intended to be readable by a fresh Claude session (or human) with no prior context. **Zero client-specific information.**

---

## 1. What this project is (one paragraph)

The pipeline turns each Accruity client into a single comprehensive **Client Intelligence Dossier**: a markdown file synthesizing every workbook, email, meeting, Notion record, and Claude session about that client into one source-tagged living document. Each refresh produces (a) a new dated `.md` deliverable, (b) updates the client's row in the Notion **Executive Summaries** database with a TL;DR + pointer URLs, and (c) logs a row in the Notion **Claude Summaries** database for audit. The project is a **cumulative living-document system** — every refresh appends/amends; nothing is overwritten.

---

## 2. Storage architecture — where everything lives

| Artifact | Canonical location | Mirror / pointer | Notes |
| --- | --- | --- | --- |
| **Per-client dossier** (markdown, ~250–940 lines) | `dossiers/<ClientFolderNoSpaces>/dossier.md` in the git repo | Notion Exec Summary DB row's `📄 Dossier` URL property points here | Plan calls for a Drive copy at `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\<Client>_Client_Intelligence_<YYYY-MM-DD>.md` — not yet wired |
| **Per-client state** (progress markers + sidecar URLs) | `dossiers/<ClientFolderNoSpaces>/state.json` | — | Read at start of each refresh; updated as turns complete |
| **Notion Executive Summaries DB row** | `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b` | Body intentionally left empty; pointer-only model | One row per client (multi-row per engagement lens for some clients) |
| **Notion Claude Summaries log row** | `collection://86dca8a4-3522-40c4-a568-b99bc98fc756` | One row per refresh | Audit trail of what Claude did, when, with what files |
| **Project session instructions** | `CLAUDE.md` in repo root | Auto-loaded by Claude Code in any session opened in this directory | THE canonical instruction file |
| **Per-client invocation contract** | `docs/BATCH_REFRESH_PROMPT.md` | — | The prompt template for running one client at a time |
| **Approved plan / design spec** | `/root/.claude/plans/g-shared-drives-smj-product-development-parallel-blum.md` (Linux sandbox) | Mirrored intent in repo's `CLAUDE.md` and `BATCH_REFRESH_PROMPT.md` | Original design doc; superseded by docs in the repo for runtime use |
| **Python generator scaffold** (intended automation) | `execsumm_emails/` in repo | — | Currently stubs (`raise NotImplementedError`); will replace Claude-as-runtime when wired |
| **Reference dossiers** | `dossiers/SpringBengtzen/` (771 lines, full) · `dossiers/TommyHarr/` · `dossiers/AlexDykesMarkFerguson/` (medium) · `dossiers/AidanMcIsaac/` (sparse) | — | Templates new agents read at session start |
| **Run-level handoff doc** | `docs/HANDOFF_<YYYY-MM-DD>.md` | — | Created at end of each batch run summarizing what was done |
| **Branch** | `claude/update-exec-summary-notion-118m7` on GitHub | Pushed after every commit | All work stays on this branch until reviewed |
| **User's local instruction folder** | `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` | Read by user's local Claude Code | NOT writable from a remote/cloud sandbox; only the user's local Claude can sync into it |

---

## 3. Execution model

### Two runtimes coexist:

**A. Claude-as-runtime (current state)**
The pipeline is currently driven by Claude itself acting as the orchestrator. Two patterns:

- **11-turn pattern** (used for the first two pilots and any client where deep iterative analysis is wanted): one section of the dossier per turn; read state.json + dossier.md, append the section, update state, commit, push, status line, stop. Each turn is a separate message exchange.
- **Single-Write optimized pattern** (used for batched runs after pilots): one tool-call message does parallel sidecar fetch from Notion; one Write produces the entire dossier; one Notion update populates DB row properties; one Notion create logs the Claude Summary; one git commit/push closes the run.

**B. Parallel subagents (added during batch run)**
The main Claude can launch up to 5 concurrent subagents via the `Agent` tool. Each subagent:
- Receives a self-contained prompt naming ONE client + the reference files to read
- Runs the single-Write optimized pattern in its own context
- Writes to its OWN client subfolder (no merge conflicts since paths are disjoint)
- Notifies the main Claude on completion via async task notifications

When one finishes, the main Claude immediately launches a replacement to maintain the concurrency target.

**C. Future Python generator (target state, not yet wired)**
The `execsumm_emails/` package defines the pipeline as a real Python program (`execsumm refresh <Client>` and `execsumm refresh-all`). All readers (`pbc_workbook.py`, `tax_memo.py`, `transcripts.py`, `emails.py`, etc.) currently raise `NotImplementedError`. Once wired against Drive/Outlook/Notion APIs and run from a Drive-mounted environment, this replaces Claude-as-runtime entirely. Estimated speed: minutes per client vs. minutes-to-hours under Claude-as-runtime.

### Per-client refresh invocation
A user runs one of these from their local Claude Code session opened in this repo:
- `run <Client Name>` — full 11-turn refresh with confirmation between turns
- `continue` — advance one turn
- `refresh all` / `run the next batch` — walk the queue from `docs/BATCH_REFRESH_PROMPT.md` one client at a time
- `status` / `where are we` — read state.json for the active client

The `CLAUDE.md` at repo root tells any Claude what those commands mean.

---

## 4. Memory model

There is **no in-process memory across runs** — every refresh starts fresh. State is persisted to disk and to Notion:

- **`dossiers/<Client>/state.json`** — turn-by-turn progress, sidecar URLs, entities discovered, plumbing flags. Read at start of every turn; updated after each turn closes.
- **`dossiers/<Client>/dossier.md`** — the cumulative living document. The current refresh reads it, appends/amends sections per the rules below, and writes the next dated file.
- **Notion Claude Summaries DB** — one row per refresh: Thread Title, Date, Account relation, Clients, Topics, Files Reviewed, Notion Pages Created, Summary. The next refresh queries this DB to discover what prior Claude work exists.
- **Notion Claude Activity Log DB** — one row per substantive Claude action across the workspace; complementary to Claude Summaries.
- **Prior dated dossier files** are retained forever — readers can see how the narrative evolved across refreshes.

### The cumulative living-document rules

| Section type | Rule |
| --- | --- |
| Conversations Log (§3 Email Intelligence), Timeline (in §3/§4), Claude Chats (§6) | **Append-only.** New entries inserted chronologically; prior entries preserved verbatim |
| Factual sections (§2 Entity Stack, §5 Files & Links, §8 Strategy table, §9 Opportunity Flags) | **In-place update.** When a fact changes, add `(was: X per [source], changed to: Y per [source] on <date>)` inline so history is visible |
| Narrative sections (§1, §10, §11, §13) | **Amended, not overwritten.** New dated revision block goes ABOVE the old; old block preserved |
| `## §13 Changed Since Last Refresh` | Always emitted at top of §13 with delta-only summary against the prior refresh |

### Provenance

Every non-obvious fact in a dossier carries an inline source tag like `[AdvExec §Issue 1]`, `[Email 2026-04-13 …]`, `[Meeting 2025-12-03 …]`, `[Claude 2026-04-08 …]`. §12 Provenance Index at the foot of the dossier resolves every tag to a direct URL.

---

## 5. Dossier section structure (§1–§13)

Every dossier follows the same skeleton. Sparse-mode dossiers compress empty sections to one-line gap flags; full-depth dossiers expand each section with tables, narratives, and cross-references.

| § | Section |
| --- | --- |
| 0 | Header (client metadata, date, depth mode, data sources, files-not-accessible) |
| 1 | Executive Overview |
| 2 | Client Profile (entity stack, principals, third parties) |
| 3 | Email Intelligence (active threads, noise filter, rollup, gaps) |
| 4 | Meeting History (every Meetings Tracker row + recap URLs) |
| 5 | Document Inventory (Engagement Letters, Files & Links, external platforms, unlinked workbooks) |
| 6 | Claude Work Product (prior Claude Summaries + Activity Log entries tied to account) |
| 7 | Action Items — Rolled Up (across email + meetings + Advisory issues + DB rows + dossier-gen flags) |
| 8 | Tax Strategies & Projected Savings |
| 9 | Opportunity Flags (auto-detected: Cost Seg + S-Corp classifier from `execsumm_emails/opportunity_flags.py`) |
| 10 | Operations Analysis |
| 11 | Individual Profile(s) (one sub per principal in joint households) |
| 12 | Provenance Index (every source tag → direct link) |
| 13 | Changed Since Last Refresh |

---

## 6. Tools used

### Notion MCP — primary read/write
- `notion-search` — search Notion content + connected sources
- `notion-fetch` — fetch a page or DB row by URL/ID
- `notion-query-data-sources` — SQL-style query against a Notion DB
- `notion-update-page` (`update_properties`, `update_content`, `replace_content`) — update DB row properties and/or page body
- `notion-create-pages` — create new rows in a DB (used for Claude Summaries log + missing Exec Summary rows)
- Auxiliary: `notion-create-comment`, `notion-get-users`, `notion-update-data-source`, etc.

Workspace contains the Notion DBs the pipeline reads from (Accounts, Reporting Entities, Engagement Letters, Files & Links, Email Log, Meetings Tracker, Engagement Inquiries, Tax Ascend, Insights Project Status, Tax Engagements, Cost Seg Proposals, Claude Summaries, Claude Activity Log, etc.). Full ID list in `CLAUDE.md`.

### GitHub MCP — branch/PR management
- `mcp__github__create_pull_request`, `subscribe_pr_activity`, etc.
- The pipeline currently pushes via raw `git push` from Bash; the GitHub MCP is reserved for PR / issue work.

### SharePoint / Outlook / Granola MCP — read-only intelligence
- `sharepoint_search`, `sharepoint_folder_search` — find documents in SharePoint
- `outlook_email_search`, `outlook_calendar_search`, `chat_message_search`, `find_meeting_availability` — read Outlook (intended for backfilling email logs that aren't in Notion)
- Granola MCP (`get_meeting_transcript`, `query_granola_meetings`, etc.) — pull meeting transcripts

### Make.com MCP — DO NOT TOUCH
The user has Make scenarios that pipe captured emails into the Notion **Client Email Log** DB. The pipeline must NOT create, update, delete, activate, or modify any Make scenario, hook, data store, or connection. Make integration is operationally invisible to the pipeline; we only consume the Notion DB rows it produces.

### GitHub MCP scope
Restricted to `smj1058/1040-comprehnensive`. Cross-repo operations are denied.

### Native tools
- `Bash` — git operations, filesystem checks, shell utilities
- `Read`, `Write`, `Edit` — file I/O within the sandbox
- `TodoWrite` — main-thread progress tracking
- `Agent` — subagent launch (with optional `model: sonnet` / `opus` / `haiku` override)

### Tools intentionally NOT used
- Make scenario tools — by user direction
- `replace_content` for the Notion DB row body — would create a drift-prone duplicate of the dossier markdown; pointer-only model is canonical

---

## 7. The 11-turn workflow (full-depth refresh)

| Turn | Scope | Output |
| --- | --- | --- |
| 1 | Account lookup + fetch all sidecars + load prior dossier if exists | `dossiers/<Client>/state.json` + seeded `dossier.md` header |
| 2 | §1 Executive Overview + §2 Client Profile | append |
| 3 | §3 Email Intelligence | append |
| 4 | §4 Meeting History | append |
| 5 | §5 Document Inventory | append |
| 6 | §6 Claude Work Product | append |
| 7 | §7 Action Items rolled up | append |
| 8 | §8 Tax Strategies + §9 Opportunity Flags | append (split into 2 sub-turns if size risks timeout) |
| 9 | §10 Operations + §11 Individual Profile(s) | append (split if needed) |
| 10 | §12 Provenance Index + §13 Changed Since Last Refresh | append (split if needed) |
| 11 | Notion write — pointer-only: `update_properties` on Exec Summary DB row + `notion-create-pages` Claude Summary log row | Notion write |

After each turn: read state, write section, update state, commit, push, status line, **stop**. Do not start the next turn in the same response.

---

## 8. The optimized single-Write batch workflow

Used for batched runs after the first two pilots. Collapses the 11 turns into ~5 tool calls per client:

1. Search the Accounts DB for the client → resolve canonical Account URL
2. **Parallel-fetch ALL sidecars** in ONE message (one `notion-fetch` per sidecar URL: Account + every EL + every Meeting + every F&L + every Email Log + Insights Project + Tax Ascend + Tax Engagements + Cost Seg Proposals + Claude Summaries query)
3. Pick depth mode based on data: SPARSE (<5 sidecars) / MEDIUM (5–15) / FULL (15+)
4. **Write the entire dossier** in ONE `Write` to `dossiers/<Client>/dossier.md` — match depth to data; sparse sections compressed to one-line gap flags
5. Write `state.json` to same folder
6. `notion-update-page update_properties` on the Exec Summary DB row (CREATE NEW row via `notion-create-pages` if no existing row)
7. `notion-create-pages` into Claude Summaries DB to log the refresh
8. `git add` + `git commit` + `git push origin claude/update-exec-summary-notion-118m7`

Sparse clients run in ~5 minutes wall-clock with this pattern. Full-depth clients still take 25–45 min because of dossier length.

---

## 9. Parallel batch execution

The `Agent` tool launches a subagent in its own context. Each subagent runs the single-Write workflow above for one client, end-to-end. Up to 5 concurrent agents was the practical ceiling without hitting Notion API rate limits.

Pattern:
- Each agent's prompt is self-contained: client name + 4 reference dossier paths + the optimized workflow + hard rules + reporting contract
- Each agent works in its own subfolder (`dossiers/<Client>/`) so file-merge conflicts are impossible
- Each agent commits + pushes its own work
- The main Claude maintains a 5-concurrent target: when one completes, the main Claude immediately launches a replacement
- On completion each agent reports back: dossier path + line count, Notion URLs, depth mode, top 5 findings, action item counts, F&L URL collision Y/N, last commit SHA

Sonnet vs Opus tradeoff: Sonnet completes most clients reliably; one client (Casey Quinn) failed on both Sonnet and Opus due to data-record ambiguity. Sonnet costs materially less for this work.

---

## 10. Hard rules (non-negotiable)

1. **One section per turn** in the 11-turn pattern. Read state, write, update state, commit, push, status line, stop.
2. **Append-only** for Conversations / Timeline / Claude Chats — never overwrite.
3. **In-place update** for factual sections — when a fact changes, annotate the change with source tags + date.
4. **Amended, not overwritten** for narrative sections — new dated block ABOVE the old; old preserved.
5. **Source tags on every non-obvious fact.** Build §12 Provenance Index in Turn 10.
6. **No fabricated $ figures.** Use `?` and `Pending workbook ingestion` if data is not in the file.
7. **Pointer-only Notion model.** Update DB row properties; the `📄 Dossier` URL property points to the markdown; **DO NOT** push the markdown into the Notion page body via `replace_content` — that creates a drift-prone duplicate.
8. **Do not touch Make scenarios.** No create/update/delete/activate on hooks, scenarios, data stores, connections.
9. **Designated branch:** `claude/update-exec-summary-notion-118m7`. Stay on it.
10. **Commit + push after every turn** (the stop-hook enforces this).
11. **Commit message format:** `<Client> — Turn N appended (<section>)` with a 2–4 sentence body summarising additions and key findings.
12. **Per-turn status line at end of each turn**: e.g. `§4 done — 12 meetings synthesized, 3 restricted excluded, next: §5`. Then stop.

---

## 11. Known limitations

- **The cloud sandbox cannot reach `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\`.** Only the user's local Claude Code on their Windows laptop can read/write that path. Anything that needs to land there has to be picked up by the local Claude session, or sync via OneDrive/Drive Desktop.
- **The `G:\` Drive deliverable path is not yet wired.** Plan calls for dossier copies at `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\` — currently the local repo mirror at `dossiers/<Client>/` is the only persisted markdown copy.
- **The Python generator scaffold's readers are stubs.** `execsumm_emails/readers/*.py` raise `NotImplementedError`. Until they're wired against Drive/Outlook/Notion, Claude is the runtime.
- **Workbook content is not yet ingested.** PBC Workbook, Tax Extraction, Tax Analysis Workbook, Tax Planning Memo, Meeting Prep Notes — most clients have these unlinked on their Account record. Until linked, §8/§9 sections marked `? Pending workbook ingestion` for many strategy/flag rows.
- **Meeting transcripts are referenced but not parsed.** Fathom/Fellow recap URLs are captured, but full transcript pull is deferred to next refresh in a Drive-mounted environment.
- **Email Outlook live scan is deferred.** Pipeline currently reads the Notion Client Email Log; broader Outlook scans against client domains over the last 18 months are flagged as next-refresh work.
- **Files & Links template-default URL collision** affects ~10 clients (same SharePoint URLs across Document Inventory + PBC PDF Package). Flagged for ops sweep.

---

## 12. Branch / commit conventions

- All work on `claude/update-exec-summary-notion-118m7`
- Each turn (or single-Write client) → one commit → push immediately
- Commit message format spelled out in rule #11 above
- Stop-hook enforces clean working tree at end of each Claude turn — uncommitted files block session close

---

## 13. Where each artifact type lives — at-a-glance

```
GitHub repo (smj1058/1040-comprehnensive, branch claude/update-exec-summary-notion-118m7)
├── CLAUDE.md                           ← session instructions (auto-loaded)
├── README.md                           ← public-facing project overview
├── pyproject.toml                      ← Python package config
├── docs/
│   ├── BATCH_REFRESH_PROMPT.md         ← per-client invocation template
│   ├── HANDOFF_2026-04-22.md           ← run-level summary doc
│   └── PROJECT_OVERVIEW.md             ← THIS FILE
├── execsumm_emails/                    ← Python generator scaffold (stubs)
│   ├── cli.py
│   ├── config.py
│   ├── account_loader.py
│   ├── notion_client.py
│   ├── template.py
│   ├── merge.py
│   ├── provenance.py
│   ├── opportunity_flags.py            ← Cost Seg + S-Corp classifier rules
│   ├── writer.py
│   └── readers/                        ← all readers raise NotImplementedError today
│       ├── pbc_workbook.py
│       ├── insights_workbook.py
│       ├── tax_analysis.py
│       ├── tax_memo.py
│       ├── tax_meeting_prep.py
│       ├── transcripts.py
│       ├── emails.py
│       ├── claude_chats.py
│       └── notion_sources.py
├── dossiers/                           ← per-client subfolders
│   └── <ClientFolderNoSpaces>/
│       ├── dossier.md                  ← THE deliverable (markdown)
│       └── state.json                  ← progress + sidecar URLs
└── extracts/                           ← sidecar extraction JSONs (placeholder for future)

Notion workspace (read/write via Notion MCP)
├── Executive Summaries DB              ← one row per client; body empty; properties populated
│   └── 📄 Dossier URL property          ← points to dossier.md on GitHub or Drive
├── Claude Summaries DB                 ← one row per refresh (audit trail)
├── Claude Activity Log DB              ← per-action audit
├── Accounts DB                         ← canonical client records
├── Reporting Entities DB               ← per-entity records
├── Email Log DB                        ← email threads (populated by user's Make scenarios)
├── Meetings Tracker DB                 ← meeting records w/ recap URLs
├── Engagement Letters Tracker DB
├── Files & Links DB
├── Insights Project Status DB
├── Tax Engagements DB
├── Tax Ascend DB
├── Cost Seg Proposal Intake DB
├── Engagement Inquiries DB
├── Service Requests DB
└── Intake Requests DB

Cloud Sandbox (Linux container — where this Claude session runs)
├── /home/user/1040-Comprehnensive/     ← clone of the GitHub repo
└── /root/.claude/plans/                ← original approved plan (Linux-only path)

User's Windows laptop (this Claude can NOT reach)
├── C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\   ← canonical instruction folder (per user)
└── G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\   ← Drive deliverable path (not wired yet)

Local Claude Code session (user's laptop — different process from this sandbox)
└── Reads C:\ and G:\ natively; can sync from the GitHub branch
```

---

## 14. How to invoke (cheat sheet)

| Goal | Command (typed in user's local Claude Code session opened in this repo) |
| --- | --- |
| Refresh one client | `run <Client Name>` |
| Continue the active turn-by-turn run | `continue` |
| Refresh the whole queue | `refresh all` (one client at a time) |
| Status check | `status` / `where are we` |
| Open a draft PR | `open a draft PR for the current branch` (uses GitHub MCP) |
| Sync handoff doc into C:\ folder | (run from local laptop Claude) `copy docs/HANDOFF_<date>.md to C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` |

For batch runs in a remote sandbox where C:\ isn't reachable: spawn parallel `Agent` calls (one per client), each running the single-Write optimized workflow, with `model: "sonnet"` for cost efficiency.

---

## 15. Future state (when the Python generator is wired)

The intent is to replace Claude-as-runtime with `python -m execsumm_emails.cli refresh-all`. When the readers in `execsumm_emails/readers/` are connected to actual Drive/Outlook/Notion APIs, one cron job runs the entire pipeline in minutes per client (vs. minutes-to-hours under the Claude-as-runtime pattern). Claude becomes a once-per-client review tool rather than the orchestrator.

Until then, this document and `CLAUDE.md` define the manual-orchestration contract.

---

*Project overview as of 2026-04-22. Drop this into `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` (via your local Claude Code) as the canonical project-level reference.*
