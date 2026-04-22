"""Resolve a client name to an Account record and all its linked data sources."""

from __future__ import annotations

from dataclasses import dataclass, field

from .notion_client import NotionMCP


@dataclass
class Account:
    name: str
    page_url: str
    client_number: str | None = None
    mango_client_id: str | None = None
    mango_display_name: str | None = None
    pbc_workbook_url: str | None = None
    sharepoint_drive_url: str | None = None
    tax_extraction_url: str | None = None
    tax_planning_memo_url: str | None = None
    meeting_prep_notes_url: str | None = None
    primary_contact_url: str | None = None
    relationship_manager_url: str | None = None
    reporting_entities: list[str] = field(default_factory=list)
    tax_engagements: list[str] = field(default_factory=list)
    back_office_engagements: list[str] = field(default_factory=list)
    tax_ascend: list[str] = field(default_factory=list)
    exec_summary_rows: list[str] = field(default_factory=list)
    email_log_rows: list[str] = field(default_factory=list)
    engagement_inquiries: list[str] = field(default_factory=list)
    service_requests: list[str] = field(default_factory=list)
    intake_requests: list[str] = field(default_factory=list)
    meetings: list[str] = field(default_factory=list)
    meeting_transcripts: list[str] = field(default_factory=list)
    claude_activity: list[str] = field(default_factory=list)
    claude_summaries: list[str] = field(default_factory=list)
    files_and_links: list[str] = field(default_factory=list)
    documents: list[str] = field(default_factory=list)
    engagement_letters: list[str] = field(default_factory=list)
    cost_seg_proposals: list[str] = field(default_factory=list)
    cost_seg_engagements: list[str] = field(default_factory=list)
    fileforms_engagements: list[str] = field(default_factory=list)
    controversy_intake: list[str] = field(default_factory=list)


def load(client: str, notion: NotionMCP | None = None) -> Account:
    """Given a client name, resolve the Accounts row and every linked relation."""
    notion = notion or NotionMCP()
    row = notion.find_account(client)
    return Account(
        name=row["Account Name"],
        page_url=row["url"],
        client_number=row.get("Client #"),
        mango_client_id=row.get("Mango Client ID"),
        mango_display_name=row.get("Mango Display Name"),
        pbc_workbook_url=row.get("PBC Workbook"),
        sharepoint_drive_url=row.get("SharePoint Drive"),
        tax_extraction_url=row.get("Tax Extraction"),
        tax_planning_memo_url=row.get("Tax Planning Memo"),
        meeting_prep_notes_url=row.get("Meeting Prep Notes"),
        primary_contact_url=notion.first(row.get("Primary Contact")),
        relationship_manager_url=notion.first(row.get("Relationship Manager")),
        reporting_entities=notion.urls(row.get("Reporting Entities")),
        tax_engagements=notion.urls(row.get("Tax Engagements")),
        back_office_engagements=notion.urls(row.get("Back Office Engagements")),
        tax_ascend=notion.urls(row.get("Tax Ascend")),
        exec_summary_rows=notion.urls(row.get("Executive Summaries")),
        email_log_rows=notion.urls(row.get("Email Log")),
        engagement_inquiries=notion.urls(row.get("Engagement Inquiries")),
        service_requests=notion.urls(row.get("Service Requests")),
        intake_requests=notion.urls(row.get("Intake Requests")),
        meetings=notion.urls(row.get("Meetings")),
        meeting_transcripts=notion.urls(row.get("Meeting Transcripts")),
        claude_activity=notion.urls(row.get("Claude Activity Log")),
        claude_summaries=notion.urls(row.get("Claude Summaries")),
        files_and_links=notion.urls(row.get("Files & Links")),
        documents=notion.urls(row.get("Documents")),
        engagement_letters=notion.urls(row.get("Engagement Letters")),
        cost_seg_proposals=notion.urls(row.get("Cost Seg Proposals")),
        cost_seg_engagements=notion.urls(row.get("Cost Seg Engagements")),
        fileforms_engagements=notion.urls(row.get("Fileforms Engagements")),
        controversy_intake=notion.urls(row.get("Controversy Intake")),
    )


def all_in_exec_summary_index(notion: NotionMCP | None = None) -> list[str]:
    """Every client name referenced from the `📋 Client Executive Summaries` index."""
    notion = notion or NotionMCP()
    return notion.list_clients_in_exec_summary_index()
