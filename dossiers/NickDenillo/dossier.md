# Nick Denillo — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Nick Denillo (household: Nick & Alexandra Denillo) |
| Client # | **14110415-01** |
| Mango Client ID | **937731** |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Depth mode | **MEDIUM** — single meeting on record; 5 action items; 2 active compliance projects; rich Tax Ascend + engagement letter data; Tax Memo delivered; no email log rows on Account |
| Engagement Stage | Tax Ascend — New Client GC · Insights (DELIVERED) · Compliance (2 active returns) |
| Engagement Fee | **$4,000** (compliance EL signed/executed) |
| Temperature | Active in compliance — both 1040 and 1120-S extended, with offshore; S-Corp W-2 optimization in flight; 5 meeting action items not started |
| Relationship Manager | Seth Johnson |
| Primary Contact | Nick Denillo · nick@denillo.com · (412) 608-4761 |
| Data Sources (this refresh) | Notion Accounts record · Engagement Letter (Signed/Executed) · Tax Ascend record · Insights Project record · 1 Meetings Tracker row · 5 Meeting Action Items · 3 Files & Links rows · 2 Tax Compliance Project rows · 2 Outsourcing Assignment Tracker rows · Client Contacts record · Email addresses record |
| Files NOT Accessible This Refresh | Tax Planning Memo (URL present on Tax Ascend but not surfaced as structured text); Analysis file + Extraction 1040 (links present on Insights record but workbooks not parsed); PBC Workbook (Account field empty) |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

Nick and Alexandra Denillo are an **active Accruity household** enrolled in the full Tax Ascend New Client GC track: Insights (delivered) + Compliance (2 returns, both extended and with offshore). The engagement is operationally in-motion but carries **5 open Meeting Action Items** from the January 22 Tax Insights Clarification call — none yet marked started — representing meaningful unfinished work from the core planning session.

**Key structural fact:** Nick runs **Denillo Heating and Cooling** as an **S-Corporation** (1120-S). The Jan 22 planning session revealed a significant S-Corp W-2 optimization opportunity: Nick's W-2 was running at ~$194K; the plan is to drop it to ~$100K, saving **~$7K annually in SE tax**. This was recorded as a HIGH-priority action item assigned to Nick (AI-78). `[MAI:AI-78]`

**Compliance status (as of 2026-05-07):** Both the 1040 and 1120-S are extended and with offshore (Xpitax). The 1120-S (original due 2026-03-15, extended to 2026-09-15) is ahead of the 1040 (original due 2026-04-15, extended to 2026-10-15) in workflow — the 1120-S is at "07 L1 Revisions (External)" while the 1040 is at "03 Collect and Review K-1s," suggesting K-1 output from the S-Corp return must flow into the personal return. `[TCP:1120-S]` `[TCP:1040]`

**Tax Memo sent 2025-12-22; EL signed 2025-12-29.** Scope per Tax Ascend: Semi-Annual Year-end Tax Projection Analysis, Semi-Annual Custom Tax Planning, Annual Organization Chart Refresh, Tax Preparation (business & personal). Planning status on Tax Ascend shows "New Client GC" — consistent with this being the first comprehensive planning cycle. `[TaxAscend:NickDenillo]` `[EL:NickDenillo]`

**Important contact note:** Alexandra Denillo uses alexandra@denillo.com for future tax emails (per EL notes). Nick's primary is nick@denillo.com / (412) 608-4761. `[EL:NickDenillo §Notes]` `[Contact:Nick]`

**Open plumbing gap:** 0 email log rows on the Account; Tax Ascend compliance status shows "Open Items List - Client feedback" — which may indicate PBC items are pending client response rather than fully received. `[TaxAscend §Compliance Status]`

---

## §2. Client Profile

| Item | Value | Source |
| --- | --- | --- |
| Account name | Nick Denillo | `[Accounts]` |
| Household filing | Nick & Alexandra Denillo (joint — MFJ assumed) | `[EL §CLIENT]` |
| Client # | 14110415-01 | `[Accounts]` |
| Mango Client ID | 937731 | `[Accounts]` |
| Primary email | nick@denillo.com | `[Contact:Nick]` `[EmailDB]` |
| Alexandra email | alexandra@denillo.com | `[EL §Notes (PBC OPEN ITEMS)]` |
| Primary phone | (412) 608-4761 | `[Contact:Nick]` |
| Relationship Manager | Seth Johnson | `[Accounts §Relationship Manager]` |
| Partner | Per Account relation `30d4917287518141bf8acf3dca2654a7` — identity not surfaced | `[Accounts §Partner]` |
| Engagement type | Tax Ascend New Client GC — Insights + Compliance | `[TaxAscend §TAX ASCEND TYPE]` |
| EL status | **Signed · Executed** | `[EL §Engagement Letter Status]` `[EL §Compliance Group Status]` |
| EL date | Batch added 2026-01-23; Date Signed 2025-12-29 | `[EL §Batch Added]` `[EL §Date Signed]` |
| Engagement fee | **$4,000** | `[EL §Price]` |
| Deposit | Paid ✓ | `[EL §Deposit Paid]` |
| Mango portal | Customer Accessed ✓ | `[EL §Mango Portal Invite]` |
| PBC list sent | 2026-01-29 | `[EL §Date PBC list sent]` |
| PBC status | "Received PBC items" | `[EL §PBC list status]` |
| Open items email | Sent 2026-03-09 (`Denillo_Open_Items_-_2026_03_09.msg`) | `[EL §Ext Email Sent]` `[EL §Date EXT EMAIL sent]` |
| Tax Memo sent | 2025-12-22 | `[TaxAscend §date:Tax Memo Sent]` |
| Tax Memo status | SENT | `[TaxAscend §TAX MEMO STATUS]` |
| Insights status | **DELIVERED** (Analysis: Completed) | `[Insights §Status (Precheck)]` `[Insights §Analysis]` |
| Planning status | New Client GC | `[TaxAscend §Planning Status]` |
| Compliance status | Open Items List - Client feedback | `[TaxAscend §Compliance Status]` |

### 2.1 Entity Stack

| Entity | Form | Role | Status | Source |
| --- | --- | --- | --- | --- |
| Nick & Alexandra Denillo (personal) | **1040** | Joint personal return | Extended to 2026-10-15 · Stage: Collect & Review K-1s | `[TCP:1040]` |
| **Denillo Heating and Cooling** | **1120-S** | S-Corporation (operating entity) | Extended to 2026-09-15 · Stage: L1 Revisions (External) · With Xpitax | `[TCP:1120-S]` `[OAT:1120-S]` |

> Note: EL entity compliance services field reads "No services ticked on signed EL" — this may mean entity compliance is rolled into the primary engagement scope or that the EL was finalized before entity list was populated. `[EL §Entity Compliance services]`

### 2.2 Principals

- **Nick Denillo** — primary; owns/runs Denillo Heating and Cooling S-Corp; primary point of contact; historically ran W-2 at ~$194K (flagged for optimization) `[MAI:AI-78]`
- **Alexandra Denillo** — spouse; preferred email alexandra@denillo.com for tax correspondence going forward `[EL §Notes]`

---

## §3. Email Intelligence

**0 email threads on Account** in the Client Email Log. The Account record has no `Email Log` relation populated and no `📧 Email Intelligence` subpage. `[Accounts §Email Log]`

**Evidence of email activity found in sidecars:**
- EL tracker carries two Outlook attachments: `Nick_Denillo.msg` and `Denillo_-_Open_Items.msg` (PBC open items communication), plus `Denillo_Open_Items_-_2026_03_09.msg` in the EL page body
- Open items email sent 2026-03-09; extension email sent 2026-03-09 `[EL §Ext Email Sent]` `[EL §Date EXT EMAIL sent]`
- Contact note: **always use alexandra@denillo.com** for future tax emails (per EL notes)
- A Client Meetings search result references: `"📝 Nick Denillo's Tax Insights Clarification Call on Jan 22 — Key decisions inside.msg"` suggesting a meeting recap/summary email was sent to the account on 2026-01-28 `[Search:ClientMeetings]`

**Plumbing gap:** Make pipeline has not connected Denillo email threads to the Client Email Log. Promote to §7.

---

## §4. Meeting History

**1 meeting on file.** Only one meeting row linked to the Account.

| Date | Type | Time (EST) | Status | Recap | Source |
| --- | --- | --- | --- | --- | --- |
| **2026-01-22** | Tax Insights — Clarification Call | 1:00 PM – 2:00 PM | Done ✓ | [Fellow](https://sg5.fellow.app/uni/ls/click?upn=u001.Y1tiWTgJ1PJMrKyj7dbJHqPp-2FT6JwyJKYnLKCSUh0dRKOQm2cj6PWWcYw1WzaV8IB9FGQODOjD0Q-2B5JJcCrN5OybSGI1b-2BgKX4rIMjn2QxGMRMi1xTYiMHANgq8KChN2chUu5CqWkLqzFSjzMeeODN2bLA9cE0CaSDeUzWz8eB10l2Gd3-2Fy6ouPXeVkFUpRdWLnfUXPFp0T8ELZQfmLOFW6u94nqgP3eECpJc-2BHMlagjXK-2FxoguWsB2mMb6c88DyMA0n-2FLRbxxTtJ1mI7N2SJQa35EMJ-2Bm-2FJiYfUzS2gI31LyD62MOKtoHsXUZa0E9p-2BnRRkaPoJBP3TfBLiTwzJkxf8CWSuyNjSfOHzDIzrxKWTnx0RiCL14nIrbfdK7H-2F8AtB2cKuEdc65HCEKDlZ34CND5swzAv-2FlGqYGRqKKBbQpLm3LsidJk-2F03hCckMlFHButRWoL4NeKyWI7fW1dlX8iwBAnP-2BpyklrbK9QUWQGK8adMNbZCTm22B1ajabbuy7kUGGr-2Fz7-2FAWsW69Bj-2BXA1THhY-2BnZT6YuqC5SfZP1aIEuwHvUhS-2FWAe0O-2BWbmyOo9eWq_nCyD0OjfWWda0fny7BdXCaZa1dTuV49YyfNg3yJrg97FL3Kv0EHJMcicPdkuqwuRVRn6Mu-2BScohXEswDG7xQorYek-2Bl35xulZiQcqw4XVChofL9N47SO-2BXSqvdhIAv91lRSYwApPWQabuHbojdOXXrZJ0aXLJk-2F4hmjuh1yc2M1ROX0kme5x-2B93T-2FjErUjs2-2FEDyMxw8nUDvKKhrvi4jKeXdr3b-2BN-2FJGY8uOlfI8Wkr81IVAIZNwajOzIevnPOBqd3VUrk34qY19nXLpwB8rdhJ-2F7H2zfs5UDYPVVwmrnZI7F3Bbi3fftkBwpSLghunQhFnm-2FgqMKxdikiHOFv282vkZhn0tclCnG-2Bb1Ln76JXkqpMVpB3Nl8YeUbCFvS5gcKpRQeIFOm-2FCRq4R7lAKdPcCmSwoqHxd56Ofj6GS-2FbSKabH-2BJqapGAeUiL-2BJDkyug) | `[Meeting 2026-01-22]` |

**What this meeting produced:** 5 action items (AI-75 through AI-79) covering: updated tax planning memo delivery, EL + PBC checklist send, S-Corp W-2 optimization ($194K → $100K, saves ~$7K/yr SE tax), 529 rules research re: NIL pay for child, and W-2 print/distribution. All 5 remain "Not started" as of 2026-04-01. `[MAI:AI-75 through AI-79]`

**Cadence note:** Only 1 meeting on file despite being a New Client GC enrollment. The Tax Ascend record notes "Temp Filter: Piah to do - Check meeting recap 04/29" — suggesting a follow-up meeting may have occurred around 2026-04-29 whose recap had not been linked to the Meetings Tracker as of this refresh. `[Insights §Temp Filter]`

**Restricted flag:** 0/1 meetings restricted. 0 Meeting Transcripts linked to Account.

---

## §5. Document Inventory

### 5.1 Engagement Letter (clean state)

| Field | Value | Source |
| --- | --- | --- |
| EL name | Nick & Alexandra Denillo | `[EL §CLIENT]` |
| Status | Signed · Executed | `[EL]` |
| Price | **$4,000** | `[EL §Price]` |
| Deposit | Paid ✓ | `[EL §Deposit Paid]` |
| Docusign status | Done | `[EL §Docusign Status]` |
| Signed EL (Mangoshare) | [app.mangoshare.com/share/37a4c07a18214ce0c5ece628](https://app.mangoshare.com/share/37a4c07a18214ce0c5ece628) | `[EL §Signed EL mangoshare]` |
| PBC folder (Imaginetime/Mango) | [app.imaginetime.com/firm/5331/workspaces/937731/files/18410815/folder](https://app.imaginetime.com/firm/5331/workspaces/937731/files/18410815/folder) | `[EL §PBC Folder Link]` |
| PBC list (SharePoint xlsx) | [SharePoint link](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDQivwbolZUQoqOV7H6oNKJAWXsAiza-E_SzdGOVvUL_x8?e=gv7DvN) | `[EL §PBC list link]` |
| PBC list sent | 2026-01-29 | `[EL §Date PBC list sent]` |
| PBC status | Received PBC items | `[EL §PBC list status]` |
| Open items email | Sent 2026-03-09 | `[EL §Ext Email Sent]` |
| Ext email sent | 2026-03-09 | `[EL §Date EXT EMAIL sent]` |
| Outlook msgs retained | `Nick_Denillo.msg` · `Denillo_-_Open_Items.msg` · `Denillo_Open_Items_-_2026_03_09.msg` | `[EL attachments]` |

### 5.2 Insights Project Artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| **Counting file** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBznu9cAoFNToOhoLKs1OquAa6wuSb31Q2Q7RwSghExSkg?e=oc59fj) | `[Insights §Counting file]` |
| **Extraction 1040** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCwk3YfGiMdSablDVmmwAPiASC5EtovqTyiXxi_SFR1Zq8?e=rpWRHj) | `[Insights §Extraction 1040]` |
| **Tax Memo** | [SharePoint docx](https://subledgesl.sharepoint.com/:w:/s/NickDenillo/IQC4pH1iP41BSpsnf3tme-cBAW5y85-fRc3yk56oYU2WaWE?e=3sFfvS) | `[TaxAscend §Tax Memo URL]` |
| **Document Inventory (Account)** | [SharePoint xlsx](https://subledgesl-my.sharepoint.com/personal/seth_accruity_com/Documents/_Client%20Intake/_Master%20Mango%20File%20Zip/NickDenillo_DocInv.xlsx) | `[Accounts §Document Inventory]` |

> **Note:** Analysis file on Insights Project is listed as "Completed" but the link was not rendered as a parsed URL in this fetch; it may require Drive-mount access to open. Flag for next refresh.

### 5.3 Compliance Project Files

| Project | Client Folder | Source |
| --- | --- | --- |
| **Denillo Heating & Cooling (1120-S)** | [SharePoint folder](https://subledgesl.sharepoint.com/:f:/s/AccruityTax/IgD0dqT58PNORr5uUDZxLIQpATAnlksTSRjIlFMakdWg-UE?e=oeuwhC) | `[OAT:1120-S §Client Folder link]` |
| **SOW (Mangoshare)** | [app.mangoshare.com/share/5704b91f36829abd1bdb4f55](https://app.mangoshare.com/share/5704b91f36829abd1bdb4f55) | `[OAT:1120-S §Link to SOW]` |

### 5.4 Files & Links Rows (3) — URL collision flag

| Row | Name | URLs populated | Flag |
| --- | --- | --- | --- |
| `33b4…ee1f` | "Engagement Letter" | all empty | — |
| `33b4…be91` | "Executive Summary" | all empty | — |
| `33b4…2291` | "Nick Denillo" | Document Inventory + PBC PDF Package | ⚠️ **Same SharePoint URLs as Spring Bengtzen & Alex Dykes — template defaults, not client-specific** |

Matching SharePoint URLs (template defaults):
- Document Inventory: `IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw` (identical to Spring + Alex Dykes)
- PBC PDF Package: `IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA` (identical to Spring + Alex Dykes)

**F&L URL collision: YES.** System-wide template-default issue confirmed on a third client. `[FL:NickDenillo]` `[FL:Spring §Document Inventory]` `[FL:AlexDykes §Document Inventory]`

### 5.5 Account-level Workbooks Not Linked

The Account's top-level `Tax Extraction`, `PBC Workbook`, and `Tax Planning Memo` fields are all empty, despite the Insights Project having a Counting File + Extraction 1040 + Tax Memo on SharePoint. Same pattern as Spring Bengtzen and Alex Dykes. `[Accounts §Tax Extraction]` `[Accounts §PBC Workbook]` `[Accounts §Tax Planning Memo]`

---

## §6. Claude Work Product

**0 prior Claude sessions** tied to Nick Denillo found in Claude Summaries DB or Claude Activity Log search. This refresh creates the first Claude Summary log row.

A search for "Nick Denillo's Tax Insights Clarification Call on Jan 22" in Client Meetings space returned a hit with `.msg` suffix — suggesting a Claude-generated email summary may have been sent internally on 2026-01-28, but this has not been logged as a formal Claude Summary DB row. `[Search:ClientMeetings]`

This refresh's Claude Summary row will be created in §11 with: Thread Title `Nick Denillo — Client Intelligence Dossier Refresh — 2026-05-07` · Topics `File Review · Notion Build · Compliance · Tax Planning` · Account relation = canonical Account.

---

## §7. Action Items — Rolled Up

### 7.1 Meeting Action Items (from 2026-01-22 Tax Insights Clarification)

| # | Action ID | Action | Assigned To | Owner | Priority | Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AI-75 | **Update tax planning memo with 2024 data and new strategies; deliver early next week** | Seth / Bryan | Accruity | 🔴 HIGH | Not started | `[MAI:AI-75]` |
| 2 | AI-76 | **Send 2025 engagement letter + PBC checklist; file S-Corp by Feb 28, 1040 2 weeks later** | Seth | Accruity | 🔴 HIGH | Not started | `[MAI:AI-76]` |
| 3 | AI-77 | Research 529 rules re: NIL pay; report back to Nick & Alexandra | Seth | Accruity | 🟡 MED | Not started | `[MAI:AI-77]` |
| 4 | AI-78 | **Set W-2s to ~$100K; monitor Q4 bonus; keep 2026 Q1 ES same; adjust Q2** (saves ~$7K/yr SE tax; $194K → $100K safe harbor) | Nick Denillo | Client | 🔴 HIGH | Not started | `[MAI:AI-78]` |
| 5 | AI-79 | Print & distribute employee W-2s; inform that W-2 is source of truth | Nick Denillo | Client | 🟡 MED | Not started | `[MAI:AI-79]` |

> **Note on AI-75 and AI-76:** Both were sourced from 2026-01-22 and show "Not started" as of the most recent pull (2026-04-01). However, the EL was in fact sent/signed by 2025-12-29 — before the meeting — suggesting AI-76 may reflect pre-meeting context (the meeting may have confirmed next steps rather than initiated them). The Tax Memo was sent 2025-12-22 (AI-75 context: "update with 2024 data" implies a second revision was requested). These items warrant status verification. `[TaxAscend §date:Tax Memo Sent]` `[EL §date:Date Signed]`

### 7.2 Compliance & Operational Actions

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 6 | **Verify AI-75 / AI-76 status** — EL already signed 12/29 and Tax Memo sent 12/22; confirm if the "Not started" status is stale data or genuinely open | Seth | 🔴 HIGH | `[MAI:AI-75]` `[MAI:AI-76]` `[EL §Date Signed]` |
| 7 | **Confirm W-2 reduction to ~$100K** (AI-78) executed for 2025 — deadline-sensitive if not yet done; saves ~$7K/yr SE tax | Seth (confirm) / Nick (action) | 🔴 HIGH | `[MAI:AI-78]` |
| 8 | **1120-S return (Denillo Heating and Cooling)**: at "L1 Revisions (External)" — confirm L1 review complete and route to L2; extended due 2026-09-15 | Deontae Lafayette | 🟡 MED | `[TCP:1120-S]` `[OAT:1120-S]` |
| 9 | **1040 return**: at "Collect and Review K-1s" stage — K-1 from 1120-S must complete before 1040 can advance; extended due 2026-10-15 | Deontae Lafayette | 🟡 MED | `[TCP:1040]` |
| 10 | **Possible follow-up meeting 2026-04-29** — Tax Ascend "Temp Filter: Piah to do - Check meeting recap 04/29" flag. Verify if meeting occurred; if so, link recap to Meetings Tracker | Generator / Piah | 🟡 MED | `[Insights §Temp Filter]` |
| 11 | **Backfill email log** — 0 threads on Account; check Make pipeline for Denillo + alexandra@denillo.com routing | Accruity ops | 🟡 MED | `[§3]` |
| 12 | **F&L URL collision** — "Nick Denillo" Files & Links row has Document Inventory + PBC PDF Package URLs identical to Spring Bengtzen & Alex Dykes. System-wide remediation needed | Accruity ops | 🟡 MED (data integrity) | `[§5.4]` |
| 13 | **Research 529 / NIL pay** (AI-77) — confirm if Seth completed or still pending | Seth | 🟡 MED | `[MAI:AI-77]` |
| 14 | **Sync Insights workbook URLs** (Extraction 1040, Tax Memo) up to Account.Tax Extraction / Tax Planning Memo top-level fields | Accruity ops | 🟢 LOW (plumbing) | `[§5.5]` |
| 15 | **Surface Partner identity** — Account `Partner` relation ID not resolved to a name this refresh | Generator | 🟢 LOW | `[Accounts §Partner]` |
| 16 | **Check SOW year-of-coverage** for 1120-S (Outsourcing tracker notes: "SOW version June 2025. No year of coverage") — confirm coverage year with Stacy | Stacy / Seth | 🟢 LOW | `[OAT:1120-S §Notes (adding year of coverage)]` |

**Total: 16 open items (4 HIGH, 7 MED, 5 LOW).**

---

## §8. Tax Strategies & Projected Savings

### 8.1 Confirmed Strategies (from Tax Insights Clarification + Tax Ascend record)

| Strategy | Detail | Status | Projected Savings | Source |
| --- | --- | --- | --- | --- |
| **S-Corp W-2 Optimization** | Reduce Nick's W-2 from ~$194K to ~$100K (safe harbor) to minimize SE tax on distributions | In flight — assigned to Nick (AI-78) | **~$7,000/yr** | `[MAI:AI-78 §Context]` |
| **Reasonable Compensation structuring** | $100K W-2 is the stated safe harbor floor; Q4 bonus monitoring + Q2 ES adjustment | Recommended · Status TBD | Included above | `[MAI:AI-78]` |
| **529 / NIL Pay analysis** | Research 529 rules related to NIL (Name, Image, Likeness) pay — implication: likely a student-athlete child or dependent receiving NIL income; 529 distributions may be affected | Research assigned to Seth (AI-77) | ? Pending research | `[MAI:AI-77]` |
| **Semi-Annual Tax Projection Analysis** | Per scope in Tax Ascend — twice-annual projections | Per engagement scope | ? Pending workbook ingestion | `[TaxAscend §STACY DESCRIPTION]` |
| **Semi-Annual Custom Tax Planning** | Per engagement scope | Per engagement scope | ? Pending workbook ingestion | `[TaxAscend §STACY DESCRIPTION]` |
| **Annual Organization Chart Refresh** | Ensures entity structure stays current | Per engagement scope | Structural benefit | `[TaxAscend §STACY DESCRIPTION]` |

### 8.2 Strategies Referenced in Tax Memo (not yet parsed)
The Tax Memo (sent 2025-12-22, URL on Tax Ascend) is the primary strategy document. Its contents are not yet parsed in this environment (SharePoint link present but workbook not ingested). Full strategy table will populate on next refresh once memo is accessible. `[TaxAscend §Tax Memo URL]`

---

## §9. Opportunity Flags (auto-detected)

### 9.1 S-Corp Classifier — TRIGGERED

**S-Corp election is ACTIVE** (Denillo Heating and Cooling — 1120-S on file, currently in compliance). The W-2 optimization AI-78 confirms this is already known and in progress. Key remaining question: was the $194K → $100K W-2 reduction executed for 2025, or is it a forward 2026 action? If 2025 is already filed/extended with the higher W-2, the savings may not materialize until 2026. `[TCP:1120-S]` `[MAI:AI-78]`

**Flag: HIGH** — W-2 reduction execution status unconfirmed. Promote to §7 #7.

### 9.2 529 / NIL Pay — NOVEL FLAG

The 529 / NIL Pay action item (AI-77) is notable: NIL income for student-athletes creates unique tax treatment questions (self-employment income, 529 qualified expenses, scholarship interaction). This is an emerging planning area. Once Seth's research completes, a planning memo update may be warranted. `[MAI:AI-77]`

**Flag: MED** — research in flight; outcome unknown.

### 9.3 Cost Seg Classifier — BLOCKED

No Property records or real estate entities surfaced in any record this refresh. Cost Seg classifier cannot run. If Denillo Heating and Cooling owns commercial/industrial real property, a Cost Seg study could be material — confirm at next refresh.

### 9.4 Entity Expansion

Scope includes "Annual Organization Chart Refresh" — implies multi-entity awareness. Only 1 entity (1120-S) confirmed to date. Confirm whether Nick has additional LLCs, holding entities, or rental properties that should appear in the org chart. `[TaxAscend §STACY DESCRIPTION]`

---

## §10. Operations Analysis

**Engagement is active but carrying stale action items.** The planning session on 2026-01-22 generated 5 action items; as of 2026-04-01 (70 days later), all 5 remain "Not started" in the tracker. This may reflect a data-entry lag rather than true inaction (the EL was signed before the meeting, the Tax Memo was sent before the meeting), but the tracker is not a reliable signal of completion without verification.

**Compliance execution is on-track:**
- 1120-S: extended to 2026-09-15 · assigned to Xpitax (offshore) · at L1 Revisions stage · Mango status "In Progress"
- 1040: extended to 2026-10-15 · at K-1 collection stage · depends on 1120-S completing first
- Both returns managed by Deontae Lafayette; Deontae is billing partner

**Sequencing risk:** The 1040 is explicitly at "Collect and Review K-1s" status, meaning it is waiting on the K-1 from Denillo Heating and Cooling. If the 1120-S is delayed (currently at L1 Revisions External), the 1040 will be correspondingly delayed. Both have ample runway (extended through Sep 15 and Oct 15 respectively), but the dependency chain should be tracked. `[TCP:1040 §Correct Status]` `[TCP:1120-S §Correct Status]`

**Communication note:** The "always use alexandra@denillo.com" flag in the EL notes is operationally important — future PBC sends, planning deliveries, and return drafts should route through Alexandra's email, not Nick's. Ensure Mango portal and Make routing reflect this. `[EL §Notes (PBC OPEN ITEMS)]`

**New client trajectory:** This is a New Client GC engagement (per Tax Ascend planning status). The engagement started Dec 2025 (Tax Memo 12/22, EL signed 12/29), with the first planning session 2026-01-22. The Tax Ascend "Insights: Delivered · Analysis: Completed" status confirms the initial analysis phase is done. The engagement is now squarely in compliance execution + follow-through on planning recommendations.

**Relationship temperature:** Healthy — client has Mango portal access, PBC items received, EL fully executed. No relationship-risk signals visible. The primary risk is the stale action items in the tracker that may give a false impression of open tasks.

---

## §11. Individual Profiles

### §11.1 Nick Denillo
- Primary contact; owner/operator of Denillo Heating and Cooling (S-Corp)
- Email: nick@denillo.com · Phone: (412) 608-4761
- Key planning action: reduce own W-2 from ~$194K to ~$100K to optimize SE tax (~$7K/yr savings) — this is a CLIENT-OWNER action item (AI-78)
- May have a child receiving NIL income (529/NIL Pay research, AI-77)
- Active on Mango portal
- No relationship-risk signals this refresh

### §11.2 Alexandra Denillo
- Spouse; co-filer on joint 1040
- Preferred tax correspondence email: **alexandra@denillo.com** (per EL notes — must use this address for all future emails)
- No separate business entity surfaced
- Not separately listed as a client contact in the Client Contacts DB (only Nick appears)

---

## §12. Provenance Index

### Notion — Account & DB rows
- `[Accounts:NickDenillo]` → [notion.so/30d49172875181a0bdc5f8f877ba040b](https://www.notion.so/30d49172875181a0bdc5f8f877ba040b)
- `[ExecSum:NickDenillo]` → [notion.so/33b49172875181b3bbaee98f710189fc](https://www.notion.so/33b49172875181b3bbaee98f710189fc) (existing — body has empty Activity Log header)
- `[EL:NickDenillo]` → [notion.so/2ef491728751808c9167cabc34e3c138](https://www.notion.so/2ef491728751808c9167cabc34e3c138) — Signed/Executed/$4,000
- `[Insights:NickDenillo]` → [notion.so/2fd49172875180d5a5bbcf96d88ada0f](https://www.notion.so/2fd49172875180d5a5bbcf96d88ada0f) — DELIVERED · Analysis Completed
- `[TaxAscend:NickDenillo]` → [notion.so/2f0491728751803cbe49f9d6cf3b3428](https://www.notion.so/2f0491728751803cbe49f9d6cf3b3428)
- `[Contact:Nick]` → [notion.so/30d4917287518112a107f3a01977384f](https://www.notion.so/30d4917287518112a107f3a01977384f) — nick@denillo.com · (412) 608-4761
- `[EmailDB:Nick]` → [notion.so/2fc49172875180dfb26ac18c4173a74f](https://www.notion.so/2fc49172875180dfb26ac18c4173a74f)

### Notion — Meeting Action Items (5)
- `[MAI:AI-75]` → [notion.so/335491728751811a8ed6ed6e8cfae1fc](https://www.notion.so/335491728751811a8ed6ed6e8cfae1fc) — Update tax planning memo with 2024 data · HIGH · Seth/Bryan
- `[MAI:AI-76]` → [notion.so/3354917287518110ad90d080806998c9](https://www.notion.so/3354917287518110ad90d080806998c9) — Send 2025 EL + PBC checklist · HIGH · Seth
- `[MAI:AI-77]` → [notion.so/33549172875181cb8ff7ebf7834846ba](https://www.notion.so/33549172875181cb8ff7ebf7834846ba) — Research 529 / NIL pay · Normal · Seth
- `[MAI:AI-78]` → [notion.so/33549172875181d8bd8be7506f7240ad](https://www.notion.so/33549172875181d8bd8be7506f7240ad) — Set W-2 to ~$100K · HIGH · Nick Denillo · ~$7K/yr SE tax savings
- `[MAI:AI-79]` → [notion.so/3354917287518167a9a7d839e4f3116c](https://www.notion.so/3354917287518167a9a7d839e4f3116c) — Print/distribute employee W-2s · Normal · Nick Denillo

### Notion — Meetings Tracker (1)
- `[Meeting 2026-01-22]` → [notion.so/2fb4917287518057bb32c91c61215b82](https://www.notion.so/2fb4917287518057bb32c91c61215b82) — Tax Insights Clarification · Fellow recap linked

### Notion — Files & Links (3)
- `[FL:NickDenillo EL]` → [notion.so/33b491728751814da1add1e191b9ee1f](https://www.notion.so/33b491728751814da1add1e191b9ee1f) (empty)
- `[FL:NickDenillo ExecSum]` → [notion.so/33b49172875181daa723ca005dcfbe91](https://www.notion.so/33b49172875181daa723ca005dcfbe91) (empty)
- `[FL:NickDenillo]` → [notion.so/33b49172875181cfbcd7e9f77d532291](https://www.notion.so/33b49172875181cfbcd7e9f77d532291) (Document Inventory + PBC PDF Package — template URL collision)

### Notion — Tax Compliance Projects (2)
- `[TCP:1040]` → [notion.so/d2a49172875182d2b90a01d124aa2484](https://www.notion.so/d2a49172875182d2b90a01d124aa2484) — 1040 Nick & Alexandra Denillo · Stage: K-1 collection · Due 2026-10-15
- `[TCP:1120-S]` → [notion.so/4f74917287518222bab101e74d55e419](https://www.notion.so/4f74917287518222bab101e74d55e419) — 1120-S Denillo Heating and Cooling · Stage: L1 Revisions · Due 2026-09-15

### Notion — Outsourcing Assignment Tracker
- `[OAT:1120-S]` → [notion.so/30c49172875180c280b5e5bf6ef5d590](https://www.notion.so/30c49172875180c280b5e5bf6ef5d590) — Xpitax · Sent for L1 Review · Assigned 2026-02-13

### SharePoint / Drive
- Signed EL (Mangoshare): [app.mangoshare.com/share/37a4c07a18214ce0c5ece628](https://app.mangoshare.com/share/37a4c07a18214ce0c5ece628)
- PBC folder (Imaginetime): [app.imaginetime.com/firm/5331/workspaces/937731/files/18410815/folder](https://app.imaginetime.com/firm/5331/workspaces/937731/files/18410815/folder)
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQDQivwbolZUQoqOV7H6oNKJAWXsAiza-E_SzdGOVvUL_x8?e=gv7DvN)
- Counting file (Insights): [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBznu9cAoFNToOhoLKs1OquAa6wuSb31Q2Q7RwSghExSkg?e=oc59fj)
- Extraction 1040: [SharePoint xlsx](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQCwk3YfGiMdSablDVmmwAPiASC5EtovqTyiXxi_SFR1Zq8?e=rpWRHj)
- Tax Memo (SharePoint NickDenillo site): [SharePoint docx](https://subledgesl.sharepoint.com/:w:/s/NickDenillo/IQC4pH1iP41BSpsnf3tme-cBAW5y85-fRc3yk56oYU2WaWE?e=3sFfvS)
- Document Inventory (Account): [SharePoint xlsx](https://subledgesl-my.sharepoint.com/personal/seth_accruity_com/Documents/_Client%20Intake/_Master%20Mango%20File%20Zip/NickDenillo_DocInv.xlsx)
- Denillo H&C client folder (AccruityTax site): [SharePoint folder](https://subledgesl.sharepoint.com/:f:/s/AccruityTax/IgD0dqT58PNORr5uUDZxLIQpATAnlksTSRjIlFMakdWg-UE?e=oeuwhC)
- SOW (Mangoshare): [app.mangoshare.com/share/5704b91f36829abd1bdb4f55](https://app.mangoshare.com/share/5704b91f36829abd1bdb4f55)

### Cross-dossier references
- `[FL:Spring §Document Inventory]` → template-default URL collision flag (Spring Bengtzen reference)
- `[FL:AlexDykes §Document Inventory]` → second instance of same collision

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.**

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- Joint Accruity household (Nick & Alexandra Denillo) — New Client GC enrollment Dec 2025
- Engagement fee $4,000 · EL Signed/Executed · Deposit Paid · Mango portal accessed · PBC items received
- **Denillo Heating and Cooling — S-Corp (1120-S) confirmed** — currently at L1 Revisions with Xpitax offshore; extended to 2026-09-15
- **1040 — at K-1 collection stage**, dependent on 1120-S; extended to 2026-10-15; Deontae Lafayette managing
- Tax Insights delivered; Analysis completed; Tax Memo sent 2025-12-22 (NickDenillo SharePoint site)
- 5 Meeting Action Items from 2026-01-22 Clarification Call — all "Not started" in tracker

**New — key planning items:**
- **S-Corp W-2 optimization** (AI-78): ~$194K → ~$100K safe harbor = **~$7K/yr SE tax savings** — HIGH priority, assigned to Nick
- **529 / NIL Pay research** (AI-77): novel planning area — likely NIL income for student-athlete dependent
- Updated Tax Planning Memo with 2024 data requested (AI-75)

**New — discoveries / flags:**
- ⚠️ **F&L URL collision** confirmed on Nick Denillo (third instance) — Document Inventory + PBC PDF Package in "Nick Denillo" F&L row are identical to Spring Bengtzen + Alex Dykes template defaults
- 0 email threads on Account (plumbing gap)
- Possible unlogged meeting ~2026-04-29 (Tax Ascend Temp Filter note)
- SOW for 1120-S has no year-of-coverage (outsourcing tracker note)
- AI-75 and AI-76 "Not started" status may be stale — EL and Tax Memo were already sent before the meeting; verify

**Auto-detected flags:**
- 🔴 HIGH: S-Corp W-2 optimization execution unconfirmed
- 🟡 MED: 529/NIL Pay research pending
- Cost Seg: blocked (no property records)

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 16 | Open action items (4 HIGH, 7 MED, 5 LOW) | §7 |
| 1 | Meetings on file | §4 |
| 2 | Active compliance returns (1040 + 1120-S, both extended) | §5.3 |
| 5 | Meeting action items from Jan 22 (all Not started in tracker) | §7.1 |
| 1 | System-wide F&L URL collision (third confirmed instance) | §5.4 |
| 0 | Email threads on Account | §3 |
| 1 | HIGH opportunity flag: S-Corp W-2 optimization | §9.1 |
| 1 | MED opportunity flag: 529/NIL Pay research | §9.2 |

### 13.3 What a reader should look at first

1. **§7.1 AI-78** — W-2 reduction to ~$100K: was this actually executed for 2025? If not, it's a deadline-sensitive HIGH-priority item with quantified savings (~$7K/yr). Confirm with Nick.
2. **§4 Cadence** — only 1 meeting on record; Tax Ascend hints at a 2026-04-29 meeting not yet linked. Check and backfill.
3. **§10 K-1 dependency** — 1040 cannot advance until 1120-S K-1 is issued; 1120-S is at L1 Revisions. Track the handoff.
4. **§3 Alexandra email** — ensure alexandra@denillo.com is the routed address for all future correspondence.

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/NickDenillo/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: MEDIUM (1 meeting, 5 MAIs, 2 active returns, Tax Memo delivered; no email log) · Next refresh: trigger on W-2 confirmation, K-1 issuance, or next planning session*
