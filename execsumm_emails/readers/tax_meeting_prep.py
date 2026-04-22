"""Tax Meeting Prep doc/sheet reader. Source tag: `[MtgPrep <date>]`."""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - needs Drive mount
    raise NotImplementedError("tax_meeting_prep.read requires Drive mount.")
