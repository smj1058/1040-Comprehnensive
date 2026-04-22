"""Source readers. Each module exposes `read(account) -> dict` returning the
distilled extraction for that source, with source-tag-able structure.

Readers must:
- Download / fetch the full file or record (no sampling for large files).
- Write a sidecar JSON to `extracts/<Client>_<source>_<YYYY-MM-DD>.extract.json`.
- Return a dict the template renderer can cite with inline source tags.
"""
