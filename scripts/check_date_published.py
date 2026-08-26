#!/usr/bin/env python3
"""
Enforce ``date_published`` on first public ship of Braze Docs articles.

Check 1 — first public ship (new eligible file, or unhide / leave config_only
with no date already present)
  The field must be present, formatted YYYY-MM-DD, and not in the past
  (UTC). Today and future dates are allowed so writers can set the date they
  expect the PR to merge. Hidden and config_only pages are exempt until they
  become public.

Check 2 — immutability
  If the base version already had a valid ``date_published`` and the page is
  public (or is becoming public), the value must not change.

Existing public articles without the field are left alone (no backfill). Adding
the field later is allowed only when the date is older than the homepage
recency window (14 days) and is not in the future.
Renames of in-scope files are not treated as new.

Usage
-----
  python3 scripts/check_date_published.py --base origin/develop
  python3 scripts/check_date_published.py --base origin/develop --json findings.json
  python3 scripts/check_date_published.py --github-annotations findings.json

Exit codes
  0  No findings
  1  One or more findings
  2  Script or git error
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

COLLECTIONS = (
    'user_guide',
    'developer_guide',
    'api',
    'partners',
    'help',
)
SCOPE_PREFIXES = tuple(f'_docs/_{name}/' for name in COLLECTIONS)
HOMEPAGE_WINDOW_DAYS = 14

DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
FM_LINE_RE = re.compile(r'^([A-Za-z0-9_]+):\s*(.*?)\s*$')
TRUE_VALUES = frozenset({'true', 'yes', 'on'})
_ANNOTATION_FILE_RE = re.compile(
    r'^_docs/_(' + '|'.join(COLLECTIONS) + r')/[A-Za-z0-9_./\-]+\.md$'
)

CODES = {
    'missing': 'Missing date_published',
    'stale': 'date_published must not be in the past (UTC)',
    'malformed': 'Malformed date_published',
    'modified': 'date_published must not change',
    'recency': 'date_published would appear on the New card',
}


@dataclass(frozen=True)
class Frontmatter:
    exists: bool
    values: dict[str, str]
    key_lines: dict[str, int]
    last_key_line: int | None
    last_key_text: str | None
    opening_line: int | None
    date_line_text: str | None


EMPTY_FRONTMATTER = Frontmatter(
    exists=False,
    values={},
    key_lines={},
    last_key_line=None,
    last_key_text=None,
    opening_line=None,
    date_line_text=None,
)


@dataclass(frozen=True)
class DiffEntry:
    status: str
    head_path: str
    base_path: str | None


@dataclass(frozen=True)
class Finding:
    file: str
    code: str
    message: str
    line: int | None
    suggested_anchor_line: int | None
    suggested_original: str | None
    suggested_replacement: str | None
    expected_date: str | None
    current_value: str | None
    base_value: str | None


def utc_today() -> date:
    return datetime.now(timezone.utc).date()


def parse_iso_date(value: str | None) -> date | None:
    if not value or not DATE_RE.match(value):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def would_surface_on_new_card(value: date, today: date) -> bool:
    window_start = today - timedelta(days=HOMEPAGE_WINDOW_DAYS)
    return value >= window_start


def in_scope(path: str) -> bool:
    normalized = path.replace('\\', '/')
    return normalized.endswith('.md') and any(
        normalized.startswith(prefix) for prefix in SCOPE_PREFIXES
    )


def _unquote(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        return raw[1:-1]
    if ' #' in raw:
        raw = raw.split(' #', 1)[0].strip()
        if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
            return raw[1:-1]
    return raw


def parse_frontmatter(text: str) -> Frontmatter:
    if text.startswith('\ufeff'):
        text = text[1:]
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return EMPTY_FRONTMATTER

    values: dict[str, str] = {}
    key_lines: dict[str, int] = {}
    last_key_line: int | None = None
    last_key_text: str | None = None
    date_line_text: str | None = None
    closing_index: int | None = None

    for index, line in enumerate(lines[1:], start=2):
        if line.strip() == '---':
            closing_index = index
            break
        match = FM_LINE_RE.match(line)
        if not match:
            continue
        key, raw = match.group(1), match.group(2)
        values[key] = _unquote(raw)
        key_lines[key] = index
        last_key_line = index
        last_key_text = line
        if key == 'date_published':
            date_line_text = line

    if closing_index is None:
        return EMPTY_FRONTMATTER

    return Frontmatter(
        exists=True,
        values=values,
        key_lines=key_lines,
        last_key_line=last_key_line,
        last_key_text=last_key_text,
        opening_line=1,
        date_line_text=date_line_text,
    )


def is_yaml_true(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in TRUE_VALUES


def is_eligible(fm: Frontmatter) -> bool:
    return not is_yaml_true(fm.values.get('hidden')) and not is_yaml_true(
        fm.values.get('config_only')
    )


def parse_name_status_line(line: str) -> DiffEntry | None:
    line = line.strip()
    if not line:
        return None
    parts = line.split('\t')
    status_token = parts[0]
    status = status_token[0]
    if status in {'A', 'M'} and len(parts) == 2:
        path = parts[1]
        return DiffEntry(status, path, None if status == 'A' else path)
    if status in {'R', 'C'} and len(parts) == 3:
        old_path, new_path = parts[1], parts[2]
        if status == 'C':
            return DiffEntry('A', new_path, None)
        return DiffEntry('R', new_path, old_path)
    return None


def _suggestion_for_missing(fm: Frontmatter, today_iso: str) -> tuple[int, str | None, str | None]:
    new_line = f'date_published: "{today_iso}"'
    if not fm.exists:
        return 1, None, None
    opening = fm.opening_line or 1
    return opening, '---', f'---\n{new_line}'


def _suggestion_for_date_line(fm: Frontmatter, today_iso: str) -> tuple[int | None, str | None, str | None]:
    line_no = fm.key_lines.get('date_published')
    if line_no is None or fm.date_line_text is None:
        return None, None, None
    return line_no, fm.date_line_text, f'date_published: "{today_iso}"'


def _immutability_finding(
    *,
    head_path: str,
    head_fm: Frontmatter,
    base_fm: Frontmatter,
    base_date: str,
    head_date: str | None,
) -> Finding | None:
    line = head_fm.key_lines.get('date_published') or base_fm.key_lines.get(
        'date_published'
    )
    if head_date is None:
        original = base_fm.date_line_text or f'date_published: "{base_date}"'
        return Finding(
            file=head_path,
            code='modified',
            message=(
                f'`date_published` is a first-ship date and must not be removed. '
                f'Restore `{base_date}`.'
            ),
            line=line,
            suggested_anchor_line=line,
            suggested_original=None,
            suggested_replacement=original,
            expected_date=base_date,
            current_value=None,
            base_value=base_date,
        )
    if head_date != base_date:
        original = head_fm.date_line_text or f'date_published: "{head_date}"'
        return Finding(
            file=head_path,
            code='modified',
            message=(
                f'`date_published` is a first-ship date and must not change. '
                f'This file shipped with `{base_date}`.'
            ),
            line=line,
            suggested_anchor_line=line,
            suggested_original=original,
            suggested_replacement=f'date_published: "{base_date}"',
            expected_date=base_date,
            current_value=head_date,
            base_value=base_date,
        )
    return None


def evaluate_change(
    *,
    head_path: str,
    head_text: str,
    base_path: str | None,
    base_text: str | None,
    today: date,
) -> Finding | None:
    if not in_scope(head_path):
        return None

    head_fm = parse_frontmatter(head_text)
    base_fm = parse_frontmatter(base_text) if base_text is not None else EMPTY_FRONTMATTER
    base_in_scope = bool(base_path and in_scope(base_path) and base_text is not None)
    base_eligible = base_in_scope and is_eligible(base_fm)
    base_date = base_fm.values.get('date_published') if base_in_scope else None
    head_date = head_fm.values.get('date_published')
    today_iso = today.isoformat()
    head_eligible = is_eligible(head_fm)
    parsed_base_date = parse_iso_date(base_date)

    if base_eligible and base_date is not None:
        return _immutability_finding(
            head_path=head_path,
            head_fm=head_fm,
            base_fm=base_fm,
            base_date=base_date,
            head_date=head_date,
        )

    becoming_public = head_eligible and not base_eligible
    if becoming_public and parsed_base_date is not None and base_date is not None:
        return _immutability_finding(
            head_path=head_path,
            head_fm=head_fm,
            base_fm=base_fm,
            base_date=base_date,
            head_date=head_date,
        )

    if becoming_public:
        return _first_public_ship_finding(
            head_path=head_path,
            head_fm=head_fm,
            head_date=head_date,
            base_date=base_date,
            today=today,
            today_iso=today_iso,
        )

    if base_eligible and base_date is None and head_date:
        return _late_add_finding(
            head_path=head_path,
            head_fm=head_fm,
            head_date=head_date,
            today=today,
        )

    return None


def _first_public_ship_finding(
    *,
    head_path: str,
    head_fm: Frontmatter,
    head_date: str | None,
    base_date: str | None,
    today: date,
    today_iso: str,
) -> Finding | None:
    if head_date is None:
        anchor, original, replacement = _suggestion_for_missing(head_fm, today_iso)
        return Finding(
            file=head_path,
            code='missing',
            message=(
                f'Add `date_published: "{today_iso}"` (today, UTC) or the UTC date '
                'you expect this PR to merge. This field is required the first time '
                'a public article ships. Confirm the date is still accurate before merge.'
            ),
            line=anchor,
            suggested_anchor_line=anchor if original is not None else None,
            suggested_original=original,
            suggested_replacement=replacement,
            expected_date=today_iso,
            current_value=None,
            base_value=base_date,
        )

    parsed = parse_iso_date(head_date)
    if parsed is None:
        anchor, original, replacement = _suggestion_for_date_line(head_fm, today_iso)
        return Finding(
            file=head_path,
            code='malformed',
            message=(
                f'`date_published` must be a quoted ISO 8601 date (`YYYY-MM-DD`). '
                f'Replace it with `"{today_iso}"` (today, UTC) or a future UTC merge date.'
            ),
            line=anchor,
            suggested_anchor_line=anchor,
            suggested_original=original,
            suggested_replacement=replacement,
            expected_date=today_iso,
            current_value=head_date,
            base_value=base_date,
        )

    if parsed < today:
        anchor, original, replacement = _suggestion_for_date_line(head_fm, today_iso)
        return Finding(
            file=head_path,
            code='stale',
            message=(
                f'`date_published` must be today\'s UTC date (`{today_iso}`) or a '
                f'future UTC date (the day you expect this PR to merge). '
                f'This file has `{head_date}`, which is in the past.'
            ),
            line=anchor,
            suggested_anchor_line=anchor,
            suggested_original=original,
            suggested_replacement=replacement,
            expected_date=today_iso,
            current_value=head_date,
            base_value=base_date,
        )

    return None


def _late_add_finding(
    *,
    head_path: str,
    head_fm: Frontmatter,
    head_date: str,
    today: date,
) -> Finding | None:
    parsed = parse_iso_date(head_date)
    line = head_fm.key_lines.get('date_published')
    if parsed is None:
        return Finding(
            file=head_path,
            code='malformed',
            message=(
                '`date_published` must be a quoted ISO 8601 date (`YYYY-MM-DD`). '
                'On an already-public article, use a date older than '
                f'{HOMEPAGE_WINDOW_DAYS} days, or omit the field.'
            ),
            line=line,
            suggested_anchor_line=None,
            suggested_original=None,
            suggested_replacement=None,
            expected_date=None,
            current_value=head_date,
            base_value=None,
        )

    if would_surface_on_new_card(parsed, today):
        cutoff = (today - timedelta(days=HOMEPAGE_WINDOW_DAYS + 1)).isoformat()
        return Finding(
            file=head_path,
            code='recency',
            message=(
                'Do not add a `date_published` value that would appear on the '
                f'New in Braze Docs card (the last {HOMEPAGE_WINDOW_DAYS} days, '
                'or a future date) to an already-public article. Use a date on or '
                f'before `{cutoff}`, or omit the field.'
            ),
            line=line,
            suggested_anchor_line=None,
            suggested_original=None,
            suggested_replacement=None,
            expected_date=None,
            current_value=head_date,
            base_value=None,
        )
    return None


def git_repo_root() -> Path:
    result = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or 'not a git repository')
    return Path(result.stdout.strip())


def git_merge_base(root: Path, base: str) -> str:
    result = subprocess.run(
        ['git', 'merge-base', base, 'HEAD'],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip() or f'git merge-base failed against {base}'
        )
    sha = result.stdout.strip()
    if not sha:
        raise RuntimeError(f'git merge-base returned empty against {base}')
    return sha


def git_show(root: Path, ref: str, path: str) -> str:
    result = subprocess.run(
        ['git', 'show', f'{ref}:{path}'],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or f'exit {result.returncode}'
        raise RuntimeError(f'git show {ref}:{path} failed: {detail}')
    return result.stdout


def git_diff_entries(root: Path, base: str) -> list[DiffEntry]:
    result = subprocess.run(
        [
            'git',
            'diff',
            '--name-status',
            '--find-renames',
            '--diff-filter=ACMR',
            f'{base}...HEAD',
            '--',
            '_docs',
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f'git diff failed against {base}')
    entries: list[DiffEntry] = []
    for line in result.stdout.splitlines():
        entry = parse_name_status_line(line)
        if entry is None:
            continue
        if in_scope(entry.head_path):
            entries.append(entry)
    return entries


def collect_findings(
    *,
    root: Path,
    base: str,
    today: date,
) -> list[Finding]:
    merge_base = git_merge_base(root, base)
    findings: list[Finding] = []
    for entry in git_diff_entries(root, base):
        head_file = root / entry.head_path
        if not head_file.is_file():
            continue
        try:
            head_text = head_file.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError) as exc:
            raise RuntimeError(f'could not read {entry.head_path}: {exc}') from exc
        base_text = (
            git_show(root, merge_base, entry.base_path) if entry.base_path else None
        )
        finding = evaluate_change(
            head_path=entry.head_path,
            head_text=head_text,
            base_path=entry.base_path,
            base_text=base_text,
            today=today,
        )
        if finding is not None:
            findings.append(finding)
    return findings


def emit_github_annotations(findings_path: str) -> int:
    try:
        raw = json.loads(Path(findings_path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        print(f'error: {findings_path} not found', file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f'error: malformed JSON in {findings_path}: {exc}', file=sys.stderr)
        return 2

    if not isinstance(raw, list):
        print(f'error: {findings_path} must contain a JSON array', file=sys.stderr)
        return 2

    for item in raw:
        if not isinstance(item, dict):
            continue
        file = item.get('file', '')
        if not isinstance(file, str):
            continue
        file_norm = file.replace('\\', '/').strip()
        if '..' in file_norm or not _ANNOTATION_FILE_RE.match(file_norm):
            print(
                f'warning: skipping workflow annotation for unexpected file path: {file!r}',
                file=sys.stderr,
            )
            continue
        line = item.get('line')
        line_suffix = f',line={line}' if isinstance(line, int) and line > 0 else ''
        title = CODES.get(str(item.get('code', '')), 'date_published')
        msg = re.sub(r'\s+', ' ', str(item.get('message', '')).split('\n')[0].strip())
        msg = re.sub(r'[\r\n]', ' ', msg).replace('::', ': ')
        print(f'::error file={file_norm}{line_suffix},title={title}::{msg}')
    return 0


def _print_findings(findings: list[Finding]) -> None:
    for finding in findings:
        loc = f'{finding.file}:{finding.line}' if finding.line else finding.file
        print(f'{loc}: {finding.message}')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--base',
        help='Git ref to diff against (for example origin/develop)',
    )
    parser.add_argument('--json', dest='json_output', help='Write findings JSON to this path')
    parser.add_argument(
        '--github-annotations',
        metavar='FILE',
        help='Emit GitHub workflow annotations from a findings JSON file and exit',
    )
    parser.add_argument(
        '--today',
        help='Override UTC today (YYYY-MM-DD) for tests',
    )
    args = parser.parse_args(argv)

    if args.github_annotations:
        return emit_github_annotations(args.github_annotations)

    if not args.base:
        print('error: --base is required (for example origin/develop)', file=sys.stderr)
        return 2

    if args.today:
        if not DATE_RE.match(args.today):
            print('error: --today must be YYYY-MM-DD', file=sys.stderr)
            return 2
        today = date.fromisoformat(args.today)
    else:
        today = utc_today()

    try:
        root = git_repo_root()
        findings = collect_findings(root=root, base=args.base, today=today)
    except RuntimeError as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2

    if args.json_output:
        Path(args.json_output).write_text(
            json.dumps([asdict(item) for item in findings], indent=2) + '\n',
            encoding='utf-8',
        )

    if findings:
        _print_findings(findings)
        print(
            f'\n{len(findings)} date_published issue(s). '
            'Add or restore the field as described above. '
            "On first ship, use today's UTC date or a future UTC merge date.",
            file=sys.stderr,
        )
        return 1

    print('date_published check passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
