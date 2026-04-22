"""Claude Activity Log + Claude Summaries reader.

Source tag: `[Claude <date> <thread-title>]`.
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - MCP
    """Every Claude session tied to this account: date, thread title, topics,
    files reviewed, Notion pages created, and a one-line takeaway.
    """
    raise NotImplementedError("claude_chats.read binds Notion MCP at runtime.")
