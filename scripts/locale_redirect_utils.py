"""Shared helpers for locale-prefixed redirect mirrors."""

from __future__ import annotations

import re

LOCALES = ("ko", "es", "fr", "pt-br", "ja", "de")
LOCALE_SEGMENT = r"(?:ko|es|fr|pt-br|ja|de)"
LOCALE_IN_PATH = re.compile(rf"^/docs/{LOCALE_SEGMENT}(/|$)")

VALIDURLS_RE = re.compile(
    r"validurls\['((?:\\'|[^'])*)'\]\s*=\s*'((?:\\'|[^'])*)'\s*;"
)


def unescape_js_string(value: str) -> str:
    return value.replace("\\'", "'")


def escape_js_string(value: str) -> str:
    return value.replace("'", "\\'")


def parse_validurls(js_text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in js_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("//"):
            continue
        match = VALIDURLS_RE.search(stripped)
        if not match:
            continue
        source = unescape_js_string(match.group(1))
        dest = unescape_js_string(match.group(2))
        entries[source] = dest
    return entries


def strip_locale_prefix(path: str) -> tuple[str | None, str]:
    match = re.match(rf"^/docs/({LOCALE_SEGMENT})(/.*)$", path)
    if not match:
        return None, path
    return match.group(1), f"/docs{match.group(2)}"


def add_locale_prefix(locale: str, path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    if LOCALE_IN_PATH.match(path):
        return path
    if path.startswith("/docs/"):
        return f"/docs/{locale}{path[5:]}"
    return path


def is_en_bulk_source(path: str) -> bool:
    if not path.startswith("/docs/"):
        return False
    if LOCALE_IN_PATH.match(path):
        return False
    if "#" in path.split("?", 1)[0]:
        return False
    if "?" in path:
        return False
    return True


def is_bulk_eligible_source(path: str) -> bool:
    base = path.split("?", 1)[0]
    return "#" not in base and "?" not in path


def format_validurl_line(source: str, dest: str) -> str:
    return (
        f"validurls['{escape_js_string(source)}'] = "
        f"'{escape_js_string(dest)}';"
    )


def mirror_en_redirect_to_locales(
    source: str,
    destination: str,
    existing: dict[str, str],
) -> list[tuple[str, str]]:
    """Return locale mirror pairs not already present in existing."""
    if not is_en_bulk_source(source):
        return []
    if destination.startswith("http://") or destination.startswith("https://"):
        if "/docs/" not in destination:
            return []

    mirrors: list[tuple[str, str]] = []
    for locale in LOCALES:
        locale_source = add_locale_prefix(locale, source)
        locale_dest = add_locale_prefix(locale, destination)
        if locale_source == locale_dest:
            continue
        if locale_source in existing:
            continue
        mirrors.append((locale_source, locale_dest))
    return mirrors


def missing_locale_mirrors(validurls: dict[str, str]) -> list[tuple[str, str]]:
    """All locale mirrors missing for EN bulk-eligible redirects."""
    missing: list[tuple[str, str]] = []
    seen: set[str] = set()
    for source, destination in validurls.items():
        for locale_source, locale_dest in mirror_en_redirect_to_locales(
            source, destination, validurls
        ):
            if locale_source in seen:
                continue
            seen.add(locale_source)
            missing.append((locale_source, locale_dest))
    missing.sort(key=lambda pair: pair[0])
    return missing


def missing_mirrors_for_en_sources(
    sources: list[str],
    validurls: dict[str, str],
) -> list[tuple[str, str]]:
    """Locale mirrors missing for a specific list of EN redirect sources."""
    missing: list[tuple[str, str]] = []
    seen: set[str] = set()
    for source in sources:
        destination = validurls.get(source)
        if destination is None:
            continue
        for locale_source, locale_dest in mirror_en_redirect_to_locales(
            source, destination, validurls
        ):
            if locale_source in seen:
                continue
            seen.add(locale_source)
            missing.append((locale_source, locale_dest))
    missing.sort(key=lambda pair: pair[0])
    return missing


def parse_added_validurl_sources(diff_text: str) -> list[str]:
    """Return EN validurl sources added in a git diff of broken_redirect_list.js."""
    added: list[str] = []
    for line in diff_text.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        match = VALIDURLS_RE.search(line[1:])
        if not match:
            continue
        source = unescape_js_string(match.group(1))
        if is_en_bulk_source(source):
            added.append(source)
    return added
