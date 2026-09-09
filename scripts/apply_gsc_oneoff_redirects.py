#!/usr/bin/env python3
"""Apply manual GSC one-off redirects not covered by generate_gsc_redirect_batch.py."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from generate_gsc_redirect_batch import apply_entries
from locale_redirect_utils import (
    is_en_bulk_source,
    mirror_en_redirect_to_locales,
    parse_validurls,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"

MARKER = "// GSC 2026-09-09: translation gaps, malformed URLs, and locale stragglers"

# EN bulk-eligible sources in broken_redirect_list.js to locale-mirror for locale-only 404s.
EN_MIRROR_SOURCES = (
    "/docs/partners/additional_channels/support/pypestream",
    "/docs/partners/data_and_infrastructure_agility/analytics/amplitude",
    "/docs/partners/data_and_infrastructure_agility/analytics/contentsquare",
    "/docs/partners/data_and_infrastructure_agility/analytics/looker",
    "/docs/partners/data_augmentation/recommendation/amazon_personalize",
    "/docs/partners/message_orchestration/channel_extensions/loyalty/viralsweep",
    "/docs/api/endpoints/custom_objects/objects/put_replace_custom_object",
)

ONEOFF_ENTRIES: dict[str, str] = {
    "/docs/de/user_guide/data/unification/cloud_ingestion/sync_accounts_data": "/docs/de/user_guide/data/unification/cloud_ingestion",
    "/docs/ja/user_guide/data/unification/cloud_ingestion/sync_accounts_data": "/docs/ja/user_guide/data/unification/cloud_ingestion",
    "/docs/es/compliance_documentation/index.md": "/docs/compliance_documentation",
    "/docs/es/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify": "/docs/es/partners/ecommerce/shopify/shopify_overview",
    "/docs/fr/developer_guide/push_notifications/live_notifications?sdktab=swift": "/docs/fr/developer_guide/live_notifications?sdktab=swift",
    "/docs/fr/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/index.md": "/docs/fr/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup",
    "/docs/ko/developer_guide/sdk_integration/initialization/?sdktab=web": "/docs/ko/developer_guide/sdk_integration/initialization?sdktab=web",
    "/docs/ko/releases/sdk_changelogs": "/docs/ko/developer_guide/changelogs",
    "/docs/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents": "/docs/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents",
    "/docs/partners/message_orchestration/ab_testing/offerfit": "/docs/partners/message_personalization/dynamic_content/content_optimization_testing",
    "/docs/pt-br/developer_guide/analytics/sdk-tracking.iad-01.braze.com": "/docs/pt-br/developer_guide/analytics",
    "/docs/pt-br/partners/data_and_analytics/analytics/amplitude": "/docs/pt-br/partners/data_and_analytics/customer_data_platform/amplitude",
    "/docs/pt-br/partners/ecommerce/product_search_recommendations/stylitics": "/docs/pt-br/partners/message_personalization/dynamic_content/visual_and_interactive_content/stylitics",
}


def add_entry(
    entries: dict[str, str],
    source: str,
    dest: str,
    existing: dict[str, str],
) -> None:
    if source == dest or source in existing or source in entries:
        return
    entries[source] = dest


def build_entries(
    validurls: dict[str, str],
) -> tuple[dict[str, str], list[str]]:
    entries: dict[str, str] = {}
    warnings: list[str] = []
    existing = dict(validurls)

    for source, dest in ONEOFF_ENTRIES.items():
        if is_en_bulk_source(source):
            add_entry(entries, source, dest, existing)
            merged = {**existing, **entries}
            for locale_source, locale_dest in mirror_en_redirect_to_locales(
                source, dest, merged
            ):
                add_entry(entries, locale_source, locale_dest, existing)
        else:
            add_entry(entries, source, dest, existing)

    for en_source in EN_MIRROR_SOURCES:
        en_dest = validurls.get(en_source)
        if not en_dest:
            warnings.append(f"No EN redirect found for mirror source: {en_source}")
            continue
        merged = {**existing, **entries}
        for locale_source, locale_dest in mirror_en_redirect_to_locales(
            en_source, en_dest, merged
        ):
            add_entry(entries, locale_source, locale_dest, existing)

    return entries, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    from locale_redirect_utils import parse_validurls

    validurls = parse_validurls(REDIRECT_JS.read_text(encoding="utf-8"))
    entries, warnings = build_entries(validurls)
    print(f"One-off entries: {len(entries)}")
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for source in sorted(entries):
        print(f"  {source}")

    if not args.apply:
        print("\nDry run. Re-run with --apply to write broken_redirect_list.js")
        return 0

    apply_entries(REDIRECT_JS, entries, MARKER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
