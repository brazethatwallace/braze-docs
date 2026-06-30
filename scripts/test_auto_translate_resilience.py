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


class TestChunkedTranslationRouting:
    def test_pricing_path_chunks_below_max_file_kb(self):
        path = "_docs/_unlisted_docs/pricing/message_credits_gamma_0dhr.md"
        assert at._uses_chunked_translation(path, 53)

    def test_normal_doc_not_force_chunked_at_same_size(self):
        assert not at._uses_chunked_translation("_docs/_user_guide/foo.md", 53)

    def test_oversized_file_always_chunked(self):
        assert at._uses_chunked_translation("_docs/_user_guide/foo.md", 200)
