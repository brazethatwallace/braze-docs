#!/usr/bin/env python3
"""Sync ``scripts/glossaries/*.json`` from Phrase TMS term bases.

Phrase term bases are the source of truth for glossary entries. This script
downloads each configured locale's term base (see ``phrase_term_bases.json``),
converts the Xlsx export to ``{english: translation}`` JSON, and writes
``scripts/glossaries/{locale}.json``.

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
from phrase_tms_client import (  # noqa: E402
    exchange_bearer_jwt,
    fetch_glossary_for_locale,
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


def generate_report(results: dict[str, dict]) -> str:
    lines = [
        "## Phrase glossary sync\n",
        "Synced `scripts/glossaries/*.json` from Phrase TMS term bases "
        "(see `scripts/phrase_term_bases.json`).\n",
    ]
    total_added = total_removed = total_changed = 0
    for locale, row in sorted(results.items()):
        stats = row["diff"]
        total_added += stats["added"]
        total_removed += stats["removed"]
        total_changed += stats["changed"]
        lines.append(
            f"### {locale}\n"
            f"- **Phrase term base:** {row['term_base_name']} (`{row['uid']}`)\n"
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
) -> tuple[dict[str, dict], int]:
    config = load_term_base_config()
    unknown = [locale for locale in locales if locale not in config]
    if unknown:
        raise SystemExit(
            f"Unknown locale(s): {', '.join(unknown)}. "
            f"Expected: {', '.join(sorted(config))}"
        )

    bearer = exchange_bearer_jwt()
    results: dict[str, dict] = {}
    total_changes = 0

    for locale in locales:
        entry = config[locale]
        glossary_path = GLOSSARY_DIR / f"{locale}.json"
        old = (
            json.loads(glossary_path.read_text(encoding="utf-8"))
            if glossary_path.exists()
            else {}
        )
        print(f"Fetching {locale} from Phrase ({entry['name']})...")
        new = fetch_glossary_for_locale(bearer, locale, config)
        diff = _diff_summary(old, new)
        changes = diff["added"] + diff["removed"] + diff["changed"]
        total_changes += changes
        results[locale] = {
            "uid": entry["uid"],
            "term_base_name": entry["name"],
            "old_count": len(old),
            "new_count": len(new),
            "diff": diff,
            "glossary": new,
        }
        print(
            f"  {len(old)} → {len(new)} entries "
            f"(+{diff['added']} / -{diff['removed']} / ~{diff['changed']})"
        )
        if not dry_run and changes:
            _write_glossary(glossary_path, new)

    return results, total_changes


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
    args = parser.parse_args()

    load_dotenv()
    config = load_term_base_config()
    locales = args.locales or sorted(config)

    results, total_changes = sync_locales(locales, dry_run=args.dry_run)
    report = generate_report(results)
    report_path = Path(args.report)
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to {report_path}")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as handle:
            handle.write(f"total_changes={total_changes}\n")
            handle.write(f"locales_synced={len(results)}\n")

    if args.dry_run:
        print("Dry run — no glossary files written.")
    elif total_changes == 0:
        print("Glossaries already match Phrase.")
    else:
        print(f"Updated {total_changes} glossary row(s) across {len(results)} locale(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
