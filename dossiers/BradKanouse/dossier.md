# Brad Kanouse — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Brad Kanouse (Wilhar LLC + 1040) |
| Client # | **02041105-02** (canonical, has all engagement data) |
| Mango Client ID | **937668** |
| Sibling Account | Client # 02041105-01 (Notion `30b49172…0c9854a1`) — has 2026-01-21 + 2026-01-28 Insights meetings linked but no engagement data; flagged 🔴 |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-04-22 |
| Prior Refresh | first run |
| Depth mode | **FULL** — Insights cycle DELIVERED, Tax Memo SENT, Tax Planning Session DELIVERED with full transcript (~$10K savings plan), 2 Cost Seg Proposal rows live, 2 emails (one with full strategy detail), 6 Meeting Action Items, S-Corp + Cost Seg + REPS all in scope |
| Engagement Stage | Tax Ascend — Insights ✓ delivered → Tax Planning ✓ delivered (memo sent 2026-02-10) → Tax Compliance (extension Accepted, PBC items received) → Cost Seg Estimate phase (proposal 2026-03-31) |
| Engagement Fee | **$3,275** (compliance EL) + Cost Seg study **$750** (discounted 50% from $1,500) |
| Temperature | Active & engaged — full ascend cycle complete, post-4/15 strategy execution pending |
| Relationship Manager | Seth Johnson (per Tax Planning Session transcript) |
| Primary Contact | Brad Kanouse · `brad@gowithbreeze.com` · (817) 726-2775 · Portal access: ❌ NO |
| Data Sources (this refresh) | 2 Notion Account records (1 marked To-Delete, 1 active — see §10) · EL tracker (Signed/Executed/$3,275) · Insights Project (DELIVERED 2026-01-29) · Tax Ascend (Memo SENT 2026-02-10, Bi-Annual planning) · Tax Planning Session (DELIVERED 2026-02-19, ~$10K savings) · 2 Cost Seg Proposal rows (parent + 5420 Juniper Dr sub-item) · 4 Meetings Tracker rows · 2 Email Log entries · 6 Meeting Action Items · 3 Files & Links rows · existing Exec Summary DB row |
| Files NOT Accessible This Refresh | Insights Counting File / Extraction 1040 SharePoint workbooks (linked on Insights project but not parsed here) · Tax Memo PDF (Tax Ascend SharePoint URL not fetched) · Cost Seg Estimate Fellow recap (Apr 13 forwarded email, body truncated) |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

**TL;DR.** Brad Kanouse is a **Kansas-based real estate broker (Go With Breeze) running Wilhar LLC as an S-Corp**, plus a 1099 side gig and a newly-acquired rental at 5420 Juniper Dr, Roeland Park KS. He has been through Accruity's **full Tax Ascend cycle** in 2026: Insights delivered 2026-01-29 → Tax Memo sent 2026-02-10 → Tax Planning Session delivered 2026-02-19 (Bi-Annual planning, Mango step 6) → Compliance EL Signed/Executed/$3,275 with extension Accepted, PBC items received, Mango portal `Customer Accessed`. Now in **Cost Seg Estimate phase** — proposal generated 2026-03-31 for the Juniper Dr property (~$40K bonus depreciation, $750 study). `[Tax Ascend:Brad Kanouse]` `[Insights:Brad Kanouse]` `[EL:Brad Kanouse]` `[TPS:Brad Kanouse]` `[CostSeg:Brad Kanouse parent]`

**The strategy stack quantified (§8 detail).** Per the 2026-02-19 Tax Planning transcript, the recommended bundle delivers **~$10,000 in 2025 tax savings**: $5,460 income tax + $2,540 payroll tax. Stack = (1) reduce W-2 from $6K/mo → $4K/mo (saves ~$2,500 payroll), (2) Solo 401k ~$12K/yr (Roth-rollover-capable provider TBD), (3) cost seg on Juniper Dr ($230K basis, ~$40K bonus dep, $750 fee), (4) accountable plan for home-office (10% of mortgage = $1,413.50/mo), (5) hire kids (ages 8 & 5) via 1099 up to $15K each, (6) REPS qualification confirmed (Brad is a real estate broker — full passive-loss unlock available). `[TPS Transcript 2026-02-19]`

**What matters right now.** Compared with Spring/Tommy (HIGH-urgency open issues) or Alex Dykes (post-Insights quiet), Brad is **mid-execution** — Insights + Planning are done, compliance is mid-flight (extension accepted, PBC received, surplus of $10,330 means no extension payment needed), and the next major lever is **Cost Seg Approval + Solo 401k + W-2 adjustment** post-4/15. Brad's 2026-04-11 reply email shows he is **engaged but confused** on (a) what "PY overpayment $5,165" means, (b) what "entity activity changes" means, and (c) what "other payments" means — Deontae owes him a clarifying reply (§7 #1, HIGH because it is post-4/15 and unanswered). `[Email 2026-04-11 Re: April 15]`

**Discovery flags.**
- **Duplicate Account record** — there are TWO Brad Kanouse rows in the Accounts DB. Canonical is `30d4…7ae335` (Client# 02041105-02, Mango 937668, marked `To Delete: YES` paradoxically) which has all engagement data; sibling `30b4…9854a1` (Client# 02041105-01, Mango blank, icon 🔴) carries 2 Insights meeting links + 2 Reporting Entities + 3 Tax Engagements + the existing Exec Summary row. The To-Delete-flagged record is the data-rich one. Promoted to §7 #1 (HIGH plumbing) and §10. `[Accounts:Kanouse-canonical]` `[Accounts:Kanouse-sibling]`
- **Files & Links URL collision** — Brad's "Brad Kanouse" Files & Links row carries Document Inventory + PBC PDF Package URLs **byte-identical to Spring Bengtzen's and Alex Dykes & Mark Ferguson's**. Confirms the system-wide template-default issue flagged on prior dossiers — at least 3 clients now demonstrably affected. Promoted to §7 #3. `[FL:Brad Kanouse]` `[FL:Spring]` `[FL:Alex Dykes]`
- **Portal Access flag** — Client Contacts record has `Portal Access: NO` despite EL `Mango Portal Invite: Customer Accessed` and AI-55 (Verify Brad has portal access) still `Not started`. Either the contact flag is stale, or there is a true mismatch. §7 #6. `[Contact:Brad Kanouse]` `[EL:Brad Kanouse §Mango Portal Invite]` `[AI-55]`

---

## §2. Client Profile

| Item | Value | Source |
| --- | --- | --- |
| Account name (canonical) | Brad Kanouse | `[Accounts:Kanouse-canonical]` |
| Client # | 02041105-02 | `[Accounts]` |
| Mango Client ID | 937668 | `[Accounts]` |
| Engagement | Tax Ascend — INSIGHTS + PLANNING + COMPLIANCE (full ascend) | `[Tax Ascend §TAX ASCEND TYPE]` |
| Tax Ascend planning cadence | **Bi-Annual** | `[Tax Ascend §Type of Planning]` |
| EL status | **Signed · Executed** | `[EL §Engagement Letter Status]` `[EL §Compliance Group Status]` |
| Deposit | Paid ✓ | `[EL §Deposit Paid]` |
| Extension | **Accepted** ✓ | `[EL §Extension]` |
| Engagement fee | $3,275 | `[EL §Price]` |
| Mango portal | Customer Accessed ✓ (but Contact record says Portal Access NO — see §10 flag) | `[EL §Mango Portal Invite]` |
| PBC items | Received ✓ (PBC list sent 2026-02-25) | `[EL §PBC list status]` |
| Insights status | **DELIVERED** 2026-01-29 | `[Insights §Insights]` `[Insights §date:Date delivered]` |
| Tax Memo | **SENT** 2026-02-10 | `[Tax Ascend §TAX MEMO STATUS]` `[Tax Ascend §date:Tax Memo Sent]` |
| Planning Status | **Tax Planning Delivered** | `[Tax Ascend §Planning Status]` |
| Tax Planning Session | DELIVERED 2026-02-19 (Mango step 6: meeting delivered) | `[TPS §Mango task Status]` |
| Date Signed (Tax Ascend) | 2026-02-02 | `[Tax Ascend §date:Date Signed]` |
| Date Added (EL batch) | 2026-01-30 | `[EL §date:Batch Added]` |

### Principal at a glance

- **Brad Kanouse** — primary; real estate broker at **Go With Breeze** (`gowithbreeze.com`); Wilhar LLC (S-Corp) generates net profit of **$21K** (2025) on **$765K total expenses** including **$48K** contractor + W-2 to Brad. Owns rental at 5420 Juniper Dr, Roeland Park KS 66205 (purchased Feb 2025, $230K, $11K new roof). Two children ages **8 and 5**. Wife has W-2 wages. AGI $78,734 (2025 projected). REPS-qualifying via real-estate broker hours. `[TPS Transcript 2026-02-19]` `[Email 2026-04-11]` `[CostSeg:5420 Juniper]`
- **Phone:** (817) 726-2775 (Texas area code despite KS residency — historical) `[Contact:Brad Kanouse]`
- **Email:** brad@gowithbreeze.com `[Contact:Brad Kanouse]`
- **Filing context:** appears to be MFJ given wife's W-2 + two children dependents; not explicitly tagged but consistent with transcript

### Entities & properties known

| Entity / Property | Type | Status | Source |
| --- | --- | --- | --- |
| **Wilhar LLC** | S-Corp (Brad's brokerage operating co; flips income flows here) | Active; books well-organized; 2025 prep waiting for 1040 | `[TPS 2026-02-19]` |
| **Go With Breeze** | DBA / brokerage brand (Wilhar LLC d/b/a) | Active | `[Email 2026-04-11 §From]` |
| **5420 Juniper Drive, Roeland Park KS 66205** | Rental property (KS-located) | Purchased 2025-02-19 for $230K (20% down, $178K mortgage); $11K new roof; cost seg estimate phase | `[CostSeg:5420 Juniper]` `[TPS §Cost segregation]` |
| Future LLC (proposed) | Real-estate-holding LLC (separate from Wilhar S-Corp) | Recommended in TPS — not yet stood up | `[TPS §Real estate structure]` |

> **State filing complexity.** Brad domiciled in MO (broker activity) with rental in KS — Tax Team must split returns: rental income → KS, brokerage/service income → MO. Confirmed in TPS. `[TPS §Real estate structure (46:44)]`

---

## §3. Email Intelligence

**2 email log entries on canonical Account.** Both surface a single live thread plus a Fellow-meeting forwarded recap. No `📧 Email Intelligence` subpage on the Account.

### 3.1 Active threads

| # | Date | Subject | Direction | From | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **2026-04-11** | **Re: April 15 — You're Covered for 2025** | Inbound | brad@gowithbreeze.com | 🟡 Medium | **Open — Deontae owes reply** |
| 2 | 2026-04-13 | FW: Brad Kanouse - Cost Seg Estimate on Mar 31 - Key decisions inside | Inbound | Exchange DN sender (Fellow recap fwd) | 🟡 Medium | Reference / archived |

### 3.2 Thread #1 — "Re: April 15 — You're Covered for 2025" (2026-04-11)

**The pivotal active thread.** Brad responds to Deontae's pre-4/15 status email with three direct questions:

1. *"What does 'changes in Wilhar or entity activity' mean?"* — Brad notes he only has his real estate agent business + rental house + side gigs; nothing has materially changed.
2. *"What does 'other payments' refer to?"*
3. *"What's the 'prior year overpayment of $5,165'?"* — Brad recalls receiving an IRS refund last year and does not understand the "overpayment" framing.

**Tax math sent to Brad (Deontae's original):**
- Wilhar net profit: **$21,000**
- AGI: **$78,734** · federal tax: $1,175
- W-2 withholding: $6,340 · PY overpayment applied: $5,165 · **Total payments: $11,505**
- **Estimated surplus: $10,330** — no 4/15 extension payment needed ✓

**Strategy backlog (post-4/15) referenced in thread:**
- Reduce W-2 to $4K/mo (saves $2,500 payroll)
- Solo 401k ~$12K
- Cost seg on 5420 Juniper Dr ($230K basis, $40K bonus dep, $750 study)

**Participants:** Brad → Deontae Lafayette (cc: Tax@accruity, Seth Johnson, Sophia Leonardo, Stacy Cvengros). Open since 2026-04-11. `[Email 2026-04-11]`

### 3.3 Thread #2 — Cost Seg Estimate Fellow recap (forwarded)

Forwarded 2026-04-13 to portal as part of batch archive. Body truncated in fetch; references the **2026-03-31 Cost Seg Estimate meeting** (Touchbase type, Fellow recap [link](https://urldefense.proofpoint.com/v2/url?u=https-3A__sg5.fellow.app_uni_ls_click)). Cross-walks to Meetings Tracker row `3344917287518045aa0cc2f501434fb5`. `[Email 2026-04-13 Cost Seg]`

### 3.4 Email gaps & plumbing

- **Tax Insights** kickoff (2026-01-21) and Insights delivery (2026-01-28) emails — not in log; only meeting recap fathom links surface them
- **Tax Memo Sent** (2026-02-10) — no email log row; presumably `[Tax Ascend §Tax Memo URL]` was sent via Outlook but not captured by Make
- **EL/PBC sequence** emails (`Brad_Kanouse.msg`, `RE__2025_Taxes-Docs_on_portal.msg`) are retained as EL tracker attachments but not on Account email log
- **Cost Seg Proposal** delivery / signing — no email yet; AI-53 (Send cost seg intake form) is `Not started` per Meeting Action Items

→ §7 plumbing: backfill via Outlook scan for `brad@gowithbreeze.com` / `Kanouse` / `Wilhar` patterns.

---

## §4. Meeting History

**4 meetings on file across 70 days (2026-01-21 → 2026-03-31).** All `Done`. Append-only on next refresh.

| Date | Type | Time (EST) | Status | Restricted | Recap | Account linkage | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **2026-01-21** | Full Insights — **Clarification call** | 3:30 – 4:00 PM | Done ✓ | No | [Fathom](https://fathom.video/share/zs_S261jTjV4vpGBr6Z_Qx7srxK4q8BF) | sibling 🔴 record | `[Meeting 2026-01-21 Clarification]` |
| **2026-01-28** | Full Insights — **Delivery call** | 3:30 – 4:30 PM | Done ✓ | No | [Fathom](https://fathom.video/share/sCdBuQxe1rTA_im37HF3Ekiz2zQvFzWy) | sibling 🔴 record | `[Meeting 2026-01-28 Delivery]` |
| **2026-02-19** | **Tax Planning Session** | 2:30 – 3:00 PM | Done ✓ | No | [Fellow](https://fellow.link/5sgXNOvP) | canonical record | `[Meeting 2026-02-19 TPS]` |
| **2026-03-31** | Touchbase (Cost Seg Estimate) | 4:30 – 5:00 PM | Done ✓ | No | [Fellow](https://urldefense.proofpoint.com/v2/url?u=https-3A__sg5.fellow.app_uni_ls_click) | canonical record | `[Meeting 2026-03-31 Touchbase]` |

**Cadence note.** Two Insights meetings inside 7 days (1/21 + 1/28) = clean kickoff-to-delivery sprint. Then 22 days to Tax Planning Session (2/19). Then 40 days to Cost Seg touchbase (3/31). All within healthy Tax Ascend rhythm. `[§4]`

**Restricted flag**: 0/4 meetings restricted.

**Plumbing flag** (§7 #1 / §10): the two Insights meeting rows (1/21 + 1/28) link to the **sibling 🔴 Account record** (Client# 02041105-01), while the Tax Planning Session and Touchbase link to the **canonical record** (Client# 02041105-02). When the duplicate is reconciled, ensure these meetings re-point.

### 4.1 Tax Planning Session deep-dive (2026-02-19, 30 min, full Fellow transcript)

**The richest single artifact in the file.** Mango step 6 (delivered). Memo sent 2026-02-10 (per Tax Ascend). Topics surfaced (verbatim from transcript):

- **W-2 wage optimization** — Brad currently $6K/mo since June 2025 ($72K/yr); recommended $4K/mo ($48K/yr); ~$2,500 payroll tax savings
- **Solo 401k** — $23,500 employee + 25% employer (~$10K) capacity; recommended ~$12K target; Roth-rollover-capable provider needed (Brad over $300K threshold may need backdoor Roth)
- **Cost seg study** — 5420 Juniper Dr; $230K purchase Feb 2025; ~$40K bonus dep; $750 promo (50% off normal $1,500); 5-yr/15-yr/39-yr breakdown; 20-30% qualifies for 100% bonus
- **Real estate structure** — REPS qualified ✓; do NOT use S-Corp to buy real estate; spin up separate LLC for RE; flipping income → S-Corp via mgmt fee (avoid 15.3% SE tax)
- **State allocation** — KS for rental, MO for brokerage (Brad's domicile)
- **Home office** — 10% of mortgage = $1,413.50/mo; accountable plan reimbursement (S-Corp friendlier than Sched C)
- **Augusta Rule** — flagged by Seth as more heavily scrutinized; needs strong substantiation
- **Hiring kids** — ages 8 & 5; up to $15K/yr each via 1099 (NOT payroll); standard deduction shields tax; deposit to education / HYSA
- **Total projected savings** — ~$10K (= $5,460 income + $2,540 payroll)
- **Wilhar 2025** — $21K net profit on $765K expenses; $48K paid to Brad; books clean; business return waits for 1040
- **Next call cadence** — mid-April 2026 quarterly; **Brad has portal access concerns** (AI-55 Not started)

**Action items captured (6, all Not started as of refresh):** see §7.

---

## §5. Document Inventory

### 5.1 Engagement Letter (clean state)

| Field | Value |
| --- | --- |
| Status | Signed · Executed |
| Price | **$3,275** |
| Deposit | Paid |
| Extension | Accepted (Ext Email Sent: `RE__2025_Taxes-Docs_on_portal.msg`) |
| Mangoshare signed EL | [app.mangoshare.com/share/feddbf4584607d8b0fd47445](https://app.mangoshare.com/share/feddbf4584607d8b0fd47445) |
| PBC folder (ImagineTime) | [app.imaginetime.com/firm/5331/workspaces/937668/files/18524212/folder](https://app.imaginetime.com/firm/5331/workspaces/937668/files/18524212/folder) — workspace `937668` matches Mango ID |
| PBC list (SharePoint xlsx) | [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQApagVi_XcjSJudnsEEF9KAAeqbc4yqEVMMQ1IfDvSKlOk?e=IDz2Zg) (Sent 2026-02-25) |
| Open Items / Ext Email | `RE__2025_Taxes-Docs_on_portal.msg` (retained as attachment) |
| Outlook EL email | `Brad_Kanouse.msg` (retained as attachment) |
| Tax Memo (SharePoint .docx) | [SharePoint](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQCxhhBRRLWoSbs2AM4qMakDAXJqNyMd8cNfUzI28nFL7Gg?e=4OwZ4G) — sent 2026-02-10 |

### 5.2 Insights Project artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| Counting File | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBEJ0Vr_xRHT4a_AscSiEi7AR7BOVdeGOwA47ArKvPJMyw?e=JPXksJ) | `[Insights §Counting file]` |
| Extraction 1040 | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCWo4zl9FbLQpi27pG11VV1ATNe6U5oCCyYZoKl-rqsXnM?e=1NCDmQ) | `[Insights §Extraction 1040]` |
| Insights delivery (Fathom) | [fathom.video/sCdBuQxe1rTA_im37HF3Ekiz2zQvFzWy](https://fathom.video/share/sCdBuQxe1rTA_im37HF3Ekiz2zQvFzWy) | `[Insights §Meeting link]` |
| Insights status | DELIVERED · Analysis Completed · Tax Team Checked ✓ | `[Insights]` |
| Date delivered | 2026-01-29 | `[Insights §date:Date delivered]` |

> **Plumbing gap** (same pattern as Spring + Alex). The Insights workbook URLs above are linked on the Insights project record but **not propagated up to the Account top-level fields** (`Account.Tax Extraction`, `Account.PBC Workbook`, `Account.Tax Planning Memo` are all empty on the canonical Brad Kanouse record). System-wide ops issue. → §7 #4. `[Accounts:Kanouse-canonical]` `[Insights:Brad Kanouse]`

### 5.3 Tax Ascend / Tax Planning artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| Tax Memo (delivered 2026-02-10) | [SharePoint .docx](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQCxhhBRRLWoSbs2AM4qMakDAXJqNyMd8cNfUzI28nFL7Gg?e=4OwZ4G) | `[Tax Ascend §Tax Memo URL]` |
| Tax Planning Session (Fellow recap) | [fellow.link/5sgXNOvP](https://fellow.link/5sgXNOvP) | `[TPS §Meeting 1 Link]` |
| TPS Mango Status | step 6 (meeting delivered) | `[TPS §Mango task Status]` |

### 5.4 Cost Seg Proposal artifacts

| Artifact | Detail | Source |
| --- | --- | --- |
| **Parent proposal row** | `34a4917287518098986cc369bacccae1` — Status: New - Enter in Portal · Approve: NO | `[CostSeg:Brad Kanouse parent]` |
| **Sub-item — 5420 Juniper Drive** | Roeland Park, KS 66205 · Purchase Date 2025-02-19 · Purchase Price $230,000 · Status: New - Enter in Portal · Approve: NO | `[CostSeg:5420 Juniper]` |
| Estimated bonus dep (per TPS) | ~$40,000 | `[TPS §Cost segregation]` |
| Study fee | $750 (50% promo from $1,500) | `[TPS §Cost segregation]` |
| Cost Seg Estimate meeting | 2026-03-31 — Touchbase, Fellow recap | `[Meeting 2026-03-31]` |
| Email forwarded to portal | 2026-04-13 (FW Cost Seg Estimate Key decisions) | `[Email 2026-04-13]` |

### 5.5 Files & Links rows (3) — with data-integrity flag

| Row | Name | URLs populated | Flag |
| --- | --- | --- | --- |
| `33b4…8730` | "Engagement Letter" | empty placeholder | — |
| `33b4…b0ef` | "Executive Summary" | empty placeholder | — |
| `33b4…aa96` | "Brad Kanouse" | Document Inventory + PBC PDF Package | ⚠️ **URLs are byte-identical to Spring Bengtzen's AND Alex Dykes & Mark Ferguson's same fields** — confirmed system-wide template-default issue |

The matching SharePoint URLs:
- Document Inventory: `IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw` (same on Spring + Alex + Brad)
- PBC PDF Package: `IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA` (same on Spring + Alex + Brad)

**Now confirmed across 3 clients** — every dossier should keep checking and tally. `[FL:Brad Kanouse]` `[FL:Spring]` `[FL:Alex Dykes]`

---

## §6. Claude Work Product

**0 prior Claude sessions** tied to Brad Kanouse found via search of Claude Summaries DB. This refresh creates the first Claude Summary log row.

This refresh's Claude Summary row will be created on Turn 11 with:
- Thread Title: `Brad Kanouse — Client Intelligence Dossier Refresh — 2026-04-22`
- Topics: `File Review · Notion Build · Compliance · Tax Planning · Cost Seg`
- Account relation: canonical Brad Kanouse Account (`30d4…7ae335`)

**Existing Exec Summary DB row** (`33b49172875181bc8c41ffb62a1f16c9`) has one Activity Log entry already:
- 2026-04-09 — Cost Seg Estimate — 5420 Juniper Dr, Roeland Park KS — referenced page `33d4917287518116a7dac9058ec04848` (not fetched this refresh; surface next pass)

> Note: the existing Exec Summary row is parented to the **sibling 🔴 Account record** (`30b4…9854a1`), not the canonical record. Either re-parent or re-create on canonical (§7 #1 reconciliation).

---

## §7. Action Items — Rolled Up

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **Reconcile duplicate Account records** — canonical `30d4…7ae335` (Client# 02041105-02, marked `To Delete: YES` paradoxically) carries all engagement data; sibling 🔴 `30b4…9854a1` (Client# 02041105-01) carries 2 Insights meetings + 2 Reporting Entities + 3 Tax Engagements + Exec Summary row. Decide canonical, merge meeting links + Reporting Entities + Tax Engagements + Exec Summary row, then delete the loser | Accruity ops / Seth | 🔴 **HIGH (data integrity)** | `[Accounts:Kanouse-canonical]` `[Accounts:Kanouse-sibling]` |
| 2 | **Reply to Brad's 4/11 questions** — clarify (a) PY overpayment $5,165 concept, (b) "entity activity changes" definition, (c) "other payments." Open since 2026-04-11; Brad is engaged but stuck. Post-4/15 strategy momentum at risk | Deontae | 🔴 HIGH | `[Email 2026-04-11]` |
| 3 | **System-wide check confirmed across 3 clients**: Files & Links Document Inventory + PBC PDF Package URLs IDENTICAL across Spring + Alex Dykes + Brad. Sweep all client Files & Links rows; remediate template defaults | Accruity ops | 🟡 MED (data integrity) | `[FL:Brad]` `[FL:Spring]` `[FL:Alex]` |
| 4 | **Sync Insights workbook URLs (Counting File, Extraction 1040, Tax Memo) up to canonical Account.Tax Extraction / PBC Workbook / Tax Planning Memo** — currently empty on Account record | Accruity ops | 🟡 MED (plumbing) | `[Accounts:Kanouse-canonical]` `[Insights]` `[Tax Ascend]` |
| 5 | **AI-50** Brad to send 2025 budget spreadsheets + P&L to tax@accruity.com | Brad Kanouse (Client) | 🟡 MED | `[AI-50]` |
| 6 | **AI-51** Adjust W-2 from $6K/mo → $4K/mo; remainder as distributions (saves ~$2,500) | Brad Kanouse (Client) | 🔴 HIGH (per AI-51 Priority field) | `[AI-51]` |
| 7 | **AI-52** Send Solo 401k provider recommendations + comparison doc | Seth (Accruity) | 🟡 MED | `[AI-52]` |
| 8 | **AI-53** Send cost segregation intake form for Roeland Park rental | Seth (Accruity) | 🟡 MED — proposal already drafted but Approve: NO; intake → approve loop | `[AI-53]` `[CostSeg:5420 Juniper]` |
| 9 | **AI-54** Brad to set up Solo 401k by 2026-12-31 | Brad Kanouse (Client) | 🟡 MED | `[AI-54]` |
| 10 | **AI-55** Verify Brad's portal access — Contact record says Portal Access: NO; EL says Customer Accessed; reconcile | Seth (Accruity) | 🟡 MED | `[AI-55]` `[Contact]` `[EL §Mango Portal Invite]` |
| 11 | **Cost Seg Proposal approval loop** — both Cost Seg Proposal rows have `Approve: NO` and `Status: New - Enter in Portal`; advance approve → engagement | Seth / Cost Seg ops | 🟡 MED | `[CostSeg:Brad Kanouse parent]` `[CostSeg:5420 Juniper]` |
| 12 | **Spin up separate LLC for real estate** (per TPS recommendation) — current Juniper Dr title path unclear; Wilhar S-Corp should not hold RE | Brad Kanouse (Client) | 🟢 LOW | `[TPS §Real estate structure]` |
| 13 | **State allocation prep** — 2025 returns will need MO + KS split (rental income → KS, brokerage income → MO); flag for prep team | Tax Team | 🟢 LOW | `[TPS §Real estate structure (46:44)]` |
| 14 | **Augusta Rule substantiation** — if Brad plans to use, document 14-day business events with stronger evidence | Brad / Tax Team | 🟢 LOW | `[TPS §Augusta Rule]` |
| 15 | **Hiring kids documentation** — if Brad implements $15K/kid via 1099, document tasks and ensure IRS-defensible | Brad Kanouse (Client) | 🟢 LOW | `[TPS §Additional tax strategies]` |
| 16 | **Backfill email log** — Insights kickoff/delivery emails, Tax Memo Sent (2/10), Cost Seg intake email all missing from Account email log; Make scenario coverage gap | Accruity ops | 🟢 LOW (plumbing) | `[§3.4]` |

**Total: 16 open items (3 HIGH, 8 MED, 5 LOW).** Active engagement with execution levers; HIGH cluster centers on data hygiene + Brad's open questions.

---

## §8. Tax Strategies & Projected Savings

**Source: 2026-02-19 Tax Planning Session transcript (Fellow recap [link](https://fellow.link/5sgXNOvP)) + 2026-04-11 email recap.**

| # | Strategy | Mechanism | Projected Savings | Status | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | **W-2 reduction (Wilhar)** | $6K/mo → $4K/mo; remainder as S-Corp distributions; required reasonable comp ~30-33% of net | **~$2,500/yr payroll** (15.3% FICA on $24K reclassified) | 🟡 Open — AI-51 (HIGH, Not started) | `[TPS §W-2 wage optimization]` |
| 2 | **Solo 401k** | $12K target; employee + employer match; Roth-rollover-capable provider; deductible by S-Corp filing deadline | Tax-deferred ~$12K @ marginal rate; deferral, not pure savings | 🟡 Open — AI-52 (Seth) + AI-54 (Brad due 2026-12-31) | `[TPS §Solo 401k planning]` |
| 3 | **Cost Seg — 5420 Juniper Dr** | $230K basis; 5/15/39-yr split; 20-30% bonus-eligible | **~$40,000 bonus depreciation** at REPS rates ≈ $5,460 income tax (TPS-stated) | 🟡 Open — proposal drafted, Approve: NO; AI-53 sends intake form; $750 study fee (50% promo) | `[TPS §Cost segregation]` `[CostSeg:5420 Juniper]` |
| 4 | **Accountable plan (home office)** | S-Corp reimburses 10% of mortgage = $1,413.50/mo + utilities; book-to-tax adjustment | Quantify on extraction; cleaner than Sched C 8829 | 🟡 In design | `[TPS §Home office deductions]` |
| 5 | **Hiring kids (8 & 5)** | Up to $15K/kid via 1099 (NOT payroll); standard deduction shields tax | Up to ~$30K family deduction at marginal rate | 🟢 Strategy presented; not yet implemented | `[TPS §Additional tax strategies (33:29)]` |
| 6 | **REPS election + rental loss unlock** | Brad's broker hours qualify; lets full cost-seg loss offset active income | Synergistic with #3 — cost seg savings only realize fully under REPS | ✓ Qualifying — confirmed in TPS | `[TPS §Real estate structure (51:04)]` |
| 7 | **Augusta Rule (14-day rental)** | Rent home to S-Corp 14 days/yr at FMV; shielded from income | Optional; Seth flagged elevated IRS scrutiny — needs documentation | 🟢 Optional / on-hold | `[TPS §Augusta Rule]` |
| 8 | **State allocation (MO + KS)** | Split rental income to KS, brokerage to MO domicile-based | No new $ savings; compliance correctness | 🟡 Built into 2025 prep | `[TPS §Real estate structure (46:44)]` |
| 9 | **Separate LLC for RE** | Spin RE-holding LLC distinct from Wilhar S-Corp | Structural cleanup; protects S-Corp from RE basis issues | 🟢 Proposed | `[TPS §Real estate structure (56:11)]` |

**Aggregate quantified savings (per TPS slide):** **~$10,000 in 2025** = $5,460 income tax + $2,540 payroll tax. Excludes Solo 401k deferral and longer-tail items. `[TPS §Additional tax strategies (42:37)]`

**Compliance status:**
- 2025 1040: extension Accepted; PBC items received; surplus $10,330 → no payment due 4/15 ✓
- Wilhar S-Corp 2025: books clean; draft can be prepared; **wait to file until personal return ready** (avoid amendment loop) `[TPS §Business overview (01:02:01)]`

---

## §9. Opportunity Flags (auto-detected)

Rule-based flags from `execsumm_emails/opportunity_flags.py` patterns:

| Flag | Trigger | Brad's status | Confidence |
| --- | --- | --- | --- |
| **HIGH — S-Corp election** | Schedule-C-only entity earning enough to merit S-Corp + reasonable comp | ✓ **Already elected** (Wilhar LLC = S-Corp); strategy is ongoing W-2 calibration, not election | ✓ Confirmed |
| **HIGH — Cost Seg eligibility** | Owned rental + REPS-likely + basis ≥ ~$200K | ✓ **MET** — $230K basis, REPS-qualifying broker, KS rental | ✓ Confirmed (proposal drafted) |
| **HIGH — REPS qualification** | Real estate broker / agent hours ≥ 750 + > 50% time | ✓ **MET** — Brad confirmed real estate broker hours per TPS | ✓ Confirmed |
| **HIGH — Solo 401k unfunded** | S-Corp owner + W-2 + no current 401k = available deferral | ✓ **MET** — Brad has no current 401k; ~$12K capacity recommended | ✓ Confirmed |
| **MED — Hiring kids strategy** | Children under 18 + business owner | ✓ MET — ages 8 & 5 | ✓ |
| **MED — Augusta Rule** | Owns primary residence + has S-Corp | ✓ MET; on-hold per IRS scrutiny note | ~ |
| **MED — Accountable plan** | S-Corp + home office | ✓ MET — 10% mortgage allocation in motion | ✓ |
| **LOW — Separate RE LLC** | Owns RE through S-Corp or personally where structure matters | ✓ MET — structurally desirable | ✓ |

**HIGH-flag count: 4** — Cost Seg, REPS, Solo 401k, S-Corp wage calibration. Three of four are already in execution; the W-2 calibration (HIGH per AI-51) is the most actionable.

---

## §10. Operations Analysis

**Brad Kanouse is the cleanest exemplar of a full-Tax-Ascend client this batch.** Indicators:

- **Process velocity**: Insights kickoff → Insights delivery (1/21 → 1/28, 7 days) → Tax Memo sent (2/10, 13 days post-delivery) → TPS delivered (2/19, 9 days post-memo) = textbook ascend cadence
- **Engagement health**: deposit paid · EL Executed · extension Accepted · Mango portal Customer Accessed · PBC items received · all 6 TPS action items captured · cost seg proposal drafted within 40 days of TPS
- **Brad's posture**: high engagement (replied to 4/11 status email same day), articulates real questions, understands strategy stack at a high level, uses Quicken, maintains his own books — strong DIY profile augmented by Accruity
- **Wilhar S-Corp health**: $21K net profit on $765K expenses; well-organized books per Seth's TPS commentary
- **Breeze brokerage backdrop**: Brad's brokerage business (Go With Breeze) is the WHY behind REPS qualification — material time + active broker hours

**Operational risks surfaced this refresh:**

1. **Duplicate Account records.** Canonical (Client# 02041105-02) marked `To Delete: YES` while sibling 🔴 (Client# 02041105-01) is `To Delete: NO`. The To-Delete-tagged record holds all engagement data; the keeper holds Reporting Entities + Tax Engagements + the existing Exec Summary row. Either the To-Delete flag is inverted, or someone intended to merge but the merge never executed. **HIGH** — cannot proceed safely on data ops without reconciling. `[§7 #1]`
2. **Brad's open questions** (4/11 email) un-replied as of refresh. Material risk: Brad may execute strategies (W-2 reduction, Solo 401k) without clarity on his prior-year tax posture, or may stall entirely. **HIGH** — Deontae owes reply. `[§7 #2]`
3. **Cost Seg Proposal not yet approved.** Both rows `Approve: NO` and `Status: New - Enter in Portal`. The 3/31 Touchbase produced a Fellow recap (forwarded 4/13) but no signed engagement. Stalled at intake-form-not-sent gate (AI-53 Not started). `[§7 #8]`
4. **Portal Access mismatch.** Contact record says NO; EL says Customer Accessed; AI-55 Not started. Either the record is stale or there is a true access issue. `[§7 #10]`
5. **Files & Links template-default URL collision** — confirmed across 3 clients now. Spring + Alex + Brad all have identical Document Inventory + PBC PDF Package URLs. System-wide. `[§7 #3]`

**Strategic theme.** Brad is a **high-yield client** — small Wilhar net profit but full ascend buy-in, multiple HIGH opportunity flags already engaged, REPS-qualifying which unlocks the cost seg play. Lever for Accruity: **clear his 4/11 questions promptly, advance Cost Seg approval, send Solo 401k provider doc.** Three small unblocking moves capture the projected $10K/yr savings.

---

## §11. Individual Profile

**§11.1 Brad Kanouse** — single principal on this dossier.

- **Profession**: Real estate broker at Go With Breeze (`gowithbreeze.com`); operating co Wilhar LLC (S-Corp); REPS-qualifying via broker hours
- **Geography**: domicile MO (assumed per TPS state-allocation discussion); rental in KS (5420 Juniper Dr, Roeland Park 66205); phone Texas area code (817) suggests TX origin
- **Family**: Wife earns W-2; two children ages 8 and 5
- **Financial snapshot (2025 projected)**: AGI $78,734 · federal tax $1,175 · W-2 withholding $6,340 · PY overpayment $5,165 · total payments $11,505 · estimated surplus $10,330 — **no 4/15 extension payment due**
- **Wilhar 2025**: $21K net profit on $765K total expenses; $48K in contractor + W-2 to Brad; books clean per Seth
- **Tools**: Quicken for payroll/books; uses Outlook (`brad@gowithbreeze.com`); detailed P&L spreadsheets shared monthly per TPS
- **Outstanding personally**: AI-50 (send 2025 budgets/P&L) · AI-51 (W-2 adjustment, HIGH) · AI-54 (Solo 401k by 2026-12-31) — 3 client-owned items
- **Posture**: engaged, responsive (same-day reply 4/11), but **needs handholding on tax math vocabulary** (PY overpayment, "entity activity changes" — phrasing landed unclear)

**Risk signal**: Brad's 4/11 questions express genuine confusion, not pushback. Resolve quickly to preserve the trust momentum built via Insights + TPS. `[Email 2026-04-11]`

---

## §12. Provenance Index

### Notion — Account & DB rows
- `[Accounts:Kanouse-canonical]` → [notion.so/30d4917287518144a26add85b37ae335](https://www.notion.so/30d4917287518144a26add85b37ae335) — Client# 02041105-02 · Mango 937668 · marked To Delete: YES (paradox)
- `[Accounts:Kanouse-sibling]` → [notion.so/30b49172875181c4bfb0d9130c9854a1](https://www.notion.so/30b49172875181c4bfb0d9130c9854a1) — Client# 02041105-01 · 🔴 icon · holds existing Exec Summary + 2 Reporting Entities + 3 Tax Engagements + Insights meetings
- `[ExecSum:Brad Kanouse]` → [notion.so/33b49172875181bc8c41ffb62a1f16c9](https://www.notion.so/33b49172875181bc8c41ffb62a1f16c9) — parented to sibling record; has 1 Activity Log entry (2026-04-09 Cost Seg)
- `[EL:Brad Kanouse]` → [notion.so/2fb491728751803dbd3cf2c8a5e8503e](https://www.notion.so/2fb491728751803dbd3cf2c8a5e8503e) — Signed/Executed/$3,275/Extension Accepted
- `[Tax Ascend:Brad Kanouse]` → [notion.so/2f049172875180368aecd8367c9edb3d](https://www.notion.so/2f049172875180368aecd8367c9edb3d) — TAX INSIGHTS + PLANNING + COMPLIANCE; Memo SENT 2/10; Bi-Annual planning
- `[Insights:Brad Kanouse]` → [notion.so/2f549172875180478a54e6ee96b195b6](https://www.notion.so/2f549172875180478a54e6ee96b195b6) — DELIVERED 2026-01-29 · Tax Team Checked
- `[TPS:Brad Kanouse]` → [notion.so/2fc49172875180d29b57cbe56238ec4e](https://www.notion.so/2fc49172875180d29b57cbe56238ec4e) — Tax Planning Session DELIVERED 2026-02-19 · Mango step 6
- `[Contact:Brad Kanouse]` → [notion.so/30d4917287518135ba15d18c8af18991](https://www.notion.so/30d4917287518135ba15d18c8af18991) — primary, brad@gowithbreeze.com, (817) 726-2775, Portal Access: NO

### Notion — Cost Seg Proposals (2)
- `[CostSeg:Brad Kanouse parent]` → [notion.so/34a4917287518098986cc369bacccae1](https://www.notion.so/34a4917287518098986cc369bacccae1) — parent row, Approve: NO
- `[CostSeg:5420 Juniper]` → [notion.so/35249172875180278426f8547484b7d9](https://www.notion.so/35249172875180278426f8547484b7d9) — sub-item, $230K purchase 2025-02-19, Approve: NO

### Notion — Meetings Tracker (4)
- `[Meeting 2026-01-21 Clarification]` → [notion.so/2fb4917287518000863ac66c95f3a979](https://www.notion.so/2fb4917287518000863ac66c95f3a979) — [Fathom](https://fathom.video/share/zs_S261jTjV4vpGBr6Z_Qx7srxK4q8BF) — links to sibling
- `[Meeting 2026-01-28 Delivery]` → [notion.so/2fb4917287518045b15bfedeb92f479f](https://www.notion.so/2fb4917287518045b15bfedeb92f479f) — [Fathom](https://fathom.video/share/sCdBuQxe1rTA_im37HF3Ekiz2zQvFzWy) — links to sibling
- `[Meeting 2026-02-19 TPS]` → [notion.so/30c49172875180ddad4af400255bbd9b](https://www.notion.so/30c49172875180ddad4af400255bbd9b) — [Fellow](https://fellow.link/5sgXNOvP) — links to canonical
- `[Meeting 2026-03-31 Touchbase]` → [notion.so/3344917287518045aa0cc2f501434fb5](https://www.notion.so/3344917287518045aa0cc2f501434fb5) — [Fellow](https://urldefense.proofpoint.com/v2/url?u=https-3A__sg5.fellow.app_uni_ls_click) — links to canonical

### Notion — Email Log (2)
- `[Email 2026-04-11]` → [notion.so/342491728751815d9c11edd67e7f8b9a](https://www.notion.so/342491728751815d9c11edd67e7f8b9a) — Re: April 15 — You're Covered for 2025 · Inbound from brad@gowithbreeze.com · Risk Medium
- `[Email 2026-04-13 Cost Seg]` → [notion.so/34249172875181408b7cde75ff493b69](https://www.notion.so/34249172875181408b7cde75ff493b69) — FW Cost Seg Estimate Key decisions · forwarded recap

### Notion — Meeting Action Items (6)
- `[AI-50]` → [notion.so/3354917287518167a7d0f56faed60241](https://www.notion.so/3354917287518167a7d0f56faed60241) — Send budgets + P&L (Brad, Normal)
- `[AI-51]` → [notion.so/335491728751819a817af95c0926c018](https://www.notion.so/335491728751819a817af95c0926c018) — Adjust W-2 $6K→$4K (Brad, **High**)
- `[AI-52]` → [notion.so/33549172875181ce8facc79956244b87](https://www.notion.so/33549172875181ce8facc79956244b87) — Send Solo 401k provider doc (Seth, Normal)
- `[AI-53]` → [notion.so/33549172875181b18a57e84ac10f1934](https://www.notion.so/33549172875181b18a57e84ac10f1934) — Send cost seg intake (Seth, Normal)
- `[AI-54]` → [notion.so/3354917287518173ba8cc9718b38c674](https://www.notion.so/3354917287518173ba8cc9718b38c674) — Brad to set up Solo 401k by 2026-12-31 (Brad, Normal)
- `[AI-55]` → [notion.so/3354917287518177b427c935838af193](https://www.notion.so/3354917287518177b427c935838af193) — Verify Brad's portal access (Seth, Normal)

### Notion — Files & Links (3)
- `[FL:Brad Kanouse Engagement Letter]` → [notion.so/33b4917287518198b2e2e5d6bff08730](https://www.notion.so/33b4917287518198b2e2e5d6bff08730) — empty placeholder
- `[FL:Brad Kanouse Executive Summary]` → [notion.so/33b49172875181cdbd5dec54fdf2b0ef](https://www.notion.so/33b49172875181cdbd5dec54fdf2b0ef) — empty placeholder
- `[FL:Brad Kanouse]` → [notion.so/33b49172875181ae957bc39d30d5aa96](https://www.notion.so/33b49172875181ae957bc39d30d5aa96) — Document Inventory + PBC PDF Package — same URLs as Spring & Alex (template-default flag)

### SharePoint / Drive / Mango
- Signed EL Mangoshare: [app.mangoshare.com/share/feddbf4584607d8b0fd47445](https://app.mangoshare.com/share/feddbf4584607d8b0fd47445)
- PBC folder ImagineTime: [app.imaginetime.com/firm/5331/workspaces/937668/files/18524212/folder](https://app.imaginetime.com/firm/5331/workspaces/937668/files/18524212/folder)
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQApagVi_XcjSJudnsEEF9KAAeqbc4yqEVMMQ1IfDvSKlOk?e=IDz2Zg)
- Tax Memo: [SharePoint .docx](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQCxhhBRRLWoSbs2AM4qMakDAXJqNyMd8cNfUzI28nFL7Gg?e=4OwZ4G)
- Counting File: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBEJ0Vr_xRHT4a_AscSiEi7AR7BOVdeGOwA47ArKvPJMyw?e=JPXksJ)
- Extraction 1040: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCWo4zl9FbLQpi27pG11VV1ATNe6U5oCCyYZoKl-rqsXnM?e=1NCDmQ)

### Cross-dossier references
- `[FL:Spring §Document Inventory]` and `[FL:Alex Dykes §Document Inventory]` — peer references for the URL-collision flag (now confirmed across 3 clients)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.**

### 13.1 · 2026-04-22 · First-run baseline

**New — facts integrated:**
- Brad Kanouse = solo principal; KS rental + MO domicile (assumed); two children (8, 5); wife W-2; REPS-qualifying broker (Go With Breeze)
- Wilhar LLC S-Corp · 2025 net profit $21K on $765K expenses · $48K to Brad
- Engagement scope quantified: $3,275 EL Signed/Executed · deposit paid · extension Accepted · PBC received · Mango Customer Accessed
- **Full Tax Ascend cycle complete**: Insights delivered 2026-01-29 · Tax Memo sent 2026-02-10 · Tax Planning Session delivered 2026-02-19 (Bi-Annual) · TPS Mango step 6
- 2025 1040 surplus $10,330 (no 4/15 payment due) · AGI $78,734
- Cost Seg proposal drafted for 5420 Juniper Dr ($230K basis, ~$40K bonus dep, $750 study) — Approve: NO at refresh date
- 6 Meeting Action Items captured from TPS · 4 meetings on file · 2 emails on log

**New — discoveries:**
- 🔴 **HIGH — Duplicate Account record** (canonical paradoxically marked To-Delete; sibling holds the existing Exec Summary row, Reporting Entities, and Tax Engagements). §7 #1
- 🔴 **HIGH — Brad's 4/11 questions** unanswered (PY overpayment, entity activity, other payments). §7 #2
- 🟡 **Files & Links URL collision now confirmed across 3 clients** (Spring + Alex + Brad). §7 #3
- 🟡 **Insights workbook URLs not synced to Account top-level fields** — same pattern as Spring + Alex. §7 #4
- 🟡 **Portal Access mismatch** between Contact record (NO) and EL (Customer Accessed). §7 #10
- 4 HIGH opportunity flags (Cost Seg, REPS, Solo 401k, S-Corp wage calibration) — three already in motion

**Strategic theme:** mid-execution full-ascend client; **~$10K/yr savings stack** documented; three small unblocking moves (clarify 4/11 email, advance Cost Seg approval, send Solo 401k provider doc) capture the value.

**Auto-detected flags:** **4 HIGH** flags promotable (Cost Seg, REPS, Solo 401k, S-Corp wage calibration); confidence high — all confirmed in TPS transcript.

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 16 | Open action items (3 HIGH, 8 MED, 5 LOW) | §7 |
| 4 | Meetings on file (full ascend cycle) | §4 |
| 2 | Email Log threads (1 active, 1 archived recap) | §3 |
| 6 | Tax Planning Action Items (AI-50 → AI-55) | §7 #5–10 |
| 9 | Tax strategies stacked (~$10K/yr savings) | §8 |
| 4 | HIGH opportunity flags promotable | §9 |
| 2 | Cost Seg Proposal rows (parent + 5420 Juniper sub) | §5.4 |
| 1 | System-wide data-integrity flag (URL collision now 3/3 clients) | §5.5 |
| 1 | Duplicate Account record needing reconciliation | §10 #1 |

### 13.3 What a reader should look at first

1. **§7 #1 — Duplicate Account reconciliation** (HIGH) — must precede any structural data ops on Brad
2. **§7 #2 — Reply to Brad's 4/11 questions** (HIGH) — Deontae; clears post-4/15 strategy momentum
3. **§8 strategy stack** — $10K/yr quantified; W-2 adjustment is the single highest-priority client-side move (AI-51 HIGH)
4. **§5.4 Cost Seg Approval loop** — proposal drafted, intake form not yet sent (AI-53); 1-touch to advance
5. **§5.5 Files & Links template-default URL collision** — system-wide, now demonstrated across 3 clients

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/BradKanouse/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-04-22 · Depth mode: FULL (Insights + Tax Memo + TPS transcript + Cost Seg proposals + emails + 16 action items) · Next refresh: trigger on Brad's 4/11 reply OR cost seg approval OR mid-April 2026 quarterly check-in*
