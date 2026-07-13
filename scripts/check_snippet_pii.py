#!/usr/bin/env python3
"""
Scan fenced code blocks in English canonical markdown for likely PII.

Uses the same pattern library as ``check_screenshot_pii.py`` (via ``pii_text_scan``)
with snippet-specific tuning: skips alphanumeric external_id values common in API
examples, and relaxes numeric ID rules when the block uses documented placeholders.

Dismissals
----------
Add a sidecar next to the markdown file:

  _docs/path/to/page.md.pii-audit-dismiss.json

Same JSON shape as screenshot sidecars (``reason``, ``dismiss_ids``, ``dismiss_all``).

Usage
-----
  python3 scripts/check_snippet_pii.py _docs/user_guide/foo.md
  python3 scripts/check_snippet_pii.py --json violations.json _docs/foo.md _includes/bar.md

Paths must be under ``_docs/`` or root ``_includes/`` (English canonical only).

Exit codes
  0  No violations (after sidecar dismissals)
  1  One or more violations remain
  2  Script or dependency error
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from pii_text_scan import (
    Violation,
    active_violations,
    apply_dismissals,
    git_repo_root,
    scan_snippet_text,
)

DOC_PREFIXES = ('_docs/', '_includes/')
_ANNOTATION_FILE_RE = re.compile(r'^(?:_docs|_includes)/[A-Za-z0-9_./\-]+\.md$')

_FENCE_OPEN_RE = re.compile(r'^([ \t]*)(`{3,}|~{3,})(.*)$')


@dataclass(frozen=True)
class FencedBlock:
    body: str
    start_line: int
    end_line: int
    info: str


def resolve_cli_doc_path(raw: str, repo_root: Path) -> Path:
    raw = raw.strip().replace('\\', '/')
    if not raw or raw.startswith('-'):
        raise ValueError(f'Invalid markdown path: {raw!r}')
    if raw.startswith('_lang/'):
        raise ValueError(f'Locale paths are out of scope (got {raw!r})')
    if not any(raw.startswith(p) for p in DOC_PREFIXES):
        raise ValueError(
            f'Markdown path must be under _docs/ or _includes/ (got {raw!r})'
        )
    if not raw.endswith('.md'):
        raise ValueError(f'Expected a .md file (got {raw!r})')
    candidate = (repo_root / raw).resolve()
    docs = (repo_root / '_docs').resolve()
    includes = (repo_root / '_includes').resolve()
    try:
        candidate.relative_to(docs)
    except ValueError:
        try:
            candidate.relative_to(includes)
        except ValueError as exc:
            raise ValueError(
                f'Path must resolve under _docs/ or _includes/ (got {candidate})'
            ) from exc
    return candidate


def iter_fenced_blocks(markdown: str) -> list[FencedBlock]:
    """Return fenced code blocks (``` or ~~~) with 1-based line numbers."""
    lines = markdown.splitlines()
    blocks: list[FencedBlock] = []
    i = 0
    while i < len(lines):
        m = _FENCE_OPEN_RE.match(lines[i])
        if not m:
            i += 1
            continue
        indent, fence, info = m.group(1), m.group(2), m.group(3).strip()
        open_line = i + 1
        body_lines: list[str] = []
        i += 1
        close_re = re.compile(r'^' + re.escape(indent) + re.escape(fence) + r'\s*$')
        while i < len(lines):
            if close_re.match(lines[i]):
                close_line = i + 1
                body_start = open_line + 1
                body_end = close_line - 1 if body_lines else open_line
                blocks.append(
                    FencedBlock(
                        body='\n'.join(body_lines),
                        start_line=body_start,
                        end_line=body_end,
                        info=info,
                    )
                )
                i += 1
                break
            body_lines.append(lines[i])
            i += 1
    return blocks


def check_markdown_file(md_path: Path) -> list[Violation]:
    resolved = md_path.resolve()
    if not resolved.is_file():
        print(f'warning: file not found: {md_path}', file=sys.stderr)
        return []

    repo = git_repo_root()
    try:
        file_key = resolved.relative_to(repo.resolve()).as_posix()
    except ValueError:
        file_key = resolved.as_posix()

    text = resolved.read_text(encoding='utf-8', errors='replace')
    violations: list[Violation] = []
    for block in iter_fenced_blocks(text):
        if not block.body.strip():
            continue
        violations.extend(
            scan_snippet_text(
                file_key,
                block.body,
                line_start=block.start_line,
                line_end=block.end_line,
            )
        )
    return apply_dismissals(violations, resolved)


def emit_github_annotations(violations_path: str) -> int:
    try:
        raw = json.loads(Path(violations_path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        print(f'error: {violations_path} not found', file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f'error: malformed JSON in {violations_path}: {exc}', file=sys.stderr)
        return 2

    if not isinstance(raw, list):
        print(f'error: {violations_path} must contain a JSON array', file=sys.stderr)
        return 2

    for item in raw:
        if not isinstance(item, dict):
            continue
        if item.get('dismissed'):
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
        line = item.get('line_start')
        line_suffix = f',line={line}' if isinstance(line, int) and line > 0 else ''
        msg = re.sub(r'\s+', ' ', str(item.get('message', '')).split('\n')[0].strip())
        msg = re.sub(r'[\r\n]', ' ', msg)
        msg = msg.replace('::', ': ')
        print(f'::warning file={file_norm}{line_suffix},title=Snippet PII audit (advisory)::{msg}')
    return 0


def main() -> int:
    args = sys.argv[1:]
    json_output_path: str | None = None

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

    if not args:
        print(
            'error: provide one or more markdown paths under _docs/ or _includes/',
            file=sys.stderr,
        )
        return 2

    repo = git_repo_root()
    all_violations: list[Violation] = []
    for arg in args:
        try:
            path = resolve_cli_doc_path(arg, repo)
        except ValueError as exc:
            print(f'error: {exc}', file=sys.stderr)
            return 2
        try:
            all_violations.extend(check_markdown_file(path))
        except ValueError as exc:
            print(f'error: {exc}', file=sys.stderr)
            return 2

    if json_output_path:
        Path(json_output_path).write_text(
            json.dumps([asdict(v) for v in all_violations], indent=2),
            encoding='utf-8',
        )

    remaining = active_violations(all_violations)
    dismissed = [v for v in all_violations if v.dismissed]

    if dismissed:
        print(f'Dismissed {len(dismissed)} finding(s) via sidecar file(s):')
        for v in dismissed:
            print(f'  [{v.id}] {v.file}: {v.match!r} — {v.dismiss_reason}')

    if remaining:
        for v in remaining:
            loc = ''
            if v.line_start is not None:
                end = v.line_end if v.line_end and v.line_end != v.line_start else None
                loc = f' (lines {v.line_start}-{end})' if end else f' (line {v.line_start})'
            print(
                f'{v.file}{loc} [{v.id}] [{v.violation_type}]: {v.message}\n'
                f'  Match: {v.match!r}\n'
                f'  Fix: {v.fix_hint}'
            )
        count = len(remaining)
        print(
            f'\nFound {count} snippet PII violation{"s" if count != 1 else ""}. '
            'Fix the code block or add a .pii-audit-dismiss.json sidecar next to the markdown file.'
        )
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
