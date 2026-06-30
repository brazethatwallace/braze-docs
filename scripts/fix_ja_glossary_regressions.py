#!/usr/bin/env python3
"""Revert glossary-pass regressions: tool frontmatter, UI filter names, code fences."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JA_ROOT = REPO / "_lang" / "ja"

# ``{% tab %}`` labels in ``_api/`` stay English to match sibling tabs (User Data, etc.).
API_LIQUID_TAB_FIXES = [
    ("{% tab キャンペーン %}", "{% tab Campaigns %}"),
    ("{% tab キャンバス %}", "{% tab Canvas %}"),
    ("{% tab セグメント %}", "{% tab Segments %}"),
]

TOOL_REVERT = {
    "tool: キャンペーン": "tool: Campaigns",
    "tool: キャンバス": "tool: Canvas",
    "tool: セグメント": "tool: Segments",
}

# Braze dashboard / log identifiers — keep English product strings.
UI_IDENTIFIER_FIXES = [
    ("Last Received Message from キャンペーン or キャンバス With Tag", "Last Received Message from Campaign or Canvas With Tag"),
    ("Received Message from キャンペーン or キャンバス with Tag", "Received Message from Campaign or Canvas with Tag"),
    ("Received Message from キャンペーン or キャンバス With Tag", "Received Message from Campaign or Canvas With Tag"),
    ("Clicked/Opened キャンペーン or キャンバス With Tag", "Clicked/Opened Campaign or Canvas With Tag"),
    ("Clicked/Opened キャンペーン or キャンバス with Tag", "Clicked/Opened Campaign or Canvas with Tag"),
    ("Has Never Received a Message from キャンペーン or キャンバス Step", "Has Never Received a Message from Campaign or Canvas Step"),
    ("Clicked Alias in Any キャンペーン or キャンバス Step", "Clicked Alias in Any Campaign or Canvas Step"),
    ("Last Received Message from Specific キャンバス Step", "Last Received Message from Specific Canvas Step"),
    ("Last Received Message from Specific キャンペーン", "Last Received Message from Specific Campaign"),
    ("Last Received Specific キャンバス Step", "Last Received Specific Canvas Step"),
    ("Received Message from キャンバス Step", "Received Message from Canvas Step"),
    ("Received Message from キャンペーン", "Received Message from Campaign"),
    ("Clicked Alias in キャンバス Step", "Clicked Alias in Canvas Step"),
    ("Clicked Alias in キャンペーン", "Clicked Alias in Campaign"),
    ("Clicked/Opened キャンペーン or キャンバス with Tag", "Clicked/Opened Campaign or Canvas with Tag"),
    ("Clicked/Opened キャンペーン", "Clicked/Opened Campaign"),
    ("Interact with キャンペーン", "Interact with Campaign"),
    ("Install Attribution キャンペーン", "Install Attribution Campaign"),
    ("Converted From キャンペーン", "Converted From Campaign"),
    ("Converted From キャンバス", "Converted From Canvas"),
    ("Converted from キャンバス", "Converted from Canvas"),
    ("Received キャンペーン Variant", "Received Campaign Variant"),
    ("Received キャンバス Step", "Received Canvas Step"),
    ("Entered キャンバス Variation", "Entered Canvas Variation"),
    ("In キャンバス Control Group", "In Canvas Control Group"),
    ("In キャンペーン Control Group", "In Campaign Control Group"),
    ("**キャンバス Messages Received**", "**Canvas Messages Received**"),
    ("**Save キャンペーン**", "**キャンペーンを保存**"),
    ("Save キャンペーン", "キャンペーンを保存"),
    ("**キャンペーン Received**", "**Campaign Received**"),
    ("Clicked Alias in キャンバスステップ", "Clicked Alias in Canvas Step"),
    ("Received Message from キャンバスステップ", "Received Message from Canvas Step"),
    ("Last Received Message from Specific キャンバスステップ", "Last Received Message from Specific Canvas Step"),
    ("Has Never Received a Message from キャンペーン or キャンバスステップ", "Has Never Received a Message from Campaign or Canvas Step"),
    ("Clicked Alias in Any キャンペーン or キャンバスステップ", "Clicked Alias in Any Campaign or Canvas Step"),
    ("- name: キャンペーン\n", "- name: Campaigns\n"),
    ("- name: キャンバス\n", "- name: Canvas\n"),
    ("- name: セグメント\n", "- name: Segments\n"),
    ("      - キャンペーン\n", "      - Campaigns\n"),
    ("      - キャンバス\n", "      - Canvas\n"),
    ("      - セグメント\n", "      - Segments\n"),
    ("`400 Invalid キャンペーン ID`", "`400 Invalid Campaign ID`"),
    ("`キャンペーン does not exist`", "`Campaign does not exist`"),
    ("`Missing/Invalid キャンペーン ID`", "`Missing/Invalid Campaign ID`"),
    ("「The キャンバス is archived. Unarchive the キャンバス to ensure trigger requests will take effect.」", "「The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect.」"),
    ("「The キャンバス is paused. Resume the キャンバス to ensure trigger requests will take effect.」", "「The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.」"),
    ("**キャンペーン Details**", "**キャンペーンの詳細**"),
    ("**キャンバス Details**", "**キャンバスの詳細**"),
    ("キャンペーン Details**", "キャンペーンの詳細**"),
    ("キャンバス Details**", "キャンバスの詳細**"),
    ("**Campaign Details**", "**キャンペーンの詳細**"),
    ("**Canvas Details**", "**キャンバスの詳細**"),
    ("Campaign Details**", "キャンペーンの詳細**"),
    ("Canvas Details**", "キャンバスの詳細**"),
    ("Campaign Details", "キャンペーンの詳細"),
    ("Canvas Details", "キャンバスの詳細"),
    ("キャンペーン Details", "キャンペーンの詳細"),
    ("キャンバス Details", "キャンバスの詳細"),
    ("Set Up Canvas Details", "キャンバスの詳細を設定"),
    ("Comments within キャンバス", "Comments within Canvas"),
    ('feature="Control over card creation in キャンバス steps"', 'feature="Control over card creation in Canvas steps"'),
    ("The キャンバス is paused", "The Canvas is paused"),
    ("The キャンバス is archived", "The Canvas is archived"),
    ("Unarchive the キャンバス to", "Unarchive the Canvas to"),
    ("Resume the キャンバス to", "Resume the Canvas to"),
]

# Inside fenced code / schema comments (English API docs).
FENCE_REVERT = [
    ("see キャンペーン Details", "see Campaign Details"),
    ("see キャンペーンの詳細 endpoint", "see Campaign Details endpoint"),
    ("targeted by the キャンバス", "targeted by the Canvas"),
    ("triggered a キャンバス", "triggered a Canvas"),
    ("the キャンバス or campaign", "the Canvas or campaign"),
    ("the キャンペーン API", "the Campaign API"),
    ("the キャンバス API", "the Canvas API"),
    ("the キャンバス name", "the Canvas name"),
    ("the キャンバス description", "the Canvas description"),
    ("associated with the キャンバス", "associated with the Canvas"),
    ("used with キャンバス", "used with Canvas"),
    ("type of キャンバス", "type of Canvas"),
    ("whether this キャンバス", "whether this Canvas"),
    ("The キャンバス is", "The Canvas is"),
    ("the キャンバス is", "the Canvas is"),
    ("Unarchive the キャンバス", "Unarchive the Canvas"),
    ("Resume the キャンバス", "Resume the Canvas"),
    ("of the キャンバス ", "of the Canvas "),
    ("of the キャンバス,", "of the Canvas,"),
    ("of the キャンバス.", "of the Canvas."),
    ("of the キャンバス\n", "of the Canvas\n"),
    ("a キャンバス;", "a Canvas;"),
    ("a キャンバス ", "a Canvas "),
    ("this キャンバス ", "this Canvas "),
    ("the キャンバス ", "the Canvas "),
    ("キャンバス context", "Canvas context"),
    ("stings) the キャンバス", "stings) the Canvas"),
    ("from キャンバス", "from Canvas"),
    ("キャンバスStepApiId", "CanvasStepApiId"),
    ("キャンバスVariationApiId", "CanvasVariationApiId"),
]

MALFORMED_FENCE = re.compile(r"^(`{4,})(json)?\s*$")


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", text, re.DOTALL)
    if not m:
        return "", text
    return text[: m.end()], text[m.end() :]


def normalize_fences(text: str) -> str:
    lines = []
    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        m = MALFORMED_FENCE.match(stripped)
        if m:
            lang = m.group(2) or ""
            lines.append(f"```{lang}\n" if lang else "```\n")
        else:
            lines.append(line)
    return "".join(lines)


def split_fences(body: str) -> list[tuple[str, bool]]:
    parts: list[tuple[str, bool]] = []
    lines = body.splitlines(keepends=True)
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


def fix_fence_content(text: str) -> str:
    for src, dst in FENCE_REVERT:
        text = text.replace(src, dst)
    # Remaining hybrid schema phrases in English comment lines.
    text = re.sub(r"\bthe キャンバス\b", "the Canvas", text)
    text = re.sub(r"\bthis キャンバス\b", "this Canvas", text)
    text = re.sub(r"\ba キャンバス\b", "a Canvas", text)
    text = re.sub(r"\bthe キャンペーン\b", "the Campaign", text)
    return text


def fix_tool_line(line: str) -> str:
    stripped = line.rstrip("\n\r")
    if stripped in TOOL_REVERT:
        return TOOL_REVERT[stripped] + ("\n" if line.endswith("\n") else "")
    return line


def fix_frontmatter(fm: str) -> str:
    if not fm:
        return fm
    return "".join(fix_tool_line(line) for line in fm.splitlines(keepends=True))


def fix_tool_lines_anywhere(text: str) -> str:
    """dev_guide landing pages may not parse as frontmatter; fix tool: lines globally."""
    out = []
    for line in text.splitlines(keepends=True):
        if re.match(r"^tool:\s", line.rstrip("\n")):
            out.append(fix_tool_line(line))
        else:
            out.append(line)
    return "".join(out)


def fix_api_liquid_tabs(path: Path, text: str) -> str:
    if "/_api/" not in path.as_posix():
        return text
    for src, dst in API_LIQUID_TAB_FIXES:
        text = text.replace(src, dst)
    return text


def fix_prose(text: str) -> str:
    for src, dst in UI_IDENTIFIER_FIXES:
        text = text.replace(src, dst)
    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(original)
    fm = fix_prose(fix_frontmatter(fm))
    body = normalize_fences(body)
    parts = []
    for part, is_fence in split_fences(body):
        if is_fence:
            parts.append(fix_fence_content(part))
        else:
            parts.append(fix_prose(part))
    merged = fm + "".join(parts)
    updated = fix_prose(fix_tool_lines_anywhere(merged))
    updated = fix_fence_content(updated)
    updated = fix_api_liquid_tabs(path, updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for path in sorted(JA_ROOT.rglob("*.md")):
        if process_file(path):
            changed += 1
    print(f"Updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
