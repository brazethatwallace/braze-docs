"""Propagate glossary audit changes into ``_lang/`` locale markdown.

When the weekly glossary audit adds a term or updates a translation, this
module searches the matching locale tree and applies safe in-prose replacements
(English source term or outdated translation → current glossary value).

Skipped by design: code fences, ``image_buster`` paths, markdown link URL targets,
Liquid alert keys, glossary YAML identifiers, structural front matter (``permalink``, ``link``,
``search_tag``, ``tool``, ``channel``, etc.), URLs, asset paths, and a small
set of partner/UI literals (e.g. Segment.com).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
PROPAGATION_EXCLUSIONS_PATH = (
    SCRIPTS_DIR / "phrase_glossary_locale_propagation_exclusions.json"
)
HEADING_ANCHOR_RE = re.compile(r"\{#[^}]+\}")

# Glossary JSON keys (``scripts/glossaries/{lang}.json``) → ``_lang/`` folders.
LANG_GLOSSARY_TO_DIR = {
    "de": "de",
    "es": "es",
    "fr": "fr_fr",
    "ja": "ja",
    "ko": "ko",
    "pt-br": "pt_br",
}

IMAGE_BUSTER_RE = re.compile(r"\{%\s*image_buster\s+[^%]+%\}", re.IGNORECASE)
FENCE_LINE_RE = re.compile(r"^(?P<ticks>`{3,})(?P<rest>.*)$")


def _fence_line(line: str) -> tuple[int, str | None] | None:
    """Return (backtick_count, info_string_or_none) for a fence line."""
    match = FENCE_LINE_RE.match(line.strip())
    if not match:
        return None
    info = match.group("rest").strip()
    return len(match.group("ticks")), info or None
FM_IDENTIFIER_LINE_RE = re.compile(
    r"^\s*(?:-\s*)?name:\s|"
    r"^\s+tags:\s|"
    r"^\s+-\s+[A-Za-z].*membership|"
    r"^\s+glossary_tags:"
)


def _fm_line_is_translatable(line: str) -> bool:
    """Only these front matter fields may receive glossary replacements."""
    stripped = line.lstrip()
    return (
        stripped.startswith("description:")
        or "display_name:" in line
        or stripped.startswith("guide_")
        or stripped.startswith("article_title:")
        or stripped.startswith("nav_title:")
    )
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
LINK_URL_RE = re.compile(r"\]\(([^)]+)\)")
ABSOLUTE_URL_RE = re.compile(r"https?://[^\s\)\]<>'\"]+")

LINE_SKIP_RES = [
    re.compile(r"include\.alert"),
    re.compile(r"alert\s*=\s*['\"]"),
    re.compile(r"/assets/img/"),
]

SEGMENT_SKIP_RE = re.compile(
    r"(?i)("
    r"segment\.com|/segment/|segment_for_currents|braze-segment|"
    r"Segment Swift|Segment Kotlin|Segment Android|Braze Segment|"
    r"Segment Editor|Segment Sync|Segment Membership|Segment Details|"
    r"Segment Insights|Segment Data Export|Segment API Identifier|"
    r"Go to Segment|By Segment|Segment breakdown|"
    r"Segment Extension|Segment Extensions|"
    r"Braze Segment Extension|"
    r"{% tab Segment %}|as it is exported to Segment|"
    r"Added Segment|Edited Segment|Exported Segment|Segment Users Deleted|"
    r"Segmentation|"
    r"Online Shoppers Segment|"
    r"Conversion Segment|Segment Label|"
    r"available=\"Segment|"
    r"Segment >|Create Segment|"
    r"Segment Cohorts|Segment or CSV|"
    r"Segmentコホート|"
    r"Segmentを使用しているクライアント|Segmentでコホート"
    r")"
)


def _is_ascii_term(s: str) -> bool:
    return bool(s) and all(ord(c) < 128 for c in s)


def _term_pattern(search: str) -> re.Pattern[str]:
    escaped = re.escape(search)
    if _is_ascii_term(search):
        return re.compile(
            rf"(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])",
            re.IGNORECASE,
        )
    return re.compile(escaped)


def _should_skip_line(line: str, search: str, lang: str) -> bool:
    if any(p.search(line) for p in LINE_SKIP_RES):
        return True
    if re.match(r"^\s*(?:tool|channel):\s", line):
        return True
    if search.lower() == "segment" and SEGMENT_SKIP_RE.search(line):
        return True
    if (
        lang == "ja"
        and search.lower() == "operator"
        and re.search(r"BrazeAI Operator", line, re.IGNORECASE)
    ):
        return True
    if (
        search.lower() == "segment"
        and re.search(r"\[Segment\]\([^)]*segment", line, re.IGNORECASE)
    ):
        return True
    return False


def _split_fences(text: str) -> list[tuple[str, bool]]:
    parts: list[tuple[str, bool]] = []
    lines = text.splitlines(keepends=True)
    chunk: list[str] = []
    i = 0
    while i < len(lines):
        parsed = _fence_line(lines[i])
        if parsed is not None:
            open_ticks, _info = parsed
            if chunk:
                parts.append(("".join(chunk), False))
                chunk = []
            fence = [lines[i]]
            i += 1
            while i < len(lines):
                close_parsed = _fence_line(lines[i])
                if (
                    close_parsed is not None
                    and close_parsed[1] is None
                    and close_parsed[0] >= open_ticks
                ):
                    fence.append(lines[i])
                    parts.append(("".join(fence), True))
                    i += 1
                    break
                fence.append(lines[i])
                i += 1
            else:
                parts.append(("".join(fence), True))
        else:
            chunk.append(lines[i])
            i += 1
    if chunk:
        parts.append(("".join(chunk), False))
    return parts


def _replace_outside_inline_code(line: str, pattern: re.Pattern[str], replace: str) -> tuple[str, int]:
    total = 0
    out: list[str] = []
    last = 0
    for m in INLINE_CODE_RE.finditer(line):
        chunk, c = pattern.subn(replace, line[last : m.start()])
        out.append(chunk)
        total += c
        out.append(m.group(0))
        last = m.end()
    chunk, c = pattern.subn(replace, line[last:])
    out.append(chunk)
    total += c
    return "".join(out), total


def _replace_in_line(line: str, search: str, replace: str, lang: str) -> tuple[str, int]:
    if search == replace or not search:
        return line, 0
    if _should_skip_line(line, search, lang):
        return line, 0
    if FM_IDENTIFIER_LINE_RE.match(line.rstrip("\n")):
        return line, 0

    placeholders: list[str] = []
    link_url_placeholders: list[str] = []
    absolute_url_placeholders: list[str] = []

    def _mask_image_buster(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"__IMAGE_BUSTER_{len(placeholders) - 1}__"

    def _mask_link_url(match: re.Match[str]) -> str:
        link_url_placeholders.append(match.group(1))
        return f"](__LINK_URL_{len(link_url_placeholders) - 1}__)"

    def _mask_absolute_url(match: re.Match[str]) -> str:
        absolute_url_placeholders.append(match.group(0))
        return f"__ABS_URL_{len(absolute_url_placeholders) - 1}__"

    anchor_placeholders: list[str] = []

    def _mask_heading_anchor(match: re.Match[str]) -> str:
        anchor_placeholders.append(match.group(0))
        return f"__HEADING_ANCHOR_{len(anchor_placeholders) - 1}__"

    masked = HEADING_ANCHOR_RE.sub(_mask_heading_anchor, line)
    masked = IMAGE_BUSTER_RE.sub(_mask_image_buster, masked)
    masked = LINK_URL_RE.sub(_mask_link_url, masked)
    masked = ABSOLUTE_URL_RE.sub(_mask_absolute_url, masked)
    pattern = _term_pattern(search)
    new_masked, count = _replace_outside_inline_code(masked, pattern, replace)
    if not count:
        return line, 0
    new_line = new_masked
    for i, url in enumerate(link_url_placeholders):
        new_line = new_line.replace(f"](__LINK_URL_{i}__)", f"]({url})")
    for i, url in enumerate(absolute_url_placeholders):
        new_line = new_line.replace(f"__ABS_URL_{i}__", url)
    for i, anchor in enumerate(anchor_placeholders):
        new_line = new_line.replace(f"__HEADING_ANCHOR_{i}__", anchor)
    for i, blob in enumerate(placeholders):
        new_line = new_line.replace(f"__IMAGE_BUSTER_{i}__", blob)
    return new_line, count


def replace_in_markdown(text: str, search: str, replace: str, lang: str) -> tuple[str, int]:
    """Apply one glossary-driven replacement across a locale markdown file."""
    if search == replace or not search:
        return text, 0

    fm_match = re.match(r"^(---\s*\r?\n.*?\r?\n---\s*(?:\r?\n|$))", text, re.DOTALL)
    total = 0
    if fm_match:
        fm, body = fm_match.group(1), text[fm_match.end() :]
        fm_lines: list[str] = []
        for line in fm.splitlines(keepends=True):
            if not _fm_line_is_translatable(line):
                fm_lines.append(line)
                continue
            new_line, c = _replace_in_line(line, search, replace, lang)
            total += c
            fm_lines.append(new_line)
        fm = "".join(fm_lines)
    else:
        fm, body = "", text

    out_parts = [fm]
    for part, in_fence in _split_fences(body):
        if in_fence:
            out_parts.append(part)
            continue
        lines: list[str] = []
        for line in part.splitlines(keepends=True):
            new_line, c = _replace_in_line(line, search, replace, lang)
            total += c
            lines.append(new_line)
        out_parts.append("".join(lines))
    return "".join(out_parts), total


def replace_outside_fences(text: str, search: str, replace: str) -> tuple[str, int]:
    """Replace ``search`` with ``replace`` only outside markdown code fences."""
    if not search or search == replace or search not in text:
        return text, 0

    out_parts: list[str] = []
    total = 0
    for part, in_fence in _split_fences(text):
        if in_fence:
            out_parts.append(part)
            continue
        count = part.count(search)
        if count:
            out_parts.append(part.replace(search, replace))
            total += count
        else:
            out_parts.append(part)
    return "".join(out_parts), total


def load_propagation_exclusions(
    path: Path | None = None,
) -> dict[str, list[str]]:
    """Load per-locale and global English keys to skip during propagation."""
    exclusions_path = path or PROPAGATION_EXCLUSIONS_PATH
    if not exclusions_path.is_file():
        return {"global": []}
    data = json.loads(exclusions_path.read_text(encoding="utf-8"))
    return {
        "global": [term.casefold() for term in data.get("global", [])],
        **{
            locale: [term.casefold() for term in terms]
            for locale, terms in data.items()
            if locale not in {"_comment", "global"}
        },
    }


def is_propagation_excluded(
    lang: str,
    term: str,
    exclusions: dict[str, list[str]] | None = None,
) -> bool:
    exclusions = exclusions or load_propagation_exclusions()
    key = term.casefold()
    if key in exclusions.get("global", []):
        return True
    return key in exclusions.get(lang, [])


def build_locale_changes_from_glossary_diff(
    lang: str,
    old: dict[str, str],
    new: dict[str, str],
    exclusions: dict[str, list[str]] | None = None,
) -> list[dict]:
    """Build ``locale_changes`` entries from one locale's glossary diff."""
    exclusions = exclusions or load_propagation_exclusions()
    changes: list[dict] = []
    old_keys = set(old)
    new_keys = set(new)

    for term in sorted(new_keys - old_keys, key=str.casefold):
        if is_propagation_excluded(lang, term, exclusions):
            continue
        replace = new[term]
        if not replace or term == replace:
            continue
        changes.append(
            {
                "lang": lang,
                "term": term,
                "kind": "added",
                "search": term,
                "replace": replace,
            }
        )

    for term in sorted(old_keys & new_keys, key=str.casefold):
        old_val = old[term]
        new_val = new[term]
        if old_val == new_val or is_propagation_excluded(lang, term, exclusions):
            continue
        if old_val and old_val != new_val:
            changes.append(
                {
                    "lang": lang,
                    "term": term,
                    "kind": "updated",
                    "search": old_val,
                    "replace": new_val,
                }
            )
        if (
            _is_ascii_term(term)
            and term != new_val
            and old_val.casefold() != term.casefold()
        ):
            changes.append(
                {
                    "lang": lang,
                    "term": term,
                    "kind": "updated",
                    "search": term,
                    "replace": new_val,
                }
            )

    return changes


def build_locale_changes_from_sync_results(
    results: dict[str, dict],
    exclusions: dict[str, list[str]] | None = None,
) -> list[dict]:
    """Build propagation changes from ``sync_glossaries_from_phrase`` results."""
    changes: list[dict] = []
    for locale, row in sorted(results.items()):
        old = row.get("old_glossary") or {}
        new = row.get("glossary") or {}
        changes.extend(
            build_locale_changes_from_glossary_diff(locale, old, new, exclusions)
        )
    return changes


def apply_ja_glossary_removal_repairs(
    repo_root: Path | None = None,
    *,
    dry_run: bool = False,
) -> dict:
    """Repair leaked English campaign-composer UI labels in Japanese docs."""
    repo_root = repo_root or REPO_ROOT
    from auto_translate import repair_ja_campaign_composer_ui  # noqa: WPS433

    locale_root = repo_root / "_lang" / "ja"
    if not locale_root.is_dir():
        return {"files_changed": 0, "repairs": 0, "details": []}

    file_totals: dict[Path, int] = {}
    for md_path in sorted(locale_root.rglob("*.md")):
        original = md_path.read_text(encoding="utf-8")
        repaired, repair_notes = repair_ja_campaign_composer_ui(
            str(md_path), original, "ja"
        )
        if repair_notes and repaired != original:
            file_totals[md_path] = len(repair_notes)
            if not dry_run:
                md_path.write_text(repaired, encoding="utf-8")

    details = [
        {
            "file": str(path.relative_to(repo_root)),
            "repairs": count,
        }
        for path, count in sorted(file_totals.items(), key=lambda x: (-x[1], str(x[0])))
    ]
    return {
        "files_changed": len(file_totals),
        "repairs": sum(file_totals.values()),
        "details": details,
    }


def propagate_phrase_sync_to_locales(
    results: dict[str, dict],
    *,
    repo_root: Path | None = None,
    dry_run: bool = False,
) -> dict:
    """Propagate Phrase glossary sync diffs into ``_lang/`` markdown."""
    repo_root = repo_root or REPO_ROOT
    changes = build_locale_changes_from_sync_results(results)
    propagation = propagate_glossary_changes(
        changes,
        repo_root=repo_root,
        dry_run=dry_run,
    )

    ja_removed = any(
        row.get("diff", {}).get("removed", 0) > 0
        for locale, row in results.items()
        if locale == "ja"
    )
    ja_repairs = (
        apply_ja_glossary_removal_repairs(repo_root, dry_run=dry_run)
        if ja_removed
        else {"files_changed": 0, "repairs": 0, "details": []}
    )

    changed_files = {
        row["file"] for row in propagation.get("details", [])
    } | {
        row["file"] for row in ja_repairs.get("details", [])
    }

    return {
        "changes_planned": len(_normalize_changes(changes)),
        "propagation": propagation,
        "ja_repairs": ja_repairs,
        "locale_files_changed": len(changed_files),
        "locale_replacements": propagation["replacements"] + ja_repairs["repairs"],
    }


def _normalize_changes(changes: Iterable[dict]) -> list[dict]:
    """Drop no-ops and sort longest search strings first."""
    normalized = []
    for ch in changes:
        search = ch.get("search") or ch.get("term") or ""
        replace = ch.get("replace") or ""
        if not search or search == replace:
            continue
        normalized.append(
            {
                "lang": ch["lang"],
                "term": ch.get("term", search),
                "kind": ch.get("kind", "updated"),
                "search": search,
                "replace": replace,
            }
        )
    return sorted(normalized, key=lambda c: len(c["search"]), reverse=True)


def propagate_glossary_changes(
    changes: Iterable[dict],
    repo_root: Path | None = None,
    dry_run: bool = False,
) -> dict:
    """Apply glossary audit changes across ``_lang/`` trees.

    Each change dict: ``lang``, ``term``, ``kind`` (``added``|``updated``),
    ``search`` (text to find), ``replace`` (glossary value).

    Returns summary with ``files_changed``, ``replacements``, ``details``.
    """
    repo_root = repo_root or REPO_ROOT
    lang_root = repo_root / "_lang"
    normalized = _normalize_changes(changes)

    if not normalized:
        return {
            "files_changed": 0,
            "replacements": 0,
            "details": [],
            "by_lang": {},
        }

    by_lang: dict[str, list[dict]] = {}
    for ch in normalized:
        by_lang.setdefault(ch["lang"], []).append(ch)

    file_totals: dict[Path, int] = {}
    by_lang_counts: dict[str, int] = {lang: 0 for lang in by_lang}

    for lang, lang_changes in by_lang.items():
        lang_dir = LANG_GLOSSARY_TO_DIR.get(lang)
        if not lang_dir:
            continue
        locale_root = lang_root / lang_dir
        if not locale_root.is_dir():
            continue

        for md_path in sorted(locale_root.rglob("*.md")):
            original = md_path.read_text(encoding="utf-8")
            text = original
            file_count = 0
            for ch in lang_changes:
                text, n = replace_in_markdown(text, ch["search"], ch["replace"], lang)
                file_count += n
            if file_count and text != original:
                file_totals[md_path] = file_count
                by_lang_counts[lang] = by_lang_counts.get(lang, 0) + file_count
                if not dry_run:
                    md_path.write_text(text, encoding="utf-8")

    details = [
        {
            "file": str(path.relative_to(repo_root)),
            "replacements": count,
        }
        for path, count in sorted(file_totals.items(), key=lambda x: (-x[1], str(x[0])))
    ]

    return {
        "files_changed": len(file_totals),
        "replacements": sum(file_totals.values()),
        "details": details,
        "by_lang": {k: v for k, v in by_lang_counts.items() if v},
    }
