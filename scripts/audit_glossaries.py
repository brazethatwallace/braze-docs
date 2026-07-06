#!/usr/bin/env python3
"""
Audit braze-docs glossaries against source-of-truth localization files.

``scripts/glossaries/*.json`` are synced from Phrase TMS term bases
(``scripts/sync_glossaries_from_phrase.py``). This script compares those
glossaries against in-product locale files to surface drift:

  - Platform dashboard locale files (dashboard/config/locales/*.{lang}.braze.json)
  - Android SDK strings (android-sdk-ui/src/main/res/values*/strings.xml)
  - Swift SDK strings (Sources/BrazeUI/Resources/Localization/*.lproj/*.strings)
  - GrapesJS locale files (src/i18n/locale/{lang}.js)

With ``--fix``, updates glossary files from product repos and propagates
changes into ``_lang/`` docs. **Deprecated for routine use** — prefer
updating Phrase term bases and re-running the Phrase sync instead.

Usage:
    python audit_glossaries.py [--platform-repo ../platform] [--output report.json]
    python audit_glossaries.py --fix [--output report.json]   # legacy; avoid in CI
    python audit_glossaries.py --fix --no-propagate-locales
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"

# Single source of truth for the Braze product-name allowlist — shared with
# ``scripts/auto_translate.py``'s runtime glossary override so the two
# scripts can't drift apart. The previous "keep in sync" duplication was
# flagged by Copilot on PR #13303.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _glossary_protected_terms import PROTECTED_PRODUCT_TERMS  # noqa: E402
from _glossary_locale_propagation import propagate_glossary_changes  # noqa: E402


def _protected_value(term, lang_key):
    """Canonical glossary value for a protected product term, or ``None``.

    Returns ``None`` if ``term`` is not in the protected allowlist; the
    locale-specific override if one exists (e.g. ``Canvases`` → ``Canvas``
    in Romance locales); otherwise falls back to the English term.
    """
    if term not in PROTECTED_PRODUCT_TERMS:
        return None
    return PROTECTED_PRODUCT_TERMS[term].get(lang_key, term)

LANG_MAP = {
    "de":    {"platform": "de",    "android": "values-de",  "swift": "de",    "grapesjs": "de"},
    "es":    {"platform": "es",    "android": "values-es",  "swift": "es",    "grapesjs": "es"},
    "fr":    {"platform": "fr",    "android": "values-fr",  "swift": "fr",    "grapesjs": "fr"},
    "ja":    {"platform": "ja",    "android": "values-ja",  "swift": "ja",    "grapesjs": None},
    "ko":    {"platform": "ko",    "android": "values-ko",  "swift": "ko",    "grapesjs": "ko"},
    "pt-br": {"platform": "pt-br", "android": "values-pt",  "swift": "pt",    "grapesjs": "pt"},
}

# ---------------------------------------------------------------------------
# Parsers for each source repo
# ---------------------------------------------------------------------------

def _extract_leaves(obj):
    """Recursively extract leaf string values from nested dicts."""
    for v in obj.values():
        if isinstance(v, dict):
            yield from _extract_leaves(v)
        elif isinstance(v, str):
            yield v


def parse_platform(repo_path, lang_key):
    """Parse platform dashboard locale files. Returns {english: translation}."""
    locales = Path(repo_path) / "dashboard" / "config" / "locales"
    if not locales.is_dir():
        return {}

    en_files = sorted(locales.glob("*.en.braze.json"))
    pairs = {}

    for en_file in en_files:
        namespace = en_file.name.rsplit(".en.braze.json", 1)[0]
        lang_file = locales / f"{namespace}.{lang_key}.braze.json"
        if not lang_file.exists():
            continue

        try:
            en_data = json.loads(en_file.read_text())
            lang_data = json.loads(lang_file.read_text())
        except (json.JSONDecodeError, OSError):
            continue

        # Strip the top-level language key so flattened paths match
        # Structure: {"en": {"braze": {"ns": ...}}} -> {"braze": {"ns": ...}}
        en_inner = next(iter(en_data.values())) if en_data else {}
        lang_inner = next(iter(lang_data.values())) if lang_data else {}

        en_leaves = _flatten_keys(en_inner)
        lang_leaves = _flatten_keys(lang_inner)

        for key, en_val in en_leaves.items():
            lang_val = lang_leaves.get(key)
            if lang_val and isinstance(en_val, str) and isinstance(lang_val, str):
                pairs[en_val] = lang_val

    return pairs


def _flatten_keys(obj, prefix=""):
    """Flatten nested dict to {dotted.key: leaf_value}."""
    result = {}
    for k, v in obj.items():
        full = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(_flatten_keys(v, full))
        else:
            result[full] = v
    return result


def parse_android_sdk(repo_path, locale_dir):
    """Parse Android strings.xml. Returns {english: translation}."""
    res = Path(repo_path) / "android-sdk-ui" / "src" / "main" / "res"
    en_file = res / "values" / "strings.xml"
    lang_file = res / locale_dir / "strings.xml"
    if not en_file.exists() or not lang_file.exists():
        return {}

    en_strings = _parse_android_strings(en_file)
    lang_strings = _parse_android_strings(lang_file)

    return {
        en_strings[k]: lang_strings[k]
        for k in en_strings
        if k in lang_strings
    }


def _parse_android_strings(path):
    """Parse Android strings.xml into {name: value}."""
    try:
        tree = ET.parse(path)
    except ET.ParseError:
        return {}
    result = {}
    for elem in tree.findall(".//string"):
        name = elem.get("name", "")
        if elem.get("translatable") == "false":
            continue
        text = elem.text or ""
        result[name] = text.replace("\\n", "\n")
    return result


def parse_swift_sdk(repo_path, locale):
    """Parse Swift SDK .strings files. Returns {english: translation}."""
    base = Path(repo_path) / "Sources" / "BrazeUI" / "Resources" / "Localization"
    en_dir = base / "en.lproj"
    lang_dir = base / f"{locale}.lproj"
    if not en_dir.is_dir() or not lang_dir.is_dir():
        return {}

    pairs = {}
    for en_file in en_dir.glob("*.strings"):
        lang_file = lang_dir / en_file.name
        if not lang_file.exists():
            continue
        en_strings = _parse_dot_strings(en_file)
        lang_strings = _parse_dot_strings(lang_file)
        for k in en_strings:
            if k in lang_strings:
                pairs[en_strings[k]] = lang_strings[k]
    return pairs


def _parse_dot_strings(path):
    """Parse Apple .strings file into {key: value}."""
    result = {}
    for line in path.read_text(errors="replace").splitlines():
        m = re.match(r'^"(.+?)"\s*=\s*"(.+?)"\s*;', line)
        if m:
            result[m.group(1)] = m.group(2)
    return result


def parse_grapesjs(repo_path, locale):
    """Parse GrapesJS JS locale file. Returns {english: translation}."""
    if locale is None:
        return {}
    base = Path(repo_path) / "src" / "i18n" / "locale"
    en_file = base / "en.js"
    lang_file = base / f"{locale}.js"
    if not en_file.exists() or not lang_file.exists():
        return {}

    en_strings = _parse_grapesjs_strings(en_file)
    lang_strings = _parse_grapesjs_strings(lang_file)

    return {
        en_strings[k]: lang_strings[k]
        for k in en_strings
        if k in lang_strings
    }


def _parse_grapesjs_strings(path):
    """Extract key-value string assignments from a GrapesJS locale JS file."""
    result = {}
    text = path.read_text(errors="replace")
    for m in re.finditer(r"(\w+)\s*:\s*['\"](.+?)['\"]", text):
        result[m.group(1)] = m.group(2)
    return result


# ---------------------------------------------------------------------------
# Comparison engine
# ---------------------------------------------------------------------------

def _bounded_substring_match(key_lower: str, haystack_lower: str) -> bool:
    """True if key_lower appears in haystack_lower as a whole token/phrase.

    Uses non-alphanumeric boundaries on both sides (or string start/end) so
    naive substring traps are avoided, e.g. \"connect\" inside \"connection\",
    \"review\" inside \"preview\", \"log\" inside \"changelog\".
    English locale keys are ASCII-heavy; this deliberately does not use \\b so
    hyphen and apostrophe boundaries still work (e.g. \"user\" in \"user's\").
    """
    if not key_lower or not haystack_lower:
        return False
    escaped = re.escape(key_lower)
    pattern = re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])")
    return bool(pattern.search(haystack_lower))


def find_mismatches(
    glossary, source_pairs, source_name, include_substring_mismatches=False
):
    """Compare glossary entries against source localization pairs.

    For each glossary English term, look for exact matches in the source
    English strings. When ``include_substring_mismatches`` is true (CLI:
    ``--include-substring-mismatches``), also report short source strings where
    the term appears with different translations; those rows are not
    auto-fixed. Substring detection requires the glossary key to appear as a
    whole word/phrase (non-alphanumeric boundaries), so letter-only overlaps
    like "connect" in "connection" or "review" in "preview" are not flagged.

    Returns list of mismatch dicts.
    """
    mismatches = []
    source_en_lower = {k.lower(): k for k in source_pairs}

    for gloss_en, gloss_trans in glossary.items():
        gloss_en_lower = gloss_en.lower()

        # 1) Exact match (case-insensitive on English, case-sensitive on translation)
        if gloss_en_lower in source_en_lower:
            original_key = source_en_lower[gloss_en_lower]
            source_trans = source_pairs[original_key]
            if not _translations_match(gloss_trans, source_trans):
                mismatches.append({
                    "term": gloss_en,
                    "match_type": "exact",
                    "glossary_value": gloss_trans,
                    "source_value": source_trans,
                    "source": source_name,
                })
            continue

        if not include_substring_mismatches:
            continue

        # Substring: only for short source strings that are close variants
        # (at most ~2x the glossary term length to avoid sentence matches).
        # Require whole-token boundaries so we do not flag "Connect" vs
        # "Connection Error" or "Review" vs "Preview".
        if len(gloss_en) < 4:
            continue
        max_src_len = max(len(gloss_en) * 2.5, len(gloss_en) + 15)
        for src_en, src_trans in source_pairs.items():
            if len(src_en) > max_src_len:
                continue
            src_lower = src_en.lower()
            if src_lower != gloss_en_lower and _bounded_substring_match(
                gloss_en_lower, src_lower
            ):
                if not _translations_match(gloss_trans, src_trans):
                    mismatches.append({
                        "term": gloss_en,
                        "match_type": "substring",
                        "glossary_value": gloss_trans,
                        "source_value": src_trans,
                        "source_english": src_en,
                        "source": source_name,
                    })
                    break

    return mismatches


def _translations_match(glossary_val, source_val):
    """Check if a glossary translation is consistent with the source.

    Handles glossaries that list alternatives with 'or' (e.g. "放棄カート or カート放棄").
    Also does substring and case-insensitive checks since UI context may
    capitalize differently than docs prose.
    """
    gv = glossary_val.strip()
    sv = source_val.strip()
    if gv.lower() == sv.lower():
        return True
    alternatives = [a.strip() for a in re.split(r'\s+or\s+', gv)]
    for alt in alternatives:
        if alt.lower() == sv.lower() or alt.lower() in sv.lower() or sv.lower() in alt.lower():
            return True
    if gv.lower() in sv.lower() or sv.lower() in gv.lower():
        return True
    return False


def _is_ascii_only(s):
    """True if string has no code points above 127 (no CJK, accents, etc.)."""
    if not s:
        return True
    return all(ord(c) < 128 for c in s)


def _has_non_ascii(s):
    """True if the glossary/translation uses any character outside basic ASCII."""
    return any(ord(c) >= 128 for c in (s or ""))


def should_skip_ascii_downgrade(glossary_value, source_value):
    """Avoid overwriting a localized glossary entry with ASCII-only source text.

    Source repos sometimes ship English (or mixed) strings in non-English locale
    files. The audit would otherwise \"fix\" the glossary to match that
    English, de-localizing Korean/Japanese/etc. glossaries.

    Note: Translations written only with ASCII Latin letters (e.g. Spanish
    \"clic\") are not protected by this check.
    """
    if not source_value or glossary_value == source_value:
        return False
    return _has_non_ascii(glossary_value) and _is_ascii_only(source_value)


COMMON_WORDS = frozenset({
    "a", "an", "the", "is", "it", "in", "on", "or", "and", "to", "of", "for",
    "by", "at", "as", "if", "no", "not", "but", "so", "do", "be", "we", "he",
    "me", "my", "up", "go", "am", "us", "all", "new", "one", "two", "get",
    "set", "can", "use", "add", "see", "try", "run", "end", "has", "had",
    "did", "was", "are", "may", "its", "our", "out", "off", "you", "yes",
    "with", "from", "that", "this", "will", "have", "been", "they", "them",
    "then", "than", "when", "what", "some", "more", "also", "only", "just",
    "back", "here", "each", "like", "make", "your", "into", "over", "such",
    "done", "true", "false", "none", "null", "save", "edit", "copy", "date",
    "time", "name", "type", "data", "sent", "open", "next", "last", "show",
    "hide", "note", "test", "text", "link", "file", "list", "view", "size",
    "both", "same", "live", "line",
})


def find_missing_terms(source_pairs, glossary, docs_path, min_occurrences=5):
    """Find source terms that appear in docs but aren't in the glossary.

    Filters aggressively to surface only genuinely useful terminology:
    - 6+ characters or multi-word (contains a space)
    - Not a common English word
    - Appears at least min_occurrences times in docs
    """
    glossary_lower = {k.lower() for k in glossary}
    candidates = {}

    for en_val, trans_val in source_pairs.items():
        if len(en_val) > 50:
            continue
        if en_val.lower() in glossary_lower:
            continue
        if re.match(r'^[\d\s{}\-_.]+$', en_val):
            continue
        if en_val.lower() in COMMON_WORDS:
            continue
        has_space = " " in en_val.strip()
        if not has_space and len(en_val) < 6:
            continue
        if en_val == trans_val:
            continue
        candidates[en_val] = trans_val

    if not candidates:
        return []

    docs_content = _load_docs_content(docs_path)
    docs_lower = docs_content.lower()

    missing = []
    for en_val, trans_val in candidates.items():
        count = docs_lower.count(en_val.lower())
        if count >= min_occurrences:
            missing.append({
                "term": en_val,
                "source_translation": trans_val,
                "frequency_in_docs": count,
            })

    missing.sort(key=lambda x: -x["frequency_in_docs"])
    return missing[:200]


_docs_cache = {}

def _load_docs_content(docs_path):
    """Load and cache all English docs content as one big string."""
    key = str(docs_path)
    if key in _docs_cache:
        return _docs_cache[key]

    parts = []
    for md in Path(docs_path).rglob("*.md"):
        try:
            parts.append(md.read_text(errors="replace"))
        except OSError:
            pass
    content = "\n".join(parts)
    _docs_cache[key] = content
    return content


# ---------------------------------------------------------------------------
# Auto-fix
# ---------------------------------------------------------------------------

def apply_fixes(report):
    """Apply audit fixes to glossary files on disk.

    - Exact mismatches: update glossary value to match the source.
    - Exact mismatches that would replace a non-ASCII glossary value with an
      ASCII-only source value are skipped (avoids de-localization from
      incomplete third-party locale files).
    - Missing terms: add new entries with the source translation.
    - Substring mismatches are skipped (ambiguous, need human judgment).

    Returns {"fixes_applied": N, "terms_added": M, "fixes_skipped_downgrade": K,
             "skipped_downgrade_details": [...], "details": {...},
             "locale_changes": [...]}.
    """
    total_fixed = 0
    total_added = 0
    total_skipped_downgrade = 0
    skipped_downgrade_details = []
    details = {}
    locale_changes = []

    for lang_key, lang_data in sorted(report["languages"].items()):
        glossary_path = GLOSSARY_DIR / f"{lang_key}.json"
        if not glossary_path.exists():
            continue

        glossary = json.loads(glossary_path.read_text("utf-8"))
        lang_fixed = 0
        lang_added = 0
        lang_skipped_downgrade = 0

        exact = [m for m in lang_data.get("mismatches", [])
                 if m["match_type"] == "exact"]

        mismatches_by_term = {}
        for m in exact:
            mismatches_by_term.setdefault(m["term"], []).append(m)
        for term, term_mismatches in mismatches_by_term.items():
            if term not in glossary:
                continue
            # Never let an upstream dashboard/SDK translation override a
            # protected Braze product term (e.g. 'Segment' → 'Segmento
            # faturável', 'Canvas' → 'キャンバス'). These would silently
            # re-introduce the glossary drift that translation_prompt.md
            # specifically forbids.
            protected = _protected_value(term, lang_key)
            if protected is not None and glossary[term] == protected:
                print(
                    f"  {lang_key}: skipping '{term}' — protected product "
                    f"term; translation_prompt requires English."
                )
                continue
            source_values = {m["source_value"] for m in term_mismatches}
            if len(source_values) == 1:
                new_val = term_mismatches[0]["source_value"]
                old_val = glossary[term]
                if should_skip_ascii_downgrade(old_val, new_val):
                    lang_skipped_downgrade += 1
                    src = term_mismatches[0].get("source", "")
                    print(
                        f"  {lang_key}: skipping '{term}' — would downgrade "
                        f"localized glossary to ASCII-only source ({new_val!r})"
                    )
                    skipped_downgrade_details.append({
                        "lang": lang_key,
                        "term": term,
                        "glossary_value": old_val,
                        "source_value": new_val,
                        "source": src,
                    })
                    continue
                glossary[term] = new_val
                lang_fixed += 1
                if old_val != new_val:
                    locale_changes.append({
                        "lang": lang_key,
                        "term": term,
                        "kind": "updated",
                        "search": old_val,
                        "replace": new_val,
                    })
            else:
                print(f"  {lang_key}: skipping '{term}' — conflicting sources: {source_values}")

        glossary_lower = {k.lower() for k in glossary}
        for m in lang_data.get("missing", []):
            term = m["term"]
            if term.lower() not in glossary_lower:
                # Protected product terms always land as their English
                # canonical, regardless of what the upstream source says.
                protected = _protected_value(term, lang_key)
                new_val = (
                    protected if protected is not None else m["source_translation"]
                )
                glossary[term] = new_val
                glossary_lower.add(term.lower())
                lang_added += 1
                if term != new_val:
                    locale_changes.append({
                        "lang": lang_key,
                        "term": term,
                        "kind": "added",
                        "search": term,
                        "replace": new_val,
                    })

        if lang_fixed or lang_added:
            sorted_glossary = {k: glossary[k] for k in sorted(glossary, key=str.lower)}
            glossary_path.write_text(
                json.dumps(sorted_glossary, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"  {lang_key}: {lang_fixed} fixed, {lang_added} added")

        total_fixed += lang_fixed
        total_added += lang_added
        total_skipped_downgrade += lang_skipped_downgrade
        details[lang_key] = {
            "fixed": lang_fixed,
            "added": lang_added,
            "skipped_downgrade": lang_skipped_downgrade,
        }

    return {
        "fixes_applied": total_fixed,
        "terms_added": total_added,
        "fixes_skipped_downgrade": total_skipped_downgrade,
        "skipped_downgrade_details": skipped_downgrade_details,
        "details": details,
        "locale_changes": locale_changes,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_markdown_report(report, fix_results=None, locale_results=None):
    """Generate a markdown summary from the audit report.

    When fix_results is provided, the report is formatted as a PR body
    showing what was fixed, what was added, and what was skipped.
    """
    fixed_mode = fix_results is not None
    lines = ["## Glossary audit summary\n"] if fixed_mode else ["# Glossary Audit Report\n"]

    stats = report["stats"]

    if fixed_mode:
        lines.append(f"**Fixes applied:** {fix_results['fixes_applied']}")
        lines.append(f"**Terms added:** {fix_results['terms_added']}")
        sk = fix_results.get("fixes_skipped_downgrade", 0)
        if sk:
            lines.append(
                f"**Fixes skipped (de-localization guard):** {sk}"
            )
        if locale_results:
            lines.append(
                f"**Locale docs updated:** {locale_results['files_changed']} files, "
                f"{locale_results['replacements']} replacements"
            )
        lines.append(f"**Languages audited:** {stats['languages_audited']}")
        lines.append(f"**Source strings scanned:** {stats['total_source_strings']}")
    else:
        lines.append(f"**Languages audited:** {stats['languages_audited']}")
        lines.append(f"**Glossary entries checked:** {stats['total_glossary_entries']}")
        lines.append(f"**Source strings scanned:** {stats['total_source_strings']}")
        lines.append(f"**Mismatches found:** {stats['total_mismatches']}")
        lines.append(f"**Missing high-value terms:** {stats['total_missing']}")
    lines.append("")

    for lang_key, lang_data in sorted(report["languages"].items()):
        mismatches = lang_data.get("mismatches", [])
        missing = lang_data.get("missing", [])
        if not mismatches and not missing:
            continue

        exact = [m for m in mismatches if m["match_type"] == "exact"]
        substr = [m for m in mismatches if m["match_type"] == "substring"]

        lines.append(f"### {lang_key}\n")

        if exact:
            header = "Fixed — exact mismatches" if fixed_mode else "Exact mismatches"
            lines.append(f"**{header}**\n")
            lines.append("| Term | Old value | New value (source) | Source repo |")
            lines.append("|------|-----------|-------------------|-------------|")
            for m in exact:
                lines.append(
                    f"| {m['term']} | {m['glossary_value']} "
                    f"| {m['source_value']} | {m['source']} |"
                )
            lines.append("")

        if missing:
            header = "Added — new terms" if fixed_mode else "Missing terms (appear in docs but not in glossary)"
            lines.append(f"**{header}**\n")
            lines.append("| Term | Translation | Docs occurrences |")
            lines.append("|------|-------------|-----------------|")
            for m in missing[:50]:
                lines.append(
                    f"| {m['term']} | {m['source_translation']} "
                    f"| {m['frequency_in_docs']} |"
                )
            if len(missing) > 50:
                lines.append(f"\n*...and {len(missing) - 50} more*\n")
            lines.append("")

        if substr:
            header = "Skipped — substring mismatches (needs human review)" if fixed_mode else "Substring mismatches"
            lines.append(f"**{header}**\n")
            lines.append(
                "These rows are **not** auto-fixed: the English UI string in a source repo "
                "is a *longer phrase* that merely **contains** the glossary’s English key, so "
                "the right translation is ambiguous.\n\n"
                "**Matching rule:** The audit only treats a hit as a substring when the "
                "glossary key appears as a **whole word or phrase** inside that longer "
                "English string (non-alphanumeric boundaries on both sides). That suppresses "
                "spurious overlaps such as **Connect** inside **Connection** or **Review** "
                "inside **Preview**, while still allowing cases like **Mobile** in "
                "**Mobile Landscape**.\n\n"
                "**How to read the table**\n\n"
                "| Column | Meaning |\n"
                "|--------|--------|\n"
                "| **Glossary key (English)** | The English string used as the key in that language’s glossary JSON under `scripts/glossaries/` (same term docs use as the UI reference). |\n"
                "| **Current glossary translation** | What the glossary maps that key to today in this language. |\n"
                "| **Source UI string (English)** | The **full** English string from the product/SDK locale file where the glossary key appears as a **whole word or phrase** (e.g. “Mobile Landscape” for key “Mobile”, or “Edit campaign” for key “Campaign”). |\n"
                "| **Source UI translation** | The localized string shipped with that **full** English source string. |\n"
                "| **Source repo** | Which repository that English/translation pair came from. |\n\n"
                "Use this to decide whether to align the glossary with the source, keep both "
                "intentionally different (different surfaces), or fix data upstream.\n"
            )
            lines.append(
                "| Glossary key (English) | Current glossary translation | "
                "Source UI string (English) | Source UI translation | Source repo |"
            )
            lines.append(
                "|--------------------------|------------------------------|"
                "------------------------------|-------------------------|-------------|"
            )
            for m in substr[:30]:
                lines.append(
                    f"| {m['term']} | {m['glossary_value']} "
                    f"| {m.get('source_english', '')} "
                    f"| {m['source_value']} | {m['source']} |"
                )
            if len(substr) > 30:
                lines.append(f"\n*...and {len(substr) - 30} more*\n")
            lines.append("")

    if fixed_mode and locale_results and locale_results.get("details"):
        lines.append("### Locale doc propagation\n")
        lines.append(
            "Glossary adds/updates were applied to matching prose in "
            "``_lang/`` (code fences, alert keys, glossary identifiers, and "
            "partner/UI literals are skipped).\n"
        )
        lines.append("| File | Replacements |")
        lines.append("|------|-------------|")
        for row in locale_results["details"][:40]:
            lines.append(f"| `{row['file']}` | {row['replacements']} |")
        if len(locale_results["details"]) > 40:
            lines.append(
                f"\n*...and {len(locale_results['details']) - 40} more files*\n"
            )
        lines.append("")

    if fixed_mode and fix_results.get("skipped_downgrade_details"):
        lines.append("### Skipped — de-localization guard\n")
        lines.append(
            "These exact mismatches were not applied: glossary had non-ASCII "
            "text but the source string was ASCII-only (usually English left "
            "in a locale file). Update the source repo or fix manually.\n"
        )
        lines.append("| Language | Term | Glossary (kept) | Source (not applied) | Source repo |")
        lines.append("|----------|------|-----------------|----------------------|-------------|")
        for row in fix_results["skipped_downgrade_details"]:
            lines.append(
                f"| {row['lang']} | {row['term']} | {row['glossary_value']} "
                f"| {row['source_value']} | {row.get('source', '')} |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_audit(args):
    docs_path = REPO_ROOT / "_docs"

    # Resolve repo paths -- default to sibling directories of braze-docs
    parent = REPO_ROOT.parent
    platform_repo = Path(args.platform_repo or os.environ.get(
        "PLATFORM_REPO", str(parent / "platform")))
    android_repo = Path(args.android_repo or os.environ.get(
        "ANDROID_SDK_REPO", str(parent / "braze-android-sdk")))
    swift_repo = Path(args.swift_repo or os.environ.get(
        "SWIFT_SDK_REPO", str(parent / "braze-swift-sdk")))
    grapesjs_repo = Path(args.grapesjs_repo or os.environ.get(
        "GRAPESJS_REPO", str(parent / "grapesjs")))

    report = {"languages": {}, "stats": {}}
    total_mismatches = 0
    total_missing = 0
    total_glossary_entries = 0
    total_source_strings = 0
    include_substring = getattr(args, "include_substring_mismatches", False)

    for lang_key, mappings in LANG_MAP.items():
        glossary_path = GLOSSARY_DIR / f"{lang_key}.json"
        if not glossary_path.exists():
            print(f"  SKIP {lang_key}: no glossary file")
            continue

        glossary = json.loads(glossary_path.read_text())
        total_glossary_entries += len(glossary)

        print(f"\nAuditing {lang_key} ({len(glossary)} glossary entries)...")

        all_source_pairs = {}
        all_mismatches = []

        # Platform
        if platform_repo.is_dir():
            print(f"  Parsing platform ({mappings['platform']})...")
            pairs = parse_platform(platform_repo, mappings["platform"])
            print(f"    {len(pairs)} string pairs loaded")
            total_source_strings += len(pairs)
            all_source_pairs.update(pairs)
            mismatches = find_mismatches(
                glossary, pairs, "platform", include_substring
            )
            all_mismatches.extend(mismatches)
            if mismatches:
                print(f"    {len(mismatches)} mismatches found")
        else:
            print(f"  SKIP platform: {platform_repo} not found")

        # Android SDK
        if android_repo.is_dir():
            pairs = parse_android_sdk(android_repo, mappings["android"])
            total_source_strings += len(pairs)
            all_source_pairs.update(pairs)
            mismatches = find_mismatches(
                glossary, pairs, "android-sdk", include_substring
            )
            all_mismatches.extend(mismatches)
            if pairs:
                print(f"  Android SDK: {len(pairs)} pairs, {len(mismatches)} mismatches")

        # Swift SDK
        if swift_repo.is_dir():
            pairs = parse_swift_sdk(swift_repo, mappings["swift"])
            total_source_strings += len(pairs)
            all_source_pairs.update(pairs)
            mismatches = find_mismatches(
                glossary, pairs, "swift-sdk", include_substring
            )
            all_mismatches.extend(mismatches)
            if pairs:
                print(f"  Swift SDK: {len(pairs)} pairs, {len(mismatches)} mismatches")

        # GrapesJS
        if grapesjs_repo.is_dir() and mappings["grapesjs"]:
            pairs = parse_grapesjs(grapesjs_repo, mappings["grapesjs"])
            total_source_strings += len(pairs)
            all_source_pairs.update(pairs)
            mismatches = find_mismatches(
                glossary, pairs, "grapesjs", include_substring
            )
            all_mismatches.extend(mismatches)
            if pairs:
                print(f"  GrapesJS: {len(pairs)} pairs, {len(mismatches)} mismatches")

        # Missing terms (use the already-loaded source pairs)
        if all_source_pairs:
            print(f"  Scanning docs for missing high-value terms...")
            missing = find_missing_terms(all_source_pairs, glossary, docs_path)
            print(f"    {len(missing)} missing terms found")
        else:
            missing = []

        report["languages"][lang_key] = {
            "glossary_entries": len(glossary),
            "source_pairs": len(all_source_pairs),
            "mismatches": all_mismatches,
            "missing": missing,
        }
        total_mismatches += len(all_mismatches)
        total_missing += len(missing)

    report["stats"] = {
        "languages_audited": len(report["languages"]),
        "total_glossary_entries": total_glossary_entries,
        "total_source_strings": total_source_strings,
        "total_mismatches": total_mismatches,
        "total_missing": total_missing,
    }

    # Write JSON report
    output = Path(args.output)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nJSON report written to {output}")

    # Auto-fix if requested
    fix_results = None
    locale_results = None
    if getattr(args, "fix", False) and (total_mismatches > 0 or total_missing > 0):
        print("\nApplying fixes...")
        fix_results = apply_fixes(report)
        print(
            f"  Total: {fix_results['fixes_applied']} fixed, "
            f"{fix_results['terms_added']} added, "
            f"{fix_results.get('fixes_skipped_downgrade', 0)} skipped (de-localization)"
        )

        if (
            not getattr(args, "no_propagate_locales", False)
            and fix_results.get("locale_changes")
        ):
            print("\nPropagating glossary changes to _lang/ docs...")
            locale_results = propagate_glossary_changes(
                fix_results["locale_changes"],
                repo_root=REPO_ROOT,
            )
            print(
                f"  Locale docs: {locale_results['files_changed']} files, "
                f"{locale_results['replacements']} replacements"
            )

    # Write markdown report
    md_output = output.with_suffix(".md")
    md_output.write_text(
        generate_markdown_report(report, fix_results, locale_results)
    )
    print(f"Markdown report written to {md_output}")

    print(f"\nAudit complete:")
    print(f"  Languages:   {report['stats']['languages_audited']}")
    print(f"  Mismatches:  {total_mismatches}")
    print(f"  Missing:     {total_missing}")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as handle:
            handle.write(f"total_mismatches={total_mismatches}\n")
            handle.write(f"total_missing={total_missing}\n")

    if fix_results:
        total_changes = fix_results["fixes_applied"] + fix_results["terms_added"]
        locale_files = locale_results["files_changed"] if locale_results else 0
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as handle:
                handle.write(f"fixes_applied={fix_results['fixes_applied']}\n")
                handle.write(f"terms_added={fix_results['terms_added']}\n")
                handle.write(f"total_changes={total_changes}\n")
                handle.write(f"locale_files_changed={locale_files}\n")
        return 0

    # Report-only runs treat mismatches as findings, not a failed process (CI
    # must reach the create-pull-request step when drift exists).
    return 0


def main():
    parser = argparse.ArgumentParser(description="Audit glossaries against source repos")
    parser.add_argument("--platform-repo", help="Path to platform repo")
    parser.add_argument("--android-repo", help="Path to braze-android-sdk repo")
    parser.add_argument("--swift-repo", help="Path to braze-swift-sdk repo")
    parser.add_argument("--grapesjs-repo", help="Path to grapesjs repo")
    parser.add_argument("--fix", action="store_true",
                        help="Auto-fix glossaries and write a PR-ready summary")
    parser.add_argument(
        "--output", default="glossary_audit_report.json",
        help="Output path for the JSON report (default: glossary_audit_report.json)",
    )
    parser.add_argument(
        "--include-substring-mismatches",
        action="store_true",
        help=(
            "Report fuzzy substring mismatches (noisy; not auto-fixed). "
            "Default is exact mismatches only."
        ),
    )
    parser.add_argument(
        "--no-propagate-locales",
        action="store_true",
        help=(
            "With --fix, update glossaries only; do not search _lang/ docs "
            "for new or updated terms."
        ),
    )
    args = parser.parse_args()
    sys.exit(run_audit(args))


if __name__ == "__main__":
    main()
