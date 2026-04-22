# ExecSumm-Emails — Comprehensive Client Intelligence Dossier Generator

This repository rebuilds the per-client dossiers that live in the Google Shared Drive folder
`G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\`, raising them to
the depth of the existing Tax Planning / Advisory exemplars in Notion (Matt & Chelsea
Iannaccio, Brett Zanotto, Spring Bengtzen + Brian Charlesworth, Sean Kennedy memo) and
mirroring the full content into the **Executive Summaries** database in Notion.

## Why

The Executive Summary pages in Notion today are thin — a "Current Status" paragraph and a
few bullets. The `💳 Full dossier: <Client>_Client_Intelligence_<date>.md` pointer in
Drive is in the same register. The Tax Planning / Advisory exemplars show what a real
dossier looks like: entity structure, property portfolio, books & tax status, strategies
with projected savings, a conversations log, action items with owners, strategic themes.

This generator produces one comprehensive dossier per client by synthesising **everything
on file** — PBC Workbook, Insights Delivery Workbook, Insights Transcript, Tax Analysis
Workbook, Tax Meeting Prep, Tax Planning Memo, email threads, meeting transcripts, Claude
chat sessions, and every Notion record — with an inline source tag on every non-obvious
fact and a Provenance Index so any claim is one click from its source.

## Output destinations

Each refresh writes to two places:

1. **Drive** — `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\<Client>_Client_Intelligence_<YYYY-MM-DD>.md`
   (prior dated versions retained as history).
2. **Notion** — the client's row in the Executive Summaries database
   (`20f69b74-b140-4c3c-8041-ba71e7792478`, data source
   `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b`). The row's page body is
   `replace_content`-ed with the rendered markdown; every DB property is populated
   (`Summary`, `Summary Type`, `Tax Engagement Type`, `Reporting Entity`, `Last
   Synthesized`, `📄 Dossier`, `📧 Email Summary`, `🎙 Meeting Summary`,
   `⚡ Action Items Summary`, `📁 Files & Links Summary`, `🤖 Claude Summary`).

Missing clients in the DB (Andrew Franklin, Andy Karabinos, Brittany Byma, Chandlor
Mullins, Colin Ushkowitz, Dan Wilcynski, Dylan Kozlina) are created as new rows on their
first refresh. Duplicate `🗑️ DELETE —` rows are logged to a cleanup queue — never
auto-deleted.

## Cumulative / living document

Each refresh is not an overwrite:

- Factual sections (Entity Structure, Property Portfolio, Books Status, Tax Status) are
  **updated in place** with the new source tag; the prior value is retained only if it
  changed, in which case a `(was: X per [source], changed to: Y per [source] on <date>)`
  note is appended.
- Narrative sections (Client Overview, Operations Analysis, Individual Profile, Strategic
  Themes) are **amended, not overwritten** — a dated revision block is added when the
  narrative materially shifts.
- Conversations Log, Recent Activity Timeline, and Claude Chats are **append-only**.
- A `## Changed Since Last Refresh` block is emitted at the top of every new file.

## Dossier sections (0–15)

1. **Changed Since Last Refresh** — append-only diff block.
2. **Client Overview** — narrative plus the one-line "what matters right now".
3. **Operations Analysis** — how the business actually runs (revenue engine, staff,
   tools, cadence, KPIs, risk).
4. **Individual Profile(s)** — one sub-section per principal (goals, wealth picture,
   life events).
5. **Entity Structure** — table + optional org chart.
6. **Property Portfolio** — table.
7. **Books Status** — per entity.
8. **Tax Status** — filing status, prior year, projection, ES payments, notices,
   extensions, engagement letter.
9. **Tax Strategies & Projected Savings** — table from memo / Tax Analysis.
   - **§8a. Opportunity Flags (auto-detected)** — `opportunity_flags.py` runs
     rule-based analyzers on every refresh: Cost Segregation candidates per
     property (HIGH/MEDIUM/LOW/NOT APPLICABLE, with basis, bonus-window,
     usability path, and est. first-year accelerated depreciation), and S-Corp
     Election candidates per operating entity (HIGH/MEDIUM/LOW/NOT APPLICABLE,
     with net SE earnings, reasonable salary target, est. SE savings, Form
     2553 timing notes). `HIGH` candidates auto-promote into §10 Critical
     Open Items. Cross-references Cost Seg Proposals/Engagements DB and
     FileForms Engagements DB so in-flight opportunities are marked
     `IN PROGRESS` rather than double-counted.
10. **Conversations Log** — email threads + meetings + Claude chats, all append-only.
11. **Critical Open Items** — numbered, owner-tagged.
12. **Action Items (rolled up)** — aggregated across every source.
13. **Recent Activity Timeline** — append-only.
14. **Strategic Themes** — amended, not overwritten.
15. **File Inventory** — every file on record + whether read this refresh.
16. **Provenance Index** — every source tag with a direct link.

## Repository layout

```
execsumm_emails/
  cli.py                  # `execsumm refresh <client>` entry point
  config.py               # Notion IDs, Drive paths, engagement lens mapping
  notion_client.py        # thin wrapper over Notion MCP
  account_loader.py       # resolve Account → entities, engagements, contacts
  readers/
    pbc_workbook.py       # reads PBC xlsx from Drive
    insights_workbook.py  # reads Insights Delivery / Tax Extraction xlsx
    tax_analysis.py       # reads Tax Analysis xlsx
    tax_memo.py           # .docx parser
    tax_meeting_prep.py
    transcripts.py        # Granola / Fathom / Fellow
    emails.py             # Outlook + Client Email Log + 📧 Email Intelligence subpages
    claude_chats.py       # Claude Activity Log + Claude Summaries
    notion_sources.py     # Engagement Inquiries, Service Requests, Intake Requests, etc.
  template.py             # section 0–16 renderer
  merge.py                # cumulative merge with prior dossier
  provenance.py           # source tag format + Provenance Index builder
  writer.py               # Notion DB row upsert + Drive .md write + Claude log entry

dossiers/                 # local mirror of the Drive dossiers folder (committed for PR review)
extracts/                 # local mirror of the Drive extracts folder (sidecar JSONs)
```

## Pilot output

The first two comprehensive dossiers are committed under `dossiers/`:

- `SpringBengtzen_Client_Intelligence_2026-04-22.md`
- `TommyHarr_Client_Intelligence_2026-04-22.md`

and mirrored into their Executive Summaries DB rows in Notion.

## Running

The Python generator is currently a scaffold — the live pilot runs were produced via
Notion / Outlook / Granola MCP tool calls. The scaffold modules define the pipeline that
will be executed inside the Drive-mounted environment where the large workbooks, memos,
and transcripts are all reachable.

```
python -m execsumm_emails.cli refresh "Spring Bengtzen"
python -m execsumm_emails.cli refresh "Tommy Harr"
python -m execsumm_emails.cli refresh-all           # all clients in the exec summary index
```

See `/root/.claude/plans/g-shared-drives-smj-product-development-parallel-blum.md` for
the full approved design.
