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

from sf_kb_phase2_run_batches import (  # noqa: E402
    _topic_bucket,
    batch_context,
    find_topic_mismatch_rows,
    filter_claimed_siblings,
    verify_batch,
)
from sf_kb_overlap_scan import BatchOverlapReport, OverlapHit, OverlapScanner, PrRef  # noqa: E402


def _actionable_row(article_id: str, title: str) -> dict[str, str]:
    return {
        "article_id": article_id,
        "title": title,
        "suggested_change": f"### {title}?\n\nAnswer for {title}.",
        "conflict_resolution": "codebase confirms knowledge",
        "target": "docs",
    }


class FilterClaimedSiblingsTests(unittest.TestCase):
    def test_drops_only_claimed_ids(self) -> None:
        rows = [
            _actionable_row("ka-claimed", "Claimed"),
            _actionable_row("ka-sibling", "Sibling"),
        ]
        report = BatchOverlapReport(
            doc_path="_docs/_user_guide/foo.md",
            article_ids=("ka-claimed", "ka-sibling"),
            hits=[
                OverlapHit(
                    kind="article_id",
                    message="`ka-claimed` already claimed in a PR body",
                    blocking=True,
                ),
            ],
        )
        remaining, claimed = filter_claimed_siblings(
            rows, id_column="article_id", overlap=report
        )
        self.assertEqual([r["article_id"] for r in remaining], ["ka-sibling"])
        self.assertEqual([r["article_id"] for r in claimed], ["ka-claimed"])


class BatchContextPartialClaimTests(unittest.TestCase):
    def test_partial_claim_keeps_unclaimed_siblings(self) -> None:
        rows = [
            _actionable_row("ka-claimed", "Claimed"),
            _actionable_row("ka-sibling", "Sibling"),
        ]
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        claimed_pr = PrRef(20, "merged", False, "Done", "url", ("salesforce migration",))
        scanner._path_prs = {}  # noqa: SLF001
        scanner._article_prs = {"ka-claimed": [claimed_pr]}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value="clean"):
            with patch.object(scanner, "_recent_develop_sf_commits", return_value=[]):
                with patch.object(scanner, "_remote_sf_branches", return_value=[]):
                    with patch(
                        "sf_kb_phase2_run_batches.assignees_for_doc_path",
                        return_value=[],
                    ):
                        ctx = batch_context(
                            "_docs/_user_guide/foo.md",
                            rows,
                            id_column="article_id",
                            scanner=scanner,
                            ignore_warnings=True,
                            allow_topic_mismatch=False,
                        )

        self.assertIsNotNone(ctx)
        assert ctx is not None
        self.assertEqual([aid for aid, _ in ctx["articles"]], ["ka-sibling"])
        self.assertEqual(
            [(aid, reason) for aid, _title, reason in ctx["skipped"]],
            [("ka-claimed", "already claimed in a PR body")],
        )

    def test_path_open_pr_still_blocks_whole_batch(self) -> None:
        rows = [
            _actionable_row("ka-a", "A"),
            _actionable_row("ka-b", "B"),
        ]
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        open_pr = PrRef(10, "open", False, "Open batch", "url", ())
        scanner._path_prs = {"_docs/_user_guide/foo.md": [open_pr]}  # noqa: SLF001
        scanner._article_prs = {}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value="clean"):
            with patch.object(scanner, "_recent_develop_sf_commits", return_value=[]):
                with patch.object(scanner, "_remote_sf_branches", return_value=[]):
                    ctx = batch_context(
                        "_docs/_user_guide/foo.md",
                        rows,
                        id_column="article_id",
                        scanner=scanner,
                        ignore_warnings=True,
                        allow_topic_mismatch=False,
                    )

        self.assertIsNone(ctx)


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


class TopicMismatchGuardTests(unittest.TestCase):
    def test_topic_bucket_normalizes_md_stems(self) -> None:
        self.assertEqual(
            _topic_bucket("_docs/_developer_guide/sdk_integration.md"),
            _topic_bucket("_docs/_developer_guide/sdk_integration/google_tag_manager.md"),
        )

    def test_find_topic_mismatch_rows_blocks_cross_area_batch(self) -> None:
        row = _actionable_row("ka-cross", "Retake Braze Certification Exam")
        with patch(
            "sf_kb_phase2_run_batches.infer_best_doc_path",
            return_value=(
                "_docs/_user_guide/administer/personal/braze_certification.md",
                "best-fit doc (topic score)",
            ),
        ):
            mismatches = find_topic_mismatch_rows(
                "_docs/_user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq.md",
                [row],
            )
        self.assertEqual(len(mismatches), 1)
        aid, _title, inferred, _note = mismatches[0]
        self.assertEqual(aid, "ka-cross")
        self.assertEqual(
            inferred,
            "_docs/_user_guide/administer/personal/braze_certification.md",
        )

    def test_topic_mismatch_override_allows_batch_context(self) -> None:
        rows = [_actionable_row("ka-cross", "Certification retake")]
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        scanner._path_prs = {}  # noqa: SLF001
        scanner._article_prs = {}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value="clean"):
            with patch.object(scanner, "_recent_develop_sf_commits", return_value=[]):
                with patch.object(scanner, "_remote_sf_branches", return_value=[]):
                    with patch(
                        "sf_kb_phase2_run_batches.assignees_for_doc_path",
                        return_value=[],
                    ):
                        with patch(
                            "sf_kb_phase2_run_batches.find_topic_mismatch_rows",
                            return_value=[
                                (
                                    "ka-cross",
                                    "Certification retake",
                                    "_docs/_user_guide/administer/personal/braze_certification.md",
                                    "best-fit mismatch",
                                )
                            ],
                        ):
                            blocked = batch_context(
                                "_docs/_user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq.md",
                                rows,
                                id_column="article_id",
                                scanner=scanner,
                                ignore_warnings=True,
                                allow_topic_mismatch=False,
                            )
                            allowed = batch_context(
                                "_docs/_user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq.md",
                                rows,
                                id_column="article_id",
                                scanner=scanner,
                                ignore_warnings=True,
                                allow_topic_mismatch=True,
                            )

        self.assertIsNone(blocked)
        self.assertIsNotNone(allowed)


if __name__ == "__main__":
    unittest.main()
