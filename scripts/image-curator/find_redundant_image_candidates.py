#!/usr/bin/env python3
"""Find referenced images in English docs that may be redundant or unneeded.

Scans _docs/ and root _includes/ for image references, then flags candidates
using style-guide heuristics (filename, alt text, surrounding prose). Optional
OCR via Tesseract when available (same dependency as check_screenshot_pii.py).

Usage (from repo root):
  python3 scripts/image-curator/find_redundant_image_candidates.py
  python3 scripts/image-curator/find_redundant_image_candidates.py --csv out.csv
  python3 scripts/image-curator/find_redundant_image_candidates.py --min-confidence high

Pull request (Image Pruning / curation batches):
  - Title prefix: [IC]
  - Label: image pruning
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGLISH_SCAN_DIRS = ("_docs", "_includes")
SCAN_EXTENSIONS = {".md", ".html", ".htm", ".yml", ".yaml"}

PROTECTED_IMG_PREFIXES = (
    "assets/img/logos/",
    "assets/img/braze_icons/",
    "assets/img/icons/",
    "assets/img/contributing/style_guide/",
)

PR_TITLE_PREFIX = "[IC]"
PR_LABEL = "image pruning"

Confidence = Literal["high", "medium", "low"]

# Markdown / Liquid image reference patterns.
_MD_IMAGE = re.compile(
    r"!\[([^\]]*)\]\(([^)]+)\)",
    re.IGNORECASE,
)
_HTML_IMG = re.compile(
    r'<img\b[^>]*?\bsrc=["\']([^"\']+)["\'][^>]*>',
    re.IGNORECASE,
)
_ALT_ATTR = re.compile(r'\balt=["\']([^"\']*)["\']', re.IGNORECASE)
_IMAGE_BUSTER = re.compile(
    r"image_buster\s+/?(assets/(?:img|img_archive)/[^\s%}]+)",
    re.IGNORECASE,
)
_YAML_IMAGE = re.compile(
    r"^\s*image:\s*['\"]?/?(assets/(?:img|img_archive)/[^\s'\"]+)['\"]?\s*$",
    re.IGNORECASE | re.MULTILINE,
)

# Heuristic signals (filename + alt + OCR text).
# Narrow list/home/overview chrome — safe to flag; still needs corroboration for high.
_FILENAME_LIST_HOME = re.compile(
    r"(?:"
    r"homepage|home_page|home_dashboard|landing-pages-homepage|"
    r"reporting_home|credits_usage_overview|survey-analytics|"
    r"keyword_home|export_logs_cancel|cancel_calculation|cancel_number"
    r")",
    re.IGNORECASE,
)
# Save/cancel filenames — medium at most unless alt/OCR corroborates.
_FILENAME_SAVE_CANCEL = re.compile(
    r"(?:"
    r"save(?:_button|_changes|_as_template|_flow)?|"
    r"cancel(?:_button|_calculation|_number|_export)?|"
    r"submit(?:_button)?"
    r")",
    re.IGNORECASE,
)
# Full-page chrome and nav-only shots.
_FILENAME_CHROME = re.compile(
    r"(?:"
    r"full_(?:page|dashboard|screen)|entire_dashboard|"
    r"browser_(?:frame|chrome)|url_bar|"
    r"left_(?:nav|sidebar)|sidebar_only|header_only"
    r")",
    re.IGNORECASE,
)
# Builder/editor UI filenames — keep (paired with builder path check).
_BUILDER_UI_FILENAME = re.compile(
    r"(?:"
    r"(?:^|/)dnd\.|/form\.|page_container|device_responsive|wrap_with_span|"
    r"span_properties|get-snippet|select-personalization|pre-fill|lp_liquid|"
    r"lp-optional|connect_subdomain|segmentation_selected|trigger\.|"
    r"url-handle-example|manage-lp-template|copy-url|"
    r"landing_pages/template\.png|"
    r"placement_details|content_card_|full_page\.|_home_icon\.|teams\.png|"
    r"sms_keywords|identifier_for_reporting"
    r")",
    re.IGNORECASE,
)
_ALT_HIGH = re.compile(
    r"(?:"
    r"\bsave\b.*\bbutton\b|\bcancel\b.*\bbutton\b|"
    r"\bhome\s*page\b|\blanding\s*page\b|"
    r"\bentire\s+dashboard\b|\bfull\s+dashboard\b|"
    r"\bleft\s+(?:navigation|nav|sidebar)\b|"
    r"\bbrowser\s+(?:frame|chrome|window)\b|"
    r"\burl\s+bar\b|\bbookmarks?\b.*\btabs?\b|"
    r"\bscreenshot\s+of\s+the\s+(?:entire|full)\b"
    r")",
    re.IGNORECASE,
)
_ALT_REDUNDANT_PREFIX = re.compile(
    r"^(?:a\s+)?(?:screenshot|image|picture)\s+of\s+",
    re.IGNORECASE,
)
_OCR_BUTTON_ONLY = re.compile(
    r"^(?:save|cancel|submit|done|ok|close|back|next)\s*$",
    re.IGNORECASE,
)
_OCR_MIN_USEFUL_LEN = 40
PARTNER_SOURCE_PREFIX = "_docs/_partners/"
BUILDER_SOURCE_PREFIXES = (
    "_docs/_user_guide/messaging/landing_pages/",
    "_includes/span_text.md",
)

# Diagrams, workflows, and integration graphics — keep; do not auto-curate.
_DIAGRAM_WORKFLOW = re.compile(
    r"(?:"
    r"diagram|workflow|flowchart|flow.?chart|architecture|schematic|"
    r"data.?flow|process.?flow|integration.?flow|lifecycle|funnel|"
    r"overview.?graphic|graphic.?showing|shows?\s+how|fit\s+together|"
    r"arrow.?point|process\s+to\s+update|connection\s+flow|"
    r"churn_overview|rate_limiting_overview|user_profile_process|"
    r"overview of churn|venn diagram"
    r")",
    re.IGNORECASE,
)
# Third-party admin consoles (GCP, AWS, Infobip, etc.) — keep.
_THIRD_PARTY_CONSOLE = re.compile(
    r"(?:"
    r"google cloud|gcp|aws |amazon web services|azure|infobip|"
    r"meta ads|facebook ads|service account|cloud console|fabric console|"
    r"iam section|manage keys|create service account"
    r")",
    re.IGNORECASE,
)
# Metric tiles and chart examples — keep even on dashboard pages.
_METRIC_CHART_EXAMPLE = re.compile(
    r"(?:"
    r"metric tile|trend line|chart|graph showing|performance over time|"
    r"increase badge|percent increase"
    r")",
    re.IGNORECASE,
)
# Instructional placement — pencil icons, permissions panels, card types.
_ALT_INSTRUCTIONAL_PLACEMENT = re.compile(
    r"(?:"
    r"pencil icon|placement (?:ID|details)|permissions|content card|"
    r"identifier for reporting|opt-in keywords|custom attribute checkbox"
    r")",
    re.IGNORECASE,
)


@dataclass
class ImageRef:
    source_file: str
    line_number: int
    alt_text: str
    image_path: str
    match_line: str
    context_before: str
    context_after: str
    reasons: list[str] = field(default_factory=list)
    confidence: Confidence = "low"
    ocr_snippet: str = ""

    def normalized_path(self) -> str:
        path = self.image_path.strip()
        path = re.sub(r"\{%\s*image_buster\s+", "", path, flags=re.IGNORECASE)
        path = path.rstrip(" %}){:\"'")
        if path.startswith("/"):
            path = path[1:]
        if not path.startswith("assets/"):
            if "assets/img/" in path:
                path = path[path.index("assets/") :]
            elif "assets/img_archive/" in path:
                path = path[path.index("assets/") :]
        return unquote(path.split()[0])


def is_protected_path(rel_path: str) -> bool:
    rel_path = rel_path.replace("\\", "/")
    return any(rel_path.startswith(prefix) for prefix in PROTECTED_IMG_PREFIXES)


def is_partner_page(source_file: str) -> bool:
    return source_file.replace("\\", "/").startswith(PARTNER_SOURCE_PREFIX)


def is_diagram_or_workflow(path: str, alt: str, ocr_text: str) -> bool:
    combined = f"{path} {alt} {ocr_text}".lower()
    return bool(_DIAGRAM_WORKFLOW.search(combined))


def is_builder_editor_ui(source_file: str, path: str) -> bool:
    sf = source_file.replace("\\", "/")
    basename = Path(path).name.lower()
    if "landing-pages-homepage" in basename or basename.endswith("homepage.png"):
        return False
    if any(sf.startswith(prefix) or sf == prefix.rstrip("/") for prefix in BUILDER_SOURCE_PREFIXES):
        return True
    if "/messaging/landing_pages/" in sf:
        return True
    return bool(_BUILDER_UI_FILENAME.search(path))


def is_reference_table_icon(ref: ImageRef) -> bool:
    line = ref.match_line
    if "|" in line and "image_buster" in line:
        return True
    alt = ref.alt_text.strip().lower()
    if "icon" in alt and "`" in f"{ref.context_before}\n{line}\n{ref.context_after}":
        return True
    if "_home_icon" in ref.normalized_path():
        return True
    return False


def is_third_party_console(path: str, alt: str, match_line: str) -> bool:
    basename = Path(path).name
    if _FILENAME_SAVE_CANCEL.search(basename):
        return False
    combined = f"{path} {alt} {match_line}"
    return bool(_THIRD_PARTY_CONSOLE.search(combined))


def is_metric_chart_example(alt: str, ocr_text: str) -> bool:
    combined = f"{alt} {ocr_text}"
    return bool(_METRIC_CHART_EXAMPLE.search(combined))


def is_instructional_placement(alt: str, match_line: str) -> bool:
    return bool(_ALT_INSTRUCTIONAL_PLACEMENT.search(f"{alt} {match_line}"))


def iter_english_files() -> list[Path]:
    files: list[Path] = []
    for rel_dir in ENGLISH_SCAN_DIRS:
        root = REPO_ROOT / rel_dir
        if not root.is_dir():
            continue
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                if Path(name).suffix.lower() in SCAN_EXTENSIONS:
                    files.append(Path(dirpath) / name)
    return sorted(files)


def resolve_image_on_disk(normalized: str) -> Path | None:
    if normalized.startswith("assets/img_archive/"):
        candidate = REPO_ROOT / normalized
    elif normalized.startswith("assets/img/"):
        candidate = REPO_ROOT / normalized
    else:
        return None
    return candidate if candidate.is_file() else None


def try_ocr(image_path: Path) -> str:
    try:
        import subprocess

        result = subprocess.run(
            ["tesseract", str(image_path), "stdout", "-l", "eng"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode == 0:
            return (result.stdout or "").strip()
    except (FileNotFoundError, subprocess.SubprocessError, OSError):
        pass
    return ""


def prose_covers_alt(context: str, alt: str) -> bool:
    if not alt or len(alt) < 20:
        return False
    alt_norm = re.sub(r"[^\w\s]", " ", alt.lower())
    alt_norm = re.sub(r"\s+", " ", alt_norm).strip()
    if len(alt_norm) < 15:
        return False
    ctx = re.sub(r"[^\w\s]", " ", context.lower())
    ctx = re.sub(r"\s+", " ", ctx)
    words = [w for w in alt_norm.split() if len(w) > 3]
    if not words:
        return False
    hits = sum(1 for w in words if w in ctx)
    return hits / len(words) >= 0.7


def score_candidate(ref: ImageRef, ocr_text: str) -> None:
    path = ref.normalized_path()
    basename = Path(path).name
    alt = ref.alt_text.strip()
    combined = f"{basename} {alt} {ocr_text}".lower()
    context = f"{ref.context_before}\n{ref.context_after}"

    if is_protected_path(path):
        ref.reasons.append("protected_path")
        ref.confidence = "low"
        return

    if is_partner_page(ref.source_file):
        ref.reasons.append("partner_page_skip")
        ref.confidence = "low"
        return

    if is_diagram_or_workflow(path, alt, ocr_text):
        ref.reasons.append("diagram_or_workflow")
        ref.confidence = "low"
        return

    if is_builder_editor_ui(ref.source_file, path):
        ref.reasons.append("builder_editor_ui")
        ref.confidence = "low"
        return

    if is_reference_table_icon(ref):
        ref.reasons.append("reference_table_icon")
        ref.confidence = "low"
        return

    if is_third_party_console(path, alt, ref.match_line):
        ref.reasons.append("third_party_console")
        ref.confidence = "low"
        return

    if is_metric_chart_example(alt, ocr_text):
        ref.reasons.append("metric_chart_example")
        ref.confidence = "low"
        return

    if is_instructional_placement(alt, ref.match_line):
        ref.reasons.append("instructional_placement")
        ref.confidence = "low"
        return

    if _FILENAME_LIST_HOME.search(path) or _FILENAME_LIST_HOME.search(basename):
        ref.reasons.append("filename_list_home_chrome")
    if _FILENAME_SAVE_CANCEL.search(basename):
        ref.reasons.append("filename_save_cancel")
    if _FILENAME_CHROME.search(path) or _FILENAME_CHROME.search(basename):
        ref.reasons.append("filename_page_chrome")
    if alt and _ALT_HIGH.search(alt):
        ref.reasons.append("alt_describes_redundant_ui")
    if alt and _ALT_REDUNDANT_PREFIX.match(alt) and prose_covers_alt(context, alt):
        ref.reasons.append("alt_redundant_with_prose")
    if not alt or alt.lower() in {"", "image", "screenshot"}:
        if prose_covers_alt(context, basename.replace("_", " ")):
            ref.reasons.append("missing_alt_prose_already_covers")

    if ocr_text:
        ref.ocr_snippet = ocr_text[:200].replace("\n", " ")
        ocr_compact = re.sub(r"\s+", " ", ocr_text).strip()
        if len(ocr_compact) < _OCR_MIN_USEFUL_LEN and _OCR_BUTTON_ONLY.match(ocr_compact):
            ref.reasons.append("ocr_button_only")
        elif re.search(r"\b(?:save|cancel|submit)\b", ocr_compact, re.I) and len(ocr_compact) < 40:
            ref.reasons.append("ocr_mostly_action_button")

    # Style guide: don't use images for terminal/code output.
    if re.search(r"(?:terminal|console|command.?line|code.?sample)", combined):
        ref.reasons.append("terminal_or_code_as_image")

    if not ref.reasons:
        ref.confidence = "low"
        return

    # High confidence requires corroboration (test PR #14293: ~75% false positives
    # when filename alone triggered high).
    corroborating = {
        "filename_list_home_chrome",
        "filename_page_chrome",
        "alt_describes_redundant_ui",
        "alt_redundant_with_prose",
        "ocr_button_only",
        "ocr_mostly_action_button",
    }
    medium_only = {
        "filename_save_cancel",
        "missing_alt_prose_already_covers",
        "terminal_or_code_as_image",
    }

    active = set(ref.reasons)
    corroboration_count = len(active & corroborating)

    if corroboration_count >= 2:
        ref.confidence = "high"
    elif (
        corroboration_count >= 1
        and ("filename_list_home_chrome" in active or "filename_page_chrome" in active)
        and active & {"alt_describes_redundant_ui", "alt_redundant_with_prose", "ocr_button_only", "ocr_mostly_action_button"}
    ):
        ref.confidence = "high"
    elif active & medium_only or corroboration_count == 1:
        ref.confidence = "medium"
    else:
        ref.confidence = "low"


def extract_refs_from_file(path: Path) -> list[ImageRef]:
    rel = path.relative_to(REPO_ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    refs: list[ImageRef] = []

    def context(idx: int) -> tuple[str, str]:
        before = "\n".join(lines[max(0, idx - 3) : idx])
        after = "\n".join(lines[idx + 1 : min(len(lines), idx + 4)])
        return before, after

    for idx, line in enumerate(lines, start=1):
        for match in _MD_IMAGE.finditer(line):
            alt, url = match.group(1), match.group(2)
            before, after = context(idx - 1)
            refs.append(
                ImageRef(
                    source_file=rel,
                    line_number=idx,
                    alt_text=alt,
                    image_path=url,
                    match_line=line.strip(),
                    context_before=before,
                    context_after=after,
                )
            )
        for match in _HTML_IMG.finditer(line):
            src = match.group(1)
            alt_match = _ALT_ATTR.search(match.group(0))
            alt = alt_match.group(1) if alt_match else ""
            before, after = context(idx - 1)
            refs.append(
                ImageRef(
                    source_file=rel,
                    line_number=idx,
                    alt_text=alt,
                    image_path=src,
                    match_line=line.strip(),
                    context_before=before,
                    context_after=after,
                )
            )
        for match in _IMAGE_BUSTER.finditer(line):
            if _MD_IMAGE.search(line) or _HTML_IMG.search(line):
                continue
            img_path = match.group(1)
            before, after = context(idx - 1)
            refs.append(
                ImageRef(
                    source_file=rel,
                    line_number=idx,
                    alt_text="",
                    image_path=img_path,
                    match_line=line.strip(),
                    context_before=before,
                    context_after=after,
                )
            )

    for match in _YAML_IMAGE.finditer(text):
        line_no = text[: match.start()].count("\n") + 1
        img_path = match.group(1)
        before, after = context(line_no - 1)
        refs.append(
            ImageRef(
                source_file=rel,
                line_number=line_no,
                alt_text="",
                image_path=img_path,
                match_line=match.group(0).strip(),
                context_before=before,
                context_after=after,
            )
        )

    return refs


def collect_candidates(
    *,
    min_confidence: Confidence | None = None,
    use_ocr: bool = True,
) -> list[ImageRef]:
    order = {"high": 3, "medium": 2, "low": 1}
    min_rank = order[min_confidence] if min_confidence else 0

    candidates: list[ImageRef] = []
    seen: set[tuple[str, int, str]] = set()

    for file_path in iter_english_files():
        for ref in extract_refs_from_file(file_path):
            key = (ref.source_file, ref.line_number, ref.normalized_path())
            if key in seen:
                continue
            seen.add(key)

            ocr_text = ""
            if use_ocr:
                disk = resolve_image_on_disk(ref.normalized_path())
                if disk:
                    ocr_text = try_ocr(disk)

            score_candidate(ref, ocr_text)
            if order[ref.confidence] >= min_rank and ref.reasons:
                candidates.append(ref)

    candidates.sort(
        key=lambda r: (-order[r.confidence], r.source_file, r.line_number),
    )
    return candidates


def pr_title(count: int) -> str:
    return f"{PR_TITLE_PREFIX} Remove {count} redundant image references from English docs"


def print_summary(candidates: list[ImageRef]) -> None:
    by_conf: dict[str, int] = {"high": 0, "medium": 0, "low": 0}
    for c in candidates:
        by_conf[c.confidence] += 1

    print(f"Redundant image candidates: {len(candidates)}")
    print(f"  high:   {by_conf['high']}")
    print(f"  medium: {by_conf['medium']}")
    print(f"  low:    {by_conf['low']}")
    print()
    print("English scan roots:", ", ".join(ENGLISH_SCAN_DIRS))
    print(f"PR title prefix: {PR_TITLE_PREFIX}")
    print(f"PR label: {PR_LABEL}")


def write_csv(path: Path, candidates: list[ImageRef]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "confidence",
                "reasons",
                "source_file",
                "line_number",
                "image_path",
                "alt_text",
                "ocr_snippet",
                "match_line",
            ]
        )
        for ref in candidates:
            writer.writerow(
                [
                    ref.confidence,
                    ";".join(ref.reasons),
                    ref.source_file,
                    ref.line_number,
                    ref.normalized_path(),
                    ref.alt_text,
                    ref.ocr_snippet,
                    ref.match_line,
                ]
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        help="Write candidates to CSV",
    )
    parser.add_argument(
        "--min-confidence",
        choices=("high", "medium", "low"),
        default="medium",
        help="Minimum confidence to include (default: medium)",
    )
    parser.add_argument(
        "--no-ocr",
        action="store_true",
        help="Skip Tesseract OCR (faster; filename/alt heuristics only)",
    )
    args = parser.parse_args()

    candidates = collect_candidates(
        min_confidence=args.min_confidence,
        use_ocr=not args.no_ocr,
    )
    print_summary(candidates)

    if args.csv:
        write_csv(args.csv, candidates)
        print(f"Wrote {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
