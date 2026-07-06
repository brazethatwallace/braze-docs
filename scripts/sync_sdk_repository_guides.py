#!/usr/bin/env python3
"""
Sync SDK repository guide pages from public GitHub README files.

The sync pipeline:
1. Fetches README.md from each mapped SDK repository.
2. Applies post-processing so content follows Braze docs conventions.
3. Writes deterministic pages under _docs/_developer_guide/sdk_repository_guides/.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence
from urllib.parse import urlparse
from urllib.request import Request, urlopen


BEGIN_MARKER = "<!-- BEGIN GENERATED README CONTENT -->"
END_MARKER = "<!-- END GENERATED README CONTENT -->"
REPO_FOOTER = "For repository details and sample projects, see [{repo_url}]({repo_url})."

SCRIPT_OR_STYLE_TAG_PATTERN = re.compile(r"<(script|style)\b[\s\S]*?</\1>", re.IGNORECASE)
EMPTY_CENTERED_PARAGRAPH_PATTERN = re.compile(
    r"<p[^>]*align=['\"]center['\"][^>]*>\s*</p>",
    re.IGNORECASE,
)
SETEXT_UNDERLINE_PATTERN = re.compile(r"^(?P<mark>[=-])\1{2,}\s*$")
SINGLE_LINE_LOGO_PATTERN = re.compile(
    r"^\s*(?:!\[[^\]]*braze logo[^\]]*\]\([^)]+\)|<img[^>]*(?:braze-logo|braze logo|logo-light)[^>]*>)\s*$",
    re.IGNORECASE,
)
HTML_LOGO_BLOCK_PATTERN = re.compile(
    r"^\s*<p[^>]*align=['\"]center['\"][^>]*>[\s\S]*?</p>\s*$",
    re.IGNORECASE,
)
MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HTML_SRC_PATTERN = re.compile(r'src=(["\'])([^"\']+)\1')
HTML_HREF_PATTERN = re.compile(r'href=(["\'])([^"\']+)\1')
GITHUB_ALERT_HEADER_PATTERN = re.compile(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING)\]\s*$", re.IGNORECASE)
COLON_ALERT_START_PATTERN = re.compile(r"^\s*:::\s*(note|tip|important|warning)\s*$", re.IGNORECASE)
COLON_ALERT_END_PATTERN = re.compile(r"^\s*:::\s*$")
BLOCKQUOTE_NOTE_PREFIX_PATTERN = re.compile(
    r"^\s*>\s*\*\*(Note|Tip|Important|Warning)\**:?\s*(.*)$",
    re.IGNORECASE,
)
MARKDOWN_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WARNING_HEADING_PATTERN = re.compile(
    r"^\s{0,3}#{2,6}\s*(?:⚠️?|:warning:)\s*(.+?)\s*(?:⚠️?)?\s*$",
    re.IGNORECASE,
)
IAL_RE = re.compile(r"^\s*\{:.*\}\s*$")
IAL_ARIA_LABEL_RE = re.compile(r"aria-label\s*=")
LAYOUT_ROLE_RE = re.compile(r'role\s*=\s*["\']?(presentation|none)["\']?', re.IGNORECASE)
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")
STRIP_MD_RE = re.compile(
    r"\[([^\]]+)\]\([^)]+\)|`([^`]+)`|\*\*([^*]+)\*\*|\*([^*]+)\*"
)
STRIP_EXTRA_RE = re.compile(r"[`*_{}<>]")

CODE_FENCE_LANGUAGE_ALIASES: Dict[str, str] = {
    "sh": "bash",
    "shell": "bash",
    "js": "javascript",
    "ts": "typescript",
    "yml": "yaml",
    "objectivec": "objc",
}


@dataclass(frozen=True)
class RepoGuide:
    slug: str
    nav_title: str
    article_title: str
    page_order: int
    description: str
    owner: str
    repo: str
    branch: str

    @property
    def repo_url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}"

    @property
    def raw_readme_url(self) -> str:
        return f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.branch}/README.md"

    @property
    def blob_base(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}/blob/{self.branch}"

    @property
    def raw_base(self) -> str:
        return f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.branch}"


REPO_GUIDES: Sequence[RepoGuide] = (
    RepoGuide(
        slug="web",
        nav_title="Web SDK",
        article_title="Web SDK repository guide",
        page_order=1,
        description="Braze Web SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-web-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="android",
        nav_title="Android SDK",
        article_title="Android SDK repository guide",
        page_order=2,
        description="Braze Android SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-android-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="swift",
        nav_title="Swift SDK",
        article_title="Swift SDK repository guide",
        page_order=3,
        description="Braze Swift SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-swift-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="javascript",
        nav_title="JavaScript SDK",
        article_title="JavaScript SDK repository guide",
        page_order=4,
        description="Braze JavaScript SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-javascript-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="cordova",
        nav_title="Cordova SDK",
        article_title="Cordova SDK repository guide",
        page_order=5,
        description="Braze Cordova SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-cordova-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="flutter",
        nav_title="Flutter SDK",
        article_title="Flutter SDK repository guide",
        page_order=6,
        description="Braze Flutter SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-flutter-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="react_native",
        nav_title="React Native SDK",
        article_title="React Native SDK repository guide",
        page_order=7,
        description="Braze React Native SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-react-native-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="roku",
        nav_title="Roku SDK",
        article_title="Roku SDK repository guide",
        page_order=8,
        description="Braze Roku SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-roku-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="unity",
        nav_title="Unity SDK",
        article_title="Unity SDK repository guide",
        page_order=9,
        description="Braze Unity SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-unity-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="xamarin",
        nav_title=".NET MAUI (Xamarin) SDK",
        article_title=".NET MAUI (Xamarin) SDK repository guide",
        page_order=10,
        description="Braze .NET MAUI (Xamarin) SDK README reference mirrored from GitHub.",
        owner="braze-inc",
        repo="braze-xamarin-sdk",
        branch="master",
    ),
)


def fetch_readme(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "braze-docs-sync-bot/2.0",
            "Accept": "text/plain",
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def is_external_or_anchor(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data"} or url.startswith("//") or url.startswith("#")


def normalize_relative_url(url: str, guide: RepoGuide, is_image: bool) -> str:
    if is_external_or_anchor(url):
        return url

    parsed = urlparse(url)
    path = parsed.path
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""
    query = f"?{parsed.query}" if parsed.query else ""

    clean_path = path.lstrip("/")
    if path.startswith("./"):
        clean_path = path[2:]
    if not clean_path:
        return url

    return f"{guide.raw_base if is_image else guide.blob_base}/{clean_path}{query}{fragment}"


def normalize_markdown_links(content: str, guide: RepoGuide) -> str:
    def image_repl(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        link = match.group(2).strip()
        return f"![{alt_text}]({normalize_relative_url(link, guide, is_image=True)})"

    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        link = match.group(2).strip()
        return f"[{label}]({normalize_relative_url(link, guide, is_image=False)})"

    content = MARKDOWN_IMAGE_PATTERN.sub(image_repl, content)
    return MARKDOWN_LINK_PATTERN.sub(link_repl, content)


def normalize_html_asset_urls(content: str, guide: RepoGuide) -> str:
    def src_repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        url = match.group(2)
        return f'src={quote}{normalize_relative_url(url, guide, is_image=True)}{quote}'

    def href_repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        url = match.group(2)
        return f'href={quote}{normalize_relative_url(url, guide, is_image=False)}{quote}'

    content = HTML_SRC_PATTERN.sub(src_repl, content)
    return HTML_HREF_PATTERN.sub(href_repl, content)


def strip_html_script_and_style_tags(content: str) -> str:
    # Dropping script/style tags reduces render overhead and avoids injecting third-party JS/CSS.
    return SCRIPT_OR_STYLE_TAG_PATTERN.sub("", content)


def convert_setext_to_atx_headings(content: str) -> str:
    lines = content.split("\n")
    converted: List[str] = []
    index = 0

    while index < len(lines):
        if index + 1 < len(lines):
            title = lines[index].rstrip()
            underline = lines[index + 1].strip()
            match = SETEXT_UNDERLINE_PATTERN.match(underline)
            if match and title and "|" not in title:
                marker = match.group("mark")
                converted.append(f"{'#' if marker == '=' else '##'} {title}")
                index += 2
                continue
        converted.append(lines[index])
        index += 1

    return "\n".join(converted)


def strip_top_logo_and_badges(content: str) -> str:
    lines = content.splitlines()
    stripped: List[str] = []
    heading_seen = False

    for line in lines:
        if not heading_seen and HTML_LOGO_BLOCK_PATTERN.match(line):
            lower = line.lower()
            if "braze logo" in lower or "logo-light" in lower or "braze-logo" in lower:
                continue
        if not heading_seen and SINGLE_LINE_LOGO_PATTERN.match(line):
            continue

        if not heading_seen and line.lstrip().startswith("# "):
            heading_seen = True
            line = re.sub(
                r"\[\s*!\[[^\]]*\]\([^)]*shields\.io[^)]*\)\s*\]\([^)]*\)",
                "",
                line,
            )
            line = re.sub(r"!\[[^\]]*\]\([^)]*shields\.io[^)]*\)", "", line)
            line = re.sub(r"\[\s*\]\([^)]*\)", "", line)
            line = re.sub(r"\s{2,}", " ", line)
        stripped.append(line)

    return "\n".join(stripped).lstrip("\n")


def strip_leading_h1(content: str) -> str:
    lines = content.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].lstrip().startswith("# "):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
    return "\n".join(lines)


def parse_markdown_heading(line: str) -> tuple[int, str] | None:
    match = MARKDOWN_HEADING_PATTERN.match(line.strip())
    if not match:
        return None
    return len(match.group(1)), match.group(2).strip().lower()


def remove_markdown_table_of_contents(content: str) -> str:
    lines = content.splitlines()
    filtered: List[str] = []
    index = 0
    toc_titles = {"table of contents", "contents", "toc"}

    while index < len(lines):
        heading = parse_markdown_heading(lines[index])
        if heading is None:
            filtered.append(lines[index])
            index += 1
            continue

        level, title = heading
        if title not in toc_titles:
            filtered.append(lines[index])
            index += 1
            continue

        index += 1
        while index < len(lines):
            next_heading = parse_markdown_heading(lines[index])
            if next_heading and next_heading[0] <= level:
                break
            index += 1

    return "\n".join(filtered)


def strip_readme_preamble_before_sections(content: str) -> str:
    lines = content.splitlines()
    for index, line in enumerate(lines):
        heading = parse_markdown_heading(line)
        if heading and heading[0] >= 2:
            return "\n".join(lines[index:])
    return content


def convert_warning_headings_to_liquid_alerts(content: str) -> str:
    lines = content.splitlines()
    converted: List[str] = []
    for line in lines:
        match = WARNING_HEADING_PATTERN.match(line)
        if match:
            warning_text = match.group(1).strip()
            if warning_text:
                converted.append("{% alert warning %}")
                converted.append(warning_text)
                converted.append("{% endalert %}")
                continue
        converted.append(line)
    return "\n".join(converted)


def build_standard_intro(guide: RepoGuide) -> str:
    sdk_name = guide.nav_title
    return (
        f"## About the Braze {sdk_name}\n\n"
        f"The Braze {sdk_name} helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.\n\n"
        "To get started, refer to the following resources:\n\n"
        "- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)\n"
        f"- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab={guide.slug})\n"
    )


def ensure_standard_intro(content: str, guide: RepoGuide) -> str:
    trimmed = content.lstrip()
    if trimmed.lower().startswith("## about the braze "):
        return trimmed
    return f"{build_standard_intro(guide)}\n{trimmed}"


def ensure_page_h1(content: str, guide: RepoGuide) -> str:
    trimmed = content.lstrip()
    expected_h1 = f"# {guide.article_title}"
    if trimmed.startswith(f"{expected_h1}\n") or trimmed == expected_h1:
        return trimmed
    return f"{expected_h1}\n\n{trimmed}"


def convert_github_alerts_to_liquid(content: str) -> str:
    lines = content.splitlines()
    converted: List[str] = []
    index = 0

    while index < len(lines):
        header_match = GITHUB_ALERT_HEADER_PATTERN.match(lines[index])
        if header_match:
            alert_type = header_match.group(1).lower()
            alert_lines: List[str] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate.startswith(">"):
                    alert_lines.append(re.sub(r"^\s*>\s?", "", candidate))
                    index += 1
                    continue
                if candidate.strip() == "":
                    alert_lines.append("")
                    index += 1
                    continue
                break

            while alert_lines and alert_lines[-1] == "":
                alert_lines.pop()

            converted.append(f"{{% alert {alert_type} %}}")
            converted.extend(alert_lines if alert_lines else [""])
            converted.append("{% endalert %}")
            continue

        converted.append(lines[index])
        index += 1

    return "\n".join(converted)


def convert_colon_alerts_to_liquid(content: str) -> str:
    lines = content.splitlines()
    converted: List[str] = []
    index = 0

    while index < len(lines):
        start_match = COLON_ALERT_START_PATTERN.match(lines[index])
        if not start_match:
            converted.append(lines[index])
            index += 1
            continue

        alert_type = start_match.group(1).lower()
        block_lines: List[str] = []
        index += 1
        while index < len(lines) and not COLON_ALERT_END_PATTERN.match(lines[index]):
            block_lines.append(lines[index])
            index += 1

        if index < len(lines):
            index += 1

        while block_lines and block_lines[-1] == "":
            block_lines.pop()

        converted.append(f"{{% alert {alert_type} %}}")
        converted.extend(block_lines if block_lines else [""])
        converted.append("{% endalert %}")

    return "\n".join(converted)


def convert_blockquote_prefixed_alerts(content: str) -> str:
    lines = content.splitlines()
    converted: List[str] = []
    index = 0

    while index < len(lines):
        match = BLOCKQUOTE_NOTE_PREFIX_PATTERN.match(lines[index])
        if not match:
            converted.append(lines[index])
            index += 1
            continue

        alert_type = match.group(1).lower()
        first_line = match.group(2).strip()
        alert_lines: List[str] = [first_line] if first_line else []
        index += 1
        while index < len(lines):
            candidate = lines[index]
            if candidate.startswith(">"):
                alert_lines.append(re.sub(r"^\s*>\s?", "", candidate))
                index += 1
                continue
            if candidate.strip() == "":
                alert_lines.append("")
                index += 1
                continue
            break

        while alert_lines and alert_lines[-1] == "":
            alert_lines.pop()

        converted.append(f"{{% alert {alert_type} %}}")
        converted.extend(alert_lines if alert_lines else [""])
        converted.append("{% endalert %}")

    return "\n".join(converted)


def normalize_code_fences(content: str) -> str:
    lines = content.splitlines()
    normalized: List[str] = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code_block:
                language = stripped[3:].strip().lower()
                if not language:
                    language = "text"
                language = CODE_FENCE_LANGUAGE_ALIASES.get(language, language)
                normalized.append(f"``` {language}")
            else:
                normalized.append("```")
            in_code_block = not in_code_block
            continue
        normalized.append(line)

    return "\n".join(normalized)


def build_skip_mask(lines: Sequence[str]) -> List[bool]:
    skip = [False] * len(lines)
    in_fence = False
    fence_marker = ""
    in_raw = False

    for index, line in enumerate(lines):
        stripped = line.strip()

        if not in_raw and "{% raw %}" in line:
            if "{% endraw %}" not in line:
                in_raw = True
                skip[index] = True
                continue
        elif in_raw:
            skip[index] = True
            if "{% endraw %}" in line:
                in_raw = False
            continue

        if not in_fence:
            match = re.match(r"^(`{3,}|~{3,})", stripped)
            if match:
                in_fence = True
                fence_marker = match.group(1)[0] * len(match.group(1))
                skip[index] = True
                continue
        else:
            skip[index] = True
            if re.match(r"^" + re.escape(fence_marker) + r"`*\s*$", stripped):
                in_fence = False
            continue

    return skip


def is_gfm_table_row(line: str) -> bool:
    return line.lstrip().startswith("|")


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    return bool(cells) and all(TABLE_SEPARATOR_CELL_RE.match(cell) for cell in cells if cell)


def clean_heading_for_label(raw_heading: str) -> str:
    heading = STRIP_MD_RE.sub(lambda match: next(group for group in match.groups() if group is not None), raw_heading)
    heading = STRIP_EXTRA_RE.sub("", heading).strip()
    heading = heading.replace('"', "'")
    return heading or "Table"


def nearest_heading_label(lines: Sequence[str], table_start_idx: int) -> str:
    for heading_idx in range(table_start_idx - 1, -1, -1):
        match = MARKDOWN_HEADING_PATTERN.match(lines[heading_idx].strip())
        if match:
            return clean_heading_for_label(match.group(2))
    return "Table"


def count_table_columns(lines: Sequence[str], table_start_idx: int, table_end_idx: int) -> int:
    for row_idx in range(table_start_idx, table_end_idx):
        row = lines[row_idx].strip()
        if row.startswith("|") and not is_table_separator(row):
            cells = [cell for cell in row.strip("|").split("|")]
            return max(1, len(cells))
    return 2


def make_table_ial(column_count: int, label: str) -> str:
    classes = " ".join(f".reset-td-br-{index}" for index in range(1, column_count + 1))
    return f'{{: {classes} aria-label="{label}" }}'


def add_accessible_names_to_tables(content: str) -> str:
    lines = content.splitlines()
    skip = build_skip_mask(lines)
    index = 0

    while index < len(lines):
        if skip[index] or not is_gfm_table_row(lines[index]):
            index += 1
            continue

        table_start = index
        has_separator = False
        while index < len(lines) and not skip[index] and is_gfm_table_row(lines[index]):
            if is_table_separator(lines[index]):
                has_separator = True
            index += 1
        table_end = index

        if not has_separator:
            continue

        label = nearest_heading_label(lines, table_start)
        column_count = count_table_columns(lines, table_start, table_end)
        ial_line = lines[table_end].strip() if table_end < len(lines) else ""
        new_ial = make_table_ial(column_count, label)

        if IAL_RE.match(ial_line):
            if not (IAL_ARIA_LABEL_RE.search(ial_line) or LAYOUT_ROLE_RE.search(ial_line)):
                lines[table_end] = new_ial
            continue

        lines.insert(table_end, new_ial)
        skip.insert(table_end, False)
        index = table_end + 1

    return "\n".join(lines)


def collapse_excess_blank_lines(content: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", content)


def apply_post_processing(content: str, guide: RepoGuide) -> str:
    normalized = content.replace("\r\n", "\n").replace("</br>", "<br/>")
    normalized = strip_html_script_and_style_tags(normalized)
    normalized = convert_setext_to_atx_headings(normalized)
    normalized = strip_top_logo_and_badges(normalized)
    normalized = EMPTY_CENTERED_PARAGRAPH_PATTERN.sub("", normalized)
    normalized = normalize_markdown_links(normalized, guide)
    normalized = normalize_html_asset_urls(normalized, guide)
    normalized = convert_github_alerts_to_liquid(normalized)
    normalized = convert_colon_alerts_to_liquid(normalized)
    normalized = convert_blockquote_prefixed_alerts(normalized)
    normalized = convert_warning_headings_to_liquid_alerts(normalized)
    normalized = normalize_code_fences(normalized)
    normalized = strip_leading_h1(normalized)
    normalized = remove_markdown_table_of_contents(normalized)
    normalized = strip_readme_preamble_before_sections(normalized)
    normalized = ensure_standard_intro(normalized, guide)
    normalized = ensure_page_h1(normalized, guide)
    normalized = add_accessible_names_to_tables(normalized)
    normalized = collapse_excess_blank_lines(normalized)
    return normalized.rstrip() + "\n"


def output_path(repo_root: Path, slug: str) -> Path:
    return repo_root / "_docs" / "_developer_guide" / "sdk_repository_guides" / f"{slug}.md"


def build_front_matter(guide: RepoGuide) -> str:
    return (
        "---\n"
        f"nav_title: {guide.nav_title}\n"
        f"article_title: {guide.article_title}\n"
        f"page_order: {guide.page_order}\n"
        f'description: "{guide.description}"\n'
        "---\n"
    )


def build_page_content(guide: RepoGuide, processed_readme: str) -> str:
    front_matter = build_front_matter(guide)
    footer = REPO_FOOTER.format(repo_url=guide.repo_url)
    return (
        f"{front_matter}\n"
        f"{BEGIN_MARKER}\n"
        f"{processed_readme}"
        f"{END_MARKER}\n\n"
        f"{footer}\n"
    )


def fetch_all_readmes(guides: Sequence[RepoGuide]) -> Dict[str, str]:
    readmes: Dict[str, str] = {}
    max_workers = min(8, len(guides))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(fetch_readme, guide.raw_readme_url): guide for guide in guides}
        for future in concurrent.futures.as_completed(future_map):
            guide = future_map[future]
            readmes[guide.slug] = future.result()
    return readmes


def selected_guides(slugs: Iterable[str] | None) -> Sequence[RepoGuide]:
    if slugs is None:
        return REPO_GUIDES

    slug_set = {slug.strip().lower() for slug in slugs if slug.strip()}
    selected = [guide for guide in REPO_GUIDES if guide.slug in slug_set]
    missing = sorted(slug_set - {guide.slug for guide in selected})
    if missing:
        raise ValueError(f"Unknown slug(s): {', '.join(missing)}")
    return selected


def sync(repo_root: Path, guides: Sequence[RepoGuide], write: bool) -> int:
    changed = 0
    readmes = fetch_all_readmes(guides)

    for guide in guides:
        processed = apply_post_processing(readmes[guide.slug], guide)
        expected = build_page_content(guide, processed)
        destination = output_path(repo_root, guide.slug)
        current = destination.read_text(encoding="utf-8") if destination.exists() else ""

        if current == expected:
            continue

        changed += 1
        print(f"Out of sync: {destination.relative_to(repo_root)}")
        if write:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(expected, encoding="utf-8")

    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync SDK repository guide pages.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Check whether pages are up-to-date.")
    mode.add_argument("--write", action="store_true", help="Write synced page content to disk.")
    parser.add_argument(
        "--repo",
        action="append",
        dest="repos",
        help="Optional repo guide slug to limit sync. Can be passed multiple times.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent

    try:
        guides = selected_guides(args.repos)
        changed = sync(repo_root, guides=guides, write=args.write)
    except Exception as error:  # pragma: no cover
        print(f"Sync failed: {error}", file=sys.stderr)
        return 2

    if args.write:
        print(f"Updated pages: {changed}")
        return 0

    if changed > 0:
        print(f"Out-of-date pages: {changed}")
        return 1

    print("All SDK repository guide pages are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
