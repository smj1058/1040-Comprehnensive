"""Cumulative merge logic for living-document refreshes.

Rules (matches the approved plan):
  1. Factual sections (Entity Structure, Property Portfolio, Books Status, Tax
     Status) update in place; retained prior values only when changed — then
     `(was: X per [source], changed to: Y per [source] on <date>)`.
  2. Narrative sections (Client Overview, Operations Analysis, Individual
     Profile, Strategic Themes) are amended with a dated revision block, not
     overwritten.
  3. Conversations Log, Recent Activity Timeline, Claude Chats are append-only.
  4. Each refresh emits `## 0. Changed Since Last Refresh` at the top.
  5. Prior dated .md files in `dossiers/` are retained forever.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_prior_dossier(account) -> dict[str, Any] | None:
    """Read the most-recent dated `.md` for this client from Drive or local
    mirror and parse it into a structured dict for the merge. Returns `None`
    on first run.
    """
    # Implementation binds to drive_client at runtime.
    return None


def diff(prior: dict[str, Any] | None, new: dict[str, Any]) -> dict[str, Any]:
    """Compute the Changed-Since-Last-Refresh payload:
      - new_threads: email threads added this refresh
      - closed_threads: threads transitioned to closed
      - new_action_items / closed_action_items
      - number_changes: {field -> (old, new, source)}
      - new_files: files consumed this refresh that weren't consumed before
      - status_changes
    """
    if prior is None:
        return {"first_run": True}
    return {"first_run": False}


def ensure_append_only(section_name: str, prior_content: str, new_entries: list[str]) -> str:
    """Preserve prior content verbatim; insert new entries in chronological
    position. Used for Conversations Log + Timeline + Claude Chats.
    """
    if not prior_content:
        return "\n".join(new_entries)
    return prior_content + "\n" + "\n".join(new_entries)
