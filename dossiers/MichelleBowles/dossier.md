# Michelle (& Jason) Bowles — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Jason & Michelle Bowles (joint household) |
| Account Name | Jason Michelle Bowles |
| Client # | *(not yet populated on Account record)* |
| Mango Client ID | *(not yet populated — imaginetime workspace ID 937719 referenced in EL PBC folder link; same ID as Logan Bowles — flag for verification)* |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-05-07 |
| Prior Refresh | first run |
| Depth mode | **MEDIUM** — substantive Claude Activity Log (2 sessions, 2026-04-09); EL executed; Tax Ascend active; 1 email thread; 0 direct meetings linked to account; no Files & Links rows; Tax Memo sent |
| Engagement Stage | Tax Ascend — Tax Planning + Tax Compliance; EL Signed/Executed; Tax Memo Sent 2026-02-10; planning call NOT yet scheduled as of refresh date |
| Engagement Fee | **$3,675** (compliance) |
| Temperature | **ELEVATED CONCERN** — client expressed shock at extension amounts (~$19.5K actual, overstated at $65K in email); IRS delinquency history (2022/2023 + 2024 CP14); SE tax error on 2024 return (~$6.5K overpayment); planning call urgently needed; 2-month response gap |
| Relationship Manager | Seth Johnson (per Account Hub ancestry) |
| Data Sources (this refresh) | Notion Accounts record · Engagement Letter Tracker row · Tax Ascend record · 1 Client Email Log row · 2 Claude Activity Log rows · Exec Summary DB row (existing, empty body) |
| Files NOT Accessible This Refresh | Analysis File / Extraction File (Tax Ascend fields omitted); PBC Workbook (Account field empty); Tax Extraction (Account field empty); Tax Memo SharePoint doc (linked but not fetched) |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index.

**Critical disambiguation:** "Jason Michelle Bowles" is a **separate Accruity account** from "Logan Bowles." They are **co-investors / business partners** in Clayhouse Mortgage LLC (50/50 K-1 split) and both receive Clayhouse Mortgage LLC K-1s, but they file separately: Michelle files MFJ (with spouse Jason), Logan files Single. They are **not household partners with each other.** `[CAL:Bowles Tax Planning]` `[CAL:Bowles 2025 Estimates]`

---

## §1. Executive Overview

Jason & Michelle Bowles are an Accruity Tax Ascend household (Planning + Compliance) currently in a **high-urgency posture**. The engagement opened January 2026 — EL signed **2026-01-29**, PBC list sent **2026-02-03**, Tax Memo sent **2026-02-10**. As of refresh date the planning call has **not been scheduled**, a 2+ month gap from memo delivery that has become a relationship risk. `[EL:Jason Michelle Bowles]` `[TaxAscend:Michelle Bowles]`

The financial picture is **materially complex and delinquency-prone.** Michelle's household (filing MFJ with Jason) holds a 50% K-1 interest in Clayhouse Mortgage LLC (same entity as Logan Bowles), generating ~$178K K-1 income partially offset by Clay Construction passive losses (~$75K) and SE tax on ~$51.5K per spouse. The 2025 estimated total tax is **~$19,490** — but the extension email sent 2026-04-09 incorrectly stated ~$65K, causing client shock and a relationship rupture that must be addressed immediately. `[CAL:Bowles 2025 Estimates]`

IRS history is a significant underwriting risk: 2022/2023 delinquency (~$70K installment plan) and a 2024 CP14 notice (~$65.5K), with a $40K payment applied (assume cleared, unconfirmed). A **~$6,545 SE tax overpayment error** on Michelle's 2024 return was identified — this is a concrete near-term deliverable: amend 2024 to recover the overpayment. `[CAL:Bowles 2025 Estimates]`

The **primary planning play** is S-Corp formation for Clayhouse Mortgage LLC principals (new holding company for Michelle's interest), projected to save **~$37K/yr combined SE tax** across both Bowles households, with Michelle's share ~$16–20K/yr individually. The March 15 S-Corp election deadline for 2026 was missed — holding company formation is the path forward (CHMMB Holdings LLC, per Claude session). `[CAL:Bowles Tax Planning]`

No real estate on file for Michelle's household — **cost seg does not apply** this refresh. `[CAL:Bowles Tax Planning]`

**What matters right now.** (1) Correct the extension email error ($65K → ~$19.5K) and repair client trust. (2) Schedule the planning call. (3) Identify and amend the 2024 SE tax error (~$6.5K refund). (4) Advance CHMMB Holdings LLC formation + S-Corp election process. (5) Get PBC docs in — Open items status: "Sent List nothing received yet" as of EL tracker. `[EL:Jason Michelle Bowles]`

---

## §2. Client Profile

| Item | Value | Source |
| --- | --- | --- |
| Account name | Jason Michelle Bowles | `[Accounts]` |
| Account page URL | notion.so/329491728751806799d2f1c4471ce13b | `[Accounts]` |
| Client # | *(empty — not populated)* | `[Accounts]` |
| Mango Client ID | *(empty on Account record; imaginetime workspace 937719 referenced in EL PBC folder — verify; same ID as Logan, may be error)* | `[Accounts]` `[EL §PBC Folder Link]` |
| Filing status | MFJ (Michelle + Jason Bowles) | `[CAL:Bowles 2025 Estimates]` |
| Engagement type | Tax Ascend — Planning + Compliance | `[TaxAscend:Michelle Bowles]` |
| EL status | **Signed · Executed** | `[EL §Engagement Letter Status]` `[EL §Compliance Group Status]` |
| EL batch date | 2026-01-30 | `[EL §Batch Added]` |
| EL signed date | 2026-01-29 | `[TaxAscend §Date Signed]` |
| Engagement fee | **$3,675** | `[EL §Price]` |
| Deposit | Paid ✓ | `[EL §Deposit Paid]` |
| Mango portal | Portal Invite Sent ✓ | `[EL §Mango Portal Invite]` |
| Mango project | Project Created ✓ | `[EL §Mango Engagement/Project]` |
| PBC list sent | 2026-02-03 | `[EL §Date PBC list sent]` |
| PBC items received | **None received yet** (as of EL tracker) | `[EL §PBC list status]` |
| Tax Memo status | **SENT** (2026-02-10) | `[TaxAscend §TAX MEMO STATUS]` `[TaxAscend §Tax Memo Sent]` |
| Planning call | **NOT SCHEDULED** as of refresh | `[TaxAscend §Planning Status: New Client GC]` |
| Tax Ascend type | Tax Planning + Tax Compliance | `[TaxAscend §TAX ASCEND TYPE]` |

### 2.1 Principals

- **Michelle Bowles** (aka Michele Bowles — name varies in records) — primary taxpayer on Accruity record; 50% K-1 partner in Clayhouse Mortgage LLC; files MFJ with Jason; IRS delinquency history on her household `[CAL:Bowles 2025 Estimates]`
- **Jason Bowles** — spouse; co-filer MFJ; 50% SE-taxable partner alongside Michelle on Clayhouse Mortgage LLC (both draw ~$260K/yr combined from mortgage entity, zero payroll/withholding) `[CAL:Bowles 2025 Estimates]` `[CAL:Bowles Tax Planning]`

### 2.2 Entity Stack

| Entity | Role | Status | Source |
| --- | --- | --- | --- |
| Clayhouse Mortgage LLC | Operating entity; 50% K-1 to Michelle household | Active; ~$178K K-1 income | `[CAL:Bowles 2025 Estimates]` |
| Clay Construction | Passive investment; ~$75K loss offsets Clayhouse K-1 | Passive classification **questionable** — confirm at planning call | `[CAL:Bowles 2025 Estimates]` |
| CHMMB Holdings LLC | Proposed new holding co for Michelle's Clayhouse interest → S-Corp election | Formation in progress; EIN pending | `[CAL:Bowles Tax Planning]` |
| Clayhouse Mortgage LLC 1065 | Partnership return; assigned to Virtueshore | **Rejected** — needs resolution | `[CAL:Bowles Tax Planning]` |

### 2.3 Financial Snapshot (2025 estimates)

| Item | Amount | Confidence | Source |
| --- | --- | --- | --- |
| Clayhouse K-1 income (Michelle) | ~$178,000 | ~ | `[CAL:Bowles 2025 Estimates]` |
| Clay Construction passive loss | (~$75,000) | ~ | `[CAL:Bowles 2025 Estimates]` |
| SE tax base (per spouse) | ~$51,500 | ~ | `[CAL:Bowles 2025 Estimates]` |
| 2025 total estimated tax (MFJ) | **~$19,490** ($4.9K income + $14.6K SE) | ~ | `[CAL:Bowles 2025 Estimates]` |
| Extension email overstated liability | ~$65,000 (incorrect — caused client shock) | ✓ | `[CAL:Bowles 2025 Estimates]` |
| 2024 SE tax overpayment error | **~$6,545** (amendment opportunity) | ~ | `[CAL:Bowles 2025 Estimates]` |
| Combined revenue (both spouses, Clayhouse) | ~$260K/yr (zero payroll/withholding) | ~ | `[CAL:Bowles Tax Planning]` |

**Note on K-1 mismatch:** A ~$6,303 K-1 discrepancy exists between Logan Bowles' and Michelle's reported Clayhouse K-1 income on a purported 50/50 partnership — requires reconciliation. `[CAL:Bowles 2025 Estimates]`

### 2.4 Disambiguation — Logan vs Michelle Bowles

| Item | Logan Bowles | Jason Michelle Bowles |
| --- | --- | --- |
| Account URL | notion.so/30d491728751816d9949f6a4a7f23141 | notion.so/329491728751806799d2f1c4471ce13b |
| Mango Client ID | 937719 | *(empty — verify if 937719 is Logan's only)* |
| Filing | Single | MFJ (Michelle + Jason) |
| Clayhouse K-1 | 50% | 50% |
| 2025 est. tax | ~$42,500 | ~$19,490 |
| EL fee | $1,525 | $3,675 |
| Relationship | Business partner / co-investor | Separate household |
| Shared Claude sessions | Yes — 2026-04-09 sessions cover both | Yes — same sessions |

---

## §3. Email Intelligence

**1 email thread on Account.** `[EmailLog:Jason Michelle Bowles]`

### Thread 1 — Internal Notion Workspace Notification (Low)

| Field | Value |
| --- | --- |
| Subject | "Sophia@accruity commented in Jason Michelle Bowles" |
| Date | 2026-04-13 |
| Direction | Inbound |
| From | notify@mail.notion.so |
| Risk | Low |
| Action items | None |
| Source | `[EmailLog:342491728751816a911edda241785a0e]` |

**Summary:** Automated Notion notification — Sophia@accruity commented on the Jason Michelle Bowles engagement letter record, updating a workspace file path. Jane Malicdem also associated. Routine internal database maintenance. No client communication. `[EmailLog:Jason Michelle Bowles]`

**Email Intelligence gaps:**
- The **extension email** sent 2026-04-09 (that overstated liability at ~$65K) is referenced in the Claude Activity Log but does **not appear** in the Client Email Log as a distinct thread. This is a significant gap — that email is the source of the client relationship rupture. `[CAL:Bowles 2025 Estimates]`
- No inbound client emails on file. No client responses, confirmations, or PBC uploads captured.
- No Outlook direct scan has been run against Jason/Michelle Bowles email patterns.

**Plumbing gap** → §7 Action: backfill Client Email Log with the 4/9/2026 extension email thread; run Outlook scan for "Bowles" + "Michelle" + "Jason" patterns against `tax@accruitytax.com`.

---

## §4. Meeting History

**0 meetings linked to the Jason Michelle Bowles account** in the Meetings Tracker.

One **orphan meeting row** was found in the Meetings Tracker with no Account relation:

| Date | Client Name in Tracker | Type | Status | Recap | Account Linked | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-04-17 | Michelle R Bowles | *(not set)* | **Pending** | *(none)* | **NO** | `[Meeting:Michelle R Bowles]` |

This Pending row (no type, no recap, no account relation) almost certainly belongs to the Jason Michelle Bowles account. It is **not linked** — promoted to §7 as a plumbing action. The April 17 date aligns with the post-extension-email urgency (extension email 4/9, meeting set for 4/17). `[Meeting:Michelle R Bowles]`

**Cross-account note:** The Logan Bowles account has 4 linked meetings (2025-11-26 Kickoff, 2025-12-17 Clarification, 2025-12-23 Delivery, 2026-04-10 Touchbase) related to the shared Clayhouse Mortgage / Insights project, and the 2026-04-09 Claude sessions that cover both accounts reference shared planning context. These are not linked to the Michelle account but provide relevant context. `[Accounts:Logan Bowles §Meetings]`

**Restricted flag:** 0 meetings restricted.

---

## §5. Document Inventory

### 5.1 Engagement Letter (Signed/Executed)

| Field | Value |
| --- | --- |
| Status | **Signed · Executed** |
| Price | **$3,675** |
| Deposit | Paid ✓ |
| Batch added | 2026-01-30 |
| Portal invite | Sent ✓ |
| Mango project | Created ✓ |
| Signed EL Mangoshare | [app.mangoshare.com/share/f1a2bbd1dc838675b2bbc1a1](https://app.mangoshare.com/share/f1a2bbd1dc838675b2bbc1a1) |
| PBC folder (imaginetime) | [imaginetime.com/firm/5331/workspaces/937719/files/18474205/folder](https://app.imaginetime.com/firm/5331/workspaces/937719/files/18474205/folder) ⚠️ workspace 937719 = Logan's Mango ID — verify |
| PBC list (SharePoint xlsx) | [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBhuvdyU8rtS7KwsogxazWMActThbaZXT05Ne95zy1xDA0?e=zbYtSf) |
| PBC list status | **Sent List — nothing received yet** |
| Outlook msg | `Michelle_Bowles.msg` (attachment on EL tracker row) |
| Entity compliance | "No services ticked on signed EL" |
| Docusign email status | Delivered |
| Check portal/staff | 03/16 |
| Newly added | Done |

Source: `[EL:Jason Michelle Bowles]`

### 5.2 Tax Ascend

| Field | Value |
| --- | --- |
| Tax Memo status | **SENT** |
| Tax Memo sent | 2026-02-10 |
| Tax Memo URL (SharePoint .docx) | [Memo 1](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQD9rbWDMxRqSolklj0o7s6LAXl_lwVofg4X-CY0jkk3kCc?e=5c4sW5) · [Memo 2](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQBf4C6HuNzmQ6WfTPv2Ni8QAYyQJMMnVb5sEa3yiSv2kUM?e=nYHQ6L) *(same URLs as Logan Bowles — possible shared memo or template duplication; verify)* |
| Planning meeting status | *(not set)* |
| Compliance status | PBC list and Mango share emailed |
| Planning status | New Client GC |
| Mango compliance engagement | None in Mango (check EL) |
| Mango planning projects | Done |
| Linking status | N/A — Insights Project; PENDING INSERT TO INSIGHTS TRACKER |
| Analysis File | *(omitted / not accessible this refresh)* |
| Extraction File | *(omitted / not accessible this refresh)* |

Source: `[TaxAscend:Michelle Bowles]`

> **Plumbing gap — Tax Memo URL collision.** Both Michelle and Logan Tax Ascend records reference **identical Tax Memo SharePoint URLs** (Memo 1 and Memo 2). Either (a) the memo covers both households and was intentionally shared, or (b) these are template defaults that were never per-client-customized (same pattern flagged in Alex Dykes dossier). Investigate on next refresh. `[TaxAscend:Michelle Bowles]` `[TaxAscend:Logan Bowles]`

### 5.3 Files & Links

**0 Files & Links rows** on the Jason Michelle Bowles account. `[Accounts §Files & Links]`

No Document Inventory URL, no PBC PDF Package, no Executive Summary file URL populated on Account record.

### 5.4 Account-Level URL Fields

| Field | Value |
| --- | --- |
| PBC Workbook | *(empty)* |
| Tax Extraction | *(empty)* |
| Tax Planning Memo | *(empty)* |
| Document Inventory | *(empty)* |
| Executive Summary | *(empty)* |
| SharePoint Drive | *(empty)* |

All account top-level URL fields are unpopulated. Consistent with "new client" status (joined Jan 2026) and the pattern seen on other recent-onboard accounts. `[Accounts:Jason Michelle Bowles]`

---

## §6. Claude Work Product

**2 prior Claude sessions** tied to the Jason Michelle Bowles account (both dated 2026-04-09, same chat thread: [claude.ai/chat/6b78c98d-3cc6-41ab-9b07-a4d6a85099ad](https://claude.ai/chat/6b78c98d-3cc6-41ab-9b07-a4d6a85099ad)). These sessions are **cross-account** — they cover both Logan Bowles and Jason Michelle Bowles simultaneously. `[CAL:Bowles Tax Planning]` `[CAL:Bowles 2025 Estimates]`

| # | Title | Date | Type | Key Output | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Project — Bowles Tax Planning & Structure Review | 2026-04-09 | Tax Planning | S-Corp / SE savings analysis; holding co formation plan; Clayhouse 1065 rejection flag; extension email context; combined ~$37K/yr SE savings projection | `[CAL:33d4917287518110adc7d8076a84d8d9]` |
| 2 | Project — Bowles 2025 Tax Estimates, Extraction Review & IRS History | 2026-04-09 | Tax Analysis | Full 2025 tax computation MFJ; ~$19,490 total tax; extension email error (~$65K overstated); SE tax error 2024 (~$6,545); K-1 mismatch $6,303; IRS delinquency history 2022–2024; cost seg on Michelle household: N/A (no real estate) | `[CAL:33e4917287518184b1adcd8855a92c66]` |

**HTML session output:** `2026-04-09_Bowles_Thread_Summary.html` (covers both Bowles accounts) — referenced in Exec Summary Activity Log `[ExecSum:Jason Michelle Bowles]`

**Note from Exec Summary Activity Log (pre-existing entry):** "2025 estimate ~$19.5K due (construction $75K loss nets against $178K Clayhouse K-1, SE at $51.5K/spouse). Extension email overstated at $65K. IRS history: 2022/2023 delinquency ($70K installment) + 2024 CP14 ($65.5K) — $40K payment applied, assume cleared. SE tax error on 2024 return (~$6.5K overpayment). K-1 mismatch with Logan ($6.3K). Clay Construction passive classification questionable. Confirm cash vs accrual for bad debt treatment." `[ExecSum:Jason Michelle Bowles §Activity Log]`

This refresh creates the first Claude Summaries DB log row for this account.

---

## §7. Action Items — Rolled Up

| # | Action | Owner | Priority | Source |
| --- | --- | --- | --- | --- |
| 1 | **IMMEDIATE: Correct extension email error** — reach out to Michelle/Jason to clarify ~$19.5K actual liability vs. the ~$65K overstated in the 4/9/2026 email. Repair client trust before planning call. | Seth / Client Relations | 🔴 HIGH | `[CAL:Bowles 2025 Estimates]` |
| 2 | **Schedule planning call** — no planning call booked as of refresh; memo sent 2/10, now 3+ months old; client upset. Must close S-Corp conversation, walk through actual estimates, address IRS history. | Seth (RM) | 🔴 HIGH | `[TaxAscend §Planning Status]` `[CAL:Bowles Tax Planning]` |
| 3 | **Amend Michelle's 2024 return** to recover ~$6,545 SE tax overpayment identified in Claude 4/9 session. Confirm exact amount, then file 1040-X. | Tax Team | 🔴 HIGH | `[CAL:Bowles 2025 Estimates]` |
| 4 | **Link the orphan meeting row** (notion.so/349491728751807e964de541607dd502) to the Jason Michelle Bowles account; add type and recap once meeting has occurred | Accruity ops | 🟡 MED | `[Meeting:Michelle R Bowles]` |
| 5 | **Advance CHMMB Holdings LLC formation** — EIN application + S-Corp election filing; coordinate with CHMLB (Logan's holding co) since both entities are part of same Clayhouse restructuring | Tax Team / Entity Formation | 🟡 MED | `[CAL:Bowles Tax Planning]` |
| 6 | **Resolve Clayhouse Mortgage LLC 1065 rejection** at Virtueshore — this blocks partnership K-1 accuracy for both Bowles households | Tax Team | 🟡 MED | `[CAL:Bowles Tax Planning]` |
| 7 | **Get PBC docs in** — nothing received since list sent 2/2/2026; follow up with client; may be tied to shock/upset over extension email | Sophia / Client Ops | 🟡 MED | `[EL §PBC list status]` |
| 8 | **Reconcile K-1 mismatch** — $6,303 difference between Logan's and Michelle's reported Clayhouse K-1 income on purported 50/50 partnership; pull 2024 Clayhouse 1065 K-1 schedules | Tax Team | 🟡 MED | `[CAL:Bowles 2025 Estimates]` |
| 9 | **Confirm Clay Construction passive classification** — if active, the ~$75K loss is non-deductible against K-1; this changes Michelle's 2025 estimated tax materially. Also: confirm cash vs accrual for bad debt treatment | Tax Team | 🟡 MED | `[ExecSum §Activity Log]` |
| 10 | **Verify Mango Client ID** — Account record has no Mango Client ID; EL PBC folder references workspace 937719 (Logan's ID) — may be an entry error | Accruity ops | 🟡 MED (data integrity) | `[EL §PBC Folder Link]` `[Accounts:Logan Bowles §Mango Client ID]` |
| 11 | **Backfill Client Email Log** — extension email (4/9/2026) not captured; run Outlook scan for Bowles/Michelle/Jason patterns | Accruity ops | 🟡 MED | `[§3]` |
| 12 | **Tax Memo URL collision check** — both Michelle and Logan Tax Ascend rows reference identical SharePoint Tax Memo URLs; determine if intentional (shared memo) or template default | Accruity ops | 🟡 MED (data integrity) | `[TaxAscend:Michelle Bowles]` `[TaxAscend:Logan Bowles]` |
| 13 | **Populate Client # and Mango Client ID** on Account record | Accruity ops | 🟢 LOW | `[Accounts §Client #]` |
| 14 | **IRS delinquency status** — confirm 2022/2023 installment plan cleared; confirm 2024 CP14 ($65.5K) fully satisfied after $40K payment | Tax Team | 🟡 MED | `[CAL:Bowles 2025 Estimates]` |
| 15 | **Create Files & Links rows** for Michelle account (Document Inventory, Executive Summary, PBC Package) — currently 0 rows | Accruity ops | 🟢 LOW | `[§5.3]` |
| 16 | **Probe for real estate** at planning call — no properties on file; if properties exist, cost seg analysis applies | Tax Team / Seth | 🟢 LOW | `[CAL:Bowles Tax Planning]` |

Total: **16 open items** (3 HIGH, 9 MED, 4 LOW).

---

## §8. Tax Strategies & Projected Savings

### 8.1 Strategy Table

| # | Strategy | Status | Projected Savings | Source |
| --- | --- | --- | --- | --- |
| 1 | **S-Corp election via CHMMB Holdings LLC** — Michelle's Clayhouse Mortgage interest restructured through a new holding co; reasonable salary below draw eliminates SE tax on distributions | Formation in progress; EIN pending; March 15 deadline missed — holding co route required for 2026 | **~$16–20K/yr** (Michelle alone); ~$37K combined with Logan | `[CAL:Bowles Tax Planning]` |
| 2 | **2024 return amendment** — SE tax computation error; ~$6,545 overpayment recoverable via 1040-X | Identified; not yet filed | **~$6,545** (one-time refund) | `[CAL:Bowles 2025 Estimates]` |
| 3 | **Clay Construction passive loss classification** — if activity qualifies as non-passive, ~$75K loss fully deductible against K-1; confirm material participation / active status | Questionable per Claude session — needs planning call confirmation | ? (depends on classification outcome) | `[ExecSum §Activity Log]` |
| 4 | **Cash vs accrual election for bad debt** — bad debt treatment options for Clay Construction may differ by accounting method; confirm method and apply | Flagged; not yet analyzed | ? Pending workbook ingestion | `[ExecSum §Activity Log]` |
| 5 | **Quarterly estimated tax payments** — both Michelle and Jason drawing ~$260K/yr combined with zero payroll/withholding; structuring safe-harbor payments (110% of prior year, or actuals) critical to avoid underpayment penalties | Not yet addressed | Penalty avoidance value | `[CAL:Bowles Tax Planning]` |
| 6 | **Cost Segregation** | No real estate on file — **NOT APPLICABLE** this refresh | N/A | `[CAL:Bowles Tax Planning]` |
| 7 | **Augusta Rule (§280A)** | ? No information on file — probe at planning call | ? | derived |

**SE savings calculation basis:** Clayhouse Mortgage LLC distributes ~$260K/yr combined (both spouses) with zero withholding. At 15.3% SE tax (self-employment), full gross SE exposure ~$39.8K/yr for Michelle's household. Under S-Corp structure with reasonable salary ~$60K, SE exposure drops to ~$9.2K — saving ~$30.6K/yr (or $16–20K/yr per Claude session estimate accounting for state SE treatment and salary calibration). `[CAL:Bowles Tax Planning]` `[CAL:Bowles 2025 Estimates]`

---

## §9. Opportunity Flags (auto-detected)

| Flag | Trigger | Confidence | Action | Source |
| --- | --- | --- | --- | --- |
| **S-Corp — HIGH** | SE-only income ~$51.5K/spouse from Clayhouse; zero payroll; combined ~$260K/yr draw; S-Corp election structurally feasible via holding co | HIGH | CHMMB Holdings LLC formation — advance immediately | `[CAL:Bowles Tax Planning]` |
| **Amended Return — HIGH** | 2024 SE tax computation error identified; ~$6,545 overpayment; 3-year statute of limitations on refund | HIGH | File 1040-X for 2024 | `[CAL:Bowles 2025 Estimates]` |
| **IRS Risk — HIGH** | 2022/2023 installment (~$70K); 2024 CP14 (~$65.5K); balance status unconfirmed; zero withholding pattern ongoing | HIGH | Confirm clearance; advise on proactive payment structure | `[CAL:Bowles 2025 Estimates]` |
| **Cost Seg — NOT APPLICABLE** | No real estate identified in file | LOW | Probe at planning call | `[CAL:Bowles Tax Planning]` |
| **K-1 Mismatch — MEDIUM** | $6,303 discrepancy between Logan and Michelle K-1 amounts on 50/50 partnership | MED | Pull 2024 Clayhouse 1065 K-1 schedules; reconcile | `[CAL:Bowles 2025 Estimates]` |
| **Passive Loss Classification — MEDIUM** | Clay Construction ~$75K loss; passive classification uncertain; material impact on 2025 estimate | MED | Confirm at planning call | `[ExecSum §Activity Log]` |

**Classifier notes:**
- S-Corp classifier: **FIRES HIGH** — SE-only draw income with no payroll is the textbook trigger condition `[CAL:Bowles Tax Planning]`
- Cost Seg classifier: **BLOCKED** — no Reporting Entities or property records on Account; probe for real estate at planning call `[Accounts §Reporting Entities]`

---

## §10. Operations Analysis

**Engagement Health: ELEVATED CONCERN.** This is a Jan 2026 onboard with a signed EL, sent memo, but a stalled planning sequence and a client relationship under stress.

**Timeline of key events:**

| Date | Event |
| --- | --- |
| 2026-01-29 | EL signed |
| 2026-01-30 | Batch added to compliance tracker |
| 2026-02-03 | PBC list sent |
| 2026-02-10 | Tax Memo sent |
| 2026-03-15 | S-Corp election deadline **missed** |
| 2026-04-09 | Claude sessions: full tax analysis both Bowles accounts; extension email sent with overstated ~$65K figure |
| 2026-04-13 | Sophia updated workspace file path (internal Notion note) |
| 2026-04-17 | Pending meeting row: "Michelle R Bowles" (orphan — no account linked, no recap) |
| 2026-05-07 | **This dossier refresh** |

**Operational concerns:**
1. **Response gap**: Memo sent 2/10 → no planning call through 5/7 = 87 days. Either the client has been unresponsive (post-extension-email shock may explain April silence) or the call was not proactively booked. Either way it's a risk.
2. **PBC docs**: Nothing received since 2/2/2026 — 94 days. Client onboarding stalled.
3. **Extension email error**: $65K overstated vs ~$19.5K actual is a 3.3x overstatement. This caused client shock per Claude activity log. If not corrected before the planning call, it will undermine trust in the entire engagement.
4. **IRS delinquency pattern**: Multiple years of underpayment suggest the client has structural cash-flow / withholding issues. The Accruity value-add here is building a forward withholding/quarterly-payment structure — not just filing returns.
5. **Cross-account complexity**: The shared Clayhouse/Clay Construction entity stack means Michelle's and Logan's returns are interdependent. Any 1065 amendment or restructuring on Clayhouse affects both. Coordinate planning across accounts.
6. **Positive signal**: Client signed at $3,675 (higher than Logan's $1,525), accepted portal invite, and portal access was checked 3/16. Client is engaged at the onboarding level.

**Recommended next actions in priority order:**
1. Correct extension email error → repair trust
2. Book planning call (may have happened 4/17 — confirm from orphan meeting row)
3. Chase PBC docs
4. Advance CHMMB Holdings LLC + S-Corp election
5. Amend 2024 return for SE error

---

## §11. Individual Profiles

### §11.1 Michelle Bowles (aka Michele Bowles)

- Primary taxpayer on this Accruity record
- 50% partner in Clayhouse Mortgage LLC (alongside Logan Bowles)
- MFJ filer with Jason
- IRS delinquency history: 2022/2023 installment plan (~$70K); 2024 CP14 (~$65.5K; $40K payment applied, status assume cleared but unconfirmed)
- 2024 SE tax overpayment ~$6,545 — amendment candidate
- Reaction to extension email (4/9/2026): expressed **shock** at the numbers — indicates either she did not anticipate the tax liability or the overstated $65K figure was genuinely alarming; both scenarios require proactive communication to retain trust
- No email correspondence on file (the one email log entry is a Notion system notification, not client communication)
- Name appears as both "Michelle" and "Michele" across records — standardize in future communications

### §11.2 Jason Bowles

- Spouse / co-filer
- Also SE-income partner from Clayhouse Mortgage LLC (~$51.5K SE base per spouse)
- Zero payroll/withholding alongside Michelle — the same structural SE exposure applies to both
- No separate profile data available this refresh; appears in shared Claude analysis
- Full name referenced: "Jason Michelle Bowles" is account name (confirms Jason = first name of husband)

### §11.3 Relationship Dynamic

- Both Michelle and Jason draw from Clayhouse Mortgage LLC with no payroll structure — creating recurring underpayment risk
- Historical delinquency pattern (2022 → 2023 → 2024 CP14) suggests systemic underpayment rather than one-off events
- The S-Corp election is both a tax savings strategy AND an opportunity to introduce a payroll structure that prevents future underpayments

---

## §12. Provenance Index

### Notion — Account & DB rows

- `[Accounts:Jason Michelle Bowles]` → [notion.so/329491728751806799d2f1c4471ce13b](https://www.notion.so/329491728751806799d2f1c4471ce13b)
- `[Accounts:Logan Bowles]` → [notion.so/30d491728751816d9949f6a4a7f23141](https://www.notion.so/30d491728751816d9949f6a4a7f23141) (cross-reference only)
- `[ExecSum:Jason Michelle Bowles]` → [notion.so/33d4917287518117a5cef78a3b01819d](https://www.notion.so/33d4917287518117a5cef78a3b01819d) (existing row — empty body, Activity Log pre-populated by prior session)
- `[EL:Jason Michelle Bowles]` → [notion.so/2ef49172875180c2af03f3c21c76ac76](https://www.notion.so/2ef49172875180c2af03f3c21c76ac76) — Signed/Executed/$3,675
- `[TaxAscend:Michelle Bowles]` → [notion.so/314491728751802f9e12f0760e62c2b7](https://www.notion.so/314491728751802f9e12f0760e62c2b7) — Tax Planning + Compliance; Memo Sent 2026-02-10
- `[TaxAscend:Logan Bowles]` → [notion.so/2f749172875180759609f32f1c5d4949](https://www.notion.so/2f749172875180759609f32f1c5d4949) (cross-reference — Tax Memo URL collision check)

### Notion — Claude Activity Log (2 entries, cross-account)

- `[CAL:Bowles Tax Planning]` = `[CAL:33d4917287518110adc7d8076a84d8d9]` → [notion.so/33d4917287518110adc7d8076a84d8d9](https://www.notion.so/33d4917287518110adc7d8076a84d8d9) — "Project — 2026-04-09 — Bowles Tax Planning & Structure Review"
- `[CAL:Bowles 2025 Estimates]` = `[CAL:33e4917287518184b1adcd8855a92c66]` → [notion.so/33e4917287518184b1adcd8855a92c66](https://www.notion.so/33e4917287518184b1adcd8855a92c66) — "Project — 2026-04-09 — Bowles 2025 Tax Estimates, Extraction Review & IRS History"
- Claude chat thread (both sessions): [claude.ai/chat/6b78c98d-3cc6-41ab-9b07-a4d6a85099ad](https://claude.ai/chat/6b78c98d-3cc6-41ab-9b07-a4d6a85099ad)

### Notion — Client Email Log (1 entry)

- `[EmailLog:342491728751816a911edda241785a0e]` → [notion.so/342491728751816a911edda241785a0e](https://www.notion.so/342491728751816a911edda241785a0e) — "Sophia@accruity commented in Jason Michelle Bowles" (2026-04-13, internal Notion notification, low risk)

### Notion — Meetings Tracker

- `[Meeting:Michelle R Bowles]` → [notion.so/349491728751807e964de541607dd502](https://www.notion.so/349491728751807e964de541607dd502) — 2026-04-17, Pending, no account link, no recap (orphan row — assign to Jason Michelle Bowles account)

### Exec Summary Activity Log (pre-existing)

- `[ExecSum:Jason Michelle Bowles §Activity Log]` → body of [notion.so/33d4917287518117a5cef78a3b01819d](https://www.notion.so/33d4917287518117a5cef78a3b01819d) — 2026-04-09 activity note referencing same Claude session

### SharePoint / Mangoshare

- Signed EL: [app.mangoshare.com/share/f1a2bbd1dc838675b2bbc1a1](https://app.mangoshare.com/share/f1a2bbd1dc838675b2bbc1a1)
- PBC folder (imaginetime): [imaginetime.com/firm/5331/workspaces/937719/files/18474205/folder](https://app.imaginetime.com/firm/5331/workspaces/937719/files/18474205/folder) ⚠️ workspace 937719 may be Logan's — verify
- PBC list xlsx: [SharePoint](https://subledgesl-my.sharepoint.com/:x:/g/personal/seth_accruity_com/IQBhuvdyU8rtS7KwsogxazWMActThbaZXT05Ne95zy1xDA0?e=zbYtSf)
- Tax Memo (URL 1): [SharePoint .docx](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQD9rbWDMxRqSolklj0o7s6LAXl_lwVofg4X-CY0jkk3kCc?e=5c4sW5) ⚠️ same URL as Logan — verify
- Tax Memo (URL 2): [SharePoint .docx](https://subledgesl-my.sharepoint.com/:w:/g/personal/seth_accruity_com/IQBf4C6HuNzmQ6WfTPv2Ni8QAYyQJMMnVb5sEa3yiSv2kUM?e=nYHQ6L) ⚠️ same URL as Logan — verify

### Cross-dossier reference

- `[ExecSum:Logan Bowles]` → [notion.so/33b49172875181789ea0d7e9101ee49d](https://www.notion.so/33b49172875181789ea0d7e9101ee49d) — Logan's Exec Summary (Tax Planning row with rich activity log content; highly relevant for Clayhouse entity context)

---

## §13. Changed Since Last Refresh

**This is the first comprehensive refresh.**

### 13.1 · 2026-05-07 · First-run baseline

**New — facts integrated:**
- Joint Accruity household confirmed: Michelle Bowles (MFJ with Jason) + Clayhouse Mortgage LLC 50% K-1 — **distinct account** from Logan Bowles (separate household, separate filer)
- Engagement scope: $3,675 EL Signed/Executed; Tax Ascend Planning + Compliance; Tax Memo sent 2026-02-10; planning call NOT yet scheduled
- **2025 estimated tax ~$19,490** (MFJ) after Clay Construction (~$75K) passive offset against ~$178K Clayhouse K-1; SE ~$51.5K/spouse
- **Extension email error identified**: ~$65K overstated vs ~$19.5K actual; client expressed shock — HIGH urgency to correct
- **2024 SE tax overpayment ~$6,545** — amendment opportunity identified from Claude 4/9 session
- IRS delinquency history: 2022/2023 (~$70K installment) + 2024 CP14 (~$65.5K, $40K payment applied, status unconfirmed)
- CHMMB Holdings LLC formation in progress (S-Corp path); ~$16–20K/yr projected SE savings for Michelle
- Orphan meeting row (2026-04-17, "Michelle R Bowles") found — not linked to account

**New — discoveries:**
- ⚠️ **Mango Client ID missing** on Account record; imaginetime workspace 937719 in EL PBC link matches Logan Bowles' Mango ID — possible data entry error
- ⚠️ **Tax Memo URL collision** — Michelle and Logan Tax Ascend rows reference identical SharePoint Tax Memo URLs; verify if intentional
- ⚠️ **0 PBC docs received** since list sent 2/2/2026 (~94 days); 0 client emails on file
- 2 prior Claude sessions (4/9/2026) are cross-account (cover both Bowles households simultaneously)
- Clayhouse Mortgage LLC 1065 **rejected** at Virtueshore — impacts both Logan and Michelle K-1 accuracy
- $6,303 K-1 mismatch between Logan and Michelle on purported 50/50 partnership

**Strategic theme:** New client, operationally stalled. The extension email error created a trust rupture that must be repaired before any productive planning conversation. S-Corp formation is the primary lever (~$16–20K/yr SE savings). IRS delinquency history adds urgency to also building a forward withholding structure. The cross-account complexity (shared Clayhouse entity with Logan) means Michelle's return cannot be finalized in isolation.

### 13.2 Carry-over summary

| Count | Bucket | Reference |
| --- | --- | --- |
| 16 | Open action items (3 HIGH, 9 MED, 4 LOW) | §7 |
| 0 | Meetings on file (1 orphan Pending row, not linked) | §4 |
| 0 | Files & Links rows on account | §5.3 |
| 2 | Claude Activity Log sessions (cross-account, 4/9/2026) | §6 |
| 1 | Client email thread (internal Notion notification only) | §3 |
| 3 | HIGH opportunity flags (S-Corp, Amended Return, IRS Risk) | §9 |

### 13.3 What a reader should look at first

1. **§7 Actions #1–3** (HIGH): Extension email correction, planning call scheduling, 2024 amendment — all are URGENT
2. **§9 Opportunity Flags** — S-Corp (~$16–20K/yr) and 2024 amendment (~$6.5K) are immediate, concrete deliverables
3. **§8.1 Strategy #3** (Clay Construction passive classification) — material impact on 2025 estimate; resolve at planning call
4. **§5.1 Mango ID flag** — workspace 937719 may be misattributed to Michelle; verify before any portal-based document delivery

---
*Internal document — not for client distribution.*
*Accruity · www.accruity.com*
*Source: [dossiers/MichelleBowles/dossier.md](.) on branch `claude/update-exec-summary-notion-118m7`*
*First generated: 2026-05-07 · Depth mode: MEDIUM (2 rich Claude Activity Log sessions; EL data; Tax Ascend; 0 meetings linked; 1 email thread — internal only) · Next refresh: trigger on planning call completion OR 2024 amendment filed OR S-Corp formation milestone*
