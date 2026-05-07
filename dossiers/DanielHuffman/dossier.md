# Daniel Huffman — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Daniel Huffman |
| Client # | — (not populated on Account record) |
| Mango Client ID | **1900412** (Tax Compliance Projects record) |
| Mango Project | 1040- Daniel Huffman · 1065- K&D Management |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Depth mode | **Medium** — EL signed, 1 meeting, Insights delivered, active compliance in progress; no email log, no Tax Ascend row, no Reporting Entities |
| Engagement Stage | Tax Compliance — 1040 (extended to 2026-10-15) + possible 1065 (K&D Management) |
| Engagement Fee | **$3,925** (compliance EL signed 2026-03-30) |
| Temperature | Active but stalled — extension filed, PBC items not yet received; IRS transcript needed; outsourcing prep "not yet received" |
| Relationship Manager | Seth Johnson / Deontae Lafayette (billing partner) |
| Primary Contact | (not populated on Account record) |
| Data Sources (this refresh) | Notion Accounts record · 1 Engagement Letter (Signed) · 1 Insights Project record · 1 Meetings Tracker row · 3 Files & Links rows · Tax Compliance Projects record (1040) · Extensions Status Tracker · Outsourcing Assignment Tracker · Mango Planning (old + new DB) |
| Files NOT Accessible This Refresh | PBC Workbook, Tax Extraction, Tax Planning Memo, Meeting Prep Notes — all empty on Account record; no Tax Ascend row; no Reporting Entities |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

Daniel Huffman is an Accruity **Tax Compliance** client engaged on a **1040** return for the 2024/2025 tax year, with a secondary Mango project for **1065- K&D Management** suggesting a partnership interest. The engagement letter was signed on **2026-03-30** at a fee of **$3,925**, with deposit paid and an extension filed (extended due date **2026-10-15**). `[EL:Daniel Huffman]` `[TaxComp:1040 Daniel Huffman]`

**Current status — stalled on PBC items.** As of late April 2026, PBC items have not been received (`PBC list status: Sent List nothing received yet`). Internal notes from Seth/Deontae indicate the client needs to send W-2s, 1099s, brokerage statements, and confirm whether 2024 was filed. A PBC request email was sent on **2026-04-27** (generic income-document request with IRS account setup instructions). The team needs an **IRS transcript** to assess the filing status of 2024 and remediate any issues. `[EL:Daniel Huffman §Notes (PBC OPEN ITEMS)]` `[EL:Daniel Huffman §PBC list status]`

**Extension lifecycle.** Extension email sent **2026-04-10**; payment request sent **2026-04-14**; client responded and process is ongoing. `[Extensions:Daniel Huffman]`

**Outsourcing concern.** The Outsourcing Assignment Tracker shows **"No Mango Workspace — only found an old SOW in Greg Smith's workspace, no date of coverage."** This is an operational gap: the 1040 prep cannot be assigned to an outsourced preparer until the workspace issue is resolved. `[Outsourcing:Daniel Huffman]`

**Entity complexity flag.** The presence of a **1065- K&D Management** Mango project on both the old and new Mango Planning databases signals Daniel has a partnership interest. The partnership entity is not yet reflected in Reporting Entities, and there is no Reporting Entities DB row linked to the Account. `[MangoPlanningOld:Daniel Huffman]` `[MangoPlanningNew:Daniel Huffman]`

**Insights project delivered.** An Insights project exists and is status `DELIVERED` per the Insights tracker, but the Analysis and Extraction file fields are blank (`"Analysis: Waiting on Extraction"`), and no follow-up Tax Insights work is started. `[Insights:Daniel Huffman]`

**F&L URL collision check.** The three Files & Links rows contain two shell rows (EL stub, Executive Summary stub) with all URL fields blank, and one main row with SharePoint Document Inventory and PBC PDF Package URLs that appear client-specific (unlike the Spring/Alex pattern). **No collision detected this refresh.** `[FL:Daniel Huffman §Document Inventory]` `[FL:Daniel Huffman §PBC PDF Package]`

---

## §2. Client Profile

| Item | Value | Confidence | Source |
| --- | --- | --- | --- |
| Account name | Daniel Huffman | ✓ | `[Accounts:Daniel Huffman]` |
| Client # | — (blank) | ❌ | `[Accounts:Daniel Huffman.Client #]` |
| Mango Client ID | 1900412 | ✓ | `[TaxComp:1040 Daniel Huffman]` |
| Mango projects | 1040- Daniel Huffman (active) · 1065- K&D Management (active) | ✓ | `[MangoPlanningOld:Daniel Huffman]` `[MangoPlanningNew:Daniel Huffman]` |
| EL status | **Signed** · $3,925 · Batch added 2026-03-30 · Docusign Done | ✓ | `[EL:Daniel Huffman]` |
| Compliance Group Status | **Declined** ⚠️ | ✓ | `[EL:Daniel Huffman §Compliance Group Status]` |
| Tax proposal | COMMITTED | ✓ | `[EL:Daniel Huffman §TAX PROPOSAL]` |
| Docusign email status | Delivered | ✓ | `[EL:Daniel Huffman §Docusign Email Status]` |
| Mango portal | Portal Invite Sent · Project Created | ✓ | `[EL:Daniel Huffman §Mango Portal Invite]` |
| PBC list status | Sent List nothing received yet | ⚠️ | `[EL:Daniel Huffman §PBC list status]` |
| Open items status | None Sent (as of EL row) | ✓ | `[EL:Daniel Huffman §Open items Status]` |
| Extension status | Filed ✓ · Extended due 2026-10-15 · Extension email sent 2026-04-10 | ✓ | `[TaxComp:1040 Daniel Huffman]` `[Extensions:Daniel Huffman]` |
| Compliance correct status | 04 Internal WP Preparation | ✓ | `[TaxComp:1040 Daniel Huffman]` |
| Mango task | 04 Preparation (External) | ✓ | `[TaxComp:1040 Daniel Huffman]` |
| Review required | No | ✓ | `[TaxComp:1040 Daniel Huffman]` |
| Preparer / Manager | Deontae Lafayette | ✓ | `[TaxComp:1040 Daniel Huffman]` |
| SOW (Mangoshare) | [app.mangoshare.com/share/e37ffcb88b58f56aded14c74](https://app.mangoshare.com/share/e37ffcb88b58f56aded14c74) | ✓ | `[Outsourcing:Daniel Huffman]` |
| Entity services | No services ticked on signed EL | ⚠️ | `[EL:Daniel Huffman §Entity Compliance services]` |
| Insights project | DELIVERED (analysis waiting on extraction) | ~ | `[Insights:Daniel Huffman]` |
| Tax Ascend row | **None found** | ❌ | No match in Tax Ascend DB |
| Reporting Entities | **None linked** to Account | ❌ | `[Accounts:Daniel Huffman.# of Reporting Entities]` |

### Principals at a glance

- **Daniel Huffman** — individual; filing 1040; partnership interest via K&D Management (1065). No contact email, phone, or address populated on Account record.

### Entity stack

| Entity | Type | Mango Project | Status | Source |
| --- | --- | --- | --- | --- |
| Daniel Huffman (individual) | 1040 | 1040- Daniel Huffman | Active · In Progress | `[TaxComp:1040]` |
| K&D Management | 1065 (partnership) | 1065- K&D Management | Active (old + new Mango DB) | `[MangoPlanningOld §K&D]` `[MangoPlanningNew §K&D]` |

Note: K&D Management entity type, EIN, state, and ownership split are unknown — no Reporting Entity record, no workbook linked.

---

## §3. Email Intelligence

**0 email threads in Client Email Log** for Daniel Huffman. The Account record has no Email Log relation populated; no `📧 Email Intelligence` subpage exists.

**What is on file (from sidecar records):**

| Date | Direction | Subject / Content | Source |
| --- | --- | --- | --- |
| 2026-04-10 | Outbound (Accruity → Daniel) | Extension email sent | `[Extensions:Daniel Huffman §date:Date Extension Email reminder Sent]` |
| 2026-04-14 | Outbound (Accruity → Daniel) | Extension Payment Request — attachment `Extension_Payment_Request_-_Hamilton_Dan_and_Kelly.pdf` ⚠️ | `[Extensions:Daniel Huffman §Payment Request sent]` |
| 2026-04-27 | Outbound (Accruity → Daniel) | PBC request — W-2, 1099, brokerage, 2024 filing confirmation + IRS account setup instructions | `[EL:Daniel Huffman §Notes (PBC OPEN ITEMS)]` + image embedded in EL page |

**Anomaly flag — wrong-client attachment.** The extension payment request PDF is named `Extension_Payment_Request_-_Hamilton_Dan_and_Kelly.pdf`. This is a **Dan Hamilton / Kelly Hamilton document** apparently attached to Daniel Huffman's record in error. Promoted to §7 as HIGH data integrity issue. `[Extensions:Daniel Huffman §Payment Request sent]`

**Email log gap.** No Client Email Log rows are linked to Daniel's Account. This may mean Make.com is not capturing his thread, or emails are going to a personal address not yet in the system. Backfill is needed.

---

## §4. Meeting History

**1 meeting on file.**

| Date | Type | Time | Status | Recap | Notes | Source |
| --- | --- | --- | --- | --- | --- | --- |
| **2025-08-22** | Full Insights — Delivery call | 3:00 – 3:30 PM | **Pending** ⚠️ | FIND (not yet located) | Recap status "FIND" — no Fathom/Fellow URL attached | `[Meeting 2025-08-22 Huffman]` |

**Observations:**
- This is an **August 2025** meeting — predates the March 2026 EL signing by ~7 months. The Insights delivery call was likely part of the pre-engagement or prior tax year cycle.
- Recap is flagged as "FIND" — the meeting happened but the recap was never linked.
- No time zone specified; 3:00–3:30 PM EST assumed.
- 0/1 meetings restricted.

**Gap:** Pull the Fathom/Fellow transcript for 2025-08-22 Insights Delivery call next refresh.

---

## §5. Document Inventory

### 5.1 Engagement Letter

| Field | Value |
| --- | --- |
| Status | **Signed** |
| Price | **$3,925** |
| Batch Added | 2026-03-30 |
| Docusign Status | Done |
| Signed EL (Mangoshare) | [app.mangoshare.com/share/97dfbddc430a56d3a1851b4b](https://app.mangoshare.com/share/97dfbddc430a56d3a1851b4b) |
| PBC list email | None sent (as of EL record) |
| PBC list status | Sent List nothing received yet |
| Entity services | No services ticked on signed EL ⚠️ |
| Compliance Group Status | **Declined** ⚠️ |

Note: "Compliance Group Status = Declined" is notable — this typically means Daniel opted out of the standard compliance group bundle. Clarification needed.

### 5.2 Files & Links Rows (3 total)

| Row | Name | Document Inventory URL | PBC PDF Package URL | Other URLs | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Daniel Huffman (main) | [SharePoint folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw?e=QLo4ua) | [SharePoint folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA?e=2u2L6u) | — | `[FL:Daniel Huffman]` |
| 2 | Engagement Letter (stub) | — | — | All fields blank | `[FL:Engagement Letter stub]` |
| 3 | Executive Summary (stub) | — | — | All fields blank | `[FL:Executive Summary stub]` |

**F&L URL collision check:** Document Inventory and PBC Package URLs are unique SharePoint paths (not matching Spring Bengtzen's known collision paths). **No collision confirmed.** `[FL:Daniel Huffman §Document Inventory]`

### 5.3 Tax Compliance Status (Mango)

| Field | Value |
| --- | --- |
| Mango ID | 1900412 |
| Status | 04 Internal WP Preparation |
| Mango Task | 04 Preparation (External) |
| Extension filed | Yes ✓ |
| Original due | 2026-04-15 |
| Extended due | **2026-10-15** |
| Review required | No |
| Preparer | Deontae Lafayette |

### 5.4 Insights Project

| Field | Value |
| --- | --- |
| Status (Precheck) | DELIVERED |
| Status (Tax Insights) | Not started |
| Analysis | Waiting on Extraction |
| Received Files | — (blank) |
| Next Scheduled Call | Delivery Call |
| Accelo Status | To Check Accelo |
| Mango Status | To Check |
| Temp Filter | "Piah to do - Check meeting recap 04/29" ⚠️ |

Note: "Piah to do - Check meeting recap 04/29" is an internal note flagging that a staff member (Piah) needs to find the meeting recap. Ties to the §4 "FIND" flag.

### 5.5 Workbooks not accessible this refresh

| Workbook | Status |
| --- | --- |
| PBC Workbook | Not linked on Account |
| Tax Extraction | Not linked on Account |
| Tax Analysis / Planning Memo | Not linked on Account |
| Meeting Prep Notes | Not linked on Account |
| K&D Management 1065 workbook | No Reporting Entity or workbook linked |

### 5.6 Outsourcing

| Field | Value |
| --- | --- |
| Assignment status | Not Yet received |
| Client folder link | — (blank) |
| SOW | [Mangoshare](https://app.mangoshare.com/share/e37ffcb88b58f56aded14c74) |
| Notes | **"No mango Workspace. Only found an old SOW in Greg Smith's workspace, no date of coverage"** ⚠️ |
| Mango Edit Yr Status | Clarify with Stacy |
| XCM status | Notif Not Yet Rcvd |

---

## §6. Claude Work Product

**0 prior Claude Summaries found** for Daniel Huffman in the Claude Summaries DB.

**0 Activity Log rows** found tied to Daniel Huffman's Account.

This refresh (2026-05-07) creates the **first Claude Summary** for this client. The Turn 11 Notion write will create the first Claude Summaries DB row.

---

## §7. Action Items — Rolled Up

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **Receive PBC items from Daniel** — list sent 2026-04-27 (W-2, 1099, brokerage, 2024 filing confirmation); nothing received yet | Daniel / Deontae | 🔴 HIGH (compliance gating) | `[EL:Daniel Huffman §PBC list status]` |
| 2 | **Pull IRS transcript for Daniel** — needed to determine if 2024 return was filed / silently rejected | Deontae | 🔴 HIGH (compliance gating) | `[EL:Daniel Huffman §Notes (PBC OPEN ITEMS)]` |
| 3 | **Resolve outsourcing workspace gap** — "No mango Workspace; old SOW in Greg Smith's workspace, no date of coverage." Clarify with Stacy; create proper workspace before prep can proceed | Stacy / Deontae | 🔴 HIGH (prep blocking) | `[Outsourcing:Daniel Huffman §Notes]` |
| 4 | **Investigate wrong-client attachment** — extension payment request PDF named `Extension_Payment_Request_-_Hamilton_Dan_and_Kelly.pdf` was attached to Daniel Huffman's Extensions record. Likely a Dan Hamilton PDF filed in error; verify and correct | Accruity ops | 🔴 HIGH (data integrity) | `[Extensions:Daniel Huffman §Payment Request sent]` |
| 5 | **Clarify Compliance Group Status = "Declined"** — was this intentional? Affects compliance group billing and bundling | Seth / Deontae | 🟡 MED | `[EL:Daniel Huffman §Compliance Group Status]` |
| 6 | **Clarify K&D Management entity** — confirm entity type (LLC/Partnership), EIN, ownership %, state; create Reporting Entity record; determine if 1065 is in scope for 2024/2025 prep | Deontae / Seth | 🟡 MED | `[MangoPlanningOld §K&D]` |
| 7 | **Find and link meeting recap for 2025-08-22** Insights Delivery call — flagged as "FIND" / "Piah to do - Check meeting recap 04/29" | Piah / ops | 🟡 MED | `[Meeting 2025-08-22]` `[Insights §Temp Filter]` |
| 8 | **Add Reporting Entities** for Daniel Huffman (1040 individual + K&D Management 1065) | Accruity ops | 🟡 MED | `[Accounts:Daniel Huffman.# of Reporting Entities]` |
| 9 | **Populate Client # field** on Account record | Accruity ops | 🟢 LOW | `[Accounts:Daniel Huffman.Client #]` |
| 10 | **Backfill email log** — 0 threads captured; check Make scenario for Daniel's email address | Generator / ops | 🟢 LOW | `[§3]` |
| 11 | **Confirm "No services ticked on signed EL"** — entity compliance services field is blank; confirm whether any entities (K&D Management) should be included in the compliance engagement | Seth / Deontae | 🟡 MED | `[EL:Daniel Huffman §Entity Compliance services]` |

Total: **11 open items** (4 HIGH, 4 MED, 3 LOW).

---

## §8. Tax Strategies & Projected Savings

**Sparse this refresh** — engagement is in compliance-prep phase; PBC items not yet received; no Tax Analysis workbook accessible.

| Strategy | Status | Estimated Savings | Source |
| --- | --- | --- | --- |
| 1040 compliance prep (2024/2025) | In progress (awaiting PBC + IRS transcript) | N/A | `[TaxComp:1040 Daniel Huffman]` |
| K&D Management 1065 partnership return | ? Scope uncertain — no Reporting Entity, EL has no entity services ticked | `? Pending workbook ingestion` | `[MangoPlanningOld §K&D]` |
| All planning strategies | `? Pending — PBC items not received; no Tax Analysis workbook` | — | — |

**Key unknowns driving all planning gaps:**
1. 2024 return filing status (was it filed? IRS transcript needed)
2. K&D Management entity details and whether it's in scope
3. Daniel's income breakdown (W-2 vs. K-1 vs. self-employment)
4. Property ownership (Cost Seg applicability unknown)

---

## §9. Opportunity Flags (auto-detected)

**Insufficient data for full classifier this refresh.** Assessments below are based on available signals only.

### 9.1 Cost Segregation

| Signal | Result |
| --- | --- |
| Reporting Entities with real property | None found (0 Reporting Entities) |
| Property type indicators | None in file |
| **Cost Seg flag** | ⬜ NOT FLAGGED — insufficient data |

### 9.2 S-Corp Election Candidate

| Signal | Result |
| --- | --- |
| Self-employment / passthrough income | ? Unknown — no workbook, no K-1 in file |
| Entity classification | K&D Management type unknown (could be partnership electing S treatment) |
| Net SE earnings threshold ($40k+) | ? Unknown |
| **S-Corp flag** | 🟡 WATCH — K&D Management could be an LLC that would benefit from S-Corp election if SE income is material; insufficient data to confirm |

### 9.3 Other Flags

| Flag | Detail | Source |
| --- | --- | --- |
| IRS compliance risk | 2024 return filing status unknown; IRS transcript needed; first notice pattern in PBC email | `[EL:Daniel Huffman §Notes PBC]` |
| Partnership basis / K-1 complexity | K&D Management 1065 in scope; basis tracking, guaranteed payments, SE treatment all unknown | `[MangoPlanningOld §K&D]` |

**HIGH opportunity flags promotable to §7:** None confirmed (data insufficient). K&D Management S-Corp watch promoted to §7 Action #6 as investigation item.

---

## §10. Operations Analysis

Daniel Huffman is a **compliance-only engagement** in mid-2026, stalled at the PBC collection phase with three compounding blockers:

1. **IRS transcript gap** — the 2024 return may not have been filed or may have been silently rejected. This is unusual and elevates compliance risk beyond a typical extension. The internal PBC email (2026-04-27) explicitly says "This is the first notice sent when a return is missing."

2. **Outsourcing workspace missing** — the CCH Outsourcing tracker shows the preparer workspace doesn't exist; only an old SOW in Greg Smith's workspace was found. This means the return physically cannot enter preparation workflow until the workspace is created and the engagement is handed off properly.

3. **K&D Management scope ambiguity** — two Mango projects exist (1040 + 1065) but only one EL was signed ($3,925) with no entity services ticked. If the 1065 is in scope, it either needs to be added to the EL or clarified as out-of-scope. This ambiguity could delay delivery.

**Engagement health: YELLOW.** Clean EL signature and portal setup, but stalled on basics. The August 2025 Insights delivery pre-dates the March 2026 EL by 7 months — suggesting Daniel was an Insights client before converting to a compliance engagement. That conversion may be the source of the "No mango workspace" gap if the old workspace was under a prior team member.

**Manager alignment:** Seth is tagged as Manager on Mango Planning records; Deontae is the preparer and billing partner on the 1040 Tax Compliance project. Deontae should be primary driver of the PBC + transcript workflow; Seth owns the entity scope clarification.

---

## §11. Individual Profile

| Dimension | Detail | Confidence | Source |
| --- | --- | --- | --- |
| Full name | Daniel Huffman | ✓ | `[Accounts:Daniel Huffman]` |
| Email | (not populated on Account record) | ❌ | `[Accounts:Daniel Huffman.New Contact: Email]` |
| Phone | (not populated) | ❌ | `[Accounts:Daniel Huffman.New Contact: PH#]` |
| Client # | (not assigned) | ❌ | `[Accounts:Daniel Huffman.Client #]` |
| Filing type | 1040 individual + likely 1065 K&D Management | ~ | `[MangoPlanningOld §K&D]` |
| Filing status (MFJ/S/etc.) | ? Unknown — single engagement letter but no household info | ? | — |
| Engagement signed | 2026-03-30 · $3,925 | ✓ | `[EL:Daniel Huffman]` |
| Tax year in prep | 2024 (possibly also 2025) — EL notes "2024 and 2025" in PBC request | ~ | `[EL:Daniel Huffman §Notes PBC]` |
| Prior preparer | ? — SOW found in Greg Smith's workspace (old) | ~ | `[Outsourcing:Daniel Huffman §Notes]` |
| Insights history | Insights delivered pre-engagement (2025-08-22 delivery call) | ✓ | `[Meeting 2025-08-22]` `[Insights:Daniel Huffman]` |
| Relationship-risk read | YELLOW — PBC stall + IRS uncertainty + outsourcing gap; not red (EL signed, client responded to extension payment request) | derived | — |
| Outstanding to Daniel | 2 items (Action #1 — PBC docs; Action #2 pull IRS transcript) | ✓ | `[§7]` |

---

## §12. Provenance Index

### Notion — Account record
- `[Accounts:Daniel Huffman]` → [notion.so/32f49172875180b68b96e9f0f4cd1dc7](https://www.notion.so/32f49172875180b68b96e9f0f4cd1dc7) — primary Account; Client # blank; 1 meeting, 3 F&L, 1 EL, 1 Insights project

### Notion — Engagement Letters Tracker
- `[EL:Daniel Huffman]` → [notion.so/2f1491728751809f9a04e208c00c0d38](https://www.notion.so/2f1491728751809f9a04e208c00c0d38) — Signed $3,925 · 2026-03-30 · Compliance Group Status: Declined · PBC list sent but nothing received

### Notion — Insights Project Status
- `[Insights:Daniel Huffman]` → [notion.so/348491728751803cb3bccf757ac3abd6](https://www.notion.so/348491728751803cb3bccf757ac3abd6) — DELIVERED · analysis waiting on extraction · "Piah to do - Check meeting recap 04/29"

### Notion — Tax Compliance Projects
- `[TaxComp:1040 Daniel Huffman]` → [notion.so/ee149172875183d9a6df81c4f4a3a382](https://www.notion.so/ee149172875183d9a6df81c4f4a3a382) — Mango ID 1900412 · 04 Internal WP Preparation · Extended due 2026-10-15 · Deontae Lafayette

### Notion — Meetings Tracker
- `[Meeting 2025-08-22 Huffman]` → [notion.so/2fb4917287518058abdacafb8160c007](https://www.notion.so/2fb4917287518058abdacafb8160c007) — Full Insights Delivery call · 3:00–3:30 PM · Status Pending · Recap "FIND"

### Notion — Files & Links
- `[FL:Daniel Huffman]` → [notion.so/33b491728751812c8843d45950da1e6b](https://www.notion.so/33b491728751812c8843d45950da1e6b) — Document Inventory: [SharePoint](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw?e=QLo4ua) · PBC PDF Package: [SharePoint](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA?e=2u2L6u)
- `[FL:Engagement Letter stub]` → [notion.so/33b491728751816e9030eaa3dd99d94c](https://www.notion.so/33b491728751816e9030eaa3dd99d94c) — all URL fields blank
- `[FL:Executive Summary stub]` → [notion.so/33b491728751814f9eaec663e0f7fcf8](https://www.notion.so/33b491728751814f9eaec663e0f7fcf8) — all URL fields blank

### Notion — Extensions Status Tracker
- `[Extensions:Daniel Huffman]` → [notion.so/34249172875181b4a177cfd41ec6b08c](https://www.notion.so/34249172875181b4a177cfd41ec6b08c) — Extension email sent 2026-04-10 · Payment request sent 2026-04-14 · Status "In progress (Client ongoing queries)" · ⚠️ Wrong-client PDF attached

### Notion — Outsourcing Assignment Tracker
- `[Outsourcing:Daniel Huffman]` → [notion.so/33349172875180518f60e2036d7e175e](https://www.notion.so/33349172875180518f60e2036d7e175e) — Not Yet received · No mango workspace · SOW: [Mangoshare](https://app.mangoshare.com/share/e37ffcb88b58f56aded14c74)

### Notion — Mango Planning (old DB)
- `[MangoPlanningOld:Daniel Huffman 1040]` → [notion.so/33a49172875181f2b6d9f1af24cb64af](https://www.notion.so/33a49172875181f2b6d9f1af24cb64af) — 1040- Daniel Huffman
- `[MangoPlanningOld:Daniel Huffman K&D]` → [notion.so/33a491728751814cade3d7a738140ea9](https://www.notion.so/33a491728751814cade3d7a738140ea9) — 1065- K&D Management

### Notion — Mango Planning (new DB)
- `[MangoPlanningNew:Daniel Huffman 1040]` → [notion.so/342491728751816fab7ef4b36fcde3e5](https://www.notion.so/342491728751816fab7ef4b36fcde3e5) — 1040- Daniel Huffman · Tags: Tax Compliance, Extended (Compliance)
- `[MangoPlanningNew:Daniel Huffman K&D]` → [notion.so/3424917287518168ba96d866c09e2c44](https://www.notion.so/3424917287518168ba96d866c09e2c44) — 1065- K&D Management · Tags: Tax Planning, Extended (Compliance), Tax Compliance

### Portals / SharePoint
- Signed EL (Mangoshare): [app.mangoshare.com/share/97dfbddc430a56d3a1851b4b](https://app.mangoshare.com/share/97dfbddc430a56d3a1851b4b)
- SOW (Mangoshare): [app.mangoshare.com/share/e37ffcb88b58f56aded14c74](https://app.mangoshare.com/share/e37ffcb88b58f56aded14c74)
- Document Inventory (SharePoint): [link](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw?e=QLo4ua)
- PBC PDF Package (SharePoint): [link](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA?e=2u2L6u)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.** No prior dossier existed.

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- EL Signed 2026-03-30 · $3,925 · Compliance Group Status Declined · PBC sent but nothing received
- 1040 Tax Compliance project: Mango ID 1900412 · 04 Internal WP Preparation · Extension to 2026-10-15
- K&D Management 1065 project in Mango (old + new DB) — entity type/scope unclear
- Insights project DELIVERED (2025-08-22 delivery call, recap not yet linked)
- Extension process: email sent 2026-04-10, payment request 2026-04-14, client ongoing
- Outsourcing: no Mango workspace; old SOW only in Greg Smith's workspace
- 3 Files & Links rows (1 populated with SharePoint links, 2 shell stubs)

**New — discoveries:**
- ⚠️ **Wrong-client attachment** — `Extension_Payment_Request_-_Hamilton_Dan_and_Kelly.pdf` filed on Daniel Huffman's Extensions record → Action #4 HIGH
- ⚠️ **PBC notes indicate 2024 return may not have been filed** — IRS transcript urgently needed → Action #2 HIGH
- ⚠️ **No Mango outsourcing workspace** — prep cannot proceed → Action #3 HIGH
- ⚠️ **K&D Management entity scope ambiguous** — EL has no entity services ticked → Action #6 MED
- ⚠️ **Compliance Group Status = Declined** — unusual; needs clarification → Action #5 MED
- ✓ **F&L URL collision: NOT present** — Daniel's SharePoint URLs are unique

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 11 | Open action items | §7 |
| 5 | Workbooks not linked | §5.5 |
| 0 | Reporting Entities | §2 |
| 0 | Email threads | §3 |
| 1 | Meeting on file (recap missing) | §4 |
| 0 | Prior Claude Summaries | §6 |

### 13.3 What a reader should look at first

1. **§7 Action #2** — IRS transcript: 2024 may not be filed; this is a potential compliance emergency
2. **§7 Action #4** — Wrong-client attachment: data integrity issue needs immediate correction
3. **§7 Action #3** — Outsourcing workspace: prep literally cannot start until fixed
4. **§7 Action #1** — PBC items: gating all return work
5. **§7 Action #6** — K&D Management: confirm whether 1065 is in scope before the extended due date

---

*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/DanielHuffman/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: medium · Next refresh: trigger on PBC items received OR IRS transcript obtained*
