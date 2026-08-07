#!/usr/bin/env python3
"""Unit tests for Salesforce KB reference-repo verification."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

SALESFORCE_ANALYZER_DIR = Path(__file__).resolve().parent
REPO_ROOT = SALESFORCE_ANALYZER_DIR.parents[1]
sys.path.insert(0, str(SALESFORCE_ANALYZER_DIR))

from sf_kb_reference_verify import (  # noqa: E402
    reference_paths_from_text,
    resolve_logical_path,
    verify_batch_references,
    verify_row_reference,
)


class SfKbReferenceVerifyTests(unittest.TestCase):
    def test_reference_paths_strip_line_suffix(self) -> None:
        text = (
            "platform/shared_code/lib/shared/braze/user_export/csv_exporter.rb "
            "MAX_USERS_TO_ALLOW_EXPORT = 500_000; "
            "platform/shared_code/spec/shared/models/foo_spec.rb:206-214"
        )
        paths = reference_paths_from_text(text)
        self.assertIn(
            "platform/shared_code/lib/shared/braze/user_export/csv_exporter.rb",
            paths,
        )
        self.assertIn("platform/shared_code/spec/shared/models/foo_spec.rb", paths)

    def test_inconclusive_without_evidence_blocks(self) -> None:
        row = {
            "article_id": "kaTEST",
            "title": "Max Devices Rule",
            "target": "docs",
            "conflict_resolution": "inconclusive",
            "codebase_evidence": "",
        }
        result = verify_row_reference(row, require_inconclusive=True)
        self.assertIsNotNone(result.blocking_reason)
        self.assertIn("no `codebase_evidence`", result.blocking_reason or "")

    def test_inconclusive_without_evidence_allows_manual_proof(self) -> None:
        row = {
            "article_id": "kaTEST",
            "title": "Max Devices Rule",
            "target": "docs",
            "conflict_resolution": "inconclusive",
            "codebase_evidence": "",
        }
        result = verify_row_reference(
            row,
            require_inconclusive=True,
            verification_lines=[
                "Verified Max Devices Rule in `platform/shared_code/foo.rb`"
            ],
        )
        self.assertIsNone(result.blocking_reason)

    def test_batch_allows_manual_proof_without_codebase_evidence(self) -> None:
        row = {
            "article_id": "kaTEST",
            "title": "Max Devices Rule",
            "target": "docs",
            "conflict_resolution": "inconclusive",
            "codebase_evidence": "",
        }
        batch = verify_batch_references(
            [row],
            require_inconclusive=True,
            verification_lines=[
                "Verified Max Devices Rule in `platform/shared_code/foo.rb`"
            ],
        )
        self.assertTrue(batch.ok)

    def test_missing_platform_path_blocks(self) -> None:
        row = {
            "article_id": "kaTEST",
            "title": "Example",
            "target": "docs",
            "conflict_resolution": "codebase confirms knowledge",
            "codebase_evidence": "platform/does/not/exist/for_sf_kb_test.rb",
        }
        with mock.patch(
            "sf_kb_reference_verify.sibling_repo_roots",
            return_value={"platform": Path("/tmp/sf-kb-platform-mock")},
        ):
            result = verify_row_reference(row, require_inconclusive=True)
        self.assertIsNotNone(result.blocking_reason)
        self.assertIn("not found on disk", result.blocking_reason or "")

    def test_braze_docs_evidence_resolves_in_repo(self) -> None:
        logical = "braze-docs/_docs/_user_guide/channels/email/faq.md"
        resolved = resolve_logical_path(logical)
        self.assertEqual(resolved.repo_label, "braze-docs")
        if (REPO_ROOT / "_docs/_user_guide/channels/email/faq.md").is_file():
            self.assertIsNotNone(resolved.filesystem_path)

    def test_batch_collects_auto_bullets_for_existing_platform_file(self) -> None:
        platform_root = REPO_ROOT.parent / "platform"
        sample = (
            platform_root
            / "shared_code/domains/messaging_pipeline/public/braze/msg_pipeline/rate_limit_mailer.rb"
        )
        if not sample.is_file():
            self.skipTest("platform sibling clone not available")

        row = {
            "article_id": "ka0VP000000JgA1YAK",
            "title": "Canvas Messages Delayed 24+ Hours",
            "target": "docs",
            "conflict_resolution": "codebase confirms knowledge",
            "codebase_evidence": (
                "platform/shared_code/domains/messaging_pipeline/public/braze/"
                "msg_pipeline/rate_limit_mailer.rb"
            ),
        }
        batch = verify_batch_references([row], require_inconclusive=True)
        self.assertTrue(batch.ok)
        self.assertTrue(batch.auto_bullets)


if __name__ == "__main__":
    unittest.main()
