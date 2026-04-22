"""Insights Delivery Workbook (Tax Extraction) reader.

Source tag format: `[Insights:<Tab>!<Row>]`.
Produces: prior-year AGI, taxable income, total tax, effective rate, SE tax,
entity P&L slots, strategy candidates.
"""

from __future__ import annotations

from typing import Any


def read(account) -> dict[str, Any]:  # pragma: no cover - needs Drive mount
    raise NotImplementedError(
        "insights_workbook.read requires Drive mount / openpyxl."
    )
