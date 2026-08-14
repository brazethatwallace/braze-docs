#!/usr/bin/env python3
"""Tests for scripts/sync_doc_page_paths.py path rules."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sync_doc_page_paths import (  # noqa: E402
    build_sync_plan,
    enumerate_repo_paths,
    is_redirect_only,
    load_config,
    path_is_eligible,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG = load_config(REPO_ROOT / "scripts" / "doc_ownership_sync_config.yml")


class PathEligibilityTests(unittest.TestCase):
    def test_includes_primary_sections(self) -> None:
        for path in (
            "_docs/_api/basics.md",
            "_docs/_user_guide/home.md",
            "_docs/_developer_guide/home.md",
            "_docs/_partners/home.md",
            "_docs/_hidden/other/support_contact.md",
            "_docs/_unlisted_docs/private_betas/example.md",
        ):
            with self.subTest(path=path):
                self.assertTrue(path_is_eligible(path, CONFIG))

    def test_excludes_archive_subtrees(self) -> None:
        for path in (
            "_docs/_unlisted_docs/archive/inbox_vision.md",
            "_docs/_hidden/archive_docs/foo.md",
        ):
            with self.subTest(path=path):
                self.assertFalse(path_is_eligible(path, CONFIG))

    def test_excludes_archive_segment(self) -> None:
        self.assertFalse(path_is_eligible("_docs/_user_guide/foo/archive/bar.md", CONFIG))

    def test_excludes_archived_layouts_segment(self) -> None:
        self.assertFalse(
            path_is_eligible("_docs/_hidden/archived_layouts/tutorial.md", CONFIG)
        )

    def test_excludes_non_included_sections(self) -> None:
        self.assertFalse(path_is_eligible("_docs/_hidden/redirects/content_cards.md", CONFIG))
        self.assertFalse(path_is_eligible("_docs/_docs_pages/contributing.md", CONFIG))


class RedirectDetectionTests(unittest.TestCase):
    def test_detects_redirect_front_matter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "redirect.md"
            path.write_text(
                "---\nlayout: redirect\nredirect_to: /docs/foo/\n---\n",
                encoding="utf-8",
            )
            self.assertTrue(is_redirect_only(path))

    def test_ignores_normal_page(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.md"
            path.write_text("---\nnav_title: Example\n---\n\nBody\n", encoding="utf-8")
            self.assertFalse(is_redirect_only(path))


class SyncPlanTests(unittest.TestCase):
    def test_inherits_parent_writer_for_new_child_path(self) -> None:
        from sync_doc_page_paths import OwnershipRow  # noqa: PLC0415
        existing = {
            "_docs/_user_guide/channels/email": OwnershipRow(
                page_path="_docs/_user_guide/channels/email",
                writer="Lydia",
                team="Email",
                github_username="lydia-xie",
            )
        }
        plan = build_sync_plan(
            repo_paths={
                "_docs/_user_guide/channels/email",
                "_docs/_user_guide/channels/email/new_page.md",
            },
            existing_rows=existing,
            config=CONFIG,
            writer_config={"Lydia": "lydia-xie"},
        )
        self.assertEqual(plan.added_paths, ["_docs/_user_guide/channels/email/new_page.md"])
        new_row = next(
            row
            for row in plan.target_rows
            if row.page_path == "_docs/_user_guide/channels/email/new_page.md"
        )
        self.assertEqual(new_row.writer, "Lydia")
        self.assertEqual(new_row.team, "Email")
        self.assertEqual(new_row.github_username, "lydia-xie")


class RepoEnumerationTests(unittest.TestCase):
    def test_enumerate_repo_paths_respects_rules(self) -> None:
        paths = enumerate_repo_paths(REPO_ROOT, CONFIG)
        self.assertIn("_docs/_hidden/other/support_contact.md", paths)
        self.assertNotIn("_docs/_hidden/archive_docs/foo.md", paths)
        self.assertTrue(all(path.startswith("_docs/") for path in paths))


if __name__ == "__main__":
    unittest.main()
