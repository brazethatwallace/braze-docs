#!/usr/bin/env python3
"""
Tests for glossary locale propagation helpers.

Run with:
    python3 -m pytest scripts/test_glossary_locale_propagation.py -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import _glossary_locale_propagation as glp  # noqa: E402


class TestReplaceInMarkdown:
    def test_replaces_english_term_in_prose(self):
        text = "Create a Segment for your users.\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 1
        assert "セグメント" in out
        assert "Segment" not in out.split("---")[-1]

    def test_skips_code_fence(self):
        text = "```\nSegment foo\n```\nSegment in prose.\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 1
        assert "Segment foo" in out
        assert "セグメント in prose" in out

    def test_skips_extended_backtick_fence(self):
        text = (
            "`````markdown\n"
            "Partner integration with Braze.\n"
            "`````\n"
            "Partner in prose.\n"
        )
        out, n = glp.replace_in_markdown(text, "Partner", "パートナー", "ja")
        assert n == 1
        assert "Partner integration with Braze." in out
        assert "パートナー in prose." in out

    def test_skips_spaced_language_fence(self):
        text = "``` swift\nCampaign code\n```\nCampaign in prose.\n"
        out, n = glp.replace_in_markdown(text, "Campaign", "キャンペーン", "ja")
        assert n == 1
        assert "Campaign code" in out
        assert "キャンペーン in prose" in out

    def test_skips_image_buster_path(self):
        text = '{% image_buster src="/assets/img/foo/Segment_bar.png" %}\n'
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 0
        assert out == text

    def test_skips_alert_key(self):
        text = "{% alert %}{% include alert='Segment profiles first' %}{% endalert %}\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 0
        assert out == text

    def test_skips_segment_cohorts_partner(self):
        text = "Use Segment Cohorts with Braze.\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 0
        assert out == text

    def test_skips_tool_frontmatter(self):
        text = "---\ntool: Segments\n---\n"
        out, n = glp.replace_in_markdown(text, "Segments", "セグメント", "ja")
        assert n == 0
        assert "tool: Segments" in out

    def test_skips_structural_frontmatter(self):
        text = (
            "---\n"
            "search_tag: Partner\n"
            'permalink: "/docs/user_guide/content_cards/"\n'
            "link: /docs/partners/segment/\n"
            "---\n"
            "Partner integrations.\n"
        )
        out, n = glp.replace_in_markdown(text, "Partner", "パートナー", "ja")
        assert n == 1
        assert "search_tag: Partner" in out
        assert 'permalink: "/docs/user_guide/content_cards/"' in out
        assert "link: /docs/partners/segment/" in out
        assert "パートナー integrations." in out

    def test_replaces_description_frontmatter(self):
        text = "---\ndescription: Create a Segment for users.\n---\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 1
        assert "description: Create a セグメント for users." in out

    def test_preserves_relative_url_in_markdown_link(self):
        text = "[Filters](/docs/user_guide/segments/filters/) for Segment setup.\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 1
        assert "/docs/user_guide/segments/filters/" in out
        assert "セグメント setup" in out

    def test_preserves_url_when_other_term_replaced_on_same_line(self):
        text = "[Segment](/docs/user_guide/segments/filters/) and Campaign tools.\n"
        out, n = glp.replace_in_markdown(text, "Campaign", "キャンペーン", "ja")
        assert n == 1
        assert "/docs/user_guide/segments/filters/" in out
        assert "キャンペーン tools" in out

    def test_skips_segment_doc_link_for_segment_term_only(self):
        text = "See [Segment](/docs/user_guide/segments/) for Campaign setup.\n"
        out, n = glp.replace_in_markdown(text, "Campaign", "キャンペーン", "ja")
        assert n == 1
        assert "[Segment](/docs/user_guide/segments/)" in out
        assert "キャンペーン setup" in out

        out2, n2 = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n2 == 0
        assert out2 == text

    def test_replaces_prose_on_line_with_absolute_markdown_link(self):
        text = "See [docs](https://www.braze.com/docs/partner) for Campaign setup.\n"
        out, n = glp.replace_in_markdown(text, "Campaign", "キャンペーン", "ja")
        assert n == 1
        assert "https://www.braze.com/docs/partner" in out
        assert "キャンペーン setup" in out

    def test_replaces_prose_beside_bare_absolute_url(self):
        text = "Visit https://example.com/segment/page for Campaign info.\n"
        out, n = glp.replace_in_markdown(text, "Campaign", "キャンペーン", "ja")
        assert n == 1
        assert "https://example.com/segment/page" in out
        assert "キャンペーン info" in out

    def test_skips_inline_code(self):
        text = "Use the `Segment` API identifier.\n"
        out, n = glp.replace_in_markdown(text, "Segment", "セグメント", "ja")
        assert n == 0
        assert "`Segment`" in out

    def test_skips_heading_anchor_ids(self):
        text = "See {#monitoring-alerts} for monitoring details.\n"
        out, n = glp.replace_in_markdown(text, "monitoring", "監視", "ja")
        assert n == 1
        assert "{#monitoring-alerts}" in out
        assert "監視 details" in out

    def test_replace_outside_fences_skips_code_blocks(self):
        text = (
            "`````markdown\n"
            "Create this key from **Settings** > **API Keys**.\n"
            "`````\n"
            "Create this key from **Settings** > **API Keys**.\n"
        )
        out, n = glp.replace_outside_fences(
            text, "**Settings** > **API Keys**", "**設定** > **APIキー**"
        )
        assert n == 1
        assert "**Settings** > **API Keys**." in out
        assert "**設定** > **APIキー**." in out


class TestPropagationReplaceValue:
    def test_uses_primary_synonym(self):
        assert glp.propagation_replace_value("SDK or Software-Development-Kit") == "SDK"
        assert glp.propagation_replace_value("KPI or Leistungskennzahl or Leistungskennzahlen") == "KPI"

    def test_preserves_single_value(self):
        assert glp.propagation_replace_value("Kampagne") == "Kampagne"


class TestBuildLocaleChanges:
    def test_builds_added_and_updated_changes(self):
        old = {"Campaign": "キャンペーン", "contractor": "請負業者"}
        new = {"Campaign": "キャンペーン", "contractor": "業務委託先"}
        changes = glp.build_locale_changes_from_glossary_diff("ja", old, new, {"global": []})
        assert len(changes) == 2
        searches = {change["search"] for change in changes}
        assert searches == {"請負業者", "contractor"}
        assert all(change["replace"] == "業務委託先" for change in changes)

    def test_skips_excluded_terms(self):
        old = {}
        new = {"monitoring": "監視"}
        exclusions = {"global": ["monitoring"]}
        changes = glp.build_locale_changes_from_glossary_diff(
            "ja", old, new, exclusions
        )
        assert changes == []

    def test_uses_primary_synonym_for_added_terms(self):
        old = {}
        new = {"SMS": "Kurzmitteilungsdienst or SMS"}
        changes = glp.build_locale_changes_from_glossary_diff("de", old, new, {"global": []})
        assert len(changes) == 1
        assert changes[0]["replace"] == "Kurzmitteilungsdienst"


    def test_skips_duplicate_when_old_translation_equals_english_term(self):
        old = {"contractor": "contractor"}
        new = {"contractor": "業務委託先"}
        changes = glp.build_locale_changes_from_glossary_diff("ja", old, new, {"global": []})
        assert len(changes) == 1
        assert changes[0]["search"] == "contractor"
        assert changes[0]["replace"] == "業務委託先"

    def test_updated_synonym_reorder_searches_full_old_value(self):
        old = {"campaign": "campagne or Kampagne"}
        new = {"campaign": "Kampagne or campagne"}
        changes = glp.build_locale_changes_from_glossary_diff("de", old, new, {"global": []})
        translation_updates = [
            change for change in changes if change["search"] != "campaign"
        ]
        assert len(translation_updates) == 1
        assert translation_updates[0]["search"] == "campagne or Kampagne"
        assert translation_updates[0]["replace"] == "Kampagne"


class TestPropagateGlossaryChanges:
    def test_dry_run_counts_without_writing(self, tmp_path):
        lang_root = tmp_path / "_lang" / "ja" / "_docs"
        lang_root.mkdir(parents=True)
        md = lang_root / "sample.md"
        md.write_text("Hello Segment world.\n", encoding="utf-8")

        result = glp.propagate_glossary_changes(
            [{
                "lang": "ja",
                "term": "Segment",
                "kind": "added",
                "search": "Segment",
                "replace": "セグメント",
            }],
            repo_root=tmp_path,
            dry_run=True,
        )
        assert result["files_changed"] == 1
        assert result["replacements"] == 1
        assert md.read_text(encoding="utf-8") == "Hello Segment world.\n"

    def test_writes_locale_file(self, tmp_path):
        lang_root = tmp_path / "_lang" / "ja" / "_docs"
        lang_root.mkdir(parents=True)
        md = lang_root / "sample.md"
        md.write_text("Hello Segment world.\n", encoding="utf-8")

        result = glp.propagate_glossary_changes(
            [{
                "lang": "ja",
                "term": "Segment",
                "kind": "added",
                "search": "Segment",
                "replace": "セグメント",
            }],
            repo_root=tmp_path,
        )
        assert result["files_changed"] == 1
        assert "セグメント" in md.read_text(encoding="utf-8")

    def test_skips_api_reference_files(self, tmp_path):
        user_guide = tmp_path / "_lang" / "de" / "_user_guide" / "sample.md"
        api_doc = tmp_path / "_lang" / "de" / "_api" / "endpoints" / "sample.md"
        user_guide.parent.mkdir(parents=True)
        api_doc.parent.mkdir(parents=True)
        text = "Use the SDK for integration.\n"
        user_guide.write_text(text, encoding="utf-8")
        api_doc.write_text(text, encoding="utf-8")

        result = glp.propagate_glossary_changes(
            [{
                "lang": "de",
                "term": "SDK",
                "kind": "added",
                "search": "SDK",
                "replace": "Software Development Kit",
            }],
            repo_root=tmp_path,
        )
        assert result["files_changed"] == 1
        assert "Software Development Kit" in user_guide.read_text(encoding="utf-8")
        assert api_doc.read_text(encoding="utf-8") == text


class TestRepairGlossaryPropagationCorruption:
    def test_noun_restoration_skips_oder_registrieren(self):
        import repair_glossary_propagation_corruption as repair  # noqa: WPS433

        text = "melden Sie sich an oder registrieren Sie sich.\n"
        repaired, count = repair.apply_phrase_repairs(text)
        assert repaired == text
        assert count == 0

    def test_noun_restoration_fixes_der_registrieren_phrase(self):
        import repair_glossary_propagation_corruption as repair  # noqa: WPS433

        text = "nach der registrieren einer App\n"
        repaired, count = repair.apply_phrase_repairs(text)
        assert repaired == "nach der Registrierung einer App\n"
        assert count == 1

    def test_click_corruption_repairs_javascript_literals(self):
        import repair_glossary_propagation_corruption as repair  # noqa: WPS433

        text = (
            "$('#x').click(function() {});\n"
            "$('#y').on('click', function() {});\n"
            "document.getElementById('z').addEventListener('click', function () {});\n"
        )
        corrupted = text.replace("click", "Klick, der")
        repaired, count = repair.apply_click_corruption_repairs(corrupted)
        assert repaired == text
        assert count > 0

    def test_inclusive_marker_repairs_manager_doubling(self):
        import repair_glossary_propagation_corruption as repair  # noqa: WPS433

        text = 'Kontaktieren Sie Ihre:n Braze Account Manager:in:in.\n'
        repaired, count = repair.apply_inclusive_marker_repairs(text)
        assert repaired == 'Kontaktieren Sie Ihre:n Braze Account Manager:in.\n'
        assert count == 1

    def test_phrase_repairs_restore_support_form_literals(self):
        import repair_glossary_propagation_corruption as repair  # noqa: WPS433

        text = (
            "'angepasste Attribute' : {}\n"
            'document.Cookie = "x";\n'
            '"Token": "abc"\n'
        )
        repaired, count = repair.apply_phrase_repairs(text)
        assert "'Custom Attributes' :" in repaired
        assert "document.cookie" in repaired
        assert '"token":' in repaired
        assert count > 0
