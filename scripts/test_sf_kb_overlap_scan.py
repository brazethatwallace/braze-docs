#!/usr/bin/env python3
"""Unit tests for Salesforce KB overlap scanning."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "salesforce-analyzer"))

from sf_kb_overlap_scan import (  # noqa: E402
    PHASE2_MARKER,
    BatchOverlapReport,
    OverlapScanner,
    PrRef,
    merged_within_lookback,
)


class OverlapScanTests(unittest.TestCase):
    def test_merged_within_lookback_recent(self) -> None:
        pr = PrRef(
            number=1,
            state="merged",
            is_draft=False,
            title="t",
            url="u",
            labels=(),
            merged_at="2026-07-01T00:00:00Z",
        )
        self.assertTrue(merged_within_lookback(pr, days=180))

    def test_blocked_on_open_pr_and_develop_marker(self) -> None:
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        open_pr = PrRef(10, "open", False, "Open batch", "url", ())
        scanner._path_prs = {"_docs/_user_guide/foo.md": [open_pr]}  # noqa: SLF001
        scanner._article_prs = {}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value=f"intro\n{PHASE2_MARKER}\n"):
            report = scanner.check_batch(
                "_docs/_user_guide/foo.md",
                ["ka123"],
            )

        self.assertTrue(report.blocked)
        kinds = {hit.kind for hit in report.hits}
        self.assertIn("open_pr", kinds)
        self.assertIn("develop_marker", kinds)

    def test_article_id_claim_blocks(self) -> None:
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        merged_pr = PrRef(20, "merged", False, "Done", "url", ("salesforce migration",))
        scanner._path_prs = {}  # noqa: SLF001
        scanner._article_prs = {"ka999": [merged_pr]}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value="clean"):
            with patch.object(scanner, "_recent_develop_sf_commits", return_value=[]):
                with patch.object(scanner, "_remote_sf_branches", return_value=[]):
                    report = scanner.check_batch("_docs/_user_guide/bar.md", ["ka999"])

        self.assertTrue(report.blocked)
        self.assertEqual(report.hits[0].kind, "article_id")

    def test_warning_only_for_recent_merged_path(self) -> None:
        scanner = OverlapScanner(fetch_develop=False)
        scanner._loaded = True  # noqa: SLF001
        merged_pr = PrRef(
            30,
            "merged",
            False,
            "Merged",
            "url",
            (),
            merged_at="2026-07-01T00:00:00Z",
        )
        scanner._path_prs = {"_docs/_user_guide/baz.md": [merged_pr]}  # noqa: SLF001
        scanner._article_prs = {}  # noqa: SLF001

        with patch.object(scanner, "_develop_text_for", return_value="clean"):
            with patch.object(scanner, "_recent_develop_sf_commits", return_value=[]):
                with patch.object(scanner, "_remote_sf_branches", return_value=[]):
                    report = scanner.check_batch("_docs/_user_guide/baz.md", ["ka111"])

        self.assertFalse(report.blocked)
        self.assertEqual(report.status_label(), "warning")
        self.assertEqual(report.hits[0].kind, "merged_pr")

    def test_status_label_clear(self) -> None:
        report = BatchOverlapReport(doc_path="_docs/x.md", article_ids=("ka1",))
        self.assertEqual(report.status_label(), "clear")

    def test_load_pr_index_uses_bulk_pr_bodies(self) -> None:
        scanner = OverlapScanner(fetch_develop=False)
        open_raw = {
            "number": 1,
            "title": "Open",
            "url": "u",
            "isDraft": False,
            "labels": [],
            "files": [],
            "state": "OPEN",
            "mergedAt": None,
            "body": "Claims `ka-open` in body",
        }
        merged_raw = {
            "number": 2,
            "title": "Merged SF",
            "url": "u2",
            "isDraft": False,
            "labels": [{"name": "salesforce migration"}],
            "files": [],
            "state": "MERGED",
            "mergedAt": "2026-07-01T00:00:00Z",
            "body": "Also claims `ka-merged`",
        }

        def fake_list(state: str, *, limit: int) -> list[dict]:
            if state == "open":
                return [open_raw]
            return [merged_raw]

        gh_calls: list[list[str]] = []

        def fake_gh_json(args: list[str]) -> object:
            gh_calls.append(args)
            return []

        scanner.gh_json = fake_gh_json  # type: ignore[method-assign]
        with patch.object(scanner, "_list_prs", side_effect=fake_list):
            scanner._load_pr_index()  # noqa: SLF001

        self.assertEqual(
            [args for args in gh_calls if args[:3] == ["pr", "view"]],
            [],
        )
        self.assertIn("ka-open", scanner._article_prs)  # noqa: SLF001
        self.assertIn("ka-merged", scanner._article_prs)  # noqa: SLF001


if __name__ == "__main__":
    unittest.main()
