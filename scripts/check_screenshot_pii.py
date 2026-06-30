#!/usr/bin/env python3
"""
Scan documentation screenshots for likely PII before they are published.

Uses Tesseract OCR on PNG/JPG files under assets/img/ and flags patterns such as
real external_id-like values (alphanumeric or numeric IDs in import-style context),
person names, customer-specific attribute names, and production-style CSV preview data.
The literal labels ``external_id`` / ``external id`` alone are not flagged.

Dismissals (false positives)
----------------------------
Add a sidecar next to the image:

  assets/img/example.png.pii-audit-dismiss.json

  {
    "reason": "Required audit-trail explanation (min 10 characters)",
    "dismiss_all": false,
    "dismiss_ids": ["a1b2c3d4"]
  }

Maintainers may also add the ``pii-audit-dismissed`` label on the PR (CI only).
That bypasses blocking but leaves an audit comment on the PR.

Usage
-----
  python3 scripts/check_screenshot_pii.py path/to/image.png
  python3 scripts/check_screenshot_pii.py --json violations.json img1.png img2.png

Paths must be under ``assets/img/`` (run from the repo root, or any directory inside a Git checkout).

Exit codes
  0  No violations (after sidecar dismissals)
  1  One or more violations remain
  2  Script or dependency error
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict
from pathlib import Path

from pii_text_scan import (
    DISMISS_SUFFIX,
    Violation,
    active_violations,
    apply_dismissals,
    git_repo_root,
    load_dismiss_sidecar,
    scan_text,
)

IMAGE_SUFFIXES = {'.png', '.jpg', '.jpeg'}

_ANNOTATION_FILE_RE = re.compile(r'^assets/img/[A-Za-z0-9_./\-]+$')

__all__ = [
    'DISMISS_SUFFIX',
    'Violation',
    'active_violations',
    'apply_dismissals',
    'emit_github_annotations',
    'git_repo_root',
    'load_dismiss_sidecar',
    'resolve_cli_image_path',
    'scan_text',
]


def resolve_cli_image_path(raw: str, repo_root: Path) -> Path:
    """Resolve a CLI image path; must lie under assets/img/ in repo_root."""
    raw = raw.strip()
    if not raw or raw.startswith('-'):
        raise ValueError(f'Invalid image path: {raw!r}')
    candidate = (repo_root / raw).resolve()
    assets_img = (repo_root / 'assets' / 'img').resolve()
    try:
        candidate.relative_to(assets_img)
    except ValueError as exc:
        raise ValueError(
            f'Image path must be under assets/img/ (got path resolving to {candidate})'
        ) from exc
    if candidate.suffix.lower() not in IMAGE_SUFFIXES:
        raise ValueError(
            f'Unsupported image extension (expected .png, .jpg, or .jpeg): {raw!r}'
        )
    return candidate


def run_ocr(image_path: Path) -> str:
    if not shutil.which('tesseract'):
        raise RuntimeError(
            'tesseract is not installed. On macOS: brew install tesseract. '
            'On Ubuntu: apt-get install tesseract-ocr.'
        )

    result = subprocess.run(
        ['tesseract', str(image_path), 'stdout'],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f'tesseract failed for {image_path}: {result.stderr.strip() or result.stdout}'
        )
    return result.stdout


def check_image(image_path: Path) -> list[Violation]:
    resolved = image_path.resolve()
    if resolved.suffix.lower() not in IMAGE_SUFFIXES:
        return []

    if not resolved.is_file():
        print(f'warning: file not found: {image_path}', file=sys.stderr)
        return []

    repo = git_repo_root()
    try:
        file_key = resolved.relative_to(repo.resolve()).as_posix()
    except ValueError:
        file_key = resolved.as_posix()

    text = run_ocr(resolved)
    violations = scan_text(file_key, text)
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
        msg = re.sub(r'\s+', ' ', str(item.get('message', '')).split('\n')[0].strip())
        msg = re.sub(r'[\r\n]', ' ', msg)
        msg = msg.replace('::', ': ')
        print(f'::error file={file_norm},title=Screenshot PII audit::{msg}')
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
        print('error: provide one or more image paths under assets/img/', file=sys.stderr)
        return 2

    repo = git_repo_root()
    all_violations: list[Violation] = []
    for arg in args:
        try:
            path = resolve_cli_image_path(arg, repo)
        except ValueError as exc:
            print(f'error: {exc}', file=sys.stderr)
            return 2
        try:
            all_violations.extend(check_image(path))
        except (RuntimeError, ValueError) as exc:
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
                loc = f' (line {v.line_start})'
            print(
                f'{v.file}{loc} [{v.id}] [{v.violation_type}]: {v.message}\n'
                f'  Match: {v.match!r}\n'
                f'  Fix: {v.fix_hint}'
            )
        count = len(remaining)
        print(
            f'\nFound {count} screenshot PII violation{"s" if count != 1 else ""}. '
            'Fix the image, or add a .pii-audit-dismiss.json sidecar with a documented reason.'
        )
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
