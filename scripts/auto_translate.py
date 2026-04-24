#!/usr/bin/env python3
"""
Auto-translate English Braze docs into all supported languages using Claude.

Usage:
    python auto_translate.py translate --changed-files changed_files.txt
    python auto_translate.py qc
    python auto_translate.py check-aliases
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
from typing import Optional

def _get_anthropic_client():
    """Lazy-import Anthropic so commands like qc/summary work without the SDK."""
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: Install the Anthropic SDK: pip install anthropic")
        sys.exit(1)
    return Anthropic()


LANGUAGES = {
    "fr":    {"config": "fr",    "dir": "fr_fr", "name": "French"},
    "ja":    {"config": "ja",    "dir": "ja",    "name": "Japanese"},
    "ko":    {"config": "ko",    "dir": "ko",    "name": "Korean"},
    "pt-br": {"config": "pt-br", "dir": "pt_br", "name": "Portuguese (Brazil)"},
    "es":    {"config": "es",    "dir": "es",    "name": "Spanish"},
    "de":    {"config": "de",    "dir": "de",    "name": "German"},
}

MODEL = os.environ.get("TRANSLATION_MODEL", "claude-opus-4-6")
MAX_TOKENS = int(os.environ.get("TRANSLATION_MAX_TOKENS", "128000"))
MAX_FILE_KB = int(os.environ.get("TRANSLATION_MAX_FILE_KB", "130"))
CHUNK_TARGET_KB = int(os.environ.get("TRANSLATION_CHUNK_KB", "50"))
MAX_WORKERS = int(os.environ.get("TRANSLATION_WORKERS", "12"))
REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
RESULTS_FILE = REPO_ROOT / "translation_results.json"
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"
STYLEGUIDE_DIR = REPO_ROOT / "scripts" / "styleguides"
QC_RESULTS_FILE = REPO_ROOT / "qc_results.json"

NON_TRANSLATABLE_FM_KEYS = frozenset({
    "page_order", "layout", "page_type", "channel", "platform", "tool",
    "link", "image", "permalink", "hidden", "noindex", "config_only",
    "search_rank", "page_layout",
})

BRAZE_PRODUCT_NAMES = [
    "Content Cards", "Content Blocks", "Push Stories", "In-App Messages",
    "REST API", "News Feed", "Canvases", "Canvas", "Currents", "Campaigns",
    "Campaign", "Segments", "Segment", "Braze", "Liquid", "SDK", "API",
]

NON_LATIN_LANGUAGES = frozenset({"ja", "ko"})

COMPLETENESS_MIN_RATIO = float(os.environ.get("QC_MIN_RATIO", "0.6"))
COMPLETENESS_MAX_RATIO = float(os.environ.get("QC_MAX_RATIO", "1.6"))
UNTRANSLATED_BLOCK_THRESHOLD = 200


def load_prompt():
    """Load the translation system prompt from scripts/translation_prompt.md."""
    return (REPO_ROOT / "scripts" / "translation_prompt.md").read_text()


def load_styleguide(lang_key):
    """Load the style guide for a language. Returns '' if not found."""
    sg_path = STYLEGUIDE_DIR / f"{lang_key}.md"
    if sg_path.exists():
        content = sg_path.read_text().strip()
        if content:
            return f"\n\n## Style guide for this language\n\n{content}"
    return ""


def load_glossary(lang_key):
    """Load the terminology glossary for a language. Returns {} if not found."""
    glossary_path = GLOSSARY_DIR / f"{lang_key}.json"
    if glossary_path.exists():
        return json.loads(glossary_path.read_text())
    return {}


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


def split_into_chunks(content, max_chunk_kb=None):
    """Split a large Markdown file into translatable chunks at H2 boundaries.

    Returns a list of strings.  The first element is everything before the
    first ``## `` heading (front matter + intro).  Subsequent elements group
    consecutive H2 sections so that each chunk stays under *max_chunk_kb*.
    If the file has no H2 headings, falls back to a line-count split.
    """
    if max_chunk_kb is None:
        max_chunk_kb = CHUNK_TARGET_KB
    max_bytes = max_chunk_kb * 1024

    parts = re.split(r'(?=\n## )', content)

    if len(parts) <= 1:
        lines = content.split('\n')
        target_lines = max(200, len(lines) // ((len(content) // max_bytes) + 1))
        chunks = []
        for i in range(0, len(lines), target_lines):
            chunks.append('\n'.join(lines[i:i + target_lines]))
        return chunks

    preamble = parts[0]
    sections = parts[1:]

    chunks = [preamble]
    current_chunk = ""

    for section in sections:
        if current_chunk and len((current_chunk + section).encode()) > max_bytes:
            chunks.append(current_chunk)
            current_chunk = section
        else:
            current_chunk += section

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
        m = re.match(r'\n## (.+)', part)
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


def call_claude(client, system_prompt, user_message, retries=3):
    """Call the Claude API via streaming with exponential-backoff retry."""
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
            if attempt < retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"    API error: {exc} — retrying in {wait}s...")
                time.sleep(wait)
                continue
            raise

        if stop_reason == "max_tokens":
            raise RuntimeError(
                f"Output truncated (hit {MAX_TOKENS} token limit). "
                "Increase TRANSLATION_MAX_TOKENS or use chunked translation."
            )
        return strip_code_fences(full_text)


def translate_file(client, prompt, english_content, existing_translation, language_name, extra_context=""):
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

    return call_claude(client, system, user_msg)


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

Return ONLY the improved translated file — no explanations, no code fences, \
no commentary. If the translation is already high quality, return it unchanged.\
"""


def review_file(client, english_content, translated_content, language_name, extra_context=""):
    """Second-pass review of a translation for quality improvement."""
    system = [(REVIEW_PROMPT, True)]
    if extra_context:
        system.append((extra_context, False))

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## English source\n\n{english_content}\n\n"
    user_msg += f"## Translation to review and improve\n\n{translated_content}\n"

    return call_claude(client, system, user_msg)



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


# Keys whose values carry cross-section terminology (nav labels, page title,
# meta description) — the strings a reader sees in navigation and search.
_SIBLING_CONTEXT_FM_KEYS = ("nav_title", "article_title", "title", "description")

# Cap how many related pages we expose to the LLM per translation to keep
# prompt size predictable. In practice an IA move produces 1 sibling and a
# product-area tree adds 2–4 deeper guides. Cap at 5 for safety.
_SIBLING_CONTEXT_MAX = 5

# Max characters of body excerpt to include per related page. Front matter
# alone catches IA-move drift (see PR #13297 / feature_flags.md), but
# product-area drift (PR #13298 / email.md — "Standard" tier labels, bullet
# phrasing) lives in body prose, so we include a short body excerpt too.
_SIBLING_CONTEXT_BODY_CHARS = 1400


def _find_sibling_translations(basename, lang_dir, exclude_target):
    """Return already-translated files in the locale with the same basename.

    Used by the QC drift check (which only compares same-concept pages).
    See ``_find_related_locale_pages`` for the broader prompt-context lookup.
    """
    lang_root = REPO_ROOT / "_lang" / lang_dir
    if not lang_root.exists():
        return []
    exclude_resolved = exclude_target.resolve() if exclude_target else None
    hits = []
    for path in sorted(lang_root.rglob(basename)):
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
    lang_root = REPO_ROOT / "_lang" / lang_dir
    if not lang_root.exists():
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

    for path in lang_root.rglob(basename):
        _consider(path, _CAT_SAME_BASENAME)

    # Limit the stem-based searches to pages that actually live inside a
    # directory named for the stem (e.g. `.../email/**`). A global
    # ``email_*`` glob would otherwise drag in weakly-related files like
    # ``analytics/tracking/email_tracking.md`` that don't share the same
    # product-area glossary.
    if len(stem) >= 4:
        stem_prefix = f"{stem}_"
        stem_suffix = f"_{stem}.md"
        for path in lang_root.rglob("*.md"):
            if stem not in path.parts:
                continue
            if path.name == basename:
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
        "- Reuse **`nav_title`**, **`article_title`**, and **`description`** "
        "wording verbatim when the page covers the same concept.\n"
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

def translate_one(client, prompt, fpath, relative, english_content,
                  lang_key, lang_info, glossary, styleguide):
    """Translate + review a single file into one language. Returns a result dict."""
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
            lang_info["name"], extra_context,
        )
        translated = review_file(
            client, english_content, translated,
            lang_info["name"], extra_context,
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
        return {
            "ok": False,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "error": str(exc),
        }


def translate_one_chunked(client, prompt, fpath, relative, english_content,
                          lang_key, lang_info, glossary, styleguide):
    """Translate a large file by splitting into chunks, translating each, and
    reassembling.  Skips the second-pass review (chunks are self-contained and
    the review would require the full file which exceeds context limits)."""
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

    translated_chunks = []
    try:
        for i, (en_chunk, tr_chunk) in enumerate(zip(en_chunks, tr_chunks)):
            print(f"    [{lang_key}] translating chunk {i + 1}/{len(en_chunks)} "
                  f"({len(en_chunk) // 1024}KB)...")
            translated = translate_file(
                client, prompt, en_chunk, tr_chunk or None,
                lang_info["name"], extra_context,
            )
            translated_chunks.append(translated)

        full_translation = "\n\n".join(c.strip() for c in translated_chunks)
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
    """Translate changed English docs into every supported language."""
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
        if size_kb > MAX_FILE_KB:
            chunked.append(fpath)
            print(f"  CHUNKED: {fpath} ({round(size_kb)} KB — will use chunked translation)")
        else:
            translatable.append(fpath)

    if not translatable and not chunked:
        print("No translatable files found.")
        return

    total_tasks = len(translatable) * len(LANGUAGES)
    chunked_tasks = len(chunked) * len(LANGUAGES)
    print(f"Translating {len(translatable)} file(s) into {len(LANGUAGES)} language(s) "
          f"({total_tasks} tasks, {MAX_WORKERS} workers)")
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
    glossaries = {lang: load_glossary(lang) for lang in LANGUAGES}
    styleguides = {lang: load_styleguide(lang) for lang in LANGUAGES}

    # --- Normal parallel translation for files under the size limit ---
    if translatable:
        futures = {}
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            for fpath in translatable:
                relative = _relative_for_translation(fpath)
                english_content = (REPO_ROOT / fpath).read_text()

                for lang_key, lang_info in LANGUAGES.items():
                    future = pool.submit(
                        translate_one, client, prompt, fpath, relative,
                        english_content, lang_key, lang_info,
                        glossaries[lang_key], styleguides[lang_key],
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

            for lang_key, lang_info in LANGUAGES.items():
                result = translate_one_chunked(
                    client, prompt, fpath, relative, english_content,
                    lang_key, lang_info,
                    glossaries[lang_key], styleguides[lang_key],
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
                        "source": result["source"],
                        "target": result["target"],
                        "lang": result["lang"],
                        "error": result["error"],
                    })
                    print(f"    {lang_info['name']} FAILED ({result['error']})")

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
    """Extract YAML front matter and body from a markdown file."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
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
    """If ``url`` is a ``{{site.baseurl}}`` doc link whose path omits ``/``
    before ``#anchor``, insert the slash. Returns ``(new_url, changed)``.
    """
    if "{{site.baseurl}}" not in url:
        return url, False
    if "?" in url:
        return url, False
    hashidx = url.find("#")
    if hashidx <= 0:
        return url, False
    before, frag = url[:hashidx], url[hashidx + 1 :]
    if not frag or before.endswith("/"):
        return url, False
    bl = before.lower()
    if bl.endswith((".md", ".html", ".htm", ".json", ".xml")):
        return url, False
    last_seg = before.rsplit("/", 1)[-1]
    if "." in last_seg:
        return url, False
    if not _MD_LINK_FRAGMENT_ANCHOR_RE.match(frag):
        return url, False
    return f"{before}/#{frag}", True


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
    """Ensure ``ideas_and_strategies`` doc links use a trailing ``/`` before ``)``."""
    repairs = []
    new = translated_content
    for wrong, right in (
        (
            "]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)",
            "]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)",
        ),
        (
            "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)",
            "]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/)",
        ),
    ):
        if wrong in new:
            new = new.replace(wrong, right)
            repairs.append("md-link — ideas_and_strategies trailing /")
    if repairs:
        return new, repairs
    return translated_content, []


def repair_markdown_internal_link_fragments(content):
    """Normalize ``]({{site.baseurl}}/...slug#anchor)`` → ``.../slug/#anchor``."""
    repairs = []

    def repl(match):
        url = match.group(1)
        new_url, changed = _normalize_single_internal_link_url(url)
        if changed:
            preview = url if len(url) <= 100 else url[:97] + "..."
            repairs.append(
                f"md-fragment — inserted '/' before # in internal link ({preview})"
            )
        return f"]({new_url})"

    new_content = re.sub(r"\]\(([^)]+)\)", repl, content)
    return new_content, repairs


# Missing `.` before second class breaks Kramdown table styling.
_RESET_TD_BR_IAL_MISSING_DOT = re.compile(
    r"\{\:\s*\.reset-td-br-1\s+reset-td-br-2\b"
)


def repair_markdown_wire_format_tables(content):
    """Auto-fix markdown table / IAL issues from translation or English typos.

    - ``Content_Type`` → ``Content-Type`` (HTTP header spelling)
    - ``{: .reset-td-br-1 reset-td-br-2`` → ``{: .reset-td-br-1 .reset-td-br-2``
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


def repair_fr_payload_display_typography(translated_content, lang_key):
    """Normalize French ``PAYLOAD`` (English all-caps) to readable *payload* wording.

    All-caps *PAYLOAD* in prose reads like shouting; technical French often uses
    lowercase *payload* / plural *payloads* (see Copilot review on campaigns /
    Decisioning docs).
    """
    if lang_key != "fr":
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
    for rel, sibling_content in siblings:
        sib_fm, _ = _extract_front_matter(sibling_content)
        if not sib_fm:
            continue
        for key in ("nav_title", "article_title", "description"):
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
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
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


def repair_same_page_anchor_ids(english_content, translated_content):
    """Preserve English same-page anchor slugs on localized headings.

    When an English doc contains ``](#slug)`` references whose slug matches
    the auto-slug of one of its own headings, the translated doc loses those
    anchors because the localized heading auto-slugs to a different value.
    We add an explicit ``{#slug}`` to the corresponding translated heading
    (matched by positional index) so the existing link targets keep working.

    Conservative by design:
      * Only adds IDs for slugs that are (a) referenced in this file and
        (b) map 1:1 to an English heading via auto-slug.
      * Never overwrites an existing ``{#id}`` on the translated heading.
      * Skips the file if the English and translated heading counts differ
        (structure mismatch → too risky to auto-align).
    """
    # Only operate on files that actually use same-page anchors.
    referenced = set(_ANCHOR_REF_RE.findall(english_content))
    referenced |= set(_ANCHOR_REF_RE.findall(translated_content))
    if not referenced:
        return translated_content, []

    en_headings = list(_iter_doc_headings(english_content))
    tr_headings = list(_iter_doc_headings(translated_content))
    if not en_headings or len(en_headings) != len(tr_headings):
        return translated_content, []

    lines = translated_content.split("\n")
    repairs = []
    for (_, _en_lvl, en_text, en_explicit), (tr_idx, _tr_lvl, _tr_text, tr_explicit) in zip(
        en_headings, tr_headings
    ):
        slug = en_explicit or _auto_slug(en_text)
        if not slug or slug not in referenced:
            continue
        if tr_explicit:
            continue
        existing = lines[tr_idx]
        if _EXPLICIT_ID_RE.search(existing):
            continue
        new_line = existing.rstrip() + f" {{#{slug}}}"
        if new_line != existing:
            lines[tr_idx] = new_line
            repairs.append(f"anchor_id — added {{#{slug}}} to translated heading")

    if not repairs:
        return translated_content, []
    new_content = "\n".join(lines)
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

    translated_content, fm_repairs = repair_front_matter(
        english_content, translated_content
    )
    findings["repairs"].extend(fm_repairs)

    translated_content, gfl_repairs = repair_guide_featured_list_links(
        english_content, translated_content
    )
    findings["repairs"].extend(gfl_repairs)

    translated_content, anchor_id_repairs = repair_same_page_anchor_ids(
        english_content, translated_content
    )
    findings["repairs"].extend(anchor_id_repairs)

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

    translated_content, canvas_hub_repairs = (
        repair_messaging_canvas_hub_titles_from_engagement_tools(
            translated_path, translated_content
        )
    )
    findings["repairs"].extend(canvas_hub_repairs)

    translated_content, api_nav_repairs = repair_braze_dashboard_api_keys_nav_collapse(
        english_content, translated_content, lang_key
    )
    findings["repairs"].extend(api_nav_repairs)

    translated_content, ds_insights_repairs = repair_decisioning_insights_table_labels(
        english_content, translated_path, translated_content, lang_key
    )
    findings["repairs"].extend(ds_insights_repairs)

    translated_content, fr_payload_repairs = repair_fr_payload_display_typography(
        translated_content, lang_key
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

    translated_content, wire_repairs = repair_markdown_wire_format_tables(
        translated_content
    )
    findings["repairs"].extend(wire_repairs)

    translated_content, dup_inc_repairs = (
        repair_duplicate_adjacent_target_audiences_include(translated_content)
    )
    findings["repairs"].extend(dup_inc_repairs)

    translated_content, pt_rep_repairs = repair_pt_br_banners_reporting_performance(
        translated_path, translated_content
    )
    findings["repairs"].extend(pt_rep_repairs)

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

    translated_content, tw_repairs = repair_trailing_whitespace(translated_content)
    findings["repairs"].extend(tw_repairs)

    if findings["repairs"]:
        Path(translated_path).write_text(translated_content)

    findings["warnings"].extend(
        check_liquid_tags(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_glossary_compliance(english_content, translated_content, lang_key)
    )
    findings["warnings"].extend(
        check_completeness(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_untranslated(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_sibling_terminology_drift(translated_path, translated_content)
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


def extract_error_files(error_output, lang_dir):
    """Pull file paths from Jekyll error output that belong to a language dir."""
    pattern = rf"_lang/{re.escape(lang_dir)}/\S+\.md"
    return list(set(re.findall(pattern, error_output)))


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

            if attempt == args.max_attempts:
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": output[-3000:],
                })
                print(f"  {lang_info['name']} still failing after {args.max_attempts} attempts")
                break

            error_files = extract_error_files(output, lang_info["dir"])
            if not error_files:
                print("  Could not identify failing file(s) from build output")
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": output[-3000:],
                })
                break

            for efile in error_files:
                epath = REPO_ROOT / efile
                if not epath.exists():
                    continue
                print(f"  Fixing {efile}...")
                try:
                    content = epath.read_text()
                    fixed = fix_file(client, prompt, content, output[-3000:], lang_info["name"])
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

    sp = sub.add_parser("summary", help="Generate a PR body from translation results")
    sp.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
