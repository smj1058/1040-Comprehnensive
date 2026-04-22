"""Tax Planning Memo (.docx) reader. Source tag: `[Memo <date> §<section>]`."""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - needs Drive mount
    raise NotImplementedError("tax_memo.read requires python-docx + Drive mount.")
