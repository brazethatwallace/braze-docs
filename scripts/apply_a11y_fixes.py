#!/usr/bin/env python3
"""
Apply high-confidence accessibility fixes in-place from a violations JSON file.

Reads the JSON output produced by check_table_accessibility.py (--json flag) and
applies fixes that meet all three high-confidence criteria:

  1. The violation message is exactly "Markdown table is missing an accessible name."
     (no existing IAL at all — not a modification case)
  2. The aria-label in the suggestion is specific — NOT one of the generic headings:
     Table, Overview, Details, Notes, Summary, Introduction, Background, Results,
     Example, Examples, Reference, References
  3. The file has 3 or fewer violations total in this run

Fixes that don't meet all three criteria are printed as "skipped" and the script
exits with code 1 so the caller (e.g. the pre-commit hook) knows manual action is
still needed.

Usage
-----
  # From violations JSON produced by check_table_accessibility.py:
  python3 scripts/apply_a11y_fixes.py violations.json

  # Dry run (print what would change without writing):
  python3 scripts/apply_a11y_fixes.py --dry-run violations.json

Exit codes
  0  All violations were auto-fixed (or there were no violations)
  1  One or more violations were skipped (medium/low confidence) — manual fix required
  2  Script error (missing file, malformed JSON, etc.)
"""

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# High-confidence criteria constants (mirror the skill's classification rules)
# ---------------------------------------------------------------------------

GENERIC_LABELS: frozenset = frozenset({
    'table', 'overview', 'details', 'notes', 'summary',
    'introduction', 'background', 'results', 'example', 'examples',
    'reference', 'references',
})

HIGH_CONFIDENCE_MESSAGE = 'Markdown table is missing an accessible name.'

ARIA_LABEL_RE = re.compile(r'aria-label\s*=\s*"([^"]*)"', re.IGNORECASE)


def is_generic_label(suggestion_content: str) -> bool:
    m = ARIA_LABEL_RE.search(suggestion_content)
    if not m:
        return True  # no aria-label found → treat as generic
    return m.group(1).strip().lower() in GENERIC_LABELS


def is_high_confidence(violation: dict, file_violation_count: int) -> bool:
    return (
        violation.get('message') == HIGH_CONFIDENCE_MESSAGE
        and not is_generic_label(violation.get('suggestion_content', ''))
        and file_violation_count <= 3
    )


# ---------------------------------------------------------------------------
# Fix application
# ---------------------------------------------------------------------------

def apply_fixes(violations: list, dry_run: bool) -> tuple[int, int]:
    """Return (fixed_count, skipped_count)."""
    # Count violations per file for the threshold check
    file_counts: dict[str, int] = {}
    for v in violations:
        file_counts[v['file']] = file_counts.get(v['file'], 0) + 1

    # Separate into high-confidence (auto-fix) and skipped
    to_fix: dict[str, list] = {}  # file → list of violations, sorted high→low line
    skipped: list = []

    for v in violations:
        if is_high_confidence(v, file_counts[v['file']]):
            to_fix.setdefault(v['file'], []).append(v)
        else:
            skipped.append(v)

    fixed_count = 0

    for filepath, file_violations in to_fix.items():
        path = Path(filepath)
        if not path.exists():
            print(f'  warning: {filepath} not found — skipping', file=sys.stderr)
            skipped.extend(file_violations)
            continue

        lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

        # Apply fixes bottom-to-top to avoid line-number drift
        for v in sorted(file_violations, key=lambda x: x['suggestion_line'], reverse=True):
            line_idx = v['suggestion_line'] - 1  # convert to 0-indexed
            if line_idx < 0 or line_idx >= len(lines):
                print(
                    f'  warning: line {v["suggestion_line"]} out of range in {filepath} — skipping',
                    file=sys.stderr,
                )
                skipped.append(v)
                continue

            # suggestion_content may be multiline (last table row + IAL on next line)
            new_content = v['suggestion_content']
            if not new_content.endswith('\n'):
                new_content += '\n'

            if dry_run:
                print(f'  [dry-run] would fix {filepath}:{v["suggestion_line"]}')
                print(f'    - {lines[line_idx].rstrip()}')
                for new_line in new_content.splitlines():
                    print(f'    + {new_line}')
            else:
                # Replace the target line with the new content (may expand to 2 lines)
                lines[line_idx] = new_content
                fixed_count += 1
                label_match = ARIA_LABEL_RE.search(new_content)
                label = label_match.group(1) if label_match else '?'
                print(f'  fixed  {filepath}:{v["suggestion_line"]} — aria-label="{label}"')

        if not dry_run and file_violations:
            path.write_text(''.join(lines), encoding='utf-8')

    for v in skipped:
        reason = 'generic label' if not is_high_confidence(v, file_counts[v['file']]) else 'low confidence'
        print(
            f'  skipped {v["file"]}:{v["table_start_line"]} '
            f'({reason}) — fix manually: {v["fix_hint"]}'
        )

    return fixed_count, len(skipped)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    args = sys.argv[1:]
    dry_run = '--dry-run' in args
    args = [a for a in args if a != '--dry-run']

    if not args:
        print('usage: apply_a11y_fixes.py [--dry-run] violations.json', file=sys.stderr)
        return 2

    violations_path = args[0]
    try:
        with open(violations_path, encoding='utf-8') as fh:
            violations = json.load(fh)
    except FileNotFoundError:
        print(f'error: {violations_path} not found', file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f'error: malformed JSON in {violations_path}: {exc}', file=sys.stderr)
        return 2

    if not violations:
        return 0

    mode = 'Dry-run' if dry_run else 'Applying'
    print(f'{mode} high-confidence fixes ({len(violations)} violation(s) in input)...')

    fixed, skipped = apply_fixes(violations, dry_run)

    if not dry_run:
        print(f'\nResult: {fixed} fixed, {skipped} skipped (need manual fix)')
    else:
        print(f'\nDry-run complete: {fixed} would be fixed, {skipped} would be skipped')

    return 1 if skipped > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
