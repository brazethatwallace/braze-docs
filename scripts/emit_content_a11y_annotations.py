#!/usr/bin/env python3
"""Emit GitHub Actions workflow annotations for content accessibility violations."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

WCAG_TITLES = {
    "1.1.1": "Missing alt text",
    "2.4.4": "Non-descriptive link text",
    "2.4.6": "Heading level skip",
    "4.1.2": "Missing iframe title",
}


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "usage: emit_content_a11y_annotations.py VIOLATIONS_JSON",
            file=sys.stderr,
        )
        return 2

    violations_path = Path(sys.argv[1])
    try:
        violations = json.loads(violations_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Could not read {violations_path}: {exc}", file=sys.stderr)
        return 0

    for violation in violations:
        criterion = violation.get("wcag_criterion", "?")
        title = WCAG_TITLES.get(criterion, f"WCAG {criterion}")
        message = re.sub(
            r"\s+",
            " ",
            violation["message"].split("\n", maxsplit=1)[0].strip(),
        )
        file_path = violation["file"]
        line = violation["table_start_line"]
        print(
            f"::error file={file_path},line={line},"
            f"title=WCAG {criterion} — {title}::{message}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
