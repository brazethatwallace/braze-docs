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

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from pii_name_lexicon import GIVEN_NAMES, SURNAMES

IMAGE_SUFFIXES = {'.png', '.jpg', '.jpeg'}
DISMISS_SUFFIX = '.pii-audit-dismiss.json'

# Workflow annotations: only emit paths that look like normal repo image paths.
_ANNOTATION_FILE_RE = re.compile(r'^assets/img/[A-Za-z0-9_./\-]+$')


def git_repo_root() -> Path:
    """Repository root (for path checks). Prefers GITHUB_WORKSPACE, else nearest .git parent."""
    workspace = os.environ.get('GITHUB_WORKSPACE')
    if workspace:
        return Path(workspace).resolve()
    here = Path.cwd().resolve()
    for parent in [here, *here.parents]:
        if (parent / '.git').is_dir() or (parent / '.git').is_file():
            return parent
    return here


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

# Import / mapping UI labels (not violations themselves). Used as context so we only
# flag numeric IDs when an external-id style column is present or many IDs appear.
EXTERNAL_ID_HEADER_RE = re.compile(
    r'\b(?:external[_\s-]?id|ext[_\s-]?id)\b',
    re.IGNORECASE,
)

# Numeric IDs typical of production external_id / user_id columns (6–10 digits).
NUMERIC_USER_ID_RE = re.compile(r'\b(\d{6,10})\b')

# Alphanumeric external IDs (e.g. a82415) common in Braze CSV imports.
ALPHANUMERIC_EXTERNAL_ID_RE = re.compile(r'\b([a-zA-Z]\d{5,7})\b')

# Real email addresses. Do not use a domain-prefix negative lookahead here: it would
# skip matches like user@example.community (domain starts with example.com but is not
# an allowlisted placeholder). Rely on is_allowlisted() for exact example.* domains.
EMAIL_RE = re.compile(
    r'\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b'
)

# Customer-specific custom attribute naming seen in production CSV exports.
CUSTOMER_ATTRIBUTE_RE = re.compile(
    r'\b(?:OptIn_(?:Email|DM|Catalogue)_[A-Z][A-Za-z0-9_]+|Marketing_Transactor_Flag)\b'
)

# Production-style CSV filenames in upload modals.
PRODUCTION_CSV_FILENAME_RE = re.compile(
    r'\b(?:user[_-]?updates|customer[_-]?data|prod[_-]?export)[^.\s]*\.csv\b',
    re.IGNORECASE,
)

# Capitalized single token that may be a first or last name in a table column.
SINGLE_NAME_RE = re.compile(r'\b([A-Z][a-z]{2,20})\b')

# Name_Last column header in CSV import previews.
NAME_LAST_COLUMN_RE = re.compile(r'\bName_Last\b', re.IGNORECASE)

# Name / Name_Last column headers in CSV import previews.
NAME_COLUMN_CONTEXT_RE = re.compile(r'\bName(?:_Last)?\b', re.IGNORECASE)

# UI, product, and docs vocabulary — not person names.
NON_NAME_WORDS = frozenset({
    'about', 'access', 'account', 'action', 'actions', 'active', 'add', 'additional', 'adobe',
    'alert', 'alias', 'all', 'analytics', 'and', 'any', 'app', 'apps', 'apply', 'are',
    'assign', 'attribution', 'attribute', 'attributes', 'audience', 'audit', 'automatic',
    'automate', 'available', 'awarded', 'azure', 'back', 'basic', 'before', 'blocks',
    'body', 'brand', 'braze', 'browse', 'bucket', 'build', 'business', 'button',
    'calculate', 'calculated', 'callback', 'campaign', 'campaigns', 'cancel', 'canvas',
    'cap', 'capping', 'card', 'cards', 'catalogue', 'catalogues', 'category', 'center',
    'change', 'changelog', 'changes', 'channel', 'channels', 'check', 'checkbox', 'choose',
    'city', 'click', 'clone', 'cloud', 'column', 'columns', 'company', 'complete',
    'completed', 'compose', 'configuration', 'connected', 'content', 'context', 'control',
    'conversion', 'copy', 'correct', 'count', 'country', 'created', 'create', 'criterion',
    'criteria', 'credits', 'customer', 'custom', 'dark', 'dashboard', 'data', 'date',
    'decision', 'default', 'delivery', 'description', 'detected', 'developer', 'development',
    'details', 'device', 'disable', 'do', 'download', 'drag', 'edit', 'edited', 'else',
    'email', 'enable', 'enabled', 'end', 'enter', 'entry', 'error', 'errors', 'estimated',
    'everyone', 'event', 'events', 'exact', 'experience', 'exit', 'experiment', 'export',
    'extension', 'external', 'feature', 'features', 'field', 'fields', 'file', 'files',
    'filter', 'filters', 'firebase', 'first', 'flag', 'flags', 'flow', 'folder', 'for',
    'format', 'found', 'frequency', 'from', 'full', 'game', 'getting', 'global', 'google',
    'group', 'groups', 'guide', 'help', 'here', 'history', 'hours', 'identity', 'identifier',
    'identifiers', 'import', 'importing', 'in', 'info', 'input', 'insights', 'install',
    'integrate', 'integration', 'integrations', 'issues', 'item', 'items', 'key', 'label',
    'last', 'learn', 'limit', 'link', 'liquid', 'listener', 'list', 'log', 'looks', 'make',
    'map', 'mapping', 'marketing', 'match', 'members', 'menu', 'message', 'messages',
    'messaging', 'method', 'methods', 'microsoft', 'modal', 'mode', 'model', 'more', 'name',
    'new', 'next', 'none', 'not', 'notification', 'number', 'object', 'open', 'opt',
    'opted', 'optional', 'options', 'order', 'outbound', 'overview', 'page', 'pages',
    'pairs', 'pacific', 'panel', 'partial', 'partners', 'paths', 'performance', 'phases',
    'phone', 'policies', 'policy', 'preferences', 'predictive', 'preview', 'previewing',
    'primary', 'prize', 'privacy', 'profile', 'profiles', 'public', 'publish', 'push',
    'quiet', 'rate', 'raw', 'react', 'received', 'recipients', 'report', 'request',
    'requests', 'resource', 'results', 'rich', 'role', 'row', 'rows', 'rules', 'saved',
    'schedule', 'scheduled', 'search', 'secret', 'section', 'segment', 'segments', 'select',
    'selected', 'send', 'session', 'set', 'settings', 'shopify', 'shortcuts', 'shortening',
    'show', 'since', 'sms', 'snippet', 'split', 'start', 'started', 'state', 'states',
    'statistics', 'status', 'step', 'steps', 'string', 'subscribe', 'subscribed',
    'subscription', 'successfully', 'summary', 'switch', 'tag', 'targeting', 'technology',
    'template', 'test', 'text', 'that', 'the', 'this', 'time', 'together', 'total',
    'tracking', 'transactor', 'trigger', 'triggered', 'type', 'unity', 'unique', 'united',
    'unsubscribed', 'update', 'updates', 'upload', 'upsert', 'usage', 'used', 'user',
    'users', 'validate', 'validation', 'value', 'variable', 'variables', 'view', 'viewed',
    'warning', 'warnings', 'web', 'webhook', 'when', 'with', 'work', 'workspace', 'zone',
    'your', 'you',
    'fakebrandz', 'fake', 'brandz',
})

# Capitalized first + last name patterns (e.g. Jordan Miller).
PERSON_NAME_PAIR_RE = re.compile(
    r'\b([A-Z][a-z]{2,20})\s+([A-Z][a-z]{2,20})\b'
)

# Documented fictional example first names (writing style guide).
EXAMPLE_SINGLE_NAMES = frozenset({
    'alex',
    'lee',
    'yuri',
})

# Documented fictional example full names (writing style guide / dashboard-06).
# Only full "First Last" pairs are auto-allowed — not single names.
EXAMPLE_NAME_PAIRS = frozenset({
    'alex smith',
    'alex lee',
    'lee smith',
    'yuri kim',
})

# Braze dashboard placeholder domains / brands (style guide).
ALLOWLIST_EMAILS = frozenset({
    'test@example.com',
    'alex@example.com',
    'lee@example.com',
    'yuri@example.com',
})

ALLOWLIST_DOMAINS = frozenset({
    'example.com',
    'example.org',
    'example.net',
})

ALLOWLIST_LITERAL_TERMS = frozenset({
    'fakebrandz',
    'dashboard-06',
})

@dataclass
class Violation:
    id: str
    file: str
    violation_type: str
    match: str
    message: str
    fix_hint: str
    dismissed: bool = False
    dismiss_reason: str | None = None


def violation_id(file: str, violation_type: str, match: str) -> str:
    digest = hashlib.sha256(f'{file}:{violation_type}:{match}'.encode()).hexdigest()
    return digest[:8]


def load_dismiss_sidecar(image_path: Path) -> dict | None:
    sidecar = Path(str(image_path) + DISMISS_SUFFIX)
    if not sidecar.is_file():
        return None
    try:
        data = json.loads(sidecar.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        raise ValueError(f'Invalid JSON in {sidecar}: {exc}') from exc
    if not isinstance(data, dict):
        raise ValueError(
            f'{sidecar} must be a JSON object (got {type(data).__name__}, expected an object '
            'with "reason", optional "dismiss_all", and optional "dismiss_ids").'
        )
    dismiss_all_raw = data.get('dismiss_all', False)
    if not isinstance(dismiss_all_raw, bool):
        raise ValueError(
            f'{sidecar}: "dismiss_all" must be a JSON boolean true or false, '
            f'not {type(dismiss_all_raw).__name__}.'
        )
    dismiss_ids_raw = data.get('dismiss_ids')
    if dismiss_ids_raw is None:
        data['dismiss_ids'] = []
    elif not isinstance(dismiss_ids_raw, list):
        raise ValueError(
            f'{sidecar}: "dismiss_ids" must be a JSON array of finding IDs, '
            f'not {type(dismiss_ids_raw).__name__}.'
        )
    else:
        data['dismiss_ids'] = [str(x) for x in dismiss_ids_raw]
    reason = str(data.get('reason', '')).strip()
    if len(reason) < 10:
        raise ValueError(
            f'{sidecar} must include a "reason" string of at least 10 characters.'
        )
    return data


def apply_dismissals(violations: list[Violation], image_path: Path) -> list[Violation]:
    try:
        sidecar = load_dismiss_sidecar(image_path)
    except ValueError as exc:
        print(f'error: {exc}', file=sys.stderr)
        raise

    if not sidecar:
        return violations

    dismiss_all = bool(sidecar.get('dismiss_all', False))
    dismiss_ids = {str(x) for x in sidecar.get('dismiss_ids', [])}
    reason = str(sidecar['reason']).strip()

    for v in violations:
        if dismiss_all or v.id in dismiss_ids:
            v.dismissed = True
            v.dismiss_reason = reason

    return violations


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


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def is_allowlisted(match: str) -> bool:
    lowered = match.lower().strip()
    if lowered in ALLOWLIST_EMAILS or lowered in ALLOWLIST_LITERAL_TERMS:
        return True
    if '@' in lowered:
        domain = lowered.rsplit('@', 1)[-1]
        return domain in ALLOWLIST_DOMAINS
    return 'fakebrandz' in lowered or 'dashboard-06' in lowered


def words_from_documented_example_pairs(text: str) -> set[str]:
    """Words from style-guide example full names present in OCR text."""
    words: set[str] = set()
    normalized_lower = normalize_text(text).lower()
    for pair in EXAMPLE_NAME_PAIRS:
        if pair in normalized_lower:
            words.update(pair.split())
    return words


def is_likely_person_name_word(word: str) -> bool:
    if not word.isalpha():
        return False
    if word.lower() in NON_NAME_WORDS:
        return False
    # All-caps tokens are usually column headers or acronyms.
    if word.isupper() and len(word) > 1:
        return False
    return True


def is_plausible_given_name(word: str) -> bool:
    return word.lower() in GIVEN_NAMES


def is_plausible_surname(word: str) -> bool:
    return word.lower() in SURNAMES


def is_plausible_person_name_pair(first: str, last: str) -> bool:
    """True when OCR text looks like a real First Last person name."""
    if not is_likely_person_name_word(first) or not is_likely_person_name_word(last):
        return False
    first_key = first.lower()
    last_key = last.lower()
    # English given-name + surname order (Jordan Miller, Casey Higgins).
    if first_key in GIVEN_NAMES:
        return True
    # Surname-first order is rare in Braze UI tables but can appear in OCR.
    if first_key in SURNAMES and last_key in GIVEN_NAMES:
        return True
    return False


def is_plausible_person_name_single(word: str, text: str) -> bool:
    """True when a lone capitalized token looks like a given or family name."""
    key = word.lower()
    if key in GIVEN_NAMES:
        return True
    if NAME_LAST_COLUMN_RE.search(text) and key in SURNAMES:
        return True
    return False


def find_person_name_pairs(text: str) -> list[str]:
    """Return unique 'First Last' strings that may be person names."""
    if not has_person_name_context(text):
        return []

    seen: set[str] = set()
    matches: list[str] = []

    for first, last in PERSON_NAME_PAIR_RE.findall(text):
        if not is_plausible_person_name_pair(first, last):
            continue
        pair = f'{first} {last}'
        key = pair.lower()
        if key in EXAMPLE_NAME_PAIRS:
            continue
        if key in seen:
            continue
        seen.add(key)
        matches.append(pair)

    return matches


def words_in_name_pairs(pairs: list[str]) -> set[str]:
    words: set[str] = set()
    for pair in pairs:
        for word in pair.split():
            words.add(word.lower())
    return words


def has_name_column_context(text: str) -> bool:
    return bool(NAME_COLUMN_CONTEXT_RE.search(text))


def has_person_name_context(text: str) -> bool:
    """OCR text suggests a user table or profile listing real names."""
    if has_name_column_context(text):
        return True
    if EXTERNAL_ID_HEADER_RE.search(text):
        return True
    return False


def find_single_names_in_columns(text: str, paired_words: set[str]) -> list[str]:
    """Flag lone first/last names when Name or Name_Last columns are present."""
    if not has_name_column_context(text):
        return []

    seen: set[str] = set()
    matches: list[str] = []

    for word in SINGLE_NAME_RE.findall(text):
        if not is_likely_person_name_word(word):
            continue
        key = word.lower()
        if key in EXAMPLE_SINGLE_NAMES:
            continue
        if not is_plausible_person_name_single(word, text):
            continue
        if key in paired_words:
            continue
        if key in seen:
            continue
        seen.add(key)
        matches.append(word)

    return matches


def person_name_fix_hint() -> str:
    return (
        'Replace employee or customer names with fictional examples from the '
        '[writing style guide](https://www.braze.com/docs/contributing/style_guide/writing_style_guide/) '
        '(unisex example names), blur the value, or retake from dashboard-06. '
        'If this is already an approved example name, add a .pii-audit-dismiss.json '
        'sidecar documenting that it is fictional.'
    )


def scan_text(image_file_key: str, text: str) -> list[Violation]:
    violations: list[Violation] = []
    normalized = normalize_text(text)
    if not normalized:
        return violations

    fk = str(image_file_key).replace('\\', '/')

    seen_violation_ids: set[str] = set()

    def add(violation_type: str, match: str, message: str, fix_hint: str) -> None:
        if is_allowlisted(match):
            return
        vid = violation_id(fk, violation_type, match)
        if vid in seen_violation_ids:
            return
        seen_violation_ids.add(vid)
        violations.append(
            Violation(
                id=vid,
                file=fk,
                violation_type=violation_type,
                match=match,
                message=message,
                fix_hint=fix_hint,
            )
        )

    for match in PRODUCTION_CSV_FILENAME_RE.findall(normalized):
        add(
            'production_csv_filename',
            match,
            f'Screenshot shows a production-style CSV filename ({match!r}).',
            'Rename the file in the screenshot to a generic example (for example, '
            'sample_import.csv) or blur the filename.',
        )

    for match in CUSTOMER_ATTRIBUTE_RE.findall(normalized):
        add(
            'customer_attribute_name',
            match,
            f'Screenshot shows a customer-specific custom attribute name ({match!r}).',
            'Retake the screenshot from dashboard-06 with FakeBrandz test data, or blur '
            'custom attribute names that are not generic examples.',
        )

    for match in EMAIL_RE.findall(normalized):
        add(
            'email_address',
            match,
            f'Screenshot may contain a real email address ({match!r}).',
            'Blur the address or use name@example.com placeholders per the style guide.',
        )

    for match in ALPHANUMERIC_EXTERNAL_ID_RE.findall(normalized):
        add(
            'alphanumeric_external_id',
            match,
            f'Screenshot may contain a real external_id value ({match!r}).',
            'Replace with fictional IDs from dashboard-06 or blur identifier values.',
        )

    # Require at least one nearby external-id signal or multiple numeric IDs (table data).
    numeric_id_matches = NUMERIC_USER_ID_RE.findall(normalized)
    nearby_external = bool(EXTERNAL_ID_HEADER_RE.search(normalized))
    numeric_count = len(numeric_id_matches)
    if nearby_external or numeric_count >= 3:
        for match in numeric_id_matches:
            add(
                'numeric_user_id',
                match,
                f'Screenshot may contain real numeric user identifiers ({match!r}).',
                'Blur external_id / user_id preview rows or retake from dashboard-06 with '
                'FakeBrandz fixture data.',
            )

    name_pairs = find_person_name_pairs(normalized)
    paired_words = words_in_name_pairs(name_pairs) | words_from_documented_example_pairs(
        normalized
    )
    fix_hint = person_name_fix_hint()

    for match in name_pairs:
        add(
            'person_name',
            match,
            f'Screenshot may contain a person name ({match!r}).',
            fix_hint,
        )

    for match in find_single_names_in_columns(normalized, paired_words):
        add(
            'person_name_single',
            match,
            f'Screenshot may contain a person name in a Name/Name_Last column ({match!r}).',
            fix_hint,
        )

    return violations


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


def active_violations(violations: list[Violation]) -> list[Violation]:
    return [v for v in violations if not v.dismissed]


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
            print(
                f'{v.file} [{v.id}] [{v.violation_type}]: {v.message}\n'
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
