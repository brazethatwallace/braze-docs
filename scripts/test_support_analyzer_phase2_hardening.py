#!/usr/bin/env python3
"""Unit tests for Phase 2 path allowlisting and open-PR dedup fail-closed behavior."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path
from unittest import mock

from support_analyzer_phase2 import (
    _open_phase2_pr_for_rule,
    _validate_docs_relative_path,
    _validate_rule_edit_paths,
)
from validate_support_analyzer_phase2_rules import validate_rules_doc


_REPO_ROOT = Path(__file__).resolve().parent.parent


class DocsPathAllowlistTests(unittest.TestCase):
    def test_accepts_docs_path(self) -> None:
        self.assertEqual(
            _validate_docs_relative_path(
                "_docs/foo/bar.md", context="test"
            ),
            "_docs/foo/bar.md",
        )

    def test_rejects_outside_docs(self) -> None:
        with self.assertRaises(SystemExit):
            _validate_docs_relative_path("scripts/foo.py", context="test")

    def test_rejects_traversal(self) -> None:
        with self.assertRaises(SystemExit):
            _validate_docs_relative_path("_docs/../secrets.txt", context="test")

    def test_validate_rule_edit_paths_checks_cross_refs(self) -> None:
        rule = {
            "edits": [
                {
                    "file": "_docs/a.md",
                    "skip_if_contains_in_files": [{"file": "scripts/evil.py"}],
                }
            ]
        }
        with self.assertRaises(SystemExit):
            _validate_rule_edit_paths(rule, "test_rule")


class ValidateRulesDocTests(unittest.TestCase):
    def test_flags_invalid_match_mode(self) -> None:
        rules = [
            {
                "id": "bad_mode",
                "case_text": {
                    "fields": ["Support Cases Description"],
                    "patterns": ["(?i)test"],
                    "match_mode": "xor",
                },
                "edits": [
                    {
                        "file": "_docs/_api/foo.md",
                        "anchor_substring": "anchor",
                        "insert": "text",
                    }
                ],
            }
        ]
        errors = validate_rules_doc(root=_REPO_ROOT, rules=rules)
        self.assertTrue(any("match_mode" in e for e in errors))

    def test_flags_missing_anchor_in_file(self) -> None:
        rules = [
            {
                "id": "missing_anchor",
                "case_text": {
                    "fields": ["Support Cases Description"],
                    "patterns": ["(?i)test"],
                },
                "edits": [
                    {
                        "file": "_docs/_api/endpoints/export/campaigns/get_campaign_analytics.md",
                        "anchor_substring": "__no_such_anchor__",
                        "insert": "text",
                    }
                ],
            }
        ]
        errors = validate_rules_doc(root=_REPO_ROOT, rules=rules)
        self.assertTrue(any("anchor_substring not found" in e for e in errors))


class OpenPrDedupFailClosedTests(unittest.TestCase):
    def test_gh_list_failure_aborts(self) -> None:
        with mock.patch(
            "support_analyzer_phase2._run_capture",
            side_effect=subprocess.CalledProcessError(1, "gh", "", "api error"),
        ):
            with self.assertRaises(SystemExit):
                _open_phase2_pr_for_rule("liquid_rule", cwd=Path("."))

    def test_invalid_json_aborts(self) -> None:
        with mock.patch(
            "support_analyzer_phase2._run_capture",
            return_value="not-json",
        ):
            with self.assertRaises(SystemExit):
                _open_phase2_pr_for_rule("liquid_rule", cwd=Path("."))

    def test_matching_open_pr_returns_url(self) -> None:
        payload = json.dumps(
            [
                {
                    "headRefName": "support-analyzer/phase2-liquid_rule-2026-07-27-1",
                    "url": "https://github.com/org/repo/pull/99",
                }
            ]
        )
        with mock.patch(
            "support_analyzer_phase2._run_capture",
            return_value=payload,
        ):
            url = _open_phase2_pr_for_rule("liquid_rule", cwd=Path("."))
        self.assertEqual(url, "https://github.com/org/repo/pull/99")


if __name__ == "__main__":
    unittest.main()
