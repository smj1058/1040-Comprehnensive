"""CLI entry point: `execsumm refresh <client>` / `execsumm refresh-all`.

This is a scaffold. The live pilot runs for Spring Bengtzen and Tommy Harr were
produced via Notion/Outlook/Granola MCP tool calls and saved under
`dossiers/`. The scaffold here defines the pipeline contract that will be
executed inside the Drive-mounted environment where the large workbooks, memos,
and transcripts are reachable.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import account_loader, merge, template, writer
from .readers import (
    claude_chats,
    emails,
    insights_workbook,
    notion_sources,
    pbc_workbook,
    tax_analysis,
    tax_meeting_prep,
    tax_memo,
    transcripts,
)


def refresh_one(client: str) -> Path:
    """Full per-client pipeline. Returns the path of the .md written."""
    account = account_loader.load(client)

    context = {
        "account": account,
        "pbc": pbc_workbook.read(account),
        "insights_workbook": insights_workbook.read(account),
        "tax_analysis": tax_analysis.read(account),
        "tax_memo": tax_memo.read(account),
        "tax_meeting_prep": tax_meeting_prep.read(account),
        "transcripts": transcripts.read(account),
        "emails": emails.read(account),
        "claude_chats": claude_chats.read(account),
        "notion_sources": notion_sources.read(account),
    }

    prior = merge.load_prior_dossier(account)
    context["changed"] = merge.diff(prior, context)

    markdown = template.render(context, prior=prior)
    drive_path, local_path = writer.write_drive_and_local(account, markdown)
    writer.mirror_to_notion(account, markdown, context)
    writer.log_claude_summary(account, context, pages_created=[drive_path])
    return local_path


def refresh_all() -> list[Path]:
    clients = account_loader.all_in_exec_summary_index()
    return [refresh_one(c) for c in clients]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="execsumm")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_one = sub.add_parser("refresh", help="Refresh one client's dossier.")
    p_one.add_argument("client", help="Client name (matches an Account.Account Name).")

    sub.add_parser("refresh-all", help="Refresh every client in the Exec Summary index.")

    args = parser.parse_args(argv)
    if args.cmd == "refresh":
        path = refresh_one(args.client)
        print(f"Wrote {path}")
    elif args.cmd == "refresh-all":
        for path in refresh_all():
            print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
