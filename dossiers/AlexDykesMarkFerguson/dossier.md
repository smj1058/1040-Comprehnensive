# Alex Dykes & Mark Ferguson — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Alex Dykes & Mark Ferguson (joint household) |
| Client # | **01241311-01** |
| Mango Client ID | **939149** |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-04-22 |
| Prior Refresh | first run |
| Depth mode | **Medium** — clean Insights project cycle complete; basic compliance scope; no email log entries |
| Engagement Stage | Tax Ascend — Tax Insights (delivered 2026-03-04) → Compliance (extension accepted) |
| Engagement Fee | **$5,325** (compliance) + Insights project completed |
| Temperature | Active & on-track — full Insights cycle delivered, deposit paid, extension accepted, PBC items received |
| Relationship Manager | Seth Johnson (per Account Hub ancestry) |
| Primary Contact | Linked at `30d49172875181a8b77ffe107a0c9551` (details not surfaced — pending fetch) |
| Data Sources (this refresh) | Notion Accounts record · Engagement Letter (Signed/Executed) · Insights Project (DELIVERED) · 4 Meetings Tracker rows · 3 Files & Links rows · 1 Tax Ascend record · existing Exec Summary DB row |
| Files NOT Accessible This Refresh | PBC Workbook, Tax Planning Memo (top-level Account fields empty); but Analysis Workbook + Extraction 1040 + Tax Returns Folder ARE linked on the Insights Project record (§5) |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

Alex Dykes & Mark Ferguson are a **joint Accruity household** running on an Insights + Compliance engagement that has executed cleanly through 2026 Q1. The Tax Insights project ran a full ingestion-to-delivery cycle: kickoff **2026-01-27** → request list email **2026-02-06** due → received 2/2 files → clarifying call **2026-02-12** → first delivery call **2026-02-23** → final delivery call **2026-03-04**, with both Analysis Workbook and 1040 Extraction files delivered to SharePoint. `[Insights:Alex Dykes & Mark Ferguson]` On the compliance side: EL is **Signed** with Compliance Group Status **Executed**, deposit paid, extension **Accepted**, Mango portal status `Customer Accessed`, PBC items received. Engagement fee `$5,325`. `[EL:Alex Dykes & Mark Ferguson]`

**What matters right now.** Compared with Aidan (onboarding) or Spring/Tommy (HIGH-urgency open issues), this client is **operationally healthy with no flagged blockers** in the file. No HIGH-risk items in the email log (in fact, no email log entries on the Account at all). The post-Insights-delivery follow-up loop is the natural next stage — typical Accruity playbook would be either (a) act on Insights memo recommendations as part of 2025 return prep, or (b) re-engage on Tax Planning if scope expands. Neither is currently in flight per the file. `[Accounts:Alex Dykes & Mark Ferguson]`

**Discovery flag — data integrity.** The "Alex Dykes & Mark Ferguson" Files & Links DB row has `Document Inventory` and `PBC PDF Package` SharePoint URLs that are **byte-identical to Spring Bengtzen's same fields**. That's almost certainly a template-default that was never customized per client — likely affects an unknown number of other clients in the queue. Promoted to §7 plumbing as a system-wide flag (re-check on every subsequent client refresh). `[FL:Alex Dykes Document Inventory]` `[FL:Spring §Document Inventory]`

---

## §2. Client Profile

| Item | Value | Source |
| --- | --- | --- |
| Account name | Alex Dykes & Mark Ferguson (joint) | `[Accounts]` |
| Client # | 01241311-01 | `[Accounts]` |
| Mango Client ID | 939149 | `[Accounts]` |
| Engagement | Tax Ascend — Insights + Compliance | `[Tax Ascend]` `[Insights]` |
| EL status | **Signed · Executed** | `[EL §Engagement Letter Status]` `[EL §Compliance Group Status]` |
| Deposit | Paid ✓ | `[EL §Deposit Paid]` |
| Extension | **Accepted** ✓ | `[EL §Extension]` |
| Engagement fee | $5,325 | `[EL §Price]` |
| Mango portal | Customer Accessed ✓ | `[EL §Mango Portal Invite]` |
| PBC items | Received ✓ | `[EL §PBC list status]` |
| Insights status | **DELIVERED** (full cycle complete 2026-01-06 → 2026-03-04) | `[Insights]` |
| Files received | 2/2 | `[Insights §Received Files]` |

### Principals at a glance

- **Alex Dykes** — appears as primary on most Meetings Tracker rows (3 of 4 titled "Alex Dykes"); single-name framing in tracker
- **Mark Ferguson** — partner; appears jointly on the Feb 23 "Alex dykes and Mark ferguson" Tax Insights Delivery Call (Fellow recap); embedded EL PDF on file is named `2026-01-26-2025-FergusonA_(1).pdf`
- Filing status: joint household (likely MFJ — confirm)

---

## §3. Email Intelligence

**0 email threads on Account.** No Email Log relation populated; no `📧 Email Intelligence` subpage. The EL tracker row carries one Outlook attachment (`Alex_Dykes.msg`) and a `Tax Compliance Update_ 1_30.msg` PBC-open-items note attachment, but neither is synthesized as a thread.

**Plumbing gap** → §7 Action: backfill via Outlook scan against `Alex Dykes` / `Mark Ferguson` / `Ferguson` patterns; check Make scenarios.

---

## §4. Meeting History

**4 meetings on file — full Insights project cycle.** Append-only on next refresh.

| Date | Type | Time (EST) | Status | Recap | Source |
| --- | --- | --- | --- | --- | --- |
| **2026-01-26** | Full Insights — Kickoff Call | — | Done ✓ | [Fathom](https://fathom.video/share/cvE_QzdE3TWQzuaxtvv4Tyi-5P655WKF) | `[Meeting 2026-01-26 Kickoff]` |
| **2026-02-12** | Tax Insights — Clarification call | 10:30 – 11:30 AM | Done ✓ | [Fathom](https://fathom.video/share/32EgLFAqoW1vY6sYA4fb44SuQ-s-wzcc) | `[Meeting 2026-02-12 Clarification]` |
| **2026-02-23** | Tax Insights — Delivery Call (joint Alex + Mark) | 1:00 – 2:00 PM | Done ✓ | [Fellow](https://fellow.link/aRciEBZJ) | `[Meeting 2026-02-23 Delivery]` |
| **2026-03-04** | Tax Insights — Delivery Call (final) | — | Done ✓ | [Fathom](https://fathom.video/share/bZyX7FWJrhoJMuxJM6a9bd4Qdv2vUBmB) | `[Meeting 2026-03-04 Final Delivery]` |

**Cadence note:** 4 meetings inside a 38-day window (Jan 26 → Mar 4) = active Insights delivery project. Then 49-day silent period to refresh date. The Feb 23 + Mar 4 dual-delivery sequence is unusual — likely Feb 23 was the initial delivery, Mar 4 was the follow-up after client review. Pull both Fathom transcripts on next refresh to confirm. `[Gap: transcript ingestion]`

**Restricted flag**: 0/4 meetings restricted.

---

## §5. Document Inventory

### 5.1 Engagement Letter (clean state)

| Field | Value |
| --- | --- |
| Status | Signed · Executed |
| Price | **$5,325** |
| Deposit | Paid |
| Mangoshare signed EL | [app.mangoshare.com/share/4bc8808413f431ea52f5be9](https://app.mangoshare.com/share/4bc8808413f431ea52f5be9) |
| PBC folder (Mango) | [app.mangoshare.com/firm/5331/workspaces/939149/files/18425102/folder](https://app.mangoshare.com/firm/5331/workspaces/939149/files/18425102/folder) — Mango workspace `939149` matches Client Mango ID |
| PBC list (SharePoint xlsx) | [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDs7ZYMAN4sTbbVQHcg3Gh6ARoQFdpzlzgIViZC9EXfKo4?e=xXD6Ef) (Sent 2026-01-30) |
| Outlook attachment | `Alex_Dykes.msg` retained on tracker row |
| Open-items msg | `Tax Compliance Update_ 1_30.msg` |
| Embedded PDF | `2026-01-26-2025-FergusonA_(1).pdf` |

### 5.2 Insights Project artifacts (richest documentation on this account)

| Artifact | Link | Source |
| --- | --- | --- |
| **Analysis Workbook** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQB3ugtJqrhHR4adxDf6MqEoATd0XNoTSPbxAtsg8P49Y74?e=tYmcba) | `[Insights §Analysis Workbook]` |
| **Extraction 1040** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDZ2FHcWjjDTKDvFhhgj9ZOAVskttsrleHpDcLSgEUXbKs?e=pjeOXF) | `[Insights §Extraction 1040]` |
| **Request List Tracker** | [SharePoint Insights site xlsx](https://subledgesl.sharepoint.com/:x:/s/Insights/IQCb_31gnGJFQq3CGl1g8CHbAYa05hC2j8q3DAG5YaQSQiI?e=Bd0nla) | `[Insights §Request List]` |
| **Tax Returns Folder** | [SharePoint folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgAnOw2nF2LgQImFvviMME6uAeWKep2VIZ2oec1p9xcd80U?e=l4uEno) | `[Insights §Tax Returns Folder Link]` |
| **Insights site doc** | [SharePoint Insights](https://subledgesl.sharepoint.com/sites/Insights/_layouts/15/viewer.aspx?sourcedoc={47a96871-cc8b-439b-a9f5-d99c72e08271}) | `[Insights §Sharepoint Link]` |
| **Delivery Call recording** | [Fathom](https://fathom.video/share/bZyX7FWJrhoJMuxJM6a9bd4Qdv2vUBmB) (matches Mar 4 meeting row) | `[Insights §Meeting link]` |

> **Plumbing gap.** None of the Insights workbook URLs propagated up to the **Account record's** top-level fields (`Account.Tax Extraction`, `Account.PBC Workbook`, `Account.Tax Planning Memo` are all empty). Same pattern as Spring Bengtzen — promote to §7 as a recurring system-wide sync issue.

### 5.3 Files & Links rows (3) — with data-integrity flag

| Row | Name | URLs populated | Flag |
| --- | --- | --- | --- |
| `33b4…7775` | "Engagement Letter" | empty placeholder | — |
| `33b4…82c1` | "Executive Summary" | empty placeholder | — |
| `33b4…f79e` | "Alex Dykes & Mark Ferguson" | Document Inventory + PBC PDF Package | ⚠️ **URLs are byte-identical to Spring Bengtzen's same fields** — likely template defaults that were never per-client-customized |

The matching SharePoint URLs:
- Document Inventory: `IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw` (same on Spring + Alex)
- PBC PDF Package: `IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA` (same on Spring + Alex)

**This is a system-wide flag** — not client-specific. Add to §7 plumbing: every subsequent client refresh should check whether their Files & Links row has the same defaulted URLs, and flag if so for ops cleanup. Possibly all clients in the queue inherited template defaults that need swapping for actual client-specific folders. `[FL:Alex Dykes §Document Inventory]` `[FL:Spring §Document Inventory]`

---

## §6. Claude Work Product

**0 prior Claude sessions** tied to Alex Dykes & Mark Ferguson found via search of Claude Summaries DB and Claude Activity Log. This refresh creates the first Claude Summary log row.

This refresh's Claude Summary row will be created on Turn 11 with: Thread Title `Alex Dykes & Mark Ferguson — Client Intelligence Dossier Refresh — 2026-04-22` · Topics `File Review · Notion Build · Compliance · Tax Planning` · Account relation = canonical Account.

---

## §7. Action Items — Rolled Up

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **Pull Fathom transcripts** for 2026-01-26 / 2026-02-12 / 2026-03-04 + Fellow recap for 2026-02-23 — extract Insights memo recommendations | Generator / next refresh | 🟡 MED | `[§4]` |
| 2 | **Sync Insights workbook URLs (Analysis Workbook, Extraction 1040, Tax Returns Folder) up to Account.Tax Extraction / PBC Workbook / Tax Planning Memo** top-level fields — currently empty on Account record despite being populated on Insights project record | Accruity ops | 🟢 LOW (plumbing) | `[Accounts:Alex Dykes]` `[Insights]` |
| 3 | **System-wide check**: the Files & Links 'Alex Dykes & Mark Ferguson' row has Document Inventory + PBC PDF Package URLs IDENTICAL to Spring Bengtzen's. Likely template defaults across all clients — investigate scope and remediate | Accruity ops | 🟡 MED (data integrity) | `[FL:Alex Dykes]` `[FL:Spring]` |
| 4 | **Backfill email log** — 0 threads on Account; check Make scenarios + Outlook scan for Alex Dykes / Mark Ferguson / Ferguson patterns | Generator / Accruity ops | 🟢 LOW (plumbing) | `[§3]` |
| 5 | **Confirm joint-filing status** (MFJ vs domestic partner / single filings combined) | Sophia / Tax Team | 🟢 LOW | derived |
| 6 | **Determine post-Insights followup** — should the engagement extend into Tax Planning, or stay at Insights + Compliance only? Last meeting Mar 4 (49 days ago at refresh date) | Seth (RM) | 🟡 MED | `[§4]` |
| 7 | **Surface Primary Contact details** — primary contact relation `30d49172875181a8b77ffe107a0c9551` not enumerated; pull next refresh | Generator | 🟢 LOW | `[Accounts:Alex Dykes.Primary Contact]` |

Total: **7 open items** (0 HIGH, 3 MED, 4 LOW). Healthy posture.

---

## §8. Tax Strategies & Projected Savings

**Insights memo content not yet ingested this refresh.** The Analysis Workbook + Extraction 1040 are linked on the Insights project record but require fetching/parsing. What we know structurally:

| Strategy | Status | Source |
| --- | --- | --- |
| Insights memo recommendations | Delivered 2026-03-04; transcript pull will surface specifics | `[Insights §Delivery date]` |
| 2025 compliance | Extension accepted; PBC items received; preparation in progress | `[EL §Extension]` `[EL §PBC list status]` |
| Tax Planning extension (post-Insights) | `? Pending — conversation has not been initiated per file` | derived |

Strategy specifics (cost seg, S-corp, REPS, Augusta, accountable plan, retirement) are TBD until the Analysis Workbook is parsed or transcripts pulled. Full strategy table will populate on next refresh once those are accessible.

---

## §9. Opportunity Flags (auto-detected)

**Insufficient structured data this refresh.** No Reporting Entities populated on Account → S-Corp classifier blocked. No Property records → Cost Seg classifier blocked.

The Insights Analysis Workbook likely contains entity-level and property-level info — once parsed (next refresh, Drive-mounted env), the §9 classifier can run normally. **No HIGH flags promotable this refresh.**

---

## §10. Operations Analysis

This is a **clean Insights + Compliance engagement** with no surfaced operational stress. Key indicators:

- **Process velocity**: full Insights cycle Jan 6 → Mar 4 = 57 days (kickoff to final delivery) — solid execution
- **Engagement health**: deposit paid, EL Executed, extension Accepted, Mango portal accessed by client, PBC items received, Insights delivered
- **Quiet period**: 49 days since final delivery (Mar 4 → Apr 22) with no activity in the file — typical post-delivery dormancy or natural pause before 2025 return prep
- **Joint-household coordination**: Most meetings titled "Alex Dykes" only; the Feb 23 delivery call is the one explicitly joint Alex + Mark — confirming both spouses participate at delivery checkpoints

**Strategic theme.** Engagement is **healthy but quiet** — the natural inflection point is post-delivery: does Accruity reactivate to drive returns prep + planning, or does the relationship stay transactional? Next-meeting cadence and 2025 prep timeline are the visible levers.

---

## §11. Individual Profile

**§11.1 Alex Dykes** — primary in tracker rows; full profile pending email log + transcript ingestion. Outstanding items: 0 personally.

**§11.2 Mark Ferguson** — partner spouse; appears in joint Feb 23 Delivery Call. Embedded EL PDF named `Ferguson` suggests Ferguson is the lead surname for tax filing purposes.

Both appear engaged, responsive, and on-track. No relationship-risk signals in the file this refresh.

---

## §12. Provenance Index

### Notion — Account & DB rows
- `[Accounts:Alex Dykes & Mark Ferguson]` → [notion.so/30d49172875181a594bfeff1c8484430](https://www.notion.so/30d49172875181a594bfeff1c8484430)
- `[ExecSum:Alex Dykes & Mark Ferguson]` → [notion.so/33b49172875181e6970fe1f5731d23d5](https://www.notion.so/33b49172875181e6970fe1f5731d23d5) (existing — body has empty Activity Log header)
- `[EL:Alex Dykes & Mark Ferguson]` → [notion.so/2f84917287518025872ac085bbf7cfed](https://www.notion.so/2f84917287518025872ac085bbf7cfed) — Signed/Executed/$5,325
- `[Insights:Alex Dykes & Mark Ferguson]` → [notion.so/2fd49172875180a5aa99e30f39fa8f48](https://www.notion.so/2fd49172875180a5aa99e30f39fa8f48) — DELIVERED full cycle
- `[Tax Ascend:Alex Dykes]` → [notion.so/2f049172875180ccaf27f6e28318c1aa](https://www.notion.so/2f049172875180ccaf27f6e28318c1aa)

### Notion — Meetings Tracker (4)
- `[Meeting 2026-01-26 Kickoff]` → [notion.so/2fb4917287518006a7d5c5f32566596e](https://www.notion.so/2fb4917287518006a7d5c5f32566596e) — [Fathom](https://fathom.video/share/cvE_QzdE3TWQzuaxtvv4Tyi-5P655WKF)
- `[Meeting 2026-02-12 Clarification]` → [notion.so/2fb491728751806ca4ebff1bd00b3cca](https://www.notion.so/2fb491728751806ca4ebff1bd00b3cca) — [Fathom](https://fathom.video/share/32EgLFAqoW1vY6sYA4fb44SuQ-s-wzcc)
- `[Meeting 2026-02-23 Delivery]` → [notion.so/31049172875180489061d4f9b833fb77](https://www.notion.so/31049172875180489061d4f9b833fb77) — [Fellow](https://fellow.link/aRciEBZJ)
- `[Meeting 2026-03-04 Final Delivery]` → [notion.so/31949172875180b6853bfc03d40f9dda](https://www.notion.so/31949172875180b6853bfc03d40f9dda) — [Fathom](https://fathom.video/share/bZyX7FWJrhoJMuxJM6a9bd4Qdv2vUBmB)

### Notion — Files & Links (3)
- `[FL:Alex Dykes Engagement Letter]` → [notion.so/33b4917287518152bc97c7bcd58d5775](https://www.notion.so/33b4917287518152bc97c7bcd58d5775) (empty placeholder)
- `[FL:Alex Dykes Executive Summary]` → [notion.so/33b491728751812b9ed1d7510f8c82c1](https://www.notion.so/33b491728751812b9ed1d7510f8c82c1) (empty placeholder)
- `[FL:Alex Dykes]` → [notion.so/33b4917287518137bc1edf30abdff79e](https://www.notion.so/33b4917287518137bc1edf30abdff79e) (Document Inventory + PBC PDF Package — same URLs as Spring; flag)

### SharePoint / Drive
- Signed EL Mangoshare: [app.mangoshare.com/share/4bc8808413f431ea52f5be9](https://app.mangoshare.com/share/4bc8808413f431ea52f5be9)
- PBC folder Mango: [app.mangoshare.com/firm/5331/workspaces/939149/files/18425102/folder](https://app.mangoshare.com/firm/5331/workspaces/939149/files/18425102/folder)
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDs7ZYMAN4sTbbVQHcg3Gh6ARoQFdpzlzgIViZC9EXfKo4?e=xXD6Ef)
- Analysis Workbook: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQB3ugtJqrhHR4adxDf6MqEoATd0XNoTSPbxAtsg8P49Y74?e=tYmcba)
- Extraction 1040: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDZ2FHcWjjDTKDvFhhgj9ZOAVskttsrleHpDcLSgEUXbKs?e=pjeOXF)
- Tax Returns Folder: [SharePoint folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgAnOw2nF2LgQImFvviMME6uAeWKep2VIZ2oec1p9xcd80U?e=l4uEno)

### Cross-dossier references
- `[FL:Spring §Document Inventory]` → reference for the URL-collision flag (system-wide template-default issue)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.**

### 13.1 · 2026-04-22 · First-run baseline

**New — facts integrated:**
- Joint Accruity household (Alex Dykes + Mark Ferguson, joint household, joint compliance + Insights engagement)
- Engagement scope quantified: $5,325 EL Signed/Executed · deposit paid · extension accepted · PBC items received
- **Full Insights cycle complete** (Jan 6 → Mar 4 2026, 57 days kickoff-to-delivery, 4 meetings, 2/2 files received, Analysis Workbook + 1040 Extraction + Tax Returns Folder all on SharePoint)

**New — discoveries:**
- ⚠️ **Files & Links URL collision** — `Alex Dykes & Mark Ferguson` Files & Links row has Document Inventory + PBC PDF Package SharePoint URLs **byte-identical to Spring Bengtzen's**. Likely template defaults; system-wide flag promoted to §7 #3
- 0 emails on Account (plumbing #4)
- Insights workbook URLs not synced up to Account top-level fields (plumbing #2 — same pattern as Spring)
- 0 prior Claude sessions (this refresh creates the first)

**Strategic theme:** healthy-but-quiet engagement; natural inflection point post-Mar 4 delivery (49 days quiet at refresh date). Lever for Accruity: reactivate proactively for 2025 returns prep + Tax Planning extension, or stay transactional.

**Auto-detected flags:** 0 HIGH (insufficient structured data — Reporting Entities + Properties not populated); will run normally once Analysis Workbook is parsed.

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 7 | Open action items (0 HIGH, 3 MED, 4 LOW) | §7 |
| 4 | Meetings on file (full Insights cycle delivered) | §4 |
| 6 | Insights / SharePoint workbook URLs surfaced (not synced to Account top-level) | §5.2 |
| 1 | System-wide data-integrity flag (Files & Links template-default URL collision) | §5.3 |
| 0 | Email threads | §3 |
| 0 | HIGH opportunity flags this refresh | §9 |

### 13.3 What a reader should look at first

1. **§5.3 Files & Links URL collision flag** — **system-wide implication**, not just Alex Dykes. Worth a single ops sweep across all client Files & Links rows to remediate.
2. **§7 Action #6** — engagement health is solid; the question is whether to extend post-Insights into Tax Planning or stay transactional. RM call.
3. **§5.2 SharePoint workbook URLs** — already accessible via Insights project record; just need to be linked up to Account top-level fields for downstream readers.

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/AlexDykesMarkFerguson/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-04-22 · Depth mode: medium (Insights project rich, email log empty) · Next refresh: trigger on 2025 returns prep activation OR on Tax Planning re-engagement*
