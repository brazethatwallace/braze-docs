#!/usr/bin/env python3
"""Unit tests for markdown snippet PII scanning."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from check_snippet_pii import (
    check_markdown_file,
    emit_github_annotations,
    iter_fenced_blocks,
    resolve_cli_doc_path,
)
from pii_text_scan import scan_snippet_text


class FencedBlockTests(unittest.TestCase):
    def test_extracts_backtick_fence_with_info(self) -> None:
        md = '# Title\n\n```json\n{"email": "a@b.com"}\n```\n'
        blocks = iter_fenced_blocks(md)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].info, 'json')
        self.assertIn('email', blocks[0].body)
        self.assertEqual(blocks[0].start_line, 4)

    def test_extracts_tilde_fence(self) -> None:
        md = '~~~\nline one\nline two\n~~~\n'
        blocks = iter_fenced_blocks(md)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].body, 'line one\nline two')

    def test_skips_unclosed_fence(self) -> None:
        md = '```\nno closing fence'
        self.assertEqual(iter_fenced_blocks(md), [])


class ScanSnippetTextTests(unittest.TestCase):
    def test_flags_real_email_in_json(self) -> None:
        text = '{"email": "wallace.lee@braze.com"}'
        violations = scan_snippet_text('_docs/example.md', text, line_start=10)
        self.assertTrue(any(v.violation_type == 'email_address' for v in violations))
        self.assertEqual(violations[0].line_start, 10)

    def test_allows_example_email(self) -> None:
        text = '{"email": "alex@example.com"}'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.violation_type == 'email_address' for v in violations))

    def test_skips_alphanumeric_external_id_in_snippets(self) -> None:
        text = '{"external_id": "a82415", "name": "sample"}'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(
            any(v.violation_type == 'alphanumeric_external_id' for v in violations)
        )

    def test_skips_numeric_ids_when_placeholders_present(self) -> None:
        text = (
            'curl -H "Authorization: Bearer YOUR_REST_API_KEY" '
            '-d \'{"external_id": "42004428"}\''
        )
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.violation_type == 'numeric_user_id' for v in violations))

    def test_flags_many_numeric_ids_without_placeholders(self) -> None:
        text = (
            '{"users": [{"external_id": "42004428"}, {"external_id": "42004430"}, '
            '{"external_id": "42004437"}, {"external_id": "42004499"}]}'
        )
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertTrue(any(v.violation_type == 'numeric_user_id' for v in violations))

    def test_skips_git_ssh_urls(self) -> None:
        text = 'git clone git@github.com:braze-inc/braze-unity-sdk.git'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.violation_type == 'email_address' for v in violations))

    def test_skips_snowflake_varchar_size(self) -> None:
        text = 'EXTERNAL_ID VARCHAR(16777216), PAYLOAD VARCHAR(16777216) NOT NULL'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.violation_type == 'numeric_user_id' for v in violations))

    def test_skips_schema_modal_will(self) -> None:
        text = (
            '"is_suspected_bot_click": "(optional, boolean) Will only populate when '
            'Bot Filtering setting is enabled"'
        )
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.match == 'Will' for v in violations))

    def test_skips_geo_coordinates(self) -> None:
        text = '{"coordinates": [[-73.991443, 40.753824], [-74.044468, 40.689225]]}'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.violation_type == 'numeric_user_id' for v in violations))

    def test_skips_dont_contraction(self) -> None:
        text = '{"title": "Don\'t Forget to Complete Your Profile"}'
        violations = scan_snippet_text('_docs/example.md', text)
        self.assertFalse(any(v.match == 'Don' for v in violations))


class CheckMarkdownFileTests(unittest.TestCase):
    def test_scans_all_fenced_blocks_in_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / '_docs'
            docs.mkdir()
            md = docs / 'sample.md'
            md.write_text(
                'Intro\n\n```\nalex@example.com\n```\n\n```\nreal@company.org\n```\n',
                encoding='utf-8',
            )
            # check_markdown_file uses git_repo_root(); patch via cwd
            orig_cwd = Path.cwd()
            try:
                import os

                os.chdir(repo)
                (repo / '.git').mkdir()
                violations = check_markdown_file(md)
            finally:
                os.chdir(orig_cwd)
            emails = {v.match for v in violations if v.violation_type == 'email_address'}
            self.assertIn('real@company.org', emails)
            self.assertNotIn('alex@example.com', emails)


class PathResolutionTests(unittest.TestCase):
    def test_accepts_docs_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '_docs').mkdir()
            p = resolve_cli_doc_path('_docs/foo/bar.md', root)
            self.assertTrue(p.as_posix().endswith('_docs/foo/bar.md'))

    def test_rejects_lang_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                resolve_cli_doc_path('_lang/fr_fr/_docs/foo.md', root)


class EmitAnnotationsTests(unittest.TestCase):
    def test_emits_warning_for_doc_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'violations.json'
            path.write_text(
                json.dumps(
                    [
                        {
                            'dismissed': False,
                            'file': '_docs/user_guide/foo.md',
                            'line_start': 42,
                            'message': 'Code snippet may contain a real email',
                        }
                    ]
                ),
                encoding='utf-8',
            )
            rc = emit_github_annotations(str(path))
            self.assertEqual(rc, 0)


if __name__ == '__main__':
    unittest.main()
