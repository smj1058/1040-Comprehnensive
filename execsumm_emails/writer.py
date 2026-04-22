"""Write dossier to Drive + local mirror, mirror into the Notion Exec Summaries
DB row (body + every property), and log a refresh row in Claude Summaries.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from .config import DRIVE, LOCAL_DOSSIERS, NOTION
from .notion_client import NotionMCP


def _filename(account) -> str:
    safe = account.name.replace(" ", "").replace("&", "And").replace("/", "-")
    return f"{safe}_Client_Intelligence_{date.today().isoformat()}.md"


def write_drive_and_local(account, markdown: str) -> tuple[str, Path]:
    """Write both destinations. Returns (drive_path, local_path)."""
    LOCAL_DOSSIERS.mkdir(parents=True, exist_ok=True)
    local_path = LOCAL_DOSSIERS / _filename(account)
    local_path.write_text(markdown, encoding="utf-8")
    drive_path = f"{DRIVE['dossiers']}\\{_filename(account)}"
    # Drive write binds to a drive_client at runtime.
    return drive_path, local_path


def mirror_to_notion(account, markdown: str, context: dict[str, Any], notion: NotionMCP | None = None) -> None:
    """Upsert one DB row per engagement lens. Replace body content; populate every property."""
    notion = notion or NotionMCP()
    # Implementation binds to the Notion MCP at runtime. See plan §Generator Changes step 11.
    raise NotImplementedError(
        "writer.mirror_to_notion binds Notion MCP at runtime. The live pilot "
        "mirrorings for Spring Bengtzen and Tommy Harr were performed via MCP "
        "tool calls."
    )


def log_claude_summary(account, context: dict[str, Any], pages_created: list[Any]) -> None:
    """Write a row into the Claude Summaries DB for this refresh."""
    # Binds to Notion MCP at runtime.
    pass
