# Tax Knowledge Base — Library & Auto-Create Spec

**Companion to `docs/DEFINITIONS_LIBRARY.md`.** Where that file governs *client*
intelligence (dossiers, keyed by `Client #`), this one governs the **Tax
Technical Knowledgebase** — reusable, client-agnostic tax knowledge, keyed by
**`Entry ID`**.

This spec is written against the **live** database (not the archived "Tax
Question System V2" proposal):

| | |
| --- | --- |
| **Database** | **Tax Technical Knowledgebase** |
| Database ID | `857b8e97-7b2f-4b5c-9b0f-6f23300936d4` |
| Data source | `collection://c1c33884-96fa-42a0-bf6c-6ac7776e26dd` |
| Durable key | **`Entry ID`** (auto-increment number) + `Topic` (title) |
| Already seeded | PTET, NIIT, QSBS §1202, SE Tax, Estimated Tax & Safe Harbor, C-Corp Double Taxation, FBAR/FATCA, Foreign Tax Credit, Child Tax Credit, Standard Deduction, Tax-Loss Harvesting, … |
| Existing flag views | **⚠️ Conflict Queue** (Conflict Flag = Conflicting Sources) · **Planning Playbook** (Timing/Phase = Planning) · **By Domain** board |

> **The only addition needed for the MD-file model:** one new property —
> **`📄 KB Doc`** (URL) — pointing at the entry's `.md` in SharePoint. Adding it
> is a schema change to your hand-built DB, so I won't do it without your go.

---

## §1. Same pattern as the dossiers — different key

| | Client dossier | Tax KB entry |
| --- | --- | --- |
| **Durable key** | `Client #` + `Mango ID` (from Accounts) | **`Entry ID`** (auto-increment) + `Topic` |
| **File** | `dossiers/<Client>/dossier.md` + Drive | `Tax-Knowledge/<Domain>/KB-<EntryID>_<topic-slug>.md` (SharePoint) |
| **Pointer-of-record** | Exec Summaries row → `📄 Dossier` | Tax KB row → **`📄 KB Doc`** (new) |
| **Header taxonomy** | §0 + §1–§13 | §0 key block (mapped to the real properties) + body sections (§3) |
| **Auto-flag source** | `opportunity_flags.py` (Cost Seg / S-Corp) | the existing Conflict/Status/Last-Reviewed views + a gap detector (§4) |

The three-axis findability model from the definitions library applies
unchanged. **`Entry ID` is to a KB entry what `Client #` is to a dossier** — the
stable, stamped-in-file key. (It's auto-increment, so Notion assigns it on row
creation; the `.md` and filename quote it — never invent it.)

---

## §2. File naming & folder convention

```
Tax-Knowledge/
  Income/        Deduction/     Credit/
  Entity/        Compliance/    Procedure/     Planning/
```

- **Folder = `Domain`** (the 7 Domain values: Income, Deduction, Credit, Entity,
  Compliance, Procedure, Planning) so the path encodes the domain for browsing.
- **Filename:** `KB-<EntryID>_<topic-slug>.md`
  e.g. `KB-14_qsbs-exclusion-1202.md`, `KB-7_ptet-pass-through-entity-tax.md`.
  - `<EntryID>` = the DB's auto-increment `Entry ID` — the durable key, in the name.
  - `<topic-slug>` = kebab-case of `Topic` — human-readable, not the key.
- **Living document:** the `.md` is updated in place; git/SharePoint hold
  version history. `Last Reviewed` (in §0 and the DB) marks freshness — entries
  > 12 months flag stale. **No date in the filename** (the key is `Entry ID`,
  which is permanent).

---

## §3. KB entry `.md` header taxonomy (mapped to the real DB properties)

Every KB `.md` opens with a §0 key block whose fields **map 1:1 to the live DB
properties**, then the body. Property names below are verbatim from the DB.

### §0 — Key block

| Field (in `.md`) | DB property | Notes |
| --- | --- | --- |
| **Topic** | `Topic` (title) | Human title. |
| **Entry ID** | `Entry ID` | **The key.** Auto-assigned by Notion; quoted here, never invented. |
| **Summary** | `Summary` | Plain-language 1–2 sentence explanation (the bit pulled into prompts). |
| **Domain** | `Domain` | Income · Deduction · Credit · Entity · Compliance · Procedure · Planning (also the folder). |
| **Tax Category** | `Tax Category` | Income Tax · SE Tax · NIIT · AMT · Payroll · Excise · Estate/Gift · State (multi). |
| **Taxpayer Type** | `Taxpayer Type` | Individual · C-Corp · S-Corp · Partnership · Sole Prop · Trust/Estate · Nonprofit (multi). |
| **Jurisdiction** | `Jurisdiction` | Federal · State · Local · Multistate (multi). |
| **Return/Form** | `Return/Form` | 1040 · 1120 · 1120-S · 1065 · 1041 · 990 · Sch C/D/E (multi). |
| **Authority Level** | `Authority Level` | IRC · Treas. Reg · Rev. Rul./Proc. · Case Law · IRS Pub · Practitioner. |
| **Code Section** | `Code Section` | IRC section / reg cite / rev proc. |
| **Source/Authority** | `Source/Authority` | Pub, case, or chat link. |
| **Key Thresholds** | `Key Thresholds` | Dollar limits, %s, phase-outs. |
| **Complexity/Risk** | `Complexity/Risk` | Low · Medium · High · Gray Area. |
| **Timing/Phase** | `Timing/Phase` | Compliance · Planning · Both. |
| **Status** | `Status` | Current · Phasing Out · Sunset (TCJA) · Repealed · Proposed. |
| **Conflict Flag** | `Conflict Flag` | Clean · Conflicting Sources · Needs Reconciliation. |
| **Reconciliation Note** | `Reconciliation Note` | Only when Conflict Flag ≠ Clean. |
| **Last Reviewed** | `Last Reviewed` (date) | Stale if > 12 months. |
| **📄 KB Doc** | `📄 KB Doc` *(new)* | The URL of *this* `.md` (self-pointer / canonical body). |

(`Business vs Personal`, `Deduction Type`, `Income Type Treatment` carry over as
optional §0 fields where relevant.)

### KB body sections

| § | Header | Contents |
| --- | --- | --- |
| §1 | Issue | What this entry covers, in plain terms. |
| §2 | Rule | The governing rule / mechanics (expands `Summary`). |
| §3 | Thresholds & Numbers | Detailed limits, rates, phase-outs (expands `Key Thresholds`). |
| §4 | Authority & Citations | `Authority Level` + `Code Section` + `Source/Authority`, with links. |
| §5 | Application & Examples | Worked fact patterns; ties to `Taxpayer Type` / `Return/Form`. |
| §6 | Caveats & Gotchas | Expands `Notes/Gotchas`; edge cases, common mistakes. |
| §7 | Conflicts / Reconciliation | Only if `Conflict Flag` ≠ Clean — competing authorities + resolution. |
| §8 | Change log | Dated revision blocks (append-only), mirroring dossier §13. |

> **Pointer model:** the structured properties + `Summary` live in the Notion
> row (great for filtering/views); the **full body lives in the `.md`** and the
> row's `📄 KB Doc` points at it — no body duplication. This is the only change
> from how the DB works today (today the body lives in the Notion page itself).

---

## §4. Auto-flag + auto-create

**Make.com stays untouched** (CLAUDE.md rule #8): Make does any *watch/trigger*;
the *file-creation + pointer-stamp* step is the new part, and this spec defines
the contract it calls — it does not wire Make.

### You already have auto-flag — partly built
Your DB's existing views are flag queues:
- **⚠️ Conflict Queue** — entries with `Conflict Flag = Conflicting Sources`.
- **Planning Playbook** — `Timing/Phase = Planning`.
- Add a **Stale view** — `Last Reviewed` older than 12 months → re-review.

### Gap detector (new, modeled on `opportunity_flags.py`)
A rule-based scan that **flags missing or stale KB topics**:
- A strategy flagged `HIGH` across **N+ client dossiers** (§9) with **no KB entry
  whose `Topic`/`Code Section` matches** → flag "KB gap: create entry for X."
- An entry with `Conflict Flag = Needs Reconciliation` → flag for resolution.
- An entry with `Last Reviewed` > 12 months and `Status = Current` → flag stale.

The detector **flags**; you approve; then the create step runs — auto-flag,
human-gated create (same discipline as HIGH opportunity flags promoting to §7).

### Create step (the contract — what makes the file)
On an approved KB candidate:
1. Create/locate the DB row → Notion assigns **`Entry ID`**.
2. Render the `.md` from the §3 taxonomy, quoting that `Entry ID`.
3. Write it to `Tax-Knowledge/<Domain>/KB-<EntryID>_<topic-slug>.md`.
4. Set the row's **`📄 KB Doc`** = that file's URL; set `Last Reviewed` = today.

---

## §5. What I can build vs. what's yours (Make boundary)

| Piece | Who | Status |
| --- | --- | --- |
| This spec / taxonomy / naming, aligned to the real DB | me | ✅ done (this file) |
| Add the **`📄 KB Doc`** URL property to the live DB | me (on your go) | pending — it's a schema change to your DB |
| KB `.md` template (renderer) keyed off `Entry ID` | me | can add a `tax_kb/` module mirroring `execsumm_emails/` |
| Gap/stale detector modeled on `opportunity_flags.py` | me | can build as a classifier |
| Backfill `.md` files for the entries already in the DB | me (on your go) | one file per existing row |
| Make.com watch/trigger | **you** | I won't touch Make — I document the create-step contract it calls |

---

*Tax KB Library v1 — 2026-06-01. Written against the live "Tax Technical
Knowledgebase" (`857b8e97-7b2f-4b5c-9b0f-6f23300936d4`,
`collection://c1c33884-96fa-42a0-bf6c-6ac7776e26dd`). Supersedes the archived
"Tax Question System V2" proposal. Companion to `docs/DEFINITIONS_LIBRARY.md`.*
