# Don & Christina Fowler — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Don & Christina Fowler |
| Client # | **04140618-01** (canonical) |
| Mango Client ID | **937686** (on EL tracker + outsourcing row) |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Depth mode | **FULL** — two detailed tax planning meeting transcripts with full action-item lists, Insights project delivered, EL Signed/Executed, active compliance outsourcing, multiple entities, rich Tax Ascend record |
| Engagement Stage | Tax Ascend — Tax Planning + Tax Compliance (Signed 2025-11-22); 2024 Compliance **In Progress**, Planning delivered; Insights **DELIVERED** 2025-10-16 |
| Engagement Fee | **$1,800** (Plan + Compliance) |
| Temperature | Active & complex — tax planning delivered, compliance in progress with K-1 delays, multiple entities being stood up, cost seg in pipeline |
| Relationship Manager | Seth Johnson (Partner, seth@accruity.com) |
| Primary Contact | Don Fowler · dfowler@realeflow.com · (954) 554-9134 |
| Data Sources (this refresh) | Notion Accounts record (canonical `30b4…0108`) · Engagement Letter (Signed/Executed) · Insights Project (DELIVERED) · Tax Ascend record · 3 Meetings Tracker rows (canonical account) + 1 (to-delete account) · Tax Planning Session record + 2 sub-pages with full meeting transcripts · Files & Links (3 rows) · Reporting Entity (Don Fowler, 1040, Construction) · Tax Engagements (2 rows: Planning 2024, Compliance 2024) · Outsourcing Assignment Tracker · Tax Compliance Projects tracker · Client Contact record · Executive Summaries DB row (existing, unpopulated) |
| Files NOT Accessible This Refresh | PBC Workbook, Tax Extraction, Tax Planning Memo (not linked on canonical Account record top-level fields); Analysis File and Extraction File on Tax Ascend record are omitted |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

---

## §1. Executive Overview

Don & Christina Fowler are an **active Accruity Tax Ascend (Plan + Compliance)** household in the Construction / real estate investment space. The engagement is **complex and multi-entity**: Don holds an existing W-2 job at **Real Flow** (CRE investment platform), runs **Waterside Advisors** (S Corp, active Oct/Nov 2025), owns **Tax Professionals LLC** ($6,000/month royalty income), has paying **children on payroll** (two kids at $15K before March 2026 cycle, W-2 at $14,600), and is actively planning a **short-term rental acquisition** in 2025/2026 that will trigger a cost segregation study. `[Tax Planning Session MEETING 1]` `[Tax Planning Session MEETING 2]`

**Tax Ascend status (as of refresh):** Planning delivered (Tax Memo SENT 2025-12-22); Compliance is Open Items List — email sent; Insights delivered 2025-10-16. `[Tax Ascend:Don Fowler]` EL Signed/Executed, Deposit Paid, PBC items received, Mango portal Customer Accessed. `[EL:Don & Christina Fowler]`

**2025 compliance is in progress** with known blockers: Seven Diamonds and Real Flow K-1s not expected until August 2025 minimum. Seth's plan is to send the return to preparers (Unison Globus — outsourcing assignment dated 2026-04-23) with K-1 placeholders and finalize once received. The outsourcing row shows **Missing Information** status as of 2026-05-05 with a note from the offshore preparer requesting 2024 tax return copies. Current status: `03 Collect and Review K-1s`. Extension filed. `[TaxCompliance:1040 Don Fowler]` `[Outsourcing:1040 Don Fowler]`

**Key strategic levers in-flight:**
1. **Kids' payroll** via Waterside Re LLC (new entity to be established) to shift wages off personal return
2. **Solo/self-directed 401(k)** for Waterside Advisors S Corp — not yet set up
3. **Augusta Rule** rental income deduction (~$2,500–$3,000) — to be included in 2025 draft return
4. **Cost segregation study** — triggered when short-term rental property purchase closes (FL/GA/SC/NC, ~2025/2026)
5. **QuickBooks setup** via Accruity back office for Waterside books; historical transactions to be imported
6. **Accountable plan** for Waterside business expenses once QBO running

**Duplicate Account flag.** A second Account row `30d49172875181a3af5ad2fb9bd8f656` (Client #04140618-02, To Delete: YES) exists and is marked for deletion. The EL, Files & Links rows, Tax Ascend, Tax Planning Session, and the fourth meeting row are all linked to the to-delete Account. The canonical Account (`30b4917287518140a497eadeb0956108`) holds the Exec Summary row, Insights project, and 3 of the 4 Meetings Tracker rows. This is an important data-integrity flag — promoted to §7. `[Accounts:DonFowler-canonical]` `[Accounts:DonFowler-todelete]`

---

## §2. Client Profile

| Item | Value | Confidence | Source |
| --- | --- | --- | --- |
| Account name (canonical) | Don Fowler | ✓ | `[Accounts:DonFowler-canonical]` |
| Account name (to-delete) | Don Fowler | ✓ | `[Accounts:DonFowler-todelete]` |
| Client # (canonical) | 04140618-01 | ✓ | `[Accounts:DonFowler-canonical]` |
| Client # (to-delete) | 04140618-02 · **To Delete: YES** | ✓ | `[Accounts:DonFowler-todelete]` |
| Mango Client ID | 937686 | ✓ | `[EL:Don & Christina Fowler]` |
| Primary email | dfowler@realeflow.com | ✓ | `[Contact:Don Fowler]` |
| Primary phone | (954) 554-9134 | ✓ | `[Contact:Don Fowler]` |
| Spouse / co-filer | Christina Fowler (co-signatory on EL) | ✓ | `[EL:Don & Christina Fowler §CLIENT]` |
| Filing status | MFJ (implied by "Don & Christina" joint EL) | ~ | derived |
| Relationship manager | Seth Johnson (Partner) | ✓ | `[Accounts:DonFowler-canonical §Partner]` |
| Engagement | Tax Ascend — Tax Planning + Tax Compliance | ✓ | `[Tax Ascend:Don Fowler §TAX ASCEND TYPE]` |
| EL status | **Signed · Executed** | ✓ | `[EL §Compliance Group Status]` |
| Deposit | Paid | ✓ | `[EL §Deposit Paid]` |
| Engagement fee | **$1,800** (Plan + Compliance) | ✓ | `[EL §Price]` `[EL §SCOPE]` |
| Mango portal | Customer Accessed ✓ | ✓ | `[EL §Mango Portal Invite]` |
| PBC items | Received | ✓ | `[EL §PBC list status]` |
| Tax Ascend signed | 2025-11-22 | ✓ | `[Tax Ascend §date:Date Signed]` |
| Tax memo sent | 2025-12-22 | ✓ | `[Tax Ascend §date:Tax Memo Sent]` |
| Outsourcing assignee | Unison Globus | ✓ | `[Outsourcing §Assigned to]` |
| Compliance manager | Deontae Lafayette | ✓ | `[TaxCompliance §Manager]` |
| Compliance preparer | Deontae Lafayette | ✓ | `[TaxCompliance §Preparer]` |
| Extension filed | Yes | ✓ | `[TaxCompliance §Extension Filed]` |
| Extended due date | 2026-10-15 | ✓ | `[TaxCompliance §date:Extended Due]` |
| Industry | Construction | ✓ | `[RE:Don Fowler §Industry]` |
| Entity type | 1040 | ✓ | `[RE:Don Fowler §Entity Type]` |

### Principals at a glance

- **Don Fowler** — primary; W-2 earner at Real Flow (CRE investment platform); S Corp owner (Waterside Advisors); co-owner Tax Professionals LLC; pays children on payroll; planning STR purchase; actively engaged in tax strategy
- **Christina Fowler** — co-filer; attended Meeting 1 to take notes ("not tech-savvy" per transcript); on EL as co-signatory

### Entity Stack

| Entity | Type | Role | Status | Source |
| --- | --- | --- | --- | --- |
| Don & Christina Fowler (1040) | Personal return | Primary filing unit | In Progress / K-1 delays | `[TaxCompliance]` |
| **Waterside Advisors** | S Corp | Active income, expenses, retirement plan, kids' payroll (via new entity) | Active since Oct/Nov 2025 | `[Tax Planning MEETING 2]` |
| **Waterside Re LLC** | LLC (new) | Short-term rental holdco + kids' payroll entity | To be established | `[Tax Planning MEETING 1]` |
| **Tax Professionals LLC** | LLC | Royalty income: $6,000/mo; separate bank account | Active | `[Tax Planning MEETING 2]` |
| **Real Flow** | Employer | Don's W-2 employer; K-1 also via investment interest | Active (K-1 pending) | `[Tax Planning MEETING 1]` `[Tax Planning MEETING 2]` |
| **Seven Diamonds** | Investment | K-1 issuer; won't be available until August | Active | `[Tax Planning MEETING 2]` |

---

## §3. Email Intelligence

**0 email threads on canonical Account.** The Client Email Log query returned no results for "Fowler." The EL tracker row carries three Outlook attachment files (`Don_Fowler.msg` ×2, `Open_Items.msg`), but none are synthesized as standalone email threads in the Email Log DB. `[EL §Ext Email Sent]` `[EL §Outlook Email Msg]` `[EL §Open Items Email]`

**What the EL email attachments tell us:**
- `Don_Fowler.msg` (appears twice, likely EL delivery + follow-up)
- `Open_Items.msg` — open items list sent
- Open items email status: **Sent** · PBC list email: **Sent** (dated 2026-03-09) · Extension email sent 2026-03-09

**Plumbing gap** → §7 Action: backfill via Outlook scan against `dfowler@realeflow.com` and `christina` / `Fowler` patterns; confirm Make scenario is routing to Client Email Log. Currently 0 email threads captured from this high-activity planning engagement.

---

## §4. Meeting History

**4 meetings on file across canonical + to-delete accounts.** Full transcript content retrieved from Tax Planning Session sub-pages. Append-only on next refresh.

| # | Date | Type | Account | Time (EST) | Status | Recap | Key Content | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **2025-10-16** | Full Insights — Delivery call | canonical | 12:00–1:00 PM | Done ✓ | [Fathom](https://fathom.video/share/kqPvzuPym-vMA7pWxjPyBTizVys9qPv7) | Insights delivery; Analysis "Waiting on Extraction" per Insights Project record | `[Meeting 2025-10-16 Insights Delivery]` |
| 2 | **2026-01-07** | Tax Planning Session | canonical | 11:00–11:30 AM | **Rescheduled** | LINK (not functional) | Rescheduled per status; no recap | `[Meeting 2026-01-07 Rescheduled]` |
| 3 | **2026-01-15** | Tax Planning Session | canonical | 12:30–1:00 PM | Done ✓ | [Otter.ai](https://otter.ai/u/IEZfLwzVM4ID3M4vQd51drhKKqI?utm_source=copy_url) | Full strategic session — Waterside Re, kids' payroll, 401(k), Augusta Rule, estimated $135K 2025 tax liability, STR purchase plan (see §4.1) | `[Meeting 2026-01-15 Tax Planning 1]` `[Tax Planning MEETING 1]` |
| 4 | **2026-03-26** | Tax Planning Session | to-delete acct | 2:00–2:30 PM | Done ✓ | [Fireflies](https://app.fireflies.ai/view/seth-johnson-and-Don-Fowler::01KMGZKY0Q2A6MTA0YMEY5VKWX) | Filing timeline, K-1 delays, QuickBooks setup, entity details, April 15 payment estimate, cost seg trigger (see §4.2) | `[Meeting 2026-03-26 Tax Planning 2]` `[Tax Planning MEETING 2]` |

**Restricted flag:** 0/4 meetings restricted.

### §4.1 Meeting Detail — 2026-01-15 Tax Planning Session (Full Synthesis)

Seth Johnson and Don Fowler (+ Christina taking notes) covered:
- **2025 estimated tax liability: ~$135,000** total (W-2 + entity income + investment K-1s) `[Tax Planning MEETING 1 §Tax Planning and Estimates for 2025]`
- **Kids' payroll strategy**: Don has kids under 14; current platform (Gusto) had issues; Seth recommended QuickBooks payroll or manual payroll; entity structure — new Waterside Re LLC to be set up specifically for child payroll to avoid employee-tax complications `[Tax Planning MEETING 1 §Payroll Platforms]`
- **Self-directed 401(k)**: Don has a company 401(k) but NOT a solo/self-directed one; Seth explained solo 401(k) benefits; Waterside Advisors S Corp to host the plan `[Tax Planning MEETING 1 §Retirement Plans]`
- **Augusta Rule**: Seth to assemble rental documentation and preliminary valuation (placeholder average daily rate); paperwork to be sent to Don for review `[Tax Planning MEETING 1 §Action Items]`
- **Client portal (Mango)**: to be live within 3 weeks of meeting date (i.e., ~Feb 5, 2026); PBC items to be managed through portal `[Tax Planning MEETING 1 §Client Portal]`
- **STR property purchase**: Don plans to purchase ~$1M property in 2026; Seth flagged cost seg study via affiliated engineering firm as a major 2026 tax tool `[Tax Planning MEETING 1 §Finalizing Tax Planning]`

**Action Items from MEETING 1** (10 items):

| # | Item | Owner | Source |
| --- | --- | --- | --- |
| M1-1 | Set up Waterside Re LLC + open bank account (for property + kids' payroll) | Don | `[MEETING 1]` |
| M1-2 | Provide Real Flow K-1 timing/status and any outstanding K-1 info | Don | `[MEETING 1]` |
| M1-3 | Research payroll providers (QBO, manual) for minors; recommend | Seth | `[MEETING 1]` |
| M1-4 | Investigate QBO payroll setup; evaluate manual payroll; provide recommendation | Seth | `[MEETING 1]` |
| M1-5 | Set up solo/self-directed 401(k) for Waterside Advisors S Corp | Seth | `[MEETING 1]` |
| M1-6 | Get Mango portal live; onboard clients; collect docs (target ~3 weeks) | Seth | `[MEETING 1]` |
| M1-7 | Prepare ES payment analysis for 2026 (project actuals, advise on Q1 before 4/15) | Seth | `[MEETING 1]` |
| M1-8 | Prepare + send meeting recap, doc request list; schedule follow-up end of March | Seth | `[MEETING 1]` |
| M1-9 | Assemble Augusta Rule rental documentation + preliminary valuation | Seth | `[MEETING 1]` |
| M1-10 | Run tax savings analysis / entity structure map (payroll-tax savings, kids in S Corp) | Seth | `[MEETING 1]` |

### §4.2 Meeting Detail — 2026-03-26 Tax Planning Session (Full Synthesis)

Context: 2025 return prep, 2026 Q1 ES payment, entity / QBO setup.

Key topics:
- **K-1 delays**: Seven Diamonds + Real Flow K-1s not available until August; plan = send to Deontae with placeholders now, finalize on receipt `[MEETING 2]`
- **April 15 payment estimate**: Seth to run before 4/15 to check underpayment; Q1 2026 ES = safe harbor based on 2025 actuals; Q2 adjusted after STR purchase confirmed `[MEETING 2]`
- **QuickBooks for Waterside**: active since Oct/Nov 2025; Don has expense spreadsheet; Seth to set up QBO via Accruity back office + send affiliate link; Don to import historical; Seth uses Claude Code + MCP to auto-code bank statements `[MEETING 2]`
- **Multiple entities**: Waterside (S Corp, main active); Tax Professionals LLC ($6K/mo royalty, separate bank account); separate QBO classes for each `[MEETING 2]`
- **Kids' W-2s**: Two kids paid $15K before March 15; W-2 issued at $14,600 (may need to amend); third kid's payment as 12/31 accrual on books `[MEETING 2]`
- **Augusta Rule**: Seth to estimate ~$2,500–$3,000 deduction; include in draft with assumptions listed `[MEETING 2]`
- **STR property**: FL/GA/SC/NC; likely 2025/2026; Seth to initiate cost seg study immediately on purchase via affiliated engineering firm `[MEETING 2]`
- **Accountable plan**: after QBO is running, Seth to walk through business expenses + route through S Corp `[MEETING 2]`
- **Next touchpoint**: Q2 tax planning meeting planned for May 2026 `[MEETING 2]`

**Action Items from MEETING 2** (11 items):

| # | Item | Owner | Source |
| --- | --- | --- | --- |
| M2-1 | Send Waterside bank statements + 2025 expense spreadsheet to Seth | Don | `[MEETING 2]` |
| M2-2 | Send Tax Professionals LLC bank statements to Seth | Don | `[MEETING 2]` |
| M2-3 | Contact Real Flow CFO for estimated 2025 K-1 (already emailed per call) | Don | `[MEETING 2]` |
| M2-4 | Set up QBO via Accruity back office; send Don the affiliate/setup link | Seth | `[MEETING 2]` |
| M2-5 | Run April 15 payment estimate once financials received | Seth | `[MEETING 2]` |
| M2-6 | Prepare 2025 draft return with K-1 placeholders; send to preparers | Seth | `[MEETING 2]` |
| M2-7 | Calculate Augusta Rule deduction (~$2,500–$3,000); include in draft | Seth | `[MEETING 2]` |
| M2-8 | Verify/amend W-2 for kids' wages ($14,600 vs. $15,000) | Seth | `[MEETING 2]` |
| M2-9 | Notify Seth when STR property purchase is finalized | Don | `[MEETING 2]` |
| M2-10 | Initiate cost seg study via affiliated engineering firm upon STR purchase | Seth | `[MEETING 2]` |
| M2-11 | Schedule Q2 tax planning meeting (May 2026) | Both | `[MEETING 2]` |

---

## §5. Document Inventory

### 5.1 Engagement Letter

| Field | Value | Source |
| --- | --- | --- |
| EL title | Don & Christina Fowler | `[EL:Don & Christina Fowler]` |
| Status | **Signed · Executed** | `[EL §Engagement Letter Status]` `[EL §Compliance Group Status]` |
| Scope | **PLAN + COMPLIANCE** | `[EL §SCOPE]` |
| Price | **$1,800** | `[EL §Price]` |
| Deposit | Paid | `[EL §Deposit Paid]` |
| Docusign | Done (Delivered → Done) | `[EL §Docusign Status]` |
| Batch added | 2026-01-26 | `[EL §date:Batch Added]` |
| PBC list sent | 2026-03-09 | `[EL §date:Date PBC list sent]` |
| PBC email status | Sent | `[EL §PBC list Email]` |
| PBC items received | Yes | `[EL §PBC list status]` |
| Extension email sent | 2026-03-09 | `[EL §date:Date EXT EMAIL sent]` |
| Signed EL (Mangoshare) | [app.mangoshare.com/share/d026ad8a55748cf22d1ee3d2](https://app.mangoshare.com/share/d026ad8a55748cf22d1ee3d2) | `[EL §Signed EL mangoshare]` |
| PBC folder (Mango portal) | [app.imaginetime.com/firm/5331/workspaces/937686/files/18417535/folder](https://app.imaginetime.com/firm/5331/workspaces/937686/files/18417535/folder) | `[EL §PBC Folder Link]` |
| PBC list xlsx | [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBPl7S1t-P_QIsMHwgtMQZrAWBPESYRTymjQ1LG5z83SmM?e=YzcDVY) | `[EL §PBC list link]` |
| Mango portal | Customer Accessed | `[EL §Mango Portal Invite]` |
| Accelo status | NOT IN ACCELO (per EL TEMP FILTER note) | `[EL §TEMP FILTER]` |

### 5.2 Insights Project (delivered 2025-10-16)

| Field | Value | Source |
| --- | --- | --- |
| Status | **DELIVERED** (Precheck: DELIVERED) | `[Insights:Don Fowler §Status (Precheck)]` |
| Date delivered | 2025-10-16 | `[Insights:Don Fowler §date:Date delivered]` |
| Delivery call | [Fathom](https://fathom.video/share/kqPvzuPym-vMA7pWxjPyBTizVys9qPv7) | `[Insights §Meeting link]` |
| Analysis status | **Waiting on Extraction** | `[Insights §Analysis]` |
| Next scheduled | Delivery Call | `[Insights §Next Scheduled Call]` |
| SOW notes | "Piah to do - extraction and analysis 04/29" (as of 04/29 temp filter) | `[Insights §Temp Filter]` |
| Stacy description | "Semi-Annual Year-end Tax Projection Analysis, Semi-Annual Custom Tax Planning, Annual Organization Chart Refresh, Tax Preparation (business & personal)" | `[Tax Ascend §STACY DESCRIPTION]` |

**Gap:** Analysis Workbook and Extraction File are referenced on the Tax Ascend record but marked `<omitted>` — not accessible this refresh. `[Tax Ascend §Analysis File]` `[Tax Ascend §Extraction File]`

### 5.3 Tax Planning Session Artifacts

| Artifact | Link | Source |
| --- | --- | --- |
| Tax Planning Session record | [notion.so/2ea49172875181f9](https://www.notion.so/2ea49172875181f99864ee2ef50f64b1) | `[TaxPlanSession:Don Fowler]` |
| Tax Memo (SharePoint) | [SharePoint .docx](https://subledgesl.sharepoint.com/:w:/s/Insights/IQDFbj68DxnVQJv85faUFKTMAdf3ns1-eIl_8soapsExFCQ?e=J7hTqE) | `[Tax Ascend §Tax Memo URL]` |
| Meeting 1 recap (Otter.ai) | [Otter.ai](https://otter.ai/u/IEZfLwzVM4ID3M4vQd51drhKKqI?utm_source=copy_url) | `[Tax Planning MEETING 1]` |
| Meeting 1 recap (Fireflies) | [Fireflies](https://app.fireflies.ai/view/seth-johnson-and-Don-Fowler::01KMGZKY0Q2A6MTA0YMEY5VKWX) | `[TaxPlanSession §Meeting 1 Link]` |
| Meeting 2 recap (Fireflies) | [Fireflies](https://app.fireflies.ai/view/seth-johnson-and-Don-Fowler::01KMGZKY0Q2A6MTA0YMEY5VKWX) | `[Tax Planning MEETING 2]` |

### 5.4 Tax Engagements (2)

| Name | Type | Year | Phase | Status | Source |
| --- | --- | --- | --- | --- | --- |
| Don Fowler - Planning - 2024 | Planning | 2024 | Phase 1 | Not Started | `[TaxEng:Planning 2024]` |
| Don Fowler - Compliance - 2024 | Compliance | 2024 | Phase 1 | **In Progress** | `[TaxEng:Compliance 2024]` |

> Note: "Report Year: 2024" on both Tax Engagement records but the active work in transcripts and compliance tracker is for the 2025 tax year. The Tax Engagements DB uses "2024" for the filing cycle; the actual return being prepared is Form 1040 for tax year 2025. Confirm whether "Report Year" convention is calendar year of data or calendar year of filing.

### 5.5 Files & Links Rows (3) — with data-integrity flags

All three Files & Links rows are linked to the **to-delete Account** (`30d49172875181a3af5ad2fb9bd8f656`), not the canonical account. This is a data-integrity gap.

| Row | Name | URLs | Flag |
| --- | --- | --- | --- |
| `33b4…b3ac` | Engagement Letter | all empty | — |
| `33b4…25c1` | Executive Summary | all empty | — |
| `33b4…0d6` | Don Fowler | Document Inventory + PBC PDF Package | ⚠️ **Same URLs as Spring Bengtzen** (template default) |

The matching SharePoint URLs:
- Document Inventory: `IgCqkxeMjXQoTZO-AkTP6NpEARi_eOyGo1CIpZYMo-RRlnw` ← **identical to Spring Bengtzen and Alex Dykes**
- PBC PDF Package: `IgDL0pq68xE1RK_ZTOeU2SehAVXsUACBFadilTO5RsW-5YA` ← **identical to Spring Bengtzen and Alex Dykes**

**System-wide template-default flag confirmed again** — third occurrence (Spring, Alex Dykes, now Don Fowler). `[FL:Don Fowler §Document Inventory]`

### 5.6 Outsourcing Assignment

| Field | Value | Source |
| --- | --- | --- |
| Assignee | Unison Globus | `[Outsourcing:1040 Don Fowler §Assigned to]` |
| Assigned date | 2026-04-23 | `[Outsourcing §date:Assigned Date]` |
| Status (offshore) | **Assigned + Missing information** | `[Outsourcing §Status (Offshore)]` |
| Status (Accruity) | Not Yet received | `[Outsourcing §Status (accruity)]` |
| Open issue | Offshore preparer awaiting 2024 tax return copies + CCH access | `[Outsourcing §Offshore Quick Notes]` |
| Client folder (SharePoint) | [Don Fowler folder](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgC1e89ZgpHURLOm4qh4E8WRAS2iP1ln6bWkEs-bpE6T_mg?e=6EugZ0) | `[Outsourcing §Client Folder link]` |
| Mango SOW | [app.mangoshare.com/share/49c46cd9dcc2e9d0c2b1aae6](https://app.mangoshare.com/share/49c46cd9dcc2e9d0c2b1aae6) | `[Outsourcing §Link to SOW]` |
| MangoShare PBC | [app.mangoshare.com/share/27340432b3c32c15108513f4](https://app.mangoshare.com/share/27340432b3c32c15108513f4) | `[Outsourcing §MangoShare PBC link]` |

---

## §6. Claude Work Product

**0 prior Claude Summary sessions** tied to Don Fowler found in the Claude Summaries DB or Claude Activity Log. This refresh creates the first Claude Summary log row.

The Tax Planning Session MEETING 2 notes reference Seth using **Claude Code + MCP to auto-code bank statements into QuickBooks** — confirming Seth actively uses Accruity's AI tooling on this client's bookkeeping workflow. `[Tax Planning MEETING 2 §QuickBooks/Bookkeeping]`

This refresh (2026-05-07) creates the first Claude Summary on the Don Fowler account. Pre-stage for Notion write (Step 8 of pipeline).

---

## §7. Action Items — Rolled Up

Sourced from: §4 meeting transcripts (MEETING 1 + MEETING 2), compliance tracker status, outsourcing tracker, plumbing gaps.

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **Provide 2024 tax return copies to Unison Globus** — offshore preparer is blocked on "Missing information" (needs prior-year return + CCH access) | Accruity ops (Stacy/Deontae) | 🔴 HIGH (compliance gating) | `[Outsourcing §Offshore Quick Notes]` |
| 2 | **Provide CCH access to Unison Globus preparer** — explicitly noted in offshore notes | Accruity ops | 🔴 HIGH (compliance gating) | `[Outsourcing §Offshore Quick Notes]` |
| 3 | **Receive Seven Diamonds K-1** — not expected until August; plan is to file return with placeholder and amend/finalize on receipt | Don / Seth | 🔴 HIGH (compliance gating) | `[MEETING 2]` `[TaxCompliance §Correct Status]` |
| 4 | **Receive Real Flow K-1** — similarly delayed; Don already emailed CFO per 2026-03-26 session | Don | 🔴 HIGH (compliance gating) | `[MEETING 2]` |
| 5 | **Run April 15 estimated tax payment analysis for 2025** (now overdue — meeting said "before 4/15"; current date 2026-05-07) — confirm whether paid and amount | Seth | 🔴 HIGH (tax liability) | `[MEETING 2 §April 15 Payment]` |
| 6 | **Set up QuickBooks for Waterside via Accruity back office** — send Don affiliate/setup link; Don to import Oct/Nov 2025 → present transactions | Seth | 🟡 MED | `[MEETING 2 §QuickBooks]` |
| 7 | **Send Waterside bank statements + 2025 expense spreadsheet** to Seth | Don | 🟡 MED | `[MEETING 2 §Action 1]` |
| 8 | **Send Tax Professionals LLC bank statements** to Seth | Don | 🟡 MED | `[MEETING 2 §Action 2]` |
| 9 | **Establish Waterside Re LLC** + open bank account (child payroll + STR holdco) | Don | 🟡 MED | `[MEETING 1 §Action M1-1]` |
| 10 | **Set up solo/self-directed 401(k) for Waterside Advisors S Corp** | Seth | 🟡 MED | `[MEETING 1 §Action M1-5]` |
| 11 | **Verify / amend kids' W-2** ($14,600 issued; $15,000 paid; third kid accrual at 12/31) | Seth | 🟡 MED | `[MEETING 2 §Action 8]` |
| 12 | **Prepare 2025 draft return** with K-1 placeholders; send to Deontae for prep | Seth | 🟡 MED | `[MEETING 2 §Action 6]` |
| 13 | **Calculate + include Augusta Rule deduction** (~$2,500–$3,000) in draft return with assumptions | Seth | 🟡 MED | `[MEETING 2 §Action 7]` |
| 14 | **Schedule Q2 tax planning meeting** (May 2026 — planned per MEETING 2; confirm whether scheduled) | Seth + Don | 🟡 MED | `[MEETING 2 §Next Touchpoint]` |
| 15 | **Notify Seth immediately when STR property purchase closes** (FL/GA/SC/NC, ~$1M) | Don | 🟡 MED (triggers cost seg) | `[MEETING 1]` `[MEETING 2]` |
| 16 | **Initiate cost segregation study** via affiliated engineering firm once STR purchase confirmed | Seth | 🟡 MED (opportunity) | `[MEETING 2 §Action 10]` |
| 17 | **Resolve duplicate Account rows** — canonical `30b4…0108` vs. to-delete `30d4…f656` (marked To Delete but EL, Files & Links, Tax Ascend, Tax Planning Session all still linked to to-delete row) | Accruity ops | 🟡 MED (data integrity) | `[Accounts:DonFowler-todelete §To Delete]` |
| 18 | **Re-link EL + Files & Links + Tax Ascend + Tax Planning Session to canonical Account** (or confirm migration complete before deleting to-delete row) | Accruity ops | 🟡 MED (data integrity) | `[§2]` `[§5]` |
| 19 | **Research + set up payroll platform for children** (QBO payroll or manual payroll under Waterside Re LLC) | Seth | 🟡 MED | `[MEETING 1 §Actions M1-3, M1-4]` |
| 20 | **Confirm Accelo integration** — EL TEMP FILTER notes "NOT IN ACCELO?" | Accruity ops | 🟢 LOW (plumbing) | `[EL §TEMP FILTER]` |
| 21 | **Fix Files & Links template-default URL collision** — Document Inventory + PBC PDF Package URLs on Don Fowler row are identical to Spring Bengtzen and Alex Dykes (system-wide) | Accruity ops | 🟢 LOW (data integrity) | `[FL:Don Fowler §Document Inventory]` |
| 22 | **Backfill email log** — 0 threads in Email Log DB for Don Fowler; high-activity engagement should have captured threads | Generator / Accruity ops | 🟢 LOW (plumbing) | `[§3]` |
| 23 | **Run accountable plan setup** for Waterside once QBO is live | Seth | 🟢 LOW | `[MEETING 2 §Accountable Plan]` |
| 24 | **Set up Q2 2026 ES payment** (Q2 adjusted after STR purchase; coordinate timing) | Seth | 🟢 LOW | `[MEETING 2 §April 15 Payment]` |

**Total: 24 open items** (5 HIGH, 13 MED, 6 LOW)

---

## §8. Tax Strategies & Projected Savings

**Tax memo SENT 2025-12-22** but content not accessible this refresh (Tax Memo URL accessible via SharePoint). Strategy framework is fully reconstructable from meeting transcripts.

| Strategy | Status / Notes | Est. Savings | Source |
| --- | --- | --- | --- |
| **Kids' Payroll (Waterside Re LLC)** | Kids under 14 paid through LLC; shift wages off personal return; Waterside Re to be set up; payroll platform selection in progress | `? Pending workbook ingestion` — savings depend on children's effective tax rate vs. parent marginal rate | `[MEETING 1 §Kids' Payroll]` |
| **Solo/Self-Directed 401(k) — Waterside Advisors** | Plan to be established; Waterside Advisors S Corp hosts the plan; not yet set up | `? Pending workbook ingestion` — standard solo 401k up to $69,000 (2025 limit) | `[MEETING 1 §Retirement Plans]` |
| **Augusta Rule Rental Income Deduction** | ~$2,500–$3,000 deduction; to be included in 2025 draft return; documentation/valuation in prep | **~$2,500–$3,000** (Seth's estimate) | `[MEETING 2 §Augusta Rule]` |
| **Cost Segregation Study — STR Property** | Property not yet purchased; Seth committed to initiating cost seg study via affiliated engineering firm immediately on purchase; described as "major 2026 tax planning tool" | `? Pending property purchase` — highly dependent on property basis and STR bonus depreciation rules | `[MEETING 2 §Short-Term Rental]` |
| **Accountable Plan (Waterside)** | Pending QBO setup; meals, travel, business expenses to run through S Corp | `? Pending QBO setup + expense review` | `[MEETING 2 §Accountable Plan]` |
| **Entity-Structure Map (S Corp savings)** | Seth committed to produce estimated savings analysis (payroll-tax savings by moving child payroll and other items into S Corp) | `? Pending workbook ingestion` | `[MEETING 1 §Action M1-10]` |
| **2025 Estimated Tax / Underpayment Check** | April 15 estimate was to be run; currently past due — outcome unknown; Q2 ES will be adjusted after STR | `? Pending confirmation` — $135K total liability was 2025 estimate | `[MEETING 1]` `[MEETING 2]` |
| **Tax Professionals LLC — Royalty Income Isolation** | $6K/month royalty income isolated in separate LLC + bank account; separate QBO class | Structural/compliance (no direct savings — ensures proper character of income) | `[MEETING 2 §Multiple Entities]` |

**2025 estimated total tax liability: ~$135,000** (Seth's working estimate per MEETING 1 — driven by Real Flow W-2 + entity income + K-1s). `[MEETING 1 §Tax Planning and Estimates for 2025]` This figure is Seth's real-time estimate from the Jan 15 session; final number pending K-1s and draft return.

---

## §9. Opportunity Flags (auto-detected)

### 9.1 Cost Segregation — HIGH FLAG

**Trigger**: Don is actively planning to purchase a short-term rental property in FL/GA/SC/NC at approximately $1M purchase price in 2025/2026. Seth has already committed to initiating a cost seg study via Accruity's affiliated engineering firm immediately on purchase. `[MEETING 2 §Short-Term Rental Property]`

**Classifier output**: HIGH opportunity — STR + bonus depreciation = maximum cost seg benefit. At $1M purchase, a cost seg study typically identifies 20–35% of value as 5/7/15-year property eligible for 100% bonus depreciation (2025 rate confirmed — see 2026 tax law). Potential Year 1 deduction: **$200K–$350K** on a $1M STR (property-mix-dependent). `? Pending property purchase and workbook ingestion for exact figures.`

**Status**: Opportunity identified and in-process — Seth already flagged it. Awaiting Don to notify Seth when property purchase closes. No further discovery action needed; action is execution on notification.

### 9.2 S-Corp Election / Optimization — MED FLAG

**Trigger**: Don has Waterside Advisors as an existing S Corp and is running $6K/month royalty income through Tax Professionals LLC. The S Corp structure for Waterside Advisors is already in place; the question is whether Tax Professionals LLC should also be elected/classified as S Corp or flow through differently. `[MEETING 2 §Multiple Entities]`

**Classifier output**: MEDIUM — entity structure already partially optimized; incremental opportunity is in ensuring proper W-2 vs. distribution split on Waterside Advisors and classifying Tax Professionals LLC income correctly (royalty vs. SE income character matters).

### 9.3 Augusta Rule — ACTIVE/IN-PROGRESS

**Status**: Seth has already committed to including Augusta Rule deduction (~$2,500–$3,000) in 2025 draft return. Not a discovery flag — already in execution. `[MEETING 2 §Augusta Rule]`

### 9.4 Accountable Plan — PENDING

**Status**: Seth committed to walking through Don's business expenses once QBO is live. Not a discovery flag — already planned. `[MEETING 2 §Accountable Plan]`

### 9.5 Solo 401(k) — ACTIVE/IN-PROGRESS

**Status**: Solo 401(k) for Waterside Advisors committed to by Seth but not yet established. Action item M1-5 still open. `[MEETING 1 §Retirement Plans]`

---

## §10. Operations Analysis

Don & Christina Fowler represent one of the **most operationally complex** active engagements in the current Accruity pipeline. Key indicators:

**Engagement health score: AMBER** — structurally healthy (EL executed, planning delivered, outsourcing assigned) but with **5 HIGH-priority blockers** on the compliance side (K-1 delays, offshore preparer information gap, overdue April 15 payment estimate).

**Complexity drivers:**
- 4 entities in scope (personal 1040, Waterside Advisors S Corp, Waterside Re LLC [to establish], Tax Professionals LLC) `[§2 Entity Stack]`
- 2 third-party K-1s (Seven Diamonds + Real Flow) with August delivery timelines `[MEETING 2]`
- Kids' payroll strategy (2–3 minor children; W-2 amendment potentially needed) `[MEETING 2]`
- STR acquisition in planning stages → cost seg trigger pending `[MEETING 2]`
- QBO setup not yet complete for Waterside (Oct/Nov 2025 activity unbooked) `[MEETING 2]`
- Offshore outsourcing blocked on missing prior-year return + CCH access `[Outsourcing §Offshore Quick Notes]`

**Process timeline reconstruction:**
- 2025-10-16: Insights Delivery call
- 2025-11-22: Tax Ascend signed
- 2025-12-22: Tax memo sent to Don
- 2026-01-07: First Tax Planning Session — **RESCHEDULED**
- 2026-01-15: Tax Planning Session 1 — full strategic review (Otter.ai transcript)
- 2026-01-26: EL batch added (compliance cycle formally opened)
- 2026-03-09: PBC list sent + Extension email sent
- 2026-03-26: Tax Planning Session 2 — QBO, K-1 status, Q1 estimates (Fireflies transcript)
- 2026-04-23: Assigned to Unison Globus for outsourced prep
- 2026-05-05: Outsourcing status = Missing Information (awaiting prior return + CCH)

**Silent gap (as of 2026-05-07):** 42 days since Meeting 2 (March 26). Q2 planning meeting was targeted for May 2026 — confirm whether scheduled. April 15 estimated tax payment was to be computed before 4/15 — outcome unknown; this is the most operationally urgent open item. `[§7 Action #5]`

**Duplicate Account risk.** The to-delete Account has critical sidecar records that must be migrated before deletion: EL, Files & Links, Tax Ascend record, Tax Planning Session, one Meetings Tracker row. Deletion without migration would orphan all of these records. `[§7 Actions 17–18]`

---

## §11. Individual Profile

### §11.1 Don Fowler

| Dimension | Detail | Source |
| --- | --- | --- |
| Role | Primary client; entrepreneur + W-2 executive | `[Contact:Don Fowler]` `[MEETING 1]` |
| Email | dfowler@realeflow.com | `[Contact:Don Fowler §Email]` |
| Phone | (954) 554-9134 | `[Contact:Don Fowler §Phone]` |
| Employer | Real Flow (CRE investment platform — also K-1 source) | `[MEETING 1]` |
| Business interests | Waterside Advisors (S Corp), Waterside Re LLC (forming), Tax Professionals LLC ($6K/mo royalty), Seven Diamonds (K-1) | `[MEETING 1]` `[MEETING 2]` |
| Children | 2–3 minor children on payroll (under 14); W-2 issued at $14,600; third kid's payment as accrual | `[MEETING 2]` |
| STR plans | Targeting ~$1M property purchase in FL/GA/SC/NC 2025/2026 | `[MEETING 2]` |
| Tax engagement posture | Highly engaged; attentive to strategy; brings wife to calls for note-taking; proactively tracks expenses on spreadsheet | `[MEETING 1 §Meeting Setup]` `[MEETING 2]` |
| Portal access | Customer Accessed ✓ | `[EL §Mango Portal Invite]` |
| Outstanding actions | 5 personal/direct (M1-1, M1-2, M2-1, M2-2, M2-3/4 — bank statements, K-1 follow-up, STR notification) | `[§7]` |
| Relationship-risk read | LOW — highly engaged, signed, multi-meeting cadence; main risk is K-1 delays (external) and new-entity setup complexity | derived |

### §11.2 Christina Fowler

| Dimension | Detail | Source |
| --- | --- | --- |
| Role | Spouse / co-filer; appears on joint EL | `[EL §CLIENT]` |
| Engagement | Attended MEETING 1 to take notes; described as "not tech-savvy" per transcript | `[MEETING 1 §Meeting Setup]` |
| Portal access | Not confirmed separately — shared with Don | — |
| Filing status | Joint filer (MFJ implied) | derived |

---

## §12. Provenance Index

### Notion — Accounts
- `[Accounts:DonFowler-canonical]` → [notion.so/30b4917287518140a497eadeb0956108](https://www.notion.so/30b4917287518140a497eadeb0956108) — Client #04140618-01 · **canonical** · 🔴 icon
- `[Accounts:DonFowler-todelete]` → [notion.so/30d49172875181a3af5ad2fb9bd8f656](https://www.notion.so/30d49172875181a3af5ad2fb9bd8f656) — Client #04140618-02 · **To Delete: YES** · holds EL + Files & Links + Tax Ascend + Tax Planning Session

### Notion — Executive Summaries DB
- `[ExecSum:Don Fowler]` → [notion.so/33b4917287518182af1ccf406d897743](https://www.notion.so/33b4917287518182af1ccf406d897743) — existing row, unpopulated body (Activity Log header only)

### Notion — Reporting Entities
- `[RE:Don Fowler]` → [notion.so/30b4917287518148a3fef94e9a5dc6af](https://www.notion.so/30b4917287518148a3fef94e9a5dc6af) — 1040 · Construction industry

### Notion — Tax Engagements
- `[TaxEng:Planning 2024]` → [notion.so/30b4917287518155b73df0c82f72bb77](https://www.notion.so/30b4917287518155b73df0c82f72bb77) — Planning · 2024 · Not Started
- `[TaxEng:Compliance 2024]` → [notion.so/30b4917287518159ad6dcfc0ad186de4](https://www.notion.so/30b4917287518159ad6dcfc0ad186de4) — Compliance · 2024 · In Progress

### Notion — Meetings Tracker (4)
- `[Meeting 2025-10-16 Insights Delivery]` → [notion.so/2fb49172875180838d79d10c572bafe0](https://www.notion.so/2fb49172875180838d79d10c572bafe0) — [Fathom](https://fathom.video/share/kqPvzuPym-vMA7pWxjPyBTizVys9qPv7)
- `[Meeting 2026-01-07 Rescheduled]` → [notion.so/2fb49172875180949da8e7c5d021b40b](https://www.notion.so/2fb49172875180949da8e7c5d021b40b) — Rescheduled
- `[Meeting 2026-01-15 Tax Planning 1]` → [notion.so/2fb4917287518051892df7688f72fa09](https://www.notion.so/2fb4917287518051892df7688f72fa09) — [Otter.ai](https://otter.ai/u/IEZfLwzVM4ID3M4vQd51drhKKqI?utm_source=copy_url)
- `[Meeting 2026-03-26 Tax Planning 2]` → [notion.so/33049172875180d1a638c5899f5594ce](https://www.notion.so/33049172875180d1a638c5899f5594ce) — [Fireflies](https://app.fireflies.ai/view/seth-johnson-and-Don-Fowler::01KMGZKY0Q2A6MTA0YMEY5VKWX) (linked to to-delete account)

### Notion — Tax Ascend
- `[Tax Ascend:Don Fowler]` → [notion.so/2f0491728751802b95e5d46aaf1d028a](https://www.notion.so/2f0491728751802b95e5d46aaf1d028a) — ✅ Planning delivered · signed 2025-11-22 · memo sent 2025-12-22

### Notion — Engagement Letters Tracker
- `[EL:Don & Christina Fowler]` → [notion.so/2ef491728751805d9800c2727ff3b36c](https://www.notion.so/2ef491728751805d9800c2727ff3b36c) — ✅ Signed/Executed · $1,800 · PLAN+COMPLIANCE · PBC received

### Notion — Files & Links (3, linked to to-delete account)
- `[FL:Don Fowler Engagement Letter]` → [notion.so/33b49172875181b3926cf211f123ac2f](https://www.notion.so/33b49172875181b3926cf211f123ac2f) (empty)
- `[FL:Don Fowler Executive Summary]` → [notion.so/33b491728751815ebb32eef1a15825c1](https://www.notion.so/33b491728751815ebb32eef1a15825c1) (empty)
- `[FL:Don Fowler]` → [notion.so/33b491728751811aaf78ffb047f5c0d6](https://www.notion.so/33b491728751811aaf78ffb047f5c0d6) — Document Inventory + PBC PDF Package (template-default URLs; match Spring + Alex Dykes)

### Notion — Insights Project
- `[Insights:Don Fowler]` → [notion.so/329491728751801b8fe0cfce6237e184](https://www.notion.so/329491728751801b8fe0cfce6237e184) — 👉 DELIVERED 2025-10-16 · Analysis: Waiting on Extraction

### Notion — Tax Planning Session
- `[TaxPlanSession:Don Fowler]` → [notion.so/2ea49172875181f99864ee2ef50f64b1](https://www.notion.so/2ea49172875181f99864ee2ef50f64b1) — ✅ Meeting 1 Delivered · Mango step 6
- `[Tax Planning MEETING 1]` → [notion.so/32f4917287518029a4b5cc6af1f45bb7](https://www.notion.so/32f4917287518029a4b5cc6af1f45bb7) — 2026-01-15 full transcript; Otter.ai + Fireflies recaps; 10 action items
- `[Tax Planning MEETING 2]` → [notion.so/32f491728751808ba1c9ea216469875b](https://www.notion.so/32f491728751808ba1c9ea216469875b) — 2026-03-26 full transcript; Fireflies recap; 11 action items

### Notion — Outsourcing & Compliance Trackers
- `[Outsourcing:1040 Don Fowler]` → [notion.so/30c491728751804d9b32df9f9c6c68ca](https://www.notion.so/30c491728751804d9b32df9f9c6c68ca) — 🟡 Assigned to Unison Globus 2026-04-23 · Missing Information
- `[TaxCompliance:1040 Don Fowler]` → [notion.so/a9a491728751827d9bb401d244b365e5](https://www.notion.so/a9a491728751827d9bb401d244b365e5) — Extension filed · Due 2026-10-15 · Stage: 03 Collect and Review K-1s

### Notion — Client Contact
- `[Contact:Don Fowler]` → [notion.so/30d4917287518156bed4dd9a76fe71e8](https://www.notion.so/30d4917287518156bed4dd9a76fe71e8) — dfowler@realeflow.com · (954) 554-9134 · linked to both Accounts

### SharePoint / Drive / Portals
- Signed EL (Mangoshare): [app.mangoshare.com/share/d026ad8a55748cf22d1ee3d2](https://app.mangoshare.com/share/d026ad8a55748cf22d1ee3d2)
- PBC folder (imaginetime): [app.imaginetime.com/firm/5331/workspaces/937686/files/18417535/folder](https://app.imaginetime.com/firm/5331/workspaces/937686/files/18417535/folder)
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBPl7S1t-P_QIsMHwgtMQZrAWBPESYRTymjQ1LG5z83SmM?e=YzcDVY)
- Tax Memo (SharePoint): [SharePoint .docx](https://subledgesl.sharepoint.com/:w:/s/Insights/IQDFbj68DxnVQJv85faUFKTMAdf3ns1-eIl_8soapsExFCQ?e=J7hTqE)
- Client SharePoint folder: [SharePoint](https://subledgesl-my.sharepoint.com/:f:/g/personal/seth_accruity_com/IgC1e89ZgpHURLOm4qh4E8WRAS2iP1ln6bWkEs-bpE6T_mg?e=6EugZ0)
- Mango SOW: [app.mangoshare.com/share/49c46cd9dcc2e9d0c2b1aae6](https://app.mangoshare.com/share/49c46cd9dcc2e9d0c2b1aae6)
- Mango PBC: [app.mangoshare.com/share/27340432b3c32c15108513f4](https://app.mangoshare.com/share/27340432b3c32c15108513f4)

### Cross-dossier references
- `[FL:Spring §Document Inventory]` + `[FL:Alex Dykes §Document Inventory]` — same template-default URL collision pattern (third confirmed instance)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.** No prior dossier existed.

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- Don & Christina Fowler: MFJ household · Construction industry · Tax Ascend Plan+Compliance $1,800 · EL Signed/Executed · Insights DELIVERED 2025-10-16 · Tax Memo sent 2025-12-22
- **Multi-entity structure**: Waterside Advisors S Corp (active) + Waterside Re LLC (forming) + Tax Professionals LLC ($6K/mo royalty) + Real Flow W-2 + Seven Diamonds K-1
- **Two full tax planning meeting transcripts** synthesized: 2026-01-15 (10 action items — entity setup, kids' payroll, 401(k), Augusta Rule, ~$135K 2025 estimated liability) and 2026-03-26 (11 action items — K-1 delays, QBO setup, April 15 estimate, cost seg trigger, accountable plan)
- **Compliance is in-progress**: extension filed, assigned to Unison Globus (2026-04-23), outsourcing blocked on missing prior-year return + CCH access, current stage: Collect and Review K-1s
- Contact record confirms: dfowler@realeflow.com · (954) 554-9134

**New — discoveries:**
- ⚠️ **Duplicate Account rows** (canonical `30b4…0108` vs. to-delete `30d4…f656` marked To Delete: YES but with critical sidecar records still attached) — promoted to §7 Actions 17–18 as MED data-integrity items
- ⚠️ **Files & Links template-default URL collision** (third confirmed instance: Spring, Alex Dykes, now Don Fowler) — promoted to §7 Action 21
- **🔴 HIGH cost seg opportunity** — STR acquisition ~$1M in pipeline; Seth already committed; promoted to §9.1
- **April 15 estimated tax estimate overdue** (meeting said "before 4/15"; now 2026-05-07); promoted to §7 Action 5 as HIGH
- **Offshore preparer blocked** on missing 2024 tax return copies + CCH access; promoted to §7 Actions 1–2 as HIGH
- Files & Links rows all linked to to-delete Account, not canonical — structural data-integrity gap

**Strategic theme:** Fowler is a high-value planning engagement in a critical phase — planning delivered, but compliance is mid-stream with K-1 delays and offshore prep blocker. Multiple new entities being stood up simultaneously (Waterside Re, QBO for Waterside Advisors). The Q2 May planning meeting should be the activation trigger to clear all open items. Cost seg study is the most valuable near-term opportunity.

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 24 | Open action items (5 HIGH, 13 MED, 6 LOW) | §7 |
| 4 | Meetings on file (1 Insights delivery, 1 rescheduled, 2 planning sessions with full transcripts) | §4 |
| 21 | Action items extracted directly from meeting transcripts (M1: 10, M2: 11) | §4.1, §4.2 |
| 6 | Active entities / income streams | §2 Entity Stack |
| 2 | K-1s blocking compliance (Seven Diamonds, Real Flow) | §7 Actions 3–4 |
| 3 | Files & Links rows on to-delete Account | §5.5 |
| 1 | HIGH cost seg opportunity in pipeline | §9.1 |
| 1 | Files & Links template-default URL collision (system-wide) | §5.5 |
| 0 | Email threads in Email Log | §3 |
| 0 | Prior Claude sessions | §6 |

### 13.3 What a reader should look at first

1. **§7 Actions #1–2** — offshore preparer is blocked today. Unison Globus needs 2024 tax return copies + CCH access to proceed. This is the most immediate compliance gating item.
2. **§7 Action #5** — April 15 payment estimate was overdue as of this refresh (May 7, 2026). Confirm whether Seth ran the analysis and whether the Q1 ES payment was made. If not, underpayment penalties may have accrued.
3. **§9.1 Cost Seg** — HIGH opportunity; STR acquisition in active planning. When Don notifies Seth of purchase, the cost seg clock starts. Ensure this doesn't get lost in the K-1 waiting period.
4. **§7 Actions #17–18** — duplicate Account cleanup. The to-delete row must have EL, Files & Links, Tax Ascend, Tax Planning Session, and the March meeting migrated to the canonical row before the to-delete row is actually deleted.
5. **§4.2** — read the full MEETING 2 synthesis for the current operational picture and the 11 open action items from March 26.

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/DonFowler/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: FULL (two complete meeting transcripts, multi-entity structure, active compliance outsourcing) · Next refresh: trigger on May planning meeting OR on STR purchase close OR on K-1 receipt*
