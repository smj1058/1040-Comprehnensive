"""Central configuration: Notion IDs, Drive paths, engagement lens mapping."""

from __future__ import annotations

from pathlib import Path

# Notion — databases & data sources
NOTION = {
    "exec_summaries_db": "20f69b74-b140-4c3c-8041-ba71e7792478",
    "exec_summaries_ds": "collection://44d6ebf0-8ccf-44a8-857c-be4b2955a83b",
    "exec_summaries_index_page": "31249172-8751-8102-9b04-d9500205663d",
    "accounts_ds": "collection://8668d5ca-6472-4b62-914d-0da55334c72a",
    "reporting_entities_ds": "collection://9c91286b-e233-45f2-98b0-f065544fb89c",
    "tax_ascend_ds": "collection://2f049172-8751-80f7-bcad-000b63a307fe",
    "tax_engagements_ds": "collection://86a76ba1-ce54-411f-be12-5e600b37eee5",
    "tax_planning_actions_ds": "collection://3cc53615-141e-4afe-b27d-bf3efaf9a0e3",
    "back_office_engagements_ds": "collection://d5b2a93f-86fc-4051-bfaf-8622fb6dd93a",
    "engagement_inquiries_ds": "collection://7d71d896-b9de-4658-a02d-4caca8b0cc02",
    "service_requests_ds": "collection://806b0308-9591-4f86-8329-c4c0c9bc8e39",
    "intake_requests_ds": "collection://a6a02303-6817-43d6-b344-a9852d966e26",
    "meeting_transcripts_ds": "collection://b80239b8-8216-4e27-8492-c8a5b66c177d",
    "meetings_tracker_ds": "collection://2fb49172-8751-80df-b73d-000b4a81281e",
    "claude_summaries_ds": "collection://86dca8a4-3522-40c4-a568-b99bc98fc756",
    "claude_activity_ds": "collection://f9cc7d05-26b0-4c77-b29c-af974a234b77",
    "email_log_ds": "collection://d601d9ff-3cfb-4e25-b8ea-59c50ce3b945",
    "files_and_links_ds": "collection://4432a66e-8f29-480b-8bae-9b88525ae841",
    "documents_ds": "collection://871ca43d-c917-4f23-ba5b-24908b9fc492",
    "working_papers_ds": "collection://aaa71594-477c-4c10-bbe7-7630f0b2a5ed",
    "engagement_letters_ds": "collection://2ef49172-8751-8056-99e0-000ba1b5dd54",
    "controversy_intake_ds": "collection://d48ce60c-4dfd-4e4d-ad7d-991d831710a3",
    "fileforms_comms_ds": "collection://17ce4684-a0bc-4b8f-8358-5b3468073b9c",
    "fileforms_engagements_ds": "collection://d839f428-c9f9-4792-99b8-0462689184ba",
    "cost_seg_proposals_ds": "collection://741deb78-a449-408f-a388-8676d7b319bb",
    "cost_seg_engagements_ds": "collection://7f478b02-7a37-4632-a307-b37bd15759da",
}

# Google Drive target paths
DRIVE = {
    "dossiers": r"G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\dossiers",
    "extracts": r"G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\extracts",
}

# Local mirrors (committed to the repo for PR review and as a fallback).
REPO_ROOT = Path(__file__).resolve().parent.parent
LOCAL_DOSSIERS = REPO_ROOT / "dossiers"
LOCAL_EXTRACTS = REPO_ROOT / "extracts"

# Exec Summary row engagement lens mapping. Multi-engagement accounts get one row per lens.
ENGAGEMENT_LENSES = ("Tax Planning", "Compliance", "Advisory", "Insights", "General")

# Files that should always be listed (and read if present) for every client.
EXPECTED_FILES = (
    "PBC Workbook",
    "Insights Delivery Workbook",
    "Insights Delivery Transcript",
    "Tax Analysis Workbook",
    "Tax Meeting Prep",
    "Tax Planning Memo",
)
