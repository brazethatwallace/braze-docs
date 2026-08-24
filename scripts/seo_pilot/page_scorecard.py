#!/usr/bin/env python3
"""
Rank English _docs/ pages by SEO/AEO optimization headroom.

Combines optional GSC, Algolia, and support-case signals with in-repo metadata
and link-health checks. Writes a scorecard CSV and optional pilot-pages list.

Usage:
  python3 scripts/seo_pilot/page_scorecard.py --out scripts/temp/seo-pilot-scorecard.csv --top 15
  python3 scripts/seo_pilot/page_scorecard.py --gsc gsc.csv --support cases.csv --write-pilot-list
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "_docs"
BROKEN_LINKS_CSV = REPO_ROOT / "scripts" / "temp" / "broken-links.csv"

# Editorial hub paths (relative to _docs, without .md) — boost pilot candidacy
EDITORIAL_HUBS = [
    "_docs/_user_guide/channels/sms_mms_and_rcs",
    "_docs/_user_guide/messaging/canvas",
    "_docs/_user_guide/messaging/design_and_edit/personalize/liquid",
    "_docs/_api/home",
    "_docs/_user_guide/audience/subscription_preferences/preference_center",
    "_docs/_user_guide/channels/email",
    "_docs/_user_guide/channels/in_app_messages",
    "_docs/_user_guide/channels/push",
    "_docs/_user_guide/channels/whatsapp",
    "_docs/_user_guide/data/distribution/braze_currents",
    "_docs/_developer_guide/home",
    "_docs/_user_guide/brazeai",
    "_docs/_partners/home",
    "_docs/_user_guide/segments",
    "_docs/_user_guide/analytics",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
YAML_KV_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.+)$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    block = m.group(1)
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        out[key] = val
    return out


def doc_path_to_url(rel_md: Path) -> str:
    """_docs/_user_guide/foo/bar.md -> /docs/user_guide/foo/bar"""
    parts = rel_md.parts
    if parts[0] != "_docs" or len(parts) < 2:
        return ""
    collection = parts[1].lstrip("_")
    rest = "/".join(parts[2:]).replace(".md", "")
    if rest:
        return f"/docs/{collection}/{rest}"
    return f"/docs/{collection}"


def is_braze_host(hostname: str | None) -> bool:
    if not hostname:
        return False
    host = hostname.lower()
    return host == "braze.com" or host.endswith(".braze.com")


def extract_docs_path(url: str) -> str | None:
    """Return /docs/... pathname when url is a Braze docs URL."""
    url = url.strip()
    if url.startswith("/docs"):
        return url.split("?")[0].split("#")[0]
    parsed = urlparse(url)
    if is_braze_host(parsed.hostname) and parsed.path.startswith("/docs"):
        return parsed.path.split("?")[0].split("#")[0]
    return None


def url_to_doc_path(url: str) -> str | None:
    path = extract_docs_path(url)
    if not path:
        return None
    path = path.rstrip("/")
    rest = path[len("/docs/") :]
    segments = rest.split("/")
    if not segments or not segments[0]:
        return None
    collection = segments[0]
    sub = "/".join(segments[1:])
    md = DOCS_ROOT / f"_{collection}" / f"{sub}.md" if sub else DOCS_ROOT / f"_{collection}.md"
    if md.is_file():
        return str(md.relative_to(REPO_ROOT))
    return None


def load_gsc(path: Path) -> dict[str, dict[str, float]]:
    """Map /docs/... URL -> {impressions, clicks, ctr, position}."""
    out: dict[str, dict[str, float]] = {}
    if not path.is_file():
        return out
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return out
        fields = {c.lower().strip(): c for c in reader.fieldnames}
        page_col = fields.get("page") or fields.get("url") or fields.get("top pages")
        if not page_col:
            return out
        for row in reader:
            page = row.get(page_col, "").strip()
            if not page:
                continue
            if not page.startswith("/docs"):
                docs_path = extract_docs_path(page)
                if not docs_path:
                    continue
                page = docs_path
            page = page.rstrip("/")
            try:
                impressions = float(row.get(fields.get("impressions", "impressions"), 0) or 0)
                clicks = float(row.get(fields.get("clicks", "clicks"), 0) or 0)
                ctr_raw = row.get(fields.get("ctr", "ctr"), "") or ""
                ctr = float(str(ctr_raw).replace("%", "")) if ctr_raw else 0.0
                pos_raw = row.get(fields.get("position", "position"), "") or row.get(
                    fields.get("avg position", ""), ""
                )
                position = float(pos_raw) if pos_raw else 0.0
            except ValueError:
                continue
            out[page] = {
                "impressions": impressions,
                "clicks": clicks,
                "ctr": ctr,
                "position": position,
            }
    return out


def load_algolia(path: Path) -> dict[str, float]:
    """Map doc_path -> zero-hit / low-click weight."""
    out: dict[str, float] = defaultdict(float)
    if not path.is_file():
        return out
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            count = float(row.get("count", 1) or 1)
            doc_path = row.get("doc_path", "").strip()
            if doc_path:
                out[doc_path] += count
                continue
            query = (row.get("query") or "").lower()
            # Heuristic: map query keywords to likely doc paths
            for hub in EDITORIAL_HUBS:
                hub_slug = hub.split("/")[-1].replace("_", " ")
                if hub_slug in query or hub.replace("_", " ") in query:
                    out[f"{hub}.md"] += count * 0.5
    return dict(out)


def load_support(path: Path) -> dict[str, int]:
    """Map doc_path -> mention count from support cases."""
    out: dict[str, int] = defaultdict(int)
    if not path.is_file():
        return out
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            blob = " ".join(str(v) for v in row.values()).lower()
            for m in re.finditer(r"/docs/[a-z0-9_/-]+", blob):
                dp = url_to_doc_path(m.group(0))
                if dp:
                    out[dp] += 1
            for hub in EDITORIAL_HUBS:
                slug = hub.split("/")[-1].replace("_", " ")
                if slug in blob:
                    out[f"{hub}.md"] += 1
    return dict(out)


def load_broken_link_counts() -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    if not BROKEN_LINKS_CSV.is_file():
        return out
    with BROKEN_LINKS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fpath = row.get("File", "").strip()
            if fpath:
                out[fpath] += 1
    return dict(out)


def metadata_penalty(fm: dict[str, str], body: str) -> tuple[float, list[str]]:
    """Higher penalty = more headroom / needs work."""
    penalty = 0.0
    notes: list[str] = []
    desc = fm.get("description", "").strip()
    if not desc:
        penalty += 15
        notes.append("missing_description")
    elif len(desc) > 150:
        penalty += 10
        notes.append("description_over_150")
    title = fm.get("article_title", "").strip()
    h1_m = H1_RE.search(body)
    h1 = h1_m.group(1).strip() if h1_m else ""
    if title and h1 and title.lower() != h1.lower() and title.split()[0].lower() != h1.split()[0].lower():
        penalty += 5
        notes.append("title_h1_mismatch")
    # Intro block: words before first ##
    body_no_fm = FRONTMATTER_RE.sub("", body, count=1)
    first_h2 = re.search(r"^##\s+", body_no_fm, re.MULTILINE)
    intro = body_no_fm[: first_h2.start()] if first_h2 else body_no_fm[:500]
    intro_words = len(re.sub(r"[>#*`\[\]()]", " ", intro).split())
    if intro_words < 40:
        penalty += 8
        notes.append("short_intro")
    elif intro_words > 180:
        penalty += 4
        notes.append("long_intro_before_h2")
    return penalty, notes


def gsc_headroom(gsc: dict[str, float]) -> float:
    """High impressions + mid position + low CTR = headroom."""
    imp = gsc.get("impressions", 0)
    pos = gsc.get("position", 0)
    ctr = gsc.get("ctr", 0)
    if imp < 100:
        return 0.0
    pos_score = 0.0
    if 5 <= pos <= 20:
        pos_score = 25
    elif 3 <= pos < 5:
        pos_score = 15
    elif 20 < pos <= 40:
        pos_score = 10
    ctr_penalty = max(0, 5 - ctr) * 3 if ctr < 5 else 0
    return min(50, (imp / 1000) * 10 + pos_score + ctr_penalty)


def iter_doc_files() -> list[Path]:
    skip_prefixes = (
        "_docs/_hidden/",
        "_docs/_unlisted_docs/",
        "_docs/_docs_pages/",
        "_docs/_contributing/",
    )
    out = []
    for p in sorted(DOCS_ROOT.rglob("*.md")):
        rel = str(p.relative_to(REPO_ROOT)).replace("\\", "/")
        if any(rel.startswith(pref) for pref in skip_prefixes):
            continue
        out.append(p)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="SEO/AEO page scorecard for _docs/")
    parser.add_argument("--gsc", type=Path, help="GSC pages export CSV")
    parser.add_argument("--algolia", type=Path, help="Algolia zero-result queries CSV")
    parser.add_argument("--support", type=Path, help="Support cases CSV")
    parser.add_argument("--out", type=Path, default=REPO_ROOT / "scripts/temp/seo-pilot-scorecard.csv")
    parser.add_argument("--top", type=int, default=15, help="Flag top N as pilot_tier=yes")
    parser.add_argument("--write-pilot-list", action="store_true", help="Write scripts/temp/pilot-pages.txt")
    args = parser.parse_args()

    gsc_data = load_gsc(args.gsc) if args.gsc else {}
    algolia_data = load_algolia(args.algolia) if args.algolia else {}
    support_data = load_support(args.support) if args.support else {}
    broken_counts = load_broken_link_counts()

    hub_set = {f"{h}.md" for h in EDITORIAL_HUBS}

    rows: list[dict] = []
    for md_path in iter_doc_files():
        rel = md_path.relative_to(REPO_ROOT)
        rel_s = str(rel)
        text = md_path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if fm.get("noindex", "").lower() == "true":
            continue
        if fm.get("hidden", "").lower() == "true" and fm.get("permalink", "") == "":
            continue

        url = doc_path_to_url(rel)
        gsc = gsc_data.get(url, gsc_data.get(url + "/", {}))
        meta_pen, meta_notes = metadata_penalty(fm, text)
        editorial_boost = 35 if rel_s in hub_set else 0
        broken = broken_counts.get(rel_s, 0)
        support_n = support_data.get(rel_s, 0)
        algolia_n = algolia_data.get(rel_s, 0)

        headroom = (
            gsc_headroom(gsc)
            + meta_pen
            + editorial_boost
            + broken * 5
            + support_n * 3
            + algolia_n * 2
        )

        rows.append(
            {
                "doc_path": rel_s,
                "docs_url": url,
                "gsc_impressions": int(gsc.get("impressions", 0)),
                "gsc_avg_position": round(gsc.get("position", 0), 1),
                "gsc_ctr": round(gsc.get("ctr", 0), 2),
                "support_mentions": support_n,
                "algolia_zero_hits": round(algolia_n, 1),
                "broken_links": broken,
                "metadata_flags": ";".join(meta_notes) if meta_notes else "",
                "editorial_hub": "yes" if editorial_boost else "no",
                "headroom_score": round(headroom, 1),
                "pilot_tier": "",
            }
        )

    rows.sort(key=lambda r: -r["headroom_score"])
    for i, row in enumerate(rows):
        row["pilot_tier"] = "yes" if i < args.top else "no"

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.out}")
    print(f"Top {args.top} pilot candidates:")
    for row in rows[: args.top]:
        print(f"  {row['headroom_score']:6.1f}  {row['doc_path']}  [{row['metadata_flags']}]")

    if args.write_pilot_list:
        pilot_list = REPO_ROOT / "scripts" / "temp" / "pilot-pages.txt"
        pilot_list.parent.mkdir(parents=True, exist_ok=True)
        pilot_list.write_text(
            "\n".join(r["doc_path"] for r in rows[: args.top]) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote pilot list to {pilot_list}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
