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

  # Also write structured JSON for CI suggestion posting:
  python3 scripts/check_table_accessibility.py --json violations.json file1.md

Exit codes
  0  No violations
  1  One or more violations found
"""

import json
import re
import sys
import glob

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

IAL_RE = re.compile(r'^\s*\{:.*\}')
IAL_ARIA_LABEL_RE = re.compile(r'aria-label\s*=')
LAYOUT_ROLE_RE = re.compile(r'role\s*=\s*["\']?(presentation|none)["\']?')
HTML_TABLE_OPEN_RE = re.compile(r'<table(\s[^>]*)?>', re.IGNORECASE)
HTML_CAPTION_RE = re.compile(r'<caption[\s>]', re.IGNORECASE)
HTML_ROW_START_RE = re.compile(r'<(tr|thead|tbody)[\s>]', re.IGNORECASE)
HTML_ARIA_RE = re.compile(r'aria-label(ledby)?\s*=', re.IGNORECASE)
# Matches inline code spans with matched delimiters (CommonMark-compliant).
# (?<!`) ensures the opening run doesn't start mid-sequence (e.g. position 1
#   of ``foo` would otherwise anchor a false 1-backtick span).
# \1 backreference ensures closing run is the same length as the opening run.
# (?!`) prevents a shorter closing run from matching inside a longer run.
INLINE_CODE_RE = re.compile(r'(?<!`)(`{1,3})[^`\n]+?\1(?!`)')

HEADING_RE = re.compile(r'^#{1,6}\s+(.+)$')
STRIP_MD_RE = re.compile(
    r'\[([^\]]+)\]\([^)]+\)|`([^`]+)`|\*\*([^*]+)\*\*|\*([^*]+)\*'
)
STRIP_EXTRA_RE = re.compile(r'[`*_{}<>]')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_heading(h: str) -> str:
    h = STRIP_MD_RE.sub(lambda m: next(g for g in m.groups() if g is not None), h)
    h = STRIP_EXTRA_RE.sub('', h).strip()
    return h or 'Table'


def nearest_heading(lines: list, idx: int) -> str:
    for j in range(idx - 1, -1, -1):
        m = HEADING_RE.match(lines[j].rstrip('\n'))
        if m:
            return clean_heading(m.group(1))
    return 'Table'


def col_count(lines: list, table_start: int, table_end: int) -> int:
    """Count columns from the first non-separator table row."""
    for i in range(table_start, table_end):
        row = lines[i].strip()
        if row.startswith('|') and not re.match(r'^\|[\s|:-]+\|?\s*$', row):
            return max(1, len([c for c in row.strip('|').split('|') if c.strip()]))
    return 2


def make_ial(ncols: int, label: str) -> str:
    classes = ' '.join(f'.reset-td-br-{n}' for n in range(1, ncols + 1))
    return f'{{: {classes} aria-label="{label}" }}'


def is_gfm_table_row(line: str) -> bool:
    return line.lstrip().startswith('|')


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith('|'):
        return False
    cells = [c.strip() for c in stripped.strip('|').split('|')]
    return bool(cells) and all(re.match(r'^:?-+:?$', c) for c in cells if c)


def find_html_table_tag(line: str):
    """Return the first <table> regex match that is NOT inside an inline code span.

    Prose like ``use `<table>` here`` must not trigger a
    violation — the tag lives inside backticks and is just a name, not real HTML.
    """
    inline_spans = [(m.start(), m.end()) for m in INLINE_CODE_RE.finditer(line)]
    for m in HTML_TABLE_OPEN_RE.finditer(line):
        if not any(s <= m.start() < e for s, e in inline_spans):
            return m
    return None


def build_skip_mask(lines: list) -> list:
    skip = [False] * len(lines)
    in_fence = False
    fence_marker = ''
    in_raw = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Liquid raw blocks — only block-raw mode when tags are on separate lines
        if not in_raw and '{% raw %}' in line:
            if '{% endraw %}' not in line:
                in_raw = True
                skip[i] = True
                continue
        elif in_raw:
            skip[i] = True
            if '{% endraw %}' in line:
                in_raw = False
            continue

        # Fenced code blocks
        if not in_fence:
            m = re.match(r'^(`{3,}|~{3,})', stripped)
            if m:
                in_fence = True
                fence_marker = m.group(1)[0] * len(m.group(1))
                skip[i] = True
                continue
        else:
            skip[i] = True
            if re.match(r'^' + re.escape(fence_marker) + r'`*\s*$', stripped):
                in_fence = False
            continue

    return skip


# ---------------------------------------------------------------------------
# Violation dataclass (plain dict for JSON serialisability)
# ---------------------------------------------------------------------------

def make_violation(
    file: str,
    table_start_line: int,   # 1-indexed
    suggestion_line: int,    # 1-indexed line to replace
    suggestion_content: str, # replacement text (may be multiline)
    current_content: str,    # current text at suggestion_line
    message: str,
    fix_hint: str,
) -> dict:
    return {
        'file': file,
        'table_start_line': table_start_line,
        'suggestion_line': suggestion_line,
        'suggestion_content': suggestion_content,
        'current_content': current_content,
        'message': message,
        'fix_hint': fix_hint,
    }


# ---------------------------------------------------------------------------
# Markdown table checker
# ---------------------------------------------------------------------------

def check_markdown_tables(lines: list, skip: list, path: str) -> list:
    violations = []
    n = len(lines)
    i = 0

    while i < n:
        if skip[i] or not is_gfm_table_row(lines[i]):
            i += 1
            continue

        table_start = i
        has_separator = False
        while i < n and not skip[i] and is_gfm_table_row(lines[i]):
            if is_table_separator(lines[i]):
                has_separator = True
            i += 1
        table_end = i  # 0-indexed first line after table

        if not has_separator:
            continue

        ial_line = lines[table_end].rstrip('\n') if table_end < n else ''
        label = nearest_heading(lines, table_start)
        ncols = col_count(lines, table_start, table_end)

        # The last row of the table is always in the PR diff (it was just added).
        # Anchoring suggestions there avoids GitHub API failures when the line
        # *after* the table is context-only, outside the diff window, or past EOF.
        last_row_content = lines[table_end - 1].rstrip('\n')
        last_row_line = table_end  # 1-indexed (0-indexed last row is table_end - 1)

        if IAL_RE.match(ial_line):
            if IAL_ARIA_LABEL_RE.search(ial_line) or LAYOUT_ROLE_RE.search(ial_line):
                continue
            # Bare IAL on the line right after the table — replace that line
            suggested = make_ial(ncols, label)
            violations.append(make_violation(
                file=path,
                table_start_line=table_start + 1,
                suggestion_line=table_end + 1,  # the IAL line itself (always exists)
                suggestion_content=suggested,
                current_content=ial_line,
                message='Markdown table IAL is missing aria-label= (and no role="presentation/none" opt-out).',
                fix_hint=f'Replace the IAL with: {suggested}',
            ))
        else:
            # No IAL — anchor suggestion on the last table row and append the IAL.
            # Using the last row (not the line after) guarantees the target is in
            # the diff even when the table ends at EOF or at an unchanged line.
            suggested_ial = make_ial(ncols, label)
            violations.append(make_violation(
                file=path,
                table_start_line=table_start + 1,
                suggestion_line=last_row_line,
                suggestion_content=last_row_content + '\n' + suggested_ial,
                current_content=last_row_content,
                message='Markdown table is missing an accessible name.',
                fix_hint=f'Add after the last row: {suggested_ial}',
            ))

    return violations


# ---------------------------------------------------------------------------
# HTML table checker
# ---------------------------------------------------------------------------

def check_html_tables(lines: list, skip: list, path: str) -> list:
    violations = []
    n = len(lines)

    for i, line in enumerate(lines):
        if skip[i]:
            continue
        m = find_html_table_tag(line)
        if not m:
            continue

        tag_attrs = m.group(0)
        if LAYOUT_ROLE_RE.search(tag_attrs) or HTML_ARIA_RE.search(tag_attrs):
            continue

        found_caption = False
        after_tag = line[m.end():]
        if HTML_CAPTION_RE.search(after_tag):
            found_caption = True
        else:
            for j in range(i + 1, min(i + 30, n)):
                if skip[j]:
                    continue
                if HTML_CAPTION_RE.search(lines[j]):
                    found_caption = True
                    break
                if HTML_ROW_START_RE.search(lines[j]):
                    break

        if not found_caption:
            label = nearest_heading(lines, i)
            # Suggest adding aria-label to the <table> tag
            original_tag = m.group(0)
            suggested_tag = original_tag[:-1] + f' aria-label="{label}">'
            suggested_line = line.rstrip('\n').replace(original_tag, suggested_tag)
            violations.append(make_violation(
                file=path,
                table_start_line=i + 1,
                suggestion_line=i + 1,
                suggestion_content=suggested_line,
                current_content=line.rstrip('\n'),
                message='HTML <table> is missing an accessible name.',
                fix_hint=f'Add aria-label="{label}" to the <table> tag, or add <caption> as its first child.',
            ))

    return violations


# ---------------------------------------------------------------------------
# File runner
# ---------------------------------------------------------------------------

def check_file(path: str) -> list:
    try:
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError):
        return []

    skip = build_skip_mask(lines)
    violations = check_markdown_tables(lines, skip, path)
    violations += check_html_tables(lines, skip, path)
    return violations


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    args = sys.argv[1:]
    json_output_path = None

    if '--json' in args:
        idx = args.index('--json')
        if idx + 1 >= len(args):
            print('error: --json requires a file path argument', file=sys.stderr)
            return 2
        json_output_path = args[idx + 1]
        args = args[:idx] + args[idx + 2:]

    if args:
        files = args
    else:
        files = (
            glob.glob('_docs/**/*.md', recursive=True)
            + glob.glob('_includes/**/*.md', recursive=True)
        )

    files = [f for f in files if '_docs/_hidden/' not in f]

    all_violations: list = []
    for f in sorted(files):
        all_violations.extend(check_file(f))

    if json_output_path:
        with open(json_output_path, 'w', encoding='utf-8') as fh:
            json.dump(all_violations, fh, indent=2)

    if all_violations:
        for v in all_violations:
            print(f'{v["file"]}:{v["table_start_line"]}: {v["message"]}')
            print(f'  {v["fix_hint"]}')
        count = len(all_violations)
        print(f'\nFound {count} table{"s" if count != 1 else ""} missing an accessible name.')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
