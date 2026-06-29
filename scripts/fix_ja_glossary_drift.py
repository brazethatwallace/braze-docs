#!/usr/bin/env python3
"""Apply focused JA glossary fixes (ja.json) without wholesale Campaign/Canvas swaps."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JA = REPO / "_lang" / "ja"

# Partner / SDK / wire tokens — never rewrite bare "Segment"
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
    r"Segmentation|Segment Insights|"
    r"Online Shoppers Segment|"
    r"Conversion Segment|Segment Label|"
    r"available=\"Segment|"
    r"Segment >|Create Segment|"
    r"Segment Cohorts|Segment or CSV|"
    r"Segmentコホート|"
    r"Segmentを使用しているクライアント|Segmentでコホート"
    r")"
)

FM_IDENTIFIER_LINE_RE = re.compile(
    r"^\s*(?:-\s*)?name:\s|"
    r"^\s+tags:\s|"
    r"^\s+-\s+[A-Za-z].*membership|"
    r"^\s+glossary_tags:"
)

IMAGE_BUSTER_RE = re.compile(r"\{%\s*image_buster\s+[^%]+%\}", re.IGNORECASE)


def _fix_segment_in_line(line: str) -> tuple[str, int]:
    if SEGMENT_SKIP_RE.search(line):
        return line, 0
    if re.search(r"\[Segment\]\([^)]*segment", line, re.I):
        return line, 0
    # Liquid include alert keys and {% if include.alert %} identifiers — English only.
    if "include.alert" in line or re.search(r"alert='[^']*'", line):
        return line, 0

    placeholders: list[str] = []

    def _mask_image_buster(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"__IMAGE_BUSTER_{len(placeholders) - 1}__"

    masked = IMAGE_BUSTER_RE.sub(_mask_image_buster, line)
    new_masked, c = re.subn(
        r"(?<![A-Za-z0-9_])Segment(?![A-Za-z0-9_])",
        "セグメント",
        masked,
    )
    if not c:
        return line, 0
    new_line = new_masked
    for i, blob in enumerate(placeholders):
        new_line = new_line.replace(f"__IMAGE_BUSTER_{i}__", blob)
    return new_line, c


def fix_segment_prose(text: str) -> tuple[str, int]:
    """Segment → セグメント in running prose (skip partners, UI literals, code)."""
    fm_match = re.match(r"^(---\s*\r?\n.*?\r?\n---\s*(?:\r?\n|$))", text, re.DOTALL)
    n = 0
    if fm_match:
        fm, body = fm_match.group(1), text[fm_match.end() :]
        fm_lines = []
        for line in fm.splitlines(keepends=True):
            if FM_IDENTIFIER_LINE_RE.match(line.rstrip("\n")):
                fm_lines.append(line)
                continue
            if not (
                line.lstrip().startswith("description:")
                or "display_name:" in line
                or line.lstrip().startswith("guide_")
                or line.lstrip().startswith("article_title:")
                or line.lstrip().startswith("nav_title:")
            ):
                fm_lines.append(line)
                continue
            new_line, c = _fix_segment_in_line(line)
            n += c
            fm_lines.append(new_line)
        fm = "".join(fm_lines)
    else:
        fm, body = "", text

    out_parts = [fm]
    for part, in_fence in split_fences(body):
        if in_fence:
            out_parts.append(part)
            continue
        lines = []
        for line in part.splitlines(keepends=True):
            new_line, c = _fix_segment_in_line(line)
            n += c
            lines.append(new_line)
        out_parts.append("".join(lines))
    return "".join(out_parts), n

OPERATOR_SKIP_RE = re.compile(
    r"(?i)(BrazeAI Operator|Use BrazeAI Operator|Requested BrazeAI Operator)"
)


def split_fences(text: str) -> list[tuple[str, bool]]:
    parts: list[tuple[str, bool]] = []
    lines = text.splitlines(keepends=True)
    chunk: list[str] = []
    i = 0
    open_re = re.compile(r"^```[a-zA-Z0-9_-]*\s*$")
    close_re = re.compile(r"^```\s*$")
    while i < len(lines):
        if open_re.match(lines[i].strip()):
            if chunk:
                parts.append(("".join(chunk), False))
                chunk = []
            fence = [lines[i]]
            i += 1
            while i < len(lines) and not close_re.match(lines[i].strip()):
                fence.append(lines[i])
                i += 1
            if i < len(lines):
                fence.append(lines[i])
            parts.append(("".join(fence), True))
            i += 1
        else:
            chunk.append(lines[i])
            i += 1
    if chunk:
        parts.append(("".join(chunk), False))
    return parts


def fix_operator_analyze(path: Path, text: str) -> tuple[str, int]:
    if not path.as_posix().endswith("_user_guide/brazeai/operator/analyze.md"):
        return text, 0
    replacements = [
        ("article_title: Operator Analyze", "article_title: オペレーター分析"),
        ("# Operator Analyze", "# オペレーター分析"),
        ("Operator Analyze", "オペレーター分析"),
        ("Operatorパネル", "オペレーターパネル"),
        ("Operatorチャット", "オペレーターチャット"),
        ("Operatorが", "オペレーターが"),
        ("Operatorは", "オペレーターは"),
        ("Operatorの", "オペレーターの"),
        ("Operatorに", "オペレーターに"),
        ("Operatorを", "オペレーターを"),
        ("Operatorで", "オペレーターで"),
        ("Operatorへ", "オペレーターへ"),
    ]
    n = 0
    for old, new in replacements:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            n += count
    return text, n


def fix_operator_privacy(path: Path, text: str) -> tuple[str, int]:
    if not path.as_posix().endswith("_user_guide/brazeai/operator/data_privacy_security.md"):
        return text, 0
    n = 0
    for old, new in [
        ("Operatorがデータ", "オペレーターがデータ"),
        ("Operatorへのアクセス", "オペレーターへのアクセス"),
        ("Operatorインターフェイス", "オペレーターインターフェイス"),
        ("Operatorに提供", "オペレーターに提供"),
    ]:
        if old in text:
            c = text.count(old)
            text = text.replace(old, new)
            n += c
    return text, n


def fix_segment_extension_link(text: str) -> tuple[str, int]:
    new, n = re.subn(
        r"\[Segment Extension\]",
        "[セグメントエクステンション]",
        text,
    )
    return new, n


def process_file(path: Path, dry_run: bool) -> list[str]:
    original = path.read_text("utf-8")
    text = original
    logs: list[str] = []

    text, n1 = fix_segment_prose(text)
    if n1:
        logs.append(f"  segment→セグメント: {n1}")

    text, n2 = fix_operator_analyze(path, text)
    if n2:
        logs.append(f"  operator analyze: {n2}")

    text, n3 = fix_operator_privacy(path, text)
    if n3:
        logs.append(f"  operator privacy: {n3}")

    text, n4 = fix_segment_extension_link(text)
    if n4:
        logs.append(f"  Segment Extension link: {n4}")

    if text != original:
        rel = path.relative_to(REPO)
        if not dry_run:
            path.write_text(text, encoding="utf-8")
        logs.insert(0, str(rel))
    return logs


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = []
    for md in sorted(JA.rglob("*.md")):
        logs = process_file(md, dry_run)
        if logs:
            changed.append(logs)

    mode = "would change" if dry_run else "changed"
    print(f"{mode} {len(changed)} files")
    for logs in changed[:40]:
        print("\n".join(logs))
    if len(changed) > 40:
        print(f"... +{len(changed) - 40} more files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
