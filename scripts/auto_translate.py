#!/usr/bin/env python3
"""
Auto-translate English Braze docs into all supported languages using Claude.

Usage:
    python auto_translate.py translate --changed-files changed_files.txt
    python auto_translate.py stale-english-sources
    python auto_translate.py qc
    python auto_translate.py check-aliases
    python auto_translate.py check-path-case-collisions
    python auto_translate.py align-heading-anchor-parity
    python auto_translate.py verify --max-attempts 3
    python auto_translate.py summary
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, Set

# Single source of truth for the Braze product-name allowlist; imported by
# ``scripts/audit_glossaries.py`` too so the runtime glossary override and
# the upstream-sync guard cannot drift apart (Copilot flagged the prior
# "keep in sync" duplication on PR #13303).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _glossary_protected_terms import PROTECTED_PRODUCT_TERMS  # noqa: E402

def _get_anthropic_client():
    """Lazy-import Anthropic so commands like qc/summary work without the SDK.

    The HTTP ``timeout`` bounds **every** HTTP operation (connect, read,
    write). Without it, a stalled ``client.messages.stream(...)`` socket
    blocks the whole workflow: run 24906077736 sat on the `Translate
    changed files` step for 87+ minutes (against a typical 9-35 min
    healthy runtime for the same-wave siblings) until it was manually
    cancelled, because the streaming response simply stopped sending
    chunks with no exception raised.

    With the timeout in place, a stalled stream raises after
    ``TRANSLATION_HTTP_TIMEOUT`` seconds of silence; ``call_claude``'s
    retry loop then reissues the request (default ``TRANSLATION_API_RETRIES``
    is 6). Worst-case per-task time scales with retries and timeout; the
    workflow's ``timeout-minutes`` gives a final wall-clock ceiling on top.
    """
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: Install the Anthropic SDK: pip install anthropic")
        sys.exit(1)
    timeout_seconds = float(os.environ.get("TRANSLATION_HTTP_TIMEOUT", "240"))
    return Anthropic(timeout=timeout_seconds)


LANGUAGES = {
    "fr":    {"config": "fr",    "dir": "fr_fr", "name": "French"},
    "ja":    {"config": "ja",    "dir": "ja",    "name": "Japanese"},
    "ko":    {"config": "ko",    "dir": "ko",    "name": "Korean"},
    "pt-br": {"config": "pt-br", "dir": "pt_br", "name": "Portuguese (Brazil)"},
    "es":    {"config": "es",    "dir": "es",    "name": "Spanish"},
    "de":    {"config": "de",    "dir": "de",    "name": "German"},
}


def languages_from_cli_arg(languages_arg):
    """Subset of ``LANGUAGES`` from ``--languages`` (comma-separated keys), or all.

    Keys must match ``LANGUAGES`` (e.g. ``fr``, ``pt-br``). Order follows the
    argument list.
    """
    if not languages_arg or not str(languages_arg).strip():
        return dict(LANGUAGES)
    keys = [k.strip() for k in str(languages_arg).split(",") if k.strip()]
    bad = [k for k in keys if k not in LANGUAGES]
    if bad:
        print(
            f"ERROR: Unknown language key(s): {bad}. Valid: {list(LANGUAGES.keys())}",
            file=sys.stderr,
        )
        sys.exit(2)
    return {k: LANGUAGES[k] for k in keys}


MODEL = os.environ.get("TRANSLATION_MODEL", "claude-opus-4-6")
MAX_TOKENS = int(os.environ.get("TRANSLATION_MAX_TOKENS", "128000"))
MAX_FILE_KB = int(os.environ.get("TRANSLATION_MAX_FILE_KB", "130"))
CHUNK_TARGET_KB = int(os.environ.get("TRANSLATION_CHUNK_KB", "50"))
# Table-heavy confidential pricing pages (~50KB+) are chunked even below
# MAX_FILE_KB — single-shot requests often trigger transient API 500s (June 2026).
FORCE_CHUNK_MIN_KB = int(os.environ.get("TRANSLATION_FORCE_CHUNK_MIN_KB", "40"))
_FORCE_CHUNK_PATH_PREFIXES = tuple(
    p.strip()
    for p in os.environ.get(
        "TRANSLATION_FORCE_CHUNK_PATH_PREFIXES",
        "_docs/_unlisted_docs/pricing/",
    ).split(",")
    if p.strip()
)
MAX_WORKERS = int(os.environ.get("TRANSLATION_WORKERS", "12"))
API_RETRIES = int(os.environ.get("TRANSLATION_API_RETRIES", "6"))
FAILED_PASS_RETRIES = int(os.environ.get("TRANSLATION_FAILED_PASS_RETRIES", "6"))
FAILED_PASS_ROUNDS = int(os.environ.get("TRANSLATION_FAILED_PASS_ROUNDS", "2"))
REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
RESULTS_FILE = REPO_ROOT / "translation_results.json"
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"
STYLEGUIDE_DIR = REPO_ROOT / "scripts" / "styleguides"
QC_RESULTS_FILE = REPO_ROOT / "qc_results.json"

# Paths under `_lang/` use folder names (`fr_fr`, `pt_br`) while glossary files
# and ``PROTECTED_PRODUCT_TERMS`` overrides use CLI keys (`fr`, `pt-br`). Map
# so ``load_glossary`` and glossary compliance checks apply the intended
# Canvases → Canvas Romance overrides (Copilot / locale-key drift vs PR #13303).
_LANG_DIR_TO_GLOSSARY_LANG = {"fr_fr": "fr", "pt_br": "pt-br"}

NON_TRANSLATABLE_FM_KEYS = frozenset({
    "page_order", "layout", "page_type", "channel", "platform", "tool",
    "link", "image", "permalink", "hidden", "noindex", "config_only",
    "search_rank", "page_layout", "hide_nav", "hide_toc",
})

BRAZE_PRODUCT_NAMES = [
    "Content Cards", "Content Blocks", "Push Stories", "In-App Messages",
    "REST API", "News Feed", "Canvases", "Canvas", "Currents", "Campaigns",
    "Campaign", "Segments", "Segment", "Braze", "Liquid", "SDK", "API",
]

def protected_term_for_locale(term, lang_key):
    """Canonical glossary value for a protected product term in ``lang_key``.

    Returns ``None`` when ``term`` is not in ``PROTECTED_PRODUCT_TERMS``.
    When it is protected, returns the locale-specific override if one
    exists (for example ``Canvases`` → ``Canvas`` in Romance locales),
    otherwise falls back to the English term itself.

    No exception is raised — ``.get(lang_key, term)`` defaults to
    ``term`` for locales without a specific override. The earlier
    docstring claimed a ``KeyError`` path that the implementation has
    never actually taken (Copilot flagged the mismatch on PR #13303).
    """
    if term not in PROTECTED_PRODUCT_TERMS:
        return None
    return PROTECTED_PRODUCT_TERMS[term].get(lang_key, term)


# Case-folded lookup so ``filter_glossary``-style case-insensitive hits
# can't inject a localized entry for a lowercase spelling of a protected
# term (Copilot flagged this gap on PR #13303: pre-fix glossaries still
# carried ``campaign``→``campaña``, ``segment``→``세그먼트``, etc.).
_PROTECTED_TERM_CANONICAL_BY_LOWER = {
    term.lower(): term for term in PROTECTED_PRODUCT_TERMS
}


def _canonical_protected_term(term):
    """Return the canonical-cased protected product term for any casing of
    ``term``, or ``None`` if ``term`` is not a protected product name."""
    return _PROTECTED_TERM_CANONICAL_BY_LOWER.get(term.lower())


NON_LATIN_LANGUAGES = frozenset({"ja", "ko"})

COMPLETENESS_MIN_RATIO = float(os.environ.get("QC_MIN_RATIO", "0.6"))
COMPLETENESS_MAX_RATIO = float(os.environ.get("QC_MAX_RATIO", "1.6"))
UNTRANSLATED_BLOCK_THRESHOLD = 200


def load_prompt():
    """Load the translation system prompt from scripts/translation_prompt.md."""
    return (REPO_ROOT / "scripts" / "translation_prompt.md").read_text()


def load_styleguide(lang_key):
    """Load the style guide for a language. Returns '' if not found."""
    sg_path = STYLEGUIDE_DIR / f"{_glossary_language_key(lang_key)}.md"
    if sg_path.exists():
        content = sg_path.read_text().strip()
        if content:
            return f"\n\n## Style guide for this language\n\n{content}"
    return ""


def _glossary_language_key(lang_key):
    """Map ``_lang/`` folder suffix (for example ``fr_fr``) to glossary file key."""
    return _LANG_DIR_TO_GLOSSARY_LANG.get(lang_key, lang_key)


def load_glossary(lang_key):
    """Load the terminology glossary for a language. Returns {} if not found.

    After loading, enforces the ``translation_prompt.md`` "Braze product
    terminology" rule by **removing every case-insensitive variant** of a
    protected term from the raw glossary, then injecting exactly one
    canonical entry (English-cased key → locale override or English value).

    The case-fold step matters because ``filter_glossary`` matches the
    English term against file text case-insensitively (``en.lower() in
    text_lower``). Copilot flagged on PR #13303 that the prior
    implementation only overwrote the exact-cased key, so a glossary
    like ``"campaign" -> "campaña"`` or ``"segment" -> "세그먼트"`` still
    slipped through and contradicted the "keep product terms in English"
    rule. Stripping every case-variant up-front closes the loophole: the
    canonical ``"Campaign"`` / ``"Segment"`` entries we then inject are
    the only protected-term rows the LLM sees.
    """
    file_key = _glossary_language_key(lang_key)
    glossary_path = GLOSSARY_DIR / f"{file_key}.json"
    raw = (
        json.loads(glossary_path.read_text())
        if glossary_path.exists()
        else {}
    )
    for key in list(raw):
        if _canonical_protected_term(key) is not None:
            del raw[key]
    for term in PROTECTED_PRODUCT_TERMS:
        raw[term] = protected_term_for_locale(term, file_key)
    return raw


def filter_glossary(glossary, text, max_terms=200):
    """Return only glossary entries whose English term appears in the text.

    Case-insensitive matching. Capped at max_terms to keep prompt size
    reasonable — prioritizes longer (more specific) terms first.
    """
    text_lower = text.lower()
    matches = {
        en: target
        for en, target in glossary.items()
        if en.lower() in text_lower
    }
    if len(matches) <= max_terms:
        return matches
    sorted_by_specificity = sorted(matches.items(), key=lambda x: -len(x[0]))
    return dict(sorted_by_specificity[:max_terms])


def format_glossary_for_prompt(glossary):
    """Format filtered glossary as a markdown table for the prompt."""
    if not glossary:
        return ""
    lines = [
        "\n## Approved terminology for this file\n",
        "Use these approved translations. If an English term maps to itself, keep it in English.\n",
        "| English | Translation |",
        "|---------|-------------|",
    ]
    for en, target in sorted(glossary.items(), key=lambda x: x[0].lower()):
        lines.append(f"| {en} | {target} |")
    return "\n".join(lines)


def strip_code_fences(text):
    """Strip wrapping code fences if the model adds them despite instructions."""
    stripped = text.strip()
    match = re.match(r"^```(?:\w*)\s*\n(.*)\n```\s*$", stripped, re.DOTALL)
    return match.group(1) if match else stripped


_LIQUID_TAG_RE = re.compile(r"\{%[-\s]*(.*?)[-\s]*%\}", re.DOTALL)
_RAW_BLOCK_RE = re.compile(
    r"\{%[-\s]*raw[-\s]*%\}.*?\{%[-\s]*endraw[-\s]*%\}",
    re.DOTALL | re.IGNORECASE,
)
_LIQUID_BLOCK_PAIRS = {
    "api": "endapi",
    "details": "enddetails",
    "tabs": "endtabs",
    "tab": "endtab",
    "sdktabs": "endsdktabs",
    "sdktab": "endsdktab",
    "alert": "endalert",
    "apitags": "endapitags",
    "capture": "endcapture",
    "if": "endif",
    "unless": "endunless",
    "for": "endfor",
}
_LIQUID_CLOSE_TO_OPEN = {close: open_ for open_, close in _LIQUID_BLOCK_PAIRS.items()}
_LIQUID_PAIRED_TAGS_FOR_QC = tuple(_LIQUID_BLOCK_PAIRS.items())


def _liquid_tag_token(inner):
    """Return ('open', name), ('close', name), or (None, None) for a Liquid tag body."""
    parts = inner.strip().split()
    if not parts:
        return None, None
    name = parts[0]
    if name in _LIQUID_CLOSE_TO_OPEN:
        return "close", _LIQUID_CLOSE_TO_OPEN[name]
    if name in _LIQUID_BLOCK_PAIRS:
        return "open", name
    return None, None


def _raw_block_spans(content):
    """Return (start, end) spans for each ``{% raw %}...{% endraw %}`` region."""
    return [(m.start(), m.end()) for m in _RAW_BLOCK_RE.finditer(content)]


def _inside_raw_block(spans, position):
    return any(start <= position < end for start, end in spans)


def _liquid_content_for_qc(content):
    """Return *content* with ``{% raw %}`` regions removed for Liquid QC."""
    return _RAW_BLOCK_RE.sub("", content)


def _liquid_block_stack_at(content, position):
    """Return open Liquid block tag names at *position* in *content*."""
    raw_spans = _raw_block_spans(content)
    stack = []
    for match in _LIQUID_TAG_RE.finditer(content[:position]):
        if _inside_raw_block(raw_spans, match.start()):
            continue
        kind, name = _liquid_tag_token(match.group(1))
        if kind == "open":
            stack.append(name)
        elif kind == "close" and stack and stack[-1] == name:
            stack.pop()
    return stack


def _liquid_safe_split_offsets(content):
    """Byte offsets where a chunk boundary will not split an open Liquid block."""
    raw_spans = _raw_block_spans(content)
    offsets = [0]
    stack = []
    for match in _LIQUID_TAG_RE.finditer(content):
        if _inside_raw_block(raw_spans, match.start()):
            continue
        kind, name = _liquid_tag_token(match.group(1))
        if kind == "open":
            stack.append(name)
        elif kind == "close" and stack and stack[-1] == name:
            stack.pop()
        if not stack:
            offsets.append(match.end())
    if offsets[-1] != len(content):
        offsets.append(len(content))
    return sorted(set(offsets))


def _count_liquid_tag(content, tag_name):
    countable = _liquid_content_for_qc(content)
    return len(re.findall(rf"\{{%[-\s]*{re.escape(tag_name)}\b", countable))


def validate_liquid_paired_tags(content, label="translation"):
    """Raise ValueError when paired Liquid block tags are unbalanced."""
    problems = []
    for open_tag, close_tag in _LIQUID_PAIRED_TAGS_FOR_QC:
        open_count = _count_liquid_tag(content, open_tag)
        close_count = _count_liquid_tag(content, close_tag)
        if open_count != close_count:
            problems.append(f"{open_tag}={open_count} {close_tag}={close_count}")
    if problems:
        raise ValueError(
            f"Liquid paired-tag imbalance in {label}: " + ", ".join(problems)
        )


def _liquid_tag_line_pattern(tag_name):
    return re.compile(
        rf"(?m)^[ \t]*\{{%[-\s]*{re.escape(tag_name)}\b[^%]*%\}}[ \t]*(?:\n|\Z)"
    )


def _unmatched_open_tag_matches(content, open_tag, close_tag):
    """Return open-tag line matches that remain unmatched at end of *content*."""
    raw_spans = _raw_block_spans(content)
    events = []
    for match in _liquid_tag_line_pattern(open_tag).finditer(content):
        if not _inside_raw_block(raw_spans, match.start()):
            events.append((match.start(), 0, match))
    for match in _liquid_tag_line_pattern(close_tag).finditer(content):
        if not _inside_raw_block(raw_spans, match.start()):
            events.append((match.start(), 1, match))
    events.sort(key=lambda item: (item[0], item[1]))
    stack = []
    for _, kind, match in events:
        if kind == 0:
            stack.append(match)
        elif stack:
            stack.pop()
    return stack


def _remove_one_liquid_tag_line(
    content,
    tag_name,
    *,
    prefer_last=False,
    skip_first=False,
    preserve_first_n=0,
):
    """Remove one standalone ``{% tag %}`` line from *content*.

    ``preserve_first_n`` keeps the first N matches (use the English open-count
    when dropping extras). ``skip_first=True`` is ``preserve_first_n=1``.
    """
    if skip_first:
        preserve_first_n = max(preserve_first_n, 1)
    raw_spans = _raw_block_spans(content)
    matches = [
        match
        for match in _liquid_tag_line_pattern(tag_name).finditer(content)
        if not _inside_raw_block(raw_spans, match.start())
    ]
    if not matches:
        raise ValueError(f"No standalone {{% {tag_name} %}} line found")
    if preserve_first_n < 0:
        raise ValueError("preserve_first_n must be >= 0")
    if len(matches) <= preserve_first_n:
        raise ValueError(
            f"Only {len(matches)} {{% {tag_name} %}} line(s); "
            f"cannot preserve first {preserve_first_n}"
        )
    pool = matches[preserve_first_n:]
    match = pool[-1] if prefer_last else pool[0]
    return content[: match.start()] + content[match.end() :]


def _remove_one_extra_liquid_open_tag(content, open_tag, close_tag, *, preserve_first_n=0):
    """Remove one excess ``{% open %}`` line, preferring unmatched opens.

    Prefer the last open that is still on the Liquid stack at EOF so a spurious
    tag between two complete blocks is removed instead of a legitimate trailing
    open (Bugbot: skip_first only protecting match[0] when en_open > 1).
    Fall back to preserving the first ``preserve_first_n`` opens and dropping
    the last remaining match.
    """
    unmatched = _unmatched_open_tag_matches(content, open_tag, close_tag)
    if unmatched:
        match = unmatched[-1]
        return content[: match.start()] + content[match.end() :]
    return _remove_one_liquid_tag_line(
        content,
        open_tag,
        prefer_last=True,
        preserve_first_n=preserve_first_n,
    )


def repair_liquid_paired_tags_from_english(
    english_content, translated_content, label="translation"
):
    """Align paired Liquid tag counts with balanced English when a chunk drifts."""
    for open_tag, close_tag in _LIQUID_PAIRED_TAGS_FOR_QC:
        en_open = _count_liquid_tag(english_content, open_tag)
        en_close = _count_liquid_tag(english_content, close_tag)
        if en_open != en_close:
            raise ValueError(
                f"English reference unbalanced ({open_tag}/{close_tag}) in {label}"
            )

        tr_open = _count_liquid_tag(translated_content, open_tag)
        tr_close = _count_liquid_tag(translated_content, close_tag)

        while tr_open > en_open:
            translated_content = _remove_one_extra_liquid_open_tag(
                translated_content,
                open_tag,
                close_tag,
                preserve_first_n=en_open,
            )
            tr_open -= 1

        while tr_open > tr_close:
            translated_content = (
                translated_content.rstrip() + f"\n\n{{% {close_tag} %}}\n"
            )
            tr_close += 1

        while tr_close > en_close:
            translated_content = _remove_one_liquid_tag_line(
                translated_content,
                close_tag,
                prefer_last=True,
            )
            tr_close -= 1

    validate_liquid_paired_tags(translated_content, label=label)
    open_blocks = _liquid_block_stack_at(translated_content, len(translated_content))
    if open_blocks:
        raise ValueError(
            f"Liquid block still open at end of {label}: {open_blocks}"
        )
    return translated_content


def _validate_or_repair_chunk_liquid(en_chunk, translated, chunk_label):
    """Validate chunk Liquid; repair from English when counts drift."""
    try:
        validate_liquid_paired_tags(translated, label=chunk_label)
    except ValueError:
        translated = repair_liquid_paired_tags_from_english(
            en_chunk, translated, label=chunk_label
        )
    open_blocks = _liquid_block_stack_at(translated, len(translated))
    if open_blocks:
        raise ValueError(
            f"Liquid block still open at end of {chunk_label}: {open_blocks}"
        )
    return translated


def split_into_chunks(content, max_chunk_kb=None):
    """Split a large Markdown file into translatable chunks.

    Boundaries are chosen only where no Liquid block tag remains open, so
    ``{% details %}`` / ``{% api %}`` regions are never cut in half.  When
    possible, groups consecutive safe segments up to *max_chunk_kb* each.
    """
    if max_chunk_kb is None:
        max_chunk_kb = CHUNK_TARGET_KB
    max_bytes = max_chunk_kb * 1024

    safe_offsets = _liquid_safe_split_offsets(content)
    if len(safe_offsets) <= 2:
        lines = content.split("\n")
        target_lines = max(200, len(lines) // ((len(content) // max_bytes) + 1))
        chunks = []
        for i in range(0, len(lines), target_lines):
            chunk = "\n".join(lines[i:i + target_lines])
            start = sum(len(l) + 1 for l in lines[:i])
            if _liquid_block_stack_at(content, start + len(chunk)):
                raise ValueError(
                    "Line-based chunk split would break an open Liquid block"
                )
            chunks.append(chunk)
        return chunks

    segments = [
        content[safe_offsets[i]:safe_offsets[i + 1]]
        for i in range(len(safe_offsets) - 1)
    ]

    chunks = []
    current_chunk = ""
    for segment in segments:
        if (
            current_chunk
            and len((current_chunk + segment).encode()) > max_bytes
        ):
            chunks.append(current_chunk)
            current_chunk = segment
        else:
            current_chunk += segment

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def _extract_heading_anchor(heading_line):
    """Extract the {#anchor-id} from an H2 heading line, if present."""
    m = re.search(r'\{#([^}]+)\}', heading_line)
    return m.group(1) if m else None


def match_existing_chunks(english_chunks, existing_translation):
    """Given English chunks and a full existing translation, return a list of
    corresponding translation chunks (one per English chunk) by matching on
    heading anchor IDs (``{#id}``).  Falls back to heading text when anchors
    are absent.  Returns empty strings for unmatched chunks.
    """
    if not existing_translation:
        return [""] * len(english_chunks)

    tr_parts = re.split(r'(?=\n## )', existing_translation)

    tr_by_anchor = {}
    tr_by_text = {}
    for part in tr_parts:
        m = re.search(r"(?m)^## (.+)", part)
        if m:
            heading = m.group(1).strip()
            anchor = _extract_heading_anchor(heading)
            if anchor:
                tr_by_anchor[anchor] = part
            tr_by_text[heading] = part

    result = []
    for chunk in english_chunks:
        headings = re.findall(r'^## (.+)', chunk, re.MULTILINE)
        matched_parts = []
        for h in headings:
            h_stripped = h.strip()
            anchor = _extract_heading_anchor(h_stripped)
            if anchor and anchor in tr_by_anchor:
                matched_parts.append(tr_by_anchor[anchor])
            elif h_stripped in tr_by_text:
                matched_parts.append(tr_by_text[h_stripped])
        if matched_parts:
            result.append("".join(matched_parts))
        elif not headings:
            result.append(tr_parts[0] if tr_parts else "")
        else:
            result.append("")

    return result


_H2_HEADING_RE = re.compile(r"(?m)^## ")


def split_into_h2_chunks(content):
    """Split markdown at top-level H2 headings without merging segments.

    Boundaries are skipped inside open Liquid blocks so ``##`` lines within
    ``{% details %}`` / ``{% api %}`` regions stay with their parent section.
    """
    offsets = [0]
    for match in _H2_HEADING_RE.finditer(content):
        pos = match.start()
        if pos > 0 and not _liquid_block_stack_at(content, pos):
            offsets.append(pos)
    if len(offsets) == 1:
        return [content]
    offsets.append(len(content))
    return [
        content[offsets[i]: offsets[i + 1]]
        for i in range(len(offsets) - 1)
    ]


def _chunk_translation_key(chunk):
    """Stable key for an H2 chunk (anchor ID preferred, else heading text)."""
    headings = re.findall(r"^## (.+)", chunk, re.MULTILINE)
    if not headings:
        return "__preamble__"
    first = headings[0].strip()
    anchor = _extract_heading_anchor(first)
    if anchor:
        return f"#{anchor}"
    return first


def _normalize_chunk_for_diff(chunk):
    return chunk.strip().replace("\r\n", "\n")


def chunks_requiring_translation(en_chunks, prev_en_chunks):
    """Return a bool per *en_chunks* entry: True when re-translation is needed."""
    if not prev_en_chunks:
        return [True] * len(en_chunks)
    prev_by_key = {}
    for chunk in prev_en_chunks:
        prev_by_key[_chunk_translation_key(chunk)] = _normalize_chunk_for_diff(chunk)
    needs = []
    for chunk in en_chunks:
        key = _chunk_translation_key(chunk)
        prev = prev_by_key.get(key)
        if prev is None or prev != _normalize_chunk_for_diff(chunk):
            needs.append(True)
        else:
            needs.append(False)
    return needs


def _h2_chunk_keys(content):
    return [_chunk_translation_key(chunk) for chunk in split_into_h2_chunks(content)]


def incremental_h2_requires_full_file(english_content, previous_english_content):
    """Return True when incremental H2 reassembly is unsafe across sdktabs boundaries.

    When English gains or loses top-level H2 chunk boundaries inside ``{% sdktabs %}``,
    reusing unchanged locale chunks can leave translated ``sdktab`` structure broken.
    """
    if not previous_english_content:
        return False
    if "{% sdktabs" not in english_content and "{% sdktabs" not in previous_english_content:
        return False
    return _h2_chunk_keys(english_content) != _h2_chunk_keys(previous_english_content)


def load_english_at_git_ref(fpath, ref):
    """Return English file contents at git *ref*, or None if unavailable."""
    if not ref:
        return None
    try:
        result = subprocess.run(
            ["git", "show", f"{ref}:{fpath}"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            return None
        return result.stdout
    except (OSError, subprocess.SubprocessError):
        return None


def _resolve_english_base_ref(cli_ref=None):
    """CLI flag wins over TRANSLATION_ENGLISH_BASE_REF env (empty → disabled)."""
    if cli_ref:
        return cli_ref
    env_ref = os.environ.get("TRANSLATION_ENGLISH_BASE_REF", "").strip()
    return env_ref or None


def _build_system_blocks(system_prompt):
    """Wrap a system prompt for prompt caching.

    Accepts either a plain string (returned as-is for backward compat)
    or a list of (text, cacheable) tuples.  Cacheable blocks get an
    ``ephemeral`` cache_control marker so Anthropic can reuse them
    across calls within the same batch window (~5 min).
    """
    if isinstance(system_prompt, str):
        return system_prompt
    blocks = []
    for text, cacheable in system_prompt:
        block = {"type": "text", "text": text}
        if cacheable:
            block["cache_control"] = {"type": "ephemeral"}
        blocks.append(block)
    return blocks


_RETRYABLE_API_ERROR_TOKENS = (
    "overloaded",
    "timeout",
    "timed out",
    "rate limit",
    "rate_limit",
    "529",
    "502",
    "503",
    "504",
    "connection reset",
    "connection error",
    "connection aborted",
    "connection closed",
    "peer closed",
    "incomplete chunked",
    "chunked read",
    "broken pipe",
    "remote protocol",
    "server disconnected",
    "internal server error",
    "api_error",
)


def _uses_chunked_translation(fpath, size_kb):
    """Return True when a file should use chunked translation."""
    if size_kb > MAX_FILE_KB:
        return True
    if size_kb >= FORCE_CHUNK_MIN_KB:
        norm = fpath.replace("\\", "/")
        if any(norm.startswith(prefix) for prefix in _FORCE_CHUNK_PATH_PREFIXES):
            return True
    return False


class MaxTokensTruncatedError(RuntimeError):
    """Raised when Claude stops because the output hit max_tokens."""


def _is_max_tokens_truncation_error(exc):
    """Return True when a single-pass translation/review hit the output token cap."""
    if isinstance(exc, MaxTokensTruncatedError):
        return True
    msg = str(exc).lower()
    return "output truncated" in msg and "token limit" in msg


def _is_retryable_api_error(exc):
    """Return True when another Claude API attempt may succeed."""
    msg = str(exc).lower()
    return any(token in msg for token in _RETRYABLE_API_ERROR_TOKENS)


def _is_retryable_translation_error(error):
    """Return True when re-running the full translate pass may succeed."""
    msg = str(error)
    if _is_retryable_api_error(msg):
        return True
    # Chunked reassembly can drift {% api %}/{% endapi %} counts per locale;
    # a fresh pass often succeeds (same as manual workflow job re-runs).
    return "liquid paired-tag imbalance" in msg.lower()


def _api_retry_wait_seconds(exc, attempt):
    """Backoff delay before the next Claude API attempt."""
    wait = min(90, 2 ** (attempt + 1))
    msg = str(exc).lower()
    if "overloaded" in msg:
        wait = min(120, wait * 2)
    elif any(token in msg for token in ("peer closed", "incomplete chunked", "broken pipe")):
        wait = min(120, wait + 10)
    return wait


def call_claude(client, system_prompt, user_message, retries=None):
    """Call the Claude API via streaming with exponential-backoff retry."""
    if retries is None:
        retries = API_RETRIES
    system_blocks = _build_system_blocks(system_prompt)
    for attempt in range(retries):
        try:
            text_chunks = []
            stop_reason = None
            with client.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=0,
                system=system_blocks,
                messages=[{"role": "user", "content": user_message}],
            ) as stream:
                for text in stream.text_stream:
                    text_chunks.append(text)
                stop_reason = stream.get_final_message().stop_reason
            full_text = "".join(text_chunks)
        except Exception as exc:
            if attempt < retries - 1 and _is_retryable_api_error(exc):
                wait = _api_retry_wait_seconds(exc, attempt)
                print(f"    API error: {exc} — retrying in {wait}s...")
                time.sleep(wait)
                continue
            raise

        if stop_reason == "max_tokens":
            raise MaxTokensTruncatedError(
                f"Output truncated (hit {MAX_TOKENS} token limit). "
                "Increase TRANSLATION_MAX_TOKENS or use chunked translation."
            )
        return strip_code_fences(full_text)


def translate_file(
    client, prompt, english_content, existing_translation, language_name,
    extra_context="", api_retries=None,
):
    """Translate a single English file into the target language."""
    system = [(prompt, True)]
    if extra_context:
        system.append((extra_context, False))

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## English source (translate this)\n\n{english_content}\n\n"

    if existing_translation:
        user_msg += (
            "## Existing translation (use as reference for terminology consistency)\n\n"
            f"{existing_translation}\n"
        )
    else:
        user_msg += "## Existing translation\nNone — this is a new file. Translate from scratch.\n"

    return call_claude(client, system, user_msg, retries=api_retries)


def fix_file(client, prompt, translated_content, build_error, language_name):
    """Send a translated file back to Claude to fix Jekyll build errors."""
    fix_suffix = (
        "\n\n## ADDITIONAL CONTEXT: FIX MODE\n"
        "The file below failed the Jekyll build. Fix ONLY the structural or "
        "syntax issues that caused the failure. Preserve all translations. "
        "Return the complete fixed file and nothing else."
    )
    system = [(prompt, True), (fix_suffix, False)]

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## Translated file (has build errors)\n\n{translated_content}\n\n"
    user_msg += f"## Jekyll build error output\n```\n{build_error}\n```\n"

    return call_claude(client, system, user_msg)


REVIEW_PROMPT = """\
You are a senior translation reviewer for Braze technical documentation. \
Your job is to review a machine-translated file and improve its quality.

Compare the translation against the English source and fix any issues:

1. **Accuracy**: Correct any mistranslations or meaning shifts.
2. **Naturalness**: Rephrase anything that reads as awkward or overly literal. \
The translation should read as if originally written in the target language.
3. **Terminology**: Ensure glossary terms are used correctly. Braze product names \
(Canvas, Currents, Content Cards, etc.) must stay in English.
4. **Preservation**: Verify that Liquid tags, code blocks, URLs, front matter keys, \
HTML tags, and markdown formatting are intact and unmodified.
5. **Style guide**: Follow all rules in the language-specific style guide appended \
below (gender conventions, register, terminology preferences, etc.).
6. **Consistency**: Ensure consistent terminology and tone throughout the file.
7. **Navigation label parity**: For user-guide landing/overview docs (home, channels, \
get_started, messaging, analytics, onboarding_faq), keep locale-established card \
labels, headings, and common nouns aligned with the locale's linked pages; avoid \
introducing English variants where that locale already uses translated labels.
8. **Procedure UI labels**: In each numbered or bulleted procedure, bold \
dashboard controls must not mix English with localized forms—localize every \
breadcrumb, tab, button, and menu label together to match the in-product UI \
for that locale, or keep the whole list verbatim when the locale already uses \
English-only breadcrumbs; fix any half-and-half lists. Localized Settings \
paths (for example ES **Configuración** > **Configuración de administrador**) \
are correct—do not revert them to English.
9. **Heading anchor parity**: If some section headings use explicit Kramdown \
`{#id}` blocks, ensure peer headings that need stable deep links include the \
expected `{#slug}` (especially multi-table `_includes`).
10. **Sibling nav-title parity**: On landing pages, keep locale `nav_title` \
exactly aligned with established sibling config pages for the same concept \
when they exist (including matching wording and quote style).
11. **CJK Campaign readability**: If English glossary tokens like Campaign/ \
Campaigns must remain in Japanese/Korean prose, allow a local gloss on first \
mention (for example Campaign(キャンペーン), Campaign(캠페인)) and keep it \
consistent in that section.
12. **Sentence-case common nouns**: In localized running prose, avoid turning \
generic common-noun phrases into title case unless they are headings or exact \
UI labels.
13. **A/B terminology precision**: In A/B testing docs, keep *variant* \
terminology precise (never translate it to words meaning “variable”) and keep \
the locale's chosen “winning variant” term consistent across headings, prose, \
tables, and image alts.
14. **Heading punctuation parity**: Do not introduce trailing punctuation on \
localized headings when the English heading line has none.
15. **German data and permissions copy**: For German, fix false-friend \
*Veranstaltung*/*Veranstaltungen* used for analytics *events* (use *Ereignis* \
or *Event* per the page). Fix Denglisch plural tokens such as *Segments* or \
*Campaigns* inside German clauses—use *Segmente*/*Kampagnen* or keep full \
English labels consistently. Long ``{% details %}`` permission lists that \
mirror ``- View …`` / ``- Edit …`` in English should use established German \
permission wording (e.g. *Kampagnen anzeigen*), not verbatim English bullets \
(auto-translate PR #13340).
16. **BrazeAI agents docs hygiene**: Fix duplicate explicit IDs when two \
subsections reused the same `{#use-cases}` (use distinct canvas vs catalog \
slugs). Fix `…/agents/reference/#examples` links to \
`#canvas-agent-examples` (or `#catalog-agent-examples` when intended). In \
French `reference.md`, localize **Save** and thinking-level row labels \
(**Faible**, **Moyen**, **Élevé**). In Korean `deploying_agents.md` monitoring \
copy, localize **Usage**/**Logs**/**Export CSV**/**View** and **Canvases** \
phrasing. Add `{#general}` to Spanish `agents/faq.md` **General** heading when \
peers have it (auto-translate PR #13342).
17. **Landing hero `guide_top_text` links**: If bracket link text is still raw \
English **Segments** (or similar) inside otherwise localized prose, localize \
the label to match the sentence while preserving each \
`]({{site.baseurl}}/…)` URL. For **`fr_fr`** `guide_menu_list` entries to \
`metrics_glossary`, use **Glossaire des indicateurs de rapport** (not \
*d'indicateurs*) when that row exists (auto-translate PR #13341).
18. **`guide_top_text` English splices**: Fix bare English plurals such as \
**Campaigns** or **Segments** glued onto localized wording in hero YAML \
(for example Japanese *運用Campaigns* or German *operative Campaigns*). Use \
a single localized phrase (*運用キャンペーン*, *operative Kampagnen*, etc.) \
per that locale's hub pages (auto-translate PR #13348).
19. **B2B use-case walkthroughs** (`_user_guide/get_started/b2b_use_cases/`): \
Align bold Canvas/webhook step labels with that locale's Canvas docs (not raw \
US English alone in DE/ES/FR/JA/KO/pt-BR). Use localized **campaign** nouns \
(*campaña*, *Kampagne*, *캠페인*, *キャンペーン*, …) and **segment** wording \
for extension UI where sibling pages do—fix mixed **Campaign**/**Segment** \
English drift in procedures. **French** `nav_title`: keep accents (**Évaluation**). \
(auto-translate PR #13347).
20. **Braze agents hub (`agents.md`) polish**: German—if a question `###` line \
uses `{#…}`, keep the **`?`** before the brace when English does. French—fix \
mid-sentence **Décision**-style caps on common nouns (*décision*). \
Japanese—use **Canvasステップ** consistently with other **Canvas** tokens on \
the page, not **キャンバスステップ** (auto-translate PR #13346).
21. **Heading explicit IDs and includes**: Never put the same `{#slug}` twice \
on one heading line. If the English file has **no** YAML `---` front matter at \
the top (typical for `_includes/` partials), do not add a translated \
`nav_title`/`article_title` block—strip it so the file starts like the English \
body (auto-translate PR #13353).
22. **Markdown tables + permission code cells**: In table rows, keep a **space** \
after each ``|`` before an opening inline code token (never ``||`slug` `` with no space). \
**Spanish** ``_includes/whatsapp/template_prerequisites.md``: keep quoted \
WhatsApp permission bullets exactly as English (**View/Edit WhatsApp Message Templates**). \
**Portuguese (Brazil)**: use **um** ``delay`` (not *uma*) before the borrowed \
``delay`` token in in-app troubleshooting; keep **Campaigns** as the Braze \
product token in link-shortening includes when the rest of the file uses \
English **Campaign**/**Campaigns** (auto-translate PR #13356).
23. **Hub pages (`messaging.md`, `data.md`, `administer.md`)**: In YAML \
``guide_top_text`` / long HTML strings, never glue ``</a>`` directly to the \
next word—insert a normal space. **pt-BR** ``messaging`` featured list: the \
Canvas card must read **Canvas**, not *Canva*, when the link targets \
``/messaging/canvas``. **``data.md``**: English uses lowercase *segments* as \
a common noun in the activate paragraph—**pt-BR** should use *segmentos*, not \
capitalized English **Segments**; **JA/KO** should use bold **Segments** for \
the Braze product token in that sentence when English means the product \
surface (auto-translate PR #13357).
24. **A/B testing subtree** (`_user_guide/messaging/ab_testing/`): **Spanish** \
``race_conditions``—use **Escenario** for numbered scenario headings (never \
**Supuesto**); use **Condiciones de carrera** for *race conditions*, not \
*Condiciones de la carrera*. **Spanish** ``ab_test_projection``—keep dashboard \
labels **Target Audience**, **A/B Testing**, **Run Projection** in English bold. \
**Spanish** ``variant_distribution``—use *campaña* for generic multivariate \
sends, not lowercase English *campaign*. **Spanish** ``random_bucket_numbers`` \
step copy—use **Target Audiences** when English does. **Portuguese** \
``concepts``—keep **bucket** for random-bucket terminology (never *baldes*); \
``optimizations``—parallel plural titles and *na etapa **Públicos-alvo***. \
**Korean** ``optimizations``—**WhatsApp Campaigns** when listing channels in \
plural series. **Japanese** ``create_tests`` and campaign composer docs \
(``creating_campaign.md``, ``target_users.md``, channel create articles)—localize \
bold wizard labels from ``ja.json`` (**メッセージング** > **キャンペーン**, \
**キャンペーンを作成**, **ターゲットオーディエンス**, **配信をスケジュール**, \
**オーディエンスの概要**, **ユーザー検索**, **レビューサマリー**, \
**これらのユーザーに送信**, **マルチチャネル**, **チャネルを追加**, \
**バリアントからコピー**, **バリアントを追加**); do not leave US \
**Target Audiences** / **Schedule Delivery** / **Create Campaign** English in \
JA prose. **Japanese** ``ab_test_projection``—use **予測を実行** consistently \
for “run projection”. \
**German** ``optimizations``—**Gewinnervariante** \
/**Personalisierte Variante** (no **Winning Variant** / **Winning-Varianten**); \
``conversion_correlation``—**Nutzer:innen** / **Nutzerattribute** consistently \
(no **Benutzer** mix). **French** ``conversion_correlation``—**campagnes** in \
French prose, not English **Campaigns** mid-sentence (auto-translate PR #13359).
25. **Japanese monthly release notes** (``_lang/ja/_releases/``): In YAML \
``description``, keep the stock closing in polite **です/ます** form—for example \
「…リリースノートが**含まれています**。」—not plain dictionary-style \
「…含まれている。」 so ``description`` matches sibling months in the same \
year (auto-translate PR #13372).
26. **Monthly release notes** (``_releases/``): When English names a concrete \
REST path such as ``/raw_data/status``, keep it in **inline code** (backticks) \
in every locale—including after localized ``[API endpoint](…)`` link text—and \
avoid doubled commas or stray parentheses around the path (auto-translate \
PR #13373).
27. **Monthly release notes** (``_releases/``): The file must start with YAML \
``---`` on line 1—never a decorative ``----`` rule above it (Jekyll will not \
parse front matter). Use **spaces** (for example two spaces) for nested \
markdown bullets, not tab characters, so lists render consistently (auto-translate \
PR #13374).
28. **YAML `nav_title` / `article_title` — ampersand as “and”**: When English \
joins two ordinary words or concepts with `&` (for example **Shopify checkout & \
Liquid**), localized YAML must **not** keep a bare `&` as shorthand for *and* \
unless the English string is a **verbatim** customer-visible UI label that \
actually shows `&`. Spell it out per locale (*und*, *et*, *e*, *y*, *と*, \
*및*/*와*, etc.). Technical spellings like `checkout.liquid` stay literal \
(auto-translate PR #13375).
29. **Release notes (`_releases/`) — bold export/UI lead-ins**: When English \
uses bullets such as `* **Rows with errors:** …` / `* **All rows:** …` that \
**describe** dashboard export choices (not wire identifiers), translate the \
**bold lead-in** to the target language so the line is not half English. Keep \
tokens such as **Error** when English uses them as a literal status label \
(auto-translate PR #13375).
30. **Heading anchors + YAML titles**: Never reuse the same `{#slug}` on \
multiple headings in one file unless the English source does. If the English \
heading line has **no** explicit `{#…}` ID, do not add one in translation. \
When both `nav_title` and `article_title` exist and denote the same words, \
keep their **casing consistent** (match `article_title` to `nav_title` when \
they would otherwise differ only by capitalization) (auto-translate PR #13380).
31. **Administer / dashboard polish** (PR #13384): Do not paste huge invented \
`{#slug}` tails on headings when English has none. Keep `<style>` CSS \
selectors valid (no `nth-child(N), {` before `{`). **Table / Kramdown IAL \
and HTML `<table>` `aria-label` values** should be **localized** with the \
rest of the page (for example `"Use cases"` → `"Casos de uso"`). Do not \
revert localized table `aria-label` strings to English. The translation QC \
pass still re-localizes known nav icon phrases \
`aria-label="Open navigation menu"` / `aria-label="Select your language"` \
when they slip through as English.
32. **Brazilian Portuguese — Braze ``Analytics`` menu**: When English uses bold \
``**Analytics**`` as the dashboard section name in navigation paths (for example \
``**Analytics** > **Report Builder (New)**``) or phrases like "the **Analytics** \
page" / "the **Analytics** section", keep ``**Analytics**`` in pt-BR for that \
product chrome—do **not** substitute ``**Análise de dados**`` in those slots; it \
drifts from sibling analytics docs (auto-translate PR #13386). QC auto-repairs \
common ``**Análise de dados**`` UI fragments when they slip through.
33. **Audience segments subtree** (PR #13387): For ``cdi_segments.md``, keep YAML \
``description`` on the CDI / warehouse topic—never location-targeting boilerplate \
mirrored from a bad English string. For ``rfm_segments.md``, localize ``nav_title`` \
and the H1 away from English ``Segments RFM`` / ``RFM Segments`` in ES/pt-BR/KO. \
For ``managing_segments.md``, never set ``tool:`` to a translated word; it must \
remain ``Segments``.
34. **Liquid ``{% assign %}`` + default fields**: Never nest ``{{ }}`` around \
``${…}`` on the right-hand side of ``{% assign var = … %}`` (for example wrong \
``{% assign my_string = {{${user_id}}} | md5 %}``; correct \
``{% assign my_string = ${user_id} | md5 %}``). When prose describes a Liquid \
example that branches on language (for example ``${language} == 'spanish'``), \
keep the named language in running text **consistent** with that branch \
(auto-translate PR #13388).
35. **Markdown tables + dev_guide YAML (PR #13392)**: Do not start table body \
rows with ``||``—use standard ``| col1 | col2 |`` so you do not insert a blank \
first column. When ``guide_top_text`` embeds HTML with double-quoted attributes \
(``href="..."``), wrap the **whole** YAML value in double quotes and escape inner \
``"`` as ``\"`` so the front matter parses. Match sibling locales' explicit \
``{#…}`` fragments on comparable H1s when deep links depend on them.
36. **Decisioning Studio › audience (PR #13389)**: Use **Google Cloud Storage** \
(and **GCS**) for Braze-controlled export *buckets*—never *Google Cloud Services* \
in that bucket context. In ``{% tabs %}``, when sibling ``{% tab … %}`` labels \
are localized, translate the **Other Platforms** tab label too (do not leave it \
in English alone). On **prepare_data** hub YAML, each ``guide_featured_list`` \
``name:`` should match the linked page's established title in that locale (for \
example pt-BR **Ativos de dados críticos** for the **Critical data assets** row, \
not a divergent synonym). German ``get_started``—localize stray English section \
titles such as **Best Practices** when the surrounding section is German.
37. **CDI SQL Editor** (``…/cloud_ingestion/sql_editor.md``): Keep ``PAYLOAD`` \
and ``UPDATED_AT`` in backticks with **English casing**. Translate \
troubleshooting ``###`` error-topic headings (do not leave titles such as \
**No preview available** in English when the page is localized). On those \
four ``###`` lines, add ``{#no-preview-available}``, ``{#identity-column-required}``, \
``{#no-attributes-to-sync}``, and ``{#query-execution-timed-out}`` so anchors \
stay stable across locales (auto-translate PR #13397).

Return ONLY the improved translated file — no explanations, no code fences, \
no commentary. If the translation is already high quality, return it unchanged.\
"""


def review_file(
    client, english_content, translated_content, language_name,
    extra_context="", api_retries=None,
):
    """Second-pass review of a translation for quality improvement."""
    system = [(REVIEW_PROMPT, True)]
    if extra_context:
        system.append((extra_context, False))

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## English source\n\n{english_content}\n\n"
    user_msg += f"## Translation to review and improve\n\n{translated_content}\n"

    return call_claude(client, system, user_msg, retries=api_retries)



ACCEPTED_PREFIXES = ("_docs/", "_includes/")


def _relative_for_translation(fpath):
    """Return the path relative to ``_lang/<code>/`` for use with translation_path().

    _docs/ files are stored directly under _lang/<code>/ so we strip the
    ``_docs/`` prefix.  _includes/ files keep their prefix because
    _lang/<code>/ mirrors the top-level _includes/ directory.
    """
    if fpath.startswith("_docs/"):
        return str(Path(fpath).relative_to("_docs"))
    return fpath


def translation_path(english_relative, lang_dir):
    """Map an English-relative path to its _lang/ counterpart."""
    return REPO_ROOT / "_lang" / lang_dir / english_relative


def _git_path_last_commit_ts(rel_path: str) -> int:
    """Latest commit unix time touching ``rel_path`` (0 if unknown)."""
    r = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", rel_path],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return 0
    s = (r.stdout or "").strip()
    return int(s) if s.isdigit() else 0


def _parse_git_touch_map(max_commits: int) -> dict[str, int]:
    """Map repo-relative paths to the latest commit time touching them.

    Built from recent first-parent history so routine ``workflow_dispatch``
    runs avoid one ``git log`` per file.
    """
    lang_roots = [f"_lang/{info['dir']}/" for info in LANGUAGES.values()]
    r = subprocess.run(
        [
            "git",
            "log",
            "-m",
            "--first-parent",
            f"-n{max_commits}",
            "--format=%ct",
            "--name-only",
            "HEAD",
            "--",
            "_docs/",
            "_includes/",
            *lang_roots,
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if r.returncode != 0:
        return {}
    touch: dict[str, int] = {}
    current_ts: Optional[int] = None
    for raw in (r.stdout or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.isdigit():
            current_ts = int(line)
            continue
        if current_ts is None:
            continue
        prev = touch.get(line)
        if prev is None or current_ts > prev:
            touch[line] = current_ts
    return touch


def _list_git_english_markdown_paths() -> list[str]:
    """Tracked ``*.md`` under ``_docs/`` and ``_includes/`` (repo-relative)."""
    r = subprocess.run(
        ["git", "ls-files"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    paths: list[str] = []
    for line in r.stdout.splitlines():
        p = line.strip()
        if not p.endswith(".md"):
            continue
        if p.startswith("_docs/") or p.startswith("_includes/"):
            paths.append(p)
    return paths


def cmd_stale_english_sources(args: argparse.Namespace) -> None:
    """Print English paths that are missing or older than any locale mirror.

    Used when ``workflow_dispatch`` runs with no ``since_commit`` / ``files``:
    compare last-touch times from git so operators do not paste SHAs.
    Locale files live under ``_lang/<dir>/`` using ``_relative_for_translation``
    (``_docs/`` prefix stripped); stdout still lists canonical ``_docs/…`` /
    ``_includes/…`` paths for the workflow.
    """
    lang_dirs = [info["dir"] for info in LANGUAGES.values()]
    touch_map = _parse_git_touch_map(args.max_history_commits)
    fallback_cache: dict[str, int] = {}

    def ts_for(rel: str) -> int:
        if rel in touch_map:
            return touch_map[rel]
        if rel in fallback_cache:
            return fallback_cache[rel]
        t = _git_path_last_commit_ts(rel)
        fallback_cache[rel] = t
        return t

    english_paths = _list_git_english_markdown_paths()
    stale: list[str] = []
    for en in english_paths:
        en_ts = ts_for(en)
        trans_rel = _relative_for_translation(en)
        need = False
        for ld in lang_dirs:
            loc_rel = f"_lang/{ld}/{trans_rel}"
            loc_path = REPO_ROOT / loc_rel
            if not loc_path.is_file():
                need = True
                break
            loc_ts = ts_for(loc_rel)
            if loc_ts < en_ts:
                need = True
                break
        if need:
            stale.append(en)

    stale.sort()
    if len(stale) > 250:
        print(
            "stale-english-sources: WARNING: large batch - consider "
            "`since_commit` or `files` to narrow scope if this was unintentional.",
            file=sys.stderr,
        )
    print(
        f"stale-english-sources: {len(stale)} file(s) need translation "
        f"(of {len(english_paths)} English markdown paths tracked in git)",
        file=sys.stderr,
    )
    body = "\n".join(stale) + ("\n" if stale else "")
    sys.stdout.write(body)
    sys.stdout.flush()


# Keys whose values carry cross-section terminology (nav labels, page
# title, meta description, hero header). These are the strings a reader
# sees in navigation, search, and landing-page heroes — the surfaces
# where "same product, different wording" is most jarring.
#
# ``guide_top_header`` is included because the prompt already tells the
# LLM to reuse it for cross-section consistency (``translation_prompt.md``
# "Cross-section consistency" section) and it appears widely across
# ``_lang/*`` front matter; omitting it here meant the injected context
# and the QC drift check both silently ignored a key the prompt was
# asking the model to mirror (Copilot flag on PR #13303).
_SIBLING_CONTEXT_FM_KEYS = (
    "nav_title",
    "article_title",
    "title",
    "description",
    "guide_top_header",
)

# Cap how many related pages we expose to the LLM per translation to keep
# prompt size predictable. In practice an IA move produces 1 sibling and a
# product-area tree adds 2–4 deeper guides. Cap at 5 for safety.
_SIBLING_CONTEXT_MAX = 5

# Max characters of body excerpt to include per related page. Front matter
# alone catches IA-move drift (see PR #13297 / feature_flags.md), but
# product-area drift (PR #13298 / email.md — "Standard" tier labels, bullet
# phrasing) lives in body prose, so we include a short body excerpt too.
_SIBLING_CONTEXT_BODY_CHARS = 1400


# Per-process cache of ``list(lang_root.rglob("*.md"))`` per locale.
#
# Without this, ``_find_related_locale_pages`` (which does one rglob per
# translated file for basename + one for every ``.md`` in the locale
# when ``len(stem) >= 4``) scanned ~12K paths per locale × 6 locales
# × N translated files in a wave, turning prompt-building into the
# dominant cost of a batch. Copilot flagged the O(N × M) hot path on
# PR #13303. Caching the path list once per process collapses that to
# a single walk per locale; the cache is bounded (≤6 locales × ~12K
# entries ≈ 72K Path objects) and a fresh process is spawned per CLI
# invocation, so there's no stale-data risk.
_LOCALE_MD_PATH_CACHE: dict = {}


def _locale_md_paths(lang_dir):
    """Return a cached list of every ``.md`` path under ``_lang/<lang_dir>/``.

    The first call walks ``_lang/<lang_dir>/`` once and memoizes the
    result; subsequent calls in the same process reuse the list.
    """
    cached = _LOCALE_MD_PATH_CACHE.get(lang_dir)
    if cached is not None:
        return cached
    lang_root = REPO_ROOT / "_lang" / lang_dir
    if not lang_root.exists():
        _LOCALE_MD_PATH_CACHE[lang_dir] = []
        return _LOCALE_MD_PATH_CACHE[lang_dir]
    _LOCALE_MD_PATH_CACHE[lang_dir] = list(lang_root.rglob("*.md"))
    return _LOCALE_MD_PATH_CACHE[lang_dir]


def _find_sibling_translations(basename, lang_dir, exclude_target):
    """Return already-translated files in the locale with the same basename.

    Used by the QC drift check (which only compares same-concept pages).
    See ``_find_related_locale_pages`` for the broader prompt-context lookup.
    """
    all_paths = _locale_md_paths(lang_dir)
    if not all_paths:
        return []
    exclude_resolved = exclude_target.resolve() if exclude_target else None
    hits = []
    for path in sorted(p for p in all_paths if p.name == basename):
        try:
            if exclude_resolved and path.resolve() == exclude_resolved:
                continue
        except OSError:
            continue
        try:
            content = path.read_text()
        except OSError:
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        hits.append((rel, content))
        if len(hits) >= _SIBLING_CONTEXT_MAX:
            break
    return hits


_SECTION_RANK = {
    "_user_guide": 0,
    "_developer_guide": 1,
    "_partners": 2,
    "_help": 2,
    "_hidden": 3,
    "_api": 4,
    "_includes": 5,
}

# Candidate categories (lower wins):
#   0 — same-basename (IA-move sibling)
#   1 — stem-prefix/suffix filename (e.g. email.md → email_services.md)
#   2 — same-stem-directory (e.g. channels/email.md → …/email/**/*.md)
_CAT_SAME_BASENAME = 0
_CAT_STEM_FILENAME = 1
_CAT_STEM_DIRECTORY = 2


def _related_page_priority(path, lang_dir, category):
    """Lower is better. Favors user-facing sections, then category."""
    parts = path.parts
    try:
        lang_idx = parts.index(lang_dir)
        section = parts[lang_idx + 1] if lang_idx + 1 < len(parts) else ""
    except ValueError:
        section = ""
    section_rank = _SECTION_RANK.get(section, 9)
    return (section_rank, category, len(parts), str(path))


def _find_related_locale_pages(fpath, lang_dir, exclude_target):
    """Return locale pages likely to cover the same Braze product area.

    Candidates are gathered from three lookups and then ranked so the most
    relevant pages win the ``_SIBLING_CONTEXT_MAX`` slots:

    1. **Same-basename** siblings — an IA move relocates ``_docs/a/foo.md``
       to ``_docs/b/foo.md``; the locale's existing ``_lang/<locale>/.../foo.md``
       is an authoritative terminology reference (see PR #13297).
    2. **Stem-prefix/suffix** filenames — for ``channels/email.md`` the
       locale's ``email_services.md``, ``email_setup.md``, etc. are
       near-canonical terminology references even when buried several
       levels deep. Also picks up ``_email.md``-style suffixes
       (see PR #13298).
    3. **Same-stem-directory** pages — for ``channels/email.md``, every
       ``_lang/<locale>/.../email/**/*.md`` is in the same product area,
       covering the locale's glossary and phrasing conventions (tier
       labels, bullet sentence structure, etc.).

    Priority ranking favors ``_user_guide/`` over ``_api/`` / ``_includes/``,
    then prefers same-basename → stem-filename → stem-directory so
    canonical user-facing prose wins out over machine-format fragments.
    """
    basename = Path(fpath).name
    stem = Path(fpath).stem
    all_paths = _locale_md_paths(lang_dir)
    if not all_paths:
        return []

    exclude_resolved = exclude_target.resolve() if exclude_target else None
    candidates = {}

    def _consider(path, category):
        try:
            resolved = path.resolve()
        except OSError:
            return
        if exclude_resolved and resolved == exclude_resolved:
            return
        existing = candidates.get(resolved)
        prio = _related_page_priority(path, lang_dir, category)
        if existing is None or prio < existing[0]:
            candidates[resolved] = (prio, path)

    # Single pass over the cached locale index — categorise each file by
    # whichever lookup rule it matches, if any. The earlier implementation
    # did one ``rglob(basename)`` plus one ``rglob("*.md")`` per call, so
    # a wave of 40 files × 6 locales walked the ``_lang`` tree 480 times;
    # the shared ``_locale_md_paths`` cache now walks it 6 times per
    # process (Copilot performance flag on PR #13303).
    stem_ok = len(stem) >= 4
    stem_prefix = f"{stem}_" if stem_ok else ""
    stem_suffix = f"_{stem}.md" if stem_ok else ""
    for path in all_paths:
        if path.name == basename:
            _consider(path, _CAT_SAME_BASENAME)
            continue
        # The stem-based lookups are scoped to pages that actually live
        # inside a directory named for the stem (e.g. ``.../email/**``).
        # A global ``email_*`` glob would otherwise drag in weakly-related
        # files like ``analytics/tracking/email_tracking.md`` that don't
        # share the same product-area glossary.
        if not stem_ok or stem not in path.parts:
            continue
        if path.name.startswith(stem_prefix) or path.name.endswith(stem_suffix):
            _consider(path, _CAT_STEM_FILENAME)
        else:
            _consider(path, _CAT_STEM_DIRECTORY)

    ordered = sorted(candidates.values(), key=lambda item: item[0])
    out = []
    for _, path in ordered:
        if len(out) >= _SIBLING_CONTEXT_MAX:
            break
        try:
            content = path.read_text()
        except OSError:
            continue
        out.append((path.relative_to(REPO_ROOT).as_posix(), content))
    return out


def _sibling_front_matter_snippet(content):
    """Extract only the cross-section terminology keys from a sibling file."""
    fm, _ = _extract_front_matter(content)
    if not fm:
        return ""
    lines = []
    for key in _SIBLING_CONTEXT_FM_KEYS:
        block = _extract_fm_block(fm, key)
        if block:
            lines.append(block)
    return "\n".join(lines)


def _related_page_snippet(content):
    """Return FM (terminology keys) + a short body excerpt for prompt context.

    The body excerpt captures body-level glossary drift (tier labels in
    bullet lists, preferred sentence patterns, etc.) that front matter alone
    misses. Capped at ``_SIBLING_CONTEXT_BODY_CHARS`` to keep token use
    predictable.
    """
    parts = []
    fm_snippet = _sibling_front_matter_snippet(content)
    if fm_snippet:
        parts.append("Front matter (terminology reference):\n```yaml\n"
                     + fm_snippet + "\n```")
    _, body = _extract_front_matter(content)
    if body:
        excerpt = body.lstrip()
        if len(excerpt) > _SIBLING_CONTEXT_BODY_CHARS:
            excerpt = excerpt[:_SIBLING_CONTEXT_BODY_CHARS].rstrip() + "\n…"
        if excerpt.strip():
            parts.append("Body excerpt (glossary/phrasing reference — do "
                         "NOT translate or copy this):\n```markdown\n"
                         + excerpt + "\n```")
    return "\n\n".join(parts)


def _build_sibling_context(fpath, lang_dir, target):
    """Build a prompt section listing related locale pages for terminology.

    Returns an empty string when no related pages exist, so the function is
    safe to always call.
    """
    related = _find_related_locale_pages(fpath, lang_dir, target)
    if not related:
        return ""
    blocks = []
    for rel, content in related:
        snippet = _related_page_snippet(content)
        if not snippet:
            continue
        blocks.append(f"### {rel}\n\n{snippet}")
    if not blocks:
        return ""
    header = (
        "## Cross-section consistency (related locale pages)\n\n"
        "The target locale already ships translated page(s) that cover the "
        "same Braze concept or product area as the file you are about to "
        "translate — either because an information-architecture move "
        "relocated the English source (same basename) or because deeper "
        "guides live under a directory named for this product (e.g. "
        "`…/email/…` guides when you are translating `channels/email.md`). "
        "Use them as the **authoritative terminology and phrasing reference "
        "for this locale**:\n\n"
        "- Reuse **`nav_title`**, **`article_title`**, **`title`**, "
        "**`description`**, and (when present) **`guide_top_header`** wording "
        "verbatim when the page covers the same concept — the QC step "
        "compares these keys against same-basename siblings and reviewers "
        "flag paraphrases (e.g. German FAQ `description` drift on PR #13316).\n"
        "- Reuse body **glossary terms** — product names, tier/plan labels, "
        "UI strings, and loanword conventions (e.g., Japanese katakana "
        "`スタンダード` / `デラックス` for support tiers rather than native "
        "equivalents like `標準`).\n"
        "- Match the locale's **sentence patterns for bullet lists** (e.g., "
        "Romance languages often prefer verb forms — *Mitigar y remediar…* — "
        "over nominalizations — *Mitigación y remediación de…*).\n"
        "- **Do not translate or copy** these snippets into your output. "
        "They are context only; translate the English source under "
        "`## English source`."
    )
    return header + "\n\n" + "\n\n".join(blocks) + "\n"


def load_results():
    if RESULTS_FILE.exists():
        return json.loads(RESULTS_FILE.read_text())
    return {"translated": [], "failed": []}


def save_results(results):
    RESULTS_FILE.write_text(json.dumps(results, indent=2))


# ---------------------------------------------------------------------------
# translate
# ---------------------------------------------------------------------------

def _translate_one_chunk_with_retries(
    client,
    prompt,
    en_chunk,
    tr_chunk,
    lang_name,
    extra_context,
    chunk_label,
    *,
    api_retries=None,
    chunk_liquid_attempts=None,
):
    """Translate one chunk with Liquid validation/repair and retries."""
    attempts = chunk_liquid_attempts or max(3, (api_retries or API_RETRIES) // 2)
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            candidate = translate_file(
                client,
                prompt,
                en_chunk,
                tr_chunk or None,
                lang_name,
                extra_context,
                api_retries=api_retries,
            )
            return _validate_or_repair_chunk_liquid(en_chunk, candidate, chunk_label)
        except ValueError as exc:
            last_exc = exc
            if attempt < attempts:
                print(
                    f"    Liquid check failed for {chunk_label} "
                    f"(attempt {attempt}/{attempts}): {exc}; retrying chunk..."
                )
                time.sleep(min(30, 5 * attempt))
            else:
                raise
    raise last_exc or ValueError(f"No translation for {chunk_label}")


def translate_one_incremental(
    client,
    prompt,
    fpath,
    relative,
    english_content,
    previous_english_content,
    lang_key,
    lang_info,
    glossary,
    styleguide,
    *,
    api_retries=None,
    uses_size_chunking=False,
):
    """Translate only H2 sections whose English changed since *previous_english_content*."""
    target = translation_path(relative, lang_info["dir"])
    existing = target.read_text() if target.exists() else None

    filtered = filter_glossary(glossary, english_content)
    glossary_section = format_glossary_for_prompt(filtered)
    sibling_section = _build_sibling_context(fpath, lang_info["dir"], target)
    extra_context = styleguide + glossary_section
    if sibling_section:
        extra_context = extra_context + "\n\n" + sibling_section

    en_chunks = split_into_h2_chunks(english_content)
    prev_chunks = (
        split_into_h2_chunks(previous_english_content)
        if previous_english_content
        else []
    )
    tr_chunks = match_existing_chunks(en_chunks, existing)
    needs = chunks_requiring_translation(en_chunks, prev_chunks)

    for i, (need, tr_chunk) in enumerate(zip(needs, tr_chunks)):
        if not need and not (tr_chunk or "").strip():
            needs[i] = True

    skipped = sum(1 for need in needs if not need)
    to_translate = sum(1 for need in needs if need)

    if to_translate == 0:
        print(
            f"    [{lang_key}] incremental: all {len(en_chunks)} H2 chunk(s) "
            f"unchanged — skipping"
        )
        return {
            "ok": True,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "incremental": True,
            "chunks_skipped": skipped,
            "chunks_translated": 0,
        }

    print(
        f"    [{lang_key}] incremental: {to_translate}/{len(en_chunks)} H2 chunk(s) "
        f"to translate ({skipped} unchanged)"
    )

    chunk_liquid_attempts = max(3, (api_retries or API_RETRIES) // 2)
    max_bytes = CHUNK_TARGET_KB * 1024

    try:
        if len(en_chunks) == 1 and needs[0] and not uses_size_chunking:
            translated = translate_file(
                client,
                prompt,
                english_content,
                existing,
                lang_info["name"],
                extra_context,
                api_retries=api_retries,
            )
            translated = review_file(
                client,
                english_content,
                translated,
                lang_info["name"],
                extra_context,
                api_retries=api_retries,
            )
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(translated)
            return {
                "ok": True,
                "source": fpath,
                "target": str(target.relative_to(REPO_ROOT)),
                "lang": lang_key,
                "incremental": True,
                "chunks_skipped": 0,
                "chunks_translated": 1,
            }

        output_chunks = []
        for i, (en_chunk, tr_chunk, need) in enumerate(
            zip(en_chunks, tr_chunks, needs)
        ):
            chunk_label = (
                f"{target.relative_to(REPO_ROOT)} H2 chunk {i + 1}/{len(en_chunks)}"
            )
            if not need:
                output_chunks.append(tr_chunk)
                continue

            print(
                f"    [{lang_key}] translating H2 chunk {i + 1}/{len(en_chunks)} "
                f"({len(en_chunk) // 1024}KB)..."
            )

            if uses_size_chunking and len(en_chunk.encode()) > max_bytes:
                sub_en = split_into_chunks(en_chunk)
                sub_tr = match_existing_chunks(sub_en, tr_chunk or "")
                sub_out = []
                for j, (sub_en_chunk, sub_tr_chunk) in enumerate(
                    zip(sub_en, sub_tr)
                ):
                    sub_label = f"{chunk_label} sub-chunk {j + 1}/{len(sub_en)}"
                    sub_out.append(
                        _translate_one_chunk_with_retries(
                            client,
                            prompt,
                            sub_en_chunk,
                            sub_tr_chunk,
                            lang_info["name"],
                            extra_context,
                            sub_label,
                            api_retries=api_retries,
                            chunk_liquid_attempts=chunk_liquid_attempts,
                        )
                    )
                output_chunks.append(
                    "\n\n".join(c.strip() for c in sub_out)
                )
            else:
                output_chunks.append(
                    _translate_one_chunk_with_retries(
                        client,
                        prompt,
                        en_chunk,
                        tr_chunk,
                        lang_info["name"],
                        extra_context,
                        chunk_label,
                        api_retries=api_retries,
                        chunk_liquid_attempts=chunk_liquid_attempts,
                    )
                )

        full_translation = "\n\n".join(c.strip() for c in output_chunks)
        validate_liquid_paired_tags(
            full_translation,
            label=str(target.relative_to(REPO_ROOT)),
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(full_translation)
        return {
            "ok": True,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "incremental": True,
            "chunked": uses_size_chunking,
            "chunks": len(en_chunks),
            "chunks_skipped": skipped,
            "chunks_translated": to_translate,
        }
    except Exception as exc:
        return {
            "ok": False,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "error": str(exc),
            "incremental": True,
            "chunked": uses_size_chunking,
        }


def translate_one(client, prompt, fpath, relative, english_content,
                  lang_key, lang_info, glossary, styleguide, api_retries=None,
                  english_base_ref=None):
    """Translate + review a single file into one language. Returns a result dict."""
    previous_english = load_english_at_git_ref(fpath, english_base_ref)
    if previous_english is not None and not incremental_h2_requires_full_file(
        english_content, previous_english
    ):
        return translate_one_incremental(
            client,
            prompt,
            fpath,
            relative,
            english_content,
            previous_english,
            lang_key,
            lang_info,
            glossary,
            styleguide,
            api_retries=api_retries,
            uses_size_chunking=False,
        )
    if previous_english is not None and incremental_h2_requires_full_file(
        english_content, previous_english
    ):
        print(
            f"    [{lang_key}] incremental H2 unsafe for sdktabs topology in "
            f"{relative} — full-file translation"
        )

    target = translation_path(relative, lang_info["dir"])
    existing = target.read_text() if target.exists() else None

    filtered = filter_glossary(glossary, english_content)
    glossary_section = format_glossary_for_prompt(filtered)
    sibling_section = _build_sibling_context(fpath, lang_info["dir"], target)
    extra_context = styleguide + glossary_section
    if sibling_section:
        extra_context = extra_context + "\n\n" + sibling_section

    try:
        translated = translate_file(
            client, prompt, english_content, existing,
            lang_info["name"], extra_context, api_retries=api_retries,
        )
        translated = review_file(
            client, english_content, translated,
            lang_info["name"], extra_context, api_retries=api_retries,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(translated)
        return {
            "ok": True,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
        }
    except Exception as exc:
        if _is_max_tokens_truncation_error(exc):
            print(
                f"    [{lang_key}] single-pass output hit token limit "
                f"({relative}) — falling back to chunked translation..."
            )
            return translate_one_chunked(
                client,
                prompt,
                fpath,
                relative,
                english_content,
                lang_key,
                lang_info,
                glossary,
                styleguide,
                api_retries=api_retries,
            )
        return {
            "ok": False,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "error": str(exc),
        }


def _retry_failed_translations(
    client,
    prompt,
    failed_items,
    active_langs,
    glossaries,
    styleguides,
    round_num=1,
    english_base_ref=None,
):
    """Re-run failed translations sequentially (normal and chunked paths)."""
    retriable = [
        item
        for item in failed_items
        if _is_retryable_translation_error(item.get("error", ""))
    ]
    if not retriable:
        return [], list(failed_items)

    print(
        f"\nRetrying {len(retriable)} failed translation(s) sequentially "
        f"(round {round_num}/{FAILED_PASS_ROUNDS}, "
        f"{FAILED_PASS_RETRIES} API attempts each)..."
    )
    recovered = []
    still_failed = [item for item in failed_items if item not in retriable]

    for item in retriable:
        fpath = item["source"]
        lang_key = item["lang"]
        lang_info = active_langs.get(lang_key)
        if not lang_info:
            still_failed.append(item)
            continue

        relative = _relative_for_translation(fpath)
        english_content = (REPO_ROOT / fpath).read_text()
        mode = "chunked" if item.get("chunked") else "normal"
        print(f"  RETRY ({mode}): {relative} → {lang_info['name']}...")
        time.sleep(10)

        if item.get("chunked"):
            result = translate_one_chunked(
                client,
                prompt,
                fpath,
                relative,
                english_content,
                lang_key,
                lang_info,
                glossaries[lang_key],
                styleguides[lang_key],
                api_retries=FAILED_PASS_RETRIES,
                english_base_ref=english_base_ref,
            )
        else:
            result = translate_one(
                client,
                prompt,
                fpath,
                relative,
                english_content,
                lang_key,
                lang_info,
                glossaries[lang_key],
                styleguides[lang_key],
                api_retries=FAILED_PASS_RETRIES,
                english_base_ref=english_base_ref,
            )

        if result["ok"]:
            recovered.append(result)
            print(f"  RETRY OK: {relative} → {lang_info['name']}")
        else:
            still_failed.append(result)
            print(
                f"  RETRY FAILED: {relative} → {lang_info['name']} "
                f"({result['error']})"
            )

    return recovered, still_failed


def translate_one_chunked(client, prompt, fpath, relative, english_content,
                          lang_key, lang_info, glossary, styleguide,
                          api_retries=None, english_base_ref=None):
    """Translate a large file by splitting into chunks, translating each, and
    reassembling.  Skips the second-pass review (chunks are self-contained and
    the review would require the full file which exceeds context limits)."""
    previous_english = load_english_at_git_ref(fpath, english_base_ref)
    if previous_english is not None and not incremental_h2_requires_full_file(
        english_content, previous_english
    ):
        return translate_one_incremental(
            client,
            prompt,
            fpath,
            relative,
            english_content,
            previous_english,
            lang_key,
            lang_info,
            glossary,
            styleguide,
            api_retries=api_retries,
            uses_size_chunking=True,
        )
    if previous_english is not None and incremental_h2_requires_full_file(
        english_content, previous_english
    ):
        print(
            f"    [{lang_key}] incremental H2 unsafe for sdktabs topology in "
            f"{relative} — chunked full-file translation"
        )

    target = translation_path(relative, lang_info["dir"])
    existing = target.read_text() if target.exists() else None

    filtered = filter_glossary(glossary, english_content)
    glossary_section = format_glossary_for_prompt(filtered)
    sibling_section = _build_sibling_context(fpath, lang_info["dir"], target)
    extra_context = styleguide + glossary_section
    if sibling_section:
        extra_context = extra_context + "\n\n" + sibling_section

    en_chunks = split_into_chunks(english_content)
    tr_chunks = match_existing_chunks(en_chunks, existing)

    print(f"    [{lang_key}] chunked: {len(en_chunks)} chunks")

    # Per-chunk Liquid checks: discovering a missing {% endapi %} only after
    # all ~26 chunks finish wastes ~90 minutes on Currents glossaries.
    chunk_liquid_attempts = max(3, (api_retries or API_RETRIES) // 2)

    translated_chunks = []
    try:
        for i, (en_chunk, tr_chunk) in enumerate(zip(en_chunks, tr_chunks)):
            print(f"    [{lang_key}] translating chunk {i + 1}/{len(en_chunks)} "
                  f"({len(en_chunk) // 1024}KB)...")
            chunk_label = (
                f"{target.relative_to(REPO_ROOT)} chunk {i + 1}/{len(en_chunks)}"
            )
            last_exc = None
            translated = None
            for attempt in range(1, chunk_liquid_attempts + 1):
                try:
                    candidate = translate_file(
                        client,
                        prompt,
                        en_chunk,
                        tr_chunk or None,
                        lang_info["name"],
                        extra_context,
                        api_retries=api_retries,
                    )
                    translated = _validate_or_repair_chunk_liquid(
                        en_chunk, candidate, chunk_label
                    )
                    break
                except ValueError as exc:
                    last_exc = exc
                    if attempt < chunk_liquid_attempts:
                        print(
                            f"    [{lang_key}] chunk {i + 1} Liquid check failed "
                            f"(attempt {attempt}/{chunk_liquid_attempts}): {exc}; "
                            f"retrying chunk..."
                        )
                        time.sleep(min(30, 5 * attempt))
                    else:
                        raise
            if translated is None:
                raise last_exc or ValueError(f"No translation for {chunk_label}")
            translated_chunks.append(translated)

        full_translation = "\n\n".join(c.strip() for c in translated_chunks)
        validate_liquid_paired_tags(
            full_translation,
            label=str(target.relative_to(REPO_ROOT)),
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(full_translation)
        return {
            "ok": True,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "chunked": True,
            "chunks": len(en_chunks),
        }
    except Exception as exc:
        return {
            "ok": False,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "error": str(exc),
            "chunked": True,
        }


def cmd_translate(args):
    """Translate changed English docs into every supported language (or ``--languages`` subset)."""
    active_langs = languages_from_cli_arg(getattr(args, "languages", None))
    english_base_ref = _resolve_english_base_ref(
        getattr(args, "english_base_ref", None)
    )
    if english_base_ref:
        print(f"Incremental H2 translation enabled (English base: {english_base_ref})")
    changed_path = REPO_ROOT / args.changed_files
    if not changed_path.exists():
        print("No changed-files list found. Nothing to translate.")
        return

    all_files = [line.strip() for line in changed_path.read_text().splitlines() if line.strip()]
    md_files = [
        f for f in all_files
        if any(f.startswith(p) for p in ACCEPTED_PREFIXES)
        and f.endswith(".md")
        and (REPO_ROOT / f).exists()
    ]

    if not md_files:
        print("No English .md files changed. Nothing to translate.")
        return

    translatable = []
    chunked = []
    for fpath in md_files:
        size_kb = (REPO_ROOT / fpath).stat().st_size / 1024
        if _uses_chunked_translation(fpath, size_kb):
            chunked.append(fpath)
            reason = (
                "pricing table path"
                if size_kb <= MAX_FILE_KB
                else "size limit"
            )
            print(
                f"  CHUNKED: {fpath} ({round(size_kb)} KB — "
                f"will use chunked translation, {reason})"
            )
        else:
            translatable.append(fpath)

    if not translatable and not chunked:
        print("No translatable files found.")
        return

    n_langs = len(active_langs)
    total_tasks = len(translatable) * n_langs
    chunked_tasks = len(chunked) * n_langs
    lang_label = ", ".join(active_langs.keys())
    print(f"Translating {len(translatable)} file(s) into {n_langs} language(s) "
          f"({lang_label}) — {total_tasks} tasks, {MAX_WORKERS} workers")
    if chunked:
        print(f"  + {len(chunked)} large file(s) via chunked translation "
              f"({chunked_tasks} tasks, sequential)")
    print()

    client = _get_anthropic_client()
    prompt = load_prompt()
    results = load_results()
    results["skipped"] = []
    results["chunked"] = [
        {"source": f, "size_kb": round((REPO_ROOT / f).stat().st_size / 1024)}
        for f in chunked
    ]
    glossaries = {lang: load_glossary(lang) for lang in active_langs}
    styleguides = {lang: load_styleguide(lang) for lang in active_langs}

    # --- Normal parallel translation for files under the size limit ---
    if translatable:
        futures = {}
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            for fpath in translatable:
                relative = _relative_for_translation(fpath)
                english_content = (REPO_ROOT / fpath).read_text()

                for lang_key, lang_info in active_langs.items():
                    future = pool.submit(
                        translate_one, client, prompt, fpath, relative,
                        english_content, lang_key, lang_info,
                        glossaries[lang_key], styleguides[lang_key],
                        english_base_ref=english_base_ref,
                    )
                    futures[future] = (relative, lang_info["name"])

            done_count = 0
            for future in as_completed(futures):
                done_count += 1
                relative, lang_name = futures[future]
                result = future.result()

                if result["ok"]:
                    results["translated"].append({
                        "source": result["source"],
                        "target": result["target"],
                        "lang": result["lang"],
                    })
                    print(f"  [{done_count}/{total_tasks}] {relative} → {lang_name} done")
                else:
                    results["failed"].append({
                        "source": result["source"],
                        "target": result["target"],
                        "lang": result["lang"],
                        "error": result["error"],
                    })
                    print(f"  [{done_count}/{total_tasks}] {relative} → {lang_name} "
                          f"FAILED ({result['error']})")

    # --- Chunked translation for large files ---
    if chunked:
        print(f"\nStarting chunked translation for {len(chunked)} large file(s)...")
        for fpath in chunked:
            relative = _relative_for_translation(fpath)
            english_content = (REPO_ROOT / fpath).read_text()
            print(f"\n  {fpath} ({len(english_content) // 1024}KB)")

            for lang_key, lang_info in active_langs.items():
                result = translate_one_chunked(
                    client, prompt, fpath, relative, english_content,
                    lang_key, lang_info,
                    glossaries[lang_key], styleguides[lang_key],
                    english_base_ref=english_base_ref,
                )
                if result["ok"]:
                    results["translated"].append({
                        "source": result["source"],
                        "target": result["target"],
                        "lang": result["lang"],
                    })
                    print(f"    {lang_info['name']} done "
                          f"({result.get('chunks', '?')} chunks)")
                else:
                    results["failed"].append({
                        k: result[k]
                        for k in ("source", "target", "lang", "error", "chunked", "chunks")
                        if k in result
                    })
                    print(f"    {lang_info['name']} FAILED ({result['error']})")

    for round_num in range(1, FAILED_PASS_ROUNDS + 1):
        if not results["failed"]:
            break
        recovered, still_failed = _retry_failed_translations(
            client,
            prompt,
            results["failed"],
            active_langs,
            glossaries,
            styleguides,
            round_num=round_num,
            english_base_ref=english_base_ref,
        )
        results["translated"].extend(recovered)
        results["failed"] = still_failed

    save_results(results)
    ok = len(results["translated"])
    fail = len(results["failed"])
    print(f"\nTranslation complete: {ok} succeeded, {fail} failed")
    if fail:
        sys.exit(1)


# ---------------------------------------------------------------------------
# QC checks and repairs
# ---------------------------------------------------------------------------

def _extract_front_matter(content):
    """Extract YAML front matter and body from a markdown file.

    Accepts a closing ``---`` delimiter at end-of-file with no newline after it
    (YAML-only hub pages). Requiring a body newline after ``---`` previously
    made the matcher fail so the entire file was treated as body, which inflated
    glossary substring counts for keys like ``segment`` inside YAML (PR
    #13348). Only horizontal space may follow the closing ``---`` before that
    newline or EOF so blank lines after the delimiter stay in the body.

    Optional leading spaces or tabs before the opening ``---`` are ignored so
    files such as ``_docs/_hidden/other/support_contact.md`` (indented YAML)
    still parse; otherwise QC treats English as having no front matter and
    cannot re-seed dropped locale YAML (auto-translate PR #13475).
    """
    # After the closing ``---``, only horizontal space may appear before the
    # body newline or EOF — ``\s*`` would swallow blank lines that belong to
    # the markdown body.
    match = re.match(
        r'^[ \t]*---\s*\n(.*?)\n---[ \t]*(?:\n|\Z)', content, re.DOTALL
    )
    if match:
        return match.group(1), content[match.end():]
    return None, content


def _extract_fm_block(fm_str, key):
    """Extract a full YAML block for a key (key line + indented continuation)."""
    lines = fm_str.split('\n')
    block_lines = []
    in_block = False
    for line in lines:
        if not in_block and re.match(rf'^{re.escape(key)}\s*:', line):
            in_block = True
            block_lines.append(line)
        elif in_block:
            if line and line[0] in (' ', '\t'):
                block_lines.append(line)
            else:
                break
    return '\n'.join(block_lines) if block_lines else None


def repair_front_matter(english_content, translated_content):
    """Ensure non-translatable front matter values match the English source."""
    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, tr_body = _extract_front_matter(translated_content)

    if not en_fm or not tr_fm:
        return translated_content, []

    repairs = []
    repaired_fm = tr_fm

    for key in sorted(NON_TRANSLATABLE_FM_KEYS):
        en_block = _extract_fm_block(en_fm, key)
        tr_block = _extract_fm_block(repaired_fm, key)

        if en_block and tr_block and en_block != tr_block:
            repaired_fm = repaired_fm.replace(tr_block, en_block)
            repairs.append(f"front_matter:{key} — restored from English")
        elif en_block and not tr_block:
            repaired_fm = repaired_fm.rstrip() + '\n' + en_block
            repairs.append(f"front_matter:{key} — re-added missing key")

    if repairs:
        translated_content = f"---\n{repaired_fm}\n---\n{tr_body}"

    return translated_content, repairs


def repair_spurious_front_matter_when_english_has_none(
    english_content, translated_content
):
    """Strip YAML front matter from translation when the English source has none.

    Includes (``_includes/``) and a few body-only snippets start with markdown
    directly. Models sometimes prepend a ``---`` block copied from sibling
    pages; Jekyll does not treat that as front matter in an include, so it
    renders as stray rules and visible keys (Copilot / auto-translate PR #13353).
    """
    en_fm, _ = _extract_front_matter(english_content)
    if en_fm:
        return translated_content, []
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []
    return tr_body, [
        "front_matter — removed (English source has no YAML block; "
        "includes must not start with ---)"
    ]


def repair_missing_locale_front_matter_from_english(
    english_content, translated_content
):
    """Re-seed YAML front matter from English when the locale file lost it entirely.

    :func:`repair_front_matter` only syncs keys when *both* sides parse with a
    leading ``---`` block. Models sometimes return a translation body that starts
    with HTML or markdown while the English source has Jekyll metadata (routing,
    ``layout``, ``hide_nav``). Without this repair, localized pages lose their
    front matter entirely (Copilot / auto-translate PR #13466, e.g.
    ``_hidden/other/support_contact.md``).
    """
    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not en_fm or tr_fm is not None:
        return translated_content, []
    merged = f"---\n{en_fm}\n---\n{tr_body}"
    return merged, [
        "front_matter — re-seeded from English (locale had no parseable "
        "--- header; translate nav_title/article_title on a follow-up pass "
        "if needed)"
    ]


def repair_front_matter_display_scalar_cleanup(translated_content):
    """Normalize HTML entities and rare typos in display-oriented YAML keys.

    Models sometimes emit ``&amp;`` in ``nav_title`` / ``article_title`` /
    ``guide_top_header`` so the literal entity appears in the site chrome
    (Copilot PR #13319). German ``Spam-Trap's`` in a title should be the
    plural ``Spam-Traps``.
    """
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []
    if "&amp;" not in tr_fm and "Spam-Trap's" not in tr_fm:
        return translated_content, []

    repairs = []
    out_lines = []
    for line in tr_fm.split("\n"):
        if re.match(
            r"^(nav_title|article_title|guide_top_header)\s*:.*&amp;",
            line,
        ):
            nl = line.replace("&amp;", "&")
            if nl != line:
                repairs.append("fm — &amp; → & in display YAML key")
            line = nl
        out_lines.append(line)
    new_fm = "\n".join(out_lines)
    if "Spam-Trap's" in new_fm:
        new_fm2 = new_fm.replace("Spam-Trap's", "Spam-Traps")
        if new_fm2 != new_fm:
            repairs.append("fm — Spam-Trap's → Spam-Traps")
        new_fm = new_fm2
    if not repairs:
        return translated_content, []
    return f"---\n{new_fm}\n---\n{tr_body}", repairs


def repair_duplicate_kramdown_heading_anchors(translated_content):
    """Strip duplicate explicit ``{#id}`` tails from markdown headings (keep first).

    Models sometimes repeat the same Kramdown anchor on a later heading that
    reuses a subsection title, which duplicates HTML ``id`` attributes (Copilot
    / auto-translate PR #13380). Fenced code blocks are skipped.
    """
    fm, body = _extract_front_matter(translated_content)
    if fm is None:
        body = translated_content
        prefix = None
    else:
        prefix = f"---\n{fm}\n---\n"

    repairs = []
    lines = body.split("\n")
    out_lines = []
    seen_ids = set()
    in_fence = False
    _heading_anchor_tail = re.compile(r"^(#{1,6}\s+.+?)(\s*\{#([^}]+)\})\s*$")

    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        m = _heading_anchor_tail.match(line)
        if m:
            aid = m.group(3).strip()
            if aid in seen_ids:
                line = m.group(1).rstrip()
                repairs.append(
                    f"heading_anchor — removed duplicate explicit {{#{aid}}} "
                    "(PR #13380)"
                )
            else:
                seen_ids.add(aid)
        out_lines.append(line)

    new_body = "\n".join(out_lines)
    if prefix is None:
        new_content = new_body
    else:
        new_content = prefix + new_body

    if not repairs:
        return translated_content, []

    if translated_content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    return new_content, repairs


def repair_article_title_casefold_matches_nav_title(translated_content):
    """When ``article_title`` and ``nav_title`` differ only by casing, align to ``nav_title``.

    Reviewers expect display titles to match the navigation label casing when
    they denote the same phrase (Copilot / auto-translate PR #13380).
    """
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    lines = tr_fm.split("\n")
    nav_line = None
    art_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^nav_title\s*:", line):
            nav_line = line
        if re.match(r"^article_title\s*:", line):
            art_idx = i
    if nav_line is None or art_idx is None:
        return translated_content, []

    def _scalar_tail(s):
        idx = s.find(":")
        if idx < 0:
            return ""
        return s[idx + 1 :].strip()

    def _unquote_yaml_scalar(s):
        if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
            return s[1:-1]
        return s

    nav_raw = _scalar_tail(nav_line)
    art_line = lines[art_idx]
    art_raw = _scalar_tail(art_line)
    nav_norm = _unquote_yaml_scalar(nav_raw).casefold()
    art_norm = _unquote_yaml_scalar(art_raw).casefold()
    if nav_norm != art_norm:
        return translated_content, []

    colon = nav_line.find(":")
    new_art_line = "article_title" + nav_line[colon:]
    if art_line == new_art_line:
        return translated_content, []

    lines[art_idx] = new_art_line
    new_fm = "\n".join(lines)
    return (
        f"---\n{new_fm}\n---\n{tr_body}",
        [
            "fm — article_title casing aligned to nav_title "
            "(casefold-equal; PR #13380)"
        ],
    )


def repair_releases_spurious_leading_fm_rule(translated_path, translated_content):
    """Remove a stray ``----`` line before YAML when it blocks Jekyll front matter.

    Models sometimes emit a horizontal-rule line immediately before ``---``;
    the page then loses front matter parsing (Copilot PR #13374).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_releases/" not in rel or not rel.endswith(".md"):
        return translated_content, []
    if translated_content.startswith("----\n---"):
        return translated_content[5:], [
            "releases_fm — removed stray ---- before YAML front matter (PR #13374)"
        ]
    if translated_content.startswith("----\r\n---"):
        return translated_content[6:], [
            "releases_fm — removed stray ---- before YAML (CRLF) (PR #13374)"
        ]
    return translated_content, []


def repair_releases_tab_indented_markdown_bullets(translated_path, translated_content):
    """Normalize tab-indented nested list lines to two-space indents.

    Tab-indented ``-`` items render inconsistently across Markdown tooling
    (Copilot PR #13374).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_releases/" not in rel or not rel.endswith(".md"):
        return translated_content, []
    lines = translated_content.split("\n")
    new_lines = []
    changed = 0
    for line in lines:
        if line.startswith("\t- "):
            new_lines.append("  - " + line[3:])
            changed += 1
        else:
            new_lines.append(line)
    if not changed:
        return translated_content, []
    return "\n".join(new_lines), [
        f"releases_md — tab-indented nested list → spaces ({changed} line(s); "
        "PR #13374)"
    ]


def repair_releases_bare_raw_data_status_endpoint(translated_path, translated_content):
    """Wrap the ``/raw_data/status`` REST path in backticks in monthly release notes.

    Copilot flags bare ``/raw_data/status`` after localized link text; use
    inline code so the path is unambiguous (PR #13373).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_releases/" not in rel or not rel.endswith(".md"):
        return translated_content, []
    if "/raw_data/status" not in translated_content:
        return translated_content, []
    if "`/raw_data/status`" in translated_content:
        return translated_content, []

    repairs = []
    new = translated_content
    # Double comma typo from some locales
    if ", /raw_data/status,," in new:
        new = new.replace(", /raw_data/status,,", ", `/raw_data/status`,", 1)
        repairs.append("releases — /raw_data/status inline code (double comma)")
    if ", /raw_data/status," in new:
        new = new.replace(", /raw_data/status,", ", `/raw_data/status`,", 1)
        repairs.append("releases — /raw_data/status inline code (comma delimited)")
    if "、/raw_data/statusを" in new:
        new = new.replace("、/raw_data/statusを", "、`/raw_data/status`を", 1)
        repairs.append("releases — /raw_data/status inline code (JA)")
    if "인 /raw_data/status를" in new:
        new = new.replace("인 /raw_data/status를", "인 `/raw_data/status`를", 1)
        repairs.append("releases — /raw_data/status inline code (KO)")
    if new != translated_content:
        return new, repairs
    return translated_content, []


def repair_ja_releases_description_desu_masu(translated_path, translated_content, lang_key):
    """Normalize a common plain-form ending in Japanese release-note YAML.

    Monthly ``_releases/`` pages use a stock ``description`` line; models
    sometimes emit dictionary-style 「…リリースノートが含まれている。」 while
    sibling months use polite 「…含まれています。」 (Copilot / PR #13372). Only
    the ``description`` key inside front matter is adjusted.
    """
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix()
    if "_releases/" not in rel or not rel.startswith("_lang/ja/"):
        return translated_content, []

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm or "リリースノートが含まれている" not in tr_fm:
        return translated_content, []

    desc_block = _extract_fm_block(tr_fm, "description")
    if not desc_block or "リリースノートが含まれている" not in desc_block:
        return translated_content, []

    new_desc = desc_block.replace(
        "リリースノートが含まれている", "リリースノートが含まれています"
    )
    if new_desc == desc_block:
        return translated_content, []

    new_fm = tr_fm.replace(desc_block, new_desc, 1)
    return (
        f"---\n{new_fm}\n---\n{tr_body}",
        [
            "ja_releases_fm — description: リリースノートが含まれている → "
            "リリースノートが含まれています (polite です/ます stock phrase)"
        ],
    )


def _git_ls_files_docs_trees(repo_root):
    """Return tracked paths under documentation trees, or [] if not a git checkout."""
    git_dir = repo_root / ".git"
    if not git_dir.exists():
        return []
    try:
        proc = subprocess.run(
            [
                "git",
                "-C",
                str(repo_root),
                "ls-files",
                "-z",
                "--",
                "_docs/",
                "_includes/",
                "_lang/",
            ],
            capture_output=True,
            check=False,
            text=False,
        )
    except OSError:
        return []
    if proc.returncode != 0:
        return []
    out = []
    for chunk in proc.stdout.split(b"\0"):
        if not chunk:
            continue
        try:
            out.append(chunk.decode("utf-8"))
        except UnicodeDecodeError:
            continue
    return out


def _collect_path_case_collisions(repo_root):
    """Return groups of repo-relative paths that differ but match under casefold().

    Git on macOS/Windows treats these as one file; tracking both corrupts
    ``git status`` and can drop content. The merge job runs on Linux (two
    on-disk spellings are possible) **and** may run in a full git checkout.

    We union ``git ls-files`` with a filesystem walk so untracked overlays are
    visible before ``git add``. On case-insensitive volumes the same inode
    often appears under two spellings (index uses ``mparticle/…`` while
    ``iterdir`` reports ``mParticle/…``); those are **not** reported once only
    one spelling is tracked in Git. Multiple **tracked** paths for one casefold,
    or multiple **physical** files (distinct device/inode pairs), still fail
    (PR #13372 workflow).
    """
    git_paths = set(_git_ls_files_docs_trees(repo_root))
    by_cf = {}

    def _add(rel):
        by_cf.setdefault(rel.casefold(), set()).add(rel)

    for rel in git_paths:
        _add(rel)

    roots = [
        repo_root / "_docs",
        repo_root / "_includes",
    ]
    for info in LANGUAGES.values():
        roots.append(repo_root / "_lang" / info["dir"])

    for base in roots:
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            try:
                rel = path.relative_to(repo_root).as_posix()
            except ValueError:
                continue
            _add(rel)

    collisions = []
    for paths in by_cf.values():
        if len(paths) < 2:
            continue
        sorted_paths = sorted(paths)
        in_git = [p for p in sorted_paths if p in git_paths]
        if len(set(in_git)) > 1:
            collisions.append(sorted_paths)
            continue

        stat_pairs = []
        for rel in sorted_paths:
            fp = repo_root / rel
            if fp.is_file():
                st = fp.stat()
                stat_pairs.append((st.st_dev, st.st_ino))
        if len(stat_pairs) < 2:
            continue
        if len(set(stat_pairs)) > 1:
            collisions.append(sorted_paths)

    return collisions


def repair_img_alt_inner_german_low9_closing_quote(
    translated_path, translated_content
):
    """Fix ``alt="…„Word"…"`` where German low-9 quotes break the HTML attribute.

    Models sometimes use ``„…"`` inside a double-quoted ``alt``; the inner
    ASCII ``"`` closes ``alt`` early (Copilot PR #13319, pt-BR drag-and-drop).
    Replace inner ``„Segment"``-style pairs with ASCII single quotes.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/" not in rel or "„" not in translated_content:
        return translated_content, []
    if "<img" not in translated_content or "alt=\"" not in translated_content:
        return translated_content, []

    repairs = []
    lines = translated_content.split("\n")
    new_lines = []
    for line in lines:
        if "<img" in line and "alt=\"" in line and "„" in line:
            new_line = re.sub(r"„([^\"„]+)\"", r"'\1'", line)
            if new_line != line:
                repairs.append(
                    "img-alt — German „…\" inside double-quoted alt → ASCII quotes"
                )
            line = new_line
        new_lines.append(line)
    if not repairs:
        return translated_content, []
    return "\n".join(new_lines), repairs


def repair_de_email_setup_whitelabel_dkim_spf_phrasing(
    translated_path, translated_content, lang_key
):
    """Fix mistranslated *umgehen* (bypass) for DKIM/SPF auth checks on DE setup.

    English means senders **pass** DKIM/SPF checks via whitelabeling, not
    **circumvent** them (Copilot PR #13319).
    """
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/de/" not in rel or not rel.endswith("email_setup.md"):
        return translated_content, []
    needle = "Authentifizierungsprüfungen für DKIM und SPF umgehen"
    if needle not in translated_content:
        return translated_content, []
    new = translated_content.replace(
        needle,
        "Authentifizierungsprüfungen für DKIM und SPF bestehen",
        1,
    )
    return new, [
        "de-email_setup — DKIM/SPF umgehen → bestehen (pass auth checks)"
    ]


_IMAGE_BUSTER_PATH_FUSE_RE = re.compile(
    r"(\{\%\s*)image_buster/(?=\S)",
)


def repair_liquid_image_buster_path_spacing(translated_content):
    """Insert missing space before the path in ``{% image_buster/...`` tags.

    Liquid requires ``{% image_buster /assets/... %}``. Models sometimes emit
    ``image_buster/assets`` with no space, which breaks the tag (Copilot
    PR #13318).
    """

    def _repl(m: re.Match) -> str:
        return m.group(1) + "image_buster /"

    new, n = _IMAGE_BUSTER_PATH_FUSE_RE.subn(_repl, translated_content)
    if not n:
        return translated_content, []
    return new, [f"liquid — image_buster / path spacing ({n} occurrence(s))"]


def repair_markdown_table_double_leading_row_pipes(translated_content):
    """Remove an accidental extra ``|`` at the start of markdown table rows.

    Rows like ``|| Use case | Explanation |`` render an empty first column and
    break ``.reset-td-br-*`` table styling (Copilot PR #13392).
    """

    new, n = re.subn(r"(^|\n)\|\|(\|)", r"\1|\2", translated_content, flags=re.MULTILINE)
    if not n:
        return translated_content, []
    return new, [f"md-table — double leading pipe on table rows ({n}x; PR #13392)"]


def repair_yaml_guide_top_text_unquoted_html(translated_content):
    """Quote ``guide_top_text`` HTML blobs so attribute ``"`` do not break YAML.

    Values such as ``guide_top_text: <a href="https://...">`` truncate at the
    first inner double quote unless the whole value is YAML-quoted with inner
    quotes escaped (Copilot PR #13392).
    """
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []
    out_lines = []
    changed = False
    for line in tr_fm.split("\n"):
        m = re.match(r"^(guide_top_text:)\s*(.+)$", line)
        if not m:
            out_lines.append(line)
            continue
        key, raw = m.group(1), m.group(2)
        stripped = raw.strip()
        if stripped.startswith('"') or stripped.startswith("'"):
            out_lines.append(line)
            continue
        if stripped.startswith("<") and '"' in stripped:
            esc = stripped.replace("\\", "\\\\").replace('"', '\\"')
            out_lines.append(f'{key} "{esc}"')
            changed = True
        else:
            out_lines.append(line)
    if not changed:
        return translated_content, []
    new_fm = "\n".join(out_lines)
    return (
        f"---\n{new_fm}\n---\n{tr_body}",
        ["guide_top_text_fm — quoted HTML for YAML safety (PR #13392)"],
    )
_DECISIONING_AUDIENCE_DOC_SUFFIX = "brazeai/decisioning_studio/audience.md"

_OTHER_PLATFORMS_TAB_LABEL_BY_LANG = {
    "de": "Weitere Plattformen",
    "es": "Otras plataformas",
    "fr": "Autres plateformes",
    "ja": "その他のプラットフォーム",
    "ko": "다른 플랫폼",
    "pt-br": "Outras plataformas",
}


def repair_decisioning_audience_gcs_services_typo(translated_path, translated_content):
    """Replace *Google Cloud Services* with **Google Cloud Storage** on audience page.

    Export buckets for Decisioning Studio live on **Google Cloud Storage** (GCS).
    Models sometimes write the broader *Google Cloud Services* next to *bucket*
    wording (Copilot / auto-translate PR #13389). Scoped to this doc only.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_DECISIONING_AUDIENCE_DOC_SUFFIX):
        return translated_content, []
    if "Google Cloud Services" not in translated_content:
        return translated_content, []
    new = translated_content.replace("Google Cloud Services", "Google Cloud Storage")
    n = translated_content.count("Google Cloud Services")
    return new, [f"gcs-name — Google Cloud Services → Google Cloud Storage ({n}x; PR #13389)"]


def repair_decisioning_audience_other_platforms_tab(
    translated_path, translated_content, lang_key
):
    """Localize ``{% tab Other Platforms %}`` on Decisioning Studio audience page."""
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_DECISIONING_AUDIENCE_DOC_SUFFIX):
        return translated_content, []
    label = _OTHER_PLATFORMS_TAB_LABEL_BY_LANG.get(lang_key)
    if not label:
        return translated_content, []
    before = "{% tab Other Platforms %}"
    if before not in translated_content:
        return translated_content, []
    after = "{% tab " + label + " %}"
    new = translated_content.replace(before, after)
    return new, [f"decisioning-audience — tab Other Platforms → {label} (PR #13389)"]


# ``{% assign x = {{${user_id}}} | md5 %}`` — invalid (output tags inside assign).
_ASSIGN_NESTED_DEFAULT_IN_ASSIGN_RE = re.compile(
    r"\{%\s*assign\s+(\w+)\s*=\s*\{\{\s*(\$\{[^}]+\})\s*\}\}\s*\|\s*(\w+)\s*%\}",
    re.IGNORECASE,
)


def repair_liquid_assign_nested_default_in_output(translated_content):
    """Strip nested ``{{ }}`` around Braze default fields inside ``{% assign %}``.

    Models sometimes wrap ``${user_id}`` (and similar) as ``{{${user_id}}}`` on
    the right-hand side of ``{% assign … %}``, which is invalid Liquid (Copilot
    / auto-translate PR #13388).
    """

    def _repl(m: re.Match) -> str:
        return (
            "{% assign "
            + m.group(1)
            + " = "
            + m.group(2)
            + " | "
            + m.group(3)
            + " %}"
        )

    new, n = _ASSIGN_NESTED_DEFAULT_IN_ASSIGN_RE.subn(_repl, translated_content)
    if not n:
        return translated_content, []
    return new, [
        f"liquid — assign RHS: strip {{ }} around default field ({n}x; PR #13388)"
    ]


def repair_de_global_user_management_landing_titles(
    translated_path, translated_content, lang_key
):
    """Normalize DE **User management** hub compound (administer / global).

    ``Nutzer:in Verwaltung`` reads like two words; use the established compound
    **Nutzer:innenverwaltung** in nav and headers (Copilot PR #13318).
    """
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_user_guide/administer/global/user_management.md"):
        return translated_content, []
    needle = "Nutzer:in Verwaltung"
    if needle not in translated_content:
        return translated_content, []
    new = translated_content.replace(needle, "Nutzer:innenverwaltung")
    return new, [
        "de-user-mgmt-landing — Nutzer:in Verwaltung → Nutzer:innenverwaltung"
    ]


def repair_front_matter_miscapitalized_tool_key(content):
    """Normalize ``Tool:`` / ``Tool :`` to ``tool:`` in YAML front matter.

    Jekyll exposes ``page.tool`` from the lowercase key. A capitalized
    ``Tool`` key is a different identifier and skips tool taxonomy (Copilot /
    PR reviews on Canvas ``preview_user_paths`` and similar pages).
    """
    tr_fm, tr_body = _extract_front_matter(content)
    if not tr_fm:
        return content, []
    if not re.search(r"^Tool\s*:\s*", tr_fm, re.MULTILINE):
        return content, []
    repaired_fm = re.sub(r"^Tool\s*:", "tool:", tr_fm, flags=re.MULTILINE)
    if repaired_fm == tr_fm:
        return content, []
    new_content = f"---\n{repaired_fm}\n---\n{tr_body}"
    return new_content, ["front_matter — Tool: → tool: (Jekyll page.tool)"]


def _collect_guide_featured_list_field(block, field):
    """Return ordered list of ``link:`` or ``image:`` values in ``guide_featured_list``."""
    if not block:
        return []
    out = []
    for line in block.splitlines():
        m = re.match(rf"^\s+{re.escape(field)}:\s*(.+)$", line)
        if m:
            out.append(m.group(1).strip().strip("\"'"))
    return out


def repair_guide_featured_list_links(english_content, translated_content):
    """Sync ``link:`` (and ``image:`` when safe) under ``guide_featured_list`` to English.

    Display ``name`` values are often translated, so matching by list position is more
    reliable than matching by ``name`` text. Icon paths are locale-invariant assets;
    models sometimes alter or drop them—restore from English when counts match.
    """
    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not en_fm or not tr_fm:
        return translated_content, []

    en_block = _extract_fm_block(en_fm, "guide_featured_list")
    tr_block = _extract_fm_block(tr_fm, "guide_featured_list")
    if not en_block or not tr_block:
        return translated_content, []

    en_links = _collect_guide_featured_list_field(en_block, "link")
    tr_links = _collect_guide_featured_list_field(tr_block, "link")
    if len(en_links) != len(tr_links):
        return translated_content, [
            "guide_featured_list — link count mismatch "
            f"(English: {len(en_links)}, translated: {len(tr_links)}); skipped link sync"
        ]

    en_images = _collect_guide_featured_list_field(en_block, "image")
    tr_images = _collect_guide_featured_list_field(tr_block, "image")
    sync_images = (
        len(en_images) == len(tr_images) == len(en_links) and len(en_images) > 0
    )

    new_lines = []
    idx_link = 0
    idx_image = 0
    link_sync = 0
    image_sync = 0
    for line in tr_block.splitlines():
        m_link = re.match(r"^(\s+link:\s*)(.+)$", line)
        if m_link and idx_link < len(tr_links):
            want = en_links[idx_link]
            got = tr_links[idx_link]
            idx_link += 1
            if want != got:
                new_lines.append(m_link.group(1) + want)
                link_sync += 1
                continue
        if sync_images:
            m_img = re.match(r"^(\s+image:\s*)(.+)$", line)
            if m_img and idx_image < len(tr_images):
                want = en_images[idx_image]
                got = tr_images[idx_image]
                idx_image += 1
                if want != got:
                    new_lines.append(m_img.group(1) + want)
                    image_sync += 1
                    continue
        new_lines.append(line)

    if link_sync == 0 and image_sync == 0:
        return translated_content, []

    new_tr_block = "\n".join(new_lines)
    new_tr_fm = tr_fm.replace(tr_block, new_tr_block, 1)
    translated_content = f"---\n{new_tr_fm}\n---\n{tr_body}"
    parts = []
    if link_sync:
        parts.append(f"{link_sync} link(s)")
    if image_sync:
        parts.append(f"{image_sync} image path(s)")
    return translated_content, [
        "guide_featured_list — synced " + " and ".join(parts) + " from English"
    ]


def repair_pt_br_push_channel_token(translated_path, translated_content, lang_key):
    """Normalize Push channel YAML list item for Brazilian Portuguese under the Push hub.

    Sibling ``_lang/pt_br/_user_guide/channels/push`` pages use capitalized
    ``Push`` in ``channel:`` lists; MT sometimes emits lowercase ``push``,
    which triggers inconsistency reviews (Copilot / auto-translate PR #13393).
    Only front matter is scanned; lines must match ``- push`` exactly (leading
    whitespace + list marker + bare token).
    """
    if lang_key != "pt-br":
        return translated_content, []

    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "/_lang/pt_br/_user_guide/channels/push" not in rel:
        return translated_content, []

    fm, body = _extract_front_matter(translated_content)
    if not fm:
        return translated_content, []

    new_fm, n = re.subn(r"^(\s*)- push\s*$", r"\1- Push", fm, flags=re.MULTILINE)
    if not n:
        return translated_content, []

    return f"---\n{new_fm}\n---\n{body}", [
        f"pt_br channel — capitalized Push in YAML list ({n} line(s))",
    ]


def repair_es_api_obligatorio_typo(translated_path, translated_content, lang_key):
    """Normalize ``Obligatoria`` → ``Obligatorio`` in Spanish API parameter tables.

    MT sometimes uses the feminine form in the fixed ``| Parámetro | … |``
    column; sibling ES API pages use **Obligatorio** for that column (Copilot /
    auto-translate PR #13458).
    """
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "/_lang/es/_api/" not in rel:
        return translated_content, []
    if "Obligatoria" not in translated_content:
        return translated_content, []
    new_content, n = re.subn(
        r"(\|)\s*Obligatoria(\*?)\s*(\|)",
        r"\1 Obligatorio\2 \3",
        translated_content,
    )
    if not n:
        return translated_content, []
    return new_content, [
        f"es api — Obligatorio column/token repair ({n} occurrence(s))",
    ]


def repair_de_dashboard_capture_english_bleed(
    translated_path, translated_content, lang_key
):
    """Replace known English ``dashboard_match`` captures in DE includes.

    Alerts that interpolate ``{{ dashboard_match }}`` read poorly when the
    capture still uses English hyphen labels (Copilot / auto-translate PR
    #13458).
    """
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "/_lang/de/" not in rel or "/_includes/" not in rel:
        return translated_content, []
    if "dashboard_match" not in translated_content:
        return translated_content, []
    replacements = (
        (
            "{% capture dashboard_match %}Dashboard-Canvas-Analytics{% endcapture %}",
            "{% capture dashboard_match %}Canvas-Analytics im Dashboard{% endcapture %}",
        ),
        (
            "{% capture dashboard_match %}Dashboard-Engagement-Analytics{% endcapture %}",
            "{% capture dashboard_match %}Engagement-Analytics im Dashboard{% endcapture %}",
        ),
        (
            "{% capture dashboard_match %}dashboard Canvas analytics{% endcapture %}",
            "{% capture dashboard_match %}Canvas-Analytics im Dashboard{% endcapture %}",
        ),
        (
            "{% capture dashboard_match %}dashboard Engagement analytics{% endcapture %}",
            "{% capture dashboard_match %}Engagement-Analytics im Dashboard{% endcapture %}",
        ),
    )
    out = translated_content
    applied = 0
    for old, new_val in replacements:
        if old in out:
            out = out.replace(old, new_val)
            applied += 1
    if not applied:
        return translated_content, []
    return out, [
        f"de include — localized dashboard_match capture ({applied} block(s))",
    ]


def check_guide_featured_list_duplicate_links(
    english_content, translated_content, english_path="", translated_path=""
):
    """Emit QC warnings when ``guide_featured_list`` repeats the same ``link:``.

    Duplicate destinations produce two visually distinct cards pointing at one
    article (English source drift or bad MT). Fix by removing/editing rows in the
    **English** `_docs/` file — translation QC syncs routes from English
    (auto-translate / Copilot PR #13393).
    """
    warnings = []

    def _dupes(label, fm_fragment, filepath):
        if not fm_fragment:
            return
        block = _extract_fm_block(fm_fragment, "guide_featured_list")
        if not block:
            return
        links = _collect_guide_featured_list_field(block, "link")
        ctr = Counter(links)
        for link_val, cnt in ctr.items():
            if cnt <= 1 or not link_val:
                continue
            extras = filepath or "(path unknown)"
            warnings.append(
                "guide_featured_list — duplicate destination "
                f"({cnt}× link: {link_val}) in {label} ({extras})"
            )

    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, _ = _extract_front_matter(translated_content)
    _dupes("English source", en_fm, str(english_path))
    _dupes("translation", tr_fm, str(translated_path))
    return warnings


# English Braze dashboard strings that often leak into localized Agents docs
# when the model copies US UI labels verbatim. Keys: lang_key. Order is applied
# longest-first per file to reduce partial-match issues.
_AGENTS_EN_UI_COMMON = {
    "pt_br": [
        ("**Recalculate when catalog rows update**",
         "**Recalcular quando as linhas do catálogo forem atualizadas**"),
        ("**Apply AI agent**", "**Aplicar agente IA**"),
        ("**Response Field**", "**Campo de Resposta**"),
        ("**Cost estimation**", "**Estimativa de custo**"),
        ("**Add fields**", "**Adicionar campos**"),
        ("**Export CSV**", "**Exportar CSV**"),
        ("**Edit Item**", "**Editar Item**"),
        ("**Confirm**", "**Confirmar**"),
        ('"Apply AI agent"', '"Aplicar agente IA"'),
        ("'Apply AI agent'", "'Aplicar agente IA'"),
    ],
    "fr_fr": [
        ("**Recalculate when catalog rows update**",
         "**Recalculer lors de la mise à jour des lignes du catalogue**"),
        ("**Apply AI agent**", "**Appliquer l'agent IA**"),
        ("**Response Field**", "**Champ de réponse**"),
        ("**Cost estimation**", "**Estimation des coûts**"),
        ("**Add fields**", "**Ajouter des champs**"),
        ("**Export CSV**", "**Exporter CSV**"),
        ("**Edit Item**", "**Modifier l'élément**"),
        ("**Confirm**", "**Confirmer**"),
        ("« Apply AI agent »", "« Appliquer l'agent IA »"),
        ('"Apply AI agent"', '"Appliquer l\'agent IA"'),
    ],
    "ja": [
        ("**Recalculate when catalog rows update**",
         "**カタログ行の更新時に再計算**"),
        ("**Apply AI agent**", "**AIエージェントを適用**"),
        ("**Response Field**", "**応答フィールド**"),
        ("**Cost estimation**", "**コスト見積もり**"),
        ("**Add fields**", "**フィールドを追加**"),
        ("**Export CSV**", "**CSVをエクスポート**"),
        ("**Edit Item**", "**アイテムを編集**"),
        ("**Confirm**", "**確認**"),
        ("「Apply AI agent」", "「AIエージェントを適用」"),
        ('"Apply AI agent"', '"AIエージェントを適用"'),
    ],
}

# Short labels that are risky to replace outside the catalog deployment article.
_AGENTS_EN_UI_DEPLOYING_ONLY = {
    "pt_br": [
        ("**Usage**", "**Uso**"),
        ("**View**", "**Ver**"),
    ],
    "fr_fr": [
        ("**Usage**", "**Utilisation**"),
        ("**View**", "**Afficher**"),
    ],
    "ja": [
        ("**Usage**", "**使用状況**"),
        ("**View**", "**表示**"),
    ],
}


def repair_agents_catalog_en_ui(translated_path, translated_content, lang_key):
    """Fix US-English dashboard labels leaked into localized BrazeAI Agents docs."""
    rel = Path(translated_path).as_posix()
    if "/brazeai/agents/" not in rel and "brazeai/agents/" not in rel:
        return translated_content, []
    if "_lang/" not in rel:
        return translated_content, []
    if not rel.endswith(".md"):
        return translated_content, []

    basename = Path(translated_path).name
    pairs = list(_AGENTS_EN_UI_COMMON.get(lang_key, []))
    if basename == "deploying_agents.md":
        pairs.extend(_AGENTS_EN_UI_DEPLOYING_ONLY.get(lang_key, []))
    if not pairs:
        return translated_content, []

    pairs.sort(key=lambda item: len(item[0]), reverse=True)
    new_content = translated_content
    n = 0
    for old, new in pairs:
        if old in new_content:
            new_content = new_content.replace(old, new)
            n += 1
    if new_content == translated_content:
        return translated_content, []
    return new_content, [
        f"agents_catalog_ui — replaced {n} leaked EN UI string(s) for {lang_key}"
    ]


def repair_yaml_syntax(translated_content):
    """Validate YAML front matter and auto-fix common parse errors.

    Fixes:
    - German „...ASCII" → „...Unicode" (ASCII closing quote inside YAML strings)
    - Unquoted values containing colons (wraps in double quotes)
    """
    import yaml as _yaml

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    try:
        _yaml.safe_load(tr_fm)
        return translated_content, []
    except _yaml.YAMLError:
        pass

    repairs = []
    repaired_fm = tr_fm

    # Fix 1: German ASCII closing quotes — „(text)" where " is U+0022
    if "\u201e" in repaired_fm:
        fixed = re.sub(r'\u201e([^\u201e\u201c]*?)"', '\u201e\\1\u201c', repaired_fm)
        if fixed != repaired_fm:
            repaired_fm = fixed
            repairs.append("yaml_syntax — replaced ASCII closing quotes after „ with Unicode \u201c")

    # Fix 2: Unquoted values containing bare colons
    fixed_lines = []
    for line in repaired_fm.split("\n"):
        m = re.match(r'^(\s*(?:description|name|title|nav_title|article_title'
                     r'|guide_top_text|guide_top_header|glossary_top_header'
                     r'|glossary_top_text|glossary_filter_text'
                     r'|search_tag)):\s+(.+)$', line)
        if m:
            key_part, value = m.group(1), m.group(2)
            if not value.startswith('"') and ":" in value:
                escaped = value.replace("\\", "\\\\").replace('"', '\\"')
                line = f'{key_part}: "{escaped}"'
                repairs.append(f"yaml_syntax — quoted {key_part.strip()} (contains colon)")
        fixed_lines.append(line)
    repaired_fm = "\n".join(fixed_lines)

    if repairs:
        try:
            _yaml.safe_load(repaired_fm)
            translated_content = f"---\n{repaired_fm}\n---\n{tr_body}"
        except _yaml.YAMLError:
            repairs.append("yaml_syntax — auto-repair attempted but YAML still invalid")

    return translated_content, repairs


def _extract_code_blocks(content):
    """Extract fenced code blocks with positions."""
    pattern = re.compile(r'(^```[^\n]*\n)(.*?)(^```\s*$)', re.MULTILINE | re.DOTALL)
    return [
        (m.start(), m.end(), m.group(0), m.group(2))
        for m in pattern.finditer(content)
    ]


def repair_code_blocks(english_content, translated_content):
    """Replace translated code block contents with English originals."""
    en_blocks = _extract_code_blocks(english_content)
    tr_blocks = _extract_code_blocks(translated_content)

    if not en_blocks:
        return translated_content, []

    if len(en_blocks) != len(tr_blocks):
        return translated_content, [
            f"code_blocks — count mismatch (English: {len(en_blocks)}, "
            f"translated: {len(tr_blocks)}); skipped auto-repair"
        ]

    repairs = []
    repaired = translated_content
    for i in range(len(en_blocks) - 1, -1, -1):
        en_full = en_blocks[i][2]
        tr_full = tr_blocks[i][2]
        if en_full != tr_full:
            repaired = (
                repaired[:tr_blocks[i][0]] + en_full + repaired[tr_blocks[i][1]:]
            )
            repairs.append(f"code_block[{i}] — restored English content")

    return repaired, repairs


def _extract_md_link_urls(content):
    """Extract markdown link/image URLs in order."""
    return re.findall(r'\[(?:[^\]]*)\]\(([^)]+)\)', content)


# Kramdown/Jekyll: `.../page_slug#anchor-id` can fuse slug and fragment; use
# `.../page_slug/#anchor-id` when the slug is extensionless (not `file.md#`).
_MD_LINK_FRAGMENT_ANCHOR_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]*$")


def _normalize_single_internal_link_url(url):
    """If ``url`` is a ``{{site.baseurl}}`` doc link with ``/`` before ``#anchor``,
    remove the slash. Returns ``(new_url, changed)``.
    """
    if "{{site.baseurl}}" not in url:
        return url, False
    if "?" in url:
        return url, False
    hashidx = url.find("#")
    if hashidx <= 0:
        return url, False
    before, frag = url[:hashidx], url[hashidx + 1 :]
    if not frag or not before.endswith("/"):
        return url, False
    bl = before.lower()
    if bl.endswith((".md", ".html", ".htm", ".json", ".xml")):
        return url, False
    last_seg = before.rstrip("/").rsplit("/", 1)[-1]
    if "." in last_seg:
        return url, False
    if not _MD_LINK_FRAGMENT_ANCHOR_RE.match(frag):
        return url, False
    return f"{before.rstrip('/')}#{frag}", True


_SUP_BOLD_STAR_TYPO = re.compile(r"<sup>\*\*([^*<]+)\*</sup>")


def repair_sup_addon_footnote_bold_typo(translated_content: str):
    """Fix ``<sup>**text*</sup>`` copied from English (unbalanced ``**`` / ``*``).

    Models sometimes preserve a malformed footnote after channel tables; it
    breaks Markdown emphasis pairing in some pipelines (see Copilot on PR #13285).
    """
    new, n = _SUP_BOLD_STAR_TYPO.subn(
        lambda m: f"<sup>{m.group(1).strip()}</sup>", translated_content
    )
    if n:
        return new, [f"html-sup — normalized {n} add-on footnote(s) (removed **…*)"]
    return translated_content, []


def repair_ideas_and_strategies_internal_link_trailing_slash(translated_content: str):
    """Remove trailing ``/`` from ``ideas_and_strategies`` doc links."""
    repairs = []
    new = translated_content
    for wrong, right in (
        (
            "]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)",
            "]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)",
        ),
        (
            "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/)",
            "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)",
        ),
    ):
        if wrong in new:
            new = new.replace(wrong, right)
            repairs.append("md-link — ideas_and_strategies trailing / removed")
    if repairs:
        return new, repairs
    return translated_content, []


def repair_markdown_site_baseurl_link_paren_typos(translated_content: str):
    """Repair malformed ``{{site.baseurl}}`` Markdown links (extra parentheses).

    Models occasionally emit ``[label](({{site.baseurl}}/path`` instead of correct
    ``[label]({{site.baseurl}}/path`` (Copilot PR #13396). Run before
    ``repair_markdown_internal_link_fragments``.

    We intentionally do **not** collapse ``]({{site.baseurl}}/path))`` to a
    single ``)``: prose often wraps the link in parentheses, so the first ``)``
    closes the markdown link and the second closes the outer ``(…`` (for example
    ``unless they are [encrypted](url))``). A prior ``dup_pat`` rule stripped that
    outer close and broke list rendering (Cursor Bugbot / PR #13605).
    """
    repairs = []
    new = translated_content
    bad_open = "](" + "(" + "{{" + "site.baseurl}}"
    good_open = "](" + "{{" + "site.baseurl}}"
    if bad_open in new:
        n = new.count(bad_open)
        new = new.replace(bad_open, good_open)
        repairs.append(
            "md-link — removed extra '(' before {{site.baseurl}} "
            f"({n}x; PR #13396)"
        )
    if repairs:
        return new, repairs
    return translated_content, []


def repair_markdown_internal_link_fragments(content):
    """Normalize ``]({{site.baseurl}}/...slug/#anchor)`` → ``.../slug#anchor``."""
    repairs = []

    def repl(match):
        url = match.group(1)
        new_url, changed = _normalize_single_internal_link_url(url)
        if changed:
            preview = url if len(url) <= 100 else url[:97] + "..."
            repairs.append(
                f"md-fragment — removed '/' before # in internal link ({preview})"
            )
        return f"]({new_url})"

    new_content = re.sub(r"\]\(([^)]+)\)", repl, content)
    return new_content, repairs


# Missing `.` before second class breaks Kramdown table styling.
_RESET_TD_BR_IAL_MISSING_DOT = re.compile(
    r"\{\:\s*\.reset-td-br-1\s+reset-td-br-2\b"
)


_MD_TABLE_SEP_RE = re.compile(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$")
_IAL_LINE_RE = re.compile(r"^\s*\{:\s*[^}]*\}\s*$")
_RESET_TD_CLASS_RE = re.compile(r"\.reset-td-br-(\d+)")


def _dot_missing_reset_td_br_tokens_in_ial_lines(text: str) -> tuple[str, int]:
    """Insert ``.`` before ``reset-td-br-N`` tokens that lost their class dot.

    Models (and occasionally English) emit ``{: .reset-td-br-1 .reset-td-br-2
    .reset-td-br-3 reset-td-br-4}`` — the last token is missing its leading
    ``.``, so Kramdown does not apply the column class (Copilot / PR #13395).
    Only touches whole-line ``{:` … ``}`` IAL blocks.
    """
    lines = text.split("\n")
    total = 0
    out: list[str] = []
    for line in lines:
        if "{:" not in line or "reset-td-br-" not in line:
            out.append(line)
            continue
        if not _IAL_LINE_RE.match(line):
            out.append(line)
            continue
        new_line, n = re.subn(r"(\s)(reset-td-br-\d+)", r"\1.\2", line)
        total += n
        out.append(new_line)
    if not total:
        return text, 0
    new_text = "\n".join(out)
    if text.endswith("\n") and not new_text.endswith("\n"):
        new_text += "\n"
    return new_text, total


def _count_md_table_cells(line):
    """Count cells in a markdown table row (header/body/separator)."""
    s = line.strip()
    if not s.startswith("|") or not s.endswith("|"):
        return 0
    inner = s[1:-1]
    return len([c for c in inner.split("|")])


def _rebuild_md_separator(header_cols, original_sep):
    """Return a separator row with ``header_cols`` cells, preserving each
    original cell's alignment marker where available."""
    s = original_sep.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells = [c.strip() or "---" for c in s.split("|")]
    if len(cells) < header_cols:
        cells.extend(["---"] * (header_cols - len(cells)))
    else:
        cells = cells[:header_cols]
    return "| " + " | ".join(cells) + " |"


def _clamp_reset_td_br_ial(ial_line, header_cols):
    """Remove ``.reset-td-br-N`` classes where ``N > header_cols``.

    Returns ``(new_line, removed_count)``.
    """
    removed = 0

    def repl(match):
        nonlocal removed
        n = int(match.group(1))
        if n > header_cols:
            removed += 1
            return ""
        return match.group(0)

    new = _RESET_TD_CLASS_RE.sub(repl, ial_line)
    if removed:
        new = re.sub(r" +", " ", new)
        new = re.sub(r"\s+\}", " }", new)
    return new, removed


def repair_markdown_double_leading_pipe_table_rows(content: str):
    """Replace ``||`` at the start of markdown table rows with ``|``.

    Models sometimes emit ``|| cell | cell |`` (Copilot on auto-translate
    PR #13398), which reads as an extra empty leading column. Skips lines
    inside fenced code blocks (`` ``` `` / ``~~~``) so shell ``||`` and
    similar aren't touched.
    """
    lines = content.splitlines()
    in_fence = False
    fence_delim = None
    fixed = 0
    out = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") and (fence_delim in (None, "```")):
            in_fence = not in_fence
            fence_delim = "```" if in_fence else None
            out.append(line)
            continue
        if stripped.startswith("~~~") and (fence_delim in (None, "~~~")):
            in_fence = not in_fence
            fence_delim = "~~~" if in_fence else None
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = re.match(r"^(\s*(?:>\s*)*)\|\|(.+)$", line)
        if m:
            rest = m.group(2)
            if "|" in rest:
                line = m.group(1) + "|" + rest
                fixed += 1
        out.append(line)
    if not fixed:
        return content, []
    result = "\n".join(out)
    if content.endswith("\n"):
        result += "\n"
    return result, [
        f"md-table — normalized {fixed} double-leading-pipe row(s) (||→|)"
    ]


def repair_html_href_space_before_liquid_open(content: str) -> tuple[str, list]:
    r"""Remove stray whitespace between ``href``\ 's opening quote and ``{%``.

    Copilot on auto-translate PR #13398 flagged ``href=" {% landing_page_url``
    in HTML-in-Markdown examples — the space breaks the attribute value.
    Also covers single-quoted ``href=`` and optional Liquid whitespace
    control ``{%-``.
    """
    new, n = re.subn(
        r"href=(['\"])\s+(\{\%-?)",
        r"href=\1\2",
        content,
    )
    if n:
        return new, [
            f"html-href — removed {n} stray space(s) before Liquid in href=…"
        ]
    return content, []


def repair_redirect_to_trailing_stray_quote_unquoted_url(
    translated_path: str, translated_content: str
) -> tuple[str, list]:
    r"""Remove a stray ``"`` after an unquoted ``redirect_to`` URL.

    Invalid pattern: ``redirect_to: https://example.com/path/"`` (opening
    quote missing — YAML breaks). Copilot flagged this across locales on
    auto-translate PR #13405. Scoped to ``_docs_pages/redirects/`` paths only.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_docs_pages/redirects/" not in rel:
        return translated_content, []
    new, n = re.subn(
        r"^(redirect_to:\s*https://[^\s\"\n]+)/\"\s*$",
        r"\1/",
        translated_content,
        flags=re.MULTILINE,
    )
    if n:
        return new, [
            f"yaml-redirect_to — removed {n} stray trailing quote(s) on unquoted URL"
        ]
    return translated_content, []


_REDIRECT_FM_FUSED_CLOSE_RE = re.compile(
    r"^(redirect_to:\s*https://[^\n]+)/---\s*$",
    re.MULTILINE,
)


def repair_redirect_front_matter_fused_close_delimiter(
    translated_path: str, translated_content: str
) -> tuple[str, list]:
    r"""Split ``redirect_to: …/---`` when the closing ``---`` was fused onto the URL line.

    Auto-translate PR #13405 / Copilot follow-up: invalid front matter breaks
    Jekyll and redirect-list validation. Scoped to ``_docs_pages/redirects/``.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_docs_pages/redirects/" not in rel:
        return translated_content, []
    new, n = _REDIRECT_FM_FUSED_CLOSE_RE.subn(
        r"\1/\n---\n",
        translated_content,
    )
    if n:
        return new, [
            f"yaml-fm — split {n} fused redirect_to/--- closing fence(s)"
        ]
    return translated_content, []


def repair_markdown_table_column_count(content):
    """Repair markdown tables whose separator row's cell count doesn't match
    the header row's cell count (and prune trailing ``.reset-td-br-N`` IAL
    classes that reference non-existent columns).

    The LLM was asked to preserve table shape verbatim, so when the English
    source itself has the mismatch (see PR #13302 / product_blocks.md static
    product block: 2-col header with ``| --- | --- | --- |`` separator and a
    ``.reset-td-br-3`` IAL), the bug rides into every locale. This repair
    fixes it deterministically in post-processing.

    Skips lines inside fenced code blocks (``\u200b```...\u200b```\u200b`` /
    ``~~~...~~~``) so pipe-table-looking example rows inside code fences
    (``curl -X POST ... | jq .``, SQL ``|`` unions, shell pipelines)
    aren't treated as real tables and have their structure mutated.
    Copilot flagged this gap on PR #13303 — the repair previously ran
    purely line-wise and could have rewritten example code after
    ``repair_code_blocks`` restored it.
    """
    lines = content.splitlines()
    repairs = []
    total = len(lines)
    i = 0
    in_fence = False
    fence_delim = None
    while i < total - 1:
        cur = lines[i]
        stripped = cur.strip()
        # Match both ``\u200b```\u200b`` and ``~~~`` fence delimiters. The
        # existing ``_CODE_FENCE_OPEN_RE`` only covers backticks, so track
        # both here locally to stay robust against ``~~~`` fences that show
        # up in a few of the `_api/` pages.
        if stripped.startswith("```") and (fence_delim in (None, "```")):
            in_fence = not in_fence
            fence_delim = "```" if in_fence else None
            i += 1
            continue
        if stripped.startswith("~~~") and (fence_delim in (None, "~~~")):
            in_fence = not in_fence
            fence_delim = "~~~" if in_fence else None
            i += 1
            continue
        if in_fence:
            i += 1
            continue

        nxt = lines[i + 1]
        if (
            stripped.startswith("|")
            and stripped.endswith("|")
            and not _MD_TABLE_SEP_RE.match(cur)
            and _MD_TABLE_SEP_RE.match(nxt)
        ):
            header_cols = _count_md_table_cells(cur)
            sep_cols = _count_md_table_cells(nxt)
            if header_cols > 0 and header_cols != sep_cols:
                lines[i + 1] = _rebuild_md_separator(header_cols, nxt)
                repairs.append(
                    f"md-table — separator cols {sep_cols}→{header_cols}"
                )
            # Scan forward through body rows to find the IAL (if any).
            j = i + 2
            while j < total and lines[j].strip().startswith("|"):
                j += 1
            if header_cols > 0 and j < total and _IAL_LINE_RE.match(lines[j]):
                new_ial, removed = _clamp_reset_td_br_ial(lines[j], header_cols)
                if removed:
                    lines[j] = new_ial
                    repairs.append(
                        f"md-ial — trimmed {removed} stale .reset-td-br-N "
                        f"class(es) past column {header_cols}"
                    )
            i = j
        else:
            i += 1
    if repairs:
        result = "\n".join(lines)
        if content.endswith("\n"):
            result += "\n"
        return result, repairs
    return content, []


_INTERNAL_LINK_URL_RE = re.compile(r"\]\(([^)]+)\)")
_SLASH_SKIP_EXTS = (
    ".md", ".html", ".htm", ".json", ".xml", ".png", ".jpg", ".jpeg",
    ".gif", ".svg", ".pdf", ".txt", ".yaml", ".yml", ".csv",
)


def _normalize_trailing_slash_on_baseurl(url):
    """Remove trailing ``/`` from extensionless ``{{site.baseurl}}`` doc links.

    Production URLs omit trailing slashes (Vercel ``trailingSlash: false``).
    """
    if "{{site.baseurl}}" not in url:
        return url, False
    if "?" in url or "#" in url:
        return url, False
    if not url.endswith("/"):
        return url, False
    if url.rstrip().endswith("}}"):
        return url, False
    idx = url.find("{{site.baseurl}}")
    tail = url[idx + len("{{site.baseurl}}") :]
    if not tail or not tail.startswith("/"):
        return url, False
    last_seg = tail.rstrip("/").rsplit("/", 1)[-1]
    if not last_seg:
        return url, False
    lower = last_seg.lower()
    if any(lower.endswith(ext) for ext in _SLASH_SKIP_EXTS):
        return url, False
    if "." in last_seg:
        return url, False
    return url.rstrip("/"), True


def repair_markdown_internal_link_trailing_slash(content):
    """Remove trailing ``/`` from extensionless ``{{site.baseurl}}`` directory-style links."""
    repairs = []
    counts = {}

    def repl(match):
        url = match.group(1)
        new_url, changed = _normalize_trailing_slash_on_baseurl(url)
        if changed:
            counts[url] = counts.get(url, 0) + 1
        return f"]({new_url})"

    new = _INTERNAL_LINK_URL_RE.sub(repl, content)
    if counts:
        total = sum(counts.values())
        distinct = len(counts)
        repairs.append(
            f"md-link — removed trailing / from {total} directory-style "
            f"{{{{site.baseurl}}}} link(s) ({distinct} distinct path(s))"
        )
        return new, repairs
    return content, []


def repair_korean_query_hangul_typo(translated_path, translated_content, lang_key):
    """Replace **퀴리** with **쿼리** in Korean locale Markdown.

    Technical Korean borrows English *query* as **쿼리** (U+CFDC U+B9AC).
    A long-lived ``scripts/glossaries/ko.json`` row mapped *Query Builder*
    to **퀴리 빌더**, so the approved-terminology table pushed the wrong
    hangul into prompts and the model mirrored it across analytics docs
    until Copilot flagged it on PR #13311. A plain ``str.replace`` is
    safe here: **퀴리** is not a standard morpheme in this corpus — every
    hit is the same *query* typo class.

    Only runs when ``lang_key`` is ``ko`` and the path lives under
    ``_lang/ko/``.
    """
    if lang_key != "ko":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ko/" not in rel:
        return translated_content, []
    if "퀴리" not in translated_content:
        return translated_content, []
    n = translated_content.count("퀴리")
    new = translated_content.replace("퀴리", "쿼리")
    return new, [
        f"ko-query-hangul — normalized {n} mistransliterated "
        f"퀴리→쿼리 (English *query* in Korean IT prose)"
    ]


# Latin SDK / feature tokens and localized JA product names immediately
# followed by a Japanese particle should not have an ASCII space in between.
_JA_LATIN_TOKEN_PARTICLE_RE = re.compile(
    r"(?P<tok>"
    r"Content Cards|In-App Messages|REST API|SDK|"
    r"キャンペーン|キャンバス|セグメント"
    r")\s+(?P<particle>[をのとはがも])"
)

_JA_EN_CAMPAIGN_CANVAS_SEGMENT_TERMS = (
    "Campaign",
    "Campaigns",
    "Canvas",
    "Canvases",
    "Segment",
    "Segments",
)

# Preserve English Liquid tab labels and multi-word UI strings during token repair.
_JA_PROTECTED_ENGLISH_PHRASES = (
    "Save Campaign",
    "{% tab Campaigns %}",
    "{% tab Canvas %}",
    "{% tab Segments %}",
)


def _mask_ja_protected_english_phrases(chunk: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}
    for i, phrase in enumerate(_JA_PROTECTED_ENGLISH_PHRASES):
        if phrase not in chunk:
            continue
        token = f"__JA_PHRASE_PROTECT_{i}__"
        chunk = chunk.replace(phrase, token)
        placeholders[token] = phrase
    return chunk, placeholders


def _unmask_ja_protected_english_phrases(
    chunk: str, placeholders: dict[str, str]
) -> str:
    for token, phrase in placeholders.items():
        chunk = chunk.replace(token, phrase)
    return chunk


def _ja_campaign_canvas_segment_replacement_pairs():
    """Longest-first ``(english, japanese)`` pairs for Campaign/Canvas/Segment repair."""
    glossary_path = GLOSSARY_DIR / "ja.json"
    raw = (
        json.loads(glossary_path.read_text())
        if glossary_path.exists()
        else {}
    )
    pairs = []
    for en, ja in raw.items():
        if not ja or en == ja:
            continue
        if not re.search(r"[ぁ-んァ-ン一-龥]", ja):
            continue
        if not re.search(r"(?i)(campaign|canvas|segment)", en):
            continue
        # Lowercase single tokens (``campaign``, ``canvas``, ``segment``) appear
        # inside URL slugs and anchor IDs — only Title Case + multi-word UI.
        if " " not in en and en[:1].islower():
            continue
        pairs.append((en, ja))
    for en, ja in (
        ("Canvases", "キャンバス"),
        ("Campaigns", "キャンペーン"),
        ("Segments", "セグメント"),
        ("Canvas", "キャンバス"),
        ("Campaign", "キャンペーン"),
        ("Segment", "セグメント"),
    ):
        pairs.append((en, ja))
    seen = set()
    out = []
    for en, ja in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        if en in seen:
            continue
        seen.add(en)
        out.append((en, ja))
    return out


def _replace_ja_product_terms_in_text_segment(segment, pairs):
    """Apply glossary replacements outside code fences, URLs, and ``{#anchors}``."""

    def _replace_plain(chunk: str) -> str:
        chunk, protected = _mask_ja_protected_english_phrases(chunk)
        for en, ja in pairs:
            if re.search(r"\s", en):
                chunk = chunk.replace(en, ja)
            else:
                chunk = re.sub(
                    rf"(?<![A-Za-z/_-]){re.escape(en)}(?![A-Za-z/_-])",
                    ja,
                    chunk,
                )
        return _unmask_ja_protected_english_phrases(chunk, protected)

    parts = re.split(r"(\{#[^}]+\})", segment)
    out: list[str] = []
    for part in parts:
        if part.startswith("{#") and part.endswith("}"):
            out.append(part)
            continue

        def _fix_link(m: re.Match) -> str:
            return f"[{_replace_plain(m.group(1))}]({m.group(2)})"

        part = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", _fix_link, part)
        out.append(_replace_plain(part))
    return "".join(out)


def repair_japanese_english_product_terms(
    translated_path, translated_content, lang_key
):
    """Replace English Campaign/Canvas/Segment tokens with JA glossary forms.

    JA docs historically kept Title Case product nouns in English via
    ``PROTECTED_PRODUCT_TERMS``; partner review (2026-06) expects
    **キャンペーン** / **キャンバス** / **セグメント** in prose and UI
  labels where ``ja.json`` defines a translation.
    """
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ja/" not in rel:
        return translated_content, []

    pairs = _ja_campaign_canvas_segment_replacement_pairs()
    fm_match = re.match(
        r"^([ \t]*---\s*\n.*?\n---[ \t]*(?:\n|\Z))",
        translated_content,
        re.DOTALL,
    )
    if fm_match:
        prefix = fm_match.group(1)
        body = translated_content[fm_match.end() :]
    else:
        prefix = ""
        body = translated_content
    parts = re.split(r"(```.*?```)", body, flags=re.DOTALL)
    for i in range(0, len(parts), 2):
        parts[i] = _replace_ja_product_terms_in_text_segment(parts[i], pairs)
    new = prefix + "".join(parts)
    if new == translated_content:
        return translated_content, []
    return new, [
        "ja-product-terms — replaced English Campaign/Canvas/Segment "
        "with glossary Japanese forms"
    ]


def check_japanese_english_product_terms_in_prose(
    translated_path, translated_content, lang_key
):
    """Warn when JA docs still use English Campaign/Canvas/Segment in prose."""
    if lang_key != "ja":
        return []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ja/" not in rel:
        return []
    # API/event schema pages intentionally keep English field tokens.
    if any(
        part in rel
        for part in (
            "/_api/",
            "/event_glossary/",
            "/_includes/snowflake_users_messages/",
        )
    ):
        return []

    _, body = _extract_front_matter(translated_content)
    parts = re.split(r"(```.*?```)", body, flags=re.DOTALL)
    prose = "".join(parts[i] for i in range(0, len(parts), 2))
    warnings = []
    for term in _JA_EN_CAMPAIGN_CANVAS_SEGMENT_TERMS:
        matches = re.findall(
            rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])",
            prose,
        )
        if matches:
            warnings.append(
                f"ja-product-terms — English '{term}' appears {len(matches)}x "
                f"in prose; use glossary Japanese (キャンペーン/キャンバス/セグメント)"
            )
    return warnings


def repair_japanese_latin_token_particle_spacing(
    translated_path, translated_content, lang_key
):
    """Collapse ``Token を`` → ``Tokenを`` for common Latin tokens in JA docs.

    Only ``lang_key == "ja"`` and paths under ``_lang/ja/``. Longer tokens are
    listed first inside the alternation so ``Content Cards`` wins over
    ``Content``-style false paths (not in the set anyway).
    """
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ja/" not in rel:
        return translated_content, []

    new, n = _JA_LATIN_TOKEN_PARTICLE_RE.subn(
        lambda m: m.group("tok") + m.group("particle"),
        translated_content,
    )
    if n:
        return new, [
            f"ja-latin-particle — removed {n} ASCII space(s) between "
            f"Latin product/SDK token and Japanese particle (を/の/…)"
        ]
    return translated_content, []


def repair_pt_br_german_low9_double_quote_in_body(
    translated_path, translated_content, lang_key
):
    r"""Replace German low-9 „ (U+201E) with ASCII ``"`` in pt-BR Markdown.

    The model sometimes pastes German opening quotes into Brazilian
    Portuguese image alts and pairs them with ASCII straight closers
    (Copilot on PR #13314). For nested quoted email/UI copy inside
    ``![...](...)``, pt-BR docs expect straight ASCII ``"`` pairs — not ``„``.
    """
    if lang_key != "pt-br":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/pt_br/" not in rel:
        return translated_content, []
    low9 = "\u201e"
    if low9 not in translated_content:
        return translated_content, []
    n = translated_content.count(low9)
    new = translated_content.replace(low9, '"')
    return new, [
        f"pt-br-quotes — replaced {n} German „ (U+201E) with ASCII \" "
        f"in pt-BR doc"
    ]


def repair_pt_br_subscribed_default_subscription_group_label(
    translated_content, lang_key
):
    """Normalize the default global email subscription group bold label.

    The pt-BR glossary historically mapped ``Subscribed``→*Inscreveu-se*;
    dashboards and sibling docs keep English **Subscribed** for that literal
    product token. Fix the recurring phrase that bolds the wrong token next
    to *grupo de inscrições global* (Copilot / auto-translate PR #13399).
    """
    if lang_key != "pt-br":
        return translated_content, []

    needle = "grupo de inscrições global **Inscreveu-se**"
    if needle not in translated_content:
        return translated_content, []

    replaced = translated_content.replace(
        needle,
        "grupo de inscrições global **Subscribed**",
    )
    return replaced, [
        "pt_br subscriptions — restored **Subscribed** for global group label",
    ]


_CDI_SEGMENTS_DOC_SUFFIX = "segment_extension/cdi_segments.md"
_CDI_LOCATION_DESC_SNIPPETS = (
    "Location targeting",
    "ロケーションターゲティング",
    "ciblage par localisation, vous permettant",
    "위치 타겟팅을 설정",
    "direcionamento por local",
)
_CDI_DESCRIPTION_REPLACEMENT_LINE = {
    "ja": (
        'description: "この記事では、クラウドデータ取り込み（CDI）を使った CDI セグメント'
        'エクステンションについて、データウェアハウスへのクエリと Braze でのオーディエンス定義の方法を説明します。"'
    ),
    "fr": (
        "description: \"Cet article explique comment les extensions de segments CDI "
        "s'appuient sur l'ingestion de données cloud pour interroger votre entrepôt "
        'de données et définir des audiences dans Braze."'
    ),
    "ko": (
        'description: "이 문서에서는 클라우드 데이터 수집(CDI)을 사용하는 CDI 세그먼트 확장을 통해 '
        '데이터 웨어하우스를 쿼리하고 Braze에서 오디언스를 정의하는 방법을 설명합니다."'
    ),
    "pt-br": (
        "description: \"Este artigo explica como as extensões de segmento CDI usam a ingestão de dados "
        'na nuvem para consultar seu data warehouse e definir públicos na Braze."'
    ),
}


def repair_cdi_segments_description_location_drift(
    english_content, translated_content, translated_path, lang_key
):
    """Replace legacy ``location targeting`` copy in ``cdi_segments`` YAML ``description``.

    English briefly shipped the wrong ``description``; several locales mirrored it
    (Copilot / auto-translate PR #13387). When the English file clearly describes
    CDI + Cloud Data Ingestion and the localized front matter still contains
    known location-targeting boilerplate, rewrite ``description`` to the canonical
    sentence for that locale.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_CDI_SEGMENTS_DOC_SUFFIX):
        return translated_content, []
    if "Cloud Data Ingestion" not in english_content:
        return translated_content, []

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    if not any(s in tr_fm for s in _CDI_LOCATION_DESC_SNIPPETS):
        return translated_content, []

    replacement_line = _CDI_DESCRIPTION_REPLACEMENT_LINE.get(lang_key)
    if not replacement_line:
        return translated_content, []

    new_lines = []
    changed = False
    for line in tr_fm.split("\n"):
        if line.startswith("description:") and any(s in line for s in _CDI_LOCATION_DESC_SNIPPETS):
            new_lines.append(replacement_line)
            changed = True
        else:
            new_lines.append(line)
    if not changed:
        return translated_content, []

    new_fm = "\n".join(new_lines)
    return (
        f"---\n{new_fm}\n---\n{tr_body}",
        ["cdi_segments_fm — description topic drift (location → CDI; PR #13387)"],
    )


_RFM_SEGMENTS_DOC_SUFFIX = "sql_segments/rfm_segments.md"


def repair_rfm_sql_segments_nav_and_title_mix(
    translated_path, translated_content, lang_key
):
    """Normalize RFM SQL segment extension titles that mix English ``Segments`` into Romance/KO chrome.

    Copilot on PR #13387: ``nav_title`` / H1 sometimes keep ``Segments RFM`` or
    raw ``RFM Segments`` instead of locale nouns while the rest of the page is
    localized. Preserve explicit ``{#…}`` anchors on heading lines.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_RFM_SEGMENTS_DOC_SUFFIX):
        return translated_content, []

    repairs = []
    new = translated_content

    if lang_key == "pt-br":
        if 'nav_title: "Segments RFM"' in new:
            new = new.replace('nav_title: "Segments RFM"', 'nav_title: "Segmentos RFM"')
            repairs.append("pt-br-rfm — nav_title Segments RFM → Segmentos RFM (PR #13387)")
        if "# Segments SQL RFM {#" in new:
            new = new.replace("# Segments SQL RFM {#", "# Segmentos RFM {#")
            repairs.append("pt-br-rfm — H1 Segments SQL RFM → Segmentos RFM (PR #13387)")
    elif lang_key == "es":
        if 'nav_title: "Segments RFM"' in new:
            new = new.replace('nav_title: "Segments RFM"', 'nav_title: "Segmentos RFM"')
            repairs.append("es-rfm — nav_title Segments RFM → Segmentos RFM (PR #13387)")
        if "# Segments SQL RFM {#" in new:
            new = new.replace("# Segments SQL RFM {#", "# Segmentos RFM {#")
            repairs.append("es-rfm — H1 Segments SQL RFM → Segmentos RFM (PR #13387)")
    elif lang_key == "ko":
        if 'nav_title: "RFM Segments"' in new:
            new = new.replace('nav_title: "RFM Segments"', 'nav_title: "RFM 세그먼트"')
            repairs.append("ko-rfm — nav_title RFM Segments → RFM 세그먼트 (PR #13387)")
        if "# RFM SQL Segments" in new:
            before_h1 = new
            new = new.replace("# RFM SQL Segments {#", "# RFM SQL 세그먼트 {#")
            new = new.replace("# RFM SQL Segments\n", "# RFM SQL 세그먼트\n")
            if new != before_h1:
                repairs.append("ko-rfm — H1 RFM SQL Segments → RFM SQL 세그먼트 (PR #13387)")

    if new == translated_content:
        return translated_content, []
    return new, repairs


def repair_pt_br_analytics_product_menu_label(
    translated_path, translated_content, lang_key
):
    r"""Normalize Braze dashboard **Analytics** chrome in pt-BR Markdown.

    English navigation uses the product label **Analytics** (for example
    ``**Analytics** > **Report Builder (New)**``). Models sometimes render the
    parent menu as ``**Análise de dados**``, which drifts from sibling pt-BR
    analytics docs and in-product wording (Copilot / auto-translate PR #13386).
    Only high-confidence UI fragments are rewritten — not headings that use
    *Análise de dados* as a generic section title.
    """
    if lang_key != "pt-br":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/pt_br/" not in rel:
        return translated_content, []

    pairs = (
        (
            "navegue até a página **Análise de dados** da",
            "navegue até a página **Analytics** da",
        ),
        (
            "diretamente na página **Análise de dados** da",
            "diretamente na página **Analytics** da",
        ),
        (
            "até a página **Análise de dados** da",
            "até a página **Analytics** da",
        ),
        ("**Análise de dados** >", "**Analytics** >"),
        (
            "exibida na página **Análise de dados**",
            "exibida na página **Analytics**",
        ),
        ("seção **Análise de dados**", "seção **Analytics**"),
        ("| **Análise de dados** |", "| **Analytics** |"),
        ("* **Análise de dados**:", "* **Analytics**:"),
    )

    repairs = []
    new = translated_content
    for old, rep in pairs:
        if old not in new:
            continue
        c = new.count(old)
        new = new.replace(old, rep)
        repairs.append(
            "pt-br-analytics-menu — "
            f"{old[:48]}{'…' if len(old) > 48 else ''} → **Analytics** ({c}x; PR #13386)"
        )

    if new == translated_content:
        return translated_content, []
    return new, repairs


def repair_managing_segments_tool_yaml_value(translated_path, translated_content, _lang_key):
    r"""Restore canonical ``tool: Segments`` when YAML was corrupted to ``segmentos``.

    Models sometimes lowercase the ``tool`` taxonomy value after bulk prose edits
    (Copilot / auto-translate PR #13387). ``tool`` must stay the English token
    ``Segments`` for layout filters.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_user_guide/audience/segments/managing_segments.md"):
        return translated_content, []

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    new_fm, n = re.subn(
        r"(?im)^tool:\s*segmentos\s*$",
        "tool: Segments",
        tr_fm,
    )
    if not n:
        return translated_content, []

    return (
        f"---\n{new_fm}\n---\n{tr_body}",
        [f"managing_segments_fm — tool: segmentos → Segments ({n}x; PR #13387)"],
    )


def repair_japanese_mixed_mail_campaign(
    translated_path, translated_content, lang_key
):
    """Normalize ``メール Campaign`` → ``メールキャンペーン`` in Japanese docs.

    Glossary keeps **Campaign** / **Campaigns** in English for product UI, but
    ``メール`` + English ``Campaign`` reads as half-translated; Copilot on PR
    #13314 asked for **メールキャンペーン** (or **Eメールキャンペーン**) for the
    email-campaign *concept* in running Japanese sentences.
    """
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ja/" not in rel:
        return translated_content, []
    needle = "メール Campaign"
    if needle not in translated_content:
        return translated_content, []
    n = translated_content.count(needle)
    new = translated_content.replace(needle, "メールキャンペーン")
    return new, [
        f"ja-mail-campaign — normalized {n} メール Campaign→メールキャンペーン"
    ]


def repair_de_email_use_cases_social_heading(
    translated_path, translated_content, lang_key
):
    """Align DE ``channels/email/use_cases`` Social heading with EN + sibling.

    English and ``message_building_by_channel/.../use_cases.md`` use
    ``## Social``; the channels mirror had ``## Social Media`` (Copilot on
    PR #13314), which breaks anchor parity with the established DE page.
    """
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/de/_user_guide/channels/email/use_cases.md"):
        return translated_content, []
    if "## Social Media" not in translated_content:
        return translated_content, []
    new = translated_content.replace("## Social Media", "## Social", 1)
    return new, [
        "de-email-use-cases — ## Social Media → ## Social (match EN + sibling)"
    ]


_GENERATIVE_AI_IMAGES_MD = "brazeai/generative_ai/images.md"


def repair_generative_ai_images_english_flow_bold(
    translated_path, translated_content, lang_key
):
    """Replace vestigial English bold UI labels in localized ``images.md``.

    English source uses **AI Image Generator** / **Generate Images** in
    numbered steps; Copilot on PR #13313 flagged FR/ES/pt-BR pages that left
    those strings in US English while the rest of the page was translated.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_GENERATIVE_AI_IMAGES_MD):
        return translated_content, []

    pairs_by_lang = {
        "fr": (
            ("**AI Image Generator**", "**Générateur d'images IA**"),
            ("**Generate Images**", "**Générer des images**"),
            ("**Générer des images.**", "**Générer des images**"),
        ),
        "es": (
            ("**AI Image Generator**", "**Generador de imágenes con IA**"),
            ("**Generate Images**", "**Generar imágenes**"),
        ),
        "pt-br": (
            ("**AI Image Generator**", "**Gerador de imagens por IA**"),
            ("**IA Image Generator**", "**Gerador de imagens por IA**"),
            ("**Generate Images**", "**Gerar imagens**"),
            ("**Gerar Imagens**", "**Gerar imagens**"),
        ),
    }
    pairs = pairs_by_lang.get(lang_key)
    if not pairs:
        return translated_content, []

    repairs = []
    new = translated_content
    for old, repl in pairs:
        if old in new:
            c = new.count(old)
            new = new.replace(old, repl)
            repairs.append(f"gen-ai-images — {old} → {repl} ({c}×)")
    if repairs:
        return new, repairs
    return translated_content, []


def repair_fr_generative_images_download_tooltip_article(
    translated_path, translated_content, lang_key
):
    r"""Fix missing indefinite article in FR download ``title=`` string.

    ``Ajouter image à la bibliothèque…`` is ungrammatical; Copilot on PR
    #13313 asked for ``Ajouter une image à la bibliothèque…``.
    """
    if lang_key != "fr":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_GENERATIVE_AI_IMAGES_MD):
        return translated_content, []
    old = 'title="Ajouter image à la bibliothèque multimédia"'
    new = 'title="Ajouter une image à la bibliothèque multimédia"'
    if old not in translated_content:
        return translated_content, []
    return translated_content.replace(old, new, 1), [
        "fr-gen-ai-images — Ajouter image→Ajouter une image (download title)"
    ]


def repair_generative_ai_images_add_to_media_library_title(
    translated_path, translated_content, lang_key
):
    """Localize the English-only download icon ``title`` on ``images.md``.

    Copilot on PR #13313: ``title=\"Add image to Media Library\"`` left in
    KO (and similar) while steps were Korean/Portuguese hurts accessibility.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith(_GENERATIVE_AI_IMAGES_MD):
        return translated_content, []

    en_title = 'title="Add image to Media Library"'
    if en_title not in translated_content:
        return translated_content, []

    repl = {
        "ko": 'title="미디어 라이브러리에 이미지 추가"',
        "pt-br": 'title="Adicionar imagem à biblioteca de mídia"',
    }.get(lang_key)
    if not repl:
        return translated_content, []

    n = translated_content.count(en_title)
    return translated_content.replace(en_title, repl), [
        f"gen-ai-images — localized download title ({n}×) for {lang_key}"
    ]


def repair_fr_generative_brand_guidelines_nav_directives(
    translated_path, translated_content, lang_key
):
    """Align FR generative ``brand_guidelines`` ``nav_title`` with *directives*.

    Copilot on PR #13313: ``nav_title`` used *lignes directrices* while
    ``article_title`` and body used *directives de marque*.
    """
    if lang_key != "fr":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("brazeai/generative_ai/brand_guidelines.md"):
        return translated_content, []
    if "_lang/fr_fr/" not in rel:
        return translated_content, []

    old_nav = "nav_title: Lignes directrices de la marque\n"
    new_nav = "nav_title: Directives de marque\n"
    if old_nav not in translated_content:
        return translated_content, []
    if "Directives de marque" not in translated_content:
        return translated_content, []
    return translated_content.replace(old_nav, new_nav, 1), [
        "fr-gen-ai-brand — nav_title lignes directrices→Directives de marque"
    ]


def repair_ja_generative_brand_guidelines_fm_middot(
    translated_path, translated_content, lang_key
):
    r"""Restore middot in JA generative ``brand_guidelines`` YAML chrome.

    Copilot on PR #13313: ``nav_title`` / ``article_title`` dropped **・**
    while ``administrative/.../brand_guidelines.md`` still uses
    ``ブランド・ガイドライン``, producing inconsistent navigation labels.
    """
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("brazeai/generative_ai/brand_guidelines.md"):
        return translated_content, []
    if "_lang/ja/" not in rel:
        return translated_content, []

    pairs = (
        ("nav_title: ブランドガイドライン\n", "nav_title: ブランド・ガイドライン\n"),
        (
            "article_title: AIが生成するブランドガイドライン\n",
            "article_title: AIが生成するブランド・ガイドライン\n",
        ),
    )
    repairs = []
    new = translated_content
    for old, repl in pairs:
        if old in new:
            new = new.replace(old, repl, 1)
            repairs.append(f"ja-gen-ai-brand — inserted ・ in {old.strip()[:40]}…")
    if repairs:
        return new, repairs
    return translated_content, []


# German uses U+201E („) as the opening quotation mark and U+201C (") as
# the closing one. The LLM occasionally pairs a typographic „ with an
# ASCII " (U+0022) — the latter breaks screen readers, CSS selectors, and
# PDF export, and was flagged on PR #13299. Non-greedy matching and an
# exclusion of both ASCII " and typographic „/" inside the content window
# means we only flip the *first* ASCII " after each „ opener, so straight
# quotes inside unrelated HTML attributes like ``style="max-width:70%;"``
# are never touched (they sit past the match boundary).
_DE_MISMATCHED_QUOTE_RE = re.compile(
    r'\u201E([^\u201E\u201C"]+?)"',
    re.DOTALL,
)


def repair_german_mismatched_quotes(translated_path, translated_content):
    r"""Fix ``\u201E…\u0022`` → ``\u201E…\u201C`` in ``_lang/de/`` files.

    That is: German low-9 double quote (U+201E, ``„``) incorrectly closed
    with ASCII U+0022 (``"``) becomes closed with left double quotation
    mark U+201C (``"`` / ``\u201C``). The old docstring showed ``"`` in
    monospace for both sides, which rendered identically and confused
    readers (Copilot on PR #13303).

    Only runs on German translations because „ isn't an opening quote in
    the other five locales.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    # Match both ``_lang/de/...`` (relative) and ``/.../_lang/de/...`` (abs).
    if "_lang/de/" not in rel:
        return translated_content, []

    new, n = _DE_MISMATCHED_QUOTE_RE.subn(
        lambda m: "\u201E" + m.group(1) + "\u201C",
        translated_content,
    )
    if n:
        return new, [
            f"de-quotes — closed {n} „ opening quote(s) with typographic "
            f"\u201C (was ASCII \")"
        ]
    return translated_content, []


# Code fences we trust to contain balanced ASCII double-quote strings. Other
# languages (Markdown, TypeScript's template literals, Python's triple-quotes,
# etc.) have legitimate patterns that would produce noisy false positives, so
# we scope the check to cURL/JSON/shell/Liquid — the classes where an
# unterminated string literal is almost always a real bug.
# Allow leading indentation so list-nested fences (``    ```xml``) still
# toggle fence state. Copilot on PR #13303: the old ``^````` form missed
# indented openers, so ``in_fence`` stayed false and triple-backtick
# repairs could rewrite literal fence examples inside blocks.
#
# **Closing** fences are only lines that are *solely* backticks + optional
# spaces (no info string). **Opening** lines may carry a language tag
# (`` ```json``). ``repair_triple_backtick_inline_code`` uses that
# distinction so a `` ```liquid`` line *inside* an outer fence does not
# flip ``in_fence`` until the real `` ````` closer arrives.
_CODE_FENCE_OPEN_RE = re.compile(
    r'^\s*```([A-Za-z0-9_+.-]*)\s*$',
)
_CODE_FENCE_CLOSE_RE = re.compile(r'^\s*```\s*$')
_CHECKED_FENCE_LANGS = frozenset({
    "liquid", "json", "bash", "sh", "shell", "zsh", "curl",
})
_ESCAPED_DOUBLE_QUOTE_RE = re.compile(r'\\"')


def _iter_code_fences(content):
    """Yield ``(lang, start_line, end_line, body)`` for each fenced block.

    ``start_line`` / ``end_line`` are 0-based indices into ``splitlines()``
    and point at the opening / closing ``` lines respectively. ``body``
    is the text *between* those lines (unchanged whitespace).
    """
    lines = content.splitlines()
    i = 0
    total = len(lines)
    while i < total:
        m = _CODE_FENCE_OPEN_RE.match(lines[i])
        if not m:
            i += 1
            continue
        lang = m.group(1).lower()
        j = i + 1
        while j < total and not _CODE_FENCE_CLOSE_RE.match(lines[j]):
            j += 1
        if j >= total:
            return
        body = "\n".join(lines[i + 1:j])
        yield lang, i, j, body
        i = j + 1


def check_code_fence_balanced_quotes(content, label="translated"):
    """Warn when a ``liquid``/``json``/``bash``/``shell`` fence has an odd
    number of unescaped ASCII ``"`` characters.

    PR #13305's English source shipped a broken Liquid example
    (``"Hi ${first_name}, {% connected_content ... %}``) with an opening
    quote but no closer; the auto-translate pipeline faithfully mirrored
    the unterminated string into all six locales. A character-count
    heuristic is enough to catch this class of bug without the complexity
    of actual parsing: `curl -d '{"k": "v"}'`-style lines always contain
    an even number of quotes, so any odd count in the trusted fence
    languages is strong evidence of a missing closer.

    ``label`` distinguishes whether the fence lives in the English source
    vs. a locale copy in the warning message — a ``(english source)``
    tag is a cue to fix upstream before re-running the translation.
    """
    warnings = []
    for lang, start_line, end_line, body in _iter_code_fences(content):
        if lang not in _CHECKED_FENCE_LANGS:
            continue
        stripped = _ESCAPED_DOUBLE_QUOTE_RE.sub("", body)
        count = stripped.count('"')
        if count % 2 == 1:
            first_body_line = start_line + 2
            warnings.append(
                f"code-fence — unbalanced \" in ```{lang} block starting "
                f"near line {first_body_line} ({label}): {count} unescaped "
                f"double-quote(s), expected an even number. Likely an "
                f"unterminated string — inspect the opening/closing quotes "
                f"of the first line."
            )
    return warnings


# Triple backticks inside a paragraph line (with prose before or after)
# are almost always a mis-formatted inline code span. Kramdown treats the
# run of backticks as a fenced-code-block delimiter and breaks the
# surrounding rendering. The content group forbids newlines and backticks
# so we can only match a single-line token sequence like ``WYSIWYG``.
_TRIPLE_BACKTICK_INLINE_RE = re.compile(r'```([^\s`][^\n`]*?)```')


def repair_triple_backtick_inline_code(content):
    """Rewrite mid-paragraph ``` ```word``` ``` to ``` `word` ``` (single
    backticks).

    The English source of PR #13304's
    ``_user_guide/channels/email/html_editor/troubleshooting.md`` shipped
    ``The plain text view removes your ```WYSIWYG``` (what you see...)``
    on one line. Kramdown interprets the first `` ``` `` as a fenced-
    code-block opener mid-paragraph, so everything from *WYSIWYG* onward
    renders inside a dangling code block instead of as an inline span.
    The bug rode into every locale because the auto-translate pipeline
    mirrors the English source verbatim. This repair closes the loop
    deterministically in post-processing.

    Scope rules:

    * Fence delimiter lines (``^\\s*```lang$`` / ``^\\s*```$``) are excluded
      via ``_CODE_FENCE_OPEN_RE`` / ``_CODE_FENCE_CLOSE_RE`` so we never
      touch a real fence opener or closer (including indented fences).
    * Lines *inside* an already-open fenced block are skipped so we
      don't rewrite literal examples of Kramdown fencing syntax.
    * Table-cell lines (``^\\s*\\|``) are skipped — triple backticks
      inside table cells render as inline code in practice and rewriting
      them risks altering column alignment or escaping meaning.
    * Lines that are *entirely* a triple-backtick span (no surrounding
      prose) are left alone — those are the author's shorthand for a
      single-line code block, not the PR #13304 bug class.
    * The content group ``[^\\s`][^\\n`]*?`` forbids a leading whitespace
      or backtick so we don't accidentally chew into 4-backtick spans
      or padded fence openers.
    """
    lines = content.splitlines()
    in_fence = False
    repair_count = 0
    for i, L in enumerate(lines):
        if in_fence:
            if _CODE_FENCE_CLOSE_RE.match(L):
                in_fence = False
            continue
        if _CODE_FENCE_OPEN_RE.match(L):
            in_fence = True
            continue
        if L.lstrip().startswith("|"):
            continue
        matches = list(_TRIPLE_BACKTICK_INLINE_RE.finditer(L))
        if not matches:
            continue
        residue = _TRIPLE_BACKTICK_INLINE_RE.sub("", L).strip()
        if not residue:
            continue
        new_line = _TRIPLE_BACKTICK_INLINE_RE.sub(r"`\1`", L)
        repair_count += len(matches)
        lines[i] = new_line
    if repair_count:
        result = "\n".join(lines)
        if content.endswith("\n"):
            result += "\n"
        return result, [
            f"md-code-inline — rewrote {repair_count} "
            f"\"```word```\" to \"`word`\" (triple backticks in a "
            f"paragraph break Kramdown fenced-block parsing)"
        ]
    return content, []


def check_triple_backtick_inline_code(content, label="translated"):
    """Warn-only sibling of ``repair_triple_backtick_inline_code``.

    Runs the same scan without rewriting so we can surface mid-paragraph
    triple-backticks in the **English source** (where the bug usually
    originates — PR #13304). The repair still fires on the translated
    output, but flagging the source in the QC log prods humans to fix
    upstream before the next wave of locales inherits the same mistake.
    """
    warnings = []
    lines = content.splitlines()
    in_fence = False
    for i, L in enumerate(lines, start=1):
        if in_fence:
            if _CODE_FENCE_CLOSE_RE.match(L):
                in_fence = False
            continue
        if _CODE_FENCE_OPEN_RE.match(L):
            in_fence = True
            continue
        if L.lstrip().startswith("|"):
            continue
        matches = list(_TRIPLE_BACKTICK_INLINE_RE.finditer(L))
        if not matches:
            continue
        residue = _TRIPLE_BACKTICK_INLINE_RE.sub("", L).strip()
        if not residue:
            continue
        tokens = ", ".join(sorted({m.group(1) for m in matches}))[:120]
        warnings.append(
            f"md-code-inline — line {i} ({label}) uses triple backticks "
            f"mid-paragraph around [{tokens}]; Kramdown will parse them as "
            f"a fenced-block opener. Use single backticks for inline code."
        )
    return warnings


_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*$', re.MULTILINE)
_HEADING_SLUG_TAIL_RE = re.compile(r'\s*\{#[^}]+\}\s*$')

# The heading-drift check is scoped to user-facing prose sections. API
# reference, developer guide, and partner integration pages routinely keep
# English technical headings (``## Request body``, ``## Endpoint``,
# ``## Webhooks``, ``## iOS``) as intentional loanwords, so running the
# check there produces too much noise. PR #13299's real drift lived in
# ``_user_guide/channels/email/use_cases.md`` — we keep the check focused
# on the class of files where human-readable heading translation is the
# documented convention.
_HEADING_CHECK_SECTIONS = ("_user_guide/",)


def _strip_heading_slug(text):
    return _HEADING_SLUG_TAIL_RE.sub('', text).strip()


def _heading_is_product_term_only(heading_text):
    """True when the heading is a single Braze product name (stays English)."""
    text = _strip_heading_slug(heading_text).lower()
    return any(text == name.lower() for name in BRAZE_PRODUCT_NAMES)


# Single-word headings that universally stay English across all locales
# (fictional example brand names, platform/tech proper nouns, acronyms).
# Case-folded on lookup. Kept narrow so genuinely translatable single
# words — like ``Updates`` → ``Aktualisierungen`` — still surface.
_HEADING_SINGLE_WORD_ALLOWLIST = frozenset({
    # Platform / format / protocol proper nouns.
    "ios", "android", "csv", "json", "xml", "yaml", "html",
    "whatsapp", "sms", "mms", "rcs", "http", "https",
    "webhook", "webhooks",
    "shopify", "mparticle", "salesforce", "segment.com",
    # Fictional brand names used in Braze doc examples.
    "steppington", "pantslabyrinth", "moviecanon",
    # Common English loanwords accepted unchanged in tech prose.
    "onboarding", "feedback", "upload", "download", "login", "logout",
    "setup", "dashboard", "dashboards", "engagement", "performance",
    "teams", "events", "workspaces", "integration", "integrations",
    "analytics", "customization", "customizations", "arrays",
    "general", "prerequisites", "overview",
    "endpoint", "endpoints", "response", "request",
    "audience", "audiences", "push", "email",
})


def _heading_should_skip_check(heading_text):
    """True when a verbatim-English match should *not* be flagged as drift.

    Filters out false-positive shapes observed in a sweep of shipped
    _user_guide/ translations:

    - Headings inside inline code spans (```` ``identifier`` ``).
    - Headings containing any Braze product-name substring
      (``BrazeAI Operator``, ``Canvas components``, ``Content Optimizer``).
    - Single-word headings in the platform/brand/loanword allowlist
      (``## iOS``, ``## Integration``, ``## Steppington``).

    Still fires on genuine drift: multi-word English phrases with obvious
    native translations (``## Social Media``, ``## Best practices``), and
    single-word translatables not on the allowlist (``## Updates`` →
    ``## Aktualisierungen``).
    """
    stripped = _strip_heading_slug(heading_text)
    if not stripped:
        return True
    if "`" in stripped:
        return True
    lowered = stripped.lower()
    for name in BRAZE_PRODUCT_NAMES:
        if name.lower() in lowered:
            return True
    words = stripped.split()
    if len(words) <= 1 and lowered in _HEADING_SINGLE_WORD_ALLOWLIST:
        return True
    return False


def check_untranslated_headings(
    english_content, translated_content, lang_key, translated_path=None
):
    """Warn when most user-guide headings are translated but a few stay English.

    PR #13299 had a German translation of a user-guide page where every
    heading was translated except ``## Social Media`` and ``## Updates`` —
    an outlier pattern that no existing QC catches (they're too short to
    trip ``check_untranslated``'s 200-char threshold, and they're not
    product names so glossary checks ignore them). This surfaces a
    reviewer-visible warning; no auto-edit, because a bad replacement
    would be worse than a missed translation.

    Runs only on ``_user_guide/`` files for the reason explained on
    ``_HEADING_CHECK_SECTIONS``. Within that scope, still skips headings
    that are just Braze product names (``## Canvas``) and files where
    fewer than 60% of headings already differ from English.
    """
    if translated_path is None:
        return []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not any(section in rel for section in _HEADING_CHECK_SECTIONS):
        return []

    _, en_body = _extract_front_matter(english_content)
    _, tr_body = _extract_front_matter(translated_content)

    en_heads = [(lvl, text) for lvl, text in _HEADING_RE.findall(en_body)]
    tr_heads = [(lvl, text) for lvl, text in _HEADING_RE.findall(tr_body)]

    if len(en_heads) != len(tr_heads) or len(en_heads) < 4:
        return []

    matching = []
    translated_count = 0
    for (en_lvl, en_text), (tr_lvl, tr_text) in zip(en_heads, tr_heads):
        en_stripped = _strip_heading_slug(en_text)
        tr_stripped = _strip_heading_slug(tr_text)
        if en_stripped == tr_stripped:
            if _heading_is_product_term_only(tr_text):
                continue
            if _heading_should_skip_check(tr_text):
                continue
            matching.append(tr_stripped)
        else:
            translated_count += 1

    total = len(en_heads)
    if not matching:
        return []
    if translated_count < 0.6 * total:
        return []

    preview = ", ".join(f'"{h}"' for h in matching[:5])
    more = f" (+{len(matching) - 5} more)" if len(matching) > 5 else ""
    return [
        f"headings — {len(matching)} heading(s) left in English while "
        f"{translated_count} other heading(s) are translated: "
        f"{preview}{more}"
    ]


def repair_markdown_wire_format_tables(content):
    """Auto-fix markdown table / IAL issues from translation or English typos.

    - ``Content_Type`` → ``Content-Type`` (HTTP header spelling)
    - ``{: .reset-td-br-1 reset-td-br-2`` → ``{: .reset-td-br-1 .reset-td-br-2``
    - ``{: … reset-td-br-N`` → ``{: … .reset-td-br-N`` on IAL lines (any column)
    - Restore ``Authorization`` when the header cell was translated (es/pt)
    """
    repairs = []
    new = content

    if "| Content_Type |" in new:
        new = new.replace("| Content_Type |", "| Content-Type |")
        repairs.append("md-table — Content_Type → Content-Type")

    new, n_ial = _RESET_TD_BR_IAL_MISSING_DOT.subn(
        "{: .reset-td-br-1 .reset-td-br-2", new
    )
    if n_ial:
        repairs.append(
            f"md-ial — added missing '.' before reset-td-br-2 ({n_ial}x)"
        )

    new, n_dots = _dot_missing_reset_td_br_tokens_in_ial_lines(new)
    if n_dots:
        repairs.append(
            f"md-ial — dotted {n_dots} reset-td-br-* token(s) missing leading "
            f"'.' (PR #13395)"
        )

    for wrong, right in (
        ("| Autorización |", "| Authorization |"),
        ("| Autorização |", "| Authorization |"),
    ):
        if wrong in new:
            new = new.replace(wrong, right)
            repairs.append(
                "md-table — restored Authorization header cell (wire-format token)"
            )

    if new != content:
        return new, repairs
    return content, []


_DUP_ADJACENT_TARGET_AUDIENCES = re.compile(
    r"(\{%\s*multi_lang_include\s+target_audiences\.md\s*%\})\s*\n\1"
)


def repair_duplicate_adjacent_target_audiences_include(content):
    """Collapse back-to-back duplicate ``target_audiences`` includes.

    The English ``create_a_banner`` page briefly duplicated this include;
    translations should not repeat the same block twice with only whitespace
    between (renders duplicated content).
    """
    repairs = []
    new = content
    total = 0
    while True:
        new2, n = _DUP_ADJACENT_TARGET_AUDIENCES.subn(r"\1", new, count=1)
        if not n:
            break
        new = new2
        total += n
    if total:
        return new, [
            f"liquid_include — removed duplicate adjacent target_audiences.md ({total}x)"
        ]
    return content, []


# ``</a>`` immediately followed by a letter (CJK/Latin) without whitespace.
_ANCHOR_LETTER_RUNON_AFTER_CLOSE_RE = re.compile(
    r"</a>([A-Za-z\u00C0-\u024F\u3040-\u9FFF\uAC00-\uD7A3])"
)


def repair_missing_space_after_html_anchor_close(translated_content):
    """Insert a missing space after ``</a>`` when the next character starts a word.

    Prevents ``.../a>Word`` run-ons in YAML ``guide_top_text`` and prose
    (Copilot / auto-translate PR #13357).
    """
    new, n = _ANCHOR_LETTER_RUNON_AFTER_CLOSE_RE.subn(r"</a> \1", translated_content)
    if n:
        return new, [f"html — space after </a> before word run-on ({n}x)"]
    return translated_content, []


def repair_user_guide_messaging_data_hub_copy(
    translated_path, translated_content, lang_key
):
    """Fix recurring hub-page copy drift (messaging featured list, data landing).

    Covers the Copilot patterns from auto-translate PR #13357.
    """
    lang_info = LANGUAGES.get(lang_key)
    if not lang_info:
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    data_suffix = f"_lang/{lang_info['dir']}/_user_guide/data.md"
    repairs = []
    new = translated_content

    if lang_key == "pt-br" and rel.endswith("_lang/pt_br/_user_guide/messaging.md"):
        block = (
            "name: Canva\n"
            "    link: /docs/user_guide/messaging/canvas"
        )
        if block in new:
            new = new.replace(
                block,
                "name: Canvas\n"
                "    link: /docs/user_guide/messaging/canvas",
            )
            repairs.append("pt-messaging — Canva → Canvas (guide_featured_list)")

    if rel.endswith(data_suffix):
        if lang_key == "pt-br" and " e Segments." in new:
            new = new.replace(" e Segments.", " e segmentos.")
            repairs.append("pt-data — Segments → segmentos (EN segments parity)")
        if lang_key == "ja" and "プロファイルとSegmentを使用して" in new:
            new = new.replace(
                "プロファイルとSegmentを使用して",
                "プロファイルと**Segments**を使用して",
            )
            repairs.append("ja-data — Segment → **Segments** (product token)")
        if lang_key == "ko" and "프로필과 Segment를" in new:
            new = new.replace(
                "프로필과 Segment를",
                "프로필과 **Segments**를",
            )
            repairs.append("ko-data — Segment → **Segments** (product token)")

    if new != translated_content:
        return new, repairs
    return translated_content, []


# Table row where the cell separator ``|`` touches the opening backtick of an
# inline code span (``||``\`view_foo_bar\```). Kramdown still parses, but layout
# and reviews flag it (Copilot / auto-translate PR #13356).
_TABLE_PIPE_TOUCHING_CODE_SPAN_RE = re.compile(
    r"\|\`([a-z][a-z0-9_]*(?:_[a-z0-9_]+)+)`"
)


def repair_markdown_table_pipe_adjacent_to_underscored_code(translated_content):
    r"""Insert a space between ``|`` and `\`...\` when a slug-style code token follows."""
    repairs = []
    lines_out = []
    for line in translated_content.split("\n"):
        if not line.lstrip().startswith("|"):
            lines_out.append(line)
            continue
        new_line, n = _TABLE_PIPE_TOUCHING_CODE_SPAN_RE.subn(r"| `\1`", line)
        if n:
            repairs.append(
                "md-table — space before inline code cell after `|` "
                f"({n} on one line)"
            )
        lines_out.append(new_line)
    new_content = "\n".join(lines_out)
    if new_content != translated_content:
        return new_content, repairs
    return translated_content, []


def repair_es_whatsapp_template_prerequisites_permission_bullets(
    translated_path, translated_content, lang_key
):
    """Restore English dashboard permission strings in ES WhatsApp prerequisites.

    Spanish pages keep these quoted labels verbatim so they match the Braze
    dashboard and sibling ``carousel_template_prerequisites`` (PR #13356).
    """
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_includes/whatsapp/template_prerequisites.md"):
        return translated_content, []
    replacements = (
        ('- "Ver plantillas de mensajes de WhatsApp"', '- "View WhatsApp Message Templates"'),
        ('- "Editar plantillas de mensajes de WhatsApp"', '- "Edit WhatsApp Message Templates"'),
    )
    new = translated_content
    applied = 0
    for wrong, right in replacements:
        if wrong in new:
            new = new.replace(wrong, right)
            applied += 1
    if not applied:
        return translated_content, []
    return new, [
        "es_whatsapp — restored English permission bullet strings "
        f"({applied} pattern(s))"
    ]


def repair_pt_inapp_message_troubleshooting_loanword_delay(
    translated_path, translated_content, lang_key
):
    """Fix Portuguese article gender before borrowed ``delay`` (in-app troubleshooting)."""
    if lang_key != "pt-br":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "inapp_message_troubleshooting" not in rel:
        return translated_content, []
    new = translated_content.replace("uma `delay`", "um `delay`")
    if new != translated_content:
        return new, ["pt_br — uma `delay` → um `delay` (PR #13356)"]
    return translated_content, []


def repair_pt_br_banners_reporting_performance(translated_path, translated_content):
    """Prefer ``desempenho`` over English *performance* in PT-BR banner reporting."""
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/pt_br/_user_guide/channels/banners/reporting.md"):
        return translated_content, []

    repairs = []
    new = translated_content
    if "performance da mensagem" in new:
        new = new.replace("performance da mensagem", "desempenho da mensagem")
        repairs.append("pt-banners-reporting — performance → desempenho (mensagem)")
    if "performance histórica" in new:
        new = new.replace("performance histórica", "desempenho histórico")
        repairs.append("pt-banners-reporting — performance histórica → desempenho histórico")
    if new != translated_content:
        return new, repairs
    return translated_content, []


def repair_banners_create_a_banner_verbatim_ui(translated_path, translated_content):
    """Fix English Braze UI labels whose **casing** drifted during translation.

    When the English source keeps dashboard controls in English, the model
    sometimes Title-cases them incorrectly (for example *Set Exact Priority* vs
    *Set exact priority* — Copilot / PR #13349).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/" not in rel or not rel.endswith(
        "_user_guide/channels/banners/create_a_banner.md"
    ):
        return translated_content, []

    repairs = []
    new = translated_content
    # Match English `_docs/.../create_a_banner.md` (**Set exact priority**).
    if "**Set Exact Priority**" in new:
        new = new.replace("**Set Exact Priority**", "**Set exact priority**")
        repairs.append("banners-create-a-banner — Set exact priority UI casing")

    if new != translated_content:
        return new, repairs
    return translated_content, []


def repair_fr_banners_custom_code_javascript_bridge_terms(
    translated_path, translated_content, lang_key
):
    """Keep French JavaScript-bridge wording aligned across YAML and body.

    Models sometimes use *passerelle JavaScript* in ``nav_title`` while
    ``article_title`` and prose use *pont JavaScript* (Copilot PR #13349).
    """
    if lang_key != "fr":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/fr_fr/_user_guide/channels/banners/custom_code.md"):
        return translated_content, []

    if "passerelle JavaScript" not in translated_content:
        return translated_content, []

    new = translated_content.replace("passerelle JavaScript", "pont JavaScript")
    return new, [
        "fr-banners-custom-code — passerelle JavaScript → pont JavaScript "
        "(nav/body parity)"
    ]


def repair_de_banners_custom_code_inclusive_nutzer(
    translated_path, translated_content, lang_key
):
    """Fix inconsistent singular inclusive *Nutzer:in* in DE banner custom-code."""
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/de/_user_guide/channels/banners/custom_code.md"):
        return translated_content, []

    old = (
        "Um beispielsweise einen Klick zu protokollieren, wenn eine Nutzer:in "
        "in Ihrem angepassten HTML auf einen Button tippt:"
    )
    new = (
        "Um beispielsweise einen Klick zu protokollieren, wenn Nutzer:innen "
        "in Ihrem angepassten HTML auf einen Button tippen:"
    )
    if old not in translated_content:
        return translated_content, []

    return translated_content.replace(old, new, 1), [
        "de-banners-custom-code — plural inclusive Nutzer:innen in example"
    ]


def _fm_line_for_key(fm: str, key: str) -> Optional[str]:
    """Return the full source line for ``key:`` (single-line YAML scalar) or None."""
    for line in fm.split("\n"):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            return line
    return None


def repair_messaging_canvas_hub_titles_from_engagement_tools(
    translated_path, translated_content
):
    """Sync Canvas hub title YAML with the locale's ``engagement_tools/canvas`` page.

    New ``_user_guide/messaging/canvas`` mirrors the English IA; models often
    leave ``nav_title`` / ``article_title`` / ``guide_top_header`` as English
    ``Canvas`` while ``engagement_tools/canvas`` already uses localized titles
    (e.g. Japanese キャンバス, Korean 캔버스, pt-BR Canva). Align so nav and search stay consistent.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    suffix = "_user_guide/messaging/canvas.md"
    if "_lang/" not in rel or not rel.endswith(suffix):
        return translated_content, []

    tr_path = Path(translated_path).resolve()
    # Sibling of ``messaging/`` under ``_user_guide/`` → ``engagement_tools/canvas.md``
    ref_path = tr_path.parent.parent / "engagement_tools" / "canvas.md"
    if not ref_path.is_file():
        return translated_content, []

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    ref_fm, _ = _extract_front_matter(ref_path.read_text(encoding="utf-8"))
    if not ref_fm:
        return translated_content, []

    keys = ("nav_title", "article_title", "guide_top_header")
    repairs = []
    repaired_fm = tr_fm
    for key in keys:
        ref_line = _fm_line_for_key(ref_fm, key)
        tr_line = _fm_line_for_key(repaired_fm, key)
        if not ref_line or not tr_line:
            continue
        if ref_line == tr_line:
            continue
        repaired_fm = repaired_fm.replace(tr_line, ref_line, 1)
        repairs.append(
            f"canvas-messaging-hub — {key} aligned with engagement_tools/canvas.md"
        )

    if repairs:
        return f"---\n{repaired_fm}\n---\n{tr_body}", repairs
    return translated_content, []


def repair_messaging_feature_flags_fm_from_engagement_tools(
    translated_path, translated_content
):
    """Sync Feature Flags stub front matter with ``engagement_tools/feature_flags``.

    ``messaging/feature_flags.md`` mirrors the English IA as a thin include of
    the same body as ``engagement_tools/feature_flags.md``. Models sometimes
    paraphrase ``nav_title`` / ``article_title`` / ``description`` (e.g.
    Spanish *Conmutador de características* vs established *Banderas de
    características* on the sibling — Copilot on PR #13309).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    suffix = "_user_guide/messaging/feature_flags.md"
    if "_lang/" not in rel or not rel.endswith(suffix):
        return translated_content, []

    tr_path = Path(translated_path).resolve()
    ref_path = tr_path.parent.parent / "engagement_tools" / "feature_flags.md"
    if not ref_path.is_file():
        return translated_content, []

    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []

    ref_fm, _ = _extract_front_matter(ref_path.read_text(encoding="utf-8"))
    if not ref_fm:
        return translated_content, []

    keys = ("nav_title", "article_title", "description")
    repairs = []
    repaired_fm = tr_fm
    for key in keys:
        ref_line = _fm_line_for_key(ref_fm, key)
        tr_line = _fm_line_for_key(repaired_fm, key)
        if not ref_line or not tr_line:
            continue
        if ref_line == tr_line:
            continue
        repaired_fm = repaired_fm.replace(tr_line, ref_line, 1)
        repairs.append(
            f"feature-flags-messaging-hub — {key} aligned with "
            f"engagement_tools/feature_flags.md"
        )

    if repairs:
        return f"---\n{repaired_fm}\n---\n{tr_body}", repairs
    return translated_content, []


_EN_SETTINGS_APIS_API_KEYS_NAV = (
    "**Settings** > **APIs and Identifiers** > **API Keys**"
)


def repair_braze_dashboard_api_keys_nav_collapse(
    english_content: str, translated_content: str, lang_key: str
):
    """Restore middle menu level when models collapse REST API key navigation.

    English uses **Settings** > **APIs and Identifiers** > **API Keys**; bad
    translations repeat the child label twice and drop *APIs and Identifiers*.
    """
    if _EN_SETTINGS_APIS_API_KEYS_NAV not in english_content:
        return translated_content, []

    repairs = []
    new = translated_content
    fixes = (
        (
            "ko",
            "Braze 대시보드에서 **설정** > **API 키** > **API 키**",
            "Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**",
        ),
        (
            "ja",
            "Brazeダッシュボードで、**設定** > **APIキー** > **APIキー**",
            "Brazeダッシュボードで、**設定** > **APIと識別子** > **APIキー**",
        ),
        (
            "fr",
            "**Paramètres** > **Clés API** > **Clés API**",
            "**Paramètres** > **API et identifiants** > **Clés API**",
        ),
    )
    for key, wrong, right in fixes:
        if lang_key != key:
            continue
        if wrong in new:
            new = new.replace(wrong, right)
            repairs.append(
                "nav-path — Settings > APIs and Identifiers > API Keys (collapsed fix)"
            )
    if new != translated_content:
        return new, repairs
    return translated_content, repairs


def repair_decisioning_insights_table_labels(
    english_content: str, translated_path: str, translated_content: str, lang_key: str
):
    """Fix recurring Decisioning Studio *Insights* table mistranslations."""
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("decisioning_studio/reporting/insights.md"):
        return translated_content, []

    repairs = []
    new = translated_content

    if lang_key == "ko" and "| Dimension |" in english_content:
        if "| 크기 및 위치 |" in new:
            new = new.replace("| 크기 및 위치 |", "| 차원 |")
            repairs.append("insights-table — KO Dimension row (차원)")

    if lang_key == "ja" and "| % of time chosen |" in english_content:
        if "全セレクションのうち" in new:
            new = new.replace("全セレクションのうち", "全選択のうち")
            repairs.append("insights-table — JA percent-chosen phrasing")

    if new != translated_content:
        return new, repairs
    return translated_content, repairs


def repair_pt_br_agents_reference_confidence_alt(
    translated_path: str, translated_content: str
):
    """Fix mistaken *confidence interval* wording for ``confidence_score`` alt (pt-BR).

    Models sometimes render *intervalo de confiança* next to *probability score*
    and *explanation*; the field is **confidence score** / *pontuação de confiança*.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/pt_br/_user_guide/brazeai/agents/reference.md"):
        return translated_content, []
    wrong = "pontuação de intervalo de confiança"
    if wrong not in translated_content:
        return translated_content, []
    return translated_content.replace(
        wrong, "pontuação de confiança"
    ), ["pt-agents-reference — confidence score alt wording"]


def repair_pt_br_brazeai_content_optimizer_product_name(
    translated_path: str, translated_content: str
):
    """Replace leaked English *Content Optimizer* with pt-BR **Otimizador de Conteúdo**.

    Nav/titles often localize the feature name while the model still pastes the US
    marketing string into alerts and body copy (see Copilot review on PR #13282).
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/pt_br/_user_guide/brazeai/content_optimizer.md"):
        return translated_content, []
    if "Content Optimizer" not in translated_content:
        return translated_content, []
    return translated_content.replace(
        "Content Optimizer", "Otimizador de Conteúdo"
    ), ["pt-brazeai-content_optimizer — Content Optimizer → Otimizador de Conteúdo"]


def repair_de_brazeai_schritt_three_link_text(
    translated_path: str, translated_content: str, lang_key: str
):
    """Use idiomatic ``Schritt 3`` in prose links, not ``3. Schritt`` (German agents docs)."""
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "/brazeai/agents/" not in rel or not rel.endswith(".md"):
        return translated_content, []
    marker = "[3. Schritt](#agent-instructions)"
    if marker not in translated_content:
        return translated_content, []
    return translated_content.replace(
        marker, "[Schritt 3](#agent-instructions)"
    ), ['de-agents — link text "Schritt 3" (not "3. Schritt")']


def repair_es_agents_reference_alt_sentence_case(
    translated_path: str, translated_content: str, lang_key: str
):
    """Sentence-case *gestión* inside Spanish image alt (agents reference)."""
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/es/_user_guide/brazeai/agents/reference.md"):
        return translated_content, []
    wrong = "![Página de Gestión de agentes"
    if wrong not in translated_content:
        return translated_content, []
    return translated_content.replace(
        wrong, "![Página de gestión de agentes"
    ), ["es-agents-reference — sentence case in image alt"]


def repair_es_braze_pilot_deep_links_splash_vs_welcome(
    translated_path: str, translated_content: str, lang_key: str
):
    """Disambiguate Spanish *splash* deep-link rows from ``/welcome`` (same file).

    Models sometimes label every ``/splash`` row *Pantalla de bienvenida* even when
    a separate ``.../welcome`` row uses the same phrase—mirror English *Splash
    screen* vs *welcome* semantics with distinct labels.
    """
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/es/_user_guide/get_started/braze_pilot/deep_links.md"):
        return translated_content, []

    repairs = []
    new = translated_content
    for wrong, right in (
        (
            "| Pantalla de bienvenida | `braze-pilot://navigation/steppington/splash` |",
            "| Pantalla de inicio | `braze-pilot://navigation/steppington/splash` |",
        ),
        (
            "| Pantalla de bienvenida | `braze-pilot://navigation/pantslabyrinth/splash` |",
            "| Pantalla de carga inicial | `braze-pilot://navigation/pantslabyrinth/splash` |",
        ),
        (
            "| Pantalla de bienvenida | `braze-pilot://navigation/moviecannon/splash` |",
            "| Pantalla de presentación | `braze-pilot://navigation/moviecannon/splash` |",
        ),
    ):
        if wrong in new:
            new = new.replace(wrong, right)
            repairs.append(
                "es-braze-pilot-deep_links — splash table label distinct from /welcome"
            )
    if new != translated_content:
        return new, repairs
    return translated_content, repairs


def repair_braze_pilot_deep_links_section_anchor_ids(
    translated_path: str, translated_content: str
):
    """Assign unique Kramdown ``{#…}`` slugs per Steppington / PantsLabyrinth / MovieCanon block.

    English ``deep_links.md`` repeats the same H3 titles under three ``##`` brand
    sections without explicit ids. Locale files often reuse one slug (for
    example ``{#example-deep-link}``) in every block, which duplicates HTML ids
    (Copilot PR #13350). Prefix anchors: ``steppington-``, ``pantslabyrinth-``,
    ``moviecanon-`` for the four parallel headings in each block.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/" not in rel or not rel.endswith(
        "_user_guide/get_started/braze_pilot/deep_links.md"
    ):
        return translated_content, []

    if "## Steppington" not in translated_content:
        return translated_content, []

    pattern = r"^## (Steppington|PantsLabyrinth|MovieCanon)\s*\n"
    parts = re.split(pattern, translated_content, flags=re.MULTILINE)
    if len(parts) != 7:
        return translated_content, []

    preamble, s1, body_s, s2, body_p, s3, body_m = parts
    if (s1, s2, s3) != ("Steppington", "PantsLabyrinth", "MovieCanon"):
        return translated_content, []

    prefixes = {
        "Steppington": "steppington",
        "PantsLabyrinth": "pantslabyrinth",
        "MovieCanon": "moviecanon",
    }
    slug_pairs = (
        ("{#example-deep-link}", "-example-deep-link}"),
        ("{#deep-links-without-parameters}", "-deep-links-without-parameters}"),
        ("{#deep-links-with-parameters}", "-deep-links-with-parameters}"),
        ("{#accepted-parameters}", "-accepted-parameters}"),
    )

    repairs = []
    rebuilt = [preamble]
    for sec_name, body in ((s1, body_s), (s2, body_p), (s3, body_m)):
        prefix = prefixes[sec_name]
        new_body = body
        if "{#example-deep-link}" in new_body:
            for old, suffix_tail in slug_pairs:
                if old not in new_body:
                    return translated_content, []
                new_slug = "{#" + prefix + suffix_tail
                new_body = new_body.replace(old, new_slug, 1)
            repairs.append(
                f"braze-pilot-deep_links — unique explicit ids for {sec_name} block"
            )
        rebuilt.append(f"## {sec_name}\n")
        rebuilt.append(new_body)

    new_content = "".join(rebuilt)
    if new_content != translated_content:
        return new_content, repairs
    return translated_content, []


def repair_es_braze_pilot_deep_links_general_heading(
    translated_path: str, translated_content: str, lang_key: str
):
    """Add ``{#general}`` to Spanish ``## General`` for anchor parity (PR #13350)."""
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/es/_user_guide/get_started/braze_pilot/deep_links.md"):
        return translated_content, []

    if not re.search(r"^## General\s*$", translated_content, flags=re.MULTILINE):
        return translated_content, []

    new = re.sub(
        r"^## General\s*$",
        "## General {#general}",
        translated_content,
        count=1,
        flags=re.MULTILINE,
    )
    return new, ["es-braze-pilot-deep_links — added {#general} to General heading"]


def repair_es_braze_pilot_getting_started_app_settings_bold(
    translated_path: str, translated_content: str, lang_key: str
):
    r"""Localize raw **App Settings** in Spanish Pilot getting started (PR #13350)."""
    if lang_key != "es":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/es/_user_guide/get_started/braze_pilot/getting_started.md"):
        return translated_content, []

    if "**App Settings**" not in translated_content:
        return translated_content, []

    return translated_content.replace(
        "**App Settings**",
        "**Configuración de la aplicación**",
    ), ["es-braze-pilot-getting_started — App Settings → Configuración de la aplicación"]


def repair_fr_braze_pilot_getting_started_campaign_inline_french(
    translated_path: str, translated_content: str, lang_key: str
):
    """Replace English *Campaign* tokens in French demo-send prose (PR #13350)."""
    if lang_key != "fr":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/fr_fr/_user_guide/get_started/braze_pilot/getting_started.md"):
        return translated_content, []

    new = translated_content
    for wrong, right in (
        ("certaines Campaign de démonstration", "certaines campagnes de démonstration"),
        ("les Campaign qui y sont lancées", "les campagnes qui y sont lancées"),
    ):
        if wrong in new:
            new = new.replace(wrong, right)

    if new != translated_content:
        return new, [
            "fr-braze-pilot-getting_started — Campaign → campagne(s) in demo/prose"
        ]
    return translated_content, []


def repair_ja_braze_pilot_deep_links_pilot_brand_casing(
    translated_path: str, translated_content: str, lang_key: str
):
    """Normalize ``pilotアプリ`` → ``Pilotアプリ`` in JA Pilot deep links intro."""
    if lang_key != "ja":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/ja/_user_guide/get_started/braze_pilot/deep_links.md"):
        return translated_content, []

    if "pilotアプリ" not in translated_content:
        return translated_content, []

    return translated_content.replace(
        "pilotアプリ",
        "Pilotアプリ",
    ), ["ja-braze-pilot-deep_links — Pilot product casing (pilotアプリ)"]


def repair_braze_pilot_getting_started_campaigns_in_link_anchor(
    translated_path: str, translated_content: str, lang_key: str
):
    """Keep **Canvas** English (product name) but localize *Campaigns* in link text.

    Copilot review: ``[… Campaigns …]({{site.baseurl}}/…)`` reads mixed when the
    sentence is otherwise Spanish/French; glossary keeps *Canvas* in English.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("get_started/braze_pilot/getting_started.md"):
        return translated_content, []

    repairs = []
    new = translated_content
    if lang_key == "es":
        if "[Primeros pasos: Campaigns y Canvas]" in new:
            new = new.replace(
                "[Primeros pasos: Campaigns y Canvas]",
                "[Primeros pasos: Campañas y Canvas]",
            )
            repairs.append(
                "es-braze-pilot-getting_started — Campaigns → Campañas in link anchor"
            )
    elif lang_key == "fr":
        if "[Pour commencer : Campaigns et Canvas]" in new:
            new = new.replace(
                "[Pour commencer : Campaigns et Canvas]",
                "[Pour commencer : Campagnes et Canvas]",
            )
            repairs.append(
                "fr-braze-pilot-getting_started — Campaigns → Campagnes in link anchor"
            )
    if new != translated_content:
        return new, repairs
    return translated_content, repairs


def repair_de_braze_pilot_low9_pair_ascii_close_quote(
    translated_path: str, translated_content: str, lang_key: str
):
    r"""Fix ``„…"`` (low-9 + ASCII U+0022 closer) before `` als …`` in Pilot DE alts."""
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/de/_user_guide/get_started/braze_pilot/getting_started.md"):
        return translated_content, []

    pattern = re.compile(r'„([^„]+)"(?=\s+als\s+ausgew)')
    new, n = pattern.subn(r'„\1“', translated_content)
    if n:
        return new, [
            "de-braze-pilot-getting_started — German alt „…“ (not „…\" ) before als …"
        ]
    return translated_content, []


def repair_fr_payload_display_typography(
    translated_path, translated_content, lang_key
):
    """Normalize French ``PAYLOAD`` (English all-caps) to readable *payload* wording.

    All-caps *PAYLOAD* in prose reads like shouting; technical French often uses
    lowercase *payload* / plural *payloads* (see Copilot review on campaigns /
    Decisioning docs).

    Skips ``…/cloud_ingestion/sql_editor.md``: there ``PAYLOAD`` / ``UPDATED_AT``
    are case-sensitive CDI column identifiers and must stay as English spells
    them (auto-translate PR #13397).
    """
    if lang_key != "fr":
        return translated_content, []

    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "data/unification/cloud_ingestion/sql_editor.md" in rel:
        return translated_content, []

    new = translated_content
    for wrong, right in (
        ("les PAYLOAD ", "les payloads "),
        ("les PAYLOAD à", "les payloads à"),
        ("les PAYLOAD,", "les payloads,"),
        ("leurs PAYLOAD ", "leurs payloads "),
        ("leurs PAYLOAD.", "leurs payloads."),
        ("le PAYLOAD brut", "le payload brut"),
        ("## PAYLOAD ", "## Payload "),
        ("## PAYLOAD\n", "## Payload\n"),
    ):
        if wrong in new:
            new = new.replace(wrong, right)

    new, _n = re.subn(r"\bPAYLOAD\b", "payload", new)

    if new != translated_content:
        return new, ["fr-payload — normalized PAYLOAD → payload/Payload wording"]
    return translated_content, []


def repair_yaml_tool_list_spacing(translated_content):
    """Normalize ``tool:␠`` + newline before list (``tool:\\n  -``) in front matter."""
    tr_fm, tr_body = _extract_front_matter(translated_content)
    if not tr_fm:
        return translated_content, []
    if "tool: \n" not in tr_fm and "tool: \r\n" not in tr_fm:
        return translated_content, []
    repaired = tr_fm.replace("tool: \n", "tool:\n").replace("tool: \r\n", "tool:\r\n")
    if repaired == tr_fm:
        return translated_content, []
    return f"---\n{repaired}\n---\n{tr_body}", ["front_matter — tool: trailing space before list"]


def repair_urls(english_content, translated_content):
    """Ensure markdown link URLs match the English source."""
    en_urls = _extract_md_link_urls(english_content)
    tr_urls = _extract_md_link_urls(translated_content)

    if not en_urls:
        return translated_content, []

    if len(en_urls) != len(tr_urls):
        return translated_content, [
            f"urls — count mismatch (English: {len(en_urls)}, "
            f"translated: {len(tr_urls)}); skipped auto-repair"
        ]

    repairs = []
    repaired = translated_content
    for i, (en_url, tr_url) in enumerate(zip(en_urls, tr_urls)):
        if en_url != tr_url:
            repaired = repaired.replace(f"]({tr_url})", f"]({en_url})", 1)
            repairs.append(f"url[{i}] — restored '{en_url}'")

    return repaired, repairs


def repair_apitags(english_content, translated_content):
    """Restore canonical English apitags from the English source.

    Filter/checkbox logic in event glossary layouts depends on exact tag-key
    matches.  Translated tags fragment filters and break the UI.
    """
    pattern = re.compile(
        r'(\{%\s*apitags\s*%\})(.*?)(\{%\s*endapitags\s*%\})', re.DOTALL
    )
    en_blocks = [m.group(2).strip() for m in pattern.finditer(english_content)]
    tr_matches = list(pattern.finditer(translated_content))

    if not en_blocks:
        return translated_content, []

    if len(en_blocks) != len(tr_matches):
        return translated_content, [
            f"apitags — count mismatch (English: {len(en_blocks)}, "
            f"translated: {len(tr_matches)}); skipped auto-repair"
        ]

    repairs = []
    result = translated_content
    for match, eng_block in zip(reversed(tr_matches), reversed(en_blocks)):
        tr_block = match.group(2).strip()
        if tr_block != eng_block:
            result = (
                result[:match.start(2)] + '\n' + eng_block + '\n'
                + result[match.end(2):]
            )
            repairs.append(f"apitags — restored English tags")

    if len(repairs) > 1:
        repairs = [f"apitags — restored {len(repairs)} blocks to English"]

    return result, repairs


def repair_glossary_identifiers(english_content, translated_content, lang_key):
    """Restore English glossary_tags, entry names, and entry tags for non-Latin
    languages.  Jekyll's slugify and the JS string_to_slug strip non-Latin
    characters, producing empty/identical HTML IDs that break filter checkboxes.
    """
    if lang_key not in NON_LATIN_LANGUAGES:
        return translated_content, []

    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, tr_body = _extract_front_matter(translated_content)

    if not en_fm or not tr_fm:
        return translated_content, []

    en_gt_block = _extract_fm_block(en_fm, 'glossary_tags')
    if not en_gt_block:
        return translated_content, []

    repairs = []
    repaired_fm = tr_fm

    tr_gt_block = _extract_fm_block(repaired_fm, 'glossary_tags')
    if tr_gt_block and tr_gt_block != en_gt_block:
        repaired_fm = repaired_fm.replace(tr_gt_block, en_gt_block)
        repairs.append("glossary_tags — restored English filter names")

    en_gl_block = _extract_fm_block(en_fm, 'glossaries')
    tr_gl_block = _extract_fm_block(repaired_fm, 'glossaries')

    if en_gl_block and tr_gl_block:
        en_names = re.findall(r'  - name:\s*(.*)', en_gl_block)
        tr_names = re.findall(r'  - name:\s*(.*)', tr_gl_block)
        en_tag_lists = re.findall(r'    - ([^\n]+)', en_gl_block)
        tr_tag_lists = re.findall(r'    - ([^\n]+)', tr_gl_block)

        name_fixes = 0
        for en_name, tr_name in zip(en_names, tr_names):
            en_val = en_name.strip().strip('"').strip("'")
            tr_val = tr_name.strip().strip('"').strip("'")
            if en_val != tr_val:
                old_line = f'  - name: {tr_name}'
                quoted = f'"{en_val}"' if ':' in en_val or '#' in en_val else f'"{en_val}"'
                new_line = f'  - name: {quoted}'
                repaired_fm = repaired_fm.replace(old_line, new_line, 1)
                name_fixes += 1

        tag_fixes = 0
        for en_tag, tr_tag in zip(en_tag_lists, tr_tag_lists):
            en_t = en_tag.strip()
            tr_t = tr_tag.strip()
            if en_t != tr_t:
                repaired_fm = repaired_fm.replace(
                    f'    - {tr_tag}', f'    - {en_t}', 1
                )
                tag_fixes += 1

        if name_fixes:
            repairs.append(f"glossary_names — restored {name_fixes} entry names")
        if tag_fixes:
            repairs.append(f"glossary_entry_tags — restored {tag_fixes} tags")

    if repairs:
        translated_content = f"---\n{repaired_fm}\n---\n{tr_body}"

    return translated_content, repairs


def check_liquid_paired_block_tags(english_content, translated_content):
    """Warn when paired Liquid block open/close counts drift from English."""
    warnings = []
    for open_tag, close_tag in _LIQUID_PAIRED_TAGS_FOR_QC:
        en_open = _count_liquid_tag(english_content, open_tag)
        tr_open = _count_liquid_tag(translated_content, open_tag)
        en_close = _count_liquid_tag(english_content, close_tag)
        tr_close = _count_liquid_tag(translated_content, close_tag)
        if tr_open != tr_close:
            warnings.append(
                f"liquid_paired — {open_tag}/{close_tag} unbalanced in translation "
                f"({open_tag}={tr_open}, {close_tag}={tr_close})"
            )
        elif tr_open != en_open or tr_close != en_close:
            warnings.append(
                f"liquid_paired — {open_tag}/{close_tag} count drift "
                f"(English {open_tag}={en_open}/{close_tag}={en_close}, "
                f"translation {open_tag}={tr_open}/{close_tag}={tr_close})"
            )
    return warnings


def check_liquid_tags(english_content, translated_content):
    """Check that Liquid tags are preserved between source and translation."""
    warnings = []

    en_exprs = set(re.findall(r'\{\{.*?\}\}', english_content))
    tr_exprs = set(re.findall(r'\{\{.*?\}\}', translated_content))
    for expr in sorted(en_exprs - tr_exprs):
        warnings.append(f"liquid_expr — missing: {expr}")

    en_tags = re.findall(r'\{%[-\s]*(.*?)[-\s]*%\}', english_content)
    tr_tags = re.findall(r'\{%[-\s]*(.*?)[-\s]*%\}', translated_content)

    def tag_name(t):
        return t.strip().split()[0] if t.strip() else ""

    en_counts = Counter(tag_name(t) for t in en_tags)
    tr_counts = Counter(tag_name(t) for t in tr_tags)

    for tag, count in en_counts.items():
        tr_count = tr_counts.get(tag, 0)
        if tr_count < count:
            warnings.append(
                f"liquid_tag — '{tag}' appears {count}x in English but "
                f"{tr_count}x in translation"
            )

    return warnings


def check_glossary_compliance(english_content, translated_content, lang_key):
    """Check that Braze product names appear in the translation.

    Counts both the English term and its glossary-defined translation so
    that correctly translated terms (e.g., "Campaign" → "Kampagne") are
    not flagged as missing.
    """
    _, en_body = _extract_front_matter(english_content)
    _, tr_body = _extract_front_matter(translated_content)

    code_re = re.compile(r'```.*?```', re.DOTALL)
    en_clean = code_re.sub('', en_body)
    tr_clean = code_re.sub('', tr_body)

    glossary = load_glossary(lang_key)

    warnings = []
    for name in BRAZE_PRODUCT_NAMES:
        en_count = en_clean.lower().count(name.lower())
        if en_count < 2:
            continue

        tr_count = tr_clean.lower().count(name.lower())

        glossary_term = glossary.get(name, "").strip()
        if glossary_term and glossary_term.lower() != name.lower():
            tr_count += tr_clean.lower().count(glossary_term.lower())

        if tr_count < en_count * 0.5:
            warnings.append(
                f"glossary — '{name}' appears {en_count}x in English but "
                f"only {tr_count}x in translation"
            )

    return warnings


def check_completeness(english_content, translated_content):
    """Flag translations whose length deviates significantly from the source."""
    en_len = len(english_content)
    if en_len == 0:
        return []

    ratio = len(translated_content) / en_len
    if ratio < COMPLETENESS_MIN_RATIO:
        return [
            f"completeness — translation is {ratio:.0%} of English length "
            f"(min threshold: {COMPLETENESS_MIN_RATIO:.0%}); possible truncation"
        ]
    if ratio > COMPLETENESS_MAX_RATIO:
        return [
            f"completeness — translation is {ratio:.0%} of English length "
            f"(max threshold: {COMPLETENESS_MAX_RATIO:.0%}); possible hallucination"
        ]
    return []


_IMG_BUSTER_ALT_RE = re.compile(
    r"!\[([^\]]*)\]\(\{%\s*image_buster\b",
    re.IGNORECASE,
)
# Lowercase Latin snake_case with multiple segments (internal slug style).
_SNAKE_CASE_IMAGE_ALT_RE = re.compile(
    r"^[a-z][a-z0-9]*(?:_[a-z][a-z0-9]*)+$",
)


def check_image_buster_alt_identifier_style(translated_path, translated_content):
    """Warn when ``image_buster`` image alts look like English slug identifiers.

    Models often copy ``![engagement_reports_foo]({% image_buster ...`` verbatim
    into localized docs; screen readers and Copilot expect a short descriptive
    phrase instead (auto-translate PR #13407). Only runs for paths under
    ``_lang/``.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/" not in rel:
        return []
    warnings = []
    seen = set()
    for m in _IMG_BUSTER_ALT_RE.finditer(translated_content):
        alt = m.group(1).strip()
        if len(alt) < 18 or "_" not in alt:
            continue
        if not _SNAKE_CASE_IMAGE_ALT_RE.match(alt):
            continue
        if alt in seen:
            continue
        seen.add(alt)
        preview = alt if len(alt) <= 72 else f"{alt[:69]}..."
        warnings.append(
            f"image_alt — `{preview}` looks like an English slug/identifier; "
            f"use descriptive localized alt (PR #13407)"
        )
        if len(warnings) >= 12:
            break
    return warnings


def check_untranslated(english_content, translated_content):
    """Detect large blocks of English prose left verbatim in the translation."""
    _, en_body = _extract_front_matter(english_content)
    _, tr_body = _extract_front_matter(translated_content)

    strip_patterns = [
        (re.compile(r'```.*?```', re.DOTALL), ''),
        (re.compile(r'\{[%{].*?[%}]\}'), ''),
        (re.compile(r'`[^`]+`'), ''),
        (re.compile(r'\]\([^)]+\)'), ''),
        (re.compile(r'https?://\S+'), ''),
        (re.compile(r'^\[\d+\]:\s*\S+.*$', re.MULTILINE), ''),
    ]

    en_clean = en_body
    tr_clean = tr_body
    for pattern, repl in strip_patterns:
        en_clean = pattern.sub(repl, en_clean)
        tr_clean = pattern.sub(repl, tr_clean)

    warnings = []
    for para in re.split(r'\n\s*\n', en_clean):
        text = para.strip()
        if len(text) < UNTRANSLATED_BLOCK_THRESHOLD:
            continue
        if text in tr_clean:
            preview = text[:80].replace('\n', ' ')
            warnings.append(
                f"untranslated — {len(text)}-char English block found verbatim: "
                f"\"{preview}...\""
            )

    return warnings


def check_sibling_terminology_drift(translated_path, translated_content):
    """Warn when same-basename sibling translations in the locale disagree on
    navigation/title/description wording.

    An IA move that relocates ``_docs/a/foo.md`` to ``_docs/b/foo.md`` leaves
    two copies of the translated page (old and new) until orphan cleanup
    runs. Even outside IA moves, two pages sharing a filename almost always
    cover the same concept. When their ``nav_title``, ``article_title``, or
    ``description`` drift apart, a reader jumping between sections sees
    inconsistent labels — the exact issue Copilot flagged on PR #13297.
    """
    path = Path(translated_path)
    try:
        parts = path.relative_to(REPO_ROOT).parts
    except (ValueError, RuntimeError):
        return []
    if len(parts) < 3 or parts[0] != "_lang":
        return []
    lang_dir = parts[1]

    tr_fm, _ = _extract_front_matter(translated_content)
    if not tr_fm:
        return []

    warnings = []
    siblings = _find_sibling_translations(path.name, lang_dir, path)
    # Iterate the same key set the prompt-context injection uses
    # (``_SIBLING_CONTEXT_FM_KEYS``) so the prompt guidance and the QC
    # backstop cannot drift out of sync — Copilot flagged on PR #13303
    # that ``title`` / ``guide_top_header`` drift would never warn when
    # only ``nav_title`` / ``article_title`` / ``description`` were
    # checked.
    for rel, sibling_content in siblings:
        sib_fm, _ = _extract_front_matter(sibling_content)
        if not sib_fm:
            continue
        for key in _SIBLING_CONTEXT_FM_KEYS:
            tr_block = _extract_fm_block(tr_fm, key)
            sib_block = _extract_fm_block(sib_fm, key)
            if not tr_block or not sib_block:
                continue
            if tr_block.strip() == sib_block.strip():
                continue
            tr_line = tr_block.splitlines()[0].strip()
            sib_line = sib_block.splitlines()[0].strip()
            warnings.append(
                f"sibling_terminology_drift — {key} differs from {rel}: "
                f"this page has `{tr_line}` vs sibling `{sib_line}`"
            )
    return warnings


def repair_brazeai_trademark(translated_content):
    """Fix BrazeAI trademark formatting: only TM should be in <sup>, not the product name.
    Handles trailing language particles/suffixes inside the tag (e.g. <sup>BrazeAITM의</sup>
    in Korean, <sup>BrazeAITMで</sup> in Japanese) by moving them after BrazeAI<sup>TM</sup>.
    """
    repairs = []
    patterns = [
        # BrazeAI + TM/™ + optional trailing text inside <sup> (e.g. particles 의, で)
        (re.compile(r'<sup>BrazeAI\s*(?:TM|™)([^<]*)</sup>'), r'BrazeAI<sup>TM</sup>\1',
         'brazeai-tm — BrazeAI+TM in <sup> (trailing moved out) → TM only in <sup>'),
        (re.compile(r'<sup>BrazeAI</sup>\s*(?:TM|™)'), 'BrazeAI<sup>TM</sup>',
         'brazeai-tm — BrazeAI in <sup> with TM after → TM only in <sup>'),
        (re.compile(r'BrazeAI(?:<sup>)?™(?:</sup>)?'), 'BrazeAI<sup>TM</sup>',
         'brazeai-tm — normalized ™ to TM in <sup>'),
        (re.compile(r'BrazeIA'), 'BrazeAI',
         'brazeai-tm — corrected BrazeIA typo to BrazeAI'),
    ]
    for item in patterns:
        pattern, replacement = item[0], item[1]
        message = item[2]
        if pattern.search(translated_content):
            translated_content = pattern.sub(replacement, translated_content)
            repairs.append(message)
    return translated_content, repairs


_SPURIOUS_BOLD_LINK = re.compile(
    # [**label**] that is not a link `[**...**](...)` or reference `[**...**][...]`
    r"\[\*\*([^\]]+?)\*\*\](?!\s*[\(\[])"
)


def repair_spurious_bold_link_wrappers(translated_content: str):
    """Unwrap `[**text**]` when it is not a Markdown link or reference opener.

    Models sometimes emit bracket-wrapped bold instead of `**text**`, which
    renders as a broken link.
    """
    repairs = []

    def _repl(match: re.Match) -> str:
        return f"**{match.group(1)}**"

    new_content, n = _SPURIOUS_BOLD_LINK.subn(_repl, translated_content)
    if n:
        repairs.append(
            f"markdown — unwrapped {n} spurious [**…**] pattern(s) (not a link)"
        )
        return new_content, repairs
    return translated_content, repairs


def repair_de_channels_banners_landing(translated_path, translated_content, lang_key):
    """Normalize German Banners channel landing front matter.

    Auto-translate sometimes leaves English plural \"Banners\" in German YAML;
    the de site uses \"Banner\" for nav titles and natural compounds in prose.
    """
    if lang_key != "de":
        return translated_content, []
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if not rel.endswith("_lang/de/_user_guide/channels/banners.md"):
        return translated_content, []

    repairs = []
    new = translated_content

    if "nav_title: Banners" in new:
        new = new.replace("nav_title: Banners", "nav_title: Banner")
        repairs.append("de-banners-landing — nav_title: Banners → Banner")
    if "article_title: Banners" in new:
        new = new.replace("article_title: Banners", "article_title: Banner")
        repairs.append("de-banners-landing — article_title: Banners → Banner")
    if "Braze-Banners-Kanal" in new:
        new = new.replace("Braze-Banners-Kanal", "Braze-Banner-Kanal")
        repairs.append("de-banners-landing — Braze-Banner-Kanal compound")
    if "zum Erstellen von Banners" in new:
        new = new.replace("zum Erstellen von Banners", "zum Erstellen von Bannern")
        repairs.append("de-banners-landing — Bannern in description")

    if new != translated_content:
        return new, repairs
    return translated_content, []


def repair_user_guide_data_distribution_landing(
    translated_path, translated_content, lang_key
):
    """Fix Snowflake blurb and DE YAML on the data distribution landing.

    English ``campaign data`` in the Snowflake paragraph is generic analytics
    copy, not the Braze **Campaign** UI token; models sometimes emit raw
    English *Campaign* into KO/JA/DE (Copilot PR #13308). German featured
    cards sometimes drop the hyphen in ``Braze-Daten``.
    """
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/" not in rel or not rel.endswith("_user_guide/data/distribution.md"):
        return translated_content, []

    repairs = []
    new = translated_content

    if lang_key == "ko" and "Campaign 데이터" in new:
        new = new.replace("Campaign 데이터", "캠페인 데이터", 1)
        repairs.append(
            "data-distribution-landing — Campaign 데이터 → 캠페인 데이터 "
            "(Snowflake blurb)"
        )
    if lang_key == "ja":
        if "Campaign データ" in new:
            new = new.replace("Campaign データ", "キャンペーンデータ", 1)
            repairs.append(
                "data-distribution-landing — Campaign データ → キャンペーンデータ "
                "(Snowflake blurb)"
            )
        elif "Campaignデータ" in new:
            new = new.replace("Campaignデータ", "キャンペーンデータ", 1)
            repairs.append(
                "data-distribution-landing — Campaignデータ → キャンペーンデータ "
                "(Snowflake blurb)"
            )
    if lang_key == "de":
        if "Campaign-Daten" in new:
            new = new.replace("Campaign-Daten", "Kampagnendaten", 1)
            repairs.append(
                "data-distribution-landing — Campaign-Daten → Kampagnendaten "
                "(Snowflake blurb)"
            )
        if "  - name: Braze Daten exportieren\n" in new:
            new = new.replace(
                "  - name: Braze Daten exportieren\n",
                "  - name: Braze-Daten exportieren\n",
                1,
            )
            repairs.append(
                "data-distribution-landing — Braze Daten → Braze-Daten "
                "(featured_list)"
            )

    if new != translated_content:
        return new, repairs
    return translated_content, []


_SHELL_FENCE_LANGS = {"", "bash", "sh", "shell", "zsh", "console"}
_JSON_OR_SHELL_FENCE_LANGS = _SHELL_FENCE_LANGS | {"json"}
# Single-backtick inline code span containing at least one `\"` escape. We
# disallow internal backticks and newlines so we don't greedily span across
# unrelated code spans.
_INLINE_CODE_WITH_ESCAPED_QUOTE_RE = re.compile(
    r"(?<!`)`([^`\n]*\\\"[^`\n]*)`(?!`)"
)
# Lines that start a `curl`-style command but misspell the binary as `url`.
# Requires a common curl flag on the same line so we don't rewrite prose.
_URL_CURL_TYPO_RE = re.compile(
    r"^(\s*)url(\s+-[A-Za-z]|\s+https?://)"
)
# Keys in Braze API payloads whose values are always JSON strings. If any of
# these shows up unquoted inside a JSON-ish code fence, that is invalid JSON
# (the canonical offender on Canvas/API docs is ``external_user_id``).
_JSON_STRING_VALUE_KEYS = (
    "external_user_id",
    "external_id",
    "api_key",
    "canvas_id",
    "campaign_id",
    "event_name",
    "email_address",
    "user_alias",
)
_JSON_UNQUOTED_VALUE_RE = re.compile(
    r'^(?P<prefix>\s*"(?P<key>'
    + "|".join(re.escape(k) for k in _JSON_STRING_VALUE_KEYS)
    + r')"\s*:\s*)'
    r'(?P<value>[A-Za-z_][A-Za-z0-9_]*)'
    r'(?P<suffix>\s*[,}])'
)


def _iter_fenced_code_blocks(text):
    """Yield ``(start_line, end_line, lang)`` for triple-backtick fences.

    ``start_line`` / ``end_line`` are line-index positions of the opening and
    closing fence lines; content lines are ``start_line+1 .. end_line-1``.
    """
    lines = text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        stripped = lines[i].lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            lang = stripped[3:].strip().lower()
            j = i + 1
            while j < n:
                s2 = lines[j].lstrip()
                if s2.startswith(marker):
                    break
                j += 1
            yield i, j, lang
            i = j + 1
        else:
            i += 1


def repair_inline_code_escaped_quotes(content):
    """Unescape ``\\"`` inside single-backtick inline code spans.

    Inside an inline code span the content is literal, so ``\\"`` renders as
    ``\\"`` on the page — almost always a copy/paste bug from a JSON string
    literal that leaked its shell/JSON escaping into prose. We keep the
    backticks, just drop the backslashes.
    """
    repairs = []

    def repl(match):
        inner = match.group(1)
        new_inner = inner.replace('\\"', '"')
        if new_inner != inner:
            preview = new_inner if len(new_inner) <= 60 else new_inner[:57] + "..."
            repairs.append(
                f'inline_code — unescaped \\\" → \" in code span (`{preview}`)'
            )
        return f"`{new_inner}`"

    new_content = _INLINE_CODE_WITH_ESCAPED_QUOTE_RE.sub(repl, content)
    return new_content, repairs


def repair_curl_typo_url_in_code_fence(content):
    """Rewrite ``url -X POST`` → ``curl -X POST`` inside shell code fences."""
    repairs = []
    lines = content.split("\n")
    changed = False
    for start, end, lang in _iter_fenced_code_blocks(content):
        if lang not in _SHELL_FENCE_LANGS:
            continue
        for idx in range(start + 1, end):
            if idx >= len(lines):
                break
            m = _URL_CURL_TYPO_RE.match(lines[idx])
            if not m:
                continue
            lines[idx] = _URL_CURL_TYPO_RE.sub(r"\1curl\2", lines[idx], count=1)
            changed = True
            repairs.append("code_fence — `url -X` → `curl -X` (binary typo)")
    if not changed:
        return content, []
    return "\n".join(lines), repairs


def repair_unquoted_json_string_values(content):
    """Quote known-string JSON values inside JSON / shell code fences.

    Catches samples like ``"external_user_id": Customer_123,`` where the
    value was clearly meant to be a string but lost its quotes. Keys are
    restricted to a well-known Braze-API set so we don't touch fields that
    might legitimately be numbers (``canvas_entry_properties``, etc.).
    """
    repairs = []
    lines = content.split("\n")
    changed = False
    for start, end, lang in _iter_fenced_code_blocks(content):
        if lang not in _JSON_OR_SHELL_FENCE_LANGS:
            continue
        for idx in range(start + 1, end):
            if idx >= len(lines):
                break
            m = _JSON_UNQUOTED_VALUE_RE.match(lines[idx])
            if not m:
                continue
            value = m.group("value")
            if value in {"true", "false", "null"}:
                continue
            new_line = (
                m.group("prefix")
                + f'"{value}"'
                + m.group("suffix")
                + lines[idx][m.end():]
            )
            if new_line != lines[idx]:
                lines[idx] = new_line
                changed = True
                repairs.append(
                    f'json — quoted "{m.group("key")}" value ({value}) to keep JSON valid'
                )
    if not changed:
        return content, []
    return "\n".join(lines), repairs


_HEADING_LINE_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_EXPLICIT_ID_RE = re.compile(r"\{#[A-Za-z][A-Za-z0-9_\-:\.]*\}\s*$")
_ANCHOR_REF_RE = re.compile(r"\]\(#([A-Za-z][A-Za-z0-9_\-]*)\)")


def _auto_slug(text: str) -> str:
    """Best-effort Kramdown auto-slug for an ASCII heading.

    This is intentionally conservative: we only emit slugs for headings whose
    text is ASCII (so the English counterpart produces a stable slug). This is
    all we need, because we only look up English headings for references.
    """
    # Drop emphasis/backtick markers only — keep ``_`` so identifiers like
    # ``send_to_existing_only`` survive into the slug (PR #13623).
    text = re.sub(r"[*`]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s\-_]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def _iter_doc_headings(text):
    """Yield ``(line_index, level, heading_text, explicit_id_or_None)``.

    Skips front matter and fenced code blocks so we don't pick up ``#`` lines
    that live inside shell/markdown examples.
    """
    lines = text.split("\n")
    in_fm = False
    fm_done = False
    in_fence = False
    fence_marker = ""
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if not fm_done and i == 0 and stripped.strip() == "---":
            in_fm = True
            continue
        if in_fm:
            if stripped.strip() == "---":
                in_fm = False
                fm_done = True
            continue
        if in_fence:
            if stripped.lstrip().startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            continue
        lstr = stripped.lstrip()
        if lstr.startswith("```") or lstr.startswith("~~~"):
            in_fence = True
            fence_marker = lstr[:3]
            continue
        m = _HEADING_LINE_RE.match(stripped)
        if not m:
            continue
        heading_text = m.group(2)
        explicit = None
        em = _EXPLICIT_ID_RE.search(heading_text)
        if em:
            explicit = em.group(0).strip()[2:-1]
            heading_text = heading_text[: em.start()].rstrip()
        yield i, m.group(1), heading_text, explicit


_DUPLICATE_ADJACENT_EXPLICIT_ANCHOR_RE = re.compile(
    r"(\{#[A-Za-z][A-Za-z0-9_\-:\.]*\})(?:\s+\1)+"
)


_TRANSACTIONAL_EMAIL_FREQ_CAP_FRAGMENT = (
    "{{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/"
)
_SHOW_DATA_ENTIRE_CAMPAIGN_ANCHOR = "{#show-data-by-entire-campaign-or-canvas}"


def repair_frequency_capping_transactional_outer_paren(
    translated_path, translated_content,
):
    """Restore a missing outer ``)`` after the transactional-email link bullet.

    English wraps the link in parentheses ending in ``…/))`` (link ``)`` plus
    parenthetical ``)``). Some locales drop the final ``)``, leaving
    ``…email/)`` at EOL and breaking the list (Cursor Bugbot / auto-translate
    PR #13514).
    """
    rel = str(translated_path).replace("\\", "/")
    if "/messaging/messaging_fundamentals/frequency_capping.md" not in rel:
        return translated_content, []
    needle = _TRANSACTIONAL_EMAIL_FREQ_CAP_FRAGMENT
    changed = False
    out_parts = []
    for line in translated_content.splitlines(keepends=True):
        core = line.rstrip("\r\n")
        sep = line[len(core):]
        s = core.rstrip()
        if needle in core and s.endswith("/)"):
            core = s + ")" + core[len(s):]
            changed = True
        out_parts.append(core + sep)
    if not changed:
        return translated_content, []
    return "".join(out_parts), [
        "md_paren — added missing ) after transactional email link in "
        "frequency_capping (PR #13514)"
    ]


def repair_duplicate_engagement_show_data_sections(
    translated_path, translated_content,
):
    """Remove a duplicated ``##### … {#show-data-by-entire-campaign-or-canvas}`` block.

    Auto-translation sometimes pasted the same subsection twice with the same
    explicit Kramdown ID, duplicating HTML anchors (Cursor Bugbot /
    auto-translate PR #13514).
    """
    rel = str(translated_path).replace("\\", "/")
    if "analytics/reports/engagement_reports.md" not in rel:
        return translated_content, []
    if translated_content.count(_SHOW_DATA_ENTIRE_CAMPAIGN_ANCHOR) < 2:
        return translated_content, []

    repairs = []
    content = translated_content
    while True:
        lines = content.splitlines(keepends=True)
        idxs = [
            i for i, L in enumerate(lines)
            if _SHOW_DATA_ENTIRE_CAMPAIGN_ANCHOR in L
            and re.match(r"^#{5}\s", L)
        ]
        if len(idxs) < 2:
            break
        i0, i1 = idxs[0], idxs[1]
        if lines[i0].strip() != lines[i1].strip():
            break
        content = "".join(lines[:i0] + lines[i1:])
        repairs.append(
            "dedupe — removed duplicate «Show data by entire campaign» subsection "
            "(PR #13514)"
        )

    if not repairs:
        return translated_content, []
    return content, repairs


def repair_duplicate_adjacent_explicit_heading_anchors(translated_content):
    """Collapse repeated identical ``{#id}`` tokens on the same markdown heading.

    The model (or anchor repair + model) sometimes emits ``## Title {#x} {#x}``,
    which duplicates HTML ``id`` attributes (Copilot / auto-translate PR #13353).
    Only heading lines (``#`` … at SOL) are modified.
    """
    repairs = []
    lines = translated_content.split("\n")
    out_lines = []
    for line in lines:
        if re.match(r"^#{1,6}\s+", line):
            new_line, n = _DUPLICATE_ADJACENT_EXPLICIT_ANCHOR_RE.subn(r"\1", line)
            if n:
                repairs.append(
                    f"heading_anchor — collapsed duplicate explicit {{#…}} ({n})"
                )
                line = new_line
        out_lines.append(line)
    new_content = "\n".join(out_lines)
    if new_content != translated_content:
        return new_content, repairs
    return translated_content, []


def repair_same_page_anchor_ids(english_content, translated_content):
    """Preserve English same-page anchor slugs on localized headings.

    When an English doc contains ``](#slug)`` references whose slug matches
    the auto-slug of one of its own headings, the translated doc loses those
    anchors because the localized heading auto-slugs to a different value.
    We add an explicit ``{#slug}`` to the corresponding translated heading
    (matched by positional index) so the existing link targets keep working.

    Also, when the translated heading text would auto-slug to something
    **different** from the English heading (CJK and most localized titles),
    we still add the English slug so **bookmark / cross-locale** ``#fragment``
    URLs keep resolving (Copilot PR #13319 — JA drag-and-drop FAQ, AMP for
    email).

    Conservative by design:
      * Slug always comes from the English (or explicit ``{#id}`` on English).
      * Skips when the translated heading already has the same auto-slug as
        English **and** the slug is not referenced in-file (avoids redundant
        churn on all-ASCII pages).
      * Never overwrites an existing ``{#id}`` on the translated heading.
      * Skips the file if the English and translated heading counts differ
        (structure mismatch → too risky to auto-align).
    """
    referenced = set(_ANCHOR_REF_RE.findall(english_content))
    referenced |= set(_ANCHOR_REF_RE.findall(translated_content))

    en_headings = list(_iter_doc_headings(english_content))
    tr_headings = list(_iter_doc_headings(translated_content))
    if not en_headings or len(en_headings) != len(tr_headings):
        return translated_content, []

    lines = translated_content.split("\n")
    repairs = []
    for (_, _en_lvl, en_text, en_explicit), (tr_idx, _tr_lvl, tr_text, tr_explicit) in zip(
        en_headings, tr_headings
    ):
        slug = en_explicit or _auto_slug(en_text)
        if not slug:
            continue
        if tr_explicit:
            continue
        existing = lines[tr_idx]
        if _EXPLICIT_ID_RE.search(existing):
            continue
        tr_auto = _auto_slug(tr_text)
        if slug not in referenced and tr_auto == slug:
            continue
        new_line = existing.rstrip() + f" {{#{slug}}}"
        if new_line != existing:
            lines[tr_idx] = new_line
            repairs.append(f"anchor_id — added {{#{slug}}} to translated heading")

    if not repairs:
        return translated_content, []
    new_content = "\n".join(lines)
    return new_content, repairs


class CrossLocaleHeadingAnchorConflict(RuntimeError):
    """Raised when two locales disagree on explicit ``{#id}`` for the same heading."""


def _append_explicit_kramdown_anchor_to_heading_line(line: str, anchor: str) -> str:
    """Append `` {#anchor}`` to a heading line that does not already end with an explicit ID."""
    if _EXPLICIT_ID_RE.search(line.rstrip()):
        return line
    nl = "\n" if line.endswith("\n") else ""
    core = line[:-1] if line.endswith("\n") else line
    return core.rstrip() + f" {{#{anchor}}}" + nl


def _canon_paths_from_translation_results(repo_root: Path) -> Optional[Set[str]]:
    """Return unique locale-relative paths (``_user_guide/...``) from ``translation_results.json``.

    Returns ``None`` when the results file is missing.
    """
    tr_path = repo_root / "translation_results.json"
    if not tr_path.is_file():
        return None
    data = json.loads(tr_path.read_text(encoding="utf-8"))
    valid_root = {info["dir"] for info in LANGUAGES.values()}
    canon_paths: set[str] = set()
    for entry in data.get("translated") or []:
        tgt = entry.get("target")
        if not tgt or not isinstance(tgt, str):
            continue
        parts = Path(tgt).as_posix().split("/")
        if len(parts) < 3 or parts[0] != "_lang" or parts[1] not in valid_root:
            continue
        canon_paths.add("/".join(parts[2:]))
    return canon_paths


def align_cross_locale_heading_anchors(repo_root: Path, *, full_repo_scan: bool = False):
    """Copy explicit Kramdown ``{#id}`` tails across locale mirrors when any sibling has one.

    Matrix jobs translate independently; one locale may keep or add a stable
    ``{#fragment}`` while another omits it even when English has no explicit ID
    and auto-slugs match—breaking cross-locale deep links (Copilot /
    auto-translate PR #13394).

    By default only paths listed in ``translation_results.json`` (same paths the
    workflow just merged) are scanned so a run does not touch unrelated
    localized files. Pass ``full_repo_scan=True`` for a rare whole-tree pass.

    For each markdown path, when two or more locale files exist and heading
    counts agree, if any locale exposes an explicit ID at heading index ``i``,
    every sibling file receives that same ID on the corresponding heading line.
    Conflicting IDs at the same index skip that file with a log line.

    Returns:
        ``(files_updated: int, log_lines: list[str])``
    """
    _lang = repo_root / "_lang"
    log_lines: list[str] = []
    if not _lang.is_dir():
        return 0, ["align-heading-anchor-parity: no `_lang/` directory — skipping."]

    # Skip ``_api/`` (REST reference) — locales sometimes use different Kramdown
    # slug spellings for the same English heading, so there is no safe automatic
    # winner. Product docs under the prefixes below benefit most from stable
    # cross-locale ``#fragment`` parity (auto-translate PR #13394).
    _ALIGN_REL_PREFIXES = ("_user_guide/", "_developer_guide/", "_contributing/")

    locale_dirs = [info["dir"] for info in LANGUAGES.values()]
    canon_to_lang_paths: dict[str, dict[str, Path]] = {}

    if full_repo_scan:
        for lang_dir in locale_dirs:
            root = _lang / lang_dir
            if not root.is_dir():
                continue
            for md in root.rglob("*.md"):
                rel = md.relative_to(root).as_posix()
                if not rel.startswith(_ALIGN_REL_PREFIXES):
                    continue
                canon_to_lang_paths.setdefault(rel, {})[lang_dir] = md
    else:
        canon_set = _canon_paths_from_translation_results(repo_root)
        if canon_set is None:
            return 0, [
                "align-heading-anchor-parity: translation_results.json not found — "
                "nothing to do (pass --full-repo to scan all `_lang/` markdown)."
            ]
        if not canon_set:
            return 0, [
                "align-heading-anchor-parity: translated list empty — nothing to do."
            ]
        for canon in sorted(canon_set):
            if not canon.startswith(_ALIGN_REL_PREFIXES):
                continue
            by_lang: dict[str, Path] = {}
            for lang_dir in locale_dirs:
                pth = _lang / lang_dir / canon
                if pth.is_file():
                    by_lang[lang_dir] = pth
            if len(by_lang) >= 2:
                canon_to_lang_paths[canon] = by_lang

    files_updated = 0
    for canon in sorted(canon_to_lang_paths):
        paths_by_lang = canon_to_lang_paths[canon]
        if len(paths_by_lang) < 2:
            continue

        per_lang_heads: dict[str, list] = {}
        for lang_dir, p in paths_by_lang.items():
            text = p.read_text(encoding="utf-8")
            per_lang_heads[lang_dir] = list(_iter_doc_headings(text))

        counts = {ld: len(per_lang_heads[ld]) for ld in paths_by_lang}
        if len(set(counts.values())) != 1:
            log_lines.append(
                f"align-heading-anchor-parity: skip `{canon}` — "
                f"heading count mismatch across locales: {counts!r}"
            )
            continue
        n = next(iter(counts.values()))
        if n == 0:
            continue

        canonical_by_i: dict[int, Optional[str]] = {}
        conflict = False
        for i in range(n):
            ids_at_i = []
            for lang_dir in paths_by_lang:
                _, _lvl, _text, explicit = per_lang_heads[lang_dir][i]
                ids_at_i.append(explicit)
            non_null = [x for x in ids_at_i if x]
            if not non_null:
                canonical_by_i[i] = None
                continue
            unique = set(non_null)
            if len(unique) > 1:
                log_lines.append(
                    f"align-heading-anchor-parity: skip `{canon}` — conflicting "
                    f"explicit heading IDs at index {i}: {sorted(unique)!r}"
                )
                conflict = True
                break
            canonical_by_i[i] = non_null[0]

        if conflict:
            continue

        edits: dict[Path, dict[int, str]] = {}
        for i, canonical_id in canonical_by_i.items():
            if not canonical_id:
                continue
            for lang_dir, p in paths_by_lang.items():
                tr_idx, _lvl, _text, tr_expl = per_lang_heads[lang_dir][i]
                if tr_expl == canonical_id:
                    continue
                edits.setdefault(p, {})[tr_idx] = canonical_id

        for path, idx_to_anchor in edits.items():
            text = path.read_text(encoding="utf-8")
            ends_nl = text.endswith("\n")
            lines = text.split("\n")
            for idx, anchor in sorted(idx_to_anchor.items()):
                if idx >= len(lines):
                    raise CrossLocaleHeadingAnchorConflict(
                        f"align-heading-anchor-parity: line index {idx} out of range "
                        f"for `{path.relative_to(repo_root)}`"
                    )
                lines[idx] = _append_explicit_kramdown_anchor_to_heading_line(
                    lines[idx], anchor
                )
            new_text = "\n".join(lines)
            if ends_nl and not new_text.endswith("\n"):
                new_text += "\n"
            path.write_text(new_text, encoding="utf-8")
            files_updated += 1
            n_edits = len(idx_to_anchor)
            log_lines.append(
                f"align-heading-anchor-parity: updated "
                f"`{path.relative_to(repo_root).as_posix()}` ({n_edits} heading(s))"
            )

    return files_updated, log_lines


def repair_unreferenced_explicit_heading_ids_when_english_has_none(
    english_content, translated_content
):
    """Remove translated-only ``{#id}`` when English omits explicit ids and id is unused.

    The model sometimes pastes long pseudo-slugs (often echoing UI or image
    text) onto headings. If the English heading has no explicit Kramdown id and
    nothing in either file references that fragment, drop the extra tail so
    ``repair_same_page_anchor_ids`` can attach the correct English slug when
    links require it (Copilot / auto-translate PR #13384).
    """
    en_headings = list(_iter_doc_headings(english_content))
    tr_headings = list(_iter_doc_headings(translated_content))
    if not en_headings or len(en_headings) != len(tr_headings):
        return translated_content, []

    referenced = set(_ANCHOR_REF_RE.findall(english_content))
    referenced |= set(_ANCHOR_REF_RE.findall(translated_content))
    for blob in (english_content, translated_content):
        referenced |= set(
            re.findall(
                r'(?i)href\s*=\s*["\']#([A-Za-z][A-Za-z0-9_\-]*)',
                blob,
            )
        )

    lines = translated_content.split("\n")
    repairs = []
    for (_, _en_lvl, _en_text, en_explicit), (tr_idx, _tr_lvl, tr_text, tr_explicit) in zip(
        en_headings, tr_headings
    ):
        if en_explicit is not None or not tr_explicit:
            continue
        if tr_explicit in referenced:
            continue
        line = lines[tr_idx]
        stripped = line.rstrip()
        new_stripped = re.sub(
            r"\s*\{#" + re.escape(tr_explicit) + r"\}\s*$",
            "",
            stripped,
        )
        if new_stripped == stripped:
            continue
        lines[tr_idx] = new_stripped
        slug_note = tr_explicit if len(tr_explicit) <= 72 else tr_explicit[:72] + "…"
        repairs.append(
            "heading_anchor — removed translated-only explicit "
            f"{{#{slug_note}}} (English has none; unused in-file; PR #13384)"
        )

    if not repairs:
        return translated_content, []
    new_content = "\n".join(lines)
    if translated_content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    return new_content, repairs


_STYLE_BLOCK_OPEN_RE = re.compile(r"<style\b", re.I)
_STYLE_BLOCK_CLOSE_RE = re.compile(r"</style\s*>", re.I)


def repair_css_nth_child_trailing_comma_in_style_blocks(content):
    """Fix ``nth-child(N), {`` → ``nth-child(N) {`` inside ``<style>`` blocks.

    A stray comma before ``{`` is invalid CSS and breaks table width rules
    (Copilot / auto-translate PR #13384).
    """
    lines = content.split("\n")
    out_lines = []
    in_style = False
    repairs = []
    total = 0

    for line in lines:
        if _STYLE_BLOCK_OPEN_RE.search(line):
            in_style = True
        modified = line
        if in_style:
            new_line, n = re.subn(
                r"nth-child\((\d+)\),\s*\{",
                r"nth-child(\1) {",
                modified,
            )
            if n:
                total += n
                modified = new_line
        out_lines.append(modified)
        if _STYLE_BLOCK_CLOSE_RE.search(line):
            in_style = False

    if not total:
        return content, []
    new_content = "\n".join(out_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    repairs.append(
        "css_style — removed stray comma before `{` in nth-child selector "
        f"({total}x; PR #13384)"
    )
    return new_content, repairs


_UI_ARIA_EN_PHRASES = {
    "Open navigation menu": {
        "de": "Navigationsmenü öffnen",
        "es": "Abrir el menú de navegación",
        "fr": "Ouvrir le menu de navigation",
        "ja": "ナビゲーションメニューを開く",
        "ko": "탐색 메뉴 열기",
        "pt-br": "Abrir o menu de navegação",
    },
    "Select your language": {
        "de": "Sprache auswählen",
        "es": "Seleccionar el idioma",
        "fr": "Sélectionner la langue",
        "ja": "言語を選択",
        "ko": "언어 선택",
        "pt-br": "Selecionar o idioma",
    },
}


def repair_documentation_english_aria_labels(translated_content, lang_key):
    """Swap known English ``aria-label`` strings for locale text in translated docs."""
    repairs = []
    new_content = translated_content
    for english_phrase, lang_map in _UI_ARIA_EN_PHRASES.items():
        localized = lang_map.get(lang_key)
        if not localized:
            continue
        old = f'aria-label="{english_phrase}"'
        new = f'aria-label="{localized}"'
        if old in new_content:
            new_content = new_content.replace(old, new)
            repairs.append(
                f"aria_label — {english_phrase!r} → localized (PR #13384)"
            )
    if new_content == translated_content:
        return translated_content, []
    return new_content, repairs


def repair_trailing_whitespace(translated_content: str):
    """Strip trailing spaces and tabs from each line (preserve newlines)."""
    lines = translated_content.split("\n")
    stripped = [ln.rstrip(" \t") for ln in lines]
    new_content = "\n".join(stripped)
    if translated_content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    if new_content != translated_content:
        return new_content, ["trailing_whitespace — removed end-of-line spaces/tabs"]
    return translated_content, []


_JA_CAMPAIGN_COMPOSER_UI = [
    ("**Target Audiences**", "**ターゲットオーディエンス**"),
    ("**Schedule Delivery**", "**配信をスケジュール**"),
    ("**Action-Based Delivery**", "**アクションベースの配信**"),
    ("**Action-Based**", "**アクションベース**"),
    ("**Perform Custom Event**", "**カスタムイベントを実行**"),
    ("**Perform a Back in Stock Event**", "**再入荷イベントを実行**"),
    ("**Start Time (Required)**", "**開始時刻 (必須)**"),
    ("**Edit email body**", "**メール本文を編集**"),
    ("**Campaign Monitoring**", "**キャンペーンモニタリング**"),
    ("**Set Up Alert**", "**アラートを設定**"),
    ("**Send an SMS Inbound Message**", "**SMS インバウンドメッセージを送信**"),
    ("**SMSインバウンドメッセージを送信する**", "**SMS インバウンドメッセージを送信**"),
    ("SMSインバウンドメッセージを送信する", "SMS インバウンドメッセージを送信"),
    ("**Send a WhatsApp inbound message**", "**WhatsApp インバウンドメッセージを送信**"),
    ("**WhatsAppインバウンドメッセージを送信する**", "**WhatsApp インバウンドメッセージを送信**"),
    ("WhatsAppインバウンドメッセージを送信する", "WhatsApp インバウンドメッセージを送信"),
    ("**Entry Audience**", "**エントリオーディエンス**"),
    ("**Delivery Controls**", "**配信コントロール**"),
    ("「Delivery Controls」", "「配信コントロール」"),
    ("**Send Settings:**", "**送信設定:**"),
    ("**Send Settings**", "**送信設定**"),
    ("**Audience Summary**", "**オーディエンスの概要**"),
    ("**User Lookup**", "**ユーザー検索**"),
    ("**Review Summary**", "**レビューサマリー**"),
    ("**Send to these users**", "**これらのユーザーに送信**"),
    ("**Multichannel キャンペーン**", "**マルチチャネル キャンペーン**"),
    ("**Multichannel**", "**マルチチャネル**"),
    ("**Add channel**", "**チャネルを追加**"),
    ("**Add Variant**", "**バリアントを追加**"),
    ("**Copy from Variant**", "**バリアントからコピー**"),
    ("**Create Campaign**", "**キャンペーンを作成**"),
    ("**Create キャンペーン**", "**キャンペーンを作成**"),
    ("**Audience** > **Search Users**", "**オーディエンス** > **ユーザーを検索**"),
    ("**Settings** > **API Keys**", "**設定** > **API キー**"),
    ("**Settings** > **App Settings** > **+ Add App**", "**設定** > **アプリ設定** > **アプリを追加**"),
    ("**Search Users**", "**ユーザーを検索**"),
    ("**View User Event Properties**", "**ユーザーイベントプロパティを表示**"),
    ("**Target Audience**", "**ターゲットオーディエンス**"),
    ("**Entry Schedule**", "**エントリスケジュール**"),
    ("**Pending Approval**", "**承認待ち**"),
    ("**Summary**ステップ", "**レビューサマリー**ステップ"),
    ("**Summary** step", "**レビューサマリー**ステップ"),
    ("キャンペーンコンポーザーの**Schedule**", "キャンペーンコンポーザーの**配信をスケジュール**"),
    ("campaign composer's **Schedule**", "campaign composer's **配信をスケジュール**"),
    ("**Schedule**部分", "**配信をスケジュール**部分"),
    (
        "**Allow users to become re-eligible to receive campaign**",
        "**ユーザーがキャンペーンを再度受信できるようにする**",
    ),
    ("**Approved**", "**承認済み**"),
    ("[**Target Audiences (ターゲットオーディエンス)**]", "**ターゲットオーディエンス**"),
    ("「User Lookup」", "「ユーザー検索」"),
    ("「Lookup User」", "「ユーザーを検索」"),
    ("「Schedule Delivery」", "「配信をスケジュール」"),
    ("「Send Settings」", "「送信設定」"),
    ("Schedule Deliveryステップ", "配信をスケジュールステップ"),
]


def repair_ja_campaign_composer_ui(translated_path, translated_content, lang_key):
    """Localize leaked English campaign-composer wizard labels in Japanese docs."""
    if lang_key != "ja":
        return translated_content, []

    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "_lang/ja/" not in rel:
        return translated_content, []

    from _glossary_locale_propagation import replace_outside_fences  # noqa: WPS433

    repairs = []
    new = translated_content
    for old, new_label in _JA_CAMPAIGN_COMPOSER_UI:
        if old not in new:
            continue
        updated, count = replace_outside_fences(new, old, new_label)
        if count:
            new = updated
            repairs.append(
                "ja_campaign_composer_ui — "
                f"{old.strip('*')} → {new_label.strip('*')}"
            )

    if new != translated_content:
        return new, repairs
    return translated_content, []


def repair_messaging_ab_testing_locale_drift(
    translated_path, translated_content, lang_key
):
    """Fix recurring A/B testing subtree copy drift (auto-translate PR #13359)."""
    rel = Path(translated_path).as_posix().replace("\\", "/")
    if "messaging/ab_testing" not in rel:
        return translated_content, []

    repairs = []
    new = translated_content

    def _apply(old, new_s, label):
        nonlocal new, repairs
        if old in new:
            new = new.replace(old, new_s)
            repairs.append(label)

    if lang_key == "pt-br":
        if rel.endswith("_user_guide/messaging/ab_testing/concepts.md"):
            _apply(
                "números aleatórios de baldes",
                "números de bucket aleatórios",
                "pt_ab_concepts — baldes → bucket (random bucket copy)",
            )
            _apply(
                "Números aleatórios de baldes",
                "Números de bucket aleatórios",
                "pt_ab_concepts — featured list bucket label",
            )
        if rel.endswith("_user_guide/messaging/ab_testing/optimizations.md"):
            _apply(
                "localizadas na **Etapa de Públicos-alvo**",
                "localizadas na etapa **Públicos-alvo**",
                "pt_ab_optim — Target Audiences step wording",
            )
            _apply(
                "article_title: Otimize os Testes A/B com variante vencedora ou personalizadas\n",
                "article_title: Otimize os testes A/B com variantes vencedoras ou personalizadas\n",
                "pt_ab_optim — article_title plural parallelism",
            )
            _apply(
                "# Otimize os Testes A/B com Variante vencedora ou Variantes personalizadas ",
                "# Otimize os testes A/B com variantes vencedoras ou personalizadas ",
                "pt_ab_optim — H1 plural parallelism",
            )

    if lang_key == "es":
        if rel.endswith("_user_guide/messaging/ab_testing/concepts/race_conditions.md"):
            _apply("nav_title: Condiciones de la carrera\n", "nav_title: Condiciones de carrera\n", "es_race — nav race-condition term")
            _apply("\n# Condiciones de la carrera {#race-conditions}", "\n# Condiciones de carrera {#race-conditions}", "es_race — H1 race-condition term")
            for n in (1, 2, 3):
                _apply(f"## Supuesto {n}:", f"## Escenario {n}:", f"es_race — Supuesto {n} → Escenario")
        if rel.endswith("_user_guide/messaging/ab_testing/concepts.md"):
            _apply(
                "  - name: Condiciones de la carrera\n",
                "  - name: Condiciones de carrera\n",
                "es_ab_concepts — race conditions card label",
            )
        if rel.endswith("_user_guide/messaging/ab_testing/concepts/variant_distribution.md"):
            _apply(" una campaign ", " una campaña ", "es_variant_dist — campaign → campaña")
            _apply("una campaign multivariante", "una campaña multivariante", "es_variant_dist — campaign multivariante")
            _apply("tu campaign tiene", "tu campaña tiene", "es_variant_dist — tu campaign → tu campaña")
        if rel.endswith("_user_guide/messaging/ab_testing/concepts/random_bucket_numbers.md"):
            _apply(
                "En la sección **Público objetivo** de tu campaña",
                "En la sección **Target Audiences** de tu campaña",
                "es_random_bucket — UI Target Audiences",
            )
        if rel.endswith("_user_guide/messaging/ab_testing/ab_test_projection.md"):
            _apply(
                "ve al paso **Público objetivo** del flujo",
                "ve al paso **Target Audience** del flujo",
                "es_ab_projection — Target Audience UI",
            )
            _apply(
                "En el panel **Pruebas A/B**, selecciona **Run Projection**.",
                "En el panel **A/B Testing**, selecciona **Run Projection**.",
                "es_ab_projection — A/B Testing panel UI",
            )
        if rel.endswith("_user_guide/messaging/ab_testing/optimizations.md"):
            _apply(
                "article_title: Optimiza las pruebas A/B con Variantes Ganadoras o Variantes Personalizadas\n",
                "article_title: Optimiza las pruebas A/B con variantes ganadoras o variantes personalizadas\n",
                "es_ab_optim — sentence-case article_title",
            )
            _apply(
                "# Optimiza las pruebas A/B con Variantes Ganadoras o Variantes Personalizadas ",
                "# Optimiza las pruebas A/B con variantes ganadoras o variantes personalizadas ",
                "es_ab_optim — sentence-case H1",
            )
            _apply("\n## Variante Ganadora {#winning-variant}", "\n## Variante ganadora {#winning-variant}", "es_ab_optim — sentence-case H2 winning")
            _apply(
                "\n## Variante Personalizada {#personalized-variant}",
                "\n## Variante personalizada {#personalized-variant}",
                "es_ab_optim — sentence-case H2 personalized",
            )

    if lang_key == "ko" and rel.endswith("_user_guide/messaging/ab_testing/optimizations.md"):
        _apply("WhatsApp Campaign에", "WhatsApp Campaigns에", "ko_ab_optim — WhatsApp Campaigns plural")

    if lang_key == "ja":
        if rel.endswith("_user_guide/messaging/ab_testing/ab_test_projection.md"):
            _apply("**投影の実行**", "**予測を実行**", "ja_ab_projection — run projection verb parity")

    if lang_key == "de":
        if rel.endswith("_user_guide/messaging/ab_testing/optimizations.md"):
            _apply(
                "article_title: Optimieren Sie A/B-Tests mit Winning-Varianten oder personalisierten Varianten\n",
                "article_title: Optimieren Sie A/B-Tests mit Gewinnervariante oder personalisierten Varianten\n",
                "de_ab_optim — article_title German winner term",
            )
            _apply(
                "# Optimieren Sie A/B-Tests mit Winning-Varianten oder personalisierten Varianten ",
                "# Optimieren Sie A/B-Tests mit Gewinnervariante oder personalisierten Varianten ",
                "de_ab_optim — H1 German winner term",
            )
            _apply("**Gewinnende Variante**", "**Gewinnervariante**", "de_ab_optim — Gewinnende → Gewinnervariante")
            _apply("Gewinnende Variante und Personalisierte", "Gewinnervariante und Personalisierte", "de_ab_optim — alt Gewinnende")
            _apply("**Winning Variant**", "**Gewinnervariante**", "de_ab_optim — Winning Variant UI")
            _apply("**Personalized Variant**", "**Personalisierte Variante**", "de_ab_optim — Personalized Variant UI")
        if rel.endswith("_user_guide/messaging/ab_testing/concepts/conversion_correlation.md"):
            _apply(
                "welche Benutzerattribute und Verhaltensweisen die von Ihnen",
                "welche Nutzerattribute und Verhaltensweisen von Nutzer:innen die von Ihnen",
                "de_ab_convcorr — callout Nutzerattribute / Nutzer:innen",
            )
            _apply(
                "eine Liste von Attributen und Benutzerverhalten und berechnet, ob Benutzer statistisch",
                "eine Liste von Attributen und dem Verhalten von Nutzer:innen und berechnet, ob Nutzer:innen statistisch",
                "de_ab_convcorr — overview Benutzer → Nutzer:innen",
            )

    if lang_key == "fr" and rel.endswith("_user_guide/messaging/ab_testing/concepts/conversion_correlation.md"):
        _apply(
            "- Les Campaigns et Canvas reçus",
            "- Les campagnes et Canvas reçus",
            "fr_ab_convcorr — campagnes not English Campaigns",
        )

    if new != translated_content:
        return new, repairs
    return translated_content, []


def qc_check_file(english_path, translated_path, lang_key):
    """Run all QC checks on one file pair. Auto-repairs are written back."""
    english_content = Path(english_path).read_text()
    translated_content = Path(translated_path).read_text()

    findings = {
        "file": str(translated_path),
        "lang": lang_key,
        "repairs": [],
        "warnings": [],
    }

    english_content, _ = repair_front_matter_miscapitalized_tool_key(english_content)
    translated_content, tool_key_repairs = (
        repair_front_matter_miscapitalized_tool_key(translated_content)
    )
    findings["repairs"].extend(tool_key_repairs)

    translated_content, fm_strip_repairs = (
        repair_spurious_front_matter_when_english_has_none(
            english_content, translated_content
        )
    )
    findings["repairs"].extend(fm_strip_repairs)

    translated_content, fm_seed_repairs = (
        repair_missing_locale_front_matter_from_english(
            english_content, translated_content
        )
    )
    findings["repairs"].extend(fm_seed_repairs)

    if not english_content.strip():
        if translated_content.strip():
            translated_content = ""
            findings["repairs"].append(
                "empty-source — cleared locale file (English source empty or "
                "whitespace-only; auto-translate PR #13405)"
            )

    translated_content, fm_repairs = repair_front_matter(
        english_content, translated_content
    )
    findings["repairs"].extend(fm_repairs)

    translated_content, cdi_desc_repairs = repair_cdi_segments_description_location_drift(
        english_content, translated_content, translated_path, lang_key
    )
    findings["repairs"].extend(cdi_desc_repairs)

    translated_content, mseg_tool_repairs = repair_managing_segments_tool_yaml_value(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(mseg_tool_repairs)

    translated_content, rfm_nav_repairs = repair_rfm_sql_segments_nav_and_title_mix(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(rfm_nav_repairs)

    translated_content, fm_display_repairs = repair_front_matter_display_scalar_cleanup(
        translated_content
    )
    findings["repairs"].extend(fm_display_repairs)

    translated_content, rel_fm_rule_repairs = repair_releases_spurious_leading_fm_rule(
        translated_path, translated_content
    )
    findings["repairs"].extend(rel_fm_rule_repairs)

    translated_content, raw_status_repairs = (
        repair_releases_bare_raw_data_status_endpoint(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(raw_status_repairs)

    translated_content, ja_rel_fm_repairs = repair_ja_releases_description_desu_masu(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ja_rel_fm_repairs)

    translated_content, rel_tab_list_repairs = (
        repair_releases_tab_indented_markdown_bullets(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(rel_tab_list_repairs)

    translated_content, gfl_repairs = repair_guide_featured_list_links(
        english_content, translated_content
    )
    findings["repairs"].extend(gfl_repairs)

    translated_content, pt_push_ch_repairs = repair_pt_br_push_channel_token(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(pt_push_ch_repairs)

    translated_content, es_oblig_repairs = repair_es_api_obligatorio_typo(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(es_oblig_repairs)

    translated_content, de_dash_cap_repairs = repair_de_dashboard_capture_english_bleed(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(de_dash_cap_repairs)

    translated_content, dup_anchor_repairs = (
        repair_duplicate_adjacent_explicit_heading_anchors(translated_content)
    )
    findings["repairs"].extend(dup_anchor_repairs)

    translated_content, fc_paren_repairs = (
        repair_frequency_capping_transactional_outer_paren(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(fc_paren_repairs)

    translated_content, eng_show_repairs = (
        repair_duplicate_engagement_show_data_sections(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(eng_show_repairs)

    translated_content, unused_tr_id_repairs = (
        repair_unreferenced_explicit_heading_ids_when_english_has_none(
            english_content, translated_content
        )
    )
    findings["repairs"].extend(unused_tr_id_repairs)

    translated_content, anchor_id_repairs = repair_same_page_anchor_ids(
        english_content, translated_content
    )
    findings["repairs"].extend(anchor_id_repairs)

    translated_content, pilot_dl_anchor_repairs = (
        repair_braze_pilot_deep_links_section_anchor_ids(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(pilot_dl_anchor_repairs)

    translated_content, es_pilot_general_repairs = (
        repair_es_braze_pilot_deep_links_general_heading(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(es_pilot_general_repairs)

    translated_content, es_pilot_app_settings_repairs = (
        repair_es_braze_pilot_getting_started_app_settings_bold(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(es_pilot_app_settings_repairs)

    translated_content, fr_pilot_campaign_repairs = (
        repair_fr_braze_pilot_getting_started_campaign_inline_french(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(fr_pilot_campaign_repairs)

    translated_content, ja_pilot_brand_repairs = (
        repair_ja_braze_pilot_deep_links_pilot_brand_casing(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(ja_pilot_brand_repairs)

    translated_content, img_alt_repairs = repair_img_alt_inner_german_low9_closing_quote(
        translated_path, translated_content
    )
    findings["repairs"].extend(img_alt_repairs)

    translated_content, de_dkim_repairs = (
        repair_de_email_setup_whitelabel_dkim_spf_phrasing(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(de_dkim_repairs)

    translated_content, image_buster_repairs = repair_liquid_image_buster_path_spacing(
        translated_content
    )
    findings["repairs"].extend(image_buster_repairs)

    translated_content, assign_nested_repairs = (
        repair_liquid_assign_nested_default_in_output(translated_content)
    )
    findings["repairs"].extend(assign_nested_repairs)

    translated_content, md_table_pipe_repairs = repair_markdown_table_double_leading_row_pipes(
        translated_content
    )
    findings["repairs"].extend(md_table_pipe_repairs)

    translated_content, gtt_html_repairs = repair_yaml_guide_top_text_unquoted_html(
        translated_content
    )
    findings["repairs"].extend(gtt_html_repairs)
    translated_content, ds_aud_gcs_repairs = repair_decisioning_audience_gcs_services_typo(
        translated_path, translated_content
    )
    findings["repairs"].extend(ds_aud_gcs_repairs)

    translated_content, ds_aud_tab_repairs = repair_decisioning_audience_other_platforms_tab(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ds_aud_tab_repairs)

    translated_content, de_user_mgmt_repairs = (
        repair_de_global_user_management_landing_titles(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(de_user_mgmt_repairs)

    translated_content, inline_esc_repairs = repair_inline_code_escaped_quotes(
        translated_content
    )
    findings["repairs"].extend(inline_esc_repairs)

    translated_content, curl_typo_repairs = repair_curl_typo_url_in_code_fence(
        translated_content
    )
    findings["repairs"].extend(curl_typo_repairs)

    translated_content, json_value_repairs = repair_unquoted_json_string_values(
        translated_content
    )
    findings["repairs"].extend(json_value_repairs)

    translated_content, agents_ui_repairs = repair_agents_catalog_en_ui(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(agents_ui_repairs)

    translated_content, de_banners_repairs = repair_de_channels_banners_landing(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(de_banners_repairs)

    translated_content, data_dist_repairs = (
        repair_user_guide_data_distribution_landing(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(data_dist_repairs)

    translated_content, ab_testing_repairs = repair_messaging_ab_testing_locale_drift(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ab_testing_repairs)

    translated_content, canvas_hub_repairs = (
        repair_messaging_canvas_hub_titles_from_engagement_tools(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(canvas_hub_repairs)

    translated_content, ff_hub_repairs = (
        repair_messaging_feature_flags_fm_from_engagement_tools(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(ff_hub_repairs)

    translated_content, api_nav_repairs = repair_braze_dashboard_api_keys_nav_collapse(
        english_content, translated_content, lang_key
    )
    findings["repairs"].extend(api_nav_repairs)

    translated_content, ds_insights_repairs = repair_decisioning_insights_table_labels(
        english_content, translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ds_insights_repairs)

    translated_content, fr_payload_repairs = repair_fr_payload_display_typography(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(fr_payload_repairs)

    translated_content, tool_sp_repairs = repair_yaml_tool_list_spacing(
        translated_content
    )
    findings["repairs"].extend(tool_sp_repairs)

    translated_content, pt_agents_ref_repairs = (
        repair_pt_br_agents_reference_confidence_alt(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(pt_agents_ref_repairs)

    translated_content, pt_co_repairs = (
        repair_pt_br_brazeai_content_optimizer_product_name(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(pt_co_repairs)

    translated_content, de_schritt_repairs = repair_de_brazeai_schritt_three_link_text(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(de_schritt_repairs)

    translated_content, es_agents_alt_repairs = repair_es_agents_reference_alt_sentence_case(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(es_agents_alt_repairs)

    translated_content, es_pilot_dl_repairs = (
        repair_es_braze_pilot_deep_links_splash_vs_welcome(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(es_pilot_dl_repairs)

    translated_content, pilot_gs_repairs = (
        repair_braze_pilot_getting_started_campaigns_in_link_anchor(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(pilot_gs_repairs)

    translated_content, de_pilot_quote_repairs = (
        repair_de_braze_pilot_low9_pair_ascii_close_quote(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(de_pilot_quote_repairs)

    translated_content, de_quote_repairs = repair_german_mismatched_quotes(
        translated_path, translated_content
    )
    findings["repairs"].extend(de_quote_repairs)

    translated_content, ko_query_repairs = repair_korean_query_hangul_typo(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ko_query_repairs)

    translated_content, ja_product_repairs = (
        repair_japanese_english_product_terms(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(ja_product_repairs)

    translated_content, ja_campaign_ui_repairs = repair_ja_campaign_composer_ui(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ja_campaign_ui_repairs)

    translated_content, ja_particle_repairs = (
        repair_japanese_latin_token_particle_spacing(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(ja_particle_repairs)

    translated_content, pt_low9_repairs = (
        repair_pt_br_german_low9_double_quote_in_body(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(pt_low9_repairs)

    translated_content, pt_analytics_menu_repairs = (
        repair_pt_br_analytics_product_menu_label(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(pt_analytics_menu_repairs)

    translated_content, pt_subscribed_label_repairs = (
        repair_pt_br_subscribed_default_subscription_group_label(
            translated_content, lang_key
        )
    )
    findings["repairs"].extend(pt_subscribed_label_repairs)

    translated_content, ja_mail_camp_repairs = repair_japanese_mixed_mail_campaign(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ja_mail_camp_repairs)

    translated_content, de_social_uc_repairs = (
        repair_de_email_use_cases_social_heading(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(de_social_uc_repairs)

    translated_content, gen_img_bold_repairs = (
        repair_generative_ai_images_english_flow_bold(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(gen_img_bold_repairs)

    translated_content, fr_img_tt_repairs = (
        repair_fr_generative_images_download_tooltip_article(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(fr_img_tt_repairs)

    translated_content, gen_img_title_repairs = (
        repair_generative_ai_images_add_to_media_library_title(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(gen_img_title_repairs)

    translated_content, fr_brand_nav_repairs = (
        repair_fr_generative_brand_guidelines_nav_directives(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(fr_brand_nav_repairs)

    translated_content, ja_brand_fm_repairs = (
        repair_ja_generative_brand_guidelines_fm_middot(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(ja_brand_fm_repairs)

    translated_content, yaml_repairs = repair_yaml_syntax(translated_content)
    findings["repairs"].extend(yaml_repairs)

    translated_content, cb_repairs = repair_code_blocks(
        english_content, translated_content
    )
    findings["repairs"].extend(cb_repairs)

    translated_content, url_repairs = repair_urls(
        english_content, translated_content
    )
    findings["repairs"].extend(url_repairs)

    translated_content, sb_url_paren_repairs = (
        repair_markdown_site_baseurl_link_paren_typos(translated_content)
    )
    findings["repairs"].extend(sb_url_paren_repairs)

    translated_content, css_nth_repairs = repair_css_nth_child_trailing_comma_in_style_blocks(
        translated_content
    )
    findings["repairs"].extend(css_nth_repairs)

    translated_content, aria_repairs = repair_documentation_english_aria_labels(
        translated_content, lang_key
    )
    findings["repairs"].extend(aria_repairs)

    translated_content, frag_repairs = repair_markdown_internal_link_fragments(
        translated_content
    )
    findings["repairs"].extend(frag_repairs)

    translated_content, sup_foot_repairs = repair_sup_addon_footnote_bold_typo(
        translated_content
    )
    findings["repairs"].extend(sup_foot_repairs)

    translated_content, ideas_slash_repairs = (
        repair_ideas_and_strategies_internal_link_trailing_slash(translated_content)
    )
    findings["repairs"].extend(ideas_slash_repairs)

    translated_content, link_slash_repairs = (
        repair_markdown_internal_link_trailing_slash(translated_content)
    )
    findings["repairs"].extend(link_slash_repairs)

    translated_content, href_liquid_repairs = (
        repair_html_href_space_before_liquid_open(translated_content)
    )
    findings["repairs"].extend(href_liquid_repairs)

    translated_content, redirect_quote_repairs = (
        repair_redirect_to_trailing_stray_quote_unquoted_url(
            str(translated_path), translated_content
        )
    )
    findings["repairs"].extend(redirect_quote_repairs)

    translated_content, redirect_fuse_repairs = (
        repair_redirect_front_matter_fused_close_delimiter(
            str(translated_path), translated_content
        )
    )
    findings["repairs"].extend(redirect_fuse_repairs)

    translated_content, dbl_pipe_repairs = (
        repair_markdown_double_leading_pipe_table_rows(translated_content)
    )
    findings["repairs"].extend(dbl_pipe_repairs)

    translated_content, table_col_repairs = repair_markdown_table_column_count(
        translated_content
    )
    findings["repairs"].extend(table_col_repairs)

    translated_content, tb_inline_repairs = repair_triple_backtick_inline_code(
        translated_content
    )
    findings["repairs"].extend(tb_inline_repairs)

    translated_content, wire_repairs = repair_markdown_wire_format_tables(
        translated_content
    )
    findings["repairs"].extend(wire_repairs)

    translated_content, anchor_space_repairs = (
        repair_missing_space_after_html_anchor_close(translated_content)
    )
    findings["repairs"].extend(anchor_space_repairs)

    translated_content, table_pipe_code_repairs = (
        repair_markdown_table_pipe_adjacent_to_underscored_code(translated_content)
    )
    findings["repairs"].extend(table_pipe_code_repairs)

    translated_content, wa_es_perm_repairs = (
        repair_es_whatsapp_template_prerequisites_permission_bullets(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(wa_es_perm_repairs)

    translated_content, dup_inc_repairs = (
        repair_duplicate_adjacent_target_audiences_include(translated_content)
    )
    findings["repairs"].extend(dup_inc_repairs)

    translated_content, pt_rep_repairs = repair_pt_br_banners_reporting_performance(
        translated_path, translated_content
    )
    findings["repairs"].extend(pt_rep_repairs)

    translated_content, hub_copy_repairs = repair_user_guide_messaging_data_hub_copy(
        translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(hub_copy_repairs)

    translated_content, pt_delay_repairs = (
        repair_pt_inapp_message_troubleshooting_loanword_delay(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(pt_delay_repairs)

    translated_content, banner_ui_repairs = repair_banners_create_a_banner_verbatim_ui(
        translated_path, translated_content
    )
    findings["repairs"].extend(banner_ui_repairs)

    translated_content, fr_js_bridge_repairs = (
        repair_fr_banners_custom_code_javascript_bridge_terms(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(fr_js_bridge_repairs)

    translated_content, de_banner_nutzer_repairs = (
        repair_de_banners_custom_code_inclusive_nutzer(
            translated_path, translated_content, lang_key
        )
    )
    findings["repairs"].extend(de_banner_nutzer_repairs)

    translated_content, brazeai_repairs = repair_brazeai_trademark(
        translated_content
    )
    findings["repairs"].extend(brazeai_repairs)

    translated_content, apitag_repairs = repair_apitags(
        english_content, translated_content
    )
    findings["repairs"].extend(apitag_repairs)

    translated_content, glossary_id_repairs = repair_glossary_identifiers(
        english_content, translated_content, lang_key
    )
    findings["repairs"].extend(glossary_id_repairs)

    translated_content, md_bold_repairs = repair_spurious_bold_link_wrappers(
        translated_content
    )
    findings["repairs"].extend(md_bold_repairs)

    translated_content, dup_ha_repairs = repair_duplicate_kramdown_heading_anchors(
        translated_content
    )
    findings["repairs"].extend(dup_ha_repairs)

    translated_content, art_nav_repairs = (
        repair_article_title_casefold_matches_nav_title(translated_content)
    )
    findings["repairs"].extend(art_nav_repairs)

    translated_content, tw_repairs = repair_trailing_whitespace(translated_content)
    findings["repairs"].extend(tw_repairs)

    if findings["repairs"]:
        Path(translated_path).write_text(translated_content)

    findings["warnings"].extend(
        check_liquid_tags(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_liquid_paired_block_tags(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_japanese_english_product_terms_in_prose(
            translated_path, translated_content, lang_key
        )
    )
    findings["warnings"].extend(
        check_glossary_compliance(english_content, translated_content, lang_key)
    )
    findings["warnings"].extend(
        check_completeness(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_image_buster_alt_identifier_style(
            str(translated_path), translated_content
        )
    )
    findings["warnings"].extend(
        check_untranslated(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_untranslated_headings(
            english_content, translated_content, lang_key, translated_path
        )
    )
    findings["warnings"].extend(
        check_code_fence_balanced_quotes(english_content, label="english source")
    )
    findings["warnings"].extend(
        check_code_fence_balanced_quotes(
            translated_content, label=f"{lang_key} translation"
        )
    )
    findings["warnings"].extend(
        check_triple_backtick_inline_code(english_content, label="english source")
    )
    findings["warnings"].extend(
        check_sibling_terminology_drift(translated_path, translated_content)
    )
    findings["warnings"].extend(
        check_guide_featured_list_duplicate_links(
            english_content,
            translated_content,
            english_path=english_path,
            translated_path=translated_path,
        )
    )

    return findings


def cmd_qc(_args):
    """Run deterministic quality checks on all translated files."""
    results = load_results()
    translated = results.get("translated", [])

    if not translated:
        print("No translations to QC.")
        return

    print(f"Running QC checks on {len(translated)} translated file(s)...\n")

    all_findings = []
    repair_count = 0
    warning_count = 0

    for entry in translated:
        source_path = REPO_ROOT / entry["source"]
        target_path = REPO_ROOT / entry["target"]

        if not source_path.exists() or not target_path.exists():
            print(f"  Skipping {entry['target']} — file not found")
            continue

        findings = qc_check_file(source_path, target_path, entry["lang"])

        n_repairs = len(findings["repairs"])
        n_warnings = len(findings["warnings"])
        repair_count += n_repairs
        warning_count += n_warnings

        if n_repairs or n_warnings:
            all_findings.append(findings)
            parts = []
            if n_repairs:
                parts.append(f"{n_repairs} repaired")
            if n_warnings:
                parts.append(f"{n_warnings} warnings")
            print(f"  {entry['target']} — {', '.join(parts)}")
        else:
            print(f"  {entry['target']} — passed")

    qc_data = {
        "total_files": len(translated),
        "files_with_issues": len(all_findings),
        "total_repairs": repair_count,
        "total_warnings": warning_count,
        "findings": all_findings,
    }
    QC_RESULTS_FILE.write_text(json.dumps(qc_data, indent=2))

    print(f"\nQC complete: {len(translated)} files checked, "
          f"{repair_count} auto-repairs, {warning_count} warnings")
    if warning_count:
        print("  (warnings are informational — see PR summary for details)")


# ---------------------------------------------------------------------------
# verify  (build + fix loop)
# ---------------------------------------------------------------------------

def jekyll_build(lang_config_key):
    """Run a Jekyll build for one language; return (success, output)."""
    config = f"./_config.yml,./_lang/_config_{lang_config_key}.yml"
    result = subprocess.run(
        ["bundle", "exec", "jekyll", "build", "--config", config],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    return result.returncode == 0, result.stderr + "\n" + result.stdout


VERIFY_BUILD_LOG_TAIL = 3000


def _jekyll_output_tail(output, max_chars=None):
    """Return the trailing slice of Jekyll stdout/stderr for logs and results."""
    if max_chars is None:
        max_chars = VERIFY_BUILD_LOG_TAIL
    if not output:
        return ""
    return output[-max_chars:]


def _print_build_failure_output(lang_name, output, attempt, max_attempts):
    """Emit Jekyll output to CI logs when a locale build fails."""
    tail = _jekyll_output_tail(output)
    print(f"  --- Jekyll build output ({lang_name}, attempt {attempt}/{max_attempts}) ---")
    if tail:
        print(tail)
    else:
        print("  (no build output captured)")
    print("  --- end Jekyll build output ---")


def extract_error_files(error_output, lang_dir):
    """Pull locale markdown paths from Jekyll error output."""
    paths = set()
    patterns = (
        rf"_lang/{re.escape(lang_dir)}/\S+\.md",
        rf"(?<![\w/]){re.escape(lang_dir)}/\S+\.md",
    )
    for pattern in patterns:
        for match in re.findall(pattern, error_output):
            if match.startswith("_lang/"):
                paths.add(match)
            else:
                paths.add(f"_lang/{match}")
    return list(paths)


def cmd_verify(args):
    """Build each translated language; auto-fix errors up to N times."""
    client = _get_anthropic_client()
    prompt = load_prompt()
    results = load_results()

    translated_langs = {t["lang"] for t in results.get("translated", [])}
    if not translated_langs:
        print("No translations to verify.")
        return

    build_results = {"passed": [], "fixed": [], "failed": []}

    for lang_key in sorted(translated_langs):
        lang_info = LANGUAGES[lang_key]

        for attempt in range(1, args.max_attempts + 1):
            print(f"\nBuilding {lang_info['name']} (attempt {attempt}/{args.max_attempts})...")
            ok, output = jekyll_build(lang_info["config"])

            if ok:
                bucket = "fixed" if attempt > 1 else "passed"
                build_results[bucket].append(lang_key)
                label = "fixed and passed" if attempt > 1 else "passed"
                print(f"  {lang_info['name']} build {label}")
                break

            print(f"  {lang_info['name']} build failed")
            _print_build_failure_output(
                lang_info["name"], output, attempt, args.max_attempts,
            )

            if attempt == args.max_attempts:
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": _jekyll_output_tail(output),
                })
                print(f"  {lang_info['name']} still failing after {args.max_attempts} attempts")
                break

            error_files = extract_error_files(output, lang_info["dir"])
            if not error_files:
                print("  Could not identify failing file(s) from build output")
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": _jekyll_output_tail(output),
                })
                break

            for efile in error_files:
                epath = REPO_ROOT / efile
                if not epath.exists():
                    continue
                print(f"  Fixing {efile}...")
                try:
                    content = epath.read_text()
                    fixed = fix_file(
                        client, prompt, content, _jekyll_output_tail(output),
                        lang_info["name"],
                    )
                    epath.write_text(fixed)
                except Exception as exc:
                    print(f"  Fix attempt failed: {exc}")

    results["build_results"] = build_results
    save_results(results)

    print(f"\nBuild verification complete:")
    print(f"  Passed:        {len(build_results['passed'])}")
    print(f"  Fixed & passed: {len(build_results['fixed'])}")
    print(f"  Failed:        {len(build_results['failed'])}")
    if build_results["failed"]:
        sys.exit(1)


# ---------------------------------------------------------------------------
# check-aliases  (duplicate alias guard)
# ---------------------------------------------------------------------------

def _normalize_alias_key(raw):
    """Normalize an alias value for duplicate comparison."""
    if raw is None:
        return None
    v = str(raw).strip().strip("\"'").strip()
    if not v:
        return None
    if not v.startswith("/"):
        v = "/" + v
    v = v.rstrip("/")
    return v or "/"


def _alias_key_from_front_matter(content):
    """Return normalized alias key, or None if the file has no alias."""
    fm, _ = _extract_front_matter(content)
    if not fm:
        return None
    for line in fm.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("alias:"):
            raw = stripped.split(":", 1)[1].strip()
            return _normalize_alias_key(raw)
    return None


def _collect_alias_duplicates(root, *, skip_includes):
    """Map normalized alias -> list of repo-relative posix paths under ``root``."""
    alias_map = {}
    if not root.exists():
        return alias_map
    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        key = _alias_key_from_front_matter(text)
        if not key:
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if skip_includes and "/_includes/" in rel:
            continue
        alias_map.setdefault(key, []).append(rel)
    return {k: v for k, v in alias_map.items() if len(v) > 1}


def cmd_align_heading_anchor_parity(args):
    """Merge-time: align explicit ``{#…}`` heading IDs across sibling locale files."""
    try:
        n, msgs = align_cross_locale_heading_anchors(
            REPO_ROOT, full_repo_scan=args.full_repo
        )
    except CrossLocaleHeadingAnchorConflict as err:
        print(str(err), file=sys.stderr)
        sys.exit(1)
    for line in msgs:
        print(line)
    print(f"align-heading-anchor-parity: {n} file(s) updated.")


def cmd_check_aliases(args):
    """Ensure no duplicate ``alias:`` values within each locale (and in English _docs)."""
    skip_includes = not args.include_lang_includes
    errors = []

    for alias_key, paths in sorted(
        _collect_alias_duplicates(REPO_ROOT / "_docs", skip_includes=False).items()
    ):
        errors.append(("English `_docs/`", alias_key, paths))

    for lang_key, info in LANGUAGES.items():
        root = REPO_ROOT / "_lang" / info["dir"]
        for alias_key, paths in sorted(
            _collect_alias_duplicates(root, skip_includes=skip_includes).items()
        ):
            errors.append((f"`_lang/{info['dir']}/`", alias_key, paths))

    if not errors:
        print("check-aliases: no duplicate alias values found "
              f"(per locale; _lang _includes/ {'scanned' if args.include_lang_includes else 'skipped'}).")
        return

    print("check-aliases: DUPLICATE ALIAS VALUES\n", file=sys.stderr)
    for label, alias_key, paths in errors:
        print(f"  {label}  alias {alias_key!r}:", file=sys.stderr)
        for p in paths:
            print(f"    - {p}", file=sys.stderr)
        print(file=sys.stderr)
    print(
        f"check-aliases failed: {len(errors)} duplicate alias group(s). "
        "Use layout: redirect without alias on superseded pages, or remove the "
        "extra alias. Re-run with --include-lang-includes to also scan _includes "
        "(stricter; may need cleanup before enabling in CI).",
        file=sys.stderr,
    )
    sys.exit(1)


def cmd_check_path_case_collisions(_args):
    """Fail if two tracked-on-disk paths differ only by letter case (macOS/Windows hazard)."""
    collisions = _collect_path_case_collisions(REPO_ROOT)
    if not collisions:
        print(
            "check-path-case-collisions: no case-only duplicate paths under "
            "`_docs/`, `_includes/`, or `_lang/<locale>/`."
        )
        return

    print(
        "check-path-case-collisions: DUPLICATE PATHS (case-insensitive FS "
        "would alias these files):\n",
        file=sys.stderr,
    )
    for group in sorted(collisions):
        print("  Group:", file=sys.stderr)
        for p in group:
            print(f"    - {p}", file=sys.stderr)
        print(file=sys.stderr)
    print(
        "Remove or rename one spelling in Git so only a single path remains "
        "(match English ``_docs/`` folder casing for partner trees; PR #13372).",
        file=sys.stderr,
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# summary  (generate PR body)
# ---------------------------------------------------------------------------

def cmd_summary(_args):
    """Write a markdown PR body from the translation results."""
    results = load_results()
    translated = results.get("translated", [])
    failed = results.get("failed", [])
    chunked_files = results.get("chunked", [])
    build = results.get("build_results", {})

    lines = ["## Auto-translation summary\n"]

    source_files = sorted(set(t["source"] for t in translated))
    lines.append(f"**Source files translated:** {len(source_files)}  ")
    lines.append(f"**Translation files created/updated:** {len(translated)}  ")
    if failed:
        lines.append(f"**Translation API failures:** {len(failed)}  ")
    if chunked_files:
        lines.append(f"**Large files (chunked translation):** {len(chunked_files)}  ")
    lines.append("")

    if chunked_files:
        lines.append("### Large files (chunked translation)\n")
        lines.append("These files exceeded the single-pass size limit and were "
                      "translated in chunks at H2 heading boundaries.\n")
        for item in sorted(chunked_files, key=lambda x: -x["size_kb"]):
            lines.append(f"- `{item['source']}` ({item['size_kb']} KB)")
        lines.append("")

    # Build verification table
    if build:
        lines.append("### Build verification\n")
        lines.append("| Language | Status |")
        lines.append("|----------|--------|")
        for lang in build.get("passed", []):
            lines.append(f"| {LANGUAGES[lang]['name']} | Passed |")
        for lang in build.get("fixed", []):
            lines.append(f"| {LANGUAGES[lang]['name']} | Fixed and passed |")
        for item in build.get("failed", []):
            lines.append(f"| {LANGUAGES[item['lang']]['name']} | Needs manual review |")
        lines.append("")

    # Failed builds — expandable details
    build_failures = build.get("failed", [])
    if build_failures:
        lines.append("### Build failures requiring review\n")
        for item in build_failures:
            name = LANGUAGES[item["lang"]]["name"]
            lines.append(f"<details><summary>{name}</summary>\n")
            lines.append(f"```\n{item.get('error', 'No error details available')}\n```\n")
            lines.append("</details>\n")

    # QC checks
    if QC_RESULTS_FILE.exists():
        qc = json.loads(QC_RESULTS_FILE.read_text())

        lines.append("### Quality checks\n")

        lang_stats = {}
        for f in qc.get("findings", []):
            lang = f["lang"]
            if lang not in lang_stats:
                lang_stats[lang] = {"repairs": 0, "warnings": 0, "details": []}
            lang_stats[lang]["repairs"] += len(f.get("repairs", []))
            lang_stats[lang]["warnings"] += len(f.get("warnings", []))
            for r in f.get("repairs", []):
                lang_stats[lang]["details"].append(f"[repaired] {r}")
            for w in f.get("warnings", []):
                lang_stats[lang]["details"].append(f"[warning] {w}")

        translated_langs = set(t["lang"] for t in translated)

        lines.append("| Language | Repairs | Warnings | Status |")
        lines.append("|----------|---------|----------|--------|")
        for lang_key in sorted(LANGUAGES):
            if lang_key not in lang_stats:
                if lang_key not in translated_langs:
                    lines.append(
                        f"| {LANGUAGES[lang_key]['name']} | — | — | No translations |"
                    )
                else:
                    lines.append(
                        f"| {LANGUAGES[lang_key]['name']} | 0 | 0 | Passed |"
                    )
                continue
            s = lang_stats[lang_key]
            if s["warnings"]:
                status = "Needs review"
            elif s["repairs"]:
                status = "Auto-repaired"
            else:
                status = "Passed"
            lines.append(
                f"| {LANGUAGES[lang_key]['name']} | {s['repairs']} | "
                f"{s['warnings']} | {status} |"
            )
        lines.append("")

        for lang_key in sorted(lang_stats):
            s = lang_stats[lang_key]
            if not s["details"]:
                continue
            name = LANGUAGES[lang_key]["name"]
            count = len(s["details"])
            lines.append(
                f"<details><summary>{name} — {count} finding(s)</summary>\n"
            )
            for d in s["details"]:
                lines.append(f"- {d}")
            lines.append("\n</details>\n")

    # Translated files grouped by source
    if translated:
        lines.append("### Files translated\n")
        by_source = {}
        for t in translated:
            by_source.setdefault(t["source"], []).append(t["lang"])
        for source in sorted(by_source):
            lang_names = ", ".join(
                LANGUAGES[l]["name"] for l in sorted(by_source[source])
            )
            lines.append(f"- `{source}` → {lang_names}")
        lines.append("")

    body = "\n".join(lines)
    (REPO_ROOT / "translation_pr_body.md").write_text(body)
    print(body)


def cmd_repair_ja_product_terms(args: argparse.Namespace) -> None:
    """Batch-apply ``repair_japanese_english_product_terms`` under ``_lang/ja/``."""
    ja_root = REPO_ROOT / "_lang" / "ja"
    if not ja_root.is_dir():
        print("No _lang/ja/ directory found.", file=sys.stderr)
        sys.exit(1)

    changed = 0
    for path in sorted(ja_root.rglob("*.md")):
        rel = path.relative_to(REPO_ROOT).as_posix()
        original = path.read_text()
        updated, repairs = repair_japanese_english_product_terms(
            rel, original, "ja"
        )
        if not repairs:
            continue
        changed += 1
        if args.dry_run:
            print(f"would repair: {rel}")
        else:
            path.write_text(updated)
            print(f"repaired: {rel}")

    label = "Would repair" if args.dry_run else "Repaired"
    print(f"{label} {changed} file(s) under _lang/ja/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Auto-translate Braze documentation")
    sub = parser.add_subparsers(dest="command", required=True)

    tp = sub.add_parser("translate", help="Translate changed English files")
    tp.add_argument(
        "--changed-files", default="changed_files.txt",
        help="Path to a newline-delimited list of changed English doc paths",
    )
    tp.add_argument(
        "--languages",
        default=None,
        metavar="KEYS",
        help=(
            "Comma-separated language keys to translate (subset of: fr, ja, ko, "
            "pt-br, es, de). Default: all. Used by CI matrix jobs (one key per job)."
        ),
    )
    tp.add_argument(
        "--english-base-ref",
        default=None,
        metavar="REF",
        help=(
            "Git ref for the previous English version of changed files. When set, "
            "only H2 sections whose English changed are re-translated; unchanged "
            "sections are reused from the existing locale file. Also read from "
            "TRANSLATION_ENGLISH_BASE_REF."
        ),
    )
    tp.set_defaults(func=cmd_translate)

    vp = sub.add_parser("verify", help="Build each language and auto-fix errors")
    vp.add_argument(
        "--max-attempts", type=int, default=3,
        help="Maximum fix-and-rebuild cycles per language (default: 3)",
    )
    vp.set_defaults(func=cmd_verify)

    qp = sub.add_parser("qc", help="Run deterministic quality checks on translations")
    qp.set_defaults(func=cmd_qc)

    ap = sub.add_parser(
        "check-aliases",
        help="Fail if duplicate alias: values exist within _docs or each _lang locale",
    )
    ap.add_argument(
        "--include-lang-includes",
        action="store_true",
        help="Also scan _lang/**/_includes/**/*.md (default: skip; often shares alias with a page)",
    )
    ap.set_defaults(func=cmd_check_aliases)

    cp = sub.add_parser(
        "check-path-case-collisions",
        help=(
            "Fail if two files under _docs, _includes, or _lang differ only by "
            "path letter case (prevents macOS git checkout noise)"
        ),
    )
    cp.set_defaults(func=cmd_check_path_case_collisions)

    apar = sub.add_parser(
        "align-heading-anchor-parity",
        help=(
            "After matrix merge: copy explicit Kramdown {#id} across locale mirrors "
            "when any sibling locale has one (PR #13394 class drift)"
        ),
    )
    apar.add_argument(
        "--full-repo",
        action="store_true",
        help=(
            "Scan all `_lang/` markdown under user/developer/contributing guides "
            "(default: only paths from translation_results.json)"
        ),
    )
    apar.set_defaults(func=cmd_align_heading_anchor_parity)

    sp = sub.add_parser("summary", help="Generate a PR body from translation results")
    sp.set_defaults(func=cmd_summary)

    st = sub.add_parser(
        "stale-english-sources",
        help=(
            "Print English doc paths that need translation (missing or older "
            "locale mirror vs English in git)"
        ),
    )
    st.add_argument(
        "--max-history-commits",
        type=int,
        default=12000,
        metavar="N",
        help=(
            "First-parent commits to scan for path→time map (default: 12000); "
            "paths not touched there use per-path git log"
        ),
    )
    st.set_defaults(func=cmd_stale_english_sources)

    rj = sub.add_parser(
        "repair-ja-product-terms",
        help=(
            "Replace English Campaign/Canvas/Segment tokens in _lang/ja/ "
            "with glossary Japanese forms (one-off corpus repair)"
        ),
    )
    rj.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would change without writing",
    )
    rj.set_defaults(func=cmd_repair_ja_product_terms)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
