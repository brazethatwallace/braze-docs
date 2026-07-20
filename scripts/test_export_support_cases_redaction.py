#!/usr/bin/env python3
"""Unit tests for Looker export credential redaction via `_data/pii_patterns.yml`."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from export_support_cases_from_looker import (
    _load_secret_redactions,
    _redact_embedded_secrets,
)

# Synthetic fixtures shaped like credential formats GitHub push protection scans.
# Values are fictional and must not be real secrets.
_SAMPLES: list[tuple[str, str]] = [
    ("AKIAIOSFODNN7EXAMPLE", "[REDACTED_AWS_ACCESS_KEY_ID]"),
    (
        "SG.abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ123456",
        "[REDACTED_SENDGRID_API_KEY]",
    ),
    ("ghp_" + ("A" * 36), "[REDACTED_GITHUB_TOKEN]"),
    ("github_pat_" + ("B" * 82), "[REDACTED_GITHUB_TOKEN]"),
    ("gho_" + ("C" * 36), "[REDACTED_GITHUB_TOKEN]"),
    ("ghu_" + ("D" * 36), "[REDACTED_GITHUB_TOKEN]"),
    ("ghs_" + ("E" * 36), "[REDACTED_GITHUB_TOKEN]"),
    ("ghr_" + ("F" * 36), "[REDACTED_GITHUB_TOKEN]"),
    ("xoxb-1234567890-abcdefghij", "[REDACTED_SLACK_TOKEN]"),
    ("sk_live_" + ("G" * 24), "[REDACTED_STRIPE_KEY]"),
    ("rk_test_" + ("H" * 24), "[REDACTED_STRIPE_KEY]"),
    ("AC" + ("a" * 32), "[REDACTED_TWILIO_ACCOUNT_SID]"),
    ("SK" + ("b" * 32), "[REDACTED_TWILIO_API_KEY_SID]"),
]


class LoadPiiPatternsTests(unittest.TestCase):
    def tearDown(self) -> None:
        _load_secret_redactions.cache_clear()

    def test_loads_default_yaml_with_all_known_replacements(self) -> None:
        redactions = _load_secret_redactions()
        # 12 YAML entries; Stripe live/test keys share one pattern (covered in _SAMPLES).
        self.assertEqual(len(redactions), 12)
        replacements = {replacement for _, replacement in redactions}
        expected = {replacement for _, replacement in _SAMPLES}
        self.assertTrue(expected.issubset(replacements))

    def test_rejects_empty_patterns_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.yml"
            path.write_text("version: 1\npatterns: []\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                _load_secret_redactions(str(path))

    def test_rejects_malformed_yaml_as_value_error(self) -> None:
        """Malformed YAML must surface as ValueError (caught by main), not YAMLError."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.yml"
            path.write_text("patterns:\n  - id: broken\n    pattern: [\n", encoding="utf-8")
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("Invalid YAML", str(ctx.exception))

    def test_yaml_only_new_pattern_requires_no_python_change(self) -> None:
        """Acceptance: adding a pattern in YAML alone is enough."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pii_patterns.yml"
            path.write_text(
                "version: 1\n"
                "patterns:\n"
                "  - id: demo_token\n"
                "    pattern: '\\bDEMO_[A-Z0-9]{8}\\b'\n"
                "    replacement: '[REDACTED_DEMO]'\n",
                encoding="utf-8",
            )
            text, count = _redact_embedded_secrets(
                "prefix DEMO_ABCD1234 suffix",
                patterns_path=str(path),
            )
            self.assertEqual(count, 1)
            self.assertEqual(text, "prefix [REDACTED_DEMO] suffix")


class RedactEmbeddedSecretsTests(unittest.TestCase):
    def tearDown(self) -> None:
        _load_secret_redactions.cache_clear()

    def test_redacts_each_known_pattern_type(self) -> None:
        for sample, replacement in _SAMPLES:
            with self.subTest(sample=sample[:12]):
                text, count = _redact_embedded_secrets(f"case text {sample} trailing")
                self.assertEqual(count, 1)
                self.assertIn(replacement, text)
                self.assertNotIn(sample, text)

    def test_sendgrid_key_with_csv_trailing_punctuation(self) -> None:
        # Trailing word boundary intentionally omitted for CSV punctuation.
        key = "SG.abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
        text, count = _redact_embedded_secrets(f'"{key}",next')
        self.assertEqual(count, 1)
        self.assertIn("[REDACTED_SENDGRID_API_KEY]", text)
        self.assertNotIn("SG.", text)

    def test_counts_multiple_replacements(self) -> None:
        aws = "AKIAIOSFODNN7EXAMPLE"
        slack = "xoxb-1234567890-abcdefghij"
        text, count = _redact_embedded_secrets(f"{aws} and {slack}")
        self.assertEqual(count, 2)
        self.assertIn("[REDACTED_AWS_ACCESS_KEY_ID]", text)
        self.assertIn("[REDACTED_SLACK_TOKEN]", text)

    def test_leaves_benign_text_unchanged(self) -> None:
        original = "Customer asked about Canvas entry rules and email frequency capping."
        text, count = _redact_embedded_secrets(original)
        self.assertEqual(count, 0)
        self.assertEqual(text, original)


if __name__ == "__main__":
    unittest.main()
