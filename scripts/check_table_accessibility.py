#!/usr/bin/env python3
"""
Lint script: check that every table in modified Markdown files has an accessible name.

Rules
-----
Markdown (GFM) tables
  PASS  The line immediately after the last row is a Kramdown IAL containing aria-label=
  PASS  The IAL contains role="presentation" or role="none"  (explicit opt-out: layout table)
  FAIL  No IAL on the line immediately after the last row
  FAIL  IAL present but contains neither aria-label= nor role="presentation/none"

HTML tables  (<table …>)
  PASS  The opening <table> tag contains aria-label= or aria-labelledby=
  PASS  The opening <table> tag contains role="presentation" or role="none"
  PASS  <caption> appears before the first row element (<tr>, <thead>, <tbody>)
  FAIL  None of the above

Skips
  - Content inside fenced code blocks (``` … ```)
  - Content inside {% raw %} … {% endraw %} Liquid blocks
  - Files under _docs/_hidden/

Usage
-----
  # Check specific files (CI mode — pass changed files from git diff):
  python3 scripts/check_table_accessibility.py file1.md file2.md

  # Check all _docs/ and _includes/ (local full-scan mode):
  python3 scripts/check_table_accessibility.py

Exit codes
  0  No violations
  1  One or more violations found
"""

import re
import sys
import glob
from pathlib import Path

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# Kramdown IAL: starts with {: and ends with }
IAL_RE = re.compile(r'^\s*\{:.*\}')
# IAL has an aria-label attribute
IAL_ARIA_LABEL_RE = re.compile(r'aria-label\s*=')
# IAL or tag is an explicit layout-table opt-out
LAYOUT_ROLE_RE = re.compile(r'role\s*=\s*["\']?(presentation|none)["\']?')

# HTML <table ...> opening tag (may span a single line; we capture tag attrs)
HTML_TABLE_OPEN_RE = re.compile(r'<table(\s[^>]*)?>', re.IGNORECASE)
# Caption element
HTML_CAPTION_RE = re.compile(r'<caption[\s>]', re.IGNORECASE)
# First structural row element — if we hit this before a caption, it's too late
HTML_ROW_START_RE = re.compile(r'<(tr|thead|tbody)[\s>]', re.IGNORECASE)
# aria-label / aria-labelledby on the <table> tag itself
HTML_ARIA_RE = re.compile(r'aria-label(ledby)?\s*=', re.IGNORECASE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_gfm_table_row(line: str) -> bool:
    return line.lstrip().startswith('|')


def is_table_separator(line: str) -> bool:
    """Return True for lines like |---|---| that mark the GFM header/body boundary."""
    stripped = line.strip()
    if not stripped.startswith('|'):
        return False
    cells = [c.strip() for c in stripped.strip('|').split('|')]
    return cells and all(re.match(r'^:?-+:?$', c) for c in cells if c)


def build_skip_mask(lines: list[str]) -> list[bool]:
    """
    Return a boolean list (same length as lines) where True means the line
    is inside a fenced code block or a Liquid {% raw %} block and should be
    skipped by all checks.
    """
    skip = [False] * len(lines)
    in_fence = False
    fence_marker = ''
    in_raw = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Liquid raw blocks — only enter block-raw mode when {% raw %} and
        # {% endraw %} are on different lines (block usage). Inline usage on
        # one line (e.g., table cells) should not cause the row to be skipped.
        if not in_raw and '{% raw %}' in line:
            if '{% endraw %}' not in line:
                in_raw = True
                skip[i] = True
                continue
            # else: both tags on the same line — treat as normal content
        elif in_raw:
            skip[i] = True
            if '{% endraw %}' in line:
                in_raw = False
            continue

        # Fenced code blocks (``` or ~~~, optionally with language tag)
        if not in_fence:
            m = re.match(r'^(`{3,}|~{3,})', stripped)
            if m:
                in_fence = True
                fence_marker = m.group(1)[0] * len(m.group(1))  # normalise to same char
                skip[i] = True
                continue
        else:
            skip[i] = True
            if re.match(r'^' + re.escape(fence_marker) + r'`*\s*$', stripped):
                in_fence = False
            continue

    return skip


# ---------------------------------------------------------------------------
# Markdown table checker
# ---------------------------------------------------------------------------

def check_markdown_tables(lines: list[str], skip: list[bool], path: str) -> list[str]:
    errors = []
    n = len(lines)
    i = 0

    while i < n:
        if skip[i] or not is_gfm_table_row(lines[i]):
            i += 1
            continue

        # Collect the full table block
        table_start = i
        has_separator = False
        while i < n and not skip[i] and is_gfm_table_row(lines[i]):
            if is_table_separator(lines[i]):
                has_separator = True
            i += 1
        table_end = i  # index of first line after the table

        # Only check real GFM tables (must have a separator row)
        if not has_separator:
            continue

        # The IAL must be on the very next line (no blank line — Kramdown requirement)
        ial_line = lines[table_end].rstrip('\n') if table_end < n else ''

        if IAL_RE.match(ial_line):
            if IAL_ARIA_LABEL_RE.search(ial_line):
                continue  # PASS: has aria-label
            if LAYOUT_ROLE_RE.search(ial_line):
                continue  # PASS: explicit layout-table opt-out
            # IAL present but no accessible name and no opt-out
            errors.append(
                f'{path}:{table_start + 1}: Markdown table has a Kramdown IAL but no '
                f'aria-label= and no role="presentation/none".\n'
                f'  Add aria-label to the IAL: {{: .reset-td-br-1 … aria-label="Your label here" }}'
            )
        else:
            # No IAL at all on the next line
            errors.append(
                f'{path}:{table_start + 1}: Markdown table is missing an accessible name.\n'
                f'  Add an IAL after the last row: {{: .reset-td-br-1 … aria-label="Your label here" }}'
            )

    return errors


# ---------------------------------------------------------------------------
# HTML table checker
# ---------------------------------------------------------------------------

def check_html_tables(lines: list[str], skip: list[bool], path: str) -> list[str]:
    errors = []
    n = len(lines)

    for i, line in enumerate(lines):
        if skip[i]:
            continue
        m = HTML_TABLE_OPEN_RE.search(line)
        if not m:
            continue

        tag_attrs = m.group(0)  # full <table ...> match

        # Opt-out: explicit layout/presentation role on the tag
        if LAYOUT_ROLE_RE.search(tag_attrs):
            continue

        # Accessible name directly on the tag
        if HTML_ARIA_RE.search(tag_attrs):
            continue

        # Scan forward for <caption> before the first row element
        found_caption = False
        for j in range(i + 1, min(i + 30, n)):
            if skip[j]:
                continue
            if HTML_CAPTION_RE.search(lines[j]):
                found_caption = True
                break
            if HTML_ROW_START_RE.search(lines[j]):
                break

        # Also check if <caption> is on the same line as <table>
        after_tag = line[m.end():]
        if HTML_CAPTION_RE.search(after_tag):
            found_caption = True

        if not found_caption:
            errors.append(
                f'{path}:{i + 1}: HTML <table> is missing an accessible name.\n'
                f'  Add aria-label= to the <table> tag, or add <caption> as its first child.'
            )

    return errors


# ---------------------------------------------------------------------------
# File runner
# ---------------------------------------------------------------------------

def check_file(path: str) -> list[str]:
    try:
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError):
        return []

    skip = build_skip_mask(lines)
    errors = check_markdown_tables(lines, skip, path)
    errors += check_html_tables(lines, skip, path)
    return errors


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    if sys.argv[1:]:
        files = sys.argv[1:]
    else:
        files = (
            glob.glob('_docs/**/*.md', recursive=True)
            + glob.glob('_includes/**/*.md', recursive=True)
        )

    # Exclude _docs/_hidden/ — mirrors cspell.json ignorePaths
    files = [f for f in files if '_docs/_hidden/' not in f]

    all_errors: list[str] = []
    for f in sorted(files):
        all_errors.extend(check_file(f))

    if all_errors:
        for err in all_errors:
            print(err)
        count = len(all_errors)
        print(f'\nFound {count} table{"s" if count != 1 else ""} missing an accessible name.')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
