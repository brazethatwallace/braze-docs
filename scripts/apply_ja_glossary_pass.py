#!/usr/bin/env python3
"""Apply selected ja.json glossary terms to _lang/ja markdown (one-off pass)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JA_ROOT = REPO / "_lang" / "ja"

# Longer phrases first.
REPLACEMENTS = [
    ("Recommended events", "推奨イベント"),
    ("Recommended event", "推奨イベント"),
    ("おすすめイベント", "推奨イベント"),
    ("Canvases", "キャンバス"),
    ("Campaigns", "キャンペーン"),
    ("Segments", "セグメント"),
    ("Canvas", "キャンバス"),
    ("Campaign", "キャンペーン"),
    ("Segment", "セグメント"),
]

LINE_SKIP = re.compile(
    "|".join(
        [
            r"\{% tab (Campaign|Canvas|Segment) %\}",
            r"exported to Segment",
            r"/segment/segment_for_currents",
            r"\[Segment\]\(\{\{site\.baseurl\}\}/partners/",
            r"campaign_id|canvas_id|segment_id",
            r"Campaign Conversion|users\.campaigns\.|users\.behaviors\.",
            r'^\s*"(?:event|canvas_|campaign_)',
            r"^\s*//",
            r"^\s*\{",
            r"Agent Console|Agent Management|\+ Agent context",
        ]
    )
)

AGENT_RE = re.compile(r"\bAgent\b")


def split_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        return "", text, ""
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, ""
    return text[: end + 5], text[end + 5 :], ""


def split_fences(body: str) -> list[tuple[str, bool]]:
    """Split on well-formed fenced code blocks only (line is ``` or ```lang)."""
    parts: list[tuple[str, bool]] = []
    lines = body.splitlines(keepends=True)
    chunk: list[str] = []
    i = 0
    open_re = re.compile(r"^`{3,}[a-zA-Z0-9_-]*\s*$")
    close_re = re.compile(r"^`{3,}\s*$")

    while i < len(lines):
        line_stripped = lines[i].strip()
        if open_re.match(line_stripped):
            # Normalize malformed fences (4+ backticks) to standard ```
            if not line_stripped.startswith("```"):
                lang_m = re.match(r"^`{4,}([a-zA-Z0-9_-]*)?\s*$", line_stripped)
                lines[i] = f"```{lang_m.group(1) or ''}\n" if lang_m else lines[i]
            if chunk:
                parts.append(("".join(chunk), False))
                chunk = []
            fence = [lines[i]]
            i += 1
            while i < len(lines):
                fence.append(lines[i])
                if close_re.match(lines[i].strip()):
                    break
                i += 1
            parts.append(("".join(fence), True))
            i += 1
            continue
        chunk.append(lines[i])
        i += 1
    if chunk:
        parts.append(("".join(chunk), False))
    return parts


def transform_frontmatter(fm: str) -> str:
    if not fm:
        return fm
    out_lines = []
    for line in fm.splitlines(keepends=True):
        if re.match(r"^tool:\s", line):
            out_lines.append(line)
            continue
        new_line = line
        for src, dst in REPLACEMENTS:
            new_line = new_line.replace(src, dst)
        out_lines.append(new_line)
    return "".join(out_lines)


def apply_replacements(chunk: str) -> str:
    out_lines = []
    for line in chunk.splitlines(keepends=True):
        if LINE_SKIP.search(line):
            out_lines.append(line)
            continue
        new_line = line
        for src, dst in REPLACEMENTS:
            new_line = new_line.replace(src, dst)
        # Standalone Agent → エージェント (Braze Agents product)
        if "Agent" in new_line and not LINE_SKIP.search(new_line):

            def agent_sub(m: re.Match[str]) -> str:
                return "エージェント"

            new_line = AGENT_RE.sub(agent_sub, new_line)
        out_lines.append(new_line)
    return "".join(out_lines)


def transform(body: str) -> str:
    result = []
    for part, is_fence in split_fences(body):
        result.append(part if is_fence else apply_replacements(part))
    return "".join(result)


def main() -> int:
    changed_files = 0
    for path in sorted(JA_ROOT.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        fm, body, _ = split_frontmatter(original)
        updated = transform_frontmatter(fm) + transform(body)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
    print(f"Updated {changed_files} files under {JA_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
