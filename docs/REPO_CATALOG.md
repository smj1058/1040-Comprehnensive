# Repo Catalog — Complete File Reference

> Cross-reference for everything in `smj1058/1040-Comprehnensive`. Built so you can
> point to it from any session (web Claude Code, local CLI, MCP-Projects) and
> know what each file does, the logic behind it, and how files connect.
>
> **Last cataloged**: end of FlashTax brainstorm session
> **Maintained at**: `docs/REPO_CATALOG.md`

---

## TWO PROJECTS LIVE IN THIS REPO

This repo's name is `1040-Comprehnensive` but it actually contains two distinct projects sharing a codebase. Knowing which is which avoids confusion:

| Project | Purpose | Where it lives | Trigger to refresh |
|---|---|---|---|
| **A. Tax Workbook Framework** | The 1040 calc engine — long-format `Master_Inputs` → pivots → year-sheet calc → dashboards → deliverable | `scripts/`, `docs/Master_Pivot_Framework_*.xlsx`, `docs/Tax_Workbook_*.xlsx`, `docs/EXCEL_PROMPT_*.md` | Manual — Claude runs Python scripts to build workbooks |
| **B. Client Intelligence Dossier Generator** | Generates per-client `dossier.md` files from Notion + Drive + email + transcripts. Lives in CLAUDE.md as the canonical instruction set. | `execsumm_emails/`, `dossiers/`, `extracts/`, `CLAUDE.md`, `README.md` | Manual — Claude refreshes one client per session via 11-turn workflow |

The two share only the repo. Different scripts, different data, different workflows.

---

## PROJECT A — TAX WORKBOOK FRAMEWORK

### Python scripts (`scripts/*.py`)

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| `build_master_pivot_framework.py` | The ORIGINAL builder for v5 framework. Creates Master_Inputs + Y2025 year sheet + Treatment_Profile_Map + Dropdown_Lists from scratch. | None (builds from scratch) | `docs/Master_Pivot_Framework.xlsx` |
| `build_sample_template.py` | First sample template demonstrating Tax Workbook KISS+Views architecture (schemas, closed-set dropdowns, formula patterns). | None | `docs/Tax_Workbook_Sample_Template.xlsx` |
| `build_sample_template_v2.py` | Refined sample with cascading dropdowns, derived columns, adjustment column on input table, separate strategies table with commit gating, True Tax Burden box, year-sheet ↔ pivot integrity check. | None | `docs/Tax_Workbook_Sample_Template_v2.xlsx` |
| `build_sample_template_v3.py` | Minimal current-year focused sample. Y2025 only, input table A:Q, rollup at column T, no formula-driven derived columns. | None | `docs/Tax_Workbook_Sample_Template_v3.xlsx` |
| `build_sample_template_v4.py` | Same as v1 but with `fullCalcOnLoad=True` set so Excel forces recalc on open. | None | `docs/Tax_Workbook_Sample_Template_v4.xlsx` |
| `build_groupby_variant.py` | Alternative pivot architecture using Excel 365's GROUPBY / PIVOTBY functions instead of SUMIFS. Single spilling formula per pivot tab. Requires Excel 365 current channel. | None | `docs/Master_Pivot_Framework_GROUPBY.xlsx` |
| `apply_audit_fixes_v5.py` | Phase 0 audit fixes applied to a user-uploaded v5 file: bucket typo "Adjustments"→"Adjustment", SEP-IRA TargetLine 8→10 (later reverted), R&D Credit 13→20, refresh 2023+2024 tax brackets to actual IRS values, add data validations to Year/Helper_Treatment/Primary_Line, add Activity_Type="Baseline" filter to 246 SUMIFS across pivot tabs. | `docs/Master_Pivot_Framework_v5_uploaded.xlsx` | `docs/Master_Pivot_Framework_v5_audit-fixes.xlsx` |

### Phase 3 chain (sequential — each script reads the previous output)

| # | Script | What it does | Logic |
|---|---|---|---|
| 3a | `phase3v5_control_panel_audit.py` | Adds HOUSEHOLD DETAILS section (12 fields) to Control_Panel between TAX PROFILE and ACTIVE YEAR SNAPSHOT | Inserts 12 rows at row 22. Adds taxpayer/spouse names, 65+/blind flags, CTC vs ODC dependent split, SE health ins, itemize override, prior year total tax. Adds matching named ranges. Cross-sheet refs to C19/C21 preserved. |
| 3b | `phase3v6_tax_plan_dashboard.py` | Full rebuild of Tax_Plan_Dashboard to Jeff 4-box pattern | Clears existing layout, builds Box 1 (Headline) / Box 2 (Strategy Marginal) / Box 3 (Tax Execution) / Box 4 (Checklist + Take-Home). All numeric pulls via `INDIRECT("Y"&Active_Year&"!...")`. Removes 2 legacy bar charts. |
| 3e | `phase3v7_dashboard_selector_and_3e.py` | Two parts: (A) Dashboard year selector fix (C4 from formula → static dropdown), (B) Framework_Ref STR/STD cross-ref + new Property_Appendix sheet | Adds "Our STR-ID / Jeff STD-ID / Cross-Ref Notes" columns to Framework_Ref. Creates Property_Appendix with 3 sections: Property Master List (14 cols), REPS Material Participation Tracker (§1.469-5T tests), §1.469-4 Grouping Election Tracker. |
| 3 (catalog) | `phase3v8_master_strategies_catalog.py` | Creates Master_Strategies sheet with one row per impact | 20 impact rows for 15 STR-IDs. Schema: Strategy_ID, Impact_Num, Strategy_Name, Bucket, Framework_Ref, TargetLine, HelperTreatment, Sign, Cap_Rule, Plan_Maturity_Min, Description. Includes Strategy Builder (Section D) — live tool to size a strategy. |
| (reconcile) | `phase3v9_catalog_reconcile.py` | Rebuilds catalog using year-sheet STR-IDs as authoritative | v8 catalog had wrong IDs vs year sheets (8/15 mismatched). Now all 15 IDs match. Multi-impact fan-out preserved via CounterLine pattern (STR-001 = 2 impacts, STR-009 = 3, STR-010 = 2). |
| (state stack) | `phase3v10_state_tax_stack.py` | Adds multistate capability | 3 new columns on Master_Inputs (Primary_State / State_Mix / PTET_Routed). Adds States dropdown list. New STATE TAX RATES + PTET section on Tax_Ref (51 jurisdictions). Named ranges: States, tblStateRates, PTET_States. |
| (validator) | `phase3v11_year_sheet_validator.py` | Path A safe additive — adds catalog validator columns to year sheets | Per Y2023..Y2028: STR-ID dropdown on A6:A20, 5 new columns R-V (Catalog Name / Line / Counter / Sign / Drift Check) OUTSIDE the table. tblY*_Strategies untouched (96 downstream SUMIFS preserved). |
| (LAMBDAs) | `phase3v12_kiss_lambdas.py` | Installs 6 KISS LAMBDAs to defined names | TAX_ORD (progressive bracket), TAX_CG (LTCG 0/15/20), TAX_NIIT (3.8%), TAX_SE (SS + Medicare), STD_DED (lookup), TAX_STATE (top rate). Documentation added to Setup_Guide. *Caveat: openpyxl can't validate LAMBDA syntax; user verifies in Excel.* |
| (3c) | `phase3v13_exact_marginal_savings.py` | Per-strategy exact marginal savings | Adds fn_StrategyMarginal LAMBDA. Replaces `-D6*0.32` approximation across 90 year-sheet cells + 15 dashboard cells. Routes Line 20 → credit (1:1), Line 7 → TAX_CG delta, else → TAX_ORD delta. |
| (3c-SE) | `phase3v14_marginal_se_fica.py` | Adds FICA + CounterLine to fn_StrategyMarginal | v13 returned $0 for STR-001 (ordinary nets out). Now adds counter_line param + 15.3% FICA when wage line (1z) touched. STR-001 wage shift now returns ~$3,825 FICA savings. |
| (reconcile) | `phase3v15_reconciliation_resolve.py` | Resolves 6 open reconciliation items from Section E | RECON-1: STR-006 Roth 1z→4b. RECON-2: STR-014 PTE 12→8. RECON-3: HSA confirmed. RECON-4: STR-009 catalog/year asymmetry documented. RECON-5: STR-010 case-by-case note. RECON-6: Bucket lookup column W added to year sheets. |
| (audit) | `phase3v16_audit_sheet.py` | Audit_Report sheet — static formula scan | Scans 19 sheets for hardcoded literals, magic conditionals, error values, external links. Reports: severity (FLAG/WARN/OK), kind, suggested action. Found Deliverable F50:F64 still had old × 0.32 — patched in same pass. |
| (rates) | `phase3v18_name_rates_fix_qbi_flag.py` | Names 11 calc-engine rates | Replaces literal rates with named refs: Rate_FICA_SS_Employee, Rate_FICA_Medicare_Employee, Rate_Sec1250_Recap, Rate_QBI_Deduction, Rate_QBI_W2_50pct, Rate_QBI_W2_25pct, Rate_QBI_UBIA_2_5pct, Rate_QBI_BenefitApprox, Rate_NIIT, Rate_SE_Deduction. **FLAGS QBI bug at J119/K119** (label says 50% but formula is *0.2). |
| (QBI fix) | `phase3v19_qbi_fix_audit_refine.py` | Fixes QBI bug + refines audit logic | J119/K119 × 6 sheets: `*0.2` → `*Rate_QBI_W2_50pct` (= 0.50). Audit literal-extraction refined to strip named ranges (eliminates 18 false-positive "threshold" findings from substrings like "1250" in Rate_Sec1250_Recap). |

### Phase 3 chain (input/output map)

```
docs/Master_Pivot_Framework_v5_uploaded.xlsx                  (user upload)
  ↓ apply_audit_fixes_v5.py
docs/Master_Pivot_Framework_v5_audit-fixes.xlsx
  ↓ user manual + phase3v1.xlsx through phase3v4_CC.xlsx
docs/Master_Pivot_Framework_v5_phase3v4_CC.xlsx
  ↓ phase3v5 → v6 → v7 → v8 → v9 → v10 → v11 → v12 → v13 → v14 → v15
docs/Master_Pivot_Framework_v5_phase3v15_CC.xlsx
  ↓ phase3v16 (audit) → v18 (rates+flag) → v19 (QBI fix)
docs/Master_Pivot_Framework_v5_phase3v19_CC.xlsx
  ↓ patches v20-v23 (LAMBDA recovery attempts)
docs/Master_Pivot_Framework_v5_phase3v24_CC.xlsx  ← LATEST
```

### Excel workbooks produced

| File | Origin | Status |
|---|---|---|
| `Master_Pivot_Framework.xlsx` | `build_master_pivot_framework.py` | Original baseline |
| `Master_Pivot_Framework_GROUPBY.xlsx` | `build_groupby_variant.py` | Alternative GROUPBY-based variant (needs Excel 365) |
| `Master_Pivot_Framework_v5_uploaded.xlsx` | User upload | Starting point for v5 phase work |
| `Master_Pivot_Framework_v5_audit-fixes.xlsx` / `_v2.xlsx` | `apply_audit_fixes_v5.py` | Phase 0 output |
| `Master_Pivot_Framework_v5_phase3v1.xlsx` through `phase3v4_CC.xlsx` | User manual + Claude builds | Phase 3 early iterations |
| `Master_Pivot_Framework_v5_phase3v5_CC.xlsx` through `phase3v24_CC.xlsx` | Phase 3 scripts | Phase 3 main chain |
| `Tax_Workbook_Sample_Template.xlsx` through `_v4.xlsx` | `build_sample_template*.py` | Earlier template iterations (pre-Master_Pivot) |
| `Tax_Calculator_Library.xlsx` | Manual / Claude-in-Excel | Standalone LAMBDA library (mentioned in Setup_Guide) |

### Instructional / handoff markdown files (`docs/*.md`)

| File | Purpose |
|---|---|
| **`PROJECT_OVERVIEW.md`** | High-level overview of the Tax Workbook project. Read first when picking up the project cold. |
| **`TAX_WORKBOOK_PIVOT_ARCHITECTURE.md`** | The architecture spec — long-format Master_Inputs → pivots → year sheets → dashboards → deliverable. KISS+Views philosophy. |
| **`RUNBOOK_MASTER.md`** | The master runbook — sequence of phases, what to do when. |
| **`AUDIT_REPORT_v5.md`** | Pass-1 audit findings on the v5 workbook (the basis for `apply_audit_fixes_v5.py`). |
| **`HANDOFF_2026-04-22.md`** | Older session handoff document. |
| **`COMBINED_SESSION_PROMPT.md`** | Combined-session prompt for cross-session continuity. |
| **`DESKTOP_HANDOFF_PROMPT.md`** | Prompt for moving from cloud session to local desktop session. |
| **`REAL_PIVOT_DESKTOP_PROMPT.md`** | Prompt for working with real Excel PivotTables (vs SUMIFS-driven) on desktop. |
| **`BATCH_REFRESH_PROMPT.md`** | Batch-refresh prompt (for the Dossier generator side — see Project B). |

### Excel prompts (`docs/EXCEL_PROMPT_*.md`) — for Claude-in-Excel sessions

| File | Purpose |
|---|---|
| `EXCEL_PROMPTS_INDEX.md` | Index page listing all Excel prompts and when to use each. |
| `EXCEL_PROMPT_MASTER_ORCHESTRATION.md` | Master orchestration — runs the whole sequence. |
| `EXCEL_PROMPT_KISS_LAMBDAS.md` | LAMBDA install instructions (Name Manager paste-ready bodies). |
| `EXCEL_PROMPT_ADD_QBI_COLUMNS.md` | Adds QBI-related columns to Master_Inputs. |
| `EXCEL_PROMPT_DRILL_LINKS.md` | Adds drill-down hyperlinks. |
| `EXCEL_PROMPT_EXTRACTION_IMPORT.md` | VBA-based extraction file importer pattern. |
| `EXCEL_PROMPT_JEFF_CONNECTOR.md` | Cross-workbook integration with Jeff's Accruity_Tax_Plan_Asset workbook. |

### This-session output docs (new this session)

| File | Purpose |
|---|---|
| `REMAINING_EXCEL_WORK.md` | Punch list of Excel-side work remaining on the 1040 workbook (LAMBDA install, wire-up, verification). |
| `FLASHTAX_HANDOFF.md` | Comprehensive technical handoff for a fresh Claude Code session to build the FlashTax prototype. |
| `FINATICAL_PROJECT_MEMO.md` | Strategic memo for Seth's founder meeting — Flash Reports platform vision. |
| `FULL_CONVERSATION_LOG.md` | Narrative summary of the full session. |
| `SESSION_TRANSCRIPT.md` / `.txt` | Dialog-format reconstruction of the session. |
| `REPO_CATALOG.md` | THIS FILE — cross-reference for everything in the repo. |

---

## PROJECT B — CLIENT INTELLIGENCE DOSSIER GENERATOR

### Python module (`execsumm_emails/`)

Top-level files:

| File | Purpose | Key logic |
|---|---|---|
| `__init__.py` | Package init. Version 0.1.0. Entry point: `cli:main`. | — |
| `cli.py` | Command-line interface — `execsumm refresh <client>` / `execsumm refresh-all`. Scaffold for the pipeline contract. Live pilot runs done via MCP tool calls (Notion / Outlook / Granola). | Wires up readers + merge + template + writer. |
| `config.py` | Central config. Notion data source IDs, Drive paths, engagement lens mapping. | Single source of truth for IDs across the codebase. |
| `account_loader.py` | Resolve a client name → Account record + all linked data sources. | `Account` dataclass: name, page_url, client_number, mango_client_id, pbc_workbook_url, sharepoint_drive_url, tax_extraction_url, tax_planning_memo_url, meeting_prep_notes_url, primary_contact_url, relationship_manager_url, reporting_entities list, tax_engagements list. |
| `merge.py` | Cumulative merge logic for living-document refreshes. | Rules: (1) factual sections updated in place with "was X / changed to Y" annotation; (2) narrative sections amended with dated revision blocks; (3) Conversations Log / Timeline / Claude Chats are append-only; (4) each refresh emits "Changed Since Last Refresh" at top; (5) prior dated .md files retained forever. |
| `notion_client.py` | Thin wrapper over Notion MCP. | Methods: `find_account`, `list_clients_in_exec_summary_index`, `fetch`, `query`. All NotImplementedError stubs — bound to MCP transport at runtime. |
| `opportunity_flags.py` | Rule-based opportunity flags — Cost Seg candidates + S-Corp election candidates. | Renders into §8a of dossier. Cross-references Cost Seg Proposals + FileForms Engagements so in-flight opportunities show "In Progress" not "Open". Includes BONUS_RATE_BY_YEAR mapping (2023-2026). Priority enum: HIGH/MEDIUM/LOW/NOT APPLICABLE/IN PROGRESS. |
| `provenance.py` | Source-tag formatting + Provenance Index builder. | Every non-obvious fact gets an inline tag: `[PBC:Entities!A14]`, `[Email <date> <sender>→<recipient> "<subject>"]`, `[Granola <date>]`, `[Memo <date> §<section>]`, etc. Provenance Index lists every tag with a link. |
| `template.py` | Render full dossier in Notion-flavored markdown. Sections 0-16. | HEADER_TMPL defines the dossier title, client metadata table, planning years, engagement stage, temperature, relationship manager, primary contact, data sources. |
| `writer.py` | Write dossier to Drive + local mirror + Notion Exec Summaries DB + Claude Summaries log. | `write_drive_and_local` → both destinations. Filename pattern: `<NameNoSpaces>_Client_Intelligence_<YYYY-MM-DD>.md`. |

Source readers (`execsumm_emails/readers/`):

| File | Source tag | What it reads |
|---|---|---|
| `__init__.py` | (n/a) | Contract: each reader exposes `read(account) -> dict`. Writes sidecar JSON to `extracts/<Client>_<source>_<YYYY-MM-DD>.extract.json`. |
| `pbc_workbook.py` | `[PBC:<Tab>!<Cell>]` | PBC Workbook — entity list, property schedule, books coverage, trial balance, notes. Requires Drive mount. |
| `insights_workbook.py` | `[Insights:<Tab>!<Row>]` | Insights Delivery Workbook (tax extraction). Produces prior-year AGI, taxable income, total tax, effective rate, SE tax, entity P&L slots, strategy candidates. |
| `tax_analysis.py` | `[TaxAnalysis:<Tab>!<Row>]` | Tax Analysis Workbook reader. Requires Drive + openpyxl. |
| `tax_memo.py` | `[Memo <date> §<section>]` | Tax Planning Memo (.docx) reader. Requires python-docx + Drive. |
| `tax_meeting_prep.py` | `[MtgPrep <date>]` | Tax Meeting Prep doc/sheet reader. Requires Drive. |
| `transcripts.py` | `[Granola <date>]` / `[Fellow <date>]` / `[InsightsCall <date>]` | Meeting transcripts from Granola / Fathom / Fellow. Binds Granola + Notion MCP. |
| `emails.py` | `[Email <date>]` / `[EI:<thread>]` / `[SharedInbox:<inbox> <date>]` | Email threads — Outlook client inboxes + Accruity shared inboxes (operations@, tax@, etc.) + Notion Email Log + 📧 Email Intelligence subpages. |
| `claude_chats.py` | `[Claude <date> <thread-title>]` | Claude Activity Log + Claude Summaries reader. Binds Notion MCP. |
| `notion_sources.py` | (various per source) | Engagement Inquiries, Service Requests, Intake Requests, Meeting Action Items, Controversy Intake, Fileforms Communications — every still-open or recently-closed record. |

### Dossier output (`dossiers/`)

48 client folders, each containing `dossier.md` (and sometimes `state.json` for in-progress refreshes). Reference exemplar: `dossiers/SpringBengtzen/dossier.md` (771 lines, §1-§13 + Provenance Index — the pattern to match for every other client).

Clients in the folder: AidanMcIsaac, AlexDykesMarkFerguson, AndyKarabinos, AnnMarieGeddessFrankFelice, BeckyMead, BradKanouse, BrettZanotto, BrittanyByma, DanHamilton, DanielHuffman, DavidMichelleSaward, DonFowler, EvanMeganAugustine, GaryAronov, GianCarloLies, GilRamos, GregSmith, GregWhitmire, JahniStasil, JenniferStickler, JeremyLee, JeremyMartin, JoelCabrera, KaraHinshaw, KelliSalter, LaceyBlackman, LoganBowles, MattAndChelseaIannaccio, MichaelVenereo, MichelleBowles, MikeLucas, MonicaHayes, NickDenillo, ReneeMuellerJeffCohn, ReneeMuellerSolo, RussellFaucette, SandeePayne, SeanKennedy, SpringBengtzen, TanyaToliver, TateCline, TommyHarr.

### Instructional files for Project B

| File | Purpose |
|---|---|
| `README.md` (top-level) | Project B overview — what the dossier generator does, output destinations (Drive + Notion), cumulative living-document rules. |
| `CLAUDE.md` (top-level) | THE canonical project instructions. Pre-flight, the 11-turn refresh workflow, hard rules, per-client folder convention, state.json schema, Notion IDs, remaining client queue. Read this first in any Project B session. |
| `dossiers/README.md` | Internal notes for the dossiers folder. |
| `extracts/README.md` | Sidecar JSON extraction format. Sources: `pbc`, `insights`, `tax_analysis`, `tax_memo`, `tax_meeting_prep`, `transcript`, `email_thread`, `claude_chat`, `notion`. |
| `docs/BATCH_REFRESH_PROMPT.md` | Per-client invocation contract (legacy — now done via CLAUDE.md). |

### Key Notion DB IDs (from `execsumm_emails/config.py`)

| DB | ID |
|---|---|
| Executive Summaries | `20f69b74-b140-4c3c-8041-ba71e7792478` |
| Exec Summaries data source | `collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b` |
| Accounts | `collection://8668d5ca-6472-4b62-914d-0da55334c72a` |
| Reporting Entities | `collection://9c91286b-e233-45f2-98b0-f065544fb89c` |
| Meeting Action Items | `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3` |
| Meeting Transcripts | `collection://b80239b8-8216-4e27-8492-c8a5b66c177d` |
| Meetings Tracker | `collection://2fb49172-8751-80df-b73d-000b4a81281e` |
| Claude Summaries | `collection://86dca8a4-3522-40c4-a568-b99bc98fc756` |
| Claude Activity Log | `collection://f9cc7d05-26b0-4c77-b29c-af974a234b77` |
| Engagement Inquiries | `collection://7d71d896-b9de-4658-a02d-4caca8b0cc02` |
| Engagement Letters | `collection://2ef49172-8751-8056-99e0-000ba1b5dd54` |
| Files & Links | `collection://4432a66e-8f29-480b-8bae-9b88525ae841` |
| Client Email Log | `collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945` |
| Tax Ascend | `collection://2f049172-8751-80f7-bcad-000b63a307fe` |
| Tax Engagements | `collection://86a76ba1-ce54-411f-be12-5e600b37eee5` |
| Service Requests | `collection://806b0308-9591-4f86-8329-c4c0c9bc8e39` |
| Intake Requests | `collection://a6a02303-6817-43d6-b344-a9852d966e26` |
| Tax Planning Actions | `collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3` |
| Back-Office Engagements | `collection://d5b2a93f-86fc-4051-bfaf-8622fb6dd93a` |

---

## CROSS-REFERENCE — when to use what

### Picking up Project A (Tax Workbook) cold

1. Read `docs/PROJECT_OVERVIEW.md` — what the project is
2. Read `docs/TAX_WORKBOOK_PIVOT_ARCHITECTURE.md` — the architecture
3. Read `docs/RUNBOOK_MASTER.md` — what to do when
4. Read `docs/REMAINING_EXCEL_WORK.md` — what's left to do
5. Latest workbook: `docs/Master_Pivot_Framework_v5_phase3v24_CC.xlsx`

### Picking up Project B (Dossier Generator) cold

1. Read `CLAUDE.md` (top-level) — the canonical instructions
2. Read `README.md` (top-level) — project rationale
3. Reference exemplar: `dossiers/SpringBengtzen/dossier.md`
4. Latest pending client queue: `docs/BATCH_REFRESH_PROMPT.md`

### Picking up FlashTax / Finatical work (new)

1. Read `docs/FINATICAL_PROJECT_MEMO.md` — strategic memo
2. Read `docs/FLASHTAX_HANDOFF.md` — technical build handoff
3. Read `docs/SESSION_TRANSCRIPT.md` for context if needed
4. Build target: `FlashTax_Prototype_v1_CC.xlsx` on a new branch

### Picking up Excel-side work for the 1040 workbook

1. Read `docs/REMAINING_EXCEL_WORK.md` — the punch list with paste-ready LAMBDA bodies
2. Reference: `docs/EXCEL_PROMPT_*.md` for specific Excel-side tasks
3. Working file: `docs/Master_Pivot_Framework_v5_phase3v24_CC.xlsx`

---

## NAMING CONVENTIONS (across the repo)

| Suffix / Pattern | Meaning |
|---|---|
| `_CC` | File built by Claude via openpyxl |
| `_SJ` | File built / edited by Seth in Excel |
| `v{N}` | Iteration version |
| `phase3v{N}_*` | Phase 3 sub-iteration N |
| `<Client>_Client_Intelligence_<YYYY-MM-DD>.md` | Dossier output filename |
| `<Client>_<source>_<YYYY-MM-DD>.extract.json` | Sidecar extraction (in `extracts/`) |

---

## REPO LAYOUT VISUAL

```
1040-Comprehnensive/
├── CLAUDE.md                    ← Project B instructions (Dossier generator)
├── README.md                    ← Project B overview
├── docs/                        ← Project A docs + xlsx files + Excel prompts
│   ├── *.xlsx                   ← 33 Excel workbooks (Master_Pivot_Framework + variants)
│   ├── *.md                     ← 22 markdown docs (architecture, runbook, prompts, handoffs)
│   ├── FLASHTAX_HANDOFF.md      ← (new) FlashTax prototype handoff
│   ├── FINATICAL_PROJECT_MEMO.md← (new) Founder meeting memo
│   ├── REPO_CATALOG.md          ← (new) THIS FILE
│   └── ...
├── scripts/                     ← Project A Python build scripts
│   ├── apply_audit_fixes_v5.py
│   ├── build_*.py               ← 5 framework/template builders
│   └── phase3v*_*.py            ← 13 phase-3 chain scripts
├── execsumm_emails/             ← Project B Python module
│   ├── *.py                     ← Top-level: cli, config, account_loader, merge,
│   │                              notion_client, opportunity_flags, provenance,
│   │                              template, writer
│   └── readers/                 ← Source readers per data type
│       └── *.py                 ← pbc, insights, tax_analysis, tax_memo,
│                                  tax_meeting_prep, transcripts, emails,
│                                  claude_chats, notion_sources
├── dossiers/                    ← Project B output — 48 client folders
│   └── <Client>/
│       ├── dossier.md
│       └── state.json
└── extracts/                    ← Project B intermediate extraction JSON
    └── README.md                ← Format documentation
```

---

## END OF CATALOG

If a file isn't in this catalog and you find it, add it here when you're done with that file. The catalog is the single reference point for "what's in this repo" across cloud sessions, local CLI, and MCP project folders.
