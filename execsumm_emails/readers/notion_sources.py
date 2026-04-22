"""Notion-resident open-items sources.

Engagement Inquiries, Service Requests, Intake Requests, Meeting Action Items,
Controversy Intake, Fileforms Communications — every record still open or
recently closed for this account.
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - MCP
    raise NotImplementedError("notion_sources.read binds Notion MCP at runtime.")
