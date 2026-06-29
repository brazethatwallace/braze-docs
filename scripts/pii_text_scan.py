"""Shared PII pattern matching for Braze Docs screenshot OCR and markdown code snippets."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from pii_name_lexicon import GIVEN_NAMES, SURNAMES

DISMISS_SUFFIX = '.pii-audit-dismiss.json'

EXTERNAL_ID_HEADER_RE = re.compile(
    r'\b(?:external[_\s-]?id|ext[_\s-]?id)\b',
    re.IGNORECASE,
)

NUMERIC_USER_ID_RE = re.compile(r'\b(\d{6,10})\b')
ALPHANUMERIC_EXTERNAL_ID_RE = re.compile(r'\b([a-zA-Z]\d{5,7})\b')
EMAIL_RE = re.compile(
    r'\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b'
)
CUSTOMER_ATTRIBUTE_RE = re.compile(
    r'\b(?:OptIn_(?:Email|DM|Catalogue)_[A-Z][A-Za-z0-9_]+|Marketing_Transactor_Flag)\b'
)
PRODUCTION_CSV_FILENAME_RE = re.compile(
    r'\b(?:user[_-]?updates|customer[_-]?data|prod[_-]?export)[^.\s]*\.csv\b',
    re.IGNORECASE,
)
SINGLE_NAME_RE = re.compile(r'\b([A-Z][a-z]{2,20})\b')
NAME_LAST_COLUMN_RE = re.compile(r'\bName_Last\b', re.IGNORECASE)
NAME_COLUMN_CONTEXT_RE = re.compile(r'\bName(?:_Last)?\b', re.IGNORECASE)

SNIPPET_NAME_FIELD_RE = re.compile(
    r'"(?:first_?name|last_?name|full_?name|name)"\s*:',
    re.IGNORECASE,
)

SNIPPET_PLACEHOLDER_HINT_RE = re.compile(
    r'(?:YOUR[-_][A-Z0-9_-]+|<YOUR[^>]+>|\{YOUR[^}]+\}|PLACEHOLDER|REPLACE_ME|INSERT_)',
    re.IGNORECASE,
)

GIT_SSH_EMAIL_PREFIX = 'git@'
SQL_VARCHAR_SIZE_RE = re.compile(r'VARCHAR\s*\(\s*(\d+)\s*\)', re.IGNORECASE)
GEO_COORDINATE_CONTEXT_RE = re.compile(
    r'\b(?:coordinates|longitude|latitude|geojson|geofence)\b',
    re.IGNORECASE,
)
EPOCH_TIMESTAMP_FIELD_RE = re.compile(
    r'["\']?(?:started_at|ended_at|completed_at|originalTimestamp|original_timestamp|'
    r'request_timestamp|response_timestamp|created_at|updated_at|sent_at)["\']?\s*[:=]',
    re.IGNORECASE,
)
SQL_DATETIME_VARIABLE_RE = re.compile(
    r'\b(?:fromDateTime|toDateTime|startDate|endDate)\s*=',
    re.IGNORECASE,
)
COMMERCE_ID_FIELD_RE = re.compile(
    r'"(?:product_id|variant_id|checkout_id)"',
    re.IGNORECASE,
)
CREDENTIAL_FIELD_RE = re.compile(
    r'(?:partner_api_key|client_secret)',
    re.IGNORECASE,
)
ISO_TIMESTAMP_FRACTION_RE = re.compile(
    r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+',
)
SCHEMA_MODAL_WILL_RE = re.compile(r'\bWill only\b')
SCHEMA_MARK_VERB_RE = re.compile(r'\bEmail Mark As\b|\bMark As Spam\b')
STREET_ADDRESS_CONTEXT_RE = re.compile(r'\bMadison Avenue\b|\bMadison Ave\b', re.IGNORECASE)
TRIP_NAME_CONTEXT_RE = re.compile(r'\bSydney Trip\b', re.IGNORECASE)
HTTP_HEADER_RAY_RE = re.compile(r'\bCf-Ray\b')
ORDER_ID_CONTEXT_RE = re.compile(r'"(?:order_id)"\s*:|ORD-\d{8}-', re.IGNORECASE)

_UI_LIMIT_LABEL_TAIL = (
    'age', 'bids', 'characters', 'columns', 'depth', 'duration', 'height', 'length',
    'limit', 'recipients', 'rows', 'score', 'size', 'users', 'value', 'width',
)
_UI_LIMIT_AFTER_RE = re.compile(
    r'^\s+(?:' + '|'.join(re.escape(t) for t in _UI_LIMIT_LABEL_TAIL) + r')\b',
    re.IGNORECASE,
)

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

PERSON_NAME_PAIR_RE = re.compile(
    r'\b([A-Z][a-z]{2,20})\s+([A-Z][a-z]{2,20})\b'
)

EXAMPLE_SINGLE_NAMES = frozenset({'alex', 'lee', 'yuri'})
EXAMPLE_NAME_PAIRS = frozenset({
    'alex smith', 'alex lee', 'lee smith', 'yuri kim',
})

ALLOWLIST_EMAILS = frozenset({
    'test@example.com', 'alex@example.com', 'lee@example.com', 'yuri@example.com',
})
ALLOWLIST_DOMAINS = frozenset({'example.com', 'example.org', 'example.net'})
ALLOWLIST_LITERAL_TERMS = frozenset({'fakebrandz', 'dashboard-06'})


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
    line_start: int | None = None
    line_end: int | None = None


def git_repo_root() -> Path:
    workspace = os.environ.get('GITHUB_WORKSPACE')
    if workspace:
        return Path(workspace).resolve()
    here = Path.cwd().resolve()
    for parent in [here, *here.parents]:
        if (parent / '.git').is_dir() or (parent / '.git').is_file():
            return parent
    return here


def violation_id(file: str, violation_type: str, match: str) -> str:
    digest = hashlib.sha256(f'{file}:{violation_type}:{match}'.encode()).hexdigest()
    return digest[:8]


def load_dismiss_sidecar(target_path: Path) -> dict | None:
    sidecar = Path(str(target_path) + DISMISS_SUFFIX)
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


def apply_dismissals(violations: list[Violation], target_path: Path) -> list[Violation]:
    try:
        sidecar = load_dismiss_sidecar(target_path)
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


def active_violations(violations: list[Violation]) -> list[Violation]:
    return [v for v in violations if not v.dismissed]


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def is_allowlisted(match: str) -> bool:
    lowered = match.lower().strip()
    if lowered.startswith(GIT_SSH_EMAIL_PREFIX):
        return True
    if lowered in ALLOWLIST_EMAILS or lowered in ALLOWLIST_LITERAL_TERMS:
        return True
    if '@' in lowered:
        domain = lowered.rsplit('@', 1)[-1]
        return domain in ALLOWLIST_DOMAINS
    return 'fakebrandz' in lowered or 'dashboard-06' in lowered


def is_contraction_name_fragment(word: str, text: str, end_idx: int) -> bool:
    if word != 'Don':
        return False
    tail = text[end_idx:end_idx + 2]
    if tail.lower() in ("'t", "'T"):
        return True
    if end_idx < len(text) and text[end_idx] in ('\u2019', '\u2018'):
        return text[end_idx + 1:end_idx + 2].lower() == 't'
    return False


def is_schema_prose_false_positive_name(word: str, text: str) -> bool:
    lowered = word.lower()
    if lowered == 'will' and SCHEMA_MODAL_WILL_RE.search(text):
        return True
    if lowered == 'mark' and SCHEMA_MARK_VERB_RE.search(text):
        return True
    if lowered == 'madison' and STREET_ADDRESS_CONTEXT_RE.search(text):
        return True
    if lowered == 'sydney' and TRIP_NAME_CONTEXT_RE.search(text):
        return True
    if lowered == 'ray' and HTTP_HEADER_RAY_RE.search(text):
        return True
    return False


def should_skip_numeric_snippet_match(raw_text: str, match: str) -> bool:
    if match == '16777216' and SQL_VARCHAR_SIZE_RE.search(raw_text):
        return True
    if GEO_COORDINATE_CONTEXT_RE.search(raw_text):
        return True
    if EPOCH_TIMESTAMP_FIELD_RE.search(raw_text) and len(match) == 10 and match.isdigit():
        return True
    if SQL_DATETIME_VARIABLE_RE.search(raw_text) and len(match) == 10 and match.isdigit():
        return True
    if COMMERCE_ID_FIELD_RE.search(raw_text):
        return True
    if CREDENTIAL_FIELD_RE.search(raw_text):
        return True
    if ISO_TIMESTAMP_FRACTION_RE.search(raw_text):
        return True
    if ORDER_ID_CONTEXT_RE.search(raw_text):
        return True
    if 'plus:' in raw_text and match.isdigit():
        return True
    if 'tag=' in raw_text.lower() and 'sip:' in raw_text.lower():
        return True
    if re.search(r'\bassign\b', raw_text, re.IGNORECASE) and match.isdigit():
        # Liquid duration examples (seconds / day multiples).
        return True
    return False


def is_ui_limit_label_at(word: str, text: str, end_idx: int) -> bool:
    if word.lower() not in {'max', 'min'}:
        return False
    if _UI_LIMIT_AFTER_RE.match(text[end_idx:]):
        return True
    # Channel copy limits such as "Max 60 characters".
    return bool(re.match(r'^\s+\d+\s+\w', text[end_idx:]))


def words_from_documented_example_pairs(text: str) -> set[str]:
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
    if word.isupper() and len(word) > 1:
        return False
    return True


def is_plausible_given_name(word: str) -> bool:
    return word.lower() in GIVEN_NAMES


def is_plausible_surname(word: str) -> bool:
    return word.lower() in SURNAMES


def is_plausible_person_name_pair(first: str, last: str) -> bool:
    if not is_likely_person_name_word(first) or not is_likely_person_name_word(last):
        return False
    if is_plausible_given_name(first) and is_plausible_surname(last):
        return True
    if is_plausible_surname(first) and is_plausible_given_name(last):
        return True
    return False


def is_plausible_person_name_single(word: str, text: str) -> bool:
    if is_plausible_given_name(word):
        return True
    if NAME_LAST_COLUMN_RE.search(text) and is_plausible_surname(word):
        return True
    return False


def has_name_column_context(text: str) -> bool:
    return bool(NAME_COLUMN_CONTEXT_RE.search(text))


def has_person_name_context(text: str) -> bool:
    if has_name_column_context(text):
        return True
    if EXTERNAL_ID_HEADER_RE.search(text):
        return True
    return False


def has_snippet_name_column_context(text: str) -> bool:
    return has_name_column_context(text) or bool(SNIPPET_NAME_FIELD_RE.search(text))


def has_snippet_person_name_context(text: str) -> bool:
    if has_snippet_name_column_context(text):
        return True
    if EXTERNAL_ID_HEADER_RE.search(text):
        return True
    return False


def snippet_looks_like_documented_example(text: str) -> bool:
    if SNIPPET_PLACEHOLDER_HINT_RE.search(text):
        return True
    lowered = text.lower()
    return 'fakebrandz' in lowered or 'dashboard-06' in lowered


def find_person_name_pairs_with_context(
    text: str,
    has_context: Callable[[str], bool],
) -> list[str]:
    if not has_context(text):
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


def find_person_name_pairs(text: str) -> list[str]:
    return find_person_name_pairs_with_context(text, has_person_name_context)


def words_in_name_pairs(pairs: list[str]) -> set[str]:
    words: set[str] = set()
    for pair in pairs:
        for word in pair.split():
            words.add(word.lower())
    return words


def find_single_names_in_columns(
    text: str,
    paired_words: set[str],
    *,
    name_column_context: Callable[[str], bool] | None = None,
) -> list[str]:
    context_fn = name_column_context or has_name_column_context
    if not context_fn(text):
        return []

    seen: set[str] = set()
    matches: list[str] = []

    words_with_non_ui_occurrence: set[str] = set()
    for m in SINGLE_NAME_RE.finditer(text):
        word = m.group(1)
        if not is_likely_person_name_word(word):
            continue
        if is_contraction_name_fragment(word, text, m.end()):
            continue
        if is_schema_prose_false_positive_name(word, text):
            continue
        if word.lower() in {'max', 'min'} and is_ui_limit_label_at(word, text, m.end()):
            continue
        words_with_non_ui_occurrence.add(word)

    for word in sorted(words_with_non_ui_occurrence):
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


def person_name_fix_hint(*, for_snippet: bool = False) -> str:
    if for_snippet:
        return (
            'Replace real names with fictional examples from the '
            '[writing style guide](https://www.braze.com/docs/contributing/style_guide/writing_style_guide/) '
            '(for example alex@example.com, Alex Smith), or use documented placeholders '
            '(YOUR_REST_API_KEY). Add a `.pii-audit-dismiss.json` sidecar next to the '
            'markdown file if the value is already approved.'
        )
    return (
        'Replace employee or customer names with fictional examples from the '
        '[writing style guide](https://www.braze.com/docs/contributing/style_guide/writing_style_guide/) '
        '(unisex example names), blur the value, or retake from dashboard-06. '
        'If this is already an approved example name, add a .pii-audit-dismiss.json '
        'sidecar documenting that it is fictional.'
    )


def _scan_common_pii(
    file_key: str,
    normalized: str,
    *,
    source_label: str,
    for_snippet: bool,
    line_start: int | None = None,
    line_end: int | None = None,
    include_alphanumeric_ids: bool = True,
    include_numeric_ids: bool = True,
    numeric_id_min_count: int = 3,
    person_name_context: Callable[[str], bool] | None = None,
    name_column_context: Callable[[str], bool] | None = None,
    raw_text: str | None = None,
) -> list[Violation]:
    violations: list[Violation] = []
    fk = str(file_key).replace('\\', '/')
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
                line_start=line_start,
                line_end=line_end,
            )
        )

    for match in PRODUCTION_CSV_FILENAME_RE.findall(normalized):
        add(
            'production_csv_filename',
            match,
            f'{source_label} shows a production-style CSV filename ({match!r}).',
            'Use a generic example filename (for example, sample_import.csv).',
        )

    for match in CUSTOMER_ATTRIBUTE_RE.findall(normalized):
        add(
            'customer_attribute_name',
            match,
            f'{source_label} shows a customer-specific custom attribute name ({match!r}).',
            'Replace with generic FakeBrandz examples or documented placeholders.',
        )

    for match in EMAIL_RE.findall(normalized):
        add(
            'email_address',
            match,
            f'{source_label} may contain a real email address ({match!r}).',
            'Use name@example.com placeholders per the style guide.',
        )

    if include_alphanumeric_ids:
        for match in ALPHANUMERIC_EXTERNAL_ID_RE.findall(normalized):
            add(
                'alphanumeric_external_id',
                match,
                f'{source_label} may contain a real external_id value ({match!r}).',
                'Replace with fictional IDs from dashboard-06 or documented placeholders.',
            )

    if include_numeric_ids:
        numeric_id_matches = NUMERIC_USER_ID_RE.findall(normalized)
        nearby_external = bool(EXTERNAL_ID_HEADER_RE.search(normalized))
        numeric_count = len(numeric_id_matches)
        if nearby_external or numeric_count >= numeric_id_min_count:
            snippet_source = raw_text if raw_text is not None else normalized
            for match in numeric_id_matches:
                if for_snippet and should_skip_numeric_snippet_match(snippet_source, match):
                    continue
                add(
                    'numeric_user_id',
                    match,
                    f'{source_label} may contain real numeric user identifiers ({match!r}).',
                    'Replace with fictional IDs from dashboard-06 or documented placeholders.',
                )

    ctx_fn = person_name_context or has_person_name_context
    name_pairs = find_person_name_pairs_with_context(normalized, ctx_fn)
    paired_words = words_in_name_pairs(name_pairs) | words_from_documented_example_pairs(
        normalized
    )
    fix_hint = person_name_fix_hint(for_snippet=for_snippet)

    for match in name_pairs:
        add(
            'person_name',
            match,
            f'{source_label} may contain a person name ({match!r}).',
            fix_hint,
        )

    for match in find_single_names_in_columns(
        normalized,
        paired_words,
        name_column_context=name_column_context or has_name_column_context,
    ):
        add(
            'person_name_single',
            match,
            f'{source_label} may contain a person name in a Name/Name_Last column ({match!r}).',
            fix_hint,
        )

    return violations


def scan_text(image_file_key: str, text: str) -> list[Violation]:
    normalized = normalize_text(text)
    if not normalized:
        return []
    return _scan_common_pii(
        image_file_key,
        normalized,
        source_label='Screenshot',
        for_snippet=False,
        include_alphanumeric_ids=True,
        include_numeric_ids=True,
        numeric_id_min_count=3,
    )


def scan_snippet_text(
    file_key: str,
    text: str,
    *,
    line_start: int | None = None,
    line_end: int | None = None,
) -> list[Violation]:
    """Scan a fenced code block with rules tuned for docs snippets."""
    normalized = normalize_text(text)
    if not normalized:
        return []

    skip_numeric = snippet_looks_like_documented_example(text)
    return _scan_common_pii(
        file_key,
        normalized,
        source_label='Code snippet',
        for_snippet=True,
        line_start=line_start,
        line_end=line_end,
        include_alphanumeric_ids=False,
        include_numeric_ids=not skip_numeric,
        numeric_id_min_count=4,
        person_name_context=has_snippet_person_name_context,
        name_column_context=has_snippet_name_column_context,
        raw_text=text,
    )
