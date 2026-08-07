#!/usr/bin/env python3
"""Unit tests for SF KB Phase 2 --verify-only behavior."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock
from unittest.mock import patch

SALESFORCE_ANALYZER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SALESFORCE_ANALYZER_DIR))

from sf_kb_phase2_run_batches import verify_batch  # noqa: E402


class VerifyOnlyBatchTests(unittest.TestCase):
    def test_empty_actionable_returns_skip_not_fail(self) -> None:
        rows = [
            {
                "title": "Internal note",
                "suggested_change": "",
                "conflict_resolution": "codebase confirms knowledge",
            }
        ]
        outcome = verify_batch(
            "_docs/_user_guide/foo.md",
            rows,
            verification_lines=[],
            require_verification=True,
            pull_repos=False,
            write_verification=False,
            dry_run=True,
        )
        self.assertEqual(outcome, "skip")

    def test_verify_only_ignores_overlap_scan(self) -> None:
        rows = [
            {
                "article_id": "kaTEST",
                "title": "Delayed send alerts",
                "suggested_change": "### Who receives the alert?\n\nWorkspace admins.",
                "conflict_resolution": "codebase confirms knowledge",
                "target": "docs",
            }
        ]
        with patch(
            "sf_kb_phase2_run_batches.run_reference_verification",
            return_value=([], True),
        ):
            with patch(
                "sf_kb_phase2_run_batches.batch_context",
                return_value=None,
            ) as mock_ctx:
                outcome = verify_batch(
                    "_docs/_user_guide/messaging/canvas/faqs.md",
                    rows,
                    verification_lines=[],
                    require_verification=True,
                    pull_repos=False,
                    write_verification=False,
                    dry_run=True,
                )
        mock_ctx.assert_not_called()
        self.assertEqual(outcome, "ok")

    def test_incomplete_proof_returns_fail(self) -> None:
        rows = [
            {
                "article_id": "kaTEST",
                "title": "Multi-page IAM backgrounds",
                "suggested_change": "### Can backgrounds span pages?\n\nYes.",
                "conflict_resolution": "inconclusive",
                "target": "docs",
            }
        ]
        with patch(
            "sf_kb_phase2_run_batches.run_reference_verification",
            return_value=([], True),
        ):
            outcome = verify_batch(
                "_docs/_user_guide/channels/in_app_messages/faq.md",
                rows,
                verification_lines=[],
                require_verification=True,
                pull_repos=False,
                write_verification=False,
                dry_run=True,
            )
        self.assertEqual(outcome, "fail")

    def test_manual_proof_without_codebase_evidence_passes_reference_gate(self) -> None:
        from sf_kb_phase2_run_batches import run_reference_verification

        rows = [
            {
                "article_id": "kaTEST",
                "title": "Max Devices Rule",
                "target": "docs",
                "conflict_resolution": "inconclusive",
                "codebase_evidence": "",
            }
        ]
        merged, ok = run_reference_verification(
            "_docs/_user_guide/foo.md",
            rows,
            [
                "Verified Max Devices Rule in `platform/shared_code/foo.rb`"
            ],
            require_verification=True,
            pull_repos=False,
            write_verification=False,
            dry_run=True,
        )
        self.assertTrue(ok)
        self.assertTrue(merged)

    def test_missing_cited_file_blocks_reference_gate(self) -> None:
        from sf_kb_phase2_run_batches import run_reference_verification

        rows = [
            {
                "article_id": "kaTEST",
                "title": "Example feature",
                "target": "docs",
                "conflict_resolution": "codebase confirms knowledge",
                "codebase_evidence": "platform/does/not/exist/for_sf_kb_test.rb",
            }
        ]
        with mock.patch(
            "sf_kb_reference_verify.sibling_repo_roots",
            return_value={"platform": Path("/tmp/sf-kb-platform-mock")},
        ):
            _merged, ok = run_reference_verification(
                "_docs/_user_guide/foo.md",
                rows,
                [],
                require_verification=True,
                pull_repos=False,
                write_verification=False,
                dry_run=True,
            )
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
