"""Tax Analysis Workbook reader. Source tag: `[TaxAnalysis:<Tab>!<Row>]`."""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - needs Drive mount
    raise NotImplementedError("tax_analysis.read requires Drive mount / openpyxl.")
