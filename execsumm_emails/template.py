"""Render a full dossier in Notion-flavored markdown. Sections 0–16."""

from __future__ import annotations

from datetime import date
from typing import Any


HEADER_TMPL = """# {name} — Client Intelligence Dossier
**Internal Working Document — Accruity**

| Item | Detail |
| --- | --- |
| Client | {client_line} |
| Client # | {client_number} |
| Mango ID | {mango_id} |
| Prepared by | {prepared_by} — Accruity |
| Date | {today} |
| Prior Refresh | {prior_refresh} |
| Planning Year(s) | {planning_years} |
| Engagement Stage | {engagement_stage} |
| Temperature | {temperature} |
| Relationship Manager | {relationship_manager} |
| Primary Contact | {primary_contact} |
| Data Sources | {data_sources} |
| Files Read This Refresh | {files_read} |

**Confidence:** ✓ Confirmed · ~ Estimated · ? Pending
**Attribution:** every non-obvious fact carries an inline source tag (see §16 Provenance Index).

---
"""


def render(context: dict[str, Any], *, prior: dict[str, Any] | None = None) -> str:
    """Render the full dossier markdown from the assembled context.

    The live pilot dossiers for Spring Bengtzen and Tommy Harr were rendered
    directly via MCP and committed under `dossiers/` — they are the reference
    implementation of the template until this function is wired end-to-end
    against the readers.
    """
    raise NotImplementedError(
        "template.render is a scaffold. See dossiers/SpringBengtzen_Client_Intelligence_2026-04-22.md "
        "and dossiers/TommyHarr_Client_Intelligence_2026-04-22.md for the reference output."
    )


def header(name: str, **kwargs: Any) -> str:
    defaults = {
        "client_line": name,
        "client_number": "—",
        "mango_id": "—",
        "prepared_by": "Accruity",
        "today": date.today().isoformat(),
        "prior_refresh": "first run",
        "planning_years": "—",
        "engagement_stage": "—",
        "temperature": "—",
        "relationship_manager": "—",
        "primary_contact": "—",
        "data_sources": "PBC Workbook · Insights Delivery · Insights Transcript · Tax Analysis · Tax Meeting Prep · Tax Memo · Email Threads · Meeting Transcripts · Claude Chats · Notion Records",
        "files_read": "—",
    }
    defaults.update(kwargs)
    return HEADER_TMPL.format(name=name, **defaults)
