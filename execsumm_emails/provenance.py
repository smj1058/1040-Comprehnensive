"""Source-tag formatting + Provenance Index builder.

Every non-obvious fact in the dossier is tagged inline:

  `[PBC:Entities!A14]`
  `[Insights:Projections!Row7]`
  `[TaxAnalysis:Summary!B12]`
  `[Memo 2025-12-10 §CostSeg]`
  `[MtgPrep 2026-04-08]`
  `[Email 2026-03-11 Seth→Spring "Open Items"]`
  `[EI:Re: Spring B - Open Items]`
  `[Granola 2025-12-03 Tax Strategy]`
  `[Fellow 2026-03-18 Tax Planning 30min Review]`
  `[Claude 2026-04-14 Spring Bengtzen Dossier Refresh]`
  `[Inquiry #42]`
  `[SR #17]`
  `[Intake #103]`
  `[AI:2026-02-19 Planning #3]`
  `[Controversy:IRS-CP2000-2025-02-14]`
  `[FF 2026-04-10]`
  `[WP:Watbash_Piney_CostSeg_2025]`
  `[EL 2026-02-02]`

The Provenance Index at the foot of every dossier lists every tag used in the
document with a direct link.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    tag: str
    kind: str  # PBC / Insights / TaxAnalysis / Memo / MtgPrep / Email / EI / Granola / Fellow / Claude / Inquiry / SR / Intake / AI / Controversy / FF / WP / EL
    link: str


def build_index(sources: list[Source]) -> str:
    seen = sorted({s.tag: s for s in sources}.items())
    if not seen:
        return ""
    lines = ["## 16. Provenance Index", ""]
    for tag, src in seen:
        lines.append(f"- `{tag}` — [{src.kind}]({src.link})")
    return "\n".join(lines)
