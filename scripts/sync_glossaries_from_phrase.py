#!/usr/bin/env python3
"""Sync ``scripts/glossaries/*.json`` from Phrase TMS term bases.

Phrase term bases are the source of truth for glossary entries. This script
downloads the configured Phrase term base (see ``phrase_term_bases.json``),
converts the Xlsx export into per-locale ``{english: translation}`` JSON files,
and writes ``scripts/glossaries/{locale}.json``.

Runtime translation still applies ``PROTECTED_PRODUCT_TERMS`` on top of the
synced files (see ``scripts/auto_translate.py``'s ``load_glossary``).

Usage:
    # Local (after copying .phrase-tms.env.example → .phrase-tms.env):
    python scripts/sync_glossaries_from_phrase.py

    python scripts/sync_glossaries_from_phrase.py --locale ja --dry-run
    python scripts/sync_glossaries_from_phrase.py --report phrase_sync_report.md

Environment:
    PHRASE_TMS_TOKEN          Phrase Platform API token (required)
    PHRASE_PLATFORM_BASE_URL  Default: https://eu.phrase.com
    PHRASE_TMS_BASE_URL       Default: https://cloud.memsource.com
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _glossary_locale_propagation import propagate_phrase_sync_to_locales  # noqa: E402
from phrase_tms_client import (  # noqa: E402
    TermBaseConfig,
    exchange_bearer_jwt,
    fetch_glossaries_for_locales,
    get_term_base,
    load_dotenv,
    load_term_base_config,
)


def _sorted_glossary(glossary: dict[str, str]) -> dict[str, str]:
    return {key: glossary[key] for key in sorted(glossary, key=str.casefold)}


def _write_glossary(path: Path, glossary: dict[str, str]) -> None:
    ordered = _sorted_glossary(glossary)
    path.write_text(
        json.dumps(ordered, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _diff_summary(
    old: dict[str, str],
    new: dict[str, str],
) -> dict[str, int | list[str]]:
    old_keys = set(old)
    new_keys = set(new)
    added = sorted(new_keys - old_keys, key=str.casefold)
    removed = sorted(old_keys - new_keys, key=str.casefold)
    changed = sorted(
        (key for key in old_keys & new_keys if old[key] != new[key]),
        key=str.casefold,
    )
    return {
        "added": len(added),
        "removed": len(removed),
        "changed": len(changed),
        "added_terms": added[:20],
        "removed_terms": removed[:20],
        "changed_terms": changed[:20],
    }


def generate_report(
    results: dict[str, dict],
    locale_results: dict | None = None,
    *,
    term_base_name: str,
    term_base_uid: str,
) -> str:
    lines = [
        "## Phrase glossary sync\n",
        "Synced `scripts/glossaries/*.json` from the Phrase TMS term base "
        f"**{term_base_name}** (`{term_base_uid}`). "
        "See `scripts/phrase_term_bases.json`.\n",
    ]
    total_added = total_removed = total_changed = 0
    for locale, row in sorted(results.items()):
        stats = row["diff"]
        total_added += stats["added"]
        total_removed += stats["removed"]
        total_changed += stats["changed"]
        lines.append(
            f"### {locale}\n"
            f"- **Target language column:** `{row['target_lang']}`\n"
            f"- **Entries:** {row['old_count']} → {row['new_count']}\n"
            f"- **Added:** {stats['added']} | **Removed:** {stats['removed']} | "
            f"**Changed:** {stats['changed']}\n"
        )
        if stats["added_terms"]:
            lines.append(
                "- Sample added: "
                + ", ".join(f"`{term}`" for term in stats["added_terms"])
                + "\n"
            )
        if stats["removed_terms"]:
            lines.append(
                "- Sample removed: "
                + ", ".join(f"`{term}`" for term in stats["removed_terms"])
                + "\n"
            )
        if stats["changed_terms"]:
            lines.append(
                "- Sample changed: "
                + ", ".join(f"`{term}`" for term in stats["changed_terms"])
                + "\n"
            )
    lines.append(
        f"\n**Totals:** {total_added} added, {total_removed} removed, "
        f"{total_changed} changed across {len(results)} locales.\n"
    )

    if locale_results:
        propagation = locale_results.get("propagation", {})
        ja_repairs = locale_results.get("ja_repairs", {})
        lines.append("\n### Locale propagation (`_lang/`)\n")
        lines.append(
            f"- **Glossary-driven replacements:** "
            f"{propagation.get('files_changed', 0)} files, "
            f"{propagation.get('replacements', 0)} replacements "
            f"({locale_results.get('changes_planned', 0)} planned change(s))\n"
        )
        if ja_repairs.get("files_changed"):
            lines.append(
                f"- **Japanese UI label repairs** (glossary removals): "
                f"{ja_repairs['files_changed']} files, "
                f"{ja_repairs['repairs']} repairs\n"
            )
        by_lang = propagation.get("by_lang") or {}
        if by_lang:
            lines.append(
                "- By locale: "
                + ", ".join(f"`{lang}` ({count})" for lang, count in sorted(by_lang.items()))
                + "\n"
            )
        sample_files = (propagation.get("details") or [])[:10]
        ja_sample = (ja_repairs.get("details") or [])[:5]
        if sample_files or ja_sample:
            lines.append("- Sample updated files:\n")
            for row in sample_files:
                lines.append(f"  - `{row['file']}` ({row['replacements']} replacements)\n")
            for row in ja_sample:
                lines.append(f"  - `{row['file']}` ({row['repairs']} JA UI repairs)\n")

    lines.append(
        "\n> **Note:** `scripts/_glossary_protected_terms.py` still overrides "
        "Braze product names at translation time (for example `Campaign` in "
        "Japanese). Update Phrase term bases when those should change in docs.\n"
    )
    return "\n".join(lines)


def sync_locales(
    locales: list[str],
    *,
    dry_run: bool = False,
) -> tuple[dict[str, dict], int, TermBaseConfig]:
    config = load_term_base_config()
    unknown = [locale for locale in locales if locale not in config.locales]
    if unknown:
        raise SystemExit(
            f"Unknown locale(s): {', '.join(unknown)}. "
            f"Expected: {', '.join(sorted(config.locales))}"
        )

    bearer = exchange_bearer_jwt()
    try:
        term_base_meta = get_term_base(bearer, config.term_base_uid)
        term_base_name = term_base_meta.get("name") or config.term_base_name
    except RuntimeError:
        term_base_name = config.term_base_name

    print(
        f"Fetching locales from Phrase term base {term_base_name} "
        f"({config.term_base_uid})..."
    )
    fetched = fetch_glossaries_for_locales(bearer, locales, config)

    results: dict[str, dict] = {}
    total_changes = 0

    for locale in locales:
        entry = config.locales[locale]
        glossary_path = GLOSSARY_DIR / f"{locale}.json"
        old = (
            json.loads(glossary_path.read_text(encoding="utf-8"))
            if glossary_path.exists()
            else {}
        )
        new = fetched[locale]
        diff = _diff_summary(old, new)
        changes = diff["added"] + diff["removed"] + diff["changed"]
        total_changes += changes
        results[locale] = {
            "uid": config.term_base_uid,
            "term_base_name": term_base_name,
            "target_lang": entry["target_lang"],
            "old_count": len(old),
            "new_count": len(new),
            "diff": diff,
            "old_glossary": old,
            "glossary": new,
        }
        print(
            f"  {locale}: {len(old)} → {len(new)} entries "
            f"(+{diff['added']} / -{diff['removed']} / ~{diff['changed']})"
        )
        if not dry_run and changes:
            _write_glossary(glossary_path, new)

    resolved_config = TermBaseConfig(
        term_base_uid=config.term_base_uid,
        term_base_name=term_base_name,
        source_lang=config.source_lang,
        locales=config.locales,
    )
    return results, total_changes, resolved_config


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync scripts/glossaries/*.json from Phrase TMS term bases."
    )
    parser.add_argument(
        "--locale",
        action="append",
        dest="locales",
        metavar="LANG",
        help="Sync only this locale (repeatable). Default: all configured locales.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and diff without writing glossary files.",
    )
    parser.add_argument(
        "--report",
        metavar="PATH",
        default="phrase_sync_report.md",
        help="Write a markdown summary for PR bodies (default: phrase_sync_report.md).",
    )
    parser.add_argument(
        "--skip-locale-propagation",
        action="store_true",
        help="Update glossaries only; do not propagate changes into _lang/.",
    )
    args = parser.parse_args()

    load_dotenv()
    config = load_term_base_config()
    locales = args.locales or sorted(config.locales)

    results, total_changes, resolved_config = sync_locales(locales, dry_run=args.dry_run)

    locale_results = None
    if (
        not args.dry_run
        and not args.skip_locale_propagation
        and total_changes > 0
    ):
        print("\nPropagating glossary changes to _lang/ docs...")
        locale_results = propagate_phrase_sync_to_locales(results)
        print(
            f"  Locale docs: {locale_results['locale_files_changed']} files, "
            f"{locale_results['locale_replacements']} replacements"
        )
        if locale_results["ja_repairs"]["files_changed"]:
            print(
                f"  JA UI repairs: {locale_results['ja_repairs']['files_changed']} files, "
                f"{locale_results['ja_repairs']['repairs']} repairs"
            )

    report = generate_report(
        results,
        locale_results,
        term_base_name=resolved_config.term_base_name,
        term_base_uid=resolved_config.term_base_uid,
    )
    report_path = Path(args.report)
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to {report_path}")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as handle:
            handle.write(f"total_changes={total_changes}\n")
            handle.write(f"locales_synced={len(results)}\n")
            if locale_results:
                handle.write(
                    f"locale_files_changed={locale_results['locale_files_changed']}\n"
                )
                handle.write(
                    f"locale_replacements={locale_results['locale_replacements']}\n"
                )

    if args.dry_run:
        print("Dry run — no glossary files written.")
    elif total_changes == 0:
        print("Glossaries already match Phrase.")
    else:
        print(f"Updated {total_changes} glossary row(s) across {len(results)} locale(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
