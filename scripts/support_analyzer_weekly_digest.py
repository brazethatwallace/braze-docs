#!/usr/bin/env python3
"""
Build a weekly support-case digest markdown from the Looker CSV export.

This is a lightweight theme summary (keyword counts). It does not triage against
the support-analyzer skill, verify product behavior, or edit _docs. Use
`.github/skills/support-analyzer/SKILL.md` on the CSV for that.
"""

import argparse
import csv
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# Common English stopwords to reduce noise in theme counts
_STOPWORDS = frozenset(
    "a an the and or for to of in on at by is are was were be been being "
    "it this that these those we you our your they their not no yes if as "
    "with from into about over after before can could would should may might "
    "will has have had do does did get got go going been out up so than then "
    "there when where what which who how all any each both few more most some "
    "such only same own than too very just also into through during per via "
    "using use used using please help need want like email app braze canvas "
    "campaign message messages user users data team hi hello thanks thank"
    .split()
)

_EMAIL_RE = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
_URL_RE = re.compile(r"\b(?:https?://|www\.)\S+", re.IGNORECASE)
_UUID_RE = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b"
)


def _strip_sensitive_content(text: str) -> str:
    """Remove common PII / high-entropy tokens from text before tokenizing."""
    text = _EMAIL_RE.sub(" ", text)
    text = _URL_RE.sub(" ", text)
    text = _UUID_RE.sub(" ", text)
    return text


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    sanitized = _strip_sensitive_content(text).lower()
    # Letters only (avoids surfacing numeric IDs and mixed tokens in the digest table)
    words = re.findall(r"[a-z]{3,}", sanitized)
    return [w for w in words if w not in _STOPWORDS]


def main() -> None:
    p = argparse.ArgumentParser(description="Build support-case digest markdown from CSV.")
    p.add_argument("input_csv", help="Path to Support Cases CSV")
    p.add_argument("output_md", help="Path to write digest markdown")
    args = p.parse_args()

    input_path = Path(args.input_csv)
    if not input_path.is_file():
        raise SystemExit(f"Input not found: {input_path}")

    required_columns = {
        "Support Cases Email Message Case ID",
        "Support Cases Description",
    }
    with input_path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing_columns = sorted(required_columns - set(fieldnames))
        if missing_columns:
            available_columns = ", ".join(fieldnames) if fieldnames else "(none)"
            raise SystemExit(
                "Input CSV is missing required column(s): "
                + ", ".join(missing_columns)
                + f". Available columns: {available_columns}"
            )
        rows = list(reader)

    case_ids = set()
    descriptions = []
    for row in rows:
        cid = (row.get("Support Cases Email Message Case ID") or "").strip()
        if cid:
            case_ids.add(cid)
        desc = row.get("Support Cases Description") or ""
        if desc.strip():
            descriptions.append(desc)

    word_counts: Counter[str] = Counter()
    for desc in descriptions:
        word_counts.update(tokenize(desc))

    top = word_counts.most_common(40)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Weekly support cases digest (automated)",
        "",
        f"_Generated {now} from Looker export. This file is not customer-facing documentation._",
        "",
        "## What this is",
        "",
        "- **Counts and keyword themes** from the latest CSV only.",
        "- **Not** a substitute for the **support-analyzer** skill (`.github/skills/support-analyzer/SKILL.md`): no triage categories, no verification against product source, and **no automated edits to `_docs`**. ",
        "",
        "## Batch stats",
        "",
        f"- **Message rows in CSV:** {len(rows)}",
        f"- **Unique case IDs:** {len(case_ids)}",
        "",
        "## Frequent terms in case descriptions",
        "",
        "Use this list to spot recurring product areas; then run the **support-analyzer** skill on `_data/support_cases_latest.csv` (branch `support-analyzer-data`) to triage and draft real doc updates.",
        "",
        "| Term | Approx. mentions |",
        "| --- | ---: |",
    ]
    for word, count in top:
        lines.append(f"| `{word}` | {count} |")

    lines.extend(
        [
            "",
            "## Next steps (human or Cursor)",
            "",
            "1. Check out `support-analyzer-data` and open `_data/support_cases_latest.csv`.",
            "2. Run `@support-analyzer` (`.github/skills/support-analyzer/SKILL.md`) on that CSV for themes outside the automated Phase 2 rules.",
            "3. Review **Support analyzer (Looker)** workflow Phase 2 draft PRs (from `.github/support_analyzer_phase2_rules.yml`) when they open.",
            "4. If the digest pull request was auto-closed after the run, download this digest from the **support-analyzer-weekly-digest** workflow artifact.",
            "5. Open additional doc PRs from manual analyzer output after you review (do not merge machine-only digests as product docs).",
            "",
        ]
    )

    out = Path(args.output_md)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
