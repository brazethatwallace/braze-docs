#!/usr/bin/env python3
"""Unit tests for Salesforce KB suggested_change triage and ship-ready checks."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SALESFORCE_ANALYZER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SALESFORCE_ANALYZER_DIR))

from sf_kb_suggested_change import (  # noqa: E402
    PHASE2_BATCH_MARKER,
    is_vague_suggested_change,
    validate_ship_ready_markdown,
)


class SuggestedChangeTests(unittest.TestCase):
    def test_vague_author_briefs(self) -> None:
        self.assertTrue(is_vague_suggested_change("Add to Canvas FAQs: delayed sends"))
        self.assertTrue(is_vague_suggested_change("Ensure IAM close button behavior is documented."))
        self.assertTrue(is_vague_suggested_change("Consider adding a troubleshooting note:"))
        self.assertFalse(
            is_vague_suggested_change(
                "### Who receives the Canvas Messages Delayed 24+ Hours email?\n\n"
                "Workspace admins with the Canvas permission receive this alert."
            )
        )

    def test_ship_ready_rejects_markers_only(self) -> None:
        raw = f"{PHASE2_BATCH_MARKER}\n\nEnsure close button docs.\n\n"
        self.assertTrue(validate_ship_ready_markdown(raw))

        polished = (
            "### Can I customize the in-app message close button?\n\n"
            "Yes. Use the **Close** control in the message editor to change placement."
        )
        self.assertFalse(validate_ship_ready_markdown(polished))

        instructional = (
            "## Setup\n\n"
            "Ensure your SDK is up to date before you test in-app messages.\n\n"
            "Update your integration if you use a custom HTML template."
        )
        self.assertFalse(validate_ship_ready_markdown(instructional))


if __name__ == "__main__":
    unittest.main()
