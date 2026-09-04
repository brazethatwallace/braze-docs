#!/usr/bin/env python3
"""
Generate Phase 1 markdown from `_data/kb_articles.csv` (skipped + actioned).

Gates: `.github/skills/salesforce-migration/SKILL.md` Phase 1 (automated). `inconclusive` + locatable
`_docs/` → not auto-skipped. Path inference: remaps, basename/fragment, topic routing — extend
`PATH_INFERENCE_EXACT`, `PATH_INFERENCE_PREFIXES`, `_CONTEXT_TOPIC_ROUTES` after confirmed mappings.

Default run **prunes** `archived` / `actioned` from the CSV; `--no-prune` only refreshes markdown;
`--infer-doc-paths` fills `doc_path`. No auto-skip for redundant-docs / workaround-only rows.
`suggested_change` should be strong draft prose (skill Phase 1).

Usage:
  python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
  python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sf_kb_article_ids import article_id_column, article_id_from_row  # noqa: E402
from sf_kb_suggested_change import is_vague_suggested_change  # noqa: E402
from sf_kb_assignees import product_vertical_for_doc_path  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "_data" / "kb_articles.csv"
SKIPPED_OUT = REPO_ROOT / "_data" / "kb_articles_skipped.md"
ACTIONED_OUT = REPO_ROOT / "_data" / "kb_articles_actioned.md"

_DOCS_PATH_RE = re.compile(
    r"(?:braze-docs/)?(_docs/[^\s\"'<>()]+)",
    re.IGNORECASE,
)

# Substrings in conflict_resolution that default to skip (see salesforce-migration skill).
CONFLICT_SKIP_SUBSTRINGS = (
    "human review",
    "no source",
    "codebase inconclusive",
    "inconclusive —",
)

# First-line implementation_status values that may proceed through Phase 1 (empty allowed).
PHASE1_ALLOWED_IMPL_STATUSES = frozenset(
    {
        "",
        "not started",
        "to be actioned",
        "delta ka",
    }
)

# Ordered path fragment remaps (CSV often uses retired IA paths).
# More specific prefixes must appear before broader `engagement_tools/` → `messaging/`.
PATH_FRAG_REMAPS: tuple[tuple[str, str], ...] = (
    ("_user_guide/engagement_tools/segments/", "_user_guide/audience/segments/"),
    ("_user_guide/engagement_tools/canvas/", "_user_guide/messaging/canvas/"),
    ("_user_guide/engagement_tools/campaigns/", "_user_guide/messaging/campaigns/"),
    ("_user_guide/engagement_tools/", "_user_guide/messaging/"),
    ("_user_guide/message_building_by_channel/", "_user_guide/channels/"),
    ("_user_guide/administrative/", "_user_guide/administer/"),
    ("_user_guide/access_braze/", "_user_guide/administer/personal/"),
    ("_user_guide/app_settings/", "_user_guide/administer/global/workspace_settings/"),
    ("_user_guide/data_and_analytics/", "_user_guide/data/"),
    ("_user_guide/channels/email/reporting_and_analytics/", "_user_guide/channels/email/reporting/"),
    ("_user_guide/data_and_analytics/", "_user_guide/data/"),
    ("_user_guide/documentation/", "_user_guide/analytics/"),
    ("_user_guide/docs_author_platform/", "_user_guide/messaging/"),
    ("/document/", "/sms_mms_and_rcs/"),
    ("reeligibility", "re_eligibility"),
    ("dataplatform", "data_platform"),
)

# --- Path inference (stale CSV `_docs/` → current on-disk targets) ---
# Keys are `normalize_remapped_doc_path(raw)` outputs (see below). Values are repo-relative `_docs/...` files.
PATH_INFERENCE_EXACT: dict[str, str] = {
    "_docs/_user_guide/messaging/campaigns/building_campaigns/rate-limiting.md": (
        "_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md"
    ),
    "_docs/_user_guide/channels/email/managing_user_subscriptions.md": (
        "_docs/_user_guide/channels/email/subscriptions.md"
    ),
    "_docs/_user_guide/data/activation/custom_data/custom_attributes.md": (
        "_docs/_user_guide/data/activation/attributes/custom_attributes.md"
    ),
    "_docs/_user_guide/data/activation/custom_data/custom_events.md": (
        "_docs/_user_guide/data/activation/events/custom_events.md"
    ),
    "_docs/_user_guide/personalization_and_dynamic_content/liquid/faq.md": (
        "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/faq.md"
    ),
    "_docs/_user_guide/administrative/app_settings/company_settings/automated_user_provisioning.md": (
        "_docs/_user_guide/administer/global/user_management/automated_user_provisioning.md"
    ),
    "_docs/_user_guide/administrative/access_braze/single_sign_on/set_up.md": (
        "_docs/_user_guide/administer/global/saml_single_sign_on/saml_sso_setup.md"
    ),
    "_docs/_user_guide/channels/sms_mms_rcs/sms/faqs.md": (
        "_docs/_user_guide/channels/sms_mms_and_rcs/faqs.md"
    ),
    "_docs/_user_guide/channels/sms_mms_rcs/link_shortening.md": (
        "_docs/_user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening.md"
    ),
    "_docs/_user_guide/channels/in_app_messages/traditional/customize/email_capture_form.md": (
        "_docs/_user_guide/channels/in_app_messages/message_types/email_capture_form.md"
    ),
    "_docs/_user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support": (
        "_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md"
    ),
    "_docs/_user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support.md": (
        "_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md"
    ),
    "_docs/_user_guide/data_and_analytics/user_data_collection/user_import/": (
        "_docs/_user_guide/audience/manage_audience/import_users/csv_import.md"
    ),
    "_docs/_user_guide/engagement_tools/segments/segmentation_filters.md": (
        "_docs/_user_guide/audience/segments/segmentation_filters.md"
    ),
    "_docs/_user_guide/engagement_tools/segments/user_profiles/duplicate_users.md": (
        "_docs/_user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior.md"
    ),
    "_docs/_user_guide/access_braze/troubleshooting.md": (
        "_docs/_user_guide/administer/personal/braze_support.md"
    ),
    "_docs/_user_guide/administrative/app_settings/email_settings.md": (
        "_docs/_user_guide/administer/global/workspace_settings/email_preferences.md"
    ),
    "_docs/_user_guide/administrative/app_settings/manage_app_group/email_settings/": (
        "_docs/_user_guide/administer/global/workspace_settings/email_preferences.md"
    ),
    "_docs/_user_guide/administrative/app_settings/manage_your_braze_users/user_permissions.md": (
        "_docs/_user_guide/administer/global/user_management/permissions.md"
    ),
    "_docs/_user_guide/administrative/app_settings/tags.md": (
        "_docs/_user_guide/administer/global/workspace_settings/tags.md"
    ),
    "_docs/_user_guide/message_building_by_channel/whatsapp/faqs.md": (
        "_docs/_user_guide/channels/whatsapp/faq.md"
    ),
    "_docs/_user_guide/message_building_by_channel/push/users_and_subscriptions.md": (
        "_docs/_user_guide/channels/push/push_registration.md"
    ),
    "_docs/_user_guide/message_building_by_channel/email/reporting_and_analytics/": (
        "_docs/_user_guide/channels/email/reporting/analytics_glossary.md"
    ),
    "_docs/_user_guide/message_building_by_channel/content_cards/create/": (
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md"
    ),
    "_docs/_user_guide/message_building_by_channel/content_cards/create.md": (
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md"
    ),
    "_docs/_user_guide/channels/content_cards/create/": (
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md"
    ),
    "_docs/_user_guide/channels/content_cards/create.md": (
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md"
    ),
    "_docs/_user_guide/message_building_by_channel/email/testing.md": (
        "_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md"
    ),
    "_docs/_user_guide/channels/email/testing.md": (
        "_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md"
    ),
    "_docs/_user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/": (
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md"
    ),
    "_docs/_user_guide/channels/email/drag_and_drop/dnd_email_style_settings/": (
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md"
    ),
    "_docs/_user_guide/channels/email/drag_and_drop/dnd_email_style_settings": (
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md"
    ),
    "_docs/_user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks.md": (
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md"
    ),
    "_docs/_user_guide/channels/email/drag_and_drop/dnd_content_blocks.md": (
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md"
    ),
    "_docs/_user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/": (
        "_docs/_user_guide/administer/global/user_management/manage_company_users.md"
    ),
    "_docs/_user_guide/administer/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/": (
        "_docs/_user_guide/administer/global/user_management/manage_company_users.md"
    ),
    "_docs/_user_guide/administer/personal/troubleshooting.md": (
        "_docs/_user_guide/administer/personal/braze_support.md"
    ),
    "_docs/_user_guide/data/activation/custom_data/custom_attributes": (
        "_docs/_user_guide/data/activation/attributes/custom_attributes.md"
    ),
    "_docs/_user_guide/help/help_articles/segments/segment_showing_0_users/": (
        "_docs/_user_guide/audience/segments/segmentation_filters.md"
    ),
    "_docs/_user_guide/help/help_articles/segments/segment_showing_0_users.md": (
        "_docs/_user_guide/audience/segments/segmentation_filters.md"
    ),
    "_docs/_user_guide/message_building_by_channel/in-app_messages/creative_details/slideup.md": (
        "_docs/_user_guide/channels/in_app_messages/message_types/slideup.md"
    ),
    "_docs/_user_guide/personalization_and_dynamic_content/liquid/using_liquid/": (
        "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/using_liquid.md"
    ),
    "_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md": (
        "_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md"
    ),
}

# Longest-old-prefix first (applied after exact map misses).
_PATH_INFERENCE_PREFIX_RAW: tuple[tuple[str, str], ...] = (
    (
        "_docs/_user_guide/messaging/campaigns/building_campaigns/delivery_types/triggered_delivery/",
        "_docs/_user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/",
    ),
    (
        "_docs/_user_guide/personalization_and_dynamic_content/liquid/",
        "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/",
    ),
    (
        "_docs/_user_guide/messaging/locations_and_geofences/",
        "_docs/_user_guide/audience/locations_and_geofences/",
    ),
    (
        "_docs/_user_guide/messaging/segments/",
        "_docs/_user_guide/audience/segments/",
    ),
    (
        "_docs/_user_guide/analytics/reporting/",
        "_docs/_user_guide/analytics/reports/",
    ),
    (
        "_docs/_user_guide/messaging/campaigns/managing_campaigns/",
        "_docs/_user_guide/messaging/campaigns/manage_campaigns/",
    ),
)
PATH_INFERENCE_PREFIXES: tuple[tuple[str, str], ...] = tuple(
    sorted(_PATH_INFERENCE_PREFIX_RAW, key=lambda kv: -len(kv[0]))
)

# Basenames that appear exactly once under `_docs/` (excluding ambiguous short/common names).
_BASENAME_INDEX_EXCLUDE: frozenset[str] = frozenset(
    {
        "faq.md",
        "index.md",
        "home.md",
        "about.md",
        "readme.md",
        "changelog.md",
    }
)
_unique_basename_to_rel: dict[str, str] | None = None
_placement_candidate_paths: list[str] | None = None

_PLACEMENT_STOPWORDS = frozenset(
    {
        "what",
        "when",
        "where",
        "why",
        "how",
        "does",
        "the",
        "and",
        "for",
        "with",
        "from",
        "that",
        "this",
        "are",
        "can",
        "not",
        "you",
        "your",
        "have",
        "has",
        "was",
        "were",
        "will",
        "braze",
        "user",
        "users",
        "about",
        "into",
        "their",
        "there",
        "been",
        "would",
        "could",
        "should",
        "than",
        "then",
        "they",
        "them",
        "any",
        "all",
        "may",
        "might",
        "also",
        "only",
        "need",
        "our",
        "via",
        "per",
        "its",
        "who",
        "why",
    }
)

_PLACEMENT_PREFERRED_BASENAMES: frozenset[str] = frozenset(
    {
        "faq.md",
        "faqs.md",
        "troubleshooting.md",
        "analytics_glossary.md",
        "reporting.md",
        "engagement_reports.md",
        "report_builder.md",
        "best_practices.md",
        "custom_attributes.md",
        "connected_content.md",
        "segmentation_filters.md",
        "subscriptions.md",
        "permissions.md",
        "braze_support.md",
        "sending_test_messages.md",
        "campaign_analytics.md",
        "custom_events_report.md",
        "data_points.md",
        "manage_company_users.md",
        "merge_duplicate_users.md",
        "sdk_integration.md",
        "reading_verbose_logs.md",
    }
)


def strip_url_fragment(path: str) -> str:
    """`_docs/foo.md#anchor` → `_docs/foo.md`."""
    return path.split("#", 1)[0].rstrip("/")


def normalize_remapped_doc_path(raw: str) -> str:
    """IA remaps + strip line ranges and URL fragments; used as key for inference maps."""
    s = raw.strip().replace("\\", "/")
    s = strip_line_range_suffix(s)
    s = strip_url_fragment(s)
    return apply_path_remaps(s)


def _exact_inference_lookup_keys(raw: str) -> list[str]:
    """Candidate keys for `PATH_INFERENCE_EXACT` (raw, remapped, with/without trailing slash)."""
    stripped = strip_url_fragment(raw.strip())
    norm = normalize_remapped_doc_path(raw)
    keys: list[str] = []
    for k in (
        norm.rstrip("/"),
        norm,
        stripped.rstrip("/"),
        stripped,
        f"{norm.rstrip('/')}.md",
        f"{stripped.rstrip('/')}.md",
    ):
        if k and k not in keys:
            keys.append(k)
    return keys


def build_unique_basename_index(root: Path) -> dict[str, str]:
    """Map `filename.md` → single `_docs/...` relative path when unambiguous repo-wide."""
    by_name: dict[str, list[str]] = defaultdict(list)
    docs = root / "_docs"
    if not docs.is_dir():
        return {}
    for p in docs.rglob("*.md"):
        if "_help/help_articles" in str(p):
            continue
        try:
            rel = p.relative_to(root).as_posix()
        except ValueError:
            continue
        if not rel.startswith("_docs/"):
            continue
        by_name[p.name].append(rel)
    out: dict[str, str] = {}
    for name, paths in by_name.items():
        if len(paths) != 1:
            continue
        if name in _BASENAME_INDEX_EXCLUDE or len(name) < 12:
            continue
        out[name] = paths[0]
    return out


def get_unique_basename_index(root: Path) -> dict[str, str]:
    global _unique_basename_to_rel
    if _unique_basename_to_rel is None:
        _unique_basename_to_rel = build_unique_basename_index(root)
    return _unique_basename_to_rel


def resolve_path_with_inference(
    raw: str,
    root: Path,
    basename_index: dict[str, str],
) -> tuple[Path | None, str | None]:
    """
    Resolve CSV `_docs/...` hint to an on-disk file: direct remaps first, then scripted inference.
    Returns (resolved Path or None, short note for logging / optional queue footnotes).
    """
    direct = resolve_existing_path(raw, root)
    if direct:
        return direct, None

    norm = normalize_remapped_doc_path(raw)
    for key in _exact_inference_lookup_keys(raw):
        if key in PATH_INFERENCE_EXACT:
            alt = PATH_INFERENCE_EXACT[key]
            hit = resolve_existing_path(alt, root)
            if hit:
                return hit, f"inferred exact map `{key}` → `{alt}`"

    for old_prefix, new_prefix in PATH_INFERENCE_PREFIXES:
        if norm.startswith(old_prefix):
            cand = new_prefix + norm[len(old_prefix) :]
            hit = resolve_existing_path(cand, root)
            if hit:
                return hit, f"inferred prefix `{old_prefix}` → `{new_prefix}` on `{norm}`"

    base = Path(norm).name
    if base.endswith(".md") and base in basename_index:
        alt = basename_index[base]
        if alt != norm:
            hit = resolve_existing_path(alt, root)
            if hit:
                return hit, f"inferred unique basename `{base}` → `{alt}`"

    # Directory-style CSV paths: prefer `faq.md` or a single `.md` in the folder.
    dir_norm = norm.rstrip("/")
    if dir_norm and not dir_norm.endswith(".md"):
        dir_path = root / dir_norm
        if dir_path.is_dir():
            faq = dir_path / "faq.md"
            if faq.is_file():
                rel = faq.relative_to(root).as_posix()
                return faq, f"inferred directory faq `{norm}` → `{rel}`"
            md_files = sorted(dir_path.glob("*.md"))
            if len(md_files) == 1:
                rel = md_files[0].relative_to(root).as_posix()
                return md_files[0], f"inferred single file in directory `{norm}` → `{rel}`"

    # Truncated CSV paths (no `.md` suffix): try basename glob under `_docs/`.
    stem = Path(norm).name
    if stem and not stem.endswith(".md"):
        pattern = stem if stem.endswith("_") else f"{stem}*"
        docs_root = root / "_docs"
        if docs_root.is_dir():
            hits = sorted(docs_root.rglob(f"{pattern}.md"))[:8]
            if len(hits) == 1:
                return hits[0], f"inferred truncated path `{norm}` → `{hits[0].relative_to(root).as_posix()}`"

    return None, None


# Keyword/topic routing when CSV has no resolvable `_docs/...` hint (agent Phase 1 subset).
_CONTEXT_TOPIC_ROUTES: tuple[tuple[re.Pattern[str], list[str]], ...] = (
    (re.compile(r"subscription\s+group", re.I), [
        "_docs/_api/endpoints/subscription_groups.md",
    ]),
    (re.compile(r"\bcurrents\b", re.I), [
        "_docs/_user_guide/data/distribution/braze_currents/faq.md",
    ]),
    (re.compile(r"\bliquid\b|abort_message", re.I), [
        "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/faq.md",
        "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/using_liquid.md",
    ]),
    (re.compile(r"content\s+card", re.I), [
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md",
        "_docs/_user_guide/channels/content_cards/reporting.md",
        "_docs/_user_guide/messaging/messaging_fundamentals/know_before_you_send.md",
    ]),
    (re.compile(r"\bcanvas\b", re.I), [
        "_docs/_user_guide/messaging/canvas/faqs.md",
    ]),
    (re.compile(r"in[- ]?app|iam\b|slideup|slide-up", re.I), [
        "_docs/_user_guide/channels/in_app_messages/troubleshooting.md",
        "_docs/_user_guide/channels/in_app_messages/customize.md",
    ]),
    (re.compile(r"\bpush\b", re.I), [
        "_docs/_user_guide/channels/push/troubleshooting.md",
        "_docs/_user_guide/channels/push/push_registration.md",
    ]),
    (re.compile(r"\bwhatsapp\b", re.I), [
        "_docs/_user_guide/channels/whatsapp/faq.md",
    ]),
    (re.compile(r"segment(ation)?\s+filter|previously part of a segment", re.I), [
        "_docs/_user_guide/audience/segments/segmentation_filters.md",
    ]),
    (re.compile(r"user\s+import|external_id", re.I), [
        "_docs/_user_guide/audience/manage_audience/import_users/csv_import.md",
    ]),
    (re.compile(r"email.*(unsubscribe|click|deliver|bounce|quota|from email)", re.I), [
        "_docs/_user_guide/channels/email/reporting/analytics_glossary.md",
        "_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md",
        "_docs/_user_guide/administer/global/workspace_settings/email_preferences.md",
    ]),
    (re.compile(r"media\s+library|dalle|ai\s+image", re.I), [
        "_docs/_user_guide/messaging/design_and_edit/media_library.md",
    ]),
    (re.compile(r"api\s+(payload\s+)?limit", re.I), [
        "_docs/_api/api_limits.md",
    ]),
    (re.compile(r"google\s+tag\s+manager|\bgtm\b", re.I), [
        "_docs/_developer_guide/sdk_integration/google_tag_manager.md",
    ]),
    (re.compile(r"deep\s+link|webview|open\s+web\s+url", re.I), [
        "_includes/developer_guide/swift/deep_linking.md",
        "_includes/developer_guide/android/_global/deep_linking.md",
    ]),
    (re.compile(r"frequency\s+cap|rate\s+limit", re.I), [
        "_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md",
    ]),
    (re.compile(r"amplitude|mau\b|dau\b|session\s+count", re.I), [
        "_docs/_user_guide/analytics/dashboards/home.md",
        "_docs/_partners/data_and_analytics/analytics/amplitude.md",
    ]),
    (re.compile(r"permission|user\s+permissions", re.I), [
        "_docs/_user_guide/administer/global/user_management/permissions.md",
    ]),
    (re.compile(r"\btag(s)?\b.*(parent|archiv)", re.I), [
        "_docs/_user_guide/administer/global/workspace_settings/tags.md",
    ]),
    (re.compile(r"connected\s+content|webhook.*response", re.I), [
        "_docs/_user_guide/messaging/design_and_edit/personalize/connected_content.md",
        "_docs/_user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries.md",
    ]),
    (re.compile(r"engagement\s+report|report\s+builder.*(expir|download|link|broken)", re.I), [
        "_docs/_user_guide/analytics/reports/engagement_reports.md",
        "_docs/_user_guide/analytics/reports/report_builder.md",
    ]),
    (re.compile(r"custom\s+attribute", re.I), [
        "_docs/_user_guide/data/activation/attributes/custom_attributes.md",
        "_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md",
    ]),
    (re.compile(r"heatmap|hidden\s+link", re.I), [
        "_docs/_user_guide/channels/email/reporting/analytics_glossary.md",
        "_docs/_user_guide/channels/email/email_setup/open_pixel_and_click_tracking.md",
    ]),
    (re.compile(r"seed\s+email|sending\s+test", re.I), [
        "_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md",
    ]),
    (re.compile(r"google\s+sso|single\s+sign\s+on|\bsso\b", re.I), [
        "_docs/_user_guide/administer/global/saml_single_sign_on/saml_sso_setup.md",
    ]),
    (re.compile(r"dark\s+mode.*email|email.*dark\s+mode", re.I), [
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md",
    ]),
    (re.compile(r"react\s+native|react\s+sdk", re.I), [
        "_docs/_developer_guide/getting_started/platform_overview.md",
        "_docs/_developer_guide/changelogs.md",
        "_docs/_developer_guide/sdk_integration.md",
    ]),
    (re.compile(r"content\s+card.*(pin|unpin|refresh|sync|session|web\s+sdk|new\s+tab|open.*tab)", re.I), [
        "_docs/_user_guide/channels/content_cards/creative_details.md",
        "_docs/_user_guide/channels/content_cards/create_a_content_card.md",
        "_docs/_developer_guide/content_cards/customizing_cards/feed.md",
    ]),
    (re.compile(r"campaign.*(analytics|metric|historical|last\s+sent)", re.I), [
        "_docs/_user_guide/analytics/reports/campaign_analytics.md",
        "_docs/_user_guide/messaging/campaigns/test_campaigns/campaign_analytics.md",
    ]),
    (re.compile(r"segment.*(profile|filter|criteria|0\s+user|reachable|match)", re.I), [
        "_docs/_user_guide/audience/segments/segmentation_filters.md",
    ]),
    (re.compile(r"duplicate.*(user|profile|email)|multiple.*profile.*email", re.I), [
        "_docs/_user_guide/audience/manage_audience/merge_duplicate_users.md",
    ]),
    (re.compile(r"dashboard\s+user|adding\s+user|email\s+is\s+already\s+taken|multiple\s+compan", re.I), [
        "_docs/_user_guide/administer/global/user_management/manage_company_users.md",
        "_docs/_user_guide/administer/global/user_management/teams.md",
        "_docs/_user_guide/administer/global/user_management/permissions.md",
    ]),
    (re.compile(r"content\s+block|drag\s+and\s+drop|dnd\s+editor|dnd\s+search|alignment\s+setting", re.I), [
        "_docs/_user_guide/channels/email/drag_and_drop/faq.md",
        "_docs/_user_guide/channels/email/drag_and_drop/dnd_editor_blocks.md",
    ]),
    (re.compile(r"click\s+track|relay.*denied|550\s+5\.7\.1|phone\s+number", re.I), [
        "_docs/_user_guide/channels/email/email_setup/open_pixel_and_click_tracking.md",
        "_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md",
    ]),
    (re.compile(r"sms.*subscrib|subscription\s+state|unique\s+recipient", re.I), [
        "_docs/_user_guide/channels/sms_mms_and_rcs/faqs.md",
        "_docs/_user_guide/channels/email/subscriptions.md",
    ]),
    (re.compile(r"\bbimi\b", re.I), [
        "_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md",
    ]),
    (re.compile(r"data\s+point|subscription.*usage|data\s+refresh", re.I), [
        "_docs/_user_guide/data/infrastructure/data_points.md",
    ]),
    (re.compile(r"api\s+campaign|delivery\s+fail", re.I), [
        "_docs/_user_guide/analytics/reports/campaign_analytics.md",
        "_docs/_api/endpoints/export/campaigns/get_campaign_analytics.md",
    ]),
    (re.compile(r"web\s+cookie|3rd\s+party.*cookie|third.party.*cookie", re.I), [
        "_docs/_developer_guide/platforms/web/content_security_policy.md",
    ]),
    (re.compile(r"azure.*whitelist|storage.*ip|whitelisting.*azure", re.I), [
        "_docs/_partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents.md",
    ]),
    (re.compile(r"exact\s+statistic|estimated\s+real\s+open|open\s+likelihood|machine\s+open", re.I), [
        "_docs/_user_guide/channels/email/reporting/analytics_glossary.md",
    ]),
    (re.compile(r"scheduled.*campaign|send.*audience|day\s+before|schedule\s+time", re.I), [
        "_docs/_user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery.md",
    ]),
    (re.compile(r"custom\s+event.*(export|identify|perform)", re.I), [
        "_docs/_user_guide/analytics/reports/custom_events_report.md",
        "_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md",
        "_docs/_user_guide/data/activation/events/custom_events.md",
    ]),
    (re.compile(r"data\s+not\s+getting|sdk.*rest.*api|user\s+data\s+discrepanc", re.I), [
        "_docs/_developer_guide/sdk_integration.md",
        "_docs/_developer_guide/sdk_integration/reading_verbose_logs.md",
    ]),
    (re.compile(r"session.*0|zero\s+session", re.I), [
        "_docs/_user_guide/analytics/dashboards/home.md",
        "_docs/_developer_guide/sdk_integration/reading_verbose_logs.md",
    ]),
    (re.compile(r"dashboard.*(load|access)|can't\s+fully\s+access", re.I), [
        "_docs/_user_guide/administer/personal/braze_support.md",
        "_docs/_user_guide/administer/global/user_management/permissions.md",
    ]),
)


def _row_context_text(row: dict[str, str]) -> str:
    return " ".join(
        filter(
            None,
            [
                row.get("title"),
                row.get("conflict"),
                row.get("suggested_change"),
                row.get("codebase_evidence"),
            ],
        )
    )


def tokenize_for_doc_placement(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]{3,}", text.lower())
    return {w for w in words if w not in _PLACEMENT_STOPWORDS}


def build_placement_candidate_index(root: Path) -> list[str]:
    """FAQ/troubleshooting/reporting and other common edit targets for best-fit placement."""
    candidates: set[str] = set()
    docs = root / "_docs"
    if docs.is_dir():
        for p in docs.rglob("*.md"):
            if "_help/help_articles" in str(p):
                continue
            try:
                rel = p.relative_to(root).as_posix()
            except ValueError:
                continue
            if not rel.startswith("_docs/"):
                continue
            if p.name in _PLACEMENT_PREFERRED_BASENAMES:
                candidates.add(rel)
                continue
            if "/channels/" in rel and p.name.startswith(("create_", "reporting")):
                candidates.add(rel)
    for _, paths in _CONTEXT_TOPIC_ROUTES:
        candidates.update(paths)
    return sorted(candidates)


def get_placement_candidate_index(root: Path) -> list[str]:
    global _placement_candidate_paths
    if _placement_candidate_paths is None:
        _placement_candidate_paths = build_placement_candidate_index(root)
    return _placement_candidate_paths


def _resolve_placement_candidate(raw: str, root: Path) -> str | None:
    """Return repo-relative `_docs/...` path when `raw` resolves on disk."""
    hit = resolve_existing_path(raw, root)
    if hit:
        try:
            rel = hit.relative_to(root).as_posix()
            if rel.startswith("_docs/"):
                return rel
        except ValueError:
            pass
    uniq = get_unique_basename_index(root)
    hit, _ = resolve_path_with_inference(raw, root, uniq)
    if hit:
        try:
            rel = hit.relative_to(root).as_posix()
            if rel.startswith("_docs/"):
                return rel
        except ValueError:
            pass
    return None


def score_doc_placement_candidate(
    rel: str,
    tokens: set[str],
    topic_patterns: list[str],
) -> float:
    low = rel.lower()
    path_tokens = set(re.findall(r"[a-z0-9]{3,}", low))
    overlap = tokens & path_tokens
    score = len(topic_patterns) * 5.0
    score += min(len(overlap), 10) * 1.5
    for tok in tokens:
        if len(tok) >= 5 and tok in low:
            score += 0.75
    base = Path(rel).name
    if base in _PLACEMENT_PREFERRED_BASENAMES:
        score += 1.5
    if "faq" in base or "troubleshooting" in base:
        score += 1.0
    return score


def infer_best_doc_path(
    row: dict[str, str],
    root: Path,
) -> tuple[str | None, str | None]:
    """
    Score topic-route and keyword-overlap candidates to pick the best existing `_docs/...` page.
    Used when CSV hints do not resolve after remaps and scripted inference.
    """
    text = _row_context_text(row)
    if not text.strip():
        return None, None
    route_text = " ".join(
        filter(None, [row.get("title"), row.get("conflict"), row.get("codebase_evidence")])
    )
    tokens = tokenize_for_doc_placement(text)
    title_tokens = tokenize_for_doc_placement(row.get("title") or "")
    matched_patterns: dict[str, list[str]] = defaultdict(list)
    for pattern, paths in _CONTEXT_TOPIC_ROUTES:
        if not pattern.search(route_text):
            continue
        for p in paths:
            matched_patterns[p].append(pattern.pattern)

    candidates: set[str] = set(matched_patterns.keys())
    for rel in get_placement_candidate_index(root):
        path_tokens = set(re.findall(r"[a-z0-9]{3,}", rel.lower()))
        if tokens & path_tokens:
            candidates.add(rel)

    best_rel: str | None = None
    best_score = 0.0
    best_patterns: list[str] = []
    for raw in candidates:
        resolved = _resolve_placement_candidate(raw, root)
        if not resolved:
            continue
        patterns = matched_patterns.get(raw, [])
        sc = score_doc_placement_candidate(resolved, tokens, patterns)
        path_tokens = set(re.findall(r"[a-z0-9]{3,}", resolved.lower()))
        sc += len(title_tokens & path_tokens) * 2.0
        if sc > best_score:
            best_score = sc
            best_rel = resolved
            best_patterns = patterns

    if not best_rel:
        return None, None
    if best_patterns:
        pat_hint = best_patterns[0][:48]
        return best_rel, f"best-fit doc (topic `{pat_hint}`, score={best_score:.1f}) → `{best_rel}`"
    if best_score >= 3.0:
        return best_rel, f"best-fit doc (keyword overlap score={best_score:.1f}) → `{best_rel}`"
    return None, None


def infer_context_doc_path(
    row: dict[str, str],
    root: Path,
) -> tuple[str | None, str | None]:
    """Topic/keyword best-fit placement when extraction + IA remaps find no on-disk file."""
    return infer_best_doc_path(row, root)


def normalized_implementation_status(raw: str | None) -> str:
    if not raw or not str(raw).strip():
        return ""
    first_line = str(raw).strip().split("\n", 1)[0].strip()
    return first_line.lower()


def strip_line_range_suffix(path: str) -> str:
    """`_docs/_api/errors.md:19-28` -> `_docs/_api/errors.md`."""
    return re.sub(r":\d+(?:-\d+)?$", "", path)


def apply_path_remaps(path: str) -> str:
    out = path.replace("\\", "/")
    for old, new in PATH_FRAG_REMAPS:
        out = out.replace(old, new)
    return out


def extract_doc_paths(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
    conflict: str | None = None,
) -> list[str]:
    """Return unique `_docs/...` paths (excluding help_articles), in discovery order."""
    seen: set[str] = set()
    out: list[str] = []
    chunks = [doc_path or "", codebase_evidence or "", suggested_change or "", conflict or ""]
    for chunk in chunks:
        for m in _DOCS_PATH_RE.finditer(chunk):
            p = m.group(1).strip().rstrip(").,;`:")
            p = strip_url_fragment(strip_line_range_suffix(p))
            if "_docs/_help/help_articles" in p:
                continue
            if not p.startswith("_docs/"):
                continue
            if p not in seen:
                seen.add(p)
                out.append(p)
    return out


def resolve_existing_path(raw: str, root: Path) -> Path | None:
    """Return first Path that exists on disk after remaps and .md fallbacks."""
    candidates: list[Path] = []
    p = strip_url_fragment(apply_path_remaps(raw.strip()))
    p = strip_line_range_suffix(p)
    full = root / p
    candidates.append(full)
    if full.suffix.lower() != ".md":
        candidates.append(full.with_suffix(".md"))
    for c in candidates:
        try:
            if c.is_file():
                return c
        except OSError:
            continue
    # If path is directory-ish, try index (rare in CSV)
    if full.suffix == "":
        for name in ("index.md", "home.md"):
            alt = full / name
            if alt.is_file():
                return alt
    return None


def resolved_primary_doc(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
    root: Path,
    conflict: str | None = None,
    allow_context_inference: bool = False,
    row_for_context: dict[str, str] | None = None,
) -> tuple[str | None, Path | None, str | None]:
    """
    First `_docs/...` path from row fields that resolves to a file under `root`.
    Tries IA remaps, then scripted inference (exact map, prefixes, unique basename).
    Returns (normalized `_docs/...` string relative to repo, resolved Path or None, inference note or None).
    """
    uniq = get_unique_basename_index(root)
    for raw in extract_doc_paths(doc_path, codebase_evidence, suggested_change, conflict):
        hit, note = resolve_path_with_inference(raw, root, uniq)
        if hit:
            try:
                rel = hit.relative_to(root)
                rel_s = rel.as_posix()
                if rel_s.startswith("_docs/"):
                    return rel_s, hit, note
            except ValueError:
                pass
    if allow_context_inference and row_for_context:
        rel, note = infer_context_doc_path(row_for_context, root)
        if rel:
            hit = resolve_existing_path(rel, root)
            if hit:
                return rel, hit, note
    return None, None, None


def help_only_paths(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
    conflict: str | None = None,
) -> bool:
    """True if every extracted _docs path is under help_articles (and at least one exists)."""
    all_paths: list[str] = []
    for chunk in (doc_path or "", codebase_evidence or "", suggested_change or "", conflict or ""):
        for m in _DOCS_PATH_RE.finditer(chunk):
            all_paths.append(m.group(1).strip().rstrip(").,;"))
    docs_hits = [p for p in all_paths if p.startswith("_docs/")]
    if not docs_hits:
        return False
    return all("_help/help_articles" in p for p in docs_hits)


def has_substantive_docs_hint(
    doc_path: str | None,
    codebase_evidence: str | None,
    suggested_change: str | None,
) -> bool:
    """Any `_docs/` reference outside help_articles in row text."""
    for chunk in (doc_path or "", codebase_evidence or "", suggested_change or "", conflict or ""):
        for m in _DOCS_PATH_RE.finditer(chunk):
            p = m.group(1)
            if "_help/help_articles" in p:
                continue
            if p.startswith("_docs/"):
                return True
    return False


def row_has_resolvable_doc(row: dict[str, str], root: Path) -> bool:
    rel, _, _ = resolved_primary_doc(
        row.get("doc_path"),
        row.get("codebase_evidence"),
        row.get("suggested_change"),
        root,
        conflict=row.get("conflict"),
        allow_context_inference=True,
        row_for_context=row,
    )
    return rel is not None


def infer_vertical(primary_rel: str | None, team: str) -> str:
    """IA bucket for batching (path-first, then team)."""
    if not primary_rel:
        return f"unknown ({team or 'no team'})"
    parts = primary_rel.split("/")
    if len(parts) >= 3 and parts[0] == "_docs":
        if parts[1] == "_user_guide" and len(parts) >= 3:
            return parts[2]
        if parts[1] in ("_api", "_developer_guide", "_partners", "_hidden", "_docs_pages", "_releases"):
            return parts[1].lstrip("_")
    return "other"


def doc_path_branch_slug(primary_rel: str) -> str:
    """Short slug for branch names, e.g. push-troubleshooting from .../push/troubleshooting.md."""
    name = Path(primary_rel.replace("\\", "/")).stem
    parts = primary_rel.replace("\\", "/").split("/")
    parent = parts[-2] if len(parts) >= 2 else ""
    if parent and parent not in ("_docs", "_user_guide", "channels", "messaging"):
        return f"{parent}-{name}"[:60].lower().replace("_", "-")
    return name[:60].lower().replace("_", "-")


def product_vertical_hint(primary_rel: str) -> str:
    """
    Fallback product vertical from `_docs` path when assignees CSV has no ``Team`` match.
    Prefer `infer_product_vertical_label()` / `product_vertical_for_doc_path()` for Phase 2.
    """
    low = primary_rel.replace("\\", "/").lower()
    if "_docs/_user_guide/channels/push" in low:
        return "Push"
    if "_docs/_user_guide/channels/email" in low:
        return "Email"
    if (
        "_docs/_user_guide/channels/sms" in low
        or "sms_mms" in low
        or "/sms_mms_and_rcs/" in low
    ):
        return "SMS / MMS / RCS"
    if "_docs/_user_guide/channels/content_cards" in low:
        return "Content Cards"
    if "_docs/_user_guide/channels/in-app" in low or "in_app_messages" in low:
        return "In-app messages"
    if "_docs/_user_guide/channels/line" in low:
        return "LINE"
    if "_docs/_user_guide/channels/whatsapp" in low:
        return "WhatsApp"
    if "_docs/_user_guide/administer/" in low:
        return "Dashboard & administration"
    if "_docs/_user_guide/messaging/design_and_edit/personalize/connected_content" in low:
        return "Messaging (Connected Content)"
    if "_docs/_user_guide/messaging/design_and_edit/personalize/liquid" in low:
        return "Messaging (Liquid personalization)"
    if "_docs/_user_guide/messaging/canvas" in low:
        if low.rstrip("/").endswith("action_paths.md"):
            return "Canvas (Email channel triggers — confirm Email vs Canvas PM if needed)"
        return "Canvas"
    if "_docs/_user_guide/messaging/" in low:
        return "Messaging & automation (Campaigns / Canvas-adjacent)"
    if "_docs/_user_guide/analytics/" in low:
        return "Analytics"
    if "_docs/_user_guide/audience/" in low:
        return "Audience & segments"
    if "braze_currents" in low or "/currents/" in low:
        return "Currents"
    if "_docs/_user_guide/data/" in low:
        return "Data platform"
    if "_docs/_user_guide/brazeai/" in low:
        return "Braze AI / Intelligence Suite"
    if "_docs/_api/" in low:
        return "API / platform engineering"
    if "_docs/_developer_guide/" in low:
        return "SDK & developer integrations"
    if "_docs/_partners/" in low:
        if "facebook" in low or "audience_sync" in low:
            return "Partners (Audience Sync / Facebook)"
        return "Partners & integrations"
    if "_docs/_releases/" in low:
        return "Product updates (cross-channel — confirm channel PM)"
    if "_docs/_user_guide/administrative/" in low:
        return "Dashboard & administration"
    if "_docs/_user_guide/onboarding" in low:
        return "Onboarding & solution engineering"
    if "_docs/_user_guide/channels/" in low:
        return "Channels (confirm Email / Push / etc.)"
    return "TBD — confirm product owner and update the table below"


def infer_product_vertical_label(primary_rel: str) -> str:
    """Product vertical from assignees CSV ``Team`` column, else path-based hint."""
    path = primary_rel.replace("\\", "/").strip()
    team = product_vertical_for_doc_path(path)
    if team:
        return team
    return product_vertical_hint(primary_rel)


def conflict_resolution_skip(raw: str | None) -> str | None:
    if not raw:
        return None
    low = raw.strip().lower()
    # Exact `inconclusive` is actionable when other gates pass; Phase 2 verifies in reference repos.
    for sub in CONFLICT_SKIP_SUBSTRINGS:
        if sub in low:
            return f"conflict_resolution signals manual skip (`{sub}`)."
    return None


@dataclass
class RowOut:
    row: dict[str, str]
    primary_rel: str | None = None
    resolved_path: Path | None = None
    vertical: str = ""
    skip_reason: str | None = None
    skip_context: str | None = None
    path_inference: str | None = None
    reference_verify: bool = False


def classify_row(
    row: dict[str, str],
    root: Path,
) -> RowOut:
    article_id = article_id_from_row(row)
    title = (row.get("title") or "").strip()
    team = (row.get("team") or "").strip()
    target = (row.get("target") or "").strip().lower()
    impl = normalized_implementation_status(row.get("implementation_status"))
    cr = row.get("conflict_resolution") or ""
    suggested = row.get("suggested_change")
    doc_path = row.get("doc_path")
    evidence = row.get("codebase_evidence")

    def skip(msg: str, ctx: str | None = None) -> RowOut:
        return RowOut(row=row, skip_reason=msg, skip_context=ctx)

    if impl == "archived":
        return skip(
            "`implementation_status` first line is `archived`.",
            ctx="Dispositioned KA; do not draft new public docs work from this row.",
        )
    if impl == "actioned":
        return skip(
            "`implementation_status` first line is `actioned`.",
            ctx="Work already recorded as done or superseded in the migration tracker.",
        )
    if impl and impl not in PHASE1_ALLOWED_IMPL_STATUSES:
        raw_first = str(row.get("implementation_status") or "").strip().split("\n", 1)[0].strip()
        return skip(
            f"`implementation_status` first line is `{impl}` — unlisted or non-public disposition; "
            "default skip per Phase 1 gates in generate_kb_phase1_outputs.py.",
            ctx=f"Raw first line: `{raw_first}`.",
        )

    if target == "inconclusive":
        return skip(
            "`target` is `inconclusive`.",
            ctx="Outcome surface for the row is unclear; do not open a Phase 2 docs PR without analyst override.",
        )

    reference_verify = cr.strip().lower() == "inconclusive"

    crs = conflict_resolution_skip(cr)
    if crs:
        cr_trim = cr.strip().replace("\n", " ")
        ctx = f"`conflict_resolution` (raw): {cr_trim[:240]}{'…' if len(cr_trim) > 240 else ''}"
        return skip(crs, ctx=ctx)

    if not suggested or not str(suggested).strip():
        return skip(
            "`suggested_change` is empty or whitespace.",
            ctx="Add a concrete implementation brief before Phase 2.",
        )

    if is_vague_suggested_change(suggested):
        first = str(suggested).strip().split("\n", 1)[0].strip()
        return skip(
            "`suggested_change` is vague or lacks a concrete first-line edit "
            "(starts with a non-actionable phrase per script heuristics).",
            ctx=f"First line: `{first}`",
        )

    if help_only_paths(doc_path, evidence, suggested, conflict=row.get("conflict")):
        hp = [m.group(1) for m in _DOCS_PATH_RE.finditer(" ".join(filter(None, [doc_path, evidence, suggested])))]
        hp = [p.strip().rstrip(").,;`") for p in hp if "_help/help_articles" in p][:4]
        ctx = "Paths: " + ", ".join(f"`{p}`" for p in hp) if hp else "All `_docs` hits point at internal help mirrors."
        return skip(
            "All extracted `_docs/...` paths are under `_docs/_help/help_articles/` (not a public edit target).",
            ctx=ctx,
        )

    if target == "knowledge_article" and not has_substantive_docs_hint(
        doc_path, evidence, suggested, conflict=row.get("conflict")
    ):
        return skip(
            "`target` is `knowledge_article` and the row has no substantive `_docs/` hint "
            "(KA-only / no Braze Docs PR from CSV).",
            ctx="Archive/consolidation-only work with no `_docs/...` path in `doc_path`, evidence, or `suggested_change`.",
        )

    primary_rel, rpath, path_inference = resolved_primary_doc(
        doc_path,
        evidence,
        suggested,
        root,
        conflict=row.get("conflict"),
        allow_context_inference=True,
        row_for_context=row,
    )
    if not primary_rel:
        extracted = extract_doc_paths(doc_path, evidence, suggested, row.get("conflict"))
        if extracted:
            shown = ", ".join(f"`{p}`" for p in extracted[:5])
            if len(extracted) > 5:
                shown += f", … (+{len(extracted) - 5} more)"
            ctx = (
                f"Extracted `_docs` candidates (none resolve after IA remaps, scripted inference, "
                f"or best-fit placement): {shown}. "
                "Fix `doc_path` / evidence paths or extend inference maps / `_CONTEXT_TOPIC_ROUTES` in "
                "`scripts/salesforce-analyzer/generate_kb_phase1_outputs.py`."
            )
        else:
            ctx = (
                "No `_docs/...` strings found in `doc_path`, `codebase_evidence`, or `suggested_change` "
                "(or only non-doc targets such as `platform/...` without a docs path). "
                "Best-fit topic/keyword placement did not score a defensible target."
            )
        return skip(
            "No locatable on-disk `_docs/...` target after path extraction, IA remaps, scripted inference, "
            "and best-fit placement (insufficient CSV path, stale path, or needs manual `doc_path` fix).",
            ctx=ctx,
        )

    vert = infer_vertical(primary_rel, team)
    return RowOut(
        row=row,
        primary_rel=primary_rel,
        resolved_path=rpath,
        vertical=vert,
        skip_reason=None,
        path_inference=path_inference,
        reference_verify=reference_verify,
    )


def load_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        print(f"Missing input: {path}", file=sys.stderr)
        sys.exit(2)
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        return fieldnames, list(reader)


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def prune_dispositioned_rows(
    rows: list[dict[str, str]],
) -> tuple[list[dict[str, str]], int, int]:
    """
    Drop rows whose implementation_status first line is archived or actioned.
    Returns (kept_rows, n_archived_removed, n_actioned_removed).
    """
    kept: list[dict[str, str]] = []
    n_archived = 0
    n_actioned = 0
    for row in rows:
        impl = normalized_implementation_status(row.get("implementation_status"))
        if impl == "archived":
            n_archived += 1
            continue
        if impl == "actioned":
            n_actioned += 1
            continue
        kept.append(row)
    return kept, n_archived, n_actioned


def score_key(row: dict[str, str]) -> tuple[int, float, str]:
    tier_s = (row.get("priority_tier") or "9").strip()
    try:
        tier = int(float(tier_s))
    except ValueError:
        tier = 9
    sc_s = (row.get("score") or "0").strip()
    try:
        sc = float(sc_s)
    except ValueError:
        sc = 0.0
    title = (row.get("title") or "").strip().lower()
    return (tier, -sc, title)


def update_inferred_doc_paths(rows: list[dict[str, str]], root: Path) -> int:
    """
    Set `doc_path` when conflict text, IA remaps, or topic routing resolve to an on-disk `_docs/...` file.
    Includes rows with `conflict_resolution` = `inconclusive`.
    """
    updated = 0
    for row in rows:
        existing = (row.get("doc_path") or "").strip()
        if existing and resolve_existing_path(existing, root):
            continue
        rel, _, note = resolved_primary_doc(
            row.get("doc_path"),
            row.get("codebase_evidence"),
            row.get("suggested_change"),
            root,
            conflict=row.get("conflict"),
            allow_context_inference=True,
            row_for_context=row,
        )
        if not rel:
            continue
        if rel == existing:
            continue
        row["doc_path"] = rel
        footnote = f"Phase 1 inferred doc_path ({note or 'resolved'})."
        prev_notes = (row.get("notes") or "").strip()
        row["notes"] = f"{prev_notes} | {footnote}".strip(" |") if prev_notes else footnote
        updated += 1
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 1 KB markdown; optional CSV prune / doc_path infer.")
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help="Skip CSV prune; only regenerate markdown.",
    )
    parser.add_argument(
        "--infer-doc-paths",
        action="store_true",
        help="Infer and write doc_path (remaps + best-fit).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    fieldnames, rows = load_csv_rows(CSV_PATH)
    if not args.no_prune:
        rows, n_archived, n_actioned = prune_dispositioned_rows(rows)
        removed = n_archived + n_actioned
        if removed:
            write_csv_rows(CSV_PATH, fieldnames, rows)
            print(
                f"Pruned {removed} ({CSV_PATH.relative_to(REPO_ROOT)}): archived={n_archived}, "
                f"actioned={n_actioned}; {len(rows)} left."
            )
    if args.infer_doc_paths:
        n_infer = update_inferred_doc_paths(rows, REPO_ROOT)
        write_csv_rows(CSV_PATH, fieldnames, rows)
        print(f"Inferred doc_path on {n_infer} row(s) ({CSV_PATH.relative_to(REPO_ROOT)}).")
    classified: list[RowOut] = [classify_row(r, REPO_ROOT) for r in rows]

    skipped = [c for c in classified if c.skip_reason]
    actionable = [c for c in classified if not c.skip_reason]

    skipped.sort(key=lambda c: (c.skip_reason or "", article_id_from_row(c.row)))
    actionable.sort(key=lambda c: score_key(c.row))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # --- skipped.md ---
    by_reason: dict[str, list[RowOut]] = defaultdict(list)
    for c in skipped:
        by_reason[c.skip_reason or "unknown"].append(c)

    def abbrev_reason(s: str, max_len: int = 100) -> str:
        t = s.strip()
        if len(t) <= max_len:
            return t
        return t[: max_len - 1] + "…"

    top_buckets = sorted(by_reason.items(), key=lambda kv: -len(kv[1]))[:8]
    bucket_lines: list[str] = [
        "**Largest skip buckets** (each bullet matches a `##` section below):",
        "",
    ]
    for reason, items in top_buckets:
        bucket_lines.append(f"- **{len(items)}** — {abbrev_reason(reason)}")
    bucket_lines.append("")

    skip_lines: list[str] = [
        "# KB articles — Phase 1 skipped rows",
        "",
        f"Generated from `{CSV_PATH.relative_to(REPO_ROOT)}` on **{now}**.",
        "",
        "**Do not hand-edit this file** — it is overwritten by `python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py` "
        f"(repo root). Update the CSV, then re-run that script; the companion `{ACTIONED_OUT.relative_to(REPO_ROOT)}` "
        "file is refreshed in the same run.",
        "",
        "Rows listed here **did not** pass Phase 1 gates (see `.github/skills/salesforce-migration/SKILL.md`). "
        f"Actionable queue: `{ACTIONED_OUT.relative_to(REPO_ROOT)}`.",
        "",
        f"**Totals:** {len(rows)} CSV rows — **{len(actionable)} actionable**, **{len(skipped)} skipped**.",
        "",
    ]
    skip_lines.extend(bucket_lines)
    for reason in sorted(by_reason.keys(), key=lambda s: (-len(by_reason[s]), s)):
        items = by_reason[reason]
        skip_lines.append(f"## {reason}")
        skip_lines.append("")
        skip_lines.append(f"**Count:** {len(items)}")
        skip_lines.append("")
        for c in sorted(items, key=lambda x: article_id_from_row(x.row)):
            rid = article_id_from_row(c.row)
            ttl = (c.row.get("title") or "").strip()
            skip_lines.append(f"- **`{rid}`** — {ttl}")
            detail = (c.skip_context or c.skip_reason or "").strip()
            if detail:
                skip_lines.append(f"  - *Explanation:* {detail}")
        skip_lines.append("")

    SKIPPED_OUT.parent.mkdir(parents=True, exist_ok=True)
    SKIPPED_OUT.write_text("\n".join(skip_lines).rstrip() + "\n", encoding="utf-8")

    # --- actioned.md (actionable backlog, not CSV status "Actioned") ---
    by_file: dict[str, list[RowOut]] = defaultdict(list)
    for c in actionable:
        assert c.primary_rel
        by_file[c.primary_rel].append(c)

    # One Phase 2 PR per primary doc (may include one or many articles).
    pr_batches_sorted = sorted(by_file.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from sf_kb_overlap_scan import OverlapScanner, format_scan_summary  # noqa: WPS433

    scanner = OverlapScanner(fetch_develop=False)
    scanner.refresh()
    overlap_inputs = [
        (
            path_key,
            [article_id_from_row(c.row) for c in group if article_id_from_row(c.row)],
        )
        for path_key, group in pr_batches_sorted
    ]
    overlap_reports = scanner.scan_batches(overlap_inputs) if scanner.available else {}

    # Needs-PR queue:
    # - Omit the whole batch when an open/draft PR already edits the path.
    # - When only some article_ids are claimed, keep unclaimed siblings in the queue
    #   (do not hide remaining work behind a partial claim).
    needs_pr_batches: list[tuple[str, list]] = []
    covered_batches: list[tuple[str, list]] = []
    claimed_articles_omitted = 0
    for path_key, group in pr_batches_sorted:
        report = overlap_reports.get(path_key)
        if report and report.path_covered_by_pr:
            covered_batches.append((path_key, group))
            continue
        claimed = report.claimed_article_ids() if report else set()
        if claimed:
            remaining = [
                c
                for c in group
                if (article_id_from_row(c.row) or "") not in claimed
            ]
            claimed_articles_omitted += len(group) - len(remaining)
        else:
            remaining = list(group)
        if remaining:
            needs_pr_batches.append((path_key, remaining))
        elif group:
            covered_batches.append((path_key, group))

    # Re-scan overlap for remaining article IDs so claimed-sibling hits do not
    # mark the filtered batch as blocked in the queue summary.
    if scanner.available and needs_pr_batches:
        needs_inputs = [
            (
                path_key,
                [article_id_from_row(c.row) for c in group if article_id_from_row(c.row)],
            )
            for path_key, group in needs_pr_batches
        ]
        overlap_reports = {
            **overlap_reports,
            **scanner.scan_batches(needs_inputs),
        }

    needs_pr_rows = sum(len(group) for _, group in needs_pr_batches)
    omit_note = (
        f"{len(covered_batches)} batch(es) omitted — open/draft PR on path "
        f"or all articles claimed"
    )
    if claimed_articles_omitted:
        omit_note += (
            f"; {claimed_articles_omitted} claimed article(s) dropped from "
            "multi-article batches"
        )

    act_lines = [
        "# KB articles — Phase 1 actionable backlog",
        "",
        f"Generated from `{CSV_PATH.relative_to(REPO_ROOT)}` on **{now}**.",
        "",
        "These rows passed Phase 1 and resolve to an on-disk `_docs/...` file. "
        "Work queue for Phase 2 — not CSV `actioned` status.",
        "",
        f"**Totals:** **{len(actionable)}** actionable rows (of {len(rows)}); "
        f"**{needs_pr_rows}** still need a Phase 2 PR written "
        f"({omit_note}).",
    ]
    ref_verify_n = sum(
        1
        for _, group in needs_pr_batches
        for c in group
        if c.reference_verify
    )
    if ref_verify_n:
        act_lines.append(
            f"**Reference-repo verification:** **{ref_verify_n}** row(s) have "
            "`conflict_resolution` = `inconclusive` — confirm behavior in reference repos "
            "(see `.github/skills/salesforce-migration/SKILL.md` Phase 2) before drafting; "
            "do not copy Salesforce Knowledge text without source verification."
        )
    act_lines.extend(
        [
            "",
            "## 1. Phase 2 PR batches still needing a PR (one primary `_docs` file per PR)",
            "",
            "Open **one PR per row** in the table below. Each PR edits **only** that file; "
            "multiple Salesforce Knowledge articles may land in the same PR when they share the same `doc_path`.",
            "",
            "Batches already covered by an open/draft PR editing the same path are "
            "**omitted**. Claimed `article_id`s are dropped from multi-article batches, "
            "but unclaimed siblings on that path stay in the queue.",
            "",
            "Do **not** batch PRs by product vertical — mixed verticals under one path are expected "
            "(for example, mis-routed paths). Use **Product vertical** (`Team` in "
            "`.github/support_analyzer_doc_assignees.csv`) and the same file for GitHub assignee when opening PRs manually. "
            "`sf_kb_phase2_run_batches.py` sets PR and Jira assignees when the CSV resolves to a username; otherwise the PR stays unassigned.",
            "",
            "Run `python3 scripts/salesforce-analyzer/sf_kb_overlap_scan.py` (or Phase 2 batch runner) "
            "to check for overlap with open/draft/merged PRs, claimed `article_id`s, `develop` content, "
            "and remote `sf-cursor-*` branches before opening work.",
            "",
            f"**Phase 2 batches needing a PR:** **{len(needs_pr_batches)}** "
            f"(omitted **{len(covered_batches)}** already covered).",
            "",
        ]
    )
    if not needs_pr_batches:
        act_lines.extend(
            [
                "| Primary `_docs` target | Articles | Overlap | Product vertical | Suggested branch slug | Product owner |",
                "| --- | ---: | --- | --- | --- | --- |",
                "| _none_ | 0 | | | | |",
                "",
            ]
        )
    else:
        needs_reports = {
            path_key: overlap_reports[path_key]
            for path_key, _ in needs_pr_batches
            if path_key in overlap_reports
        }
        if scanner.available:
            act_lines.append(f"**Overlap scan (queue only):** {format_scan_summary(needs_reports)}.")
            act_lines.append("")
        else:
            act_lines.append(
                f"**Overlap scan:** unavailable ({scanner.error or 'unknown error'}). "
                "Re-run `sf_kb_overlap_scan.py` before Phase 2."
            )
            act_lines.append("")

        act_lines.extend(
            [
                "| Primary `_docs` target | Articles | Overlap | Product vertical | Suggested branch slug | Product owner |",
                "| --- | ---: | --- | --- | --- | --- |",
            ]
        )
        for path_key, group in needs_pr_batches:
            hint = infer_product_vertical_label(path_key)
            slug = doc_path_branch_slug(path_key)
            overlap = overlap_reports.get(path_key)
            overlap_cell = overlap.status_label() if overlap else "unknown"
            act_lines.append(
                f"| `{path_key}` | {len(group)} | {overlap_cell} | {hint} | `sf-cursor-{slug}-<YYYYMMDD>` |  |"
            )
        act_lines.append("")
        for path_key, group in needs_pr_batches:
            slug = doc_path_branch_slug(path_key)
            overlap = overlap_reports.get(path_key)
            act_lines.append(
                f"### PR batch: `{path_key}` — **{len(group)}** article(s)"
            )
            act_lines.append("")
            act_lines.append(
                f"- **Branch example:** `sf-cursor-{slug}-<YYYYMMDD>`"
            )
            act_lines.append(
                f"- **Product vertical:** {infer_product_vertical_label(path_key)}"
            )
            if overlap and overlap.hits:
                act_lines.append("- **Overlap scan:**")
                act_lines.extend(overlap.format_lines(indent="  "))
            act_lines.append("")
            for c in sorted(group, key=lambda x: score_key(x.row)):
                r = c.row
                verify_note = (
                    "; **verify in reference repos** (`conflict_resolution`: inconclusive)"
                    if c.reference_verify
                    else ""
                )
                act_lines.append(
                    f"- **`{article_id_from_row(r)}`** — {r.get('title', '').strip()} "
                    f"(tier {r.get('priority_tier', '')}, score {r.get('score', '')}; team `{r.get('team', '')}`"
                    f"{verify_note})"
                )
            act_lines.append("")

    inferred_rows = [
        c
        for _, group in needs_pr_batches
        for c in group
        if c.path_inference
    ]
    if inferred_rows:
        act_lines.extend(
            [
                "### Scripted path inference / best-fit placement used (verify in Phase 2)",
                "",
                "These actionable rows had **no direct file hit** for the CSV `_docs/` string; the generator "
                "matched a current page via `PATH_INFERENCE_EXACT`, `PATH_INFERENCE_PREFIXES`, a **globally unique** "
                "`*.md` basename under `_docs/`, or **best-fit placement** (topic routes + keyword scoring). "
                "Confirm the mapping before merging content.",
                "",
                "| article_id | Title | Primary `_docs` target | Inference |",
                "| --- | --- | --- | --- |",
            ]
        )
        for c in sorted(inferred_rows, key=lambda x: score_key(x.row))[:45]:
            r = c.row
            ttl = (r.get("title") or "").replace("|", "\\|")
            inf = (c.path_inference or "").replace("|", "\\|").replace("`", "'")
            act_lines.append(
                f"| `{article_id_from_row(r)}` | {ttl} | `{c.primary_rel}` | {inf} |"
            )
        if len(inferred_rows) > 45:
            act_lines.append(f"| … | _({len(inferred_rows) - 45} more)_ | | |")
        act_lines.append("")

    ACTIONED_OUT.write_text("\n".join(act_lines).rstrip() + "\n", encoding="utf-8")

    inferred_n = sum(1 for c in actionable if c.path_inference)
    inf = f", {inferred_n} inferred path(s)" if inferred_n else ""
    print(
        f"Wrote {SKIPPED_OUT.relative_to(REPO_ROOT)} ({len(skipped)} skipped), "
        f"{ACTIONED_OUT.relative_to(REPO_ROOT)} ({len(actionable)} actionable, "
        f"{len(needs_pr_batches)} batch(es) need PR, {len(covered_batches)} covered/omitted{inf})"
    )


if __name__ == "__main__":
    main()
