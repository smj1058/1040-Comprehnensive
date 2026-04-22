# Batch Refresh Prompt — Remaining Tax Clients

Copy the block below into a fresh Claude Code session (or `@ > Run in background`)
to produce the comprehensive Client Intelligence Dossier for the next client in
the queue. Run it once per client — **do not** try to batch multiple clients in
one session, it will time out.

The workflow is the same 11 turns Spring Bengtzen used. Spring's completed
dossier at `dossiers/SpringBengtzen/dossier.md` is the reference; match depth,
structure, and source-tagging style.

---

## The prompt

> You are picking up the Accruity comprehensive Client Intelligence Dossier
> pipeline. The approved plan lives at
> `/root/.claude/plans/g-shared-drives-smj-product-development-parallel-blum.md`
> and the reference implementation is `dossiers/SpringBengtzen/dossier.md`.
>
> **Target client this session:** `<CLIENT NAME>`
>
> **What to do**
>
> Run the 11-turn pipeline, one turn per message. Each turn: (1) read
> `dossiers/<ClientFolder>/state.json` and `dossiers/<ClientFolder>/dossier.md`
> at the start, (2) write your section, (3) update the state.json progress
> marker to `done`, (4) `git add` + `git commit` + `git push origin
> claude/update-exec-summary-notion-118m7`, (5) print a one-line status like
> "§4 done — 12 meetings synthesized, 3 restricted excluded, next: §5" and
> STOP. Do not start the next turn in the same message.
>
> **If a single turn is large enough to risk a timeout, split it.** Turn 8
> (§8 + §9) and Turn 9 (§10 + §11) in particular may need splitting —
> commit §8, status line, stop; next message does §9, commit, status line,
> stop. Same shape for §10 / §11 and §12 / §13. The stop-hook enforces
> commit + push, so each micro-step lands on the branch independently.
>
> **The 11 turns**
>
> | Turn | Scope | Output |
> | --- | --- | --- |
> | 1 | Account lookup + fetch sidecars (Advisory exec, thin exec, Client Email Log rows, Engagement Letter tracker rows, Files & Links rows, Meetings Tracker rows, Engagement Inquiries, Tax Ascend) + load prior dossier if exists | `dossiers/<ClientFolder>/state.json` + seeded `dossier.md` header |
> | 2 | §1 Executive Overview + §2 Client Profile | append |
> | 3 | §3 Email Intelligence (active threads, noise, rollup, gaps) | append |
> | 4 | §4 Meeting History (every Meetings Tracker row with recap URLs) | append |
> | 5 | §5 Document Inventory (EL tracker rows, Files & Links rows, platforms in use, unlinked workbooks) | append |
> | 6 | §6 Claude Work Product (prior Claude Summaries + Activity Log rows tied to account) | append |
> | 7 | §7 Action Items rolled up across email + Advisory issues + Meeting Action Items + Engagement Inquiries + Service Requests + Intake Requests + dossier-gen flags | append |
> | 8 | §8 Tax Strategies + §9 Opportunity Flags (rule-based Cost Seg + S-Corp classifier) | append — SPLIT INTO TWO TURNS IF LARGE |
> | 9 | §10 Operations Analysis + §11 Individual Profile(s) | append — SPLIT IF LARGE |
> | 10 | §12 Provenance Index + §13 Changed Since Last Refresh | append — SPLIT IF LARGE |
> | 11 | Push final `dossier.md` into the matching **Executive Summaries DB** row body via `notion-update-page` `replace_content`, then `update_properties` to populate Summary / Summary Type / Tax Engagement Type / Reporting Entity / date:Last Synthesized:start / Updated By / 📄 Dossier / 📧 Email Summary / 🎙 Meeting Summary / ⚡ Action Items Summary / 📁 Files & Links Summary / 🤖 Claude Summary. Also log a Claude Summary DB row for the refresh itself. | Notion write |
>
> **Hard rules**
>
> - **Append-only** for Conversations Log (§3), Timeline (implicit in §3/§4),
>   Claude Chats (§6). Never overwrite prior entries.
> - **In-place update** for factual sections (§2 Entity Stack, §5 Files & Links,
>   §8 Strategy table, §9 flags) with a one-line `(was: X per [source], changed
>   to: Y per [source] on <date>)` note if a fact changed.
> - **Amended, not overwritten** for narrative sections (§1 Overview, §10
>   Operations, §11 Profiles, §13 Themes). Add a dated revision block
>   when the narrative materially shifts; keep the prior block.
> - **Source tags on every non-obvious fact** — use the format from §12
>   Provenance Index in Spring's dossier. Build the Provenance Index in
>   Turn 10.
> - **No fabricated numbers.** If a `$` figure comes from a workbook that
>   isn't linked to the Account, use `?` and flag it `? Pending workbook
>   ingestion`. Spring's §8.1 shows the pattern.
> - **Do not touch any Make.com scenarios.** Do not create, update, delete,
>   or edit Make hooks, scenarios, data stores, or connections. Read-only
>   on everything outside Notion (for sidecars) and the local repo.
>
> **Commit rules**
>
> - Designated branch: `claude/update-exec-summary-notion-118m7`. Stay on it.
> - Commit after every turn (or sub-turn if split). Push after every commit
>   — the stop-hook will fail otherwise.
> - Commit message format: `<Client> — Turn N appended (<section>)` with a
>   2–4 sentence body summarising what was added + key findings.
>
> **When done**
>
> Print a final summary listing:
> - Exec Summary DB row URL that was populated
> - Drive / local `.md` path
> - Count of open action items promoted to §7
> - Count of HIGH opportunity flags promoted from §9 to §7
> - Any dossier-gen plumbing items added to the next-refresh queue
>
> Then stop. Do not start another client.

---

## The remaining queue

Run once per client — replace `<CLIENT NAME>` in the prompt above. Spring
Bengtzen and Tommy Harr are pilots (Spring is complete through Turn 10;
Tommy is pending). After the pilots, process in whatever order matches
current business priority.

### Currently in the Executive Summaries DB (populate bodies + properties)

Alan Thompson · Alex Mayle · Beth Taylor · Brad Kanouse · Brett Zanotto ·
Chandlor Mullins (create row — see below) · Chelsea Dillick · David &
Michelle Saward · Dylan Kozlina (current row is a meeting note — create a
client-dossier row) · Gary Aronov · Greg Whitmire · Jason Michelle Bowles ·
Javier Ornelas · Jeremy Lee · Jeremy Martin · Joe Rock · Kara Hinshaw ·
Kelli Salter · Kristi Fox · Leon Howard · Logan Bowles · Matt & Chelsea
Iannaccio (existing Tax Planning row — amend, don't duplicate) · Matt
Pezon · Matthew Schneider · Meghan Botkin · Michael Venereo · Mike Lucas ·
Monica Hayes · Nico Gentile · Paul & Lisa Girard · Sandee Payne · Sean
Kennedy (existing Tax Planning Memo row — amend, don't duplicate) ·
**Spring Bengtzen ✓ (Turns 1–10 done; Turn 11 pending)** · Tate Cline ·
Tim Dent · **Tommy Harr (pilot — pending)** · Will Podrasky

### Missing from the DB — create new rows on first refresh

- Andrew Franklin
- Andy Karabinos
- Brittany Byma
- Chandlor Mullins
- Colin Ushkowitz (Champion Oak)
- Dan Wilcynski (Wilcynski Partners)
- Dylan Kozlina (the existing row is "Tax Meetings - Dylan Kozlina - 2026-04-08", a meeting note — create a proper client-dossier row)

### Duplicates — DO NOT delete; log to cleanup queue

- `🗑️ DELETE — Kristi Fox (duplicate)`
- `🗑️ DELETE — Logan Bowles (duplicate, merged into other)`
- `🗑️ DELETE — Michael Venereo (duplicate)`
- `🗑️ DELETE — Monica Hayes (duplicate, empty)`
- `🗑️ DELETE — Randy Wolfe (duplicate)`
- `🗑️ DELETE — Tate Cline (duplicate)`

---

## Reference resources

- Approved plan: `/root/.claude/plans/g-shared-drives-smj-product-development-parallel-blum.md`
- Pipeline scaffold: `execsumm_emails/` (readers, renderer, writer, merge, provenance, opportunity_flags)
- Reference dossier: `dossiers/SpringBengtzen/dossier.md`
- Reference state: `dossiers/SpringBengtzen/state.json`
- Executive Summaries DB: `20f69b74-b140-4c3c-8041-ba71e7792478` ·
  data source `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b`
- Accounts data source: `collection://8668d5ca-6472-4b62-914d-0da55334c72a`
- Reporting Entities: `collection://9c91286b-e233-45f2-98b0-f065544fb89c`
- Meeting Action Items: `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3`
- Meeting Transcripts: `collection://b80239b8-8216-4e27-8492-c8a5b66c177d`
- Claude Summaries: `collection://86dca8a4-3522-40c4-a568-b99bc98fc756`
- Engagement Inquiries: `collection://7d71d896-b9de-4658-a02d-4caca8b0cc02`
- Engagement Letters: `collection://2ef49172-8751-8056-99e0-000ba1b5dd54`
- Files & Links: `collection://4432a66e-8f29-480b-8bae-9b88525ae841`
- Client Email Log: `collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945`
- Meetings Tracker: `collection://2fb49172-8751-80df-b73d-000b4a81281e`
- Tax Ascend: `collection://2f049172-8751-80f7-bcad-000b63a307fe`
