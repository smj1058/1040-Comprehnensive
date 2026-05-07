# Tate Cline — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | Tate Cline (KNRS Properties LLC · BRC Dispositions · KR&S Properties) |
| Client # | `20050305-01` `[Accounts:Tate Cline.Client #]` |
| Mango Client ID | `937757` `[Accounts:Tate Cline.Mango Client ID]` |
| Prepared by | Accruity Tax Advisory |
| Date | 2026-04-22 |
| Prior Refresh | first run |
| Planning Year(s) | 2024 (extraction baseline), 2025 (active extension), 2026 (forward) |
| Engagement Stage | Tax Ascend — Compliance + Planning + Cost Seg (stalled) + S-Corp election (planned) |
| Temperature | Active & engaged · **HIGH urgency** (Apr 15 extension cycle, cost-seg intake stalled, 11 open items) |
| Relationship Manager | Seth Johnson (billing partner) |
| Senior Manager (Billing Partner) | Ryan Walsh `[Mango:Tax Planning - Tate Cline]` |
| Tax Planning Manager | Sophia (Tax Admin); Seth (Manager) `[Mango New DB:Tax Planning - Tate Cline]` |
| Primary Contact | Tate Cline — `knrspropertiesllc@gmail.com` · `(614) 456-6451` `[Accounts:Tate Cline.Client Contacts]` |
| Spouse / Co-filer | Whitney Cline (per Mango project name "1040 - Tate & Whitney Cline") `[Mango:1040 - Tate & Whitney Cline]` |
| Data Sources (this refresh) | Notion Account record · 6 Meetings Tracker rows (5 done, 1 cancelled, 1 rescheduled) · 1 Engagement Letter row (signed, $5,350) · 3 Files & Links rows · 4 Email Log rows (3 misclassified noise + 1 vState) · 2 Cost Seg Proposal Intake rows · 1 Tax Ascend row · 1 Insights Project · 1 Tax Planning Session · 2 Exec Summary DB rows (1 canonical + 1 duplicate flagged) · 1 prior Claude Summary · 1 Cost Seg Pipeline session (cross-client) · 2 Mango DB rows · S-Corp Election Tracker row · Delivery call transcript (84 min) |
| Files NOT Accessible This Refresh | PBC Workbook (URL empty), Tax Extraction (URL empty), SharePoint Drive (URL empty), Tax Planning Memo (URL empty on Account, but exists per Tax Ascend record), Meeting Prep Notes (URL empty) — flagged for §5 |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag. See §12 Provenance Index at the end.

---

## §1. Executive Overview

Tate Cline (`knrspropertiesllc@gmail.com` · `(614) 456-6451`) is an **Ohio real-estate investor & operator** running a multi-vertical small-business stack: **KNRS Properties LLC** (rental holding entity), **BRC Dispositions** (property flipping — currently NOT formally an S-Corp, triggering self-employment tax exposure), **KR&S Properties** (rental portfolio operations), plus a small "cooking class" side venture. Files MFJ with spouse **Whitney Cline**. `[Mango:1040 - Tate & Whitney Cline]` `[Transcript:Delivery Call 2026-02-10]`

**What matters right now — Apr 15 extension cycle is HIGH urgency and the cost-seg pipeline has STALLED.** Per the most recent Claude session (2026-04-13), extension estimate was modeled at **`$0` payment IF REPS + cost seg are applied** (yielding ~$90K suspended losses + $67.5K accelerated depreciation), but **`$25K+` balance due if those strategies fall through**. `[ClaudeSumm:Tate Cline — Extension Estimate Consolidation 2026-04-13]` The cost-seg track has a **critical execution gap**: only **111 Hancock St** (KNRS Properties · $200K purchase price · 1,584 sq ft single-family rental in Delaware, OH 43015 · placed in service 2021-05-20) was entered into the RE Cost Seg portal on 2026-04-02 — and even then, the parent intake row "Cline — Cost Seg" still shows status `New - Enter in Portal` `[CostSegProposal:Cline — Cost Seg]`. **365 Garfield was never entered at all.** `[ClaudeSumm:Extension Estimate Consolidation §Discovery]`

**Three engagement tracks are simultaneously active:**

1. **2025 Compliance + Extension** — Engagement Letter signed (`$5,350`) on 2026-02-24 batch; deposit paid; Mango portal invite sent; PBC list received. Extension email sent to Tate 2026-04-09 with two scenarios. Open Items List status: "Client feedback" (awaiting Tate's response). `[EL:Tate Cline 2026-02-24]` `[TaxAscend:Tate Cline.Compliance Status]`
2. **Tax Planning Memo Track A** — Memorandum issued 2026-03-05 (`Tax_Planning_Memorandum_Tate_Cline_2026.docx`) projecting **`$55,000` annual tax savings** across 6 strategies driven by org-chart restructure (rental partnership holdco + S-Corp operating holdco), REPS qualification, cost segregation, Solo 401(k), Augusta Rule, employing children, and accountable plan. Tax planning session delivered 2026-04-02. `[ExecSumm:Tate Cline.Activity Log 2026-03-03]` `[TaxPlanningSession:Tate Cline 2026-04-02]`
3. **S-Corp Election (planned)** — 2553 election flagged in S-Corp Election Tracker with status `Planned` and next action "Advance S-Corp election plan". Target effective date not yet set. `[SCorpTracker:Tate Cline 2026-04-22]`

**Cost segregation track — exceptionally active opportunity but executionally STALLED.** Tate appeared as one of **8 named clients in the cross-client 2026-04-08 "Cost Seg Pipeline — Property Lists, File Inventory & Follow-Up Tracker" Claude session** (alongside Tommy Harr, Andy Karabinos, Augustine, Dan Hamilton, Gil Ramos, Michael Venereo, Matt Iannaccio, Lacey Blackman, Brett Zanotto, Tanya Toliver, Renee Mueller, Randy Wolfe). `[ClaudeSumm:Cost Seg Pipeline 2026-04-08]` Tate has only **2 Cost Seg Proposal Intake rows on Account** (vs Tommy Harr's 13), but the active 2025 strategy depends on the cost seg deductions hitting before extension filing — and the intake gap (111 Hancock entered but parent row not advanced; 365 Garfield missing entirely) is the single highest-leverage execution risk this week. `[Accounts:Tate Cline.Cost Seg Proposals]`

**Property structure (per delivery call 2/10).** Discussion identified **4 of 6 properties on land contracts** with **2 transitioning to rent-to-own**, and that all rental properties currently flow to Tate's personal return — increasing IRS audit risk and blocking entity-level liability isolation. The proposed restructure: a partnership-holding company owning all rental LLCs (single K-1 to Tate's 1040) plus an S-Corp holding company over the active operating businesses. `[Transcript:Delivery Call 2026-02-10 §Solution]`

**Coverage model.** Seth Johnson is billing partner & Manager. Ryan Walsh is Senior Manager (per Mango). Sophia is admin Manager on the Tax Planning project. Bryan Szpindor and Alex Orosz appeared on the 2/10 delivery call (Alex sent calendar invite for 1:30 PM same-day pricing meeting; Bryan committed to sending slide deck and meeting recording). `[Transcript:Delivery Call 2026-02-10 §Next Steps]`

**Current refresh gaps.** PBC Workbook URL, Tax Extraction URL, Tax Planning Memo URL, and SharePoint Drive URL are all empty on the Account record, but the underlying files are referenced from the Tax Ascend record (`Tax_Memo_URL` SharePoint link, `Cline_analysis_2024.xlsm` analysis file attached). The Account record needs URL backfill on next refresh. The 2026-04-13 Claude session also flagged **11 open items** awaiting Tate's response — those drive §7. `[Accounts:Tate Cline]` `[TaxAscend:Tate Cline]`

**Bottom-line urgency.** This week's blockers, in priority order:
- (HIGH) Submit "Cline — Cost Seg" parent intake to RE Cost Seg portal so 111 Hancock can yield estimated savings before extension is filed
- (HIGH) Capture 365 Garfield property data and create second Cost Seg Proposal Intake row
- (HIGH) Receive Tate's response to Open Items List (Compliance Status: "Client feedback") and Apr 9 extension scenarios email
- (MED) Finalize $0-vs-$25K extension scenario decision and file Form 4868 by Apr 15
- (MED) Reconcile Tax Planning Memo strategies with extension assumptions to ensure REPS facts-and-circumstances test will hold

---

## §2. Client Profile

| Item | Value | Confidence | Source |
| --- | --- | --- | --- |
| Filing status | MFJ — Tate & Whitney Cline | ✓ | `[Mango:1040 - Tate & Whitney Cline]` |
| Residency | Ohio (Delaware, OH 43015 rental property; Columbus area phone 614) | ✓ | `[CostSegProposal:111 Hancock St]` `[Contact:Tate Cline.Phone]` |
| Client # | `20050305-01` | ✓ | `[Accounts:Tate Cline.Client #]` |
| Mango Client ID | `937757` | ✓ | `[Accounts:Tate Cline.Mango Client ID]` |
| Mango Display Name | (blank — falls back to Account Name "Tate Cline") | ❌ | `[Accounts:Tate Cline.Mango Display Name]` |
| Primary Contact | Tate Cline · `knrspropertiesllc@gmail.com` · `(614) 456-6451` | ✓ | `[Contact:Tate Cline]` |
| Spouse / Co-filer | Whitney Cline | ✓ (~ on contact details — no separate Notion contact row) | `[Mango:1040 - Tate & Whitney Cline]` |
| Portal Access | `__NO__` (no Notion portal access flag) | ❌ | `[Contact:Tate Cline.Portal Access]` |
| Email address roll (Email addresses tracker) | `knrspropertiesllc@gmail.com` | ✓ | `[EmailAddrs:Tate Cline 2026-02-03]` |
| Senior Manager (Billing Partner) | Ryan Walsh | ✓ | `[Mango:Tax Planning - Tate Cline]` |
| Manager / Billing Partner | Seth Johnson | ✓ | `[Mango New DB:Tax Planning - Tate Cline]` |
| Tax Admin Manager | Sophia | ✓ | `[Mango New DB:Tax Planning - Tate Cline]` |
| Account-level Tax Ascend type | Tax Compliance + Tax Planning | ✓ | `[TaxAscend:Tate Cline.TAX ASCEND TYPE]` |
| Engagement Stage | Compliance signed · Planning Memo delivered · Extension in progress · Cost Seg intake stalled · S-Corp election planned | ✓ | composite |
| Temperature | Active & engaged · **HIGH urgency** (Apr 15 extension, intake stall, 11 open items) | ✓ | `[ClaudeSumm:Extension Estimate Consolidation]` |
| Engagement Letter on file | `Tate_Cline_EL` — Signed · Deposit Paid · Price `$5,350` · Mango Portal Invite Sent · PBC items received | ✓ | `[EL:Tate Cline 2026-02-24]` |
| Insights Project | FULL INSIGHTS · Status `Delivered` (delivered 2026-02-10) · Insights Status `Delivered` · Tax Insights `Not started` (extraction backlog) | ✓ | `[InsightsProject:Tate Cline]` |
| Tax Planning Session | Meeting 1 delivered 2026-04-02 (10:30–11:00 AM, otter.ai recording on file) · Status `step 6 (meeting delivered)` · Mango task `Completed` | ✓ | `[TaxPlanningSession:Tate Cline]` |
| S-Corp Election | Status `Planned` · Type 2553 · Last touch 2026-04-22 · Next action: "Advance S-Corp election plan" | ✓ | `[SCorpTracker:Tate Cline]` |
| IRS posture | None disclosed in available sidecars (no IRS balance flagged in Tax Ascend or Email Log) | ~ | derived (absence of evidence) |

### Principals at a glance

- **Tate Cline** — Operator/principal across KNRS Properties LLC (rental holding) · BRC Dispositions (flipping) · KR&S Properties (rentals). Real-estate investor running a multi-property portfolio (4 of 6 on land contracts, 2 going rent-to-own per 2/10 delivery call). Likely qualifies for **Real Estate Professional (REPS) status for 2025** per Seth's view on the delivery call. `[Transcript:Delivery Call 2026-02-10 §Solution]`
- **Whitney Cline** — Spouse / co-filer on the joint 1040. No standalone Notion contact row this refresh; gap to backfill. `[Mango:1040 - Tate & Whitney Cline]`

### Entity stack (provisional — reconcile with PBC on next refresh)

`[Transcript:Delivery Call 2026-02-10]` `[CostSegProposal:111 Hancock St.Business Associated With]`

| Entity | Federal Form (estimated) | Role | Status this refresh | Source |
| --- | --- | --- | --- | --- |
| **KNRS Properties LLC** | TBD — currently flow-through to 1040 (likely SMLLC/disregarded or partnership) | Rental holding entity (per Cost Seg intake "Business Associated With") | Active rental owner | `[CostSegProposal:111 Hancock St]` |
| **BRC Dispositions** | Currently NOT formally an S-Corp — triggering SE tax | Property flipping operating business | Active flipping; **S-Corp election proposed** | `[Transcript:Delivery Call 2026-02-10 §Problem]` `[SCorpTracker:Tate Cline]` |
| **KR&S Properties** | Rental partnership (TBD) | Rental portfolio operations | Active | `[Transcript:Delivery Call 2026-02-10 §Solution]` |
| **"Cooking class" side venture** | TBD | Active operating business mentioned on 2/10 call | Active | `[Transcript:Delivery Call 2026-02-10 §Solution]` |
| **(Proposed) New Rental Partnership Holdco** | 1065 partnership | Single K-1 wrapper around all rental LLCs | Proposed (planning memo) | `[Transcript:Delivery Call 2026-02-10 §New Org Chart]` |
| **(Proposed) New S-Corp Holdco** | 1120-S | Owns active businesses (flipping, cooking class) | Proposed (planning memo) | `[Transcript:Delivery Call 2026-02-10 §New Org Chart]` |

### Property inventory (partial — per Cost Seg pipeline & 2/10 delivery call)

`[ClaudeSumm:Extension Estimate Consolidation]` `[CostSegProposal:111 Hancock St]`

| Property | Owner Entity | Purchase Price | Year Built | Placed in Service | Sq Ft | Cost Seg Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **111 Hancock St, Delaware OH 43015** | KNRS Properties LLC | `$200,000` | 2003 | 2021-05-20 | 1,584 | **Entered in Portal 2026-04-02** (parent intake row still says "New - Enter in Portal" — execution gap) | `[CostSegProposal:TC.111 hancock st]` |
| **365 Garfield** | TBD | TBD | TBD | TBD | TBD | **NEVER ENTERED** in Cost Seg Proposal Intake (gap flagged 2026-04-13) | `[ClaudeSumm:Extension Estimate Consolidation §Discovery]` |
| (4 others on land contracts; 2 transitioning to rent-to-own) | TBD | TBD | TBD | TBD | TBD | Not yet in Cost Seg pipeline | `[Transcript:Delivery Call 2026-02-10]` |

### Third parties in the file

| Party | Role | Status / Notes |
| --- | --- | --- |
| Bryan Szpindor (Accruity) | Insights delivery presenter on 2/10 call | Committed to sending slide deck + recording `[Transcript:Delivery Call 2026-02-10 §Next Steps]` |
| Alex Orosz (Accruity) | Pricing/sales follow-up | Sent calendar invite for 1:30 PM same-day proposal review (2026-02-10) `[Transcript:Delivery Call 2026-02-10 §Next Steps]` |
| Katie (unspecified) | Bookkeeping / spreadsheet workstream | "Push Katie to finish spreadsheet" appeared in 4/13 Email Log noise — **likely misclassified to Tate's account** (this came from Gary Aronov thread) `[EmailLog:FW Recap realestategoto.com]` |

---

## §3. Email Intelligence

**Note on data quality:** 4 email log rows are linked to Tate Cline's Account, but **3 of the 4 are misclassifications** — they are forwarded Fathom recaps for OTHER clients (Wolfe/Wilkes Southern Visions, Gary Aronov realestategoto.com, vState Filings) that the Email Log auto-tagger erroneously associated with Tate's record. Only the **vState Filings** row may have a partial connection (cost seg intake form mention). All four were forwarded by Seth from `seth@accruity.com` to `tax@accruity.com` on the same day (2026-04-13) as part of a bulk forward. `[EmailLog:Tate Cline.4 rows 2026-04-13]`

### 3.1 Active threads — substantive Tate-specific correspondence

`[ExecSumm:Tate Cline.Activity Log]`

| Date | Direction | Subject / Channel | Synopsis | Status |
| --- | --- | --- | --- | --- |
| 2026-04-09 | Outbound (Accruity → Tate) | "21 - Tate Cline - Sent.msg" — extension email | **Extension scenarios sent**: $0 payment if REPS + cost seg apply (~$90K suspended losses + $67.5K depreciation); $25K+ balance due otherwise. Confirmation questions included. | `[Activity Log 2026-04-09]` Awaiting Tate response |
| 2026-04-21 | Outbound (Accruity team) | "Fw: Tate Cline - Open Items + Tax Plan Follow Up.msg" attached to EL row content | Internal forward of Open Items List + Tax Plan follow-up correspondence | `[EL:Tate Cline.Open Items Email block]` |
| 2026-03-05 | Outbound (Accruity → Tate) | Tax Planning Memorandum sent | `Tax_Planning_Memorandum_Tate_Cline_2026.docx` delivered (SharePoint: Client Files/Cline, Tate/Tax Planning/) | `[Activity Log 2026-03-03]` `[TaxAscend:Tate Cline.Tax Memo Sent 2026-03-05]` |
| 2026-03-10 | Outbound (Accruity → Tate) | Extension email | Per EL row "Date EXT EMAIL sent 2026-03-10" — earlier extension touch | `[EL:Tate Cline.Date EXT EMAIL sent]` |

### 3.2 Misclassified noise to be routed/cleaned

| Email Log Row URL | Real Client | Recommended Action |
| --- | --- | --- |
| `https://www.notion.so/3424917287518144a4fed005ba5477b5` "FW: Recap of your meeting with Southern Visions Real Estate" | Doug Wilkes / Randy Wolfe (Southern Visions) | Re-link Account from Tate Cline → Randy Wolfe / Doug Wilkes Account |
| `https://www.notion.so/34249172875181dca589ecb01817fe48` "FW: Recap of your meeting with realestategoto.com" | Gary Aronov / Jeremy | Re-link Account from Tate Cline → Gary Aronov Account |
| `https://www.notion.so/342491728751816f8095e06804080bc2` "FW: Recap of your meeting with vState Filings" | vState Filings (entity formation vendor) — possibly Tate-relevant via cost seg intake form mention but ambiguous | Verify; if unrelated, unlink from Tate |
| `https://www.notion.so/34249172875181ba9110ffe4f537ac42` "Declined: Stacy<>Seth<>Sophia" | Internal calendar decline notice — not client-relevant | Unlink from Tate |

### 3.3 Communication channels in use

- **Primary email**: `knrspropertiesllc@gmail.com` (Gmail; standalone — not on a custom domain)
- **Phone**: `(614) 456-6451`
- **Outbound .msg files** stored in SharePoint: `Extensions/2025/4.15 Deadline/Correspondence/` and `Client Files/Cline, Tate/Tax Planning/` `[ExecSumm:Tate Cline.Activity Log]`

### 3.4 Gaps to backfill

- No inbound emails from Tate captured in Email Log this refresh — likely a Make.com pipeline gap (only outbound + misclassified inbound noise present).
- Tate's response to the 2026-04-09 extension email (with scenarios + confirmation questions) is missing from the log — either not received yet, or received and not yet ingested.

---

## §4. Meeting History

`[Meetings Tracker:Tate Cline · 6 rows]`

| # | Date | Type | Status | Time | Recap | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-01-06 | Touchbase | ✓ Done | 11:30 AM – 12:00 PM EST | [Fathom recap](https://fathom.video/share/8Bcy57djsfWvgSB1bYWExzStwDNFTpZT) | "Ask Bryan if required to be on this call" `[Meetings:2fb49172...80db]` |
| 2 | 2026-01-22 | Full Insights — Clarification call | Cancelled (per `NOTES`) | 10:30–11:30 AM EST | (none — cancelled) | Status still `Pending` on row, but notes say "cancelled" `[Meetings:2fb49172...80a1]` |
| 3 | 2026-01-29 | Full Insights — Clarification call | ✓ Done | 10:30–11:30 AM EST | [Fathom recap](https://fathom.video/share/TE7u7AYpZPv6ExW_jyKhstgH1K1cmZ4N) | "Ask Bryan if required to be on this call" `[Meetings:2fb49172...8007]` |
| 4 | 2026-02-10 | Full Insights — **Delivery call** | ✓ Done | (no time set) | [Fathom 84 min](https://fathom.video/share/84s4-kehxdHgjPzuLvYwz3GuPQN-YPR1) — **transcript on file** as Notion subpage `31849172875180d1b91af6659c05f5ca` | Scheduled delivery, no calendar invite. Bryan Szpindor + Alex Orosz attended. `[Meetings:30449172...8038]` `[TaxAscend:Tate Cline.Insights Delivery Meeting Recap]` |
| 5 | 2026-03-20 | Tax Planning Session | Rescheduled | 12:30–1:00 PM EST | (none — moved to 4/02) | Rescheduled to 2026-04-02 `[Meetings:32949172...80a0]` |
| 6 | 2026-04-02 | **Tax Planning Session** | ✓ Done | 10:30–11:00 AM EST | [otter.ai recording](https://otter.ai/u/BemfyEI1XyJqUh2A5NODAMhN2O0?utm_source=copy_url) | INVITE CONFIRMED. Memo discussed. `[Meetings:33549172...805e]` `[TaxPlanningSession:Tate Cline.Meeting 1]` |

### 4.1 Key meeting takeaways — 2/10 Delivery Call (84 minutes)

`[Transcript:Delivery Call 2026-02-10]`

**Meeting Purpose**: Review Tate's business financials and propose strategic back-office and tax plan.

**Tax Savings**: New org chart and tax plan could save up to **`$55,000` annually**, primarily via SE-tax elimination through S-Corp restructure + REPS-status accelerated depreciation to offset active flipping income.

**Financial Clarity**: Correcting BRC Dispositions accounting (treat properties as inventory, capitalize purchase + rehab costs on balance sheet until sale) will replace the current misleading **`$1,000,000` annual loss** in QuickBooks with true project-level profitability.

**Strategic Growth**: Monthly reporting will track DSCR for rentals + project-level margins for flips, enabling data-driven refinance and viability decisions.

**Time Savings**: Outsource bookkeeping (currently year-end manual categorization).

**Identified Problems**:
- Org chart unclear — BRC Dispositions not formally an S-Corp (SE tax exposure); all rental properties flow to personal return (audit risk)
- Back office: manual year-end bookkeeping, no real-time insights, BRC accounting expensing all costs creating misleading $1M loss
- Tax planning: no proactive strategy, missed QBI/REPS/cost seg, no estimated payments → year-end surprises

**Proposed Solution**:
- New rental-portfolio partnership holdco owning all rental LLCs (single K-1 to 1040)
- New S-Corp holdco owning active businesses (flipping + cooking class) — eliminates SE tax via reasonable salary + tax-free distributions
- Capitalize flipping costs as inventory
- Property/entity/portfolio-level rental tracking
- Vendor-level expense detail with ROI by lead source
- REPS qualification for 2025 (Tate likely already qualifies)
- Cost segregation on rentals (est. 20–30% of purchase price as upfront deductions)
- Solo 401(k) under S-Corp holdco (contribution up to ~$70k)
- Low-hanging fruit: Accountable Plan, Augusta Rule, employ children for marketing (~$15k/yr each up to standard deduction)

**Next Steps from 2/10 call**:
- Alex Orosz → calendar invite for 1:30 PM same-day pricing review with Tate
- Bryan Szpindor → send slide deck + meeting recording
- Tate → meet with Alex at 1:30 PM

### 4.2 4/02 Tax Planning Session

`[TaxPlanningSession:Tate Cline.Meeting 1]` — 30-minute session, otter.ai recording captured. Memo follow-up. Status `Completed`. Meetings 2 and 3 not yet scheduled.

### 4.3 Coverage map across meetings

- **Bryan Szpindor** — Lead presenter on Insights delivery (1/29 + 2/10)
- **Alex Orosz** — Pricing/sales handoff on 2/10
- **Seth Johnson** — Billing partner; primary tax advisor on 2/10 + 4/02 sessions
- **Sophia** — Tax admin (mentioned in S-Corp election workflow)

### 4.4 Restricted meetings

None marked Restricted this refresh.

---

## §5. Document Inventory

### 5.1 Engagement Letters (Engagement Letters Tracker)

| EL Row | Status | Price | Mango status | PBC | Notes |
| --- | --- | --- | --- | --- | --- |
| `Tate Cline 2026-02-24 batch` `[EL:3034917287518095a520da84b5870a1c]` | **Signed** · Deposit Paid · Docusign Delivered | `$5,350` | Project Created · Portal Invite Sent · Tag "PBC Request list" | Received PBC items · "Seth - PLENTY FILES SAVED FROM GOOGLE DRIVE. no PBC list included with open items email, no PBC saved in onedrive" | Signed EL on MangoShare; Open Items email forwarded; PBC folder linked to ImagineTime workspace 937757 |

### 5.2 Files & Links rows on Account (3 rows)

| Row | URL | Filled? |
| --- | --- | --- |
| `Engagement Letter` `[F&L:33b491728751811dbacbca1b38476f32]` | All URL fields blank | ❌ shell row |
| `Executive Summary` `[F&L:33b49172875181a39d18ee7ed412d488]` | All URL fields blank | ❌ shell row |
| `Tate Cline` `[F&L:33b491728751810fbb6df96f9abc44a7]` | Document Inventory: SharePoint folder link · PBC PDF Package: SharePoint link | ✓ partial |

**URL Collision Check.** The 3 Files & Links rows linked to Tate Cline's Account are all unique and do not collide with each other on the same `Document Inventory` URL. ✓ No collision.

### 5.3 Platforms in use

- **SharePoint** (subledgesl-my.sharepoint.com / seth_accruity_com tenant): Document Inventory folder, PBC PDF Package, Tax Planning Memo URL, Cost Seg estimate file
- **MangoShare** (`app.mangoshare.com/share/36414a8b2c835c8bbbf72641`): Signed EL
- **ImagineTime** (`app.imaginetime.com/firm/5331/workspaces/937757`): PBC folder
- **Mango Portal**: Client portal invite sent
- **Fathom** (3 meetings recorded)
- **otter.ai** (4/02 tax planning session)

### 5.4 Workbooks NOT linked to Account this refresh

`[Accounts:Tate Cline]` — these fields are EMPTY on the Account:

| Workbook / URL property | Status | Where it actually lives |
| --- | --- | --- |
| PBC Workbook | ❌ empty | Likely in ImagineTime workspace 937757 — not yet linked back to Notion Account |
| Tax Extraction | ❌ empty | Per Insights Project: status `Delivered` but `Tax Insights Not started`. Extraction file exists but is not URL-linked |
| Tax Planning Memo | ❌ empty on Account | Exists per Tax Ascend `Tax Memo URL` SharePoint link: `Tax_Planning_Memorandum_Tate_Cline_2026.docx` `[TaxAscend:Tate Cline.Tax Memo URL]` |
| SharePoint Drive | ❌ empty | Folder exists per F&L row "Tate Cline" Document Inventory link |
| Tax Analysis Workbook | ❌ empty on Account | Exists per Tax Ascend `Cline_analysis_2024.xlsm` attached file `[TaxAscend:Tate Cline.Tax Analysis Files]` |
| Meeting Prep Notes | ❌ empty | Likely in SharePoint Tax Planning folder |

**Backfill task added to next refresh queue**: copy URLs from Tax Ascend + F&L "Tate Cline" row up to Account record so future refreshes pick them up automatically.

### 5.5 Other documents referenced in Activity Log

- `Tax_Planning_Memorandum_Tate_Cline_2026.docx` (sent 2026-03-05) — SharePoint: Client Files/Cline, Tate/Tax Planning/
- `Tate_Cline_Tax_Planning_Prep_Summary_2026.docx` (2026-04-02 prep) — SharePoint
- `21 - Tate Cline - Sent.msg` (2026-04-09 extension email) — SharePoint: Extensions/2025/4.15 Deadline/Correspondence/
- `Tate_Cline_2025_Extension_Estimate.xlsx` (2026-04-13 6-tab workbook) — SharePoint
- `2026-04-13_Tate_Cline_Extension_Estimate.html` (2026-04-13 session detail with full income build-up, tax calc, cost seg status, entity status, strategy screen, 11 open items)

`[ExecSumm:Tate Cline.Activity Log]` `[ClaudeSumm:Extension Estimate Consolidation]`

---

## §6. Claude Work Product

### 6.1 Prior Claude Summaries DB rows tied to Tate

| Date | Title | Topics | Files Reviewed | Output |
| --- | --- | --- | --- | --- |
| 2026-04-08 | **Cost Seg Pipeline — Property Lists, File Inventory & Follow-Up Tracker** (cross-client) | Cost Seg | (cross-client file roll) | Built full cost seg pipeline tracker. Tate listed among 13 named clients. Tate's row noted as having 2 Cost Seg Proposal Intake records (parent + 111 Hancock sub-item). `[ClaudeSumm:33c49172...955549]` |
| 2026-04-13 | **Tate Cline — Extension Estimate Consolidation & Exec Summary Backfill** | Tax Planning · Extension Planning · Cost Seg | Cline_analysis_2024.xlsm; delivery call transcript; extension email; 2x Cost Seg Proposal Intake records; TAX ASCEND; Tax Planning Session; Account; Executive Summary; 3x Mango Planning records; Files & Links; Meetings Tracker | Built 6-tab extension estimate workbook (`$0` payment with REPS+cost seg, `$25K` without). Created HTML session file. **Discovered cost seg intake STALLED — 111 Hancock entered 4/2 but never submitted to RE Cost Seg portal; 365 Garfield not entered at all.** Backfilled Executive Summary page with 4 Activity Log entries. `[ClaudeSumm:34249172...ef60c]` |

### 6.2 Activity Log entries already on Executive Summary page

`[ExecSumm:Tate Cline.Activity Log]`

- **2026-03-03** — Tax Planning Memorandum (TYPE A). Memo from 2024 return extraction + delivery call transcript (2/10) + clarification call (1/29). 6 strategies, **`$55K` total savings**. QBI missed in 2024, BRC accounting errors, no ES payments. Sent 3/5.
- **2026-04-02** — Tax Planning Prep Summary & Call Prep. Full prep summary with entity deep-dive, property-ownership mapping (4/6 on land contracts, 2 going rent-to-own), open items analysis. April 2 planning call delivered.
- **2026-04-09** — Extension Email Sent. **`$0` payment with REPS + cost seg** (`$90K` suspended losses + `$67.5K` depreciation). Without strategies: **`$25K+` balance due**. Email sent to Tate with scenarios + confirmation questions.
- **2026-04-13** — Extension Workbook + Session Consolidation. Built extension estimate workbook (6 tabs). **Discovered cost seg STALLED**: 111 Hancock intake created 4/2 but never submitted to portal; 365 Garfield not entered. HTML session detail created with full analysis.

### 6.3 Claude Activity Log tied to this Account

No additional Claude Activity Log rows were retrieved this refresh beyond the 2 Claude Summaries above. Future refreshes should query `collection://f9cc7d05-26b0-4c77-b29c-af974a234b77` filtered to Account `30d4917287518113aaead67f8bfafece`.

---

## §7. Action Items (Rolled Up Across All Sources)

`[Aggregated from §3, §4, §5, §6 + Cost Seg Pipeline session + 2026-04-13 HTML session detail]`

### 7.1 HIGH — must move this week (Apr 15 extension cycle)

| # | Item | Owner | Source | Due |
| --- | --- | --- | --- | --- |
| H1 | **Submit "Cline — Cost Seg" parent intake row to RE Cost Seg portal** so 111 Hancock can yield estimated savings before extension is filed | Accruity (Cost Seg admin / Sophia / Seth) | `[CostSegProposal:Cline — Cost Seg.Status]` `[ClaudeSumm:Extension Estimate Consolidation]` | 2026-04-14 |
| H2 | **Capture 365 Garfield property data (address, year built, purchase date, placed-in-service, sq ft, building use) and create Cost Seg Proposal Intake row** | Accruity + Tate | `[ClaudeSumm:Extension Estimate Consolidation §Discovery]` | 2026-04-14 |
| H3 | **Receive Tate's response to 2026-04-09 extension email** (scenarios + confirmation questions) | Tate Cline | `[Activity Log 2026-04-09]` `[TaxAscend:Tate Cline.Compliance Status "Open Items List - Client feedback"]` | 2026-04-14 |
| H4 | **File Form 4868 federal extension** (and OH state extension) by Apr 15; pick $0-vs-$25K scenario based on REPS+cost seg confirmation | Accruity Compliance | `[Activity Log 2026-04-09]` | 2026-04-15 |
| H5 | **Resolve 11 Open Items List items** flagged in 2026-04-13 HTML session file | Tate + Accruity | `[ClaudeSumm:Extension Estimate Consolidation]` | 2026-04-14 (rolling) |

### 7.2 MEDIUM — post-Apr 15 deliverables

| # | Item | Owner | Source |
| --- | --- | --- | --- |
| M1 | **Advance 2553 S-Corp election plan** for BRC Dispositions; set target effective date | Seth + Tate | `[SCorpTracker:Tate Cline.Next Action]` |
| M2 | **REPS qualification documentation** — gather hours log to support Tate's REPS claim for 2025 (>750 hours; >50% of personal services in real-property trades) | Tate | `[Transcript:Delivery Call 2026-02-10 §Tax Plan]` |
| M3 | **Capitalize BRC Dispositions flipping costs as inventory** — implement bookkeeping correction to replace misleading `$1M` annual loss with true project-level P&L | Bookkeeping team | `[Transcript:Delivery Call 2026-02-10 §Solution]` |
| M4 | **Stand up new rental-portfolio partnership holdco** (entity formation via vState Filings — possibly the inbound 4/13 email recap relates here) | Seth + entity formation vendor | `[Transcript:Delivery Call 2026-02-10 §New Org Chart]` `[EmailLog:vState Filings recap]` |
| M5 | **Stand up new S-Corp holdco** over active businesses (flipping + cooking class) | Seth + entity formation vendor | `[Transcript:Delivery Call 2026-02-10 §New Org Chart]` |
| M6 | **Set up Solo 401(k)** under S-Corp holdco | Seth + Tate | `[Transcript:Delivery Call 2026-02-10 §Tax Plan]` |
| M7 | **Implement Accountable Plan + Augusta Rule + employ children** | Tate + Bookkeeping | `[Transcript:Delivery Call 2026-02-10 §Low-Hanging Fruit]` |
| M8 | **Schedule Tax Planning Meeting 2 + 3** | Sophia / Tate | `[TaxPlanningSession:Tate Cline.Meeting 2/3 status To check]` |
| M9 | **Backfill Account record URLs** (PBC Workbook, Tax Extraction, Tax Planning Memo, SharePoint Drive, Tax Analysis Workbook) from Tax Ascend + F&L | Internal ops | `[Accounts:Tate Cline]` `[TaxAscend:Tate Cline]` |

### 7.3 LOW — process / hygiene

| # | Item | Owner | Source |
| --- | --- | --- | --- |
| L1 | **Re-link 3 misclassified Email Log rows** (Wolfe/Wilkes, Gary Aronov, Declined: Stacy<>Seth<>Sophia) away from Tate's Account | Internal ops | `[EmailLog:4 rows 2026-04-13]` |
| L2 | **Verify vState Filings email log row** — confirm whether it's Tate-related (cost seg intake form / entity creation) or also misclassified | Internal ops | `[EmailLog:FW vState Filings]` |
| L3 | **Resolve Exec Summary DB duplicate** — `🗑️ DELETE — Tate Cline (duplicate)` row exists; canonical row is `33b49172...9189`. Move duplicate to cleanup queue per BATCH_REFRESH_PROMPT.md rules — DO NOT auto-delete | Internal ops | `[ExecSumm:34249172...d355dd]` `[BATCH_REFRESH_PROMPT.md §Duplicates]` |
| L4 | **Backfill F&L shell rows** — "Engagement Letter" + "Executive Summary" Files & Links rows are completely empty | Internal ops | `[F&L:33b491728751811dbacbca1b38476f32]` `[F&L:33b49172875181a39d18ee7ed412d488]` |
| L5 | **Insights Project — kick off Tax Insights extraction** — status `Not started` despite Insights `Delivered` | Piah (per Insights Project Temp Filter "Piah to do - Extraction and analysis 04/29") | `[InsightsProject:Tate Cline]` |
| L6 | **Add Whitney Cline as separate Notion contact row** (Client Contacts DB) | Internal ops | `[Contact:Tate Cline]` |

---

## §8. Tax Strategies

### 8.1 Strategy table — from 2026-03-03 Tax Planning Memorandum

`[ExecSumm:Tate Cline.Activity Log 2026-03-03]` `[Transcript:Delivery Call 2026-02-10]`

| # | Strategy | Mechanism | Estimated Savings | Status | Confidence | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **REPS (Real Estate Professional) status** | >750 hours + >50% personal services in real property trades; converts rental losses from passive to non-passive to offset active income | Embedded in `~$55K` total memo savings | Proposed for 2025 — likely qualifies | ✓ on framework, `?` on hours documentation | `[Transcript:Delivery Call §Tax Plan]` |
| 2 | **Cost Segregation — 111 Hancock + 365 Garfield (and others)** | Accelerated depreciation (5/7/15-yr property reclassed from 27.5-yr); est. 20–30% of purchase price as upfront deduction | `~$67,500` accelerated depreciation modeled in 4/9 extension scenario; broader pipeline TBD | **Stalled** at intake stage (H1/H2) | ✓ on 111 Hancock numbers, `?` on 365 Garfield | `[ClaudeSumm:Extension Estimate Consolidation]` `[CostSegProposal:111 Hancock St]` |
| 3 | **S-Corp election for BRC Dispositions (Form 2553)** | Convert flipping entity to S-Corp; pay reasonable salary; remaining profits as tax-free distributions → eliminates SE tax | Material — SE tax savings depend on profit; fits the `$55K` memo ceiling alongside REPS | Planned — S-Corp Election Tracker status `Planned` | ✓ on framework | `[SCorpTracker:Tate Cline]` `[Transcript:Delivery Call §New Org Chart]` |
| 4 | **Solo 401(k) under new S-Corp holdco** | Salary deferral up to `$23,500` + employer profit-sharing → contribution potentially up to `~$70K` | TBD — depends on salary set | Planned | ✓ on framework | `[Transcript:Delivery Call §Tax Plan]` |
| 5 | **Accountable Plan** | Reimburse owner for business-use home/auto/phone via S-Corp accountable plan (deductible to corp; tax-free to owner) | TBD | Planned | ✓ | `[Transcript:Delivery Call §Low-Hanging Fruit]` |
| 6 | **Augusta Rule (§280A(g))** | 14-day-or-fewer home rental to corp at FMV — tax-free to owner, deductible to corp | TBD — typical `$5–$15K` range | Planned | ✓ | `[Transcript:Delivery Call §Low-Hanging Fruit]` |
| 7 | **Employ children for marketing** | Wages up to standard deduction (`~$15K/yr` per child); FICA-exempt under sole-prop or family LLC structure | TBD per # of qualifying children | Planned | ✓ | `[Transcript:Delivery Call §Low-Hanging Fruit]` |
| 8 | **QBI optimization** | QBI deduction was missed on 2024 return per memo; capture going forward | `?` Pending workbook ingestion | Planned | ~ | `[ExecSumm:Activity Log 2026-03-03 "QBI missed in 2024"]` |
| 9 | **BRC Dispositions accounting cleanup (inventory method)** | Capitalize purchase + rehab costs to balance sheet; recognize at sale → replaces misleading `$1M` annual loss with true project margin | Not a tax strategy per se but enables accurate planning | Planned | ✓ | `[Transcript:Delivery Call §Solution]` |
| 10 | **New rental-portfolio partnership holdco** | All rental LLCs roll up to one partnership; single K-1 to 1040; isolates liability | TBD (structural) | Planned | ✓ | `[Transcript:Delivery Call §New Org Chart]` |

**Memo headline number**: ~`$55,000` annual tax savings combined across the strategy stack (`[Transcript:Delivery Call §Key Takeaways]`). Apr 9 extension scenario quantifies the 2025-specific REPS+cost-seg leg at `~$157,500` of deductions ($90K suspended + $67.5K accelerated) reducing 2025 balance from `~$25K` to `$0`. `[Activity Log 2026-04-09]`

### 8.2 Strategies considered but NOT applied (this refresh)

- No 1031 exchange referenced — Tate is buying-and-holding (rentals) and flipping (BRC), not 1031-able under flipping treatment
- No Opportunity Zone mention
- No DST / 721 exchange mention
- No conservation easement / ESBT / charitable trust mention

---

## §9. Opportunity Flags

### 9.1 HIGH — actionable immediately

| Flag | Rule | Why It Triggers for Tate | Action |
| --- | --- | --- | --- |
| 🟥 **HIGH — Cost Seg execution gap** | Cost Seg Proposal Intake parent row stuck at `New - Enter in Portal` despite a sub-item being entered to portal | The parent row ("Cline — Cost Seg") has NOT advanced; 111 Hancock sub-item entered 4/2 but workflow is broken. 365 Garfield never even captured. **2025 extension scenario hinges on this.** | H1 + H2 in §7.1 |
| 🟥 **HIGH — REPS qualification not documented** | REPS tax savings claimed in 4/9 extension scenario (`$90K` suspended losses unblocked) but no hours log on file | Without contemporaneous hours documentation, REPS claim is exposed at audit; if disallowed, $25K extension balance materializes | M2 in §7.2 — collect hours log |
| 🟥 **HIGH — S-Corp election timing** | BRC Dispositions actively flipping properties subject to SE tax; S-Corp Election Tracker status `Planned` — no target date set | Every quarter that passes without 2553 effective date = SE tax bleed on flipping profits | M1 in §7.2 |

### 9.2 MEDIUM — track through next quarter

| Flag | Rule | Why It Triggers for Tate |
| --- | --- | --- |
| 🟧 MED — BRC accounting misclassification | QuickBooks shows `$1M` annual loss; actual flipping margin masked | M3 in §7.2 — capitalize as inventory |
| 🟧 MED — Solo 401(k) contribution-window | Solo 401(k) must be established before SE income is realized in the contribution year | M6 in §7.2 — set up under new S-Corp holdco |
| 🟧 MED — Cost seg pipeline expansion | Tate has 6+ properties (4 land contracts, 2 rent-to-own, plus 111 Hancock + 365 Garfield); only 1 in cost seg pipeline | Land contracts pose placed-in-service date complexity; needs property-by-property eligibility screen |
| 🟧 MED — Whitney Cline contact gap | Joint 1040 filer with no separate Notion Client Contact row | L6 in §7.3 |

### 9.3 LOW — hygiene

| Flag | Rule | Why It Triggers for Tate |
| --- | --- | --- |
| 🟨 LOW — Email Log auto-tagger noise | 3 of 4 Email Log rows on Account are misclassifications | L1 in §7.3 |
| 🟨 LOW — Account URL backfill | 5+ URL fields empty on Account record despite files existing in Tax Ascend / F&L | M9 in §7.2 |
| 🟨 LOW — Insights Project extraction backlog | Tax Insights status `Not started` despite Insights `Delivered` 2026-02-10 | L5 in §7.3 |

### 9.4 Cost Seg Pipeline cross-client context

Tate is one of **8 named clients in the 2026-04-08 cross-client Cost Seg Pipeline review** (alongside Tommy Harr, Andy Karabinos, Augustine, Dan Hamilton, Gil Ramos, Michael Venereo, Matt Iannaccio — plus Lacey Blackman, Brett Zanotto, Tanya Toliver, Renee Mueller, Randy Wolfe). `[ClaudeSumm:Cost Seg Pipeline 2026-04-08]` Where Tommy Harr has 13 Cost Seg Proposal rows and Mueller has 9 SREO properties (4471 41st Ave primary `$1.6M` target), Tate sits at the small-portfolio end of this cohort with 1 entered + 1 missing — but the 2025 tax-savings dependency is just as binding.

---

## §10. Operations Analysis

**Engagement maturity.** Tate is a **mid-stage Tax Ascend client**: Insights delivered (2026-02-10), Tax Planning memo issued (2026-03-05), Tax Planning Session 1 delivered (2026-04-02), EL signed at `$5,350`. The relationship is past sales/scoping and into active execution — but the execution layer (Cost Seg intake → Extension filing) has hit a process break. `[TaxAscend:Tate Cline]` `[ExecSumm:Tate Cline.Activity Log]`

**Workflow chain breakdown observed.** The expected workflow:
`Cost Seg Proposal Intake (parent) → Sub-item per property → Submit parent + sub-items to RE Cost Seg portal → Receive proposal → Approve → Engagement → Study delivered → Depreciation schedule integrated into return`

Where it broke:
- Parent intake row "Cline — Cost Seg" exists but status is `New - Enter in Portal` — **never advanced**
- Sub-item "TC.111 hancock st" status is `Entered in Portal` (advanced 2026-04-02) — **mismatched with parent**
- 365 Garfield: **no row at all**

This is a **workflow tracker integrity issue** that the 2026-04-13 Claude session caught only because cross-referencing the extension model against the proposal DB. Without that cross-reference, the cost-seg-dependent extension scenario would have been filed against deductions that don't exist yet. `[ClaudeSumm:Extension Estimate Consolidation §Discovery]`

**Coverage health.**
- ✓ Billing partner clarity: Seth Johnson on Account; Ryan Walsh as Senior Manager on Mango records — same as Spring Bengtzen / Tommy Harr pattern
- ✓ Sales-to-delivery handoff: Bryan Szpindor (Insights presenter) → Alex Orosz (sales close) → Seth (delivery)
- `?` Bookkeeping ownership: 2/10 transcript identifies a "back office" workstream but no specific Accruity bookkeeping team member named for Tate
- `?` Cost Seg admin ownership: parent intake row's stuckness suggests no clear owner for "submit parent to portal" step

**Document hygiene.**
- Strong: SharePoint folder structure cleanly organized (`Client Files/Cline, Tate/Tax Planning/`, `Extensions/2025/4.15 Deadline/Correspondence/`)
- Weak: Account record URLs are blank despite files existing — backfill task M9
- Mixed: PBC list received per EL row, but PBC items "from google drive" not yet saved to onedrive (per EL Notes)

**Time-on-task signal.** Per Insights Project `Temp Filter`: "Piah to do - Extraction and analysis 04/29" — extraction is queued for 2026-04-29, indicating compliance work is tracking past the extension. Reasonable given the planning workstream is the active priority.

**Risk surface.**
- (HIGH) REPS facts-and-circumstances exposure if hours not documented contemporaneously
- (HIGH) Cost seg execution risk if parent intake remains stuck through Apr 15
- (MED) BRC accounting misstatement — `$1M` book loss vs true profitability could cause estimated-payment / planning errors
- (LOW) IRS audit risk per 2/10 call's note about all rentals flowing to personal return

---

## §11. Individual Profile(s)

### 11.1 Tate Cline (Primary Filer)

- **Name**: Tate Cline
- **Email**: `knrspropertiesllc@gmail.com` (Gmail; entity-name-prefixed inbox suggests Tate uses one inbox per business)
- **Phone**: `(614) 456-6451` (Columbus, OH area code)
- **Filing Status**: MFJ with Whitney Cline `[Mango:1040 - Tate & Whitney Cline]`
- **Residency**: Ohio (Delaware, OH 43015 rental; Columbus area)
- **Profession**: Real estate investor + flipper + small-business operator. Per 2/10 call: managing rental portfolio of 6+ properties + BRC Dispositions flipping operation + cooking-class side venture. Self-perceived as full-time real-estate (REPS-likely).
- **Entity exposure**: KNRS Properties LLC (rentals) · BRC Dispositions (flipping, NOT yet S-Corp) · KR&S Properties (rentals) · cooking class · 6+ underlying property LLCs (4 on land contracts, 2 going rent-to-own)
- **Compensation pattern**: All rental P&L flows to personal return (1040 Schedule E currently); BRC Dispositions SE-taxed; no W-2 captured
- **Tax posture**: 2024 extraction baseline complete (Cline_analysis_2024.xlsm); 2025 extension scenario modeled at `$0` (with strategies) or `$25K+` (without); REPS qualification likely
- **Engagement temperature**: Engaged — attended 1/29 + 2/10 + 4/02 meetings; signed EL `$5,350`; portal invited; PBC items submitted

### 11.2 Whitney Cline (Spouse / Co-filer)

- **Name**: Whitney Cline
- **Filing role**: MFJ co-filer per Mango project name
- **Notion contact row**: ❌ none (gap to backfill — L6)
- **Email / phone**: not captured this refresh
- **Profession / income role**: not captured this refresh

---

## §12. Provenance Index

This dossier draws on the following Notion records and source documents. All inline tags resolve to entries here.

### 12.1 Notion records (this refresh)

| Tag | Record | Notion URL |
| --- | --- | --- |
| `[Accounts:Tate Cline]` | Account record (canonical) | https://www.notion.so/30d4917287518113aaead67f8bfafece |
| `[Contact:Tate Cline]` | Primary Client Contact | https://www.notion.so/30d491728751819ba6ded7ae59fccf77 |
| `[EmailAddrs:Tate Cline]` | Email addresses tracker | https://www.notion.so/2fc4917287518013b778eefd8b09c2ac |
| `[ExecSumm:Tate Cline]` | Executive Summary DB row (canonical) | https://www.notion.so/33b49172875181d58542f05d50fe9189 |
| `[ExecSumm:34249172...d355dd]` | Executive Summary DB row (DUPLICATE — flagged) | https://www.notion.so/34249172875181b2a0bfe124b5d355dd |
| `[TaxAscend:Tate Cline]` | Tax Ascend record | https://www.notion.so/30449172875180a9815dfc7a657dca11 |
| `[InsightsProject:Tate Cline]` | Insights Project Status | https://www.notion.so/2fd491728751805a92b4c1c0ee77acb5 |
| `[TaxPlanningSession:Tate Cline]` | Tax Planning Session | https://www.notion.so/31949172875180129701e4369a8b17c0 |
| `[SCorpTracker:Tate Cline]` | S-Corp Election Tracker | https://www.notion.so/34a491728751819ea3f2f0667aae5650 |
| `[EL:Tate Cline 2026-02-24]` | Engagement Letter row | https://www.notion.so/3034917287518095a520da84b5870a1c |
| `[CostSegProposal:Cline — Cost Seg]` | Cost Seg Proposal Intake (parent) | https://www.notion.so/33d4917287518144b229e323ff86751e |
| `[CostSegProposal:111 Hancock St]` | Cost Seg Proposal Intake (sub-item) | https://www.notion.so/33749172875181b79d46f8ad985569eb |
| `[Mango:1040 - Tate & Whitney Cline]` | Mango Planning & Compliance OLD DB row | https://www.notion.so/33a49172875181a9b909d3da1fc1158d |
| `[Mango:Tax Planning - Tate Cline]` | Mango Planning & Compliance OLD DB row | https://www.notion.so/33a4917287518161b1bcda7e4e0b7069 |
| `[Mango New DB:Tax Planning - Tate Cline]` | Mango Planning & Compliance NEW DB | https://www.notion.so/34249172875181debc92cebe7268f966 |
| `[F&L:33b491728751811dbacbca1b38476f32]` | Files & Links — "Engagement Letter" (shell) | https://www.notion.so/33b491728751811dbacbca1b38476f32 |
| `[F&L:33b49172875181a39d18ee7ed412d488]` | Files & Links — "Executive Summary" (shell) | https://www.notion.so/33b49172875181a39d18ee7ed412d488 |
| `[F&L:33b491728751810fbb6df96f9abc44a7]` | Files & Links — "Tate Cline" (Doc Inventory + PBC) | https://www.notion.so/33b491728751810fbb6df96f9abc44a7 |
| `[Meetings:2fb49172...80db]` | 2026-01-06 Touchbase | https://www.notion.so/2fb49172875180db800ec7949abee3a7 |
| `[Meetings:2fb49172...80a1]` | 2026-01-22 Clarification (cancelled) | https://www.notion.so/2fb49172875180a1bc64ede097c3ef14 |
| `[Meetings:2fb49172...8007]` | 2026-01-29 Clarification | https://www.notion.so/2fb4917287518007913bc9c4bcc7cbd1 |
| `[Meetings:30449172...8038]` | 2026-02-10 Insights Delivery | https://www.notion.so/30449172875180389215e85f5cc183d1 |
| `[Meetings:32949172...80a0]` | 2026-03-20 Tax Planning (rescheduled) | https://www.notion.so/32949172875180a09d85d13002c63456 |
| `[Meetings:33549172...805e]` | 2026-04-02 Tax Planning Session | https://www.notion.so/335491728751805ea67bca6403e601cb |
| `[Transcript:Delivery Call 2026-02-10]` | Tate Cline's Accruity Delivery Call - February 10 (Fathom 84 min) | https://www.notion.so/31849172875180d1b91af6659c05f5ca |
| `[ClaudeSumm:Extension Estimate Consolidation]` | 2026-04-13 Claude Summary | https://www.notion.so/34249172875181bebce5e3aec36ef60c |
| `[ClaudeSumm:Cost Seg Pipeline 2026-04-08]` | Cross-client Cost Seg Pipeline session | https://www.notion.so/33c49172875181098390e5d079955549 |
| `[EmailLog:FW Southern Visions]` | Misclassified — Wolfe/Wilkes recap | https://www.notion.so/3424917287518144a4fed005ba5477b5 |
| `[EmailLog:FW realestategoto.com]` | Misclassified — Gary Aronov recap | https://www.notion.so/34249172875181dca589ecb01817fe48 |
| `[EmailLog:FW vState Filings]` | Possibly Tate-related — vState recap | https://www.notion.so/342491728751816f8095e06804080bc2 |
| `[EmailLog:Declined Stacy<>Seth<>Sophia]` | Internal calendar decline (misclassified) | https://www.notion.so/34249172875181ba9110ffe4f537ac42 |

### 12.2 External documents referenced

| Tag | Document | Location |
| --- | --- | --- |
| `Tax_Planning_Memorandum_Tate_Cline_2026.docx` | Tax Planning Memo (sent 2026-03-05) | SharePoint: Client Files/Cline, Tate/Tax Planning/ `[TaxAscend:Tax Memo URL]` |
| `Cline_analysis_2024.xlsm` | 2024 tax analysis workbook | Attached to Tax Ascend record `[TaxAscend:Tate Cline.Tax Analysis Files]` |
| `21 - Tate Cline - Sent.msg` | 2026-04-09 extension email | SharePoint: Extensions/2025/4.15 Deadline/Correspondence/ `[Activity Log 2026-04-09]` |
| `Tate_Cline_2025_Extension_Estimate.xlsx` | 2026-04-13 6-tab extension workbook | SharePoint `[ClaudeSumm:Extension Estimate Consolidation]` |
| `2026-04-13_Tate_Cline_Extension_Estimate.html` | 2026-04-13 session detail HTML | SharePoint `[ClaudeSumm:Extension Estimate Consolidation]` |
| `Fw__Tate_Cline_-_Open_Items__Tax_Plan_Follow_Up.msg` | Open items + tax plan follow-up | EL row content block `[EL:Tate Cline.Open Items Email]` |
| `Tate_Cline_Tax_Planning_Prep_Summary_2026.docx` | 2026-04-02 prep summary | SharePoint `[ExecSumm:Activity Log 2026-04-02]` |
| Cost Seg Estimate (111 Hancock) | SharePoint PDF | `[CostSegProposal:111 Hancock St.Estimate]` |
| Signed EL (MangoShare) | Engagement Letter | `app.mangoshare.com/share/36414a8b2c835c8bbbf72641` `[EL:Tate Cline.Signed EL mangoshare]` |
| PBC folder | ImagineTime workspace 937757 | `app.imaginetime.com/firm/5331/workspaces/937757/files/19182108/folder` `[EL:Tate Cline.PBC Folder Link]` |

### 12.3 BATCH_REFRESH_PROMPT.md notes

- Tate Cline appears in the **"Currently in the Executive Summaries DB"** populate-list AND in the **"Duplicates — DO NOT delete; log to cleanup queue"** list. Confirmed this refresh: canonical row is `33b49172875181d58542f05d50fe9189`; duplicate row is `34249172875181b2a0bfe124b5d355dd` (titled `🗑️ DELETE — Tate Cline (duplicate)`). `[BATCH_REFRESH_PROMPT.md §The remaining queue]`

---

## §13. Changed Since Last Refresh

**This is the first refresh** for Tate Cline under the comprehensive dossier pipeline. No prior dossier exists, so there is no delta narrative.

**Baseline established this refresh (2026-04-22):**
- Canonical Account record identified: `30d4917287518113aaead67f8bfafece`
- Duplicate Exec Summary row identified and flagged (do not auto-delete)
- 2 prior Claude Summaries surfaced (2026-04-08 cross-client cost seg + 2026-04-13 Tate-specific extension consolidation) and woven into §6
- 6 Meetings Tracker rows reviewed; 2/10 Delivery Call transcript pulled into §4.1
- Cost Seg execution gap (parent intake stuck; 365 Garfield missing) re-surfaced and promoted to §7.1 HIGH
- 11 Tax Planning strategies catalogued in §8 with `~$55K` annual savings ceiling and Apr-9 extension scenario quantified at `$0` vs `$25K`
- §7 Action Items: 5 HIGH (Apr 15 cycle), 9 MED (post-Apr 15), 6 LOW (hygiene)
- §9 Opportunity Flags: 3 HIGH (cost seg execution, REPS docs, S-Corp timing), 4 MED, 3 LOW

**Items dossier-gen flagged for next refresh queue:**
- Backfill Account record URLs (PBC Workbook, Tax Extraction, Tax Planning Memo, SharePoint Drive, Tax Analysis Workbook)
- Re-link 3 misclassified Email Log rows away from Tate's Account
- Resolve Exec Summary duplicate (move to cleanup queue)
- Add Whitney Cline as separate Notion contact row
- Pull Tax Insights extraction once Piah's 2026-04-29 work completes
- Capture 365 Garfield property data + create second Cost Seg Proposal Intake row

**Provenance summary**: 30+ Notion records reviewed, 1 Fathom transcript (84 min), 2 Claude Summaries, 1 Engagement Letter, 1 Tax Planning Memo, 1 extension workbook, 1 HTML session detail. ✓ Tate-specific data; ✓ cross-client cost seg context; ✓ duplicate row resolved.

---

*End of dossier — Tate Cline 2026-04-22 (first refresh).*
