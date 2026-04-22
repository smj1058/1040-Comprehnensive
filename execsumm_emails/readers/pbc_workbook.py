"""PBC Workbook reader — entity list, property schedule, books coverage.

Source tag format: `[PBC:<Tab>!<Cell/Row>]`.
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - needs Drive mount
    """Download the PBC workbook from Drive and distill the standard tabs.

    Expected tabs:
      - Entities            → entity list with federal form, ownership, state
      - Properties          → property schedule
      - Trial Balance       → per-entity TB and books coverage month
      - Tax Prep            → return-year working papers
      - Notes               → narrative about the client's books

    Returns a dict with keys: entities, properties, books_coverage, notes, sha.
    Also writes the full extraction JSON to extracts/.
    """
    raise NotImplementedError(
        "pbc_workbook.read requires Drive mount / openpyxl. Run inside the "
        "Drive-mounted environment."
    )
