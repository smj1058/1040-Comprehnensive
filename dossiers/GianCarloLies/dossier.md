# GianCarlo Lies — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | GianCarlo Lies |
| Client # | **07151219-01** |
| Mango Client ID | **937694** |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Depth mode | **Medium** — full Tax Ascend triple-tier (Insights + Planning + Compliance); Insights delivered; Planning memo sent; Compliance in progress with extension filed; 5 meetings on file; no email log entries; no reporting entities or Files & Links rows |
| Engagement Stage | Tax Ascend — Tax Insights (DELIVERED 2026-02-11) + Tax Planning (memo SENT 2026-03-05) + Tax Compliance (extension filed, 1040 in progress — K-1 collection phase) |
| Engagement Fee | **$9,500** (compliance) |
| Temperature | Active — full-scope Ascend client; Insights delivered; Planning memo sent; 1040 extended to 2026-10-15; K-1 collection phase active as of 2026-05-07 |
| Relationship Manager | Seth Johnson (per Account Hub ancestry) |
| Primary Contact | GianCarlo Lies · giancarlo.lies@gmail.com · (412) 657-8454 |
| Data Sources (this refresh) | Notion Accounts record · 1 Engagement Letter (Signed) · 1 Insights Project (DELIVERED) · 1 Tax Ascend record · 1 Tax Planning Session record · 1 Tax Compliance project (1040) · 1 Extension Status record · 5 Meetings Tracker rows (2 done, 3 cancelled/pending) · Email Addresses record · Exec Summary DB row |
| Files NOT Accessible This Refresh | PBC Workbook · Tax Extraction · Tax Planning Memo (top-level Account fields empty); Analysis Workbook + Extraction 1040 ARE linked on Insights Project; Tax Memo URL linked on Tax Ascend; Files & Links DB rows = 0 |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

GianCarlo Lies is an **individual 1040 taxpayer** on a **full Tax Ascend triple-tier engagement** — the only tier above the standard Insights + Compliance combo. He signed Tax Ascend on **2026-12-01** (date signed per Tax Ascend record) with all three tiers: **Tax Insights**, **Tax Planning**, and **Tax Compliance**, at a compliance engagement fee of **$9,500**. `[EL:GianCarlo]` `[Tax Ascend:GianCarlo]`

**Insights** ran to completion: kickoff and clarification activity in late January–early February 2026 despite two cancelled scheduling attempts, ultimately delivering on **2026-02-11** via a Tax Insights Delivery Call (Fathom recap on file). Analysis file and Extraction 1040 are linked on the Insights project record, and the SharePoint client folder is accessible. `[Insights:GianCarlo]` `[Meeting 2026-02-11]`

**Tax Planning** memo was drafted and **sent 2026-03-05** (Tax Memo Status = SENT), with the memo linked on the Tax Ascend record (SharePoint Word doc). `[Tax Ascend:GianCarlo §Tax Memo URL]` The Tax Planning Session tracker shows Meeting 1 as **"Reschedule (Missed Meeting)"** on 2026-04-17, with Meetings 2 and 3 status "To check" — meaning the planning review meetings have not yet been completed. The planning session is at **"step 5 (waiting for meeting)"** per Mango task status. `[TaxPlanning:GianCarlo]`

**Compliance** (1040, extended): Extension filed with **no payment required** (estimate shows likely refund) on **2026-04-15**, due date extended to **2026-10-15**. Current Mango stage is **"03 Collect and Review K-1s"** — the engagement is waiting on K-1s, which as of 2026-05-07 is the active gate. Form type: 1040. Preparer: Deontae Lafayette. Manager: Deontae/Seth. `[TaxComp:GianCarlo]` `[Ext:GianCarlo]`

**What matters right now.** The engagement is running well but has two open gates: (a) **K-1 collection** — the 1040 is stalled at stage 03 awaiting K-1s from whatever pass-through entities GianCarlo holds interests in (entities not yet surfaced in Reporting Entities DB); and (b) **Tax Planning delivery meeting** — memo has been sent, but the meeting to walk through recommendations was missed/rescheduled on 2026-04-17 and has not yet been completed. Both are 🔴 HIGH priority gates before the return can close. `[TaxComp:GianCarlo §Correct Status]` `[TaxPlanning:GianCarlo §Meeting 1 Status]`

**No email log entries** exist on the Account, and no Files & Links DB rows are linked — both are plumbing gaps given the client's engagement depth. The tax planning memo (SharePoint Word doc link on Tax Ascend) and the Insights artifacts are accessible via sidecar records but not surfaced on the Account's top-level fields. `[Accounts:GianCarlo §Tax Planning Memo]` `[Accounts:GianCarlo §PBC Workbook]`

---

## §2. Client Profile

| Item | Value | Confidence | Source |
| --- | --- | --- | --- |
| Account name | GianCarlo Lies | ✓ | `[Accounts:GianCarlo]` |
| Client # | 07151219-01 | ✓ | `[Accounts:GianCarlo]` |
| Mango Client ID | 937694 | ✓ | `[Accounts:GianCarlo]` |
| Email | giancarlo.lies@gmail.com | ✓ | `[Contact:GianCarlo]` `[EmailAddr:GianCarlo]` |
| Phone | (412) 657-8454 | ✓ | `[Contact:GianCarlo]` |
| Portal access | No (Portal Access = false) | ✓ | `[Contact:GianCarlo §Portal Access]` |
| Filing type | 1040 individual | ✓ | `[TaxComp:GianCarlo §Form Type]` |
| Engagement | Tax Ascend — Insights + Planning + Compliance (all three tiers) | ✓ | `[Tax Ascend:GianCarlo §TAX ASCEND TYPE]` |
| Date ascended | 2026-02-02 | ✓ | `[Tax Ascend:GianCarlo §Date Ascended]` |
| Date signed | 2025-12-01 | ✓ | `[Tax Ascend:GianCarlo §Date Signed]` |
| EL status | **Signed** · Extension — Accepted | ✓ | `[EL:GianCarlo §Engagement Letter Status]` `[EL:GianCarlo §Extension]` |
| Deposit | Paid ✓ | ✓ | `[EL:GianCarlo §Deposit Paid]` |
| Engagement fee | **$9,500** | ✓ | `[EL:GianCarlo §Price]` |
| Compliance Group Status | Pending Check | ✓ | `[EL:GianCarlo §Compliance Group Status]` |
| Mango portal | Portal Invite Sent | ✓ | `[EL:GianCarlo §Mango Portal Invite]` |
| PBC items | Received ✓ | ✓ | `[EL:GianCarlo §PBC list status]` |
| Relationship manager | Seth Johnson | ~ | `[Accounts:GianCarlo §Relationship Manager]` |
| Partner | Linked `30d4917287518141bf8acf3dca2654a7` | ~ | `[Accounts:GianCarlo §Partner]` |
| Reporting Entities | 0 (none populated) | ✓ | `[Accounts:GianCarlo §# of Reporting Entities]` |
| Entity category (1040) | Other | ✓ | `[TaxComp:GianCarlo §Entity Category]` |
| Tax planning session Mango status | step 5 (waiting for meeting) | ✓ | `[TaxPlanning:GianCarlo §Mango task Status]` |
| 1040 Mango status | In Progress | ✓ | `[TaxComp:GianCarlo §Mango Status]` |
| 1040 current stage | 03 Collect and Review K-1s | ✓ | `[TaxComp:GianCarlo §Correct Status]` |
| 1040 preparer | Deontae Lafayette | ✓ | `[TaxComp:GianCarlo §Preparer]` |
| Extension | Filed · No payment required · Due 2026-10-15 | ✓ | `[Ext:GianCarlo]` |
| Tax memo | SENT 2026-03-05 | ✓ | `[Tax Ascend:GianCarlo §TAX MEMO STATUS]` `[Tax Ascend:GianCarlo §Tax Memo Sent]` |

### Principals at a glance

- **GianCarlo Lies** — sole individual on Account; Primary Contact. Pittsburgh area (412 area code). Email confirmed: giancarlo.lies@gmail.com. No second spouse/partner on Account.

---

## §3. Email Intelligence

**0 email threads on Account.** No Client Email Log relation populated on Account `30d49172875181cfb584db6379a9eee1`; no `📧 Email Intelligence` subpage. The Engagement Letter tracker row carries `"PBC Emails Notes: Checking inboxes for email sent"` and `"Open items Status: None Sent"` suggesting some PBC coordination happened outside the tracked channels. The Extension Tracker row contains two Outlook attachments: `35_-_GianCarlo_Lies_-_Sent.msg` (extension notification) and `Extension_Payment_Request_-_Lies_GianCarlo.pdf`, confirming at least two emails went out for extension filing. The EL tracker notes: *"to confirm any uploads — Send email containing Temp PBC checklist from analysis file + mangoshare portal"* and *"Received PBC items"* — so PBC was eventually received even without logged threads. `[EL:GianCarlo §PBC Emails Notes]` `[EL:GianCarlo §PBC list status]` `[Ext:GianCarlo §Extensions Email sent]`

**Plumbing gap** → §7 Action: backfill email log via Outlook scan against giancarlo.lies@gmail.com / "Lies" patterns; check Make scenarios for why threads are not surfacing in Client Email Log.

---

## §4. Meeting History

**5 meetings on file — mostly cancelled; 2 completed.** The scheduling difficulty for clarification calls is notable.

| Date | Type | Time (EST) | Status | Recap | Notes | Source |
| --- | --- | --- | --- | --- | --- | --- |
| **2026-01-20** | Full Insights — Clarification call | 1:00 – 2:00 PM | Pending (labelled cancelled in notes) | LINK (not active URL) | "cancelled" | `[Meeting 2026-01-20]` |
| **2026-01-21** | Full Insights — Clarification call | 2:00 – 3:00 AM | Pending (labelled cancelled in notes) | LINK (not active URL) | "cancelled" | `[Meeting 2026-01-21]` |
| **2026-01-23** | Full Insights — Clarification call | 8:30 – 9:30 AM | Cancelled | — | "cancelled" | `[Meeting 2026-01-23]` |
| **2026-02-04** | Full Insights — Clarification call | 2:00 – 3:00 PM | **Done** ✓ | [Fathom](https://fathom.video/share/7bTsJQQueiaibKC3EfabjKCxMh-RjhCx) | "conflict. Declined" (prior slot) | `[Meeting 2026-02-04]` |
| **2026-02-11** | Tax Insights — Delivery Call | 2:00 – 3:00 PM | **Done** ✓ | [Fathom](https://fathom.video/share/W5gTyFwUDNT-qNffGVvJuEwVPzZbispm) | — | `[Meeting 2026-02-11]` |

**Cadence note:** Three failed scheduling attempts for a clarification call (Jan 20, 21, 23) before a successful one on Feb 4, followed by delivery on Feb 11 — a 22-day window from first attempt to delivery. The client showed scheduling difficulty early in the Insights cycle. Similarly, the Tax Planning meeting on 2026-04-17 was missed/rescheduled — consistent pattern of scheduling friction. `[Gap: Planning meeting not yet completed]`

**No restricted meetings** (0/5 restricted).

**Missing meeting type:** The Tax Planning session (Meeting 1 = 2026-04-17, "Reschedule") is tracked in the Tax Planning Session DB, not the Meetings Tracker — it does not appear as a formal Meetings Tracker row. Meetings 2 and 3 of the Planning session have no dates set. `[TaxPlanning:GianCarlo]`

---

## §5. Document Inventory

### 5.1 Engagement Letter

| Field | Value | Source |
| --- | --- | --- |
| Status | Signed | `[EL:GianCarlo §Engagement Letter Status]` |
| Extension | Accepted | `[EL:GianCarlo §Extension]` |
| Price | **$9,500** | `[EL:GianCarlo §Price]` |
| Deposit | Paid ✓ | `[EL:GianCarlo §Deposit Paid]` |
| Signed EL (Mangoshare) | [app.mangoshare.com/share/6222f4c16155a1d2185e42a](https://app.mangoshare.com/share/6222f4c16155a1d2185e42a) | `[EL:GianCarlo §Signed EL mangoshare]` |
| PBC list (SharePoint) | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQC9QxoqCIIMQLKhCgNLngkOASRe-PhOlz-jw7qnQhifgxU?e=5KpU8X) | `[EL:GianCarlo §PBC list link]` |
| PBC list status | **Received PBC items** ✓ | `[EL:GianCarlo §PBC list status]` |
| Mango project | Project Created · Portal Invite Sent | `[EL:GianCarlo §Mango Engagement/Project]` |
| Batch added | 2026-02-24 | `[EL:GianCarlo §Batch Added]` |
| Tax proposal | COMMITTED | `[EL:GianCarlo §TAX PROPOSAL]` |
| Entity services | Registered Agent Services | `[EL:GianCarlo §Entity Compliance services]` |

### 5.2 Insights Project Artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| **Analysis Workbook** (Counting file) | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBmD8AxICkwTan6Y3YJl_1JASi6d7Z9bCU1vr6H4shnqHw?e=MGkczF) | `[Insights:GianCarlo §Counting file]` |
| **Extraction 1040** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDEaNCQVfxzTIxklxOkEBlLAQwcC_YclEkoN974thNtnPU?e=HT55X2) | `[Insights:GianCarlo §Extraction 1040]` |
| **Client Folder (SharePoint)** | [SharePoint folder — GIANCARLO](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDr2OwthM0iRowZXKTlOL8eAaqybqGH3hB4H4vZQAmqZhM?e=AfzcOB) | `[Insights:GianCarlo §CLIENT FOLDER]` |
| **Delivery Call recording** | [Fathom](https://fathom.video/share/W5gTyFwUDNT-qNffGVvJuEwVPzZbispm) | `[Insights:GianCarlo §Meeting link]` `[Meeting 2026-02-11]` |
| Insights status | **DELIVERED** · Accelo Status: 04 Insights Delivered · Analysis: Completed | `[Insights:GianCarlo §Status (Precheck)]` |
| Date delivered | 2026-02-11 | `[Insights:GianCarlo §Date delivered]` |
| Mango status | To Check | `[Insights:GianCarlo §Mango Status]` |
| Temp Filter note | "Piah to do - analysis 04/29" | `[Insights:GianCarlo §Temp Filter]` (ops note — may indicate pending re-analysis) |

> **Plumbing gap.** Insights workbook URLs not synced to Account top-level fields (`Account.Tax Extraction`, `Account.PBC Workbook`, `Account.Tax Planning Memo` are all empty on the Account record). Same pattern as Spring Bengtzen and Alex Dykes — recurring system-wide sync issue. `[Accounts:GianCarlo §Tax Extraction]`

### 5.3 Tax Planning Memo

| Artifact | Link | Source |
| --- | --- | --- |
| **Tax Memo (SharePoint .docx)** | [SharePoint Word doc](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQBl8DGd6tadQriMQCLugzTVAb2I7-P-xCTrpjPVkoCYyDI?e=SecFf8) | `[Tax Ascend:GianCarlo §Tax Memo URL]` |
| Memo status | **SENT** · Sent date 2026-03-05 | `[Tax Ascend:GianCarlo §TAX MEMO STATUS]` `[Tax Ascend:GianCarlo §Tax Memo Sent]` |
| Planning meeting status | Meeting 1 reschedule (2026-04-17 missed) · Meetings 2 & 3 unscheduled | `[TaxPlanning:GianCarlo §Meeting 1 Status]` |

### 5.4 Compliance / Extension Artifacts

| Artifact | Detail | Source |
| --- | --- | --- |
| Extension email | `35_-_GianCarlo_Lies_-_Sent.msg` | `[Ext:GianCarlo §Extensions Email sent]` |
| Extension payment request | `Extension_Payment_Request_-_Lies_GianCarlo.pdf` — no payment required (likely refund) | `[Ext:GianCarlo §Payment Request sent]` |
| 1040 Mango ID | 1841872 | `[TaxComp:GianCarlo §Mango ID]` |
| Extended due | 2026-10-15 | `[TaxComp:GianCarlo §Extended Due]` |
| Original due | 2026-04-15 (extended) | `[TaxComp:GianCarlo §Original Due]` |

### 5.5 Files & Links DB rows

**0 rows** — no Files & Links entries exist for GianCarlo Lies. This is a plumbing gap; the Account's document footprint lives on the Insights Project, Tax Ascend, EL tracker, and Tax Compliance records but nothing has been centralized into the Files & Links DB. Note: no F&L URL collision with Spring Bengtzen (N/A — no rows to collide). `[Accounts:GianCarlo §→ Files & Links]`

---

## §6. Claude Work Product

**0 prior Claude Sessions** tied to GianCarlo Lies found via query of Claude Summaries DB (`collection://86dca8a4-3522-40c4-a568-b99bc98fc756`) or Claude Activity Log (`collection://f9cc7d05-26b0-4c77-b29c-af974a234b77`). This refresh creates the first Claude Summary log row for the Account.

This refresh's Claude Summary row will be created on Notion write step with: Thread Title `GianCarlo Lies — Client Intelligence Dossier Refresh — 2026-05-07` · Topics `File Review · Notion Build · Compliance · Tax Planning` · Account relation = `30d49172875181cfb584db6379a9eee1`.

---

## §7. Action Items — Rolled Up

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **Schedule and complete Tax Planning delivery meeting** — Meeting 1 was missed/rescheduled on 2026-04-17; memo has been sent since 2026-03-05 (63 days at refresh date with no meeting completed). Mango status "step 5 (waiting for meeting)" | Seth / Client | 🔴 HIGH | `[TaxPlanning:GianCarlo §Meeting 1 Status]` `[Tax Ascend:GianCarlo §Tax Memo Sent]` |
| 2 | **Collect K-1s** — 1040 is stalled at "03 Collect and Review K-1s." Client holds interests in pass-through entities (implied by K-1 stage; entities not yet surfaced in Reporting Entities DB). Until K-1s are received, preparation cannot advance | Deontae / Client | 🔴 HIGH | `[TaxComp:GianCarlo §Correct Status]` |
| 3 | **Identify and populate Reporting Entities** — 0 entities in Reporting Entities DB for this Account; the K-1 stage implies at least one pass-through entity. Surface entities from Insights workbook or PBC items and create Reporting Entities records | Sophia / Tax Team | 🟡 MED | `[Accounts:GianCarlo §# of Reporting Entities]` `[TaxComp:GianCarlo §Correct Status]` |
| 4 | **Backfill email log** — 0 email threads in Client Email Log despite active engagement (extension emails, PBC coordination confirmed in EL notes). Check Make scenarios + Outlook scan against giancarlo.lies@gmail.com | Generator / Accruity ops | 🟡 MED | `[§3]` |
| 5 | **Enable client portal access** — Portal Access = false on Contact record; portal invite was sent but access not confirmed. Verify client has logged in and can upload documents via Mangoshare | Sophia | 🟡 MED | `[Contact:GianCarlo §Portal Access]` `[EL:GianCarlo §Mango Portal Invite]` |
| 6 | **Sync Insights + Memo workbook URLs to Account top-level fields** — `Account.Tax Extraction`, `Account.PBC Workbook`, `Account.Tax Planning Memo` all empty despite documents being accessible via sidecar records (Insights project + Tax Ascend) | Accruity ops | 🟢 LOW (plumbing) | `[Accounts:GianCarlo §Tax Extraction]` |
| 7 | **Create Files & Links rows** for GianCarlo — currently 0 rows; documents are scattered across sidecars. Centralize SharePoint folder URL, Tax Memo URL, Extraction 1040, Analysis Workbook into F&L DB for discoverability | Accruity ops | 🟢 LOW (plumbing) | `[Accounts:GianCarlo §→ Files & Links]` |
| 8 | **Review "Piah to do - analysis 04/29" note** on Insights Project Temp Filter field — may indicate re-analysis or follow-on work item assigned to Piah (internal team member) that is not tracked elsewhere | Piah / Seth | 🟡 MED | `[Insights:GianCarlo §Temp Filter]` |
| 9 | **Confirm Registered Agent Services scope** — EL entity compliance services list "Registered Agent Services" — confirm which entity/state this covers and whether any deadline applies | Tax Team | 🟢 LOW | `[EL:GianCarlo §Entity Compliance services]` |
| 10 | **Pull and ingest Fathom transcripts** for 2026-02-04 Clarification call + 2026-02-11 Delivery call — surface Insights memo specifics (strategies, projections) | Generator / next refresh | 🟡 MED | `[Meeting 2026-02-04]` `[Meeting 2026-02-11]` |

Total: **10 open items** (2 HIGH, 5 MED, 3 LOW).

---

## §8. Tax Strategies & Projected Savings

**Partial data this refresh.** The Tax Planning Memo (SharePoint .docx) has been sent as of 2026-03-05 and is accessible via the Tax Ascend record URL, but has not been parsed/ingested in this session. The Insights Analysis Workbook and Extraction 1040 are also linked but not parsed. The table below reflects structural knowledge only — specific strategy details, savings projections, and entity-level recommendations require transcript + workbook ingestion on next refresh.

| Strategy | Status | Source |
| --- | --- | --- |
| Tax Insights analysis | **Delivered 2026-02-11**; specifics in Analysis Workbook + Fathom delivery transcript | `[Insights:GianCarlo §Date delivered]` `[Meeting 2026-02-11]` |
| Tax Planning memo | **Sent 2026-03-05**; memo at SharePoint Word doc URL; delivery meeting not yet completed | `[Tax Ascend:GianCarlo §TAX MEMO STATUS]` |
| K-1 / pass-through entity planning | `? Pending` — implied by "03 Collect and Review K-1s" stage; entities not surfaced yet | `[TaxComp:GianCarlo §Correct Status]` |
| Cost Seg | `? Pending workbook ingestion` — no properties in Reporting Entities; check Analysis Workbook | derived |
| S-Corp / entity planning | `? Pending workbook ingestion` — "Registered Agent Services" on EL suggests at least one entity; check Insights memo | `[EL:GianCarlo §Entity Compliance services]` |
| 2025 compliance | Extension filed no payment; likely refund; 1040 in progress; extended to 2026-10-15 | `[Ext:GianCarlo §Notes]` `[TaxComp:GianCarlo]` |
| Augusta Rule / accountable plan / retirement | `? Pending — not surfaced in available records` | — |

**Key insight from extension filing notes:** *"It shows you are likely to get a refund so we will file the extension with no payment."* This suggests GianCarlo's 2025 tax position is favorable (estimated refund), though the amount is not accessible without workbook ingestion. `[Ext:GianCarlo §Notes]`

Strategy specifics will populate fully on next refresh once the Tax Planning memo Word doc is parsed. The full strategy table will populate from the Analysis Workbook and the delivery call transcripts.

---

## §9. Opportunity Flags (auto-detected)

**Insufficient structured data for full classifier this refresh.** No Reporting Entities on Account → S-Corp classifier blocked. No property records → Cost Seg classifier blocked.

However, structural signals warrant flagging:

| Flag | Signal | Classifier | Priority | Source |
| --- | --- | --- | --- | --- |
| **Pass-through entity(ies) present** | 1040 at "K-1 collection" stage — at least one K-1-issuing entity | S-Corp / entity review | 🟡 MED — will escalate to HIGH once entity type confirmed | `[TaxComp:GianCarlo §Correct Status]` |
| **Registered Agent Services** on EL | Client engaged Registered Agent Services — implies entity existence | Entity structuring | 🟡 MED | `[EL:GianCarlo §Entity Compliance services]` |
| **Full triple-tier Ascend** | Client on highest tier (Insights + Planning + Compliance) at $9,500 — indicates complex tax situation above standard 1040 | Complexity flag | ~ | `[Tax Ascend:GianCarlo §TAX ASCEND TYPE]` |
| Cost Seg | No property data surfaced yet | Blocked | ? | — |
| S-Corp election | Entity type unknown yet | Blocked pending entity surfacing | ? | — |

**No HIGH flags promotable to §7 this refresh** — all flags blocked pending Reporting Entities population + workbook ingestion. Will run normally on next refresh once entities are surfaced from K-1s / PBC items.

---

## §10. Operations Analysis

GianCarlo Lies is a **full-scope Tax Ascend client** — the highest tier in Accruity's product stack — running a clean but partially stalled engagement as of 2026-05-07.

**Engagement health indicators:**
- Tax Insights delivered on schedule (Jan–Feb 2026 cycle, 22-day window from first attempt to delivery despite 3 scheduling misfires)
- Tax Planning memo sent 2026-03-05 — memo production was on-track
- Extension filed 2026-04-15 with no payment required (favorable position)
- PBC items received — good client compliance behavior
- 1040 preparation has begun (stage 03) with preparer Deontae assigned

**Two stall indicators:**
1. **Planning meeting never completed** — memo sent March 5, first meeting attempt April 17 was missed/rescheduled (43-day gap from memo to missed meeting). At refresh date May 7, 63 days have elapsed since memo was sent with no delivery meeting logged. This is the most visible engagement risk: the client received a planning memo but hasn't been walked through it.
2. **K-1 collection gate** — return is waiting on K-1s, which in May is reasonable timing (many K-1s don't arrive until late April/early May), but this needs active monitoring given the October 15 deadline.

**Scheduling friction pattern.** Three Jan–Feb scheduling cancellations for Insights clarification, and one April missed planning meeting, suggests GianCarlo may be a difficult scheduler or has an unpredictable calendar. The engagement team should use direct/assertive scheduling follow-ups.

**Financial posture.** $9,500 fee at the highest Ascend tier + "likely refund" for 2025 = a client with significant income/complexity but a favorable year. The Insights + Planning memo investment positions Accruity to surface multi-year savings.

**Strategic theme.** Get the planning delivery meeting completed before the summer lull. Once K-1s come in, Deontae can advance the return. The October 15 deadline is comfortable, but the planning meeting is the engagement activation lever — until it happens, the full value of the Insights + Planning investment hasn't been delivered to the client.

---

## §11. Individual Profile

| Dimension | Detail | Source |
| --- | --- | --- |
| Full name | GianCarlo Lies | `[Accounts:GianCarlo]` |
| Email | giancarlo.lies@gmail.com | `[Contact:GianCarlo]` |
| Phone | (412) 657-8454 | `[Contact:GianCarlo]` |
| Portal access | Not confirmed (invite sent, access = false) | `[Contact:GianCarlo §Portal Access]` |
| Filing type | 1040 individual | `[TaxComp:GianCarlo §Form Type]` |
| Filing status | ? — not surfaced in available records (no spouse on Account) | derived |
| Tax position (2025) | Likely refund (per extension estimate) | `[Ext:GianCarlo §Notes]` |
| Engagement tier | Highest — Insights + Planning + Compliance (triple-tier Tax Ascend) | `[Tax Ascend:GianCarlo §TAX ASCEND TYPE]` |
| Engagement fee | $9,500 | `[EL:GianCarlo §Price]` |
| Entity interests | Unknown (K-1s pending); Registered Agent Services on EL suggests at least one entity | `[TaxComp:GianCarlo §Correct Status]` `[EL:GianCarlo §Entity Compliance services]` |
| Scheduling behavior | Difficult — 3 cancelled Insights calls, 1 missed planning meeting | `[§4]` |
| Relationship risk | 🟡 MODERATE — missed planning meeting erodes perceived value; needs proactive re-engagement | derived |
| Outstanding to client | 2 HIGH items (Actions #1 + #2 in §7) | `[§7]` |

---

## §12. Provenance Index

### Notion — Account record
- `[Accounts:GianCarlo]` → [notion.so/30d49172875181cfb584db6379a9eee1](https://www.notion.so/30d49172875181cfb584db6379a9eee1) — client # 07151219-01, Mango 937694

### Notion — Exec Summary DB
- `[ExecSum:GianCarlo]` → [notion.so/33b491728751816d99b4c7e58b557ad1](https://www.notion.so/33b491728751816d99b4c7e58b557ad1) — existing row (empty body, empty properties except Summary Title and Account relation)

### Notion — Engagement Letter
- `[EL:GianCarlo]` → [notion.so/2ef491728751808bbd35ffd2d1cd1119](https://www.notion.so/2ef491728751808bbd35ffd2d1cd1119) — Signed · $9,500 · PBC received · Extension Accepted

### Notion — Tax Ascend
- `[Tax Ascend:GianCarlo]` → [notion.so/2f049172875180e58076da6174c51497](https://www.notion.so/2f049172875180e58076da6174c51497) — Triple-tier · Tax Memo SENT 2026-03-05

### Notion — Insights Project
- `[Insights:GianCarlo]` → [notion.so/2fd49172875180d0bb19fd427a2d90ed](https://www.notion.so/2fd49172875180d0bb19fd427a2d90ed) — DELIVERED 2026-02-11 · Analysis + Extraction 1040 on SharePoint

### Notion — Tax Planning Session
- `[TaxPlanning:GianCarlo]` → [notion.so/31949172875180b9be5ae539dc9e6be0](https://www.notion.so/31949172875180b9be5ae539dc9e6be0) — Meeting 1 Reschedule (2026-04-17) · Mango step 5

### Notion — Tax Compliance (1040)
- `[TaxComp:GianCarlo]` → [notion.so/d6b491728751823ab5ba8182997d7e7d](https://www.notion.so/d6b491728751823ab5ba8182997d7e7d) — Mango ID 1841872 · Stage 03 K-1 collection · Extended 2026-10-15

### Notion — Extension Tracker
- `[Ext:GianCarlo]` → [notion.so/342491728751815ea483ed7b8d4aaca9](https://www.notion.so/342491728751815ea483ed7b8d4aaca9) — Extension submitted · no payment · likely refund

### Notion — Meetings Tracker (5)
- `[Meeting 2026-01-20]` → [notion.so/2fb4917287518054b12beb7e70424dca](https://www.notion.so/2fb4917287518054b12beb7e70424dca) — Cancelled
- `[Meeting 2026-01-21]` → [notion.so/2fb49172875180a1b5bff47b975af518](https://www.notion.so/2fb49172875180a1b5bff47b975af518) — Cancelled
- `[Meeting 2026-01-23]` → [notion.so/2fb491728751804cb382fcd03f16a042](https://www.notion.so/2fb491728751804cb382fcd03f16a042) — Cancelled
- `[Meeting 2026-02-04]` → [notion.so/2fb4917287518012a4a5cfd47796a226](https://www.notion.so/2fb4917287518012a4a5cfd47796a226) — Done · [Fathom](https://fathom.video/share/7bTsJQQueiaibKC3EfabjKCxMh-RjhCx)
- `[Meeting 2026-02-11]` → [notion.so/304491728751809d8a29ca6ea5a02ca7](https://www.notion.so/304491728751809d8a29ca6ea5a02ca7) — Done · [Fathom](https://fathom.video/share/W5gTyFwUDNT-qNffGVvJuEwVPzZbispm)

### Notion — Contact / Email Address
- `[Contact:GianCarlo]` → [notion.so/30d49172875181328c83dcd9172bf702](https://www.notion.so/30d49172875181328c83dcd9172bf702) — Primary Contact · giancarlo.lies@gmail.com · (412) 657-8454
- `[EmailAddr:GianCarlo]` → [notion.so/2fc49172875180399ea4d69cdef5033b](https://www.notion.so/2fc49172875180399ea4d69cdef5033b) — Email addresses record

### Notion — Mango Project Tracker rows
- `[MangoTax:GianCarlo Compliance]` → [notion.so/34249172875181e2ae98feeca34b2016](https://www.notion.so/34249172875181e2ae98feeca34b2016) — 1040 GianCarlo Lies · Active · Tax Compliance · Billing partner Deontae
- `[MangoTax:GianCarlo Planning]` → [notion.so/34249172875181a99b13d3dd38e3e12b](https://www.notion.so/34249172875181a99b13d3dd38e3e12b) — Tax Planning GianCarlo Lies · Active · Manager Sophia

### SharePoint / Drive / Portals
- Signed EL Mangoshare: [app.mangoshare.com/share/6222f4c16155a1d2185e42a](https://app.mangoshare.com/share/6222f4c16155a1d2185e42a)
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQC9QxoqCIIMQLKhCgNLngkOASRe-PhOlz-jw7qnQhifgxU?e=5KpU8X)
- Client SharePoint folder: [SharePoint GIANCARLO](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDr2OwthM0iRowZXKTlOL8eAaqybqGH3hB4H4vZQAmqZhM?e=AfzcOB)
- Analysis Workbook: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBmD8AxICkwTan6Y3YJl_1JASi6d7Z9bCU1vr6H4shnqHw?e=MGkczF)
- Extraction 1040: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDEaNCQVfxzTIxklxOkEBlLAQwcC_YclEkoN974thNtnPU?e=HT55X2)
- Tax Planning Memo: [SharePoint Word doc](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQBl8DGd6tadQriMQCLugzTVAb2I7-P-xCTrpjPVkoCYyDI?e=SecFf8)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.** No prior dossier existed.

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- Full triple-tier Tax Ascend client (Insights + Planning + Compliance) · $9,500 EL Signed · deposit paid · PBC items received
- **Insights delivered** 2026-02-11 (Analysis Workbook + Extraction 1040 on SharePoint, Fathom delivery call on file)
- **Tax Planning memo SENT** 2026-03-05 (memo URL on Tax Ascend); planning delivery meeting NOT yet completed (Meeting 1 missed 2026-04-17, step 5 of planning workflow)
- **1040 compliance**: extension filed 2026-04-15 no payment (likely refund); current stage "03 Collect and Review K-1s"; extended due 2026-10-15; preparer Deontae Lafayette
- Contact confirmed: giancarlo.lies@gmail.com · (412) 657-8454

**New — discoveries:**
- ⚠️ **Planning meeting gap** — memo sent 63 days ago, no delivery meeting completed; highest-priority relationship risk
- ⚠️ **K-1 collection gate** — return blocked pending K-1s from unidentified pass-through entities
- 0 Reporting Entities in DB despite K-1 stage + Registered Agent Services on EL
- 0 Files & Links rows (no F&L URL collision — N/A)
- 0 email threads in Client Email Log despite confirmed email coordination
- **Scheduling friction pattern** — 3 cancelled Insights meetings + 1 missed planning meeting
- "Piah to do - analysis 04/29" note on Insights Project — untracked internal work item
- Portal Access = false despite invite sent — portal onboarding not confirmed

**Strategic theme:** Accruity has delivered substantial value (Insights + Planning memo at the highest tier) but the client hasn't yet received the full benefit (planning meeting not done). Getting the planning delivery meeting completed and K-1s in are the two unlock events for this engagement in 2026.

**Auto-detected flags:** 0 HIGH (blocked — no Reporting Entities); structural signals (K-1 stage + Registered Agent Services) warrant MED flags; will escalate once entities surfaced.

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 10 | Open action items (2 HIGH, 5 MED, 3 LOW) | §7 |
| 5 | Meetings on file (2 done, 3 cancelled) | §4 |
| 4 | Workbooks/documents accessible via sidecar records | §5.2–5.3 |
| 0 | Files & Links DB rows (F&L URL collision = N/A) | §5.5 |
| 0 | Email threads | §3 |
| 0 | Prior Claude sessions | §6 |
| 0 | Reporting Entities | §9 |

### 13.3 What a reader should look at first

1. **§7 Action #1** — Tax Planning delivery meeting: 63 days since memo sent, zero meetings completed. Call client now.
2. **§7 Action #2** — K-1 collection: confirm which entities are issuing K-1s and their expected receipt dates.
3. **§5.3** — Tax Planning Memo URL is directly accessible (SharePoint Word doc) — ingest and summarize on next refresh.
4. **§4** — Pull both Fathom transcripts (Feb 4 + Feb 11) on next refresh to surface Insights strategy specifics.

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/GianCarloLies/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: medium (triple-tier Ascend; Insights delivered; Planning memo sent; Compliance in progress; no email log; no Reporting Entities) · Next refresh: trigger on Planning delivery meeting completed OR K-1s received*
