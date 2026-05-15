#!/usr/bin/env python3
"""
Generate Phase 1 triage markdown from `_data/kb_articles.csv`.

Writes:
  - `_data/kb_articles_skipped.md` — skipped rows with a one-line explanation each.
  - `_data/kb_articles_actioned.md` — actionable backlog, batched by shared primary
    doc target and grouped by inferred vertical (IA bucket) + CSV `team`.

If `_data/kb_epic_bd6308_tracked_article_ids.txt` exists, `article_id` values listed there
(typically copied from Jira issues under Epic **BD-6308**) are excluded from the actionable
markdown and counted as skipped so the file does not duplicate in-flight epic work.

Usage (from repo root):
  python3 scripts/generate_kb_phase1_outputs.py

Gates align with `.cursor/rules/salesforce-analyzer.mdc` Phase 1 (automated subset).
Does not re-read doc bodies for “redundant with docs” or bug-workaround detection;
those remain manual Phase 1 checks.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import AbstractSet

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "_data" / "kb_articles.csv"
SKIPPED_OUT = REPO_ROOT / "_data" / "kb_articles_skipped.md"
ACTIONED_OUT = REPO_ROOT / "_data" / "kb_articles_actioned.md"
EPIC_BD6308_TRACKED_IDS_PATH = REPO_ROOT / "_data" / "kb_epic_bd6308_tracked_article_ids.txt"

_DOCS_PATH_RE = re.compile(
    r"(?:braze-docs/)?(_docs/[^\s\"'<>()]+)",
    re.IGNORECASE,
)

# Substrings in conflict_resolution that default to skip (see salesforce-analyzer.mdc).
CONFLICT_SKIP_SUBSTRINGS = (
    "human review",
    "no source",
    "codebase inconclusive",
    "inconclusive —",
)

# First-line suggested_change starters treated as non-actionable briefs.
VAGUE_STARTERS = (
    "might ",
    "may ",
    "consider reviewing",
    "review ",
    "tbd",
    "unclear",
    "needs investigation",
    "needs sme",
    "flag for",
)

# Ordered path fragment remaps (CSV often uses retired IA paths).
PATH_FRAG_REMAPS: tuple[tuple[str, str], ...] = (
    ("_user_guide/engagement_tools/", "_user_guide/messaging/"),
    ("_user_guide/message_building_by_channel/", "_user_guide/channels/"),
    ("_user_guide/channels/email/reporting_and_analytics/", "_user_guide/channels/email/reporting/"),
    ("_user_guide/data_and_analytics/", "_user_guide/data/"),
    ("_user_guide/documentation/", "_user_guide/analytics/"),
    ("_user_guide/docs_author_platform/", "_user_guide/messaging/"),
    ("/document/", "/sms_mms_and_rcs/"),
    ("reeligibility", "re_eligibility"),
    ("dataplatform", "data_platform"),
)


def normalized_implementation_status(raw: str | None) -> str:
    if not raw or not str(raw).strip():
        return ""
    first_line = str(raw).strip().split("\n", 1)[0].strip()
    return first_line.lower()


def strip_line_range_suffix(path: str) -> str:
    """`_docs/_api/errors.md:19-28` -> `_docs/_api/errors.md`."""
    return re.sub(r":\d+(?:-\d+)?$", "", path)


def apply_path_remaps(path: str) -> str:
    out = path.replace("\\", "/")
    for old, new in PATH_FRAG_REMAPS:
        out = out.replace(old, new)
    return out


def extract_doc_paths(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
) -> list[str]:
    """Return unique `_docs/...` paths (excluding help_articles), in discovery order."""
    seen: set[str] = set()
    out: list[str] = []
    chunks = [doc_path or "", codebase_evidence or "", suggested_change or ""]
    for chunk in chunks:
        for m in _DOCS_PATH_RE.finditer(chunk):
            p = m.group(1).strip().rstrip(").,;`:")
            p = strip_line_range_suffix(p)
            if "_docs/_help/help_articles" in p:
                continue
            if not p.startswith("_docs/"):
                continue
            if p not in seen:
                seen.add(p)
                out.append(p)
    return out


def resolve_existing_path(raw: str, root: Path) -> Path | None:
    """Return first Path that exists on disk after remaps and .md fallbacks."""
    candidates: list[Path] = []
    p = apply_path_remaps(raw.strip())
    p = strip_line_range_suffix(p)
    full = root / p
    candidates.append(full)
    if full.suffix.lower() != ".md":
        candidates.append(full.with_suffix(".md"))
    for c in candidates:
        try:
            if c.is_file():
                return c
        except OSError:
            continue
    # If path is directory-ish, try index (rare in CSV)
    if full.suffix == "":
        for name in ("index.md", "home.md"):
            alt = full / name
            if alt.is_file():
                return alt
    return None


def resolved_primary_doc(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
    root: Path,
) -> tuple[str | None, Path | None]:
    """
    First `_docs/...` path from row fields that resolves to a file under `root`.
    Returns (normalized `_docs/...` string relative to repo, resolved Path or None).
    """
    for raw in extract_doc_paths(doc_path, codebase_evidence, suggested_change):
        hit = resolve_existing_path(raw, root)
        if hit:
            try:
                rel = hit.relative_to(root)
                rel_s = rel.as_posix()
                if rel_s.startswith("_docs/"):
                    return rel_s, hit
            except ValueError:
                pass
    return None, None


def help_only_paths(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
) -> bool:
    """True if every extracted _docs path is under help_articles (and at least one exists)."""
    all_paths: list[str] = []
    for chunk in (doc_path or "", codebase_evidence or "", suggested_change or ""):
        for m in _DOCS_PATH_RE.finditer(chunk):
            all_paths.append(m.group(1).strip().rstrip(").,;"))
    docs_hits = [p for p in all_paths if p.startswith("_docs/")]
    if not docs_hits:
        return False
    return all("_help/help_articles" in p for p in docs_hits)


def has_substantive_docs_hint(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
) -> bool:
    """Any `_docs/` reference outside help_articles in row text."""
    for chunk in (doc_path or "", codebase_evidence or "", suggested_change or ""):
        for m in _DOCS_PATH_RE.finditer(chunk):
            p = m.group(1)
            if "_help/help_articles" in p:
                continue
            if p.startswith("_docs/"):
                return True
    return False


def infer_vertical(primary_rel: str | None, team: str) -> str:
    """IA bucket for batching (path-first, then team)."""
    if not primary_rel:
        return f"unknown ({team or 'no team'})"
    parts = primary_rel.split("/")
    if len(parts) >= 3 and parts[0] == "_docs":
        if parts[1] == "_user_guide" and len(parts) >= 3:
            return parts[2]
        if parts[1] in ("_api", "_developer_guide", "_partners", "_hidden", "_docs_pages", "_releases"):
            return parts[1].lstrip("_")
    return "other"


def conflict_resolution_skip(raw: str | None) -> str | None:
    if not raw:
        return None
    low = raw.strip().lower()
    if low == "inconclusive":
        return "conflict_resolution is `inconclusive` (no justified concrete docs change)."
    for sub in CONFLICT_SKIP_SUBSTRINGS:
        if sub in low:
            return f"conflict_resolution signals manual skip (`{sub}`)."
    return None


def is_vague_suggested_change(raw: str | None) -> bool:
    if not raw or not str(raw).strip():
        return True
    first = str(raw).strip().split("\n", 1)[0].strip().lower()
    return any(first.startswith(s) for s in VAGUE_STARTERS)


@dataclass
class RowOut:
    row: dict[str, str]
    primary_rel: str | None = None
    resolved_path: Path | None = None
    vertical: str = ""
    skip_reason: str | None = None
    skip_context: str | None = None


def classify_row(
    row: dict[str, str],
    root: Path,
    epic_bd6308_tracked_ids: AbstractSet[str],
) -> RowOut:
    article_id = (row.get("article_id") or "").strip()
    title = (row.get("title") or "").strip()
    team = (row.get("team") or "").strip()
    target = (row.get("target") or "").strip().lower()
    impl = normalized_implementation_status(row.get("implementation_status"))
    cr = row.get("conflict_resolution") or ""
    suggested = row.get("suggested_change")
    doc_path = row.get("doc_path")
    evidence = row.get("codebase_evidence")

    def skip(msg: str, ctx: str | None = None) -> RowOut:
        return RowOut(row=row, skip_reason=msg, skip_context=ctx)

    if impl == "archived":
        return skip(
            "`implementation_status` first line is `archived`.",
            ctx="Dispositioned KA; do not draft new public docs work from this row.",
        )
    if impl == "actioned":
        return skip(
            "`implementation_status` first line is `actioned`.",
            ctx="Work already recorded as done or superseded in the migration tracker.",
        )
    if impl and impl not in ("", "to be actioned", "delta ka"):
        raw_first = str(row.get("implementation_status") or "").strip().split("\n", 1)[0].strip()
        return skip(
            f"`implementation_status` first line is `{impl}` — unlisted or non-public disposition; "
            "default skip per salesforce-analyzer rule.",
            ctx=f"Raw first line: `{raw_first}`.",
        )

    if target == "inconclusive":
        return skip(
            "`target` is `inconclusive`.",
            ctx="Outcome surface for the row is unclear; do not open a Phase 2 docs PR without analyst override.",
        )
    if cr.strip().lower() == "inconclusive":
        ctx = None
        con = (row.get("conflict") or "").strip().replace("\n", " ")
        if con:
            ctx = f"Analyzer context (truncated): {con[:220]}{'…' if len(con) > 220 else ''}"
        return skip(
            "`conflict_resolution` is `inconclusive`.",
            ctx=ctx
            or "The pre-analysis did not justify a concrete Braze Docs change.",
        )

    crs = conflict_resolution_skip(cr)
    if crs:
        cr_trim = cr.strip().replace("\n", " ")
        ctx = f"`conflict_resolution` (raw): {cr_trim[:240]}{'…' if len(cr_trim) > 240 else ''}"
        return skip(crs, ctx=ctx)

    if not suggested or not str(suggested).strip():
        return skip(
            "`suggested_change` is empty or whitespace.",
            ctx="Add a concrete implementation brief before Phase 2.",
        )

    if is_vague_suggested_change(suggested):
        first = str(suggested).strip().split("\n", 1)[0].strip()
        return skip(
            "`suggested_change` is vague or lacks a concrete first-line edit "
            "(starts with a non-actionable phrase per script heuristics).",
            ctx=f"First line: `{first}`",
        )

    if help_only_paths(doc_path, evidence, suggested):
        hp = [m.group(1) for m in _DOCS_PATH_RE.finditer(" ".join(filter(None, [doc_path, evidence, suggested])))]
        hp = [p.strip().rstrip(").,;`") for p in hp if "_help/help_articles" in p][:4]
        ctx = "Paths: " + ", ".join(f"`{p}`" for p in hp) if hp else "All `_docs` hits point at internal help mirrors."
        return skip(
            "All extracted `_docs/...` paths are under `_docs/_help/help_articles/` (not a public edit target).",
            ctx=ctx,
        )

    if target == "knowledge_article" and not has_substantive_docs_hint(doc_path, evidence, suggested):
        return skip(
            "`target` is `knowledge_article` and the row has no substantive `_docs/` hint "
            "(KA-only / no Braze Docs PR from CSV).",
            ctx="Archive/consolidation-only work with no `_docs/...` path in `doc_path`, evidence, or `suggested_change`.",
        )

    primary_rel, rpath = resolved_primary_doc(doc_path, evidence, suggested, root)
    if not primary_rel:
        extracted = extract_doc_paths(doc_path, evidence, suggested)
        if extracted:
            shown = ", ".join(f"`{p}`" for p in extracted[:5])
            if len(extracted) > 5:
                shown += f", … (+{len(extracted) - 5} more)"
            ctx = (
                f"Extracted `_docs` candidates (none resolve to a file on disk after IA remaps): {shown}. "
                "Fix `doc_path` / evidence paths or extend remaps in `scripts/generate_kb_phase1_outputs.py`."
            )
        else:
            ctx = (
                "No `_docs/...` strings found in `doc_path`, `codebase_evidence`, or `suggested_change` "
                "(or only non-doc targets such as `platform/...` without a docs path)."
            )
        return skip(
            "No locatable on-disk `_docs/...` target after path extraction and IA remaps "
            "(insufficient CSV path, stale path, or needs manual `doc_path` fix).",
            ctx=ctx,
        )

    if article_id in epic_bd6308_tracked_ids:
        return skip(
            "Article is listed on a Jira issue under Epic **BD-6308** (Round 2); excluded from "
            "`kb_articles_actioned.md` so the CSV backlog file does not duplicate epic-tracked Phase 2 work.",
            ctx=(
                "Remove this `article_id` from `_data/kb_epic_bd6308_tracked_article_ids.txt` only after "
                "the migration task is cancelled or the article is intentionally re-queued outside the epic."
            ),
        )

    vert = infer_vertical(primary_rel, team)
    return RowOut(
        row=row,
        primary_rel=primary_rel,
        resolved_path=rpath,
        vertical=vert,
        skip_reason=None,
    )


def load_epic_bd6308_tracked_ids(path: Path) -> frozenset[str]:
    """
    One Salesforce `article_id` per non-comment, non-blank line.
    Used to omit rows already filed under Jira Epic BD-6308 from the actionable markdown queue.
    """
    if not path.is_file():
        return frozenset()
    out: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        out.add(s)
    return frozenset(out)


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        print(f"Missing input: {path}", file=sys.stderr)
        sys.exit(2)
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def score_key(row: dict[str, str]) -> tuple[int, float, str]:
    tier_s = (row.get("priority_tier") or "9").strip()
    try:
        tier = int(float(tier_s))
    except ValueError:
        tier = 9
    sc_s = (row.get("score") or "0").strip()
    try:
        sc = float(sc_s)
    except ValueError:
        sc = 0.0
    title = (row.get("title") or "").strip().lower()
    return (tier, -sc, title)


def main() -> None:
    rows = load_csv_rows(CSV_PATH)
    epic_tracked = load_epic_bd6308_tracked_ids(EPIC_BD6308_TRACKED_IDS_PATH)
    classified: list[RowOut] = [classify_row(r, REPO_ROOT, epic_tracked) for r in rows]

    skipped = [c for c in classified if c.skip_reason]
    actionable = [c for c in classified if not c.skip_reason]

    skipped.sort(key=lambda c: (c.skip_reason or "", c.row.get("article_id") or ""))
    actionable.sort(key=lambda c: score_key(c.row))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # --- skipped.md ---
    by_reason: dict[str, list[RowOut]] = defaultdict(list)
    for c in skipped:
        by_reason[c.skip_reason or "unknown"].append(c)

    skip_lines = [
        "# KB articles — Phase 1 skipped rows",
        "",
        f"Generated from `{CSV_PATH.relative_to(REPO_ROOT)}` on **{now}**.",
        "",
        "Most rows below failed an automated Phase 1 gate from `.cursor/rules/salesforce-analyzer.mdc`. "
        "Rows skipped only because they appear in `_data/kb_epic_bd6308_tracked_article_ids.txt` "
        "would otherwise be actionable — they are excluded so this queue does not duplicate Jira Epic **BD-6308** work. "
        "Redundant-with-live-docs, bug-workaround-only, and other manual checks are **not** applied here.",
        "",
        f"**Totals:** {len(rows)} CSV rows — **{len(actionable)} actionable**, **{len(skipped)} skipped**.",
        "",
    ]
    for reason in sorted(by_reason.keys(), key=lambda s: (-len(by_reason[s]), s)):
        items = by_reason[reason]
        skip_lines.append(f"## {reason}")
        skip_lines.append("")
        skip_lines.append(f"**Count:** {len(items)}")
        skip_lines.append("")
        for c in sorted(items, key=lambda x: x.row.get("article_id") or ""):
            rid = (c.row.get("article_id") or "").strip()
            ttl = (c.row.get("title") or "").strip()
            skip_lines.append(f"- **`{rid}`** — {ttl}")
            detail = (c.skip_context or c.skip_reason or "").strip()
            if detail:
                skip_lines.append(f"  - *Explanation:* {detail}")
        skip_lines.append("")

    SKIPPED_OUT.parent.mkdir(parents=True, exist_ok=True)
    SKIPPED_OUT.write_text("\n".join(skip_lines).rstrip() + "\n", encoding="utf-8")

    # --- actioned.md (actionable backlog, not CSV status "Actioned") ---
    by_file: dict[str, list[RowOut]] = defaultdict(list)
    by_vertical: dict[str, list[RowOut]] = defaultdict(list)
    for c in actionable:
        assert c.primary_rel
        by_file[c.primary_rel].append(c)
        by_vertical[c.vertical].append(c)

    multi_file = {k: v for k, v in by_file.items() if len(v) > 1}
    multi_sorted = sorted(multi_file.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    epic_skip_n = sum(1 for c in skipped if "BD-6308" in (c.skip_reason or ""))
    act_lines = [
        "# KB articles — Phase 1 actionable backlog",
        "",
        f"Generated from `{CSV_PATH.relative_to(REPO_ROOT)}` on **{now}**.",
        "",
        "These rows passed automated Phase 1 gates and resolve to an on-disk `_docs/...` file. "
        "They are **not** marked `actioned` in the CSV — this file is a **work queue** for Phase 2.",
        "",
        f"**Totals:** **{len(actionable)}** actionable rows (of {len(rows)}).",
    ]
    if epic_tracked and epic_skip_n:
        act_lines.append(
            f"**Epic BD-6308:** **{epic_skip_n}** additional rows would have appeared here but are listed in "
            f"`{EPIC_BD6308_TRACKED_IDS_PATH.relative_to(REPO_ROOT)}` (Jira child issues under the epic); "
            "see `_data/kb_articles_skipped.md` for those rows."
        )
    act_lines.extend(
        [
            "",
            "## 1. Multi-article batches (same primary doc)",
            "",
            "Use when several articles should land in **one PR** touching the same file.",
            "",
        ]
    )
    if not multi_sorted:
        act_lines.append("_No groups of 2+ articles share the same resolved primary file._")
        act_lines.append("")
    else:
        for path_key, group in multi_sorted:
            act_lines.append(f"### `{path_key}` — **{len(group)}** articles")
            act_lines.append("")
            for c in sorted(group, key=lambda x: score_key(x.row)):
                r = c.row
                act_lines.append(
                    f"- **`{r.get('article_id', '').strip()}`** — {r.get('title', '').strip()} "
                    f"(tier {r.get('priority_tier', '')}, score {r.get('score', '')}; team `{r.get('team', '')}`)"
                )
            act_lines.append("")

    act_lines.extend(
        [
            "## 2. Batches by vertical (IA bucket) and team",
            "",
            "Within each vertical, rows are sorted by **tier ascending**, **score descending**, then title.",
            "",
        ]
    )
    for vert in sorted(by_vertical.keys(), key=lambda v: v.lower()):
        group = by_vertical[vert]
        by_team: dict[str, list[RowOut]] = defaultdict(list)
        for c in group:
            by_team[(c.row.get("team") or "").strip() or "(empty team)"].append(c)

        act_lines.append(f"### Vertical: `{vert}` — **{len(group)}** articles")
        act_lines.append("")

        for tm in sorted(by_team.keys(), key=str.lower):
            tg = by_team[tm]
            act_lines.append(f"#### Team: `{tm}` — {len(tg)} articles")
            act_lines.append("")
            act_lines.append("| Tier | Score | article_id | Title | Primary `_docs` target |")
            act_lines.append("| --- | --- | --- | --- | --- |")
            for c in sorted(tg, key=lambda x: score_key(x.row)):
                r = c.row
                ttl = (r.get("title") or "").replace("|", "\\|")
                act_lines.append(
                    f"| {r.get('priority_tier', '')} | {r.get('score', '')} | `{r.get('article_id', '')}` "
                    f"| {ttl} | `{c.primary_rel}` |"
                )
            act_lines.append("")

    ACTIONED_OUT.write_text("\n".join(act_lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote {SKIPPED_OUT.relative_to(REPO_ROOT)} ({len(skipped)} skipped)")
    print(f"Wrote {ACTIONED_OUT.relative_to(REPO_ROOT)} ({len(actionable)} actionable)")


if __name__ == "__main__":
    main()
