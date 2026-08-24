#!/usr/bin/env python3
"""
Per-page SEO/AEO audit — writes recommendation packets split by approval tier.

Usage:
  python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
H2_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
FAQ_HEADING_RE = re.compile(r"faq|frequently asked", re.I)
HEADING_LEVEL_RE = re.compile(r"^(#{1,6})\s+")


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def word_count(text: str) -> int:
    return len(re.sub(r"[>#*`\[\](){}]", " ", text).split())


def suggest_description(article_title: str, h1: str, intro: str) -> str:
    raw = intro.strip()
    raw = re.sub(r"\{%[^%]+%\}", "", raw)
    raw = re.sub(r"^#+\s*", "", raw)
    raw = re.sub(r"^>\s*", "", raw)
    raw = re.sub(r"\s+", " ", raw).strip()
    if not raw or len(raw) < 20:
        topic = h1 or article_title or "this topic"
        raw = f"Learn about {topic} in Braze."
    if len(raw) > 147:
        raw = raw[:147].rsplit(" ", 1)[0] + "."
    if not raw.endswith("."):
        raw += "."
    return raw


def audit_page(md_path: Path, link_rows: list[dict]) -> str:
    rel = md_path.relative_to(REPO_ROOT)
    url_path = str(rel).replace("_docs/_", "/docs/").replace(".md", "").replace("_docs/", "/docs/")
    text = md_path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    body = FRONTMATTER_RE.sub("", text, count=1)
    h1_m = H1_RE.search(body)
    h1 = h1_m.group(1).strip() if h1_m else ""
    article_title = fm.get("article_title", "")
    description = fm.get("description", "")

    first_h2 = re.search(r"^##\s+", body, re.MULTILINE)
    intro = body[: first_h2.start()] if first_h2 else body[:800]
    intro_words = word_count(intro)

    # heading skip check
    heading_issues = []
    last_level = 0
    for m in HEADING_LEVEL_RE.finditer(body):
        level = len(m.group(1))
        if last_level and level > last_level + 1:
            heading_issues.append(f"Skipped heading level (H{last_level} to H{level}): {m.group(0).strip()}")
        last_level = level

    has_faq = bool(FAQ_HEADING_RE.search(body)) or fm.get("page_type", "").upper() == "FAQ"
    page_links = [r for r in link_rows if r.get("source_file") == str(rel)]

    lines = [
        f"# SEO/AEO recommendation: {article_title or h1}",
        "",
        f"**Page:** `{url_path}`",
        f"**Source:** `{rel}`",
        "",
        "## No-approval",
        "",
        "| Field | Current | Recommended | Rationale |",
        "|-------|---------|-------------|-----------|",
    ]

    if not description:
        rec = suggest_description(article_title, h1, intro)
        lines.append(f"| `description` | *(missing)* | `{rec}` | Required for search snippets |")
    elif len(description) > 150:
        rec = description[:147].rsplit(" ", 1)[0] + "."
        lines.append(f"| `description` | `{description[:60]}...` ({len(description)} chars) | `{rec}` | Over 150-character limit |")

    if article_title and h1 and article_title.lower() != h1.lower():
        rec_title = h1 if len(h1) <= 70 else article_title
        lines.append(
            f"| `article_title` | `{article_title}` | `{rec_title}` | Align title tag with H1 intent |"
        )

    if not has_faq and "faq" not in str(rel).lower():
        lines.append("| `page_type` | *(unset or not FAQ)* | — | No change unless promoting to FAQ hub |")

    if heading_issues:
        for issue in heading_issues[:3]:
            lines.append(f"| Heading | {issue[:50]}... | Fix level | WCAG / style guide |")

    lines.extend(["", "### Link fix table", ""])
    if page_links:
        lines.append(
            "| Section heading | Surrounding sentence | Current URL | Verified replacement | Status |"
        )
        lines.append("|-------------------|----------------------|-------------|----------------------|--------|")
        for r in page_links:
            lines.append(
                f"| {r.get('section_heading','')} | {r.get('surrounding_sentence','')[:80]}... | "
                f"`{r.get('current_url','')}` | `{r.get('verified_replacement','')}` | {r.get('status','')} |"
            )
    else:
        lines.append("*No broken or stale internal links detected on this page.*")

    lines.extend(["", "## Approval-needed", ""])

    if intro_words < 80:
        lines.extend(
            [
                "### Opening answer block (proposed)",
                "",
                f"> *Current intro is ~{intro_words} words. Target 80–120 words that directly answer the primary question before the first `##` section.*",
                "",
                f"> {suggest_description(article_title, h1, intro)}",
                "",
            ]
        )
    elif intro_words > 150:
        lines.extend(
            [
                "### Opening answer block (proposed)",
                "",
                f"> *Current intro is ~{intro_words} words before the first `##`. Consider tightening to ~120 words with a direct answer in the first sentence.*",
                "",
            ]
        )
    else:
        lines.append("### Opening answer block")
        lines.append("")
        lines.append(f"*Intro is ~{intro_words} words — within range. Optional polish only.*")
        lines.append("")

    if not has_faq:
        lines.extend(
            [
                "### FAQ additions (proposed)",
                "",
                "Consider adding 2–3 `####` FAQ entries if support cases or search queries repeat for this topic.",
                "",
            ]
        )
    else:
        lines.append("### FAQ additions")
        lines.append("")
        lines.append("*Page already has an FAQ section or `page_type: FAQ`.*")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "*Generated by `scripts/seo_pilot/page_audit.py`. No-approval items can ship in a PR; approval-needed items require editorial sign-off.*",
            "",
        ]
    )
    return "\n".join(lines)


def slugify(path: Path) -> str:
    name = path.stem
    parent = path.parent.name
    if parent.startswith("_"):
        parent = parent[1:]
    return f"{parent}-{name}" if parent not in ("_user_guide", "_api", "_developer_guide", "_partners") else name


def main() -> int:
    parser = argparse.ArgumentParser(description="Per-page SEO/AEO audit")
    parser.add_argument("--pages-file", type=Path, required=True)
    parser.add_argument(
        "--link-fix-csv",
        type=Path,
        default=REPO_ROOT / "scripts/temp/link-fix-table-pilot.csv",
    )
    parser.add_argument("--out-dir", type=Path, default=REPO_ROOT / "docs/seo_pilot/recommendations")
    args = parser.parse_args()

    pages = [
        line.strip()
        for line in args.pages_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    link_rows: list[dict] = []
    if args.link_fix_csv.is_file():
        with args.link_fix_csv.open(newline="", encoding="utf-8") as f:
            link_rows = list(csv.DictReader(f))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for page in pages:
        md_path = REPO_ROOT / page
        if not md_path.is_file():
            print(f"Skip missing: {page}", file=sys.stderr)
            continue
        content = audit_page(md_path, link_rows)
        out_name = slugify(md_path) + ".md"
        out_path = args.out_dir / out_name
        out_path.write_text(content, encoding="utf-8")
        print(f"Wrote {out_path}")

    # recommendation index template
    index_path = args.out_dir.parent / "README.md"
    if not index_path.is_file():
        index_path.write_text(
            "# SEO pilot recommendations\n\n"
            "Per-page recommendation packets from the in-house SEO/AEO pilot.\n\n"
            "See [`recommendations/`](recommendations/) for individual page audits.\n\n"
            "Regenerate with:\n\n"
            "```bash\n"
            "python3 scripts/seo_pilot/page_scorecard.py --write-pilot-list\n"
            "python3 scripts/seo_pilot/link_fix_table.py --pages-file scripts/temp/pilot-pages.txt\n"
            "python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt\n"
            "```\n",
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
