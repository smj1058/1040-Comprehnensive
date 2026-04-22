"""Email threads — Outlook + Notion Email Log + 📧 Email Intelligence subpages.

Source tags:
  `[Email <date> <sender>→<recipient> "<subject>"]` for Outlook-sourced
  `[EI:<thread>]` for already-synthesized Email Intelligence entries
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - MCP
    """Pull every substantive email thread tied to this account.

    Steps:
      1. Fetch Notion Client Email Log rows via Account.Email Log relation.
      2. Fetch the existing `📧 Email Intelligence` subpage under the account's
         thin Exec Summary child page (carry forward its synthesized threads).
      3. Live-search Outlook (`outlook_email_search`) for threads involving the
         client's primary/secondary contact emails over the last 18 months.
      4. Dedupe by Conversation ID. Noise (marketing, webinar blasts, etc.) is
         moved into a `noise` bucket.
    """
    raise NotImplementedError(
        "emails.read binds Outlook MCP + Notion MCP at runtime."
    )
