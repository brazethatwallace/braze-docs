#!/usr/bin/env python3
"""
List root _includes/*.md files referenced exactly once from _docs/ or _includes/.

Usage:
  python scripts/find_single_use_includes.py
  python scripts/find_single_use_includes.py --json
  python scripts/find_single_use_includes.py --eligible   # batch filters for inlining

Output: scripts/temp/single_use_includes_report.md (unless --json)
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INCLUDES_DIR = PROJECT_ROOT / "_includes"
SCAN_DIRS = [PROJECT_ROOT / "_docs", INCLUDES_DIR]
OUT_FILE = PROJECT_ROOT / "scripts" / "temp" / "single_use_includes_report.md"

INCLUDE_RE = re.compile(
    r"\{%-?\s*(?:multi_lang_include|include)\s+"
    r"(?:'([^']+)'|\"([^\"]+)\"|([\w/.+\-()#@~]+))",
    re.IGNORECASE,
)
PARAM_RE = re.compile(r"\{%\s*if\s+include\.|include\.[a-zA-Z_]+")


def normalize_ref(ref: str) -> str:
    ref = ref.strip()
    return ref if ref.endswith(".md") else f"{ref}.md"


def scan_references() -> dict[str, list[dict]]:
    refs: dict[str, list[dict]] = defaultdict(list)
    for root in SCAN_DIRS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            rel_src = path.relative_to(PROJECT_ROOT).as_posix()
            for match in INCLUDE_RE.finditer(text):
                inc = normalize_ref(match.group(1) or match.group(2) or match.group(3) or "")
                if not inc or inc == ".md":
                    continue
                refs[inc].append(
                    {
                        "source": rel_src,
                        "raw": match.group(0),
                    }
                )
    return refs


def classify_include(rel: str, refs: dict[str, list[dict]]) -> dict:
    path = INCLUDES_DIR / rel
    body = path.read_text(encoding="utf-8", errors="ignore")
    callers = refs.get(rel, [])
    return {
        "include": rel,
        "reference_count": len(callers),
        "callers": callers,
        "words": len(body.split()),
        "has_include_params": bool(PARAM_RE.search(body)),
        "has_liquid_logic": any(
            token in body for token in ("{% if ", "{% elsif", "{% tabs", "{% sdktab")
        ),
        "is_forwarder_stub": rel.startswith("developer_guide/")
        and "{% multi_lang_include" in body,
        "caller_in_docs": [c for c in callers if c["source"].startswith("_docs/")],
    }


def is_eligible(item: dict, *, max_words: int = 300) -> bool:
    if item["reference_count"] != 1:
        return False
    if not item["caller_in_docs"]:
        return False
    if item["has_include_params"] or item["has_liquid_logic"]:
        return False
    if item["is_forwarder_stub"]:
        return False
    if item["include"].startswith("snowflake_users_messages/"):
        return False
    if item["words"] > max_words:
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print JSON to stdout")
    parser.add_argument(
        "--eligible",
        action="store_true",
        help="Only list safe batch-1 inline candidates",
    )
    parser.add_argument("--max-words", type=int, default=300)
    args = parser.parse_args()

    refs = scan_references()
    items = []
    for path in sorted(INCLUDES_DIR.rglob("*.md")):
        rel = path.relative_to(INCLUDES_DIR).as_posix()
        item = classify_include(rel, refs)
        if args.eligible and not is_eligible(item, max_words=args.max_words):
            continue
        if not args.eligible and item["reference_count"] != 1:
            continue
        items.append(item)

    if args.json:
        print(json.dumps(items, indent=2))
        return

    lines = [
        "# Single-use includes report",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Includes scanned | {len(list(INCLUDES_DIR.rglob('*.md')))} |",
        f"| Single-reference includes | {sum(1 for i in items if i['reference_count']==1) if not args.eligible else len(items)} |",
        f"| Eligible for inlining (filters) | {sum(1 for i in items if is_eligible(i, max_words=args.max_words))} |",
        "",
    ]
    if args.eligible:
        lines.append("## Eligible batch candidates\n")
    else:
        lines.append("## Single-reference includes\n")

    for item in sorted(items, key=lambda x: (-x["words"], x["include"])):
        caller = item["callers"][0]["source"] if item["callers"] else "(none)"
        flags = []
        if item["has_include_params"]:
            flags.append("params")
        if item["has_liquid_logic"]:
            flags.append("liquid")
        if item["is_forwarder_stub"]:
            flags.append("forwarder")
        flag_text = f" ({', '.join(flags)})" if flags else ""
        lines.append(
            f"- `{item['include']}` — {item['words']} words → `{caller}`{flag_text}"
        )

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_FILE.relative_to(PROJECT_ROOT)} ({len(items)} items)")


if __name__ == "__main__":
    main()
