#!/usr/bin/env python3
"""
Lint script: check content accessibility issues in Markdown and HTML include files.

Checks
------
1.1.1  Non-text Content (alt text)
  PASS  Image has non-empty alt text:  ![Description](url)
  PASS  Image is explicitly decorative (filename matches decorative heuristic)
  FAIL  Image has empty alt and filename does NOT match decorative patterns

2.4.4  Link Purpose (In Context)
  FAIL  Link visible text matches a non-descriptive pattern such as "here",
        "click here", "learn more", "read more", "this link", "more", etc.

2.4.6  Headings and Labels
  FAIL  Heading level skips by more than one step going deeper
        (e.g. h2 followed immediately by h4 with no h3 in between)

4.1.2  Name, Role, Value — inline iframes
  FAIL  <iframe> tag in markdown content without a title= attribute

1.3.3  Sensory Characteristics — spatial directionals
  FAIL  Layout-referencing words such as "above", "below", or "to the left"
        when they point readers to content by position on the page
  PASS  Numeric comparisons ("below the input field", "above the threshold")
  PASS  Text direction terms ("left-to-right", "bi-directional")

Decorative image heuristic
  Filenames containing "divider", "spacer", "separator", "background", or "bg"
  (as a path component or filename segment) are treated as decorative.
  Empty alt is intentional for those; all others with empty alt are flagged.

Skips
  - Content inside fenced code blocks (``` / ~~~)
  - Content inside {% raw %} … {% endraw %} Liquid blocks

Usage
-----
  # Check specific files (pass changed files from git diff):
  python3 scripts/check_content_accessibility.py file1.md file2.md

  # Check all _docs/, _includes/ (full-scan mode):
  python3 scripts/check_content_accessibility.py

  # Write structured JSON for programmatic consumption:
  python3 scripts/check_content_accessibility.py --json /tmp/violations.json file1.md

Exit codes
  0  No violations
  1  One or more violations found
  2  Script error (bad arguments, unreadable file)
"""

import glob
import json
import re
import sys

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

MARKDOWN_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

# Markdown links that are NOT images (not preceded by !)
MARKDOWN_LINK_RE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')

HEADING_RE = re.compile(r'^(#{1,6})\s+')

IFRAME_RE = re.compile(r'<iframe(?:\s[^>]*|)>', re.IGNORECASE)
IFRAME_TITLE_RE = re.compile(r'\btitle\s*=\s*(?:"[^"]*"|\'[^\']*\')', re.IGNORECASE)

# Filename segments that indicate a decorative image
DECORATIVE_RE = re.compile(
    r'(?:^|[/_.-])'
    r'(?:divider|spacer|separator|background|bg)'
    r'(?:[/_.-]|$)',
    re.IGNORECASE,
)

NONDESCRIPTIVE_LINK_TEXT: frozenset = frozenset({
    'here',
    'click here',
    'this',
    'this link',
    'this page',
    'learn more',
    'read more',
    'more',
    'link',
    'click',
    'see more',
    'details',
    'read this',
    'view',
    'view here',
    'click this',
    'go here',
    'go',
    'visit',
    'more information',
})

# Trailing punctuation to strip before lookup
_TRAILING_PUNCT_RE = re.compile(r'[.,;:!?]+$')

# WCAG 1.3.3 — layout-referencing spatial language (not numeric comparisons)
SPATIAL_ABOVE_BELOW_RE = re.compile(r'\b(above|below)\b', re.IGNORECASE)

# Multi-word patterns only — never match bare "left" or "right" alone.
# Bare words produce too many false positives ("right users", "right approach",
# "float:right" in inline styles, "left" as past tense of "leave", etc.).
# A spatial UI reference almost always has a qualifying prefix or suffix.
_SPATIAL_NOT_RIGHT_LEFT_NOUNS = (
    # "right" / "left" meaning "correct" or "remaining", not a UI position.
    # Add to this list when new false-positive noun patterns are confirmed in docs.
    r'user|users|person|people|customer|customers|audience|audiences'
    r'|message|messages|content|data|format|type|approach|way|tool|tools'
    r'|channel|channels|segment|segments|campaign|campaigns|template|templates'
    r'|method|strategy|option|options|choice|choices|decision|decisions'
    r'|time|timing|place|partner|partners|team|teams|vendor|vendors'
)

SPATIAL_LEFT_RIGHT_RE = re.compile(
    r'\b(?:'
    # Prefix-anchored: "to/on/from the left/right", but NOT followed by a non-positional noun
    # (e.g. "to the right users", "on the right channel" = "correct", not a UI position).
    r'(?:to|on|from)\s+the\s+(?:left|right)(?!\s+(?:' + _SPATIAL_NOT_RIGHT_LEFT_NOUNS + r')\b)'
    # Suffix-anchored: "left/right [side|panel|column|corner|sidebar|toolbar|bar|menu|nav|hand|of]"
    r'|(?:left|right)\s+(?:of\b|side\b|panel\b|column\b|corner\b|sidebar\b|toolbar\b|bar\b|menu\b|nav\b|hand\b)'
    # Compound: "left/right-hand side"
    r'|(?:left|right)[\s-]hand\s+side'
    # Cardinal qualifier: "upper/lower/top/bottom left/right" (with or without hyphen)
    r'|(?:upper|lower|top|bottom)[\s-](?:left|right)'
    r')\b',
    re.IGNORECASE,
)

# Phrases allowed on the same line as an above/below match.
# These are contexts where "above"/"below" conveys numeric/semantic relation,
# not page-layout direction.
_SPATIAL_ALLOWLIST_RES: tuple = (
    # Numeric thresholds and bounds.
    re.compile(
        r'(?:above|below)\s+the\s+(?:entered\s+)?(?:number|threshold|value|limit|input(?:\s+field)?)',
        re.IGNORECASE,
    ),
    # Quantitative comparisons in docs prose.
    re.compile(
        r'(?:above|below)\s+(?:that|this|the|your|our)?\s*'
        r'(?:allotment|amount|volume|quota|count|number|total|minimum|maximum|limit|cap)\b',
        re.IGNORECASE,
    ),
    # Attribution/export subgroup hierarchy (semantic containment).
    re.compile(
        r'sub-?group(?:ing)?\s+(?:above|below)\s+\w+',
        re.IGNORECASE,
    ),
    # Programming/string operations (not layout instructions).
    re.compile(
        r'(?:left|right)\s+side\s+of\s+(?:a|the)?\s*string\b',
        re.IGNORECASE,
    ),
    re.compile(
        r'from\s+the\s+(?:left|right)\s+side\s+of\s+(?:a|the)?\s*string\b',
        re.IGNORECASE,
    ),
    re.compile(
        r'from\s+the\s+left\s+and\s+right\s+side\s+of\s+(?:a|the)?\s*string\b',
        re.IGNORECASE,
    ),
    re.compile(r'left-to-right|right-to-left', re.IGNORECASE),
    re.compile(r'bi-?directional', re.IGNORECASE),
)


# ---------------------------------------------------------------------------
# Violation factory
# ---------------------------------------------------------------------------

def make_violation(
    file: str,
    table_start_line: int,    # 1-indexed; for non-table items, this is the issue line
    suggestion_line: int,     # 1-indexed
    suggestion_content: str,  # replacement text (author provides for most content checks)
    current_content: str,     # current line text
    message: str,
    fix_hint: str,
    violation_type: str,      # image_missing_alt | nondescriptive_link | heading_skip | iframe_missing_title | spatial_directional
    wcag_criterion: str,      # e.g. "1.1.1"
    auto_fix_eligible: bool = True,  # allow downstream tooling to gate auto-fixes
) -> dict:
    return {
        'file': file,
        'table_start_line': table_start_line,
        'suggestion_line': suggestion_line,
        'suggestion_content': suggestion_content,
        'current_content': current_content,
        'message': message,
        'fix_hint': fix_hint,
        'violation_type': violation_type,
        'wcag_criterion': wcag_criterion,
        'auto_fix_eligible': auto_fix_eligible,
    }


# ---------------------------------------------------------------------------
# Skip mask (same approach as check_table_accessibility.py)
# ---------------------------------------------------------------------------

def build_skip_mask(lines: list) -> list:
    """Return a bool list; True = skip this line (code fence or Liquid raw block)."""
    skip = [False] * len(lines)
    in_fence = False
    fence_marker = ''
    in_raw = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Liquid {% raw %} blocks
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
# 1.1.1 — Image alt text
# ---------------------------------------------------------------------------

def _is_decorative_filename(src: str) -> bool:
    """Return True when the image filename matches a known decorative pattern."""
    filename = src.rsplit('/', 1)[-1].rsplit('?', 1)[0]
    return bool(DECORATIVE_RE.search(filename))


def check_image_alt(lines: list, skip: list, path: str) -> list:
    violations = []
    for i, line in enumerate(lines):
        if skip[i]:
            continue
        for m in MARKDOWN_IMAGE_RE.finditer(line):
            alt_text = m.group(1)
            img_src = m.group(2)

            if alt_text:
                continue  # non-empty alt — pass

            # Empty alt: is this a decorative image?
            if _is_decorative_filename(img_src):
                continue  # Decorative heuristic match — empty alt is intentional

            violations.append(make_violation(
                file=path,
                table_start_line=i + 1,
                suggestion_line=i + 1,
                suggestion_content=line.rstrip('\n'),  # author provides alt text
                current_content=line.rstrip('\n'),
                message=(
                    f'Image is missing alt text (WCAG 1.1.1): {m.group(0)!r}\n'
                    f'  If this image conveys meaning, add a description. '
                    f'If it is purely decorative, the empty alt is fine but consider '
                    f'adding a visible comment to confirm intent.'
                ),
                fix_hint=(
                    f'Replace ![]({img_src}) with ![A description of what this image shows]({img_src})\n'
                    f'  Or, if the image is decorative, leave the empty alt and no action is needed.'
                ),
                violation_type='image_missing_alt',
                wcag_criterion='1.1.1',
            ))
    return violations


# ---------------------------------------------------------------------------
# 2.4.4 — Non-descriptive link text
# ---------------------------------------------------------------------------

def check_link_purpose(lines: list, skip: list, path: str) -> list:
    violations = []
    for i, line in enumerate(lines):
        if skip[i]:
            continue
        for m in MARKDOWN_LINK_RE.finditer(line):
            link_text = m.group(1).strip()
            link_url = m.group(2)
            normalized = _TRAILING_PUNCT_RE.sub('', link_text.lower())
            if normalized not in NONDESCRIPTIVE_LINK_TEXT:
                continue
            violations.append(make_violation(
                file=path,
                table_start_line=i + 1,
                suggestion_line=i + 1,
                suggestion_content=line.rstrip('\n'),  # author provides replacement text
                current_content=line.rstrip('\n'),
                message=(
                    f'Non-descriptive link text (WCAG 2.4.4): [{link_text}]({link_url})\n'
                    f'  The text "{link_text}" does not describe the link destination.'
                ),
                fix_hint=(
                    f'Replace "{link_text}" with a phrase that describes the linked page.\n'
                    f'  Example: instead of [learn more]({link_url}), '
                    f'use [learn more about <topic>]({link_url})'
                ),
                violation_type='nondescriptive_link',
                wcag_criterion='2.4.4',
            ))
    return violations


# ---------------------------------------------------------------------------
# 2.4.6 — Heading hierarchy
# ---------------------------------------------------------------------------

def check_heading_hierarchy(lines: list, skip: list, path: str) -> list:
    violations = []
    prev_level: int | None = None

    for i, line in enumerate(lines):
        if skip[i]:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if prev_level is not None and level > prev_level + 1:
            violations.append(make_violation(
                file=path,
                table_start_line=i + 1,
                suggestion_line=i + 1,
                suggestion_content=line.rstrip('\n'),
                current_content=line.rstrip('\n'),
                message=(
                    f'Heading level skip (WCAG 2.4.6): h{prev_level} → h{level} '
                    f'(skipped h{prev_level + 1}). '
                    f'Screen reader users navigate by heading structure.'
                ),
                fix_hint=(
                    f'Either: (a) add an h{prev_level + 1} section between the h{prev_level} and '
                    f'this h{level}, or (b) promote this heading from h{level} to h{prev_level + 1}.'
                ),
                violation_type='heading_skip',
                wcag_criterion='2.4.6',
            ))
        prev_level = level

    return violations


# ---------------------------------------------------------------------------
# 4.1.2 — Inline iframes without title
# ---------------------------------------------------------------------------

def check_inline_iframes(lines: list, skip: list, path: str) -> list:
    violations = []
    for i, line in enumerate(lines):
        if skip[i]:
            continue
        for m in IFRAME_RE.finditer(line):
            tag = m.group(0)
            if IFRAME_TITLE_RE.search(tag):
                continue
            violations.append(make_violation(
                file=path,
                table_start_line=i + 1,
                suggestion_line=i + 1,
                suggestion_content=line.rstrip('\n'),
                current_content=line.rstrip('\n'),
                message=f'Inline <iframe> is missing a title attribute (WCAG 4.1.2): {tag!r}',
                fix_hint=(
                    'Add a descriptive title= attribute to the <iframe> tag.\n'
                    '  Example: <iframe ... title="Description of the embedded content">'
                ),
                violation_type='iframe_missing_title',
                wcag_criterion='4.1.2',
            ))
    return violations


def _spatial_match_allowlisted(line: str, start: int, end: int) -> bool:
    """Return True when a spatial match sits inside an allowed phrase."""
    for pat in _SPATIAL_ALLOWLIST_RES:
        for m in pat.finditer(line):
            if m.start() <= start and m.end() >= end:
                return True
    return False


def _inside_markdown_image_alt(line: str, start: int, end: int) -> bool:
    """Return True if the match is inside markdown image alt text."""
    for m in MARKDOWN_IMAGE_RE.finditer(line):
        alt_start = m.start(1)
        alt_end = m.end(1)
        if start >= alt_start and end <= alt_end:
            return True
    return False


def _is_css_declaration_line(line: str) -> bool:
    """Return True for standalone CSS declaration lines in markdown prose."""
    stripped = line.strip()
    return bool(re.match(r'^[a-zA-Z-]+\s*:\s*[^;]+;\s*$', stripped))


def _is_legal_sensitive_path(path: str) -> bool:
    """Return True for legal-content files that require manual wording review."""
    normalized = path.replace('\\', '/').lower()
    # Explicitly legal path segments.
    if re.search(r'/(legal|contracts?)/', normalized):
        return True

    filename = normalized.rsplit('/', 1)[-1]
    stem = filename.rsplit('.', 1)[0]

    # Known legal-oriented filenames anywhere under checked docs/includes paths.
    if stem in {
        'cla',
        'privacy_policy',
        'terms_of_service',
        'legal_notice',
        'license_agreement',
        'contribution_license_agreement',
    }:
        return True

    # `_docs/_docs_pages` houses site-level legal pages such as CLA.
    # Match only on token boundaries to avoid substring false positives
    # like "classification" matching "cla".
    normalized_no_lead = normalized.lstrip('/')
    if normalized_no_lead.startswith('_docs/_docs_pages/'):
        legal_tokens = {'cla', 'privacy', 'terms', 'legal', 'license', 'agreement'}
        stem_tokens = [t for t in re.split(r'[^a-z0-9]+', stem) if t]
        if any(token in legal_tokens for token in stem_tokens):
            return True

    return False


def _left_right_spatial_matches(line: str) -> list:
    """Return left/right layout matches.

    The regex already requires a qualifying prefix or suffix, so bare words
    like "right users", "right approach", and CSS tokens like "float:right" or
    "margin-left" never reach this function. Hyphen-adjacency filtering is not
    needed here; it was previously suppressing true positives such as
    "top-left corner" and "bottom-right of the panel".
    """
    return list(SPATIAL_LEFT_RIGHT_RE.finditer(line))


def check_spatial_directionals(lines: list, skip: list, path: str) -> list:
    """Flag layout-referencing above/below/left/right (WCAG 1.3.3)."""
    violations: list = []
    legal_sensitive_path = _is_legal_sensitive_path(path)
    for i, line in enumerate(lines):
        if skip[i]:
            continue
        if _is_css_declaration_line(line):
            continue

        flagged_terms: list = []

        for m in SPATIAL_ABOVE_BELOW_RE.finditer(line):
            if _inside_markdown_image_alt(line, m.start(), m.end()):
                continue
            if not _spatial_match_allowlisted(line, m.start(), m.end()):
                flagged_terms.append(m.group(0).lower())

        for m in _left_right_spatial_matches(line):
            if _inside_markdown_image_alt(line, m.start(), m.end()):
                continue
            if not _spatial_match_allowlisted(line, m.start(), m.end()):
                flagged_terms.append(m.group(0).lower())

        if not flagged_terms:
            continue

        terms = ', '.join(sorted(set(flagged_terms)))
        violations.append(make_violation(
            file=path,
            table_start_line=i + 1,
            suggestion_line=i + 1,
            suggestion_content='',
            current_content=line.rstrip('\n'),
            message=(
                f'Spatial directional language ({terms}) relies on page layout. '
                'Use a section name, anchor link, or tab name instead.'
            ),
            fix_hint=(
                'Replace layout references like "above", "below", or "to the left" '
                'with the section heading, `#anchor`, or "in the previous tab". '
                'Numeric comparisons ("below the input field", "above the threshold") '
                'and text-direction terms ("left-to-right") are allowed.'
            ),
            violation_type='spatial_directional',
            wcag_criterion='1.3.3',
            auto_fix_eligible=not legal_sensitive_path,
        ))
    return violations


# ---------------------------------------------------------------------------
# File runner
# ---------------------------------------------------------------------------

def check_file(path: str) -> list:
    try:
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
    except (OSError, UnicodeDecodeError) as exc:
        print(f'error: could not read {path}: {exc}', file=sys.stderr)
        return []

    skip = build_skip_mask(lines)
    violations: list = []
    violations += check_image_alt(lines, skip, path)
    violations += check_link_purpose(lines, skip, path)
    violations += check_heading_hierarchy(lines, skip, path)
    violations += check_inline_iframes(lines, skip, path)
    violations += check_spatial_directionals(lines, skip, path)
    return violations


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

_WCAG_TITLES: dict = {
    '1.1.1': 'Missing alt text',
    '1.3.3': 'Spatial directional language',
    '2.4.4': 'Non-descriptive link text',
    '2.4.6': 'Heading level skip',
    '4.1.2': 'Missing iframe title',
}


def emit_github_annotations(violations_path: str) -> int:
    """Read a violations JSON file and print GitHub Actions annotation lines."""
    import re as _re
    try:
        with open(violations_path, encoding='utf-8') as fh:
            violations = json.load(fh)
    except FileNotFoundError:
        print(f'error: {violations_path} not found', file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f'error: malformed JSON in {violations_path}: {exc}', file=sys.stderr)
        return 2

    for v in violations:
        criterion = v.get('wcag_criterion', '?')
        title = _WCAG_TITLES.get(criterion, f'WCAG {criterion}')
        msg = _re.sub(r'\s+', ' ', v['message'].split('\n')[0].strip())
        file = v['file']
        line = v['table_start_line']
        print(f'::error file={file},line={line},title=WCAG {criterion} - {title}::{msg}')
    return 0


def main() -> int:
    args = sys.argv[1:]
    json_output_path = None

    # --github-annotations <violations.json>
    # Reads a pre-generated violations JSON and emits GitHub Actions ::error annotations.
    # Used by CI to avoid inline Python heredocs in YAML.
    if '--github-annotations' in args:
        idx = args.index('--github-annotations')
        if idx + 1 >= len(args):
            print('error: --github-annotations requires a file path argument', file=sys.stderr)
            return 2
        return emit_github_annotations(args[idx + 1])

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
            + glob.glob('_includes/**/*.html', recursive=True)
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
            print(
                f'{v["file"]}:{v["table_start_line"]}: '
                f'[WCAG {v["wcag_criterion"]}] {v["message"]}'
            )
            print(f'  Fix: {v["fix_hint"]}')
        count = len(all_violations)
        print(
            f'\nFound {count} content accessibility violation'
            f'{"s" if count != 1 else ""}.'
        )
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
