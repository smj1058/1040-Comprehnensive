# Tax Knowledge Base — Library & Auto-Create Spec

**Companion to `docs/DEFINITIONS_LIBRARY.md`.** Where that file governs *client*
intelligence (dossiers, keyed by Client #), this one governs the **Tax Knowledge
Base (KB)** — reusable, client-agnostic tax knowledge, keyed by a **topic slug**.
It extends the existing **"Tax Question System V2"** spec
(`notion.so/33149172875181cf847aed6f3d5c0d0f`) by adding a **markdown-file + pointer**
layer so each KB entry can live as an `.md` file in SharePoint with the Notion
row pointing at it — the same model the dossiers use.

> **Assumptions to confirm (I had to guess these):**
> 1. The V2 spec page sits under "_Archive (Mirrored from Accruity)" — **confirm it's the current version**, not a stale copy.
> 2. SharePoint folder for the `.md` files — this spec assumes a new library at
>    `…/subledgesl…/Tax-Knowledge/<category>/` (the `subledge` tenant you mentioned). **Confirm the exact path.**
> 3. Whether KB bodies should live in the `.md` (pointer model, recommended) or stay as the Notion `Answer` property (your V2 spec's current approach). This doc proposes the pointer model; say if you'd rather keep it Notion-only.

---

## §1. Same pattern as the dossiers — different key

| | Client dossier | Tax KB entry |
| --- | --- | --- |
| **Durable key** | `Client #` + `Mango ID` (from Accounts) | **`Slug`** (kebab-case topic id) + `Category` |
| **File** | `dossiers/<Client>/dossier.md` + Drive | `Tax-Knowledge/<category>/<slug>.md` in SharePoint |
| **Pointer-of-record** | Exec Summaries DB row → `📄 Dossier` | Tax KB DB row → `📄 KB Doc` |
| **Header taxonomy** | §0 + §1–§13 | §0 key block + KB body sections (§3) |
| **Auto-flag source** | `opportunity_flags.py` (Cost Seg / S-Corp) | KB candidate detector (§4) |

The three-axis findability model from the definitions library applies
unchanged: **headers + slug inside the file** (primary), **Notion row +
properties** (pointer-of-record), **filename/path** (convenience). The `Slug` is
to a KB entry what `Client #` is to a dossier — the stable, stamped-in-file key
that makes it findable from any direction.

---

## §2. File naming & folder convention

```
Tax-Knowledge/
  entity-structure/
    s-corp-reasonable-comp.md
    entity-selection-criteria.md
  real-estate/
    cost-seg-criteria.md
    1031-exchange-mechanics.md
  partnership/
    k1-basis-tracking.md
  ...
```

- **One file per topic**, named `<slug>.md`. The slug is kebab-case, stable, and
  never reused for a different topic — it's the key.
- **Folder = category** (the 7 categories below), so the path also encodes the
  category for browsing/scoping.
- **Living document**, like the dossiers: the `.md` is updated in place; version
  history lives in git/SharePoint. The current state is always the file; the
  `Last Reviewed` date in §0 marks freshness (flag > 12 months old).
- Filename intentionally has **no date** — KB topics are durable; the review
  date lives inside (`Last Reviewed`), not in the name.

**Categories** (verbatim from the V2 spec, used as both the `Category` select and
the folder name):
`general` · `entity-structure` · `real-estate` · `partnership` ·
`sale-exit` · `irs-notice` · `like-kind-exchange`

---

## §3. KB entry `.md` header taxonomy

Every KB `.md` opens with a §0 key block (the searchable front matter), then the
body sections.

### §0 — Key block

| Field | Definition |
| --- | --- |
| **Title** | Short human title (= Notion `Name`). |
| **Slug** | The durable key, kebab-case (e.g. `s-corp-reasonable-comp`). **Stamped in-file — this is the lookup key.** |
| **Category** | One of the 7 categories (§2). |
| **Authority** | IRC sections, regs, IRS guidance (= `IRC / Authority`). |
| **Applies to** | Entity types / situations this is relevant for (e.g. "S-corp owner-operators with >$50k profit"). |
| **Source** | `Client Q&A` · `Seth Memo` · `External Research` · `Planning Strategy`. |
| **Confidence** | `High` · `Medium` · `Review Needed`. |
| **Last Reviewed** | ISO date; entries > 12 months flagged stale. |
| **Active** | `true`/`false` — `false` excludes from KB lookups. |
| **Related** | Slugs of related KB entries (the in-file form of `Linked Questions`). |

### KB body sections

| § | Header | Contents |
| --- | --- | --- |
| §1 | Question / Issue | The question(s) this entry answers, in plain terms. |
| §2 | Short Answer | 2–4 sentence direct answer (the bit Claude pulls as context). |
| §3 | Analysis | Full reasoning, conditions, thresholds, how to apply. |
| §4 | Authority & Citations | IRC/reg/ruling cites with links. |
| §5 | Examples | Worked examples / fact patterns. |
| §6 | Caveats & Edge cases | When it does *not* apply; common mistakes. |
| §7 | Change log | Dated revision blocks (append-only), mirroring dossier §13. |

---

## §4. Auto-flag + auto-create — how files get created

Two creation paths. **Both keep Make.com untouched** (CLAUDE.md rule #8): Make
does the *watch/trigger* you already specced; the *file-creation + pointer-stamp*
step is the new part (a Claude/Code step, or a Make "create file" call into a
documented contract — your choice). This spec defines the contract, not the Make
wiring.

### Path A — The flywheel (from your V2 spec)
A **Tax Question Response** is approved with **Add to KB** checked → a KB entry is
warranted. The create step:
1. Generate the `.md` from the approved answer using the §3 taxonomy; assign a `Slug`.
2. Write it to `Tax-Knowledge/<category>/<slug>.md`.
3. Create the Tax KB DB row (properties below) with `📄 KB Doc` = the file URL.
4. Link the Response → the new KB entry.

### Path B — Gap detector (new, modeled on `opportunity_flags.py`)
A rule-based scan that **flags missing KB topics** rather than waiting for a
question. Examples of flag rules:
- A strategy (e.g. **S-Corp election**, **Cost Seg**) is flagged `HIGH` across
  **N+ client dossiers** but has **no `Active` KB entry** for that slug → flag
  "KB topic gap: create `s-corp-reasonable-comp`."
- A `Seth Memo` exists in SharePoint with no corresponding KB entry → flag.
- An existing entry's `Last Reviewed` > 12 months → flag "stale, re-review."

The detector **outputs candidates** (it flags); a human (you) approves; then the
same create step (A1–A4) runs. Auto-flag, human-gated create — same shape as
HIGH opportunity flags auto-promoting to §7 but never auto-acting.

> **Seed set** (from your V2 spec, "5–10 entries from existing memos"):
> `s-corp-reasonable-comp`, `cost-seg-criteria`, `1031-exchange-mechanics`,
> `k1-basis-tracking`, `irs-notice-response-framework`,
> `entity-selection-criteria`, `bonus-depreciation-section-179`.

---

## §5. Tax KB Notion DB schema (pointer model)

Adopts your V2 spec's 11 properties and adds **two** for the file-pointer model:

| Property | Type | Notes |
| --- | --- | --- |
| Name | Title | Short title (V2). |
| **Slug** | Text | **NEW — the durable key**; matches the `.md` filename. |
| Category | Select | 7 categories (V2). |
| Question | Text (long) | The question it answers (V2). |
| Answer | Text (long) | **Synopsis only** under the pointer model — full body lives in the `.md`. (V2 used this as the full answer.) |
| IRC / Authority | Text | (V2) |
| Source | Select | (V2) |
| Confidence | Select | (V2) |
| Last Reviewed | Date | (V2) |
| Times Used | Number | (V2) |
| Active | Checkbox | (V2) |
| Linked Questions | Relation | Back-link to Tax Question records (V2). |
| **📄 KB Doc** | URL | **NEW — pointer to the `.md` in SharePoint.** The canonical body. |

> Pointer-only, exactly like the dossiers: the row points at the `.md`; the body
> is **not** duplicated into the Notion page. If you'd rather keep bodies in
> Notion (your V2 default), drop `📄 KB Doc` and keep `Answer` as the full text —
> but then you lose the SharePoint-file behavior you asked for.

---

## §6. What I can build vs. what's yours (Make boundary)

| Piece | Who | Status |
| --- | --- | --- |
| This spec / header taxonomy / naming | me | ✅ drafted (this file) |
| Tax KB DB created in Notion with the schema above | me (on your go) | pending your confirm |
| KB `.md` template (renderer) + slug rules | me | can add to `execsumm_emails/` or a new `tax_kb/` module |
| Gap detector (Path B), modeled on `opportunity_flags.py` | me | can build as a classifier |
| The Make.com watch/trigger (Path A flywheel) | **you** | **I won't touch Make** — I'll document the exact create-step contract it calls |

---

*Tax KB Library v1 (draft) — 2026-06-01. Built on "Spec: Tax Question System V2"
(`notion.so/33149172875181cf847aed6f3d5c0d0f`). Companion to
`docs/DEFINITIONS_LIBRARY.md`. Assumptions flagged at top — confirm before any
Notion DB or SharePoint folder is created.*
