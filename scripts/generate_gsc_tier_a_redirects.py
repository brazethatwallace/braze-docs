#!/usr/bin/env python3
"""
Generate Tier A redirect candidates from a GSC 404 export (Table.csv in zip).

Adds:
  1. Explicit /docs/{locale}/... redirects for GSC localized 404s when an English
     mapping already exists in broken_redirect_list.js.
  2. Missing English canonical redirects inferred from on-disk docs.

Localized runtime expansion in _layouts/broken_page.html remains; explicit locale
entries help crawlers and make coverage auditable.

Usage:
  python3 scripts/generate_gsc_tier_a_redirects.py \\
    --gsc-zip ~/Downloads/https___www.braze.com_docs_-Coverage-Drilldown-2026-07-01.zip \\
    --apply

  python3 scripts/generate_gsc_tier_a_redirects.py --gsc-zip ... --dry-run
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_FILE = REPO_ROOT / "assets/js/broken_redirect_list.js"
RX_VALIDURL = re.compile(r"""^validurls\['([^']+)'\]\s*=\s*'([^']*)'\s*;\s*$""")

LOCALE_RX = re.compile(r"^/docs/(ja|ko|es|fr|pt-br)/")
SUPPORTED_LOCALES = ("ja", "ko", "es", "fr", "pt-br")

GSC_PATH_FRAG_REMAPS: tuple[tuple[str, str], ...] = (
    ("_user_guide/engagement_tools/messaging_fundamentals/", "_user_guide/messaging/messaging_fundamentals/"),
    ("_user_guide/engagement_tools/testing/", "_user_guide/messaging/ab_testing/"),
    ("_user_guide/engagement_tools/locations_and_geofences/", "_user_guide/audience/locations_and_geofences/"),
    ("_user_guide/personalization_and_dynamic_content/connected_content/", "_user_guide/messaging/design_and_edit/personalize/connected_content/"),
    ("_user_guide/personalization_and_dynamic_content/key_value_pairs/", "_user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/"),
    ("_user_guide/personalization_and_dynamic_content/liquid/", "_user_guide/messaging/design_and_edit/personalize/liquid/"),
    ("_user_guide/personalization_and_dynamic_content/catalogs/", "_user_guide/data/activation/catalogs/"),
    ("_user_guide/personalization_and_dynamic_content/catalog/", "_user_guide/data/activation/catalogs/"),
    ("_user_guide/personalization_and_dynamic_content/content_blocks", "_user_guide/messaging/design_and_edit/content_blocks"),
    ("_user_guide/personalization_and_dynamic_content/", "_user_guide/messaging/design_and_edit/personalize/"),
    ("_developer_guide/platform_integration_guides/", "_developer_guide/platforms/legacy_sdks/"),
    ("_user_guide/analytics/reporting/", "_user_guide/analytics/reports/"),
)

SKIP_PATH_SUBSTRINGS = (
    "<em>",
    "%3Cem%3E",
    "javascript:",
    "{{site.baseurl}}",
    "/docs/user<em>",
    "/docs/developer_",
    "/docs/user/",
    "/docs/tour",
    "/docs/get_search",
)

# English-only gaps seen in GSC but not covered by IA prefix remaps alone.
MANUAL_ENGLISH: dict[str, str] = {
    "/docs/user_guide/analytics/reporting/reports_overview": "/docs/user_guide/analytics/reports",
    "/docs/user_guide/analytics/reporting/viewing_and_understanding_segment_data": "/docs/user_guide/audience/segments/segment_data",
    "/docs/user_guide/analytics/field_level_encryption": "/docs/user_guide/data/infrastructure/field_level_encryption",
    "/docs/user_guide/onboarding_faq": "/docs/user_guide/onboarding_faq",
    "/docs/integrations/api/basics": "/docs/api/basics",
    "/docs/sdk/flutter/overview": "/docs/developer_guide/sdk_integration?sdktab=flutter",
    "/docs/sdk/ios/overview": "/docs/developer_guide/sdk_integration?sdktab=swift",
    "/docs/sdk/react_native/overview": "/docs/developer_guide/sdk_integration?sdktab=react%20native",
    "/docs/sdk/web/overview": "/docs/developer_guide/sdk_integration?sdktab=web",
    "/docs/ai_item_recommendations": "/docs/user_guide/brazeai/item_recommendations",
}


def load_inference_module():
    path = REPO_ROOT / "scripts/salesforce-analyzer/generate_kb_phase1_outputs.py"
    mod_name = "generate_kb_phase1_outputs"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load inference module from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def norm_lhs(url: str) -> str:
    u = url.strip().rstrip("/").lower()
    if "?" in u:
        u = u.split("?", 1)[0].rstrip("/")
    return u


def parse_redirect_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("//"):
            continue
        m = RX_VALIDURL.match(line.strip())
        if not m:
            continue
        out[norm_lhs(m.group(1))] = m.group(2)
    return out


def strip_locale(path: str) -> tuple[str | None, str]:
    m = LOCALE_RX.match(path)
    if not m:
        return None, path
    return m.group(1), LOCALE_RX.sub("/docs/", path)


def localize_destination(dest: str, locale: str) -> str:
    if dest.startswith("http://") or dest.startswith("https://"):
        return dest
    if not dest.startswith("/docs/"):
        return dest
    if LOCALE_RX.match(dest):
        return dest
    return dest.replace("/docs/", f"/docs/{locale}/", 1)


def public_url_to_doc_path(url_path: str) -> str:
    p = url_path.strip()
    if not p.startswith("/docs/"):
        return ""
    _, p = strip_locale(p)
    rest = p[len("/docs/") :].rstrip("/")
    if not rest:
        return ""
    if rest.startswith("help/"):
        return f"_docs/_help/{rest[len('help/'):]}"
    return f"_docs/_{rest}"


def doc_path_to_public_url(doc_path: str, fragment: str | None = None) -> str:
    rel = doc_path
    if rel.startswith("_docs/_"):
        url = "/docs/" + rel[len("_docs/_") :]
    elif rel.startswith("_docs/"):
        url = "/docs/" + rel[len("_docs/") :]
    else:
        return ""
    if url.endswith(".md"):
        url = url[: -len(".md")]
    if fragment:
        url = f"{url}#{fragment}"
    return url


def apply_gsc_remaps(doc_path: str) -> str:
    out = doc_path.replace("\\", "/")
    for old, new in GSC_PATH_FRAG_REMAPS:
        out = out.replace(old, new)
    return out


def load_gsc_urls(zip_path: Path) -> list[str]:
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if n.endswith("Table.csv")]
        if not names:
            raise RuntimeError(f"No Table.csv in {zip_path}")
        with zf.open(names[0]) as f:
            text = f.read().decode("utf-8-sig")
    rows = csv.DictReader(text.splitlines())
    return [(row.get("URL") or row.get("url") or "").strip() for row in rows if (row.get("URL") or row.get("url"))]


def should_skip(path: str) -> bool:
    low = path.lower()
    return any(s in low for s in SKIP_PATH_SUBSTRINGS)


def lookup_english_dest(path: str, english_map: dict[str, str]) -> str | None:
    base = path.split("#", 1)[0]
    key = norm_lhs(base)
    if key in english_map:
        return english_map[key]
    if "#" in base:
        path_only = base.split("#", 1)[0]
        frag = base.split("#", 1)[1]
        pk = norm_lhs(path_only)
        if pk in english_map:
            d = english_map[pk]
            return f"{d}#{frag}" if frag else d
    return None


def infer_english_destination(
    source_path: str,
    inference_mod,
    basename_index: dict[str, str],
    english_map: dict[str, str],
) -> tuple[str | None, str]:
    dest = lookup_english_dest(source_path, english_map)
    if dest:
        return dest, "already_mapped"

    base = source_path.split("#", 1)[0]
    key = norm_lhs(base)
    if key in MANUAL_ENGLISH:
        return MANUAL_ENGLISH[key], "manual"

    doc_raw = public_url_to_doc_path(base)
    if not doc_raw:
        return None, "not_docs_path"

    doc_remapped = apply_gsc_remaps(inference_mod.apply_path_remaps(doc_raw))
    resolved, note = inference_mod.resolve_path_with_inference(
        doc_remapped, REPO_ROOT, basename_index
    )
    if resolved:
        rel = resolved.relative_to(REPO_ROOT).as_posix()
        frag = source_path.split("#", 1)[1] if "#" in source_path else None
        return doc_path_to_public_url(rel, frag), note or "inferred_disk"

    return None, "unresolved"


def find_insertion_point(lines: list[str], new_key: str) -> int:
    new_segments = new_key.rstrip("/").strip("/").split("/")
    best_match_len = 0
    last_best_idx = None
    placeholder_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "// validurls['OLD'] = 'NEW';":
            placeholder_idx = i
            continue
        m = RX_VALIDURL.match(line.strip())
        if not m:
            continue
        existing_segments = m.group(1).rstrip("/").strip("/").split("/")
        match_len = sum(1 for a, b in zip(new_segments, existing_segments) if a == b)
        if match_len > best_match_len:
            best_match_len = match_len
            last_best_idx = i
    if last_best_idx is not None and best_match_len > 0:
        return last_best_idx + 1
    if placeholder_idx is not None:
        return placeholder_idx
    return len(lines)


def build_candidates(
    gsc_urls: list[str],
    inference_mod,
    basename_index: dict[str, str],
    english_map: dict[str, str],
) -> tuple[dict[str, tuple[str, str]], dict[str, int]]:
    candidates: dict[str, tuple[str, str]] = {}
    hits: dict[str, int] = defaultdict(int)
    skipped: dict[str, int] = defaultdict(int)

    for full_url in gsc_urls:
        parsed = urlparse(full_url)
        path = parsed.path or ""
        if should_skip(path):
            skipped["malformed"] += 1
            continue
        if not path.startswith("/docs/"):
            skipped["non_docs"] += 1
            continue

        locale, en_path = strip_locale(path)
        path_no_query = path.split("?", 1)[0]
        if parsed.fragment and "#" not in path_no_query:
            path_no_query = f"{path_no_query}#{parsed.fragment}"

        hits[path_no_query] += 1

        # Localized explicit redirect when English mapping exists.
        if locale:
            dest_en = lookup_english_dest(en_path, english_map)
            if not dest_en:
                dest_en, _ = infer_english_destination(en_path, inference_mod, basename_index, english_map)
            if dest_en:
                src = path_no_query.rstrip("/") if not path_no_query.endswith("/") else path_no_query.rstrip("/")
                # Preserve fragment from en_path lookup
                dest = localize_destination(dest_en, locale)
                key = norm_lhs(src.split("#", 1)[0])
                if key not in english_map and key not in candidates:
                    candidates[src.rstrip("/") if "#" not in src else src.split("#", 1)[0].rstrip("/")] = (
                        dest,
                        "localized_from_english",
                    )
                continue
            skipped["unresolved_localized"] += 1
            continue

        # English path
        key = norm_lhs(path_no_query.split("#", 1)[0])
        if key in english_map:
            continue
        dest, reason = infer_english_destination(path_no_query, inference_mod, basename_index, english_map)
        if dest:
            src = path_no_query.split("#", 1)[0].rstrip("/")
            if "#" in path_no_query:
                src = path_no_query  # keep fragment in key for validurls
            candidates[src if "#" in path_no_query else src] = (dest, reason)
        else:
            skipped["unresolved_english"] += 1

    return candidates, dict(hits), dict(skipped)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gsc-zip", type=Path, required=True, help="GSC Coverage Drilldown zip")
    parser.add_argument("--apply", action="store_true", help="Append new redirects to broken_redirect_list.js")
    parser.add_argument("--dry-run", action="store_true", help="Report only (default unless --apply)")
    parser.add_argument("--report", type=Path, help="Write CSV report of candidates")
    args = parser.parse_args()

    inference_mod = load_inference_module()
    basename_index = inference_mod.get_unique_basename_index(REPO_ROOT)
    english_map = parse_redirect_file(REDIRECT_FILE)

    gsc_urls = load_gsc_urls(args.gsc_zip)
    candidates, hits, skipped = build_candidates(gsc_urls, inference_mod, basename_index, english_map)

    localized = sum(1 for _, (_, r) in candidates.items() if r == "localized_from_english")
    english_new = len(candidates) - localized

    print(f"GSC URLs: {len(gsc_urls)}")
    print(f"New redirect candidates: {len(candidates)} ({localized} localized, {english_new} English)")
    for reason, count in sorted(skipped.items(), key=lambda x: -x[1]):
        print(f"  skipped ({reason}): {count}")

    if args.report:
        with args.report.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["source", "destination", "reason", "gsc_hits"])
            for src in sorted(candidates, key=lambda s: -hits.get(s, 0)):
                dest, reason = candidates[src]
                w.writerow([src, dest, reason, hits.get(src, 0)])
        print(f"Wrote report: {args.report}")

    if not args.apply:
        for src in sorted(candidates, key=lambda s: -hits.get(s, 0))[:20]:
            dest, reason = candidates[src]
            print(f"  {src} -> {dest}  ({reason}, hits={hits.get(src, 0)})")
        if len(candidates) > 20:
            print(f"  ... and {len(candidates) - 20} more")
        print("Re-run with --apply to append redirects.")
        return 0

    if not candidates:
        print("Nothing to apply.")
        return 0

    lines = REDIRECT_FILE.read_text(encoding="utf-8").splitlines(keepends=True)
    lines = [l for l in lines if l.strip() != "// validurls['OLD'] = 'NEW';"]
    existing_norm = {norm_lhs(m.group(1)) for l in lines if (m := RX_VALIDURL.match(l.strip()))}

    added = 0
    for src, (dest, _reason) in sorted(candidates.items(), key=lambda kv: kv[0]):
        lhs_key = norm_lhs(src.split("#", 1)[0])
        if lhs_key in existing_norm:
            continue
        lhs = src.split("#", 1)[0] if "#" not in src else src
        if "#" not in src:
            lhs = src
        line = f"validurls['{lhs}'] = '{dest}';\n"
        idx = find_insertion_point(lines, lhs)
        lines.insert(idx, line)
        existing_norm.add(lhs_key)
        added += 1

    REDIRECT_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"Appended {added} redirects to {REDIRECT_FILE}")
    print("Run: bundle exec ruby scripts/normalize_broken_redirect_list.rb --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
