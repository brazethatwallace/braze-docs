#!/usr/bin/env python3
"""Unit tests for Salesforce KB GitHub PR body helpers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SALESFORCE_ANALYZER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SALESFORCE_ANALYZER_DIR))

from sf_kb_jira_ticket import (  # noqa: E402
    build_sf_kb_github_pr_body,
    build_verification_section_lines,
    pending_verification_titles,
)


class SfKbPrBodyTests(unittest.TestCase):
    def test_verification_includes_explicit_and_csv_proof(self) -> None:
        rows = [
            {
                "article_id": "ka0VP000000JgA1YAK",
                "title": "Delayed send alerts",
                "target": "docs",
                "conflict": "inconclusive",
                "codebase_evidence": "platform/shared_code/domains/messaging_pipeline/public/braze/msg_pipeline/rate_limit_mailer.rb",
            }
        ]
        lines = build_verification_section_lines(
            rows,
            verification_lines=[
                "Verified delayed-send email recipients in `platform/shared_code/domains/messaging_pipeline/public/braze/msg_pipeline/rate_limit_mailer.rb`"
            ],
        )
        body = "\n".join(lines)
        self.assertIn("rate_limit_mailer.rb", body)
        self.assertNotIn("Incomplete", body)

    def test_pending_inconclusive_without_proof(self) -> None:
        rows = [
            {
                "article_id": "ka0VP000000QG17YAG",
                "title": "Multi-page IAM backgrounds",
                "target": "docs",
                "conflict": "inconclusive",
            }
        ]
        self.assertEqual(
            pending_verification_titles(rows),
            ["Multi-page IAM backgrounds"],
        )

    def test_pending_inconclusive_csv_evidence_does_not_auto_clear(self) -> None:
        rows = [
            {
                "article_id": "ka0VP000000QG17YAG",
                "title": "Multi-page IAM backgrounds",
                "target": "docs",
                "conflict": "inconclusive",
                "codebase_evidence": "platform/shared_code/domains/iam/foo.rb",
            }
        ]
        self.assertEqual(
            pending_verification_titles(rows),
            ["Multi-page IAM backgrounds"],
        )
        self.assertEqual(
            pending_verification_titles(
                rows,
                verification_lines=[
                    "Verified IAM behavior in `platform/shared_code/domains/iam/foo.rb`"
                ],
            ),
            [],
        )

    def test_pr_body_has_verification_section(self) -> None:
        body = build_sf_kb_github_pr_body(
            doc_path="_docs/_user_guide/messaging/canvas/faqs.md",
            product_vertical="Canvas",
            articles=[("ka0VP000000JgA1YAK", "Delayed alerts")],
            backlog_rows=[
                {
                    "article_id": "ka0VP000000JgA1YAK",
                    "title": "Delayed alerts",
                    "target": "docs",
                    "conflict": "codebase confirms knowledge",
                }
            ],
            verification_lines=[
                "Verified alert recipients in `platform/shared_code/domains/messaging_pipeline/public/braze/msg_pipeline/rate_limit_mailer.rb`"
            ],
        )
        self.assertIn("## Verification", body)
        self.assertIn("rate_limit_mailer.rb", body)
        self.assertIn("### Contributor checklist", body)


if __name__ == "__main__":
    unittest.main()
