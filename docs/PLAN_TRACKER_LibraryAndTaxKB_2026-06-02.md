# Plan Tracker — Definitions Library + Tax KB layer

**Drop this in:** `C:\Users\SethJohnson\MCP_Projects\ExecSumm-Dossiers\` (plan
folder). The cloud session can't write to `C:\` directly — pull from the branch
or use the copy sent to you. Mirror lives in the repo at
`docs/PLAN_TRACKER_LibraryAndTaxKB_2026-06-02.md`.

| | |
| --- | --- |
| **Session date** | 2026-06-02 |
| **Branch** | `claude/md-library-headers-definitions-zSoQP` |
| **PR** | #1 (draft) → base `claude/update-exec-summary-notion-118m7` · https://github.com/smj1058/1040-Comprehnensive/pull/1 |
| **Repo** | `smj1058/1040-Comprehnensive` |

---

## What this session produced

1. **`docs/DEFINITIONS_LIBRARY.md`** — the single lookup reference: every dossier/DB
   header, file-naming convention, source-tag grammar, status symbol, domain term,
   and the three-axis findability model (headers + tags → primary; Notion DB row →
   pointer-of-record; filename → convenience). Answers "does the filename matter":
   no — headers + DB properties drive lookup; the filename just carries the dated trail.
2. **`CLAUDE.md` rule #12** — client key (`Client #` + `Mango ID`) is now MANDATORY in
   every dossier §0, resolved from the Accounts record, never fabricated; explicit
   gap flag + §7 action item if the Account has no number.
3. **`docs/TAX_KB_LIBRARY.md`** — spec for the markdown-file + pointer layer over the
   **live** Tax Technical Knowledgebase (NOT the archived V2 proposal). Keyed by
   `Entry ID`. Mirrors the dossier pointer model.
4. **`docs/PLAN_TRACKER_…_2026-06-02.md`** — this file.

## Key findings

- **Client-# audit (all 42 dossiers):** ~30 have a real client number in §0; ~11 say
  "not populated on Account record" (the Notion **Account** itself has no number — an
  upstream data gap, not a file problem). The earlier "1 missing"
  (`ReneeMuellerJeffCohn`) was a **false positive** — that dossier carries
  `Client #: 18051006-01` / Mango `937741` in an **inline `**Client #:**` header
  style** rather than the `| Client # |` table row the grep matched. Both header
  styles are valid and carry the key; **no dossier is actually missing its number.**
- **Tax KB database already exists and is seeded:** **"Tax Technical Knowledgebase"**
  - DB id `857b8e97-7b2f-4b5c-9b0f-6f23300936d4`
  - data source `collection://c1c33884-96fa-42a0-bf6c-6ac7776e26dd`
  - durable key = **`Entry ID`** (auto-increment) + `Topic`
  - rich schema (Domain, Tax Category, Taxpayer Type, Jurisdiction, Return/Form,
    Authority Level, Code Section, Complexity/Risk, Timing/Phase, Status, Conflict
    Flag, Last Reviewed, …)
  - already has flag views: **⚠️ Conflict Queue**, **Planning Playbook**, **By Domain**
  - seeded entries: PTET, NIIT, QSBS §1202, SE Tax, Estimated Tax & Safe Harbor,
    C-Corp Double Taxation, FBAR/FATCA, Foreign Tax Credit, Child Tax Credit,
    Standard Deduction, Tax-Loss Harvesting, …
  - **missing only:** a `📄 KB Doc` URL property to point at the `.md` files.
- **Archived/IGNORE:** "Spec: Tax Question System V2"
  (`notion.so/33149172875181cf847aed6f3d5c0d0f`) is an older proposal under
  "_Archive (Mirrored from Accruity)" — superseded by the live DB above.

## Open decisions / TODO

- [ ] **Merge PR #1** (or keep draft) so the docs land on the default branch.
- [x] ~~Fix `ReneeMuellerJeffCohn`~~ — false positive; already has `Client #: 18051006-01`
      (inline header style). No fix needed.
- [x] **Added `📄 KB Doc`** URL property to the Tax Technical Knowledgebase
      (`collection://c1c33884-96fa-42a0-bf6c-6ac7776e26dd`) — DONE 2026-06-02.
- [ ] **Assign Client #** on the ~11 Accounts in Notion that lack one (then they flow
      into dossiers on next refresh): Aidan McIsaac, Brittany Byma, Daniel Huffman,
      David & Michelle Saward, Gary Aronov, Jeremy Martin, Logan Bowles,
      Michael Venereo, Michelle Bowles, Renee Mueller Solo, Tommy Harr. *(Can't be
      invented — assigned by the firm upstream.)*
- [ ] **Decide build scope** for the Tax KB MD layer: template/renderer (`tax_kb/`),
      gap+stale detector (modeled on `opportunity_flags.py`), and/or backfill `.md`
      files for the existing seeded rows.
- [ ] **Confirm SharePoint folder path** for `Tax-Knowledge/<Domain>/` on the
      `subledge…` tenant.
- [ ] **New repo question:** whether to also stand up a standalone `client-intelligence`
      repo (couldn't be created from the cloud session — integration scoped to this
      repo only). Bundle was sent for manual push.

## Hard boundaries (carried from CLAUDE.md)

- **Do NOT touch Make.com** scenarios/hooks/data stores/connections (rule #8). The KB
  auto-create "trigger" stays in Make; only the file-creation + pointer-stamp step is
  ours, defined as a contract in `docs/TAX_KB_LIBRARY.md` §4.
- **Pointer-only Notion model** — body lives in the `.md`; the DB row points at it.

---

*Generated 2026-06-02 from session
https://claude.ai/code/session_015rk9WgFMvTeCPBNCbgJSyt*
