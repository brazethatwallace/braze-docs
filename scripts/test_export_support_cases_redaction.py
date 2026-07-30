#!/usr/bin/env python3
"""Unit tests for Looker export credential redaction via `_data/pii_patterns.yml`."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from export_support_cases_from_looker import (
    _count_csv_data_rows,
    _load_default_secret_redactions,
    _load_secret_redactions,
    _redact_embedded_secrets,
    _redact_export_text,
    _validate_export_row_count,
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


def _write_patterns(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")


class LoadPiiPatternsTests(unittest.TestCase):
    def tearDown(self) -> None:
        _load_default_secret_redactions.cache_clear()

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
            _write_patterns(path, "version: 1\npatterns: []\n")
            with self.assertRaises(ValueError):
                _load_secret_redactions(str(path))

    def test_rejects_malformed_yaml_as_value_error(self) -> None:
        """Malformed YAML must surface as ValueError (caught by export wrapper), not YAMLError."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.yml"
            _write_patterns(path, "patterns:\n  - id: broken\n    pattern: [\n")
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("Invalid YAML", str(ctx.exception))

    def test_rejects_non_mapping_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "list.yml"
            _write_patterns(path, "- just\n- a\n- list\n")
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("expected a mapping with a `patterns` list", str(ctx.exception))

    def test_rejects_non_dict_pattern_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "entry.yml"
            _write_patterns(path, "patterns:\n  - not-a-mapping\n")
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("expected a mapping", str(ctx.exception))

    def test_rejects_missing_pattern_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nopattern.yml"
            _write_patterns(
                path,
                "patterns:\n  - id: x\n    replacement: '[REDACTED]'\n",
            )
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("pattern", str(ctx.exception))

    def test_rejects_backslash_in_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "backref.yml"
            _write_patterns(
                path,
                "patterns:\n"
                "  - id: leaky\n"
                "    pattern: '\\\\bAC[0-9a-fA-F]{32}'\n"
                "    replacement: '[REDACTED\\\\g<0>]'\n",
            )
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("backslashes are not allowed", str(ctx.exception))

    def test_rejects_invalid_regex(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "badre.yml"
            _write_patterns(
                path,
                "patterns:\n"
                "  - id: bad\n"
                "    pattern: '(unclosed'\n"
                "    replacement: '[REDACTED]'\n",
            )
            with self.assertRaises(ValueError) as ctx:
                _load_secret_redactions(str(path))
            self.assertIn("Invalid regex", str(ctx.exception))

    def test_missing_file_raises_file_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing.yml"
            with self.assertRaises(FileNotFoundError):
                _load_secret_redactions(str(path))

    def test_yaml_only_new_pattern_requires_no_python_change(self) -> None:
        """Acceptance: adding a pattern in YAML alone is enough."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pii_patterns.yml"
            _write_patterns(
                path,
                "version: 1\n"
                "patterns:\n"
                "  - id: demo_token\n"
                "    pattern: '\\bDEMO_[A-Z0-9]{8}\\b'\n"
                "    replacement: '[REDACTED_DEMO]'\n",
            )
            text, count = _redact_embedded_secrets(
                "prefix DEMO_ABCD1234 suffix",
                patterns_path=str(path),
            )
            self.assertEqual(count, 1)
            self.assertEqual(text, "prefix [REDACTED_DEMO] suffix")

    def test_explicit_path_is_not_cached_across_calls(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path_a = Path(tmp) / "a.yml"
            path_b = Path(tmp) / "b.yml"
            _write_patterns(
                path_a,
                "patterns:\n"
                "  - pattern: '\\bAAA\\b'\n"
                "    replacement: '[A]'\n",
            )
            _write_patterns(
                path_b,
                "patterns:\n"
                "  - pattern: '\\bBBB\\b'\n"
                "    replacement: '[B]'\n",
            )
            text_a, _ = _redact_embedded_secrets("AAA BBB", patterns_path=str(path_a))
            text_b, _ = _redact_embedded_secrets("AAA BBB", patterns_path=str(path_b))
            self.assertEqual(text_a, "[A] BBB")
            self.assertEqual(text_b, "AAA [B]")


class RedactEmbeddedSecretsTests(unittest.TestCase):
    def tearDown(self) -> None:
        _load_default_secret_redactions.cache_clear()

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

    def test_literal_replacement_does_not_expand_group_refs(self) -> None:
        """Even if validation were bypassed, subn must not re-embed the secret."""
        sid = "AC" + ("a" * 32)
        pattern = __import__("re").compile(r"\bAC[0-9a-fA-F]{32}")
        # Simulate a bypassed loader returning a backreference-style replacement.
        with mock.patch(
            "export_support_cases_from_looker._load_secret_redactions",
            return_value=[(pattern, r"[REDACTED\g<0>]")],
        ):
            text, count = _redact_embedded_secrets(f"token {sid} end")
        self.assertEqual(count, 1)
        self.assertNotIn(sid, text)
        self.assertIn(r"[REDACTED\g<0>]", text)


class RedactExportTextTests(unittest.TestCase):
    def tearDown(self) -> None:
        _load_default_secret_redactions.cache_clear()

    def test_wrapper_exits_on_missing_patterns_file(self) -> None:
        with mock.patch(
            "export_support_cases_from_looker._redact_embedded_secrets",
            side_effect=FileNotFoundError("missing patterns"),
        ):
            with self.assertRaises(SystemExit) as ctx:
                _redact_export_text("anything")
            self.assertEqual(ctx.exception.code, 1)

    def test_wrapper_exits_on_value_error(self) -> None:
        with mock.patch(
            "export_support_cases_from_looker._redact_embedded_secrets",
            side_effect=ValueError("bad config"),
        ):
            with self.assertRaises(SystemExit) as ctx:
                _redact_export_text("anything")
            self.assertEqual(ctx.exception.code, 1)

    def test_wrapper_exits_on_oserror(self) -> None:
        with mock.patch(
            "export_support_cases_from_looker._redact_embedded_secrets",
            side_effect=PermissionError("denied"),
        ):
            with self.assertRaises(SystemExit) as ctx:
                _redact_export_text("anything")
            self.assertEqual(ctx.exception.code, 1)

    def test_wrapper_passes_through_successful_redaction(self) -> None:
        text, count = _redact_export_text("no secrets here")
        self.assertEqual(count, 0)
        self.assertEqual(text, "no secrets here")


class ExportRowSanityTests(unittest.TestCase):
    def test_count_csv_data_rows_excludes_header(self) -> None:
        self.assertEqual(_count_csv_data_rows("a,b\n1,2\n3,4"), 2)
        self.assertEqual(_count_csv_data_rows(""), 0)

    def test_validate_rejects_empty_export(self) -> None:
        with self.assertRaises(SystemExit):
            _validate_export_row_count("h\n", prior_row_count=None)

    def test_validate_rejects_sharp_drop(self) -> None:
        csv_text = "h\n" + "\n".join("x" for _ in range(40))
        with self.assertRaises(SystemExit):
            _validate_export_row_count(csv_text, prior_row_count=100)

    def test_validate_allows_first_export_without_prior(self) -> None:
        csv_text = "h\n" + "\n".join("x" for _ in range(10))
        self.assertEqual(_validate_export_row_count(csv_text, prior_row_count=None), 10)

    def test_validate_allows_modest_drop(self) -> None:
        csv_text = "h\n" + "\n".join("x" for _ in range(60))
        self.assertEqual(_validate_export_row_count(csv_text, prior_row_count=100), 60)


if __name__ == "__main__":
    unittest.main()
