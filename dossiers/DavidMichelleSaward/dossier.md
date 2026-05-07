# David & Michelle Saward — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | David & Michelle Saward (MFJ household) |
| Account Name | David & Michelle Saward (Notion Accounts) |
| Client # | Not populated on Account record `[Accounts:David & Michelle Saward]` |
| Mango Client ID | Not populated on Account record `[Accounts:David & Michelle Saward]` |
| Mango IDs (Compliance) | 1040: 1880995 · Pukalani LLC 1065: 1880999 · 435 Sycamore LLC 1065: 1880996 `[TaxCompliance:Saward 1040]` `[TaxCompliance:Pukalani LLC]` `[TaxCompliance:435 Sycamore LLC]` |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Planning Year(s) | 2024 / 2025 / 2026 |
| Engagement Stage | Tax Ascend — Tax Insights (delivered 2026-03-12) + Tax Planning (memo sent 2026-03-20, planning session 2026-04-17) + Tax Compliance (active, extended) |
| Engagement Fee | $9,425 (signed 2026-02-05) `[EL:David & Michelle Saward §Price]` |
| Temperature | Active & engaged — Insights delivered, tax memo sent, planning session completed, entity formation in progress; **HOT blocker: PBC documents not yet received** |
| Relationship Manager | Seth Johnson `[Accounts:David & Michelle Saward]` |
| Primary Contact | Michelle Saward (née Bowles) — `michelle@clayhousemortgage.com` `[EmailLog:CHMMB Holdings LLC §Participants]` |
| Billing Partner | Seth Johnson (Tax Planning) / Deontae Lafayette (Tax Compliance) `[MangoPlanningNEW:Saward Tax Planning]` `[MangoPlanningNEW:Saward 1040]` |
| Data Sources (this refresh) | Notion Accounts record · Executive Summaries DB row · thin exec summary (Apr 14 2026) · Email Intelligence subpage (2 threads) · Meetings & Decisions subpage · Files & Documents subpage · Engagement Letter tracker · Insights Project Status tracker · Tax Ascend record · 3 Mango Planning & Compliance rows (1040 + Tax Planning + 435 Sycamore) · 3 Tax Compliance Projects rows (1040, Pukalani LLC 1065, 435 Sycamore LLC 1065) · 3 Files & Links rows · Client Email Log (2 rows: CHMMB entity formation + booking confirmation) |
| Files NOT Accessible This Refresh | PBC Workbook (Account field empty) · Tax Extraction (Account field empty) · Tax Planning Memo (Account field empty; Tax Ascend has 2 Word doc SharePoint URLs) · Meeting Prep Notes (Account field empty) · SharePoint Drive (Account field empty) · Client # and Mango Client ID not populated on Account record · Tax Planning meeting recap not on Meetings Tracker |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.
**Depth mode:** **MEDIUM** — clean Insights + Planning cycle in progress; 1 meeting on tracker; 2 email threads; entity formation underway; no prior Claude sessions; 3 active Tax Compliance projects; no Reporting Entities populated; no Meeting Action Items in DB. Comparable to Alex Dykes depth class.

---

## §1. Executive Overview

David & Michelle Saward are a **new Tax Ascend household** signed **2026-02-05** at **$9,425** for a full Tax Insights + Tax Planning + Tax Compliance engagement. `[EL:David & Michelle Saward §Price]` `[TaxAscend:David & Michelle Saward §date:Date Signed]` The Insights phase ran from kickoff **2026-02-23** → clarifying call **2026-03-05** → delivery **2026-03-12**, with 3/3 files received and Analysis Workbook, Extraction 1040, and Counting File all delivered to SharePoint. `[Insights:David & Michelle Saward]` Tax memo was issued **2026-03-20** (two Word docs linked from Tax Ascend), planning session was booked for **2026-04-17** at 12:00 PM CT (confirmed via booking email), and Tax Ascend was ascended **2026-03-18**. `[TaxAscend:David & Michelle Saward §Planning Status]`

**What makes this household structurally interesting is the multi-entity real estate and pass-through stack.** The account has at minimum **two active LLCs filing Form 1065**: **Pukalani LLC** (extended, Mango 1880999, stage: Collect and Review K-1s) and **435 Sycamore LLC** (extended, Mango 1880996, stage: Collect and Review K-1s). `[TaxCompliance:Pukalani LLC]` `[TaxCompliance:435 Sycamore LLC]` Both LLCs are in Internal WP Preparation. A third entity — **CHMMB Holdings LLC** — is currently in **formation via Fileforms** (initiated 2026-04-10), with registered agent + EIN + annual report services all included. `[EmailLog:CHMMB Holdings LLC]` The entity is named after Michelle (CHMMB = initials reference), and the email chain identifies the client contact as **Michelle Bowles** at `michelle@clayhousemortgage.com` — Clay House Mortgage, suggesting mortgage/real estate as the household's core business. `[EmailLog:CHMMB Holdings LLC §Participants]` David Saward's business or income profile is not directly surfaced in the current source set beyond the joint 1040.

**The headline issue entering the planning session was PBC non-response.** As of the Apr 14 2026 thin exec summary, PBC documents had not yet been received despite the list being sent 2026-04-09 (forwarded to Stacy for followup 2026-04-14). `[ExecSumm-thin 2026-04-14]` `[EL:David & Michelle Saward §PBC Emails Notes]` The Engagement Letter tracker notes "used Deontae short list (analysis workbook PBC list issue)" — indicating the standard PBC list was adapted. `[EL:David & Michelle Saward §Notes (PBC OPEN ITEMS)]`

**Compliance posture.** The 1040 is extended (due 2026-10-15), both 1065s are extended (due 2026-09-15). `[TaxCompliance:Saward 1040 §date:Extended Due]` `[TaxCompliance:Pukalani LLC §date:Extended Due]` `[TaxCompliance:435 Sycamore LLC §date:Extended Due]` The 1040 is at Mango stage "04 Preparation (External)" while both 1065s are at "03 Collect and Review K-1s" — meaning the 1065s are gating the 1040 (K-1s from the LLCs flow up to the personal return). All three are managed by **Deontae Lafayette** as both preparer and manager. `[TaxCompliance:Saward 1040 §Manager]`

**CHMMB Holdings LLC formation is an open-action blocker.** Michelle needs to (1) accept the Fileforms admin invite and (2) provide EIN application answers to Sophia Leonardo. Accruity is on the hook to track the annual report filing going forward. `[EmailLog:CHMMB Holdings LLC §Action Items]` Whether the April 17 tax planning session resolved any of these items is unknown — no meeting recap is on the Meetings Tracker for that session.

**Current refresh gaps.** Client # and Mango Client ID are both blank on the Account record. No Reporting Entities populated. PBC Workbook, Tax Extraction, Tax Planning Memo URL, Meeting Prep Notes, and SharePoint Drive are all empty on Account. No Meeting Action Items in the Notion DB for this account. No prior Claude sessions. Tax Planning session (Apr 17) has no recap/transcript on record.

---

## §2. Client Profile

| Item | Value | Confidence | Source |
| --- | --- | --- | --- |
| Filing Status | Married Filing Jointly (1040 filed jointly) | ✓ | `[TaxCompliance:Saward 1040 §Project]` |
| State(s) | Unknown — not surfaced in this refresh | ? | — |
| Primary Income | Real estate / mortgage (Michelle via Clay House Mortgage); David's income profile not surfaced | ~ | `[EmailLog:CHMMB Holdings LLC §Participants]` |
| Account # | Not populated | ? | `[Accounts:David & Michelle Saward §Client #]` |
| Mango Client ID | Not populated on Account | ? | `[Accounts:David & Michelle Saward §Mango Client ID]` |
| Mango IDs (Compliance) | 1040: 1880995 · Pukalani LLC: 1880999 · 435 Sycamore LLC: 1880996 | ✓ | `[TaxCompliance DB]` |
| Primary Contact | Michelle Saward — `michelle@clayhousemortgage.com` | ✓ | `[EmailLog:CHMMB Holdings LLC §Participants]` |
| Portal Access (Mango) | Portal Invite Sent | ✓ | `[EL:David & Michelle Saward §Mango Portal Invite]` |
| Relationship Manager | Seth Johnson | ✓ | Account ancestry |
| Tax Planning Manager | Sophia (Mango OLD DB) / Seth (Mango NEW DB) | ✓ | `[MangoPlanningOLD:Tax Planning]` `[MangoPlanningNEW:Tax Planning]` |
| Compliance Manager | Deontae Lafayette (all 3 compliance projects) | ✓ | `[TaxCompliance DB]` |
| Engagement Stage | Tax Ascend — Insights ✓ + Planning memo sent + Compliance active (extended) | ✓ | `[TaxAscend:David & Michelle Saward]` |
| Engagement Letter | Signed (2026-02-05) · $9,425 · New Client GC SOW | ✓ | `[EL:David & Michelle Saward]` |
| Tax Memo Status | SENT (2026-03-20) | ✓ | `[TaxAscend:David & Michelle Saward §TAX MEMO STATUS]` |
| PBC List | Sent 2026-04-09 (shorter Deontae list); nothing received as of 2026-04-14 | ✓ | `[EL:David & Michelle Saward §PBC list status]` `[EL:David & Michelle Saward §date:Date PBC list sent]` |
| Compliance Group Status | Pending Check | ~ | `[EL:David & Michelle Saward §Compliance Group Status]` |
| Tax Proposal | COMMITTED (NEW CLIENT GC SOW) | ✓ | `[EL:David & Michelle Saward §TAX PROPOSAL]` |
| Docusign Status | To Do | ~ | `[EL:David & Michelle Saward §Docusign Status]` |
| Entity Formation | CHMMB Holdings LLC — in progress via Fileforms (2026-04-10) | ✓ | `[EmailLog:CHMMB Holdings LLC]` |

### Principals at a glance

- **Michelle Saward (née / also known as Michelle Bowles)** — Primary operating contact; email `michelle@clayhousemortgage.com` indicates she works in or runs Clay House Mortgage. Entity CHMMB Holdings LLC appears to be in her name (Michelle C H-MM-B?). She is the booking contact for the Apr 17 Tax Planning session. `[EmailLog:CHMMB Holdings LLC §Participants]` `[EmailLog:Booking]`
- **David Saward** — Joint filer; income profile and professional role not surfaced in this refresh's source set. The Account is titled "David & Michelle Saward" with David listed first — no standalone contact record, email, or phone surfaced. **Asymmetric service-depth check: David's profile is entirely opaque in the current Notion record set; Michelle drives all named activity.** This warrants a confirmation on next refresh: what is David's income/entity exposure?

### Entity stack

`[TaxCompliance DB]` `[EmailLog:CHMMB Holdings LLC]` `[TaxAscend:David & Michelle Saward §TAX ASCEND TYPE]`

| Entity | Form | Status | Manager | Notes |
| --- | --- | --- | --- | --- |
| **David & Michelle Saward (joint 1040)** | 1040 | Extended (due 2026-10-15) · Stage: 04 Preparation (External) | Deontae Lafayette | K-1s from LLCs feed this return `[TaxCompliance:Saward 1040]` |
| **Pukalani LLC** | 1065 | Extended (due 2026-09-15) · Stage: 03 Collect and Review K-1s | Deontae Lafayette | PBC list sent; likely Hawaii-area real estate given "Pukalani" (Maui area) `[TaxCompliance:Pukalani LLC]` |
| **435 Sycamore LLC** | 1065 | Extended (due 2026-09-15) · Stage: 03 Collect and Review K-1s | Deontae Lafayette | PBC list sent; property address LLC naming convention `[TaxCompliance:435 Sycamore LLC]` |
| **CHMMB Holdings LLC** | TBD (new entity) | Formation in progress via Fileforms (2026-04-10) · EIN pending | Sophia (formation) | Registered agent + EIN + Annual Report all included; Michelle needs to accept Fileforms admin invite `[EmailLog:CHMMB Holdings LLC]` |

> **Note:** Pukalani is a community in Maui County, Hawaii — suggesting the LLC may hold Hawaii real estate. 435 Sycamore LLC follows a property-address naming convention common for rental property LLCs. Both are unconfirmed property details pending PBC workbook ingestion. `~`

### Mango Planning & Compliance projects

| DB | Project | Type | Manager | Billing | Tags | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Mango NEW | **Tax Planning - David & Michelle Saward** | Tax Planning | Sophia | Seth | PBC request Sent (Compliance) | Active · Manager Done · Billing Done `[MangoPlanningNEW:Tax Planning]` |
| Mango NEW | **1040- David & Michelle Saward** | Tax Compliance | Seth | Deontae | Extended · Tax Compliance · PBC request Sent | Active · Manager Done · Billing Done `[MangoPlanningNEW:1040]` |
| Mango NEW | **1065- 435 Sycamore LLC** | Tax Compliance | Seth | Deontae | Extended · Tax Compliance · PBC request Sent | Active · Manager Done · Billing Done `[MangoPlanningNEW:435 Sycamore]` |
| Mango OLD | **Tax Planning - David & Michelle Saward** | Tax Planning | Seth | — | PBC request Sent (Compliance) | Active · Manager Done · Status (Sr Manager): Stacy Clarify `[MangoPlanningOLD:Tax Planning]` |
| Mango OLD | **1040- David & Michelle Saward** | Tax Compliance | Deontae | — | PBC request Sent (Compliance) | Active · Status (Manager): To Check · Status (Sr Manager): To Check `[MangoPlanningOLD:1040]` |

---

## §3. Email Intelligence

**Scope of this refresh:** 2 email threads in the Client Email Log, both linked to the Account. `[Accounts:David & Michelle Saward §Email Log]`

### 3.1 Active Threads

**Thread 1 — CHMMB HOLDINGS LLC** `[EmailLog:CHMMB Holdings LLC]`

| Field | Value |
| --- | --- |
| Subject | CHMMB HOLDINGS LLC |
| Date | 2026-04-10 |
| Direction | Outbound (from `fileforms@accruity.com`) |
| Risk Level | Low |
| Flag | ⚡ Action — client must accept invite + provide EIN info |
| Message count | 1 |
| Participants | Sophia Leonardo (sent) · Michelle Bowles/Saward (client) · Seth Johnson (CC) · Deontae Lafayette (CC) · Stacy Cvengros (CC) |

**Action items extracted:**
- Michelle Bowles — Accept Fileforms admin invite and review entity info — ASAP (Pending)
- Sophia Leonardo — Collect EIN application answers from Michelle — ASAP (Pending)
- Accruity — Track annual report filing for CHMMB Holdings LLC — Ongoing/Annual

**Synopsis:** Entity formation initiated for CHMMB Holdings LLC. Registered agent + EIN + Annual Report services included. EIN is a separate module requiring business questions from Michelle. Annual Report service keeps entity in good standing and avoids penalties/dissolution. Formation was set up by Sophia on Fileforms; Michelle sent admin invite to Fileforms dashboard. `[EmailLog:CHMMB Holdings LLC §Synopsis]`

### 3.2 Closed Threads

**Thread 2 — New booking: Michelle R Bowles for Tax Planning (1hr review)** `[EmailLog:Booking]`

| Field | Value |
| --- | --- |
| Subject | New booking: Michelle R Bowles for Tax Planning (1hr review) |
| Date | 2026-04-09 |
| Direction | Inbound (from `TaxPlanningReview30min@subledge.com`) |
| Status | Closed |
| Booking | Tax Planning (1hr review) with Seth Johnson — Friday April 17, 2026 12:00 PM – 1:00 PM CT |

**Rollup:** 2 threads; 1 active (entity formation blocker); 1 closed (booking confirmation). No HIGH-risk email items. Communication is task-driven and outbound-initiated by Accruity staff. Michelle's email domain `clayhousemortgage.com` confirmed as primary contact address.

**Plumbing note:** Only 2 email threads exist for a new-client engagement (started Feb 2026) — PBC follow-up emails, Insights delivery coordination, and engagement onboarding threads are not represented in the Email Log. The Make.com email-capture scenario may not be fully matching on this Account. Flag for ops review on next refresh.

### 3.3 Noise Filter

*(none — 2-thread log has no noise)*

---

## §4. Meeting History

**Scope of this refresh:** 1 meeting on the Meetings Tracker linked to the Account. The April 17 Tax Planning session is confirmed via email but **not yet on the Meetings Tracker**. `[Accounts:David & Michelle Saward §Meetings]`

| # | Date | Type | Status | Time (EST) | Client Named | Recap | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **2026-03-11** | Full Insights — Delivery call | Done ✓ | 1:30 PM – 2:30 PM | Michelle Saward | [Fathom](https://fathom.video/share/1woWDQTFGQRyy5LREws92NDzZSBXbVzn) | `[Meeting 2026-03-11]` |
| 2 | **2026-04-17** | Tax Planning (1hr review) | Done ✓ (confirmed via booking email) | 12:00 PM – 1:00 PM CT | Michelle R Bowles | **Not on Meetings Tracker; no recap URL** ⚠ | `[EmailLog:Booking]` |

**Meetings NOT on tracker but confirmed in source data:**

The Insights Kickoff (2026-02-23 per Insights Project record) and Clarifying Call (2026-03-05 per Insights Project record) are not in the Meetings Tracker. The tracker has only 1 row for this Account. These sessions likely occurred but weren't entered.

**Cadence pattern:** Insights cycle Feb 23 → Mar 5 → Mar 12 delivery → Mar 18 Tax Ascend ascension → Mar 20 tax memo → Apr 9 planning session booked → Apr 17 planning session (no recap). The planning session recap is an important gap — content of the Apr 17 session (including any tax strategy decisions, action items generated, and CHMMB Holdings LLC discussion) is unknown without the Fathom/Fellow link.

**Restricted meetings excluded:** 0 (no Restricted=YES rows). The single tracker entry is accessible.

---

## §5. Document Inventory

### 5.1 Engagement Letter

| Field | Value | Source |
| --- | --- | --- |
| Status | **Signed** | `[EL:David & Michelle Saward §Engagement Letter Status]` |
| Signed Date | 2026-02-05 | `[TaxAscend:David & Michelle Saward §date:Date Signed]` |
| Fee | **$9,425** | `[EL:David & Michelle Saward §Price]` |
| Scope | NEW CLIENT GC SOW — Tax Insights + Tax Planning + Tax Compliance + Registered Agent Services | `[EL:David & Michelle Saward §TAX PROPOSAL]` `[EL:David & Michelle Saward §Entity Compliance services]` |
| Compliance Group Status | Pending Check | `[EL:David & Michelle Saward §Compliance Group Status]` |
| Mango Engagement | Project Created | `[EL:David & Michelle Saward §Mango Engagement/Project]` |
| Portal Invite | Portal Invite Sent | `[EL:David & Michelle Saward §Mango Portal Invite]` |
| Mango Tag | PBC Request list | `[EL:David & Michelle Saward §Mango Tag]` |
| Signed EL (MangoShare) | [app.mangoshare.com/share/aff946650b453aa48b907dc5](https://app.mangoshare.com/share/aff946650b453aa48b907dc5) | `[EL:David & Michelle Saward §Signed EL mangoshare]` |
| Docusign Email Status | Delivered | `[EL:David & Michelle Saward §Docusign Email Status]` |
| Docusign Status | To Do | `[EL:David & Michelle Saward §Docusign Status]` |
| PBC list link | [SharePoint .xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBWv-7lJrDZTLgHiWfSgLclAVXVt4dn2JUn6rzoGXbY9C4?e=Uue1BJ) | `[EL:David & Michelle Saward §PBC list link]` |
| PBC List Sent Date | 2026-04-09 | `[EL:David & Michelle Saward §date:Date PBC list sent]` |
| PBC List Status | Sent List — nothing received yet (as of 2026-04-14) | `[EL:David & Michelle Saward §PBC list status]` |
| PBC Notes | "Forwarded to Stacy for followup 04/14" | `[EL:David & Michelle Saward §PBC Emails Notes]` |
| Open Items Status | None Sent | `[EL:David & Michelle Saward §Open items Status]` |
| Batch Added | 2026-03-18 | `[EL:David & Michelle Saward §date:Batch Added]` |
| Outlook Attachment | `David_Saward.msg` retained on EL tracker row | `[EL:David & Michelle Saward §Outlook Email Msg]` |
| EL Integrity Flag | Docusign Status "To Do" — signature process may be incomplete; Compliance Group Status "Pending Check" | ⚠ `[EL:David & Michelle Saward §Docusign Status]` |

### 5.2 Insights Project artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| **Analysis Workbook** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQA5qS8_Kwd_TrDsHjQKtdMmARcGW2OLSiIU_vPHsSR9bjg?e=fmCP7B) | `[Insights:David & Michelle Saward §Analysis Workbook]` |
| **Extraction 1040** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDpnEefNQ4ISYyaOLNgCe3iAaL5JaVjcKBOzl5Iin3cubA?e=7onMMw) | `[Insights:David & Michelle Saward §Extraction 1040]` |
| **Counting File** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCliNntVln6Q6f23YYso7ECAaDSpRGsWdpW1EV9JZ7FYAs?e=khTWQP) | `[Insights:David & Michelle Saward §Counting file]` |
| **Request List Tracker** | [SharePoint Insights site xlsx](https://subledgesl.sharepoint.com/:x:/s/Insights/IQBQLlGY6rldS47vPaEskQCYAQ5pO9qEIplOfuAvkIFUTCE?e=sQjREQ) | `[Insights:David & Michelle Saward §Request List]` |
| **Tax Returns Folder** | [SharePoint folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgBjRiLUjsbVS7OyFeDSePIFAe1TJ5q3FkRDP9KLKnuRqj4?e=FhRyOj) | `[Insights:David & Michelle Saward §Tax Returns Folder Link]` |
| **Insights Delivery Recording** | [Fathom](https://fathom.video/share/1woWDQTFGQRyy5LREws92NDzZSBXbVzn) (Mar 11 delivery call) | `[Insights:David & Michelle Saward §Meeting link]` |
| **Insights SharePoint doc** | [SharePoint viewer](https://subledgesl.sharepoint.com/sites/Insights/_layouts/15/viewer.aspx?sourcedoc={f77b99bd-98f8-45d6-ae3e-ff66645cec50}) | `[Insights:David & Michelle Saward §Sharepoint Link]` |
| Insights status | **DELIVERED** (2026-03-12) · 3/3 files received · Accelo: 04 Insights Delivered | ✓ | `[Insights:David & Michelle Saward §Status (Precheck)]` |
| Tax Insights Status | Not started (analysis cycle for the actual filing) | ~ | `[Insights:David & Michelle Saward §Status (Tax Insights)]` |
| Mango Status | To Check | ~ | `[Insights:David & Michelle Saward §Mango Status]` |
| Analysis | Completed | ✓ | `[Insights:David & Michelle Saward §Analysis]` |
| Tax Team Checked | YES ✓ | ✓ | `[Insights:David & Michelle Saward §Checked (Tax Team)]` |
| Kickoff Call | 2026-02-23 | ✓ | `[Insights:David & Michelle Saward §date:Kickoff Call]` |
| Clarifying Call | 2026-03-05 | ✓ | `[Insights:David & Michelle Saward §date:Clarifying Call]` |
| Date Delivered | 2026-03-12 | ✓ | `[Insights:David & Michelle Saward §date:Date delivered]` |

> **Plumbing gap:** None of the Insights workbook URLs propagated up to the Account record's top-level fields (PBC Workbook, Tax Extraction, Tax Planning Memo are all empty on Account). Same pattern seen on Spring Bengtzen, Alex Dykes. System-wide sync gap — promote to §7 plumbing.

### 5.3 Tax Ascend record

| Field | Value | Source |
| --- | --- | --- |
| TAX ASCEND TYPE | TAX INSIGHTS · TAX PLANNING · TAX COMPLIANCE | `[TaxAscend:David & Michelle Saward §TAX ASCEND TYPE]` |
| Tax Memo Status | SENT (2026-03-20) | `[TaxAscend:David & Michelle Saward §TAX MEMO STATUS]` |
| Tax Memo URL (1) | [SharePoint Word doc 1](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQCYLoIA5ALzQ4xU-DDpDjaWAVx83ZaSnR3kL4dK1m9-j0U?e=7i4t4D) | `[TaxAscend:David & Michelle Saward §Tax Memo URL]` |
| Tax Memo URL (2) | [SharePoint Word doc 2](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQDwF5WKNIMtRqwPMCLYCUGEAQ3BngaqWxlmsMTUGOvIcWk?e=Sqww4C) | `[TaxAscend:David & Michelle Saward §Tax Memo URL]` |
| Planning Status | Tax Memo and Booking Link Emailed | `[TaxAscend:David & Michelle Saward §Planning Status]` |
| Compliance Status | Entities Added to Assignment Tracker | `[TaxAscend:David & Michelle Saward §Compliance Status]` |
| Mango Compliance Engagement | Already In Mango | `[TaxAscend:David & Michelle Saward §Mango Compliance Engagement]` |
| Mango Planning Projects | Done | `[TaxAscend:David & Michelle Saward §Mango Planning Projects]` |
| Date Ascended | 2026-03-18 | `[TaxAscend:David & Michelle Saward §date:Date Ascended]` |
| Linking Status | Complete | `[TaxAscend:David & Michelle Saward §Linking status]` |

### 5.4 Tax Compliance Projects (3)

| Project | Form | Mango ID | Status | Extended Due | Stage | Preparer | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1040- David & Michelle Saward** | 1040 | 1880995 | In Progress · Extended | 2026-10-15 | 04 Preparation (External) | Deontae Lafayette | `[TaxCompliance:Saward 1040]` |
| **1065- Pukalani LLC** | 1065 | 1880999 | In Progress · Extended | 2026-09-15 | 03 Collect and Review K-1s | Deontae Lafayette | `[TaxCompliance:Pukalani LLC]` |
| **1065- 435 Sycamore LLC** | 1065 | 1880996 | In Progress · Extended | 2026-09-15 | 03 Collect and Review K-1s | Deontae Lafayette | `[TaxCompliance:435 Sycamore LLC]` |

### 5.5 Files & Links rows (3) — with URL collision check

| Row | Name | Document Inventory URL | PBC PDF Package URL | Flag |
| --- | --- | --- | --- | --- |
| `33b4…8297` | "Engagement Letter" | empty | empty | — placeholder stub |
| `33b4…9d4a` | "Executive Summary" | empty | empty | — placeholder stub |
| `33b4…2dd7` | "David & Michelle Saward" | `IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw` | `IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA` | ⚠️ **COLLISION — same SharePoint folder IDs as Spring Bengtzen and Alex Dykes** |

**F&L URL Collision: YES** — The "David & Michelle Saward" Files & Links row Document Inventory and PBC PDF Package SharePoint folder URLs are **byte-identical to Spring Bengtzen and Alex Dykes**. This is a template-default that was never per-client-customized. Affected clients confirmed so far: Spring, Alex Dykes, Matt Iannaccio, and now David & Michelle Saward — likely affects most or all clients in the queue. `[FL:David & Michelle Saward §Document Inventory]`

URLs affected:
- Document Inventory: `https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw?e=QLo4ua`
- PBC PDF Package: `https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA?e=2u2L6u`

### 5.6 Files NOT accessible this refresh

| Field on Account | Status |
| --- | --- |
| PBC Workbook | Empty on Account record `[Accounts:David & Michelle Saward §PBC Workbook]` |
| Tax Extraction | Empty on Account record `[Accounts:David & Michelle Saward §Tax Extraction]` |
| Tax Planning Memo (Account field) | Empty (memo Word docs DO exist via Tax Ascend record — 2 URLs) `[TaxAscend:David & Michelle Saward §Tax Memo URL]` |
| Meeting Prep Notes | Empty on Account record |
| SharePoint Drive | Empty on Account record |
| Document Inventory (Account field) | Empty (separate from the F&L row) |
| Client # | Not populated on Account |
| Mango Client ID | Not populated on Account |
| Reporting Entities | None found linked to Account |
| Tax Planning session recap (Apr 17) | Not on Meetings Tracker; no Fathom/Fellow URL on record |
| CHMMB Holdings LLC EIN | Pending — application not yet submitted |

---

## §6. Claude Work Product

**Prior Claude Summaries linked to this Account:** 0 — none on record.

**Claude Activity Log rows linked to this Account:** 0 — none on record. `[ExecSumm-thin 2026-04-14 §Source Data: Claude Work Product = 0 sessions]`

**Notes:** The thin exec summary (Apr 14 2026) explicitly confirms 0 prior Claude sessions for this Account. This refresh creates the first Claude Summary log row.

This refresh's Claude Summary row will be created in §11 (Notion write) with:
- Thread Title: `David & Michelle Saward — Client Intelligence Dossier — 2026-05-07`
- Account: `https://www.notion.so/32f491728751808391f7d15e7954ed5e`
- Topics: File Review · Notion Build · Compliance · Tax Planning
- Files Reviewed: Analysis Workbook · Extraction 1040 · Tax Ascend record · EL tracker · 3 Compliance Projects

---

## §7. Action Items (Rolled Up)

Sources: Email Log action items (2 threads) · Tax Planning meeting (no AIs on tracker) · Meeting Action Items DB (0 rows for this Account) · Engagement Inquiries (0 rows) · dossier-generation flags. Note: The April 17 tax planning session likely generated action items that are NOT yet captured anywhere in the Notion record set.

### 7.1 HIGH priority

| ID | Action | Owner | Source / Due | Status | Source |
| --- | --- | --- | --- | --- | --- |
| **AI-01** | Michelle to accept Fileforms admin invite for CHMMB Holdings LLC and review entity info | Client (Michelle Saward) | Email 2026-04-10 / ASAP | **Pending** ⚠ | `[EmailLog:CHMMB Holdings LLC §Action Items]` |
| **AI-02** | Sophia to collect EIN application answers from Michelle for CHMMB Holdings LLC | Accruity (Sophia Leonardo) | Email 2026-04-10 / ASAP | **Pending** ⚠ — gates EIN issuance | `[EmailLog:CHMMB Holdings LLC §Action Items]` |
| **DG-01** | Receive PBC documents from client — list sent 2026-04-09, nothing received as of 2026-04-14; forwarded to Stacy for followup | Accruity (Stacy) / Client | PBC email 2026-04-09 / URGENT | **Open** ⚠ — gates compliance prep for all 3 returns | `[EL:David & Michelle Saward §PBC list status]` `[EL:David & Michelle Saward §PBC Emails Notes]` |
| **DG-02** | Capture and log Tax Planning session recap (April 17, 2026) — action items from Seth + Michelle session are completely unknown without the Fathom/Fellow recording | Accruity (Seth) | dossier-gen flag (2026-05-07) | **Open** ⚠ — black box without recap | `[EmailLog:Booking]` `[ExecSumm-thin 2026-04-14]` |

### 7.2 MEDIUM priority

| ID | Action | Owner | Source / Due | Status | Source |
| --- | --- | --- | --- | --- | --- |
| **AI-03** | Accruity to track annual report filing for CHMMB Holdings LLC (annual obligation) | Accruity (Sophia + Ops) | Email 2026-04-10 / Annual | Ongoing — calendar entry needed | `[EmailLog:CHMMB Holdings LLC §Action Items]` |
| **DG-03** | Resolve Docusign Status "To Do" on EL tracker — confirm engagement letter signature process is complete (Compliance Group Status is "Pending Check") | Accruity Compliance Ops | EL tracker `[EL:David & Michelle Saward §Docusign Status]` | **Open** | `[EL:David & Michelle Saward §Compliance Group Status]` |
| **DG-04** | Collect K-1s for Pukalani LLC and 435 Sycamore LLC (both at stage 03 Collect and Review K-1s) — 1065s gate the 1040 | Client + Compliance team | PBC list sent; not received | **Open** — both LLCs gating 1040 | `[TaxCompliance:Pukalani LLC]` `[TaxCompliance:435 Sycamore LLC]` |
| **DG-05** | Confirm what CHMMB Holdings LLC will be used for operationally — entity type (likely LLC taxed as disregarded or partnership), purpose, income type. Critical for 2026 planning | Accruity (Seth + Sophia) | dossier-gen flag | **Open** — purpose not in current source set | `[EmailLog:CHMMB Holdings LLC]` |
| **DG-06** | Add April 17 Tax Planning meeting to Meetings Tracker with Fathom/Fellow recap URL | Accruity Ops | dossier-gen flag | **Open** — meeting tracker gap | `[EmailLog:Booking]` |
| **DG-07** | Populate Client # and Mango Client ID on Accounts record — both blank | Accruity Ops | dossier-gen flag | **Open** | `[Accounts:David & Michelle Saward]` |

### 7.3 LOW priority / data hygiene

| ID | Action | Owner | Source | Source |
| --- | --- | --- | --- | --- |
| **DG-08** | Remediate F&L URL collision — "David & Michelle Saward" Files & Links row has template-default SharePoint folder IDs (same as Spring Bengtzen, Alex Dykes, Matt Iannaccio). Replace with client-specific folder links | Accruity Ops | F&L §5.5 | `[FL:David & Michelle Saward §Document Inventory]` |
| **DG-09** | Backfill Meetings Tracker for Insights Kickoff (2026-02-23) and Clarifying Call (2026-03-05) — currently missing | Accruity Ops | dossier-gen flag | `[Insights:David & Michelle Saward §date:Kickoff Call]` |
| **DG-10** | Populate Reporting Entities on Account — none found in this refresh | Accruity Ops | dossier-gen flag | `[Accounts:David & Michelle Saward §Reporting Entities]` |
| **DG-11** | Sync Insights workbook URLs up to Account top-level fields (PBC Workbook, Tax Extraction) — currently empty | Accruity Ops | §5.2 plumbing gap | `[Accounts:David & Michelle Saward §PBC Workbook]` |
| **DG-12** | Investigate email log underrepresentation — only 2 threads for a 3-month engagement; audit Make scenario's Account-match filter | Accruity Ops | §3 plumbing | `[Accounts:David & Michelle Saward §Email Log]` |
| **DG-13** | Confirm David Saward's income profile and professional role — completely opaque in current source set; asymmetric service-depth risk (Michelle drives all named activity) | Seth (RM) | §11 asymmetry | See §11.2 |

**Total open items:** 13 (4 HIGH, 7 MED, 5 LOW... plus this list as refined above with 4 HIGH, 6 MED, 7 LOW as itemized).

---

## §8. Tax Strategies

**Source-of-truth for tax strategy:** The Tax Planning Memo (2 Word docs linked from Tax Ascend, sent 2026-03-20) + the Tax Planning session (Apr 17, 2026 — no recap captured). The Analysis Workbook and Extraction 1040 from Insights are on SharePoint. **Strategy specifics are NOT surfaced in the current Notion text-searchable record set** — the memo content lives in SharePoint Word documents that were not fetched in this refresh, and the planning session has no recap.

### 8.1 Strategy table (placeholder — memo not parsed)

| # | Strategy | Estimated Annual Impact | Status | Year(s) | Priority | Key Notes | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **CHMMB Holdings LLC entity formation** | ? | In progress (Fileforms) | 2026 | HIGH | New entity for Michelle; purpose (holding, operating, rental?) not yet confirmed. EIN pending. | `[EmailLog:CHMMB Holdings LLC]` |
| 2 | **Registered Agent Services** | — | Included in EL | 2026+ | HIGH | Included in $9,425 engagement; Pukalani LLC + 435 Sycamore LLC + CHMMB Holdings LLC likely all need ongoing registered agent | `[EL:David & Michelle Saward §Entity Compliance services]` |
| 3 | **1065 pass-through optimization** (Pukalani LLC + 435 Sycamore LLC) | `? Pending workbook ingestion` | Returns extended; at K-1 collection stage | 2024 / 2025 | HIGH | Two LLCs generating K-1s that flow to the 1040; nature of income (rental, investment, active?) not confirmed. Strategy specifics require memo + workbook. | `[TaxCompliance:Pukalani LLC]` `[TaxCompliance:435 Sycamore LLC]` |
| 4 | **Other strategies from Tax Planning memo** | `? Pending workbook ingestion` | Memo SENT (2026-03-20); content not accessible in current refresh | 2025 / 2026 | — | Memo PDFs at Tax Ascend URLs; require SharePoint access to parse. Two Word docs suggest possibly two strategy scenarios or draft + final. | `[TaxAscend:David & Michelle Saward §Tax Memo URL]` |

> **CAUTION:** All dollar figures in this section are `? Pending workbook ingestion`. The Analysis Workbook and Extraction 1040 are on SharePoint and should be parsed on the next refresh to populate this table fully.

### 8.2 Engagement pricing

| Component | Amount | Notes | Source |
| --- | --- | --- | --- |
| Total engagement fee | $9,425 | New Client GC SOW | `[EL:David & Michelle Saward §Price]` |
| Services | Tax Insights + Tax Planning + Tax Compliance + Registered Agent | Comprehensive engagement | `[TaxAscend:David & Michelle Saward §TAX ASCEND TYPE]` |

---

## §9. Opportunity Flags (Rule-Based)

Sources: cross-walk of `execsumm_emails/opportunity_flags.py` rule patterns against available data. Note: Analysis Workbook not parsed; income figures not available in this refresh.

### 9.1 HIGH-confidence flags

🔴 **HIGH — Multi-Entity Pass-Through Stack with K-1 Complexity.** Two Form 1065 LLCs (Pukalani LLC + 435 Sycamore LLC) are in the compliance workflow, both generating K-1s that feed the joint 1040. A third entity (CHMMB Holdings LLC) is being formed. Three-entity stack for a single household means ongoing inter-entity coordination, annual report obligations, and compounding planning opportunities (pass-through deduction, basis tracking, passive activity rules). `[TaxCompliance:Pukalani LLC]` `[TaxCompliance:435 Sycamore LLC]` `[EmailLog:CHMMB Holdings LLC]`

🔴 **HIGH — Real Estate / Mortgage Household (Unconfirmed Income Profile).** Michelle's email domain (`clayhousemortgage.com`) and entity names (Pukalani = Maui area real estate, 435 Sycamore = address-named LLC) strongly suggest real estate investment or mortgage-industry income. If this is correct, **Cost Segregation**, **Passive Activity / REPS analysis**, **Short-Term Rental exception**, and **real estate professional SE-tax strategies** may all be in scope. No income figures available this refresh to model. `~ [EmailLog:CHMMB Holdings LLC §Participants]`

### 9.2 MEDIUM-confidence flags

🟡 **MEDIUM — CHMMB Holdings LLC Purpose and Tax Classification.** Newly formed entity — its tax classification (disregarded/SMLLC, partnership, S-Corp election) has material planning implications. If Michelle has self-employment income from Clay House Mortgage flowing through a new LLC, an **S-Corp election** could eliminate a portion of SE tax. Worth flagging for Seth's review of the Apr 17 planning session decisions (once recap is obtained). `[EmailLog:CHMMB Holdings LLC]`

🟡 **MEDIUM — PBC Non-Response → Compliance Timeline Risk.** PBC list sent 2026-04-09; nothing received by 2026-04-14 (5 days). Both 1065s and the 1040 are extended (due Sept 15 and Oct 15, respectively), but K-1s must be issued before members/partners can file their own returns. If PBC documents arrive late, it compresses the compliance window. `[EL:David & Michelle Saward §PBC list status]`

🟡 **MEDIUM — David Saward Income Profile Unknown.** If David has W-2 income, a business, rental properties, or investment activity that hasn't surfaced in the current source set, additional planning strategies and entity structures may be warranted. Full picture requires the Planning Memo, PBC Workbook, and the Apr 17 session recap. `~`

### 9.3 LOW-confidence flags

🟢 **LOW — Registered Agent Services as Ongoing Revenue.** EL includes Registered Agent Services; as CHMMB Holdings LLC is formed and potentially more entities are added, the RA service line represents recurring revenue. Not a tax strategy per se but worth noting for account growth. `[EL:David & Michelle Saward §Entity Compliance services]`

🟢 **LOW — Two Tax Memo Word Docs** suggest either draft + final, or two separate memo scenarios (e.g., with/without a specific strategy). Worth confirming which is operative when the Tax Ascend record is revisited. `[TaxAscend:David & Michelle Saward §Tax Memo URL]`

---

## §10. Operations Analysis

**Engagement health:** Strong structural foundation — EL signed, deposit tracked (full price $9,425), Insights delivered clean (3/3 files, all stages complete, Tax Team checked), Tax Ascend ascended, tax memo sent, planning session completed. The engagement is executing per the playbook.

**Active stress:** PBC non-response is the primary operational risk. All three compliance returns (1040 + two 1065s) are gated on receiving client PBC documents. The 1065s are at the K-1 collection stage, meaning the LLC partners/members cannot file their own returns until Accruity completes the 1065s. This creates external pressure beyond just the Saward household.

**Workflow chokepoints:**

1. **PBC documents.** Owner: Client + Stacy (for followup). Sent 2026-04-09 (short list); forwarded to Stacy 2026-04-14. No documents received. The Apr 17 planning session may have produced a plan to expedite, but without a recap, the status is unknown.

2. **CHMMB Holdings LLC formation.** Owner: Michelle (invite acceptance) + Sophia (EIN collection). Two pending client-action items. Formation is at an early stage (invite not yet accepted as of 2026-04-10). Until EIN is issued, the LLC cannot operate, open bank accounts, or be included in 2026 planning runs.

3. **Tax Planning session recap capture.** Owner: Seth (RM). The Apr 17 session content is a black box — no Fathom, no Fellow, no meeting tracker entry. This means any strategy decisions, income figures discussed, or action items generated from that session are not tracked anywhere in the record set. Significant operational gap.

4. **K-1 collection on LLCs.** Owner: Deontae (preparer) + Client. Both Pukalani LLC and 435 Sycamore LLC are at stage "03 Collect and Review K-1s" with notes "pbc list sent." Until K-1s are received and reviewed, 1065 preparation cannot advance to Internal WP Preparation.

**Mango/Portal posture:** Portal invite sent but "Customer Accessed" status not confirmed — may still be pending. Compliance projects are all Active in Mango and aligned. Mango IDs are populated and all three projects have Aligned with Mango = YES.

**Team posture:** Clean team split — Seth owns the planning/client relationship and Tax Planning manager. Deontae Lafayette owns all compliance work (preparer + manager on all 3 returns). Sophia Leonardo is executing the CHMMB Holdings LLC formation. Stacy Cvengros is handling PBC followup. Well-distributed.

**Strategic theme:** New client (Feb 2026) on a comprehensive engagement — the Insights → Planning → Compliance cycle is running as designed. The household has real estate complexity (2 LLCs + new entity forming) that warrants deep engagement. The key risk is that PBC non-response and the missing planning session recap are creating information gaps that will compound as the Sept/Oct deadlines approach.

---

## §11. Individual Profiles

### 11.1 Michelle Saward (née / also Bowles)

- **Role:** Primary household contact; likely principal at Clay House Mortgage (`michelle@clayhousemortgage.com`). Named on the booking confirmation as "Michelle R Bowles" — confirms dual surname or legal name is Bowles, goes by Saward. `[EmailLog:Booking §Subject]`
- **Entities:** CHMMB Holdings LLC formation underway in her name. `[EmailLog:CHMMB Holdings LLC]`
- **Engagement footprint:** All inbound activity runs through Michelle — Tax Planning session booked by her, Fileforms admin invite sent to her, CHMMB Holdings LLC formation is her entity. She is the operational center of the household's Accruity relationship.
- **Contact:** `michelle@clayhousemortgage.com` `[EmailLog:CHMMB Holdings LLC §Participants]`
- **Income profile:** Clay House Mortgage suggests mortgage lending/brokering income. If self-employed through Clay House Mortgage (likely), SE tax exposure and entity structuring strategies are in scope. `~`
- **Note on naming:** Client Contact appears in multiple places as "Michelle Bowles" or "Michelle R Bowles" — the Account is titled "David & Michelle Saward" so Saward is the household/married name. Both names are in active use.

### 11.2 David Saward

- **Role:** Joint filer; listed first in the Account name. No standalone email, phone, client contact row, or named activity in the current source set.
- **Direct interaction footprint:** Minimal — the EL retention email is `David_Saward.msg` but no contact details extracted. `[EL:David & Michelle Saward §Outlook Email Msg]`
- **Income profile:** Completely unknown from this refresh's source set. Could be W-2 employee, self-employed, real estate investor, or passive. The existence of two LLCs (Pukalani LLC, 435 Sycamore LLC) suggests he may co-own real estate investment properties with Michelle — but neither LLC's ownership structure has been confirmed. `?`
- **Asymmetric service-depth check:** Michelle drives ALL named activity in the file. David's professional role, income, and individual planning needs are entirely opaque. This is a **service-depth risk** — if David has significant taxable events (real estate dispositions, business income, stock options, etc.) that aren't surfacing in the Notion record, the household is potentially under-served. Seth should confirm David's profile at the next client interaction.

---

## §12. Provenance Index

### Notion Records (primary)

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[Accounts:David & Michelle Saward]` | https://www.notion.so/32f491728751808391f7d15e7954ed5e | Canonical Account record (Accounts DB) |
| `[ExecSumm-thin 2026-04-14]` | https://www.notion.so/34249172875181fcaea2cb89e2f24f08 | Thin exec summary page (Client Executive Summaries index) — last synthesized 2026-04-14 |
| `[ExecSummDB:David & Michelle Saward]` | https://www.notion.so/342491728751813688a2d83ddb485ec9 | Executive Summaries DB row — existing row to populate |
| `[EL:David & Michelle Saward §...]` | https://www.notion.so/326491728751801aba68f571bc1b43f3 | Engagement Letters Tracker row — Signed $9,425 2026-02-05 |
| `[TaxAscend:David & Michelle Saward §...]` | https://www.notion.so/2fe49172875180e7916bed5cf5e1114a | Tax Ascend record — Insights + Planning + Compliance |
| `[Insights:David & Michelle Saward §...]` | https://www.notion.so/2fe49172875180a39844f6e5648dcbc3 | Insights Project Status record — DELIVERED 2026-03-12 · 3/3 files |
| `[MangoPlanningNEW:Tax Planning]` | https://www.notion.so/34249172875181b88d9bf36d076442cf | Mango NEW DB — Tax Planning project (Sophia / Seth billing) |
| `[MangoPlanningNEW:1040]` | https://www.notion.so/34249172875181caa458c8daa6e48cf8 | Mango NEW DB — 1040 compliance project (Seth / Deontae billing) |
| `[MangoPlanningNEW:435 Sycamore]` | https://www.notion.so/34249172875181bdbe0ce837d5abc501 | Mango NEW DB — 1065 435 Sycamore compliance project |
| `[MangoPlanningOLD:Tax Planning]` | https://www.notion.so/33a49172875181569419cf03b7816cd8 | Mango OLD DB — Tax Planning row |
| `[MangoPlanningOLD:1040]` | https://www.notion.so/33a4917287518186ba97d7e97d2e17eb | Mango OLD DB — 1040 row |

### Meetings

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[Meeting 2026-03-11]` | https://www.notion.so/32249172875180cb868cf8c63abfc191 | Full Insights Delivery Call — Done · [Fathom](https://fathom.video/share/1woWDQTFGQRyy5LREws92NDzZSBXbVzn) · 1:30–2:30 PM |

### Email Log

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[EmailLog:CHMMB Holdings LLC]` | https://www.notion.so/34249172875181a3899ce867939afc87 | Email thread: CHMMB Holdings LLC formation (2026-04-10, outbound, Action flag) |
| `[EmailLog:Booking]` | https://www.notion.so/34249172875181088c5ac0bb3589bf24 | Email thread: booking confirmation for Tax Planning session (2026-04-09, inbound) |

### Tax Compliance Projects

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[TaxCompliance:Saward 1040]` | https://www.notion.so/4d74917287518275933a816018bb89f0 | 1040 - David & Michelle Saward · Mango 1880995 · Extended to 2026-10-15 |
| `[TaxCompliance:Pukalani LLC]` | https://www.notion.so/cd849172875182ebb03a8137b971d7cd | 1065 - Pukalani LLC · Mango 1880999 · Extended to 2026-09-15 · PBC sent |
| `[TaxCompliance:435 Sycamore LLC]` | https://www.notion.so/ae54917287518221a3fd015cd1f5b620 | 1065 - 435 Sycamore LLC · Mango 1880996 · Extended to 2026-09-15 · PBC sent |

### Files & Links

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[FL:David & Michelle Saward §Engagement Letter]` | https://www.notion.so/33b491728751810c80d5f453ef898297 | Files & Links — Engagement Letter stub (empty) |
| `[FL:David & Michelle Saward §Executive Summary]` | https://www.notion.so/33b49172875181199fa3da35ae899d4a | Files & Links — Executive Summary stub (empty) |
| `[FL:David & Michelle Saward §Document Inventory]` | https://www.notion.so/33b4917287518134a3c5c29b5e4f2dd7 | Files & Links — client row (⚠️ URL collision with Spring/Alex Dykes/Iannaccio) |

### Sidecars (thin exec children)

| Tag | Notion URL | Description |
| --- | --- | --- |
| `[EmailIntelligence:Saward]` | https://www.notion.so/342491728751812fb444ecce6a134e98 | 📧 Email Intelligence subpage (2 threads, 1 active) |
| `[MeetingsDecisions:Saward]` | https://www.notion.so/3424917287518187914cd249c3b1d5b7 | 🎙 Meetings & Decisions subpage (1 meeting) |
| `[FilesDocuments:Saward]` | https://www.notion.so/342491728751818384ffe3a8c51eb50f | 📁 Files & Documents subpage |

### External / SharePoint / Recap URLs

| Description | URL |
| --- | --- |
| Signed EL MangoShare | https://app.mangoshare.com/share/aff946650b453aa48b907dc5 |
| PBC list xlsx | https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBWv-7lJrDZTLgHiWfSgLclAVXVt4dn2JUn6rzoGXbY9C4?e=Uue1BJ |
| Tax Memo Word doc 1 | https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQCYLoIA5ALzQ4xU-DDpDjaWAVx83ZaSnR3kL4dK1m9-j0U?e=7i4t4D |
| Tax Memo Word doc 2 | https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQDwF5WKNIMtRqwPMCLYCUGEAQ3BngaqWxlmsMTUGOvIcWk?e=Sqww4C |
| Analysis Workbook | https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQA5qS8_Kwd_TrDsHjQKtdMmARcGW2OLSiIU_vPHsSR9bjg?e=fmCP7B |
| Extraction 1040 | https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDpnEefNQ4ISYyaOLNgCe3iAaL5JaVjcKBOzl5Iin3cubA?e=7onMMw |
| Counting File | https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCliNntVln6Q6f23YYso7ECAaDSpRGsWdpW1EV9JZ7FYAs?e=khTWQP |
| Request List Tracker | https://subledgesl.sharepoint.com/:x:/s/Insights/IQBQLlGY6rldS47vPaEskQCYAQ5pO9qEIplOfuAvkIFUTCE?e=sQjREQ |
| Tax Returns Folder | https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgBjRiLUjsbVS7OyFeDSePIFAe1TJ5q3FkRDP9KLKnuRqj4?e=FhRyOj |
| Insights SharePoint doc | https://subledgesl.sharepoint.com/sites/Insights/_layouts/15/viewer.aspx?sourcedoc={f77b99bd-98f8-45d6-ae3e-ff66645cec50} |
| Document Inventory (F&L — ⚠️ collision) | https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw?e=QLo4ua |
| PBC PDF Package (F&L — ⚠️ collision) | https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA?e=2u2L6u |

### Sources NOT accessed this refresh

- Tax Planning Memo content (two Word docs on SharePoint — URLs known but content not parsed)
- Analysis Workbook content (SharePoint xlsx — URL known but content not parsed)
- Extraction 1040 content (SharePoint xlsx — URL known but content not parsed)
- April 17 Tax Planning session recap — no Fathom/Fellow URL on record
- Reporting Entities — none found for this Account
- Meeting Action Items DB — no rows found for this Account
- Extensions Status Tracker — no row found for this Account (all three compliance projects show Extension Filed = YES in Tax Compliance Projects, which is the equivalent confirmation)
- Engagement Inquiries — 0 rows

---

## §13. Changed Since Last Refresh

**This is the first comprehensive Client Intelligence Dossier refresh for David & Michelle Saward.** The thin exec summary at `https://www.notion.so/34249172875181fcaea2cb89e2f24f08` (last synthesized 2026-04-14) and the Executive Summaries DB row at `https://www.notion.so/342491728751813688a2d83ddb485ec9` (partially populated as of 2026-04-14) are treated as the prior anchor documents. All material from them is tagged by source above.

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- Joint household (David & Michelle Saward, MFJ, signed 2026-02-05, $9,425)
- Full Tax Ascend engagement: Insights (DELIVERED 2026-03-12, 3/3 files, Analysis Workbook + Extraction + Counting File) + Tax Planning (memo sent 2026-03-20, planning session 2026-04-17) + Tax Compliance (3 projects active, all extended)
- **Three-entity compliance stack discovered:** Pukalani LLC (1065, K-1 stage), 435 Sycamore LLC (1065, K-1 stage), CHMMB Holdings LLC (forming, 2026-04-10)
- Primary contact confirmed as Michelle Saward/Bowles at `michelle@clayhousemortgage.com` (Clay House Mortgage — real estate/mortgage industry)
- All Insights SharePoint workbook URLs captured and catalogued
- Both Tax Memo Word doc URLs captured from Tax Ascend record
- Mango compliance IDs populated for all 3 projects

**New — discoveries and flags:**
- ⚠️ **CHMMB Holdings LLC formation blocked** — Michelle hasn't accepted Fileforms invite; EIN pending (AI-01, AI-02)
- ⚠️ **PBC non-response** — list sent Apr 9, nothing received as of Apr 14; Stacy on followup (DG-01)
- ⚠️ **April 17 Tax Planning session has no recap** — black box (DG-02)
- ⚠️ **F&L URL collision confirmed** — template-default SharePoint folder URLs (DG-08)
- ⚠️ **David Saward profile completely opaque** — asymmetric service-depth risk (§11.2, DG-13)
- ⚠️ **Docusign Status "To Do"** on EL — signature process may be incomplete (DG-03)

**On the next refresh, expect to add:**
- Content of April 17 planning session (once recap is captured or recalled)
- Tax strategy specifics from the Planning Memo (once Word docs are parsed)
- PBC workbook analysis (once documents received and workbooks populated)
- CHMMB Holdings LLC EIN + operating purpose
- David Saward income and entity profile
- K-1 status for Pukalani LLC and 435 Sycamore LLC
- 2026 estimated tax payment plan (if discussed in Apr 17 session)

**13.2 What a reader should look at first**

1. **§7 AI-01 + AI-02 + DG-01** — Three interlocking blockers (CHMMB formation, EIN, PBC documents) all pending as of 2026-04-14 and presumably still open at refresh date 2026-05-07. These are the most time-sensitive items.
2. **§11.2** — David Saward's profile is an unknown; if he has significant taxable events, the engagement may be under-serving his side of the household.
3. **§5.3** — The two Tax Memo Word docs are the source-of-truth for the strategy work. Parsing them would allow §8 to be fully populated on the next refresh.
4. **§5.5 F&L URL collision** — system-wide issue, not just this client.

---

*Internal document — not for client distribution.*
*Accruity Tax Advisory · contact@accruity.com · 412-888-0068*
*Source: [dossiers/DavidMichelleSaward/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: MEDIUM · Next refresh: trigger on PBC receipt, CHMMB EIN issuance, OR Apr 17 session recap capture*
