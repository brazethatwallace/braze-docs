#!/usr/bin/env python3
"""
Tests for Phrase TMS glossary client helpers.

Run with:
    python3 -m pytest scripts/test_phrase_tms_client.py -v
"""

import json
import sys
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import phrase_tms_client as ptc  # noqa: E402


def _build_sample_xlsx() -> bytes:
    import openpyxl

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(["en_us", "de_de", "es"])
    worksheet.append(["Campaign", "Kampagne", "Campaña"])
    worksheet.append(["team", "Team", "equipo"])
    buffer = BytesIO()
    workbook.save(buffer)
    workbook.close()
    return buffer.getvalue()


class TestLoadTermBaseConfig:
    def test_loads_unified_config(self, tmp_path, monkeypatch):
        config_path = tmp_path / "phrase_term_bases.json"
        config_path.write_text(
            json.dumps(
                {
                    "term_base": {"uid": "abc123", "name": "Unified"},
                    "source_lang": "en_us",
                    "locales": {
                        "de": {"target_lang": "de_de"},
                        "es": {"target_lang": "es"},
                    },
                }
            ),
            encoding="utf-8",
        )
        monkeypatch.setattr(ptc, "TERM_BASES_PATH", config_path)
        config = ptc.load_term_base_config()
        assert config.term_base_uid == "abc123"
        assert config.term_base_name == "Unified"
        assert config.locales["de"]["target_lang"] == "de_de"

    def test_french_target_lang_matches_phrase_column_code(self):
        config = ptc.load_term_base_config()
        assert config.locales["fr"]["target_lang"] == "fr_fr"


class TestParseTermBaseXlsxMulti:
    def test_parses_multiple_locale_columns(self):
        glossaries = ptc.parse_term_base_xlsx_multi(
            _build_sample_xlsx(),
            source_lang="en_us",
            locale_targets={"de": "de_de", "es": "es"},
        )
        assert glossaries["de"]["Campaign"] == "Kampagne"
        assert glossaries["es"]["Campaign"] == "Campaña"
        assert glossaries["de"]["team"] == "Team"
