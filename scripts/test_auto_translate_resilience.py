#!/usr/bin/env python3
"""
Tests for auto-translate API retry and chunked-routing helpers.

Run with:
    python3 -m pytest scripts/test_auto_translate_resilience.py -v
"""

import auto_translate as at


class TestRetryableApiErrors:
    def test_internal_server_error_is_retryable(self):
        assert at._is_retryable_api_error("Internal server error")

    def test_api_error_payload_is_retryable(self):
        err = "{'type': 'error', 'error': {'type': 'api_error', 'message': 'Internal server error'}}"
        assert at._is_retryable_api_error(err)

    def test_non_transient_error_is_not_retryable(self):
        assert not at._is_retryable_api_error("YAML front matter parse error")


class TestRetryableTranslationErrors:
    def test_liquid_paired_tag_imbalance_is_retryable(self):
        err = (
            "Liquid paired-tag imbalance in "
            "_lang/fr_fr/_user_guide/data/distribution/braze_currents/"
            "event_glossary/message_engagement_events.md: api=81 endapi=80"
        )
        assert at._is_retryable_translation_error(err)

    def test_api_errors_remain_retryable(self):
        assert at._is_retryable_translation_error("Internal server error")

    def test_non_transient_translation_error_is_not_retryable(self):
        assert not at._is_retryable_translation_error(
            "YAML front matter parse error"
        )


class TestExtractErrorFiles:
    def test_matches_lang_prefixed_path(self):
        output = "Liquid error in _lang/fr_fr/_user_guide/foo/bar.md: unclosed tag"
        assert at.extract_error_files(output, "fr_fr") == [
            "_lang/fr_fr/_user_guide/foo/bar.md",
        ]

    def test_matches_collections_dir_without_lang_prefix(self):
        output = "Error reading file fr_fr/_includes/analytics/campaign_analytics.md"
        assert at.extract_error_files(output, "fr_fr") == [
            "_lang/fr_fr/_includes/analytics/campaign_analytics.md",
        ]


class TestChunkedTranslationRouting:
    def test_pricing_path_chunks_below_max_file_kb(self):
        path = "_docs/_unlisted_docs/pricing/message_credits_gamma_0dhr.md"
        assert at._uses_chunked_translation(path, 53)

    def test_normal_doc_not_force_chunked_at_same_size(self):
        assert not at._uses_chunked_translation("_docs/_user_guide/foo.md", 53)

    def test_oversized_file_always_chunked(self):
        assert at._uses_chunked_translation("_docs/_user_guide/foo.md", 200)


class TestLiquidSafeChunkSplits:
    def test_does_not_split_inside_details_block(self):
        content = (
            "---\nlayout: page\n---\n\n"
            "{% details Intro %}\n\n"
            "## Inner heading\n\n"
            "Body text.\n\n"
            "{% enddetails %}\n\n"
            "{% api %}\n## Event one\n\n"
            "Payload.\n\n"
            "{% endapi %}\n"
        )
        chunks = at.split_into_chunks(content, max_chunk_kb=1)
        assert len(chunks) >= 1
        for chunk in chunks:
            assert at._liquid_block_stack_at(chunk, len(chunk)) == []

    def test_message_engagement_chunks_have_balanced_liquid(self):
        from pathlib import Path

        path = Path(
            "_docs/_user_guide/data/distribution/braze_currents/"
            "event_glossary/message_engagement_events.md"
        )
        if not path.exists():
            return
        content = path.read_text()
        chunks = at.split_into_chunks(content)
        assert len(chunks) >= 2
        for i, chunk in enumerate(chunks):
            assert at._liquid_block_stack_at(chunk, len(chunk)) == [], (
                f"chunk {i + 1} ends with open Liquid blocks"
            )
        reassembled = "\n\n".join(c.strip() for c in chunks)
        at.validate_liquid_paired_tags(reassembled, label="reassembled")

    def test_validate_liquid_paired_tags_raises_on_imbalance(self):
        bad = "{% api %}\n## Foo\n{% enddetails %}\n"
        try:
            at.validate_liquid_paired_tags(bad)
            assert False, "expected ValueError"
        except ValueError as exc:
            assert "api=1" in str(exc)
            assert "endapi=0" in str(exc)
