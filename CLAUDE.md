# Claude Code session instructions — ExecSumm-Dossiers pipeline

You (Claude) have just been launched in the `1040-Comprehnensive` repo. This file tells you what this project is, where the canonical instructions live, and how to drive the pipeline. **Read this in full before doing anything.**

---

## What this project does

Generates a comprehensive **Client Intelligence Dossier** per client by synthesising every workbook, transcript, email thread, meeting recap, Notion record, and Claude session on file.

**Two locations matter — keep them straight:**

| Path | What it is |
| --- | --- |
| `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` | **Instructions only.** Project spec / how-to / approved plan. **READ-ONLY.** Do not write here. |
| `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\` | **Deliverable location.** Where each client's `<Client>_Client_Intelligence_<YYYY-MM-DD>.md` file actually gets saved on Drive. **WRITE HERE.** |
| `dossiers/<ClientFolder>/` (in this repo) | **Local mirror only.** Working copy for PR review and as a fallback if Drive is offline. Do not treat as the canonical deliverable. |

Output for each client (each refresh):

1. **Drive deliverable** — `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\<Client>_Client_Intelligence_<YYYY-MM-DD>.md`. Prior dated versions retained forever (cumulative / living-document rules).
2. **Local repo mirror** — `dossiers/<ClientFolder>/dossier.md` + `state.json` (committed for PR review).
3. **Notion Exec Summaries DB row** — body stays empty; the `📄 Dossier` URL property points to the Drive file (pointer-only — do not duplicate the body content into Notion).
4. **Notion Claude Summaries DB row** — logs the refresh.

The reference implementation is **Spring Bengtzen**, fully completed at:
- `dossiers/SpringBengtzen/dossier.md` (771 lines, §1–§13 + Provenance Index)
- Notion Exec Summary row: https://www.notion.so/3424917287518119aae6eeaf1cf263b2
- Notion Claude Summary row: https://www.notion.so/359491728751819899b6dab16ad6b0b4

Match its depth, structure, and source-tagging style for every other client.

---

## Where the canonical instructions live

```
C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\
```

That folder on the user's local machine is the canonical **instruction** folder (project spec, approved plan, any per-client overrides that supersede this CLAUDE.md). **At session start, list and read every `.md` file in that folder.** Read-only — do not write deliverables here.

## Where deliverables live

```
G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\
```

This is where **each client's dossier markdown file actually gets saved**. File naming:

```
<ClientNameNoSpaces>_Client_Intelligence_<YYYY-MM-DD>.md
```

Prior dated versions stay forever (cumulative living-document rules — readers can see how the narrative evolved).

The local repo path `dossiers/<ClientFolder>/dossier.md` is a **mirror for PR review and as a fallback if the Drive mount is offline**, NOT the canonical deliverable.

Repo-internal references (read these too):
- `docs/BATCH_REFRESH_PROMPT.md` — the per-client invocation contract (used to be a copy-paste prompt; now this CLAUDE.md does that job, but the spec still lives there)
- `dossiers/SpringBengtzen/dossier.md` — reference output
- `dossiers/SpringBengtzen/state.json` — reference state shape
- `execsumm_emails/` — the Python scaffold (readers + template + writer + opportunity_flags). Readers are stubs today; do not import them at runtime.

---

## How the user invokes you

Common shapes:

| User says | You do |
| --- | --- |
| `run <Client Name>` or `refresh <Client Name>` | Run Turns 1 → 11 for that client, one per response. After Turn 1, await "continue" before Turn 2. |
| `continue` | Run the next pending turn. |
| `refresh all` or `run the next batch` | Walk the queue from `docs/BATCH_REFRESH_PROMPT.md` § "remaining queue" and run **one client at a time**. Do not batch multiple clients in the same response. |
| `status` / `where are we` | Read `state.json` for the active client and report which turn is next. |

Do not start a new client until the current one is fully through Turn 11. Do not jump turns.

---

## The 11 turns

| Turn | Scope | Output |
| --- | --- | --- |
| 1 | Account lookup + fetch sidecars (Advisory exec, thin exec, Client Email Log rows, Engagement Letter tracker rows, Files & Links rows, Meetings Tracker rows, Engagement Inquiries, Tax Ascend) + load prior dossier if exists | `dossiers/<ClientFolder>/state.json` + seeded `dossier.md` header |
| 2 | §1 Executive Overview + §2 Client Profile | append |
| 3 | §3 Email Intelligence (active threads, noise, rollup, gaps) | append |
| 4 | §4 Meeting History (every Meetings Tracker row with recap URLs) | append |
| 5 | §5 Document Inventory (EL tracker rows, Files & Links rows, platforms, unlinked workbooks) | append |
| 6 | §6 Claude Work Product (prior Claude Summaries + Activity Log rows tied to account) | append |
| 7 | §7 Action Items rolled up across email + Advisory issues + Meeting Action Items + Engagement Inquiries + Service Requests + Intake Requests + dossier-gen flags | append |
| 8 | §8 Tax Strategies + §9 Opportunity Flags (rule-based Cost Seg + S-Corp classifier from `execsumm_emails/opportunity_flags.py`) | append — split into 2 sub-turns if size risks timeout |
| 9 | §10 Operations Analysis + §11 Individual Profile(s) | append — split if needed |
| 10 | §12 Provenance Index + §13 Changed Since Last Refresh | append — split if needed |
| 11 | **Drive write + Notion write — pointer-only Notion model.** Steps in order: (a) **Save the deliverable to Drive** at `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\<Client>_Client_Intelligence_<YYYY-MM-DD>.md`. (b) `notion-update-page update_properties` on the Exec Summaries DB row to populate Summary (TL;DR pulled from §1) / Summary Type / Tax Engagement Type / date:Last Synthesized:start / 📄 Dossier (Drive URL of the file just saved) / 📧 / 🎙 / ⚡ / 📁 / 🤖 (each = same Drive URL with section anchor where Drive supports it; otherwise same Drive URL). (c) `notion-create-pages` into Claude Summaries DB to log the refresh. **DO NOT** push the markdown into the Notion page body via `replace_content` — the body lives in the .md and is referenced via the 📄 Dossier URL. | Drive + Notion write |

---

## Hard rules — non-negotiable

1. **One section per turn.** Read `state.json` + `dossier.md` at start, append the section, update state, commit + push, write a one-line status, **stop**. Do not start the next turn in the same response.
2. **Append-only** for Conversations Log (§3), Timeline (implicit in §3/§4), Claude Chats (§6). Never overwrite prior entries on subsequent refreshes.
3. **In-place update** for factual sections (§2 Entity Stack, §5 Files & Links, §8 Strategy table, §9 flags). When a fact changes, add `(was: X per [source], changed to: Y per [source] on <date>)`.
4. **Amended, not overwritten** for narrative sections (§1, §10, §11, §13). Add a dated revision block; preserve the prior block.
5. **Source tags on every non-obvious fact.** Use the format from §12 Provenance Index in Spring's dossier. Build §12 in Turn 10.
6. **No fabricated numbers.** If a `$` figure depends on a workbook that isn't linked to the Account, write `?` and flag it `? Pending workbook ingestion`. Spring §8.1 shows the pattern.
7. **Pointer-only Notion model** (Turn 11). Update properties + create Claude Summary log row. **Do not** `replace_content` the dossier body into the Notion row body — that creates a drift-prone duplicate.
8. **Do not touch any Make.com scenarios.** No create / update / delete / activate on Make scenarios, hooks, data stores, or connections. Read-only on everything outside Notion (for sidecars) and the local repo.
9. **Designated branch:** `claude/update-exec-summary-notion-118m7`. Stay on it. Commit + push after every turn (the stop-hook enforces this).
10. **Commit message format:** `<Client> — Turn N appended (<section>)` with a 2–4 sentence body summarising the additions and key findings.
11. **Per-turn status line at the end of each turn**: e.g. `§4 done — 12 meetings synthesized, 3 restricted excluded, next: §5`. Then stop.
12. **Client key on every file (non-negotiable).** Every client `.md` this pipeline creates MUST carry the client key in its §0 header block — `Client #` and `Mango Client ID` — resolved at Turn 1 bootstrap from the **Accounts** record (`Client #` / `Mango Client ID` properties), never invented or retyped. The number is the durable search key (see `docs/DEFINITIONS_LIBRARY.md` §1–§2). If the Account record has no `Client #` assigned, write `— (not populated on Account record)` in the header **and** add a row to §7 Action Items to get it assigned upstream — do not leave the field silently blank and do not fabricate a number. A dossier is not "done" for the turn until the §0 `Client #` and `Mango Client ID` rows are present (real value or the explicit gap flag).

---

## Per-client folder convention

```
dossiers/
  <ClientFolderNoSpaces>/
    state.json   # progress markers + sidecar URLs + workbook gaps
    dossier.md   # the living document
```

`state.json` shape (see `dossiers/SpringBengtzen/state.json` for full reference):

```jsonc
{
  "client": "<Client Name>",
  "refresh_date": "YYYY-MM-DD",
  "prior_refresh": "first run" | "<previous date>",
  "account": { "page_url": "...", "client_number": "...", "mango_client_id": "...", ... },
  "household": { "principals": [...], "filing_status": "..." },
  "exec_summary_db_rows": [...],
  "sidecars": { "advisory_exec_summary": "...", "email_thread_*": "...", ... },
  "entities_known": [...],
  "workbooks_not_accessed_this_refresh": [...],
  "plan_turn_progress": {
    "turn_1_bootstrap": "done" | "pending" | "in progress",
    "turn_2_overview_profile": "...",
    ...
    "turn_11_push_notion": "..."
  },
  "notion_exec_summary_row_url": "...",   // populated after Turn 11
  "notion_claude_summary_row_url": "..."  // populated after Turn 11
}
```

---

## Notion IDs (use these without re-discovery)

| What | ID / collection |
| --- | --- |
| Executive Summaries DB | `20f69b74-b140-4c3c-8041-ba71e7792478` |
| Executive Summaries data source | `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b` |
| Accounts | `collection://8668d5ca-6472-4b62-914d-0da55334c72a` |
| Reporting Entities | `collection://9c91286b-e233-45f2-98b0-f065544fb89c` |
| Meeting Action Items | `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3` |
| Meeting Transcripts | `collection://b80239b8-8216-4e27-8492-c8a5b66c177d` |
| Meetings Tracker | `collection://2fb49172-8751-80df-b73d-000b4a81281e` |
| Claude Summaries | `collection://86dca8a4-3522-40c4-a568-b99bc98fc756` |
| Claude Activity Log | `collection://f9cc7d05-26b0-4c77-b29c-af974a234b77` |
| Engagement Inquiries | `collection://7d71d896-b9de-4658-a02d-4caca8b0cc02` |
| Engagement Letters | `collection://2ef49172-8751-8056-99e0-000ba1b5dd54` |
| Files & Links | `collection://4432a66e-8f29-480b-8bae-9b88525ae841` |
| Client Email Log | `collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945` |
| Tax Ascend | `collection://2f049172-8751-80f7-bcad-000b63a307fe` |

---

## Remaining client queue

See `docs/BATCH_REFRESH_PROMPT.md § "The remaining queue"` for the full list, broken into:
- existing DB rows to populate (~30 clients)
- 7 missing rows to create on first refresh
- 6 duplicate rows to log to a cleanup queue (never auto-delete)

Default running order: pilots first (Spring ✓ done, Tommy Harr next), then alphabetical by Account Name unless the user calls a specific client.

---

## Email-ingestion notes (do not act on these unless asked)

- The user owns `accruitytax.com`. The `accruity.com` mailboxes are external to that tenant.
- Make.com scenarios already pipe captured emails into the Notion **Client Email Log** DB. **Do not modify those scenarios.**
- The dossier reads emails from the Client Email Log + the `📧 Email Intelligence` subpage already populated by Make.
- Shared-inbox direct scans (`Mail.Read.Shared` against `tax@accruitytax.com` etc.) are documented in `execsumm_emails/readers/emails.py` but are not currently active runtime paths.

---

## When in doubt

Read the canonical instructions at `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` (read-only) and ask the user before deviating. Do not invent process. Do not skip turns. Do not duplicate content into Notion bodies. Save deliverables to Drive at `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers\` — not into the MCP_Projects folder.
