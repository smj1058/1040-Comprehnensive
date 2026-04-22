"""Thin wrapper over Notion MCP / the official SDK.

In live runs this binds to the Notion MCP server (the `notion-fetch`,
`notion-search`, `notion-query-data-sources`, `notion-update-page`,
`notion-create-pages` tools). For now the class exposes a minimal contract so
other modules can depend on it without pulling the MCP transport into imports.
"""

from __future__ import annotations

from typing import Any


class NotionMCP:
    def find_account(self, client_name: str) -> dict[str, Any]:  # pragma: no cover - MCP
        raise NotImplementedError

    def list_clients_in_exec_summary_index(self) -> list[str]:  # pragma: no cover - MCP
        raise NotImplementedError

    def fetch(self, page_id_or_url: str) -> dict[str, Any]:  # pragma: no cover - MCP
        raise NotImplementedError

    def query(self, data_source_url: str, sql: str, params: list[str] | None = None) -> list[dict[str, Any]]:  # pragma: no cover - MCP
        raise NotImplementedError

    def replace_content(self, page_id: str, new_markdown: str) -> None:  # pragma: no cover - MCP
        raise NotImplementedError

    def update_properties(self, page_id: str, properties: dict[str, Any]) -> None:  # pragma: no cover - MCP
        raise NotImplementedError

    def create_page(self, parent_data_source_id: str, properties: dict[str, Any], content: str) -> str:  # pragma: no cover - MCP
        raise NotImplementedError

    @staticmethod
    def urls(relation_value: Any) -> list[str]:
        if not relation_value:
            return []
        if isinstance(relation_value, str):
            import json
            try:
                parsed = json.loads(relation_value)
                return parsed if isinstance(parsed, list) else [parsed]
            except json.JSONDecodeError:
                return [relation_value]
        if isinstance(relation_value, list):
            return list(relation_value)
        return []

    @classmethod
    def first(cls, relation_value: Any) -> str | None:
        urls = cls.urls(relation_value)
        return urls[0] if urls else None
