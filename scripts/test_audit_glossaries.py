#!/usr/bin/env python3
"""
Tests for glossary audit helpers.

Run with:
    python3 -m pytest scripts/test_audit_glossaries.py -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audit_glossaries as ag  # noqa: E402


class TestStripYamlFrontMatter:
    def test_removes_leading_front_matter(self):
        text = "---\nlayout: page\nimage: /assets/foo.png\n---\n# Title\n"
        assert ag._strip_yaml_front_matter(text) == "\n# Title\n"

    def test_leaves_body_without_front_matter(self):
        text = "# Title\n\nBody **Preview** tab.\n"
        assert ag._strip_yaml_front_matter(text) == text


class TestCountBoldUiLabel:
    def test_counts_case_insensitive_bold_labels(self):
        body = "Select **Preview** tab or **preview** again.\n"
        assert ag._count_bold_ui_label("Preview", body) == 2

    def test_ignores_front_matter_and_prose(self):
        text = "---\nimage: /assets/foo.png\nlayout: page\n---\n"
        text += "The selected option is not highlighted.\n"
        body = ag._strip_yaml_front_matter(text)
        assert ag._count_bold_ui_label("Image:", body) == 0
        assert ag._count_bold_ui_label("Selected", body) == 0


class TestFindMissingTerms:
    def test_requires_bold_ui_occurrences(self, tmp_path):
        docs = tmp_path / "_docs"
        docs.mkdir()
        (docs / "sample.md").write_text(
            "---\nimage: /assets/foo.png\nlayout: page\n---\n"
            "Open the **Preview** tab.\n"
            "Another **Preview** tab here.\n"
            "Five more **Preview** mentions.\n"
            "**Preview**\n"
            "**Preview**\n"
            "**Preview**\n",
            encoding="utf-8",
        )
        source_pairs = {"Preview": "Prévisualisation"}
        missing = ag.find_missing_terms(source_pairs, {}, docs, min_occurrences=5)
        assert len(missing) == 1
        assert missing[0]["term"] == "Preview"
        assert missing[0]["frequency_in_docs"] == 6

    def test_ignores_yaml_metadata_collisions(self, tmp_path):
        docs = tmp_path / "_docs"
        docs.mkdir()
        (docs / "many.md").write_text(
            "---\nimage: /assets/foo.png\n---\n" * 20,
            encoding="utf-8",
        )
        source_pairs = {"Image:": "Bild:"}
        missing = ag.find_missing_terms(source_pairs, {}, docs, min_occurrences=5)
        assert missing == []


class TestSourceLikelyUntranslated:
    def test_flags_english_source_string(self):
        assert ag._source_likely_untranslated("클릭", "click", "Click")

    def test_flags_ascii_downgrade(self):
        assert ag._source_likely_untranslated("기기", "device", "Device")

    def test_does_not_flag_real_translation_drift(self):
        assert not ag._source_likely_untranslated("prévia", "Preview", "Pré-visualização")
