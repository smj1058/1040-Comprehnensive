"""Rule-based opportunity flags — Cost Seg candidates + S-Corp election candidates.

Runs on every refresh. Produces two tables the template renders into §8a of
the dossier. Cross-references Cost Seg Proposals / Engagements and FileForms
Engagements so already-in-flight opportunities are marked `In Progress`
instead of `Open`.

The live Spring Bengtzen and Tommy Harr pilot dossiers exercise this
classifier — see their §8a output for the end-to-end shape.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Literal

Priority = Literal["HIGH", "MEDIUM", "LOW", "NOT APPLICABLE", "IN PROGRESS"]

# 2026 bonus depreciation phasedown (TCJA). Update annually.
BONUS_RATE_BY_YEAR = {
    2023: 0.80,
    2024: 0.60,
    2025: 0.40,
    2026: 0.60,  # extended per current law — update when confirmed
    2027: 0.40,
}


@dataclass
class CostSegFlag:
    property_name: str
    entity_owner: str
    basis: float
    placed_in_service: date | None
    study_status: str  # "None", "In Progress", "Completed", "Not Applicable"
    est_bonus_depreciation: float
    priority: Priority
    basis_of_flag: str
    source_tag: str


@dataclass
class SCorpFlag:
    entity: str
    current_classification: str  # "LLC-partnership", "Sch C", "LLC-disregarded", "1120", ...
    net_se_earnings_2025: float
    reasonable_salary: float
    est_se_savings: float
    priority: Priority
    basis_of_flag: str
    source_tag: str


def _years_since(d: date | None) -> int | None:
    if d is None:
        return None
    return (date.today() - d).days // 365


def _owner_has_reps_or_active(account) -> bool:
    """Placeholder — caller supplies the determination from the Insights
    Workbook / Tax Analysis / memo.
    """
    return bool(getattr(account, "reps_status", False) or getattr(account, "has_active_offset_income", False))


def cost_seg_candidates(properties: list[dict[str, Any]], account, *, known_studies: list[str] | None = None) -> list[CostSegFlag]:
    known_studies = known_studies or []
    flags: list[CostSegFlag] = []
    current_year = date.today().year
    bonus_rate = BONUS_RATE_BY_YEAR.get(current_year, 0.60)

    for p in properties:
        basis = float(p.get("basis", 0) or 0)
        name = p.get("name") or p.get("address") or "(unnamed property)"
        owner = p.get("entity_owner") or "—"
        placed = p.get("placed_in_service")
        study_status = p.get("study_status") or "None"
        type_ = (p.get("type") or "").lower()
        years = _years_since(placed)

        reasons: list[str] = []

        # Exclusions
        if type_ in {"flip", "wholesale", "inventory"}:
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, 0.0, "NOT APPLICABLE",
                                     "Flip/inventory — held for sale, not depreciable.", p.get("source_tag", "[PBC:Properties]")))
            continue
        if p.get("personal_use_pct", 0) >= 0.20 and "triplex" not in name.lower():
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, 0.0, "NOT APPLICABLE",
                                     f"Personal use {p.get('personal_use_pct', 0):.0%} ≥ 20%.", p.get("source_tag", "[PBC:Properties]")))
            continue
        if study_status == "Completed":
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, 0.0, "NOT APPLICABLE",
                                     "Study already completed.", p.get("source_tag", "[PBC:Properties]")))
            continue
        if study_status == "In Progress" or any(name in s for s in known_studies):
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, basis * 0.25 * bonus_rate, "IN PROGRESS",
                                     f"Study in flight; est. first-year depreciation at {bonus_rate:.0%} bonus ≈ 25% of basis.", p.get("source_tag", "[PBC:Properties]")))
            continue

        # Positive candidates
        use_path_ok = _owner_has_reps_or_active(account) or type_ in {"str", "short-term rental"}
        est = basis * 0.25 * bonus_rate  # rough — land excluded, ~25% typical 5/15-yr reclass on residential

        if basis >= 200_000 and (years is None or years <= 3) and use_path_ok:
            reasons.append(f"basis ${basis:,.0f} ≥ $200K")
            reasons.append(f"placed in service {years} yr ago" if years is not None else "recent acquisition")
            reasons.append("loss usability path present (REPS/STR/active)")
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, est, "HIGH",
                                     "; ".join(reasons), p.get("source_tag", "[PBC:Properties]")))
        elif basis >= 75_000 or (years is not None and years <= 3):
            reasons.append(f"basis ${basis:,.0f}")
            reasons.append("bonus window still open" if (years is None or years <= 3) else "older acquisition")
            if not use_path_ok:
                reasons.append("REPS/active not yet established — losses may suspend")
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, est, "MEDIUM",
                                     "; ".join(reasons), p.get("source_tag", "[PBC:Properties]")))
        else:
            flags.append(CostSegFlag(name, owner, basis, placed, study_status, est, "LOW",
                                     f"basis ${basis:,.0f} below $75K threshold.", p.get("source_tag", "[PBC:Properties]")))

    return flags


def s_corp_candidates(entities: list[dict[str, Any]], account, *, open_fileforms_engagements: list[str] | None = None) -> list[SCorpFlag]:
    open_fileforms_engagements = open_fileforms_engagements or []
    flags: list[SCorpFlag] = []

    for e in entities:
        name = e.get("name", "(unnamed entity)")
        classification = e.get("classification") or e.get("federal_form") or "—"
        net_se = float(e.get("net_se_earnings_2025", 0) or 0)
        activity = (e.get("activity") or "").lower()
        passive = "rental" in activity or "holding" in activity or e.get("passive_only", False)
        appreciated_re = e.get("holds_appreciated_re", False)

        # In flight already?
        if any(name in eng for eng in open_fileforms_engagements):
            flags.append(SCorpFlag(name, classification, net_se, 0.0, 0.0, "IN PROGRESS",
                                   "FileForms S-corp election engagement in flight.",
                                   e.get("source_tag", "[PBC:Entities]")))
            continue

        # Exclusions
        if classification in {"1120S"}:
            flags.append(SCorpFlag(name, classification, net_se, 0.0, 0.0, "NOT APPLICABLE",
                                   "Already electing S-corp status.", e.get("source_tag", "[PBC:Entities]")))
            continue
        if passive and appreciated_re:
            flags.append(SCorpFlag(name, classification, net_se, 0.0, 0.0, "NOT APPLICABLE",
                                   "Passive rental holding with appreciated RE — S election triggers distribution gain recognition risk.",
                                   e.get("source_tag", "[PBC:Entities]")))
            continue
        if passive and net_se < 10_000:
            flags.append(SCorpFlag(name, classification, net_se, 0.0, 0.0, "NOT APPLICABLE",
                                   "Passive/minimal SE earnings — no SE tax to eliminate.",
                                   e.get("source_tag", "[PBC:Entities]")))
            continue

        reasonable_salary = max(round(net_se * 0.30 / 1000) * 1000, 45_000) if net_se >= 80_000 else round(net_se * 0.30 / 1000) * 1000
        est_savings = max(0.0, (net_se - reasonable_salary) * 0.1413)  # 15.3% less FUTA interaction, roughly

        if net_se >= 80_000:
            flags.append(SCorpFlag(name, classification, net_se, reasonable_salary, est_savings, "HIGH",
                                   f"Net SE earnings ${net_se:,.0f} ≥ $80K — salary target ~${reasonable_salary:,.0f}, est. SE savings ${est_savings:,.0f}/yr.",
                                   e.get("source_tag", "[PBC:Entities]")))
        elif net_se >= 40_000:
            flags.append(SCorpFlag(name, classification, net_se, reasonable_salary, est_savings, "MEDIUM",
                                   f"Net SE earnings ${net_se:,.0f} — near threshold; review growth trajectory + payroll complexity.",
                                   e.get("source_tag", "[PBC:Entities]")))
        else:
            flags.append(SCorpFlag(name, classification, net_se, 0.0, 0.0, "LOW",
                                   f"Net SE earnings ${net_se:,.0f} below $40K — compliance burden likely exceeds savings.",
                                   e.get("source_tag", "[PBC:Entities]")))

    return flags


def as_markdown(cost_seg: list[CostSegFlag], s_corp: list[SCorpFlag]) -> str:
    lines = ["### 8a. Opportunity Flags (auto-detected)", ""]

    lines.append("**Cost Segregation Candidates**")
    lines.append("")
    lines.append("| Property | Entity Owner | Basis | Placed in Service | Study Status | Est. Bonus Dep | Priority | Basis of Flag | Source |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for f in cost_seg:
        lines.append(
            f"| {f.property_name} | {f.entity_owner} | ${f.basis:,.0f} | "
            f"{f.placed_in_service or '—'} | {f.study_status} | "
            f"${f.est_bonus_depreciation:,.0f} | **{f.priority}** | {f.basis_of_flag} | `{f.source_tag}` |"
        )
    lines.append("")

    lines.append("**S-Corp Election Candidates**")
    lines.append("")
    lines.append("| Entity | Current Classification | 2025 Net SE | Reasonable Salary | Est. SE Savings | Priority | Basis of Flag | Source |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for f in s_corp:
        lines.append(
            f"| {f.entity} | {f.current_classification} | ${f.net_se_earnings_2025:,.0f} | "
            f"${f.reasonable_salary:,.0f} | ${f.est_se_savings:,.0f} | **{f.priority}** | "
            f"{f.basis_of_flag} | `{f.source_tag}` |"
        )
    lines.append("")
    lines.append(
        "> Any `HIGH` flag above is automatically promoted into §10 Critical Open Items. "
        "Flags already marked `IN PROGRESS` are cross-referenced against the Cost Seg "
        "Engagements and FileForms Engagements databases so they're not double-counted."
    )
    return "\n".join(lines)
