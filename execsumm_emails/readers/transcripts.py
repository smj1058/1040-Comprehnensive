"""Meeting transcripts — Granola / Fathom / Fellow.

Source tags: `[Granola <date>]` / `[Fellow <date>]` / `[InsightsCall <date>]`.
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - MCP
    """Pull transcripts for this account from the Notion Meeting Transcripts DB and
    Granola MCP. Return list of transcript records with date, participants,
    decisions, action items, quotes.
    """
    raise NotImplementedError("transcripts.read binds Granola + Notion MCP at runtime.")
