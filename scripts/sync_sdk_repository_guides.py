#!/usr/bin/env python3
"""
Sync SDK repository guide pages from public GitHub README files.

This script keeps docs pages in sync with upstream SDK repository READMEs.
It injects generated README content between stable markers, removes the large
Braze logo block from the top of README content, and appends a repository link
line at the end of each page.

Usage:
  python scripts/sync_sdk_repository_guides.py --check
  python scripts/sync_sdk_repository_guides.py --write
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import urlparse
from urllib.request import Request, urlopen


BEGIN_MARKER = "<!-- BEGIN GENERATED README CONTENT -->"
END_MARKER = "<!-- END GENERATED README CONTENT -->"
REPO_FOOTER = "For repository details and sample projects, see [{repo_url}]({repo_url})."


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


REPO_GUIDES: List[RepoGuide] = [
    RepoGuide(
        slug="web",
        nav_title="Web SDK",
        article_title="Web SDK repository guide",
        page_order=1,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-web-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="android",
        nav_title="Android SDK",
        article_title="Android SDK repository guide",
        page_order=2,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-android-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="swift",
        nav_title="Swift SDK",
        article_title="Swift SDK repository guide",
        page_order=3,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-swift-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="javascript",
        nav_title="JavaScript SDK",
        article_title="JavaScript SDK repository guide",
        page_order=4,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-javascript-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="cordova",
        nav_title="Cordova SDK",
        article_title="Cordova SDK repository guide",
        page_order=5,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-cordova-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="flutter",
        nav_title="Flutter SDK",
        article_title="Flutter SDK repository guide",
        page_order=6,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-flutter-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="react_native",
        nav_title="React Native SDK",
        article_title="React Native SDK repository guide",
        page_order=7,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-react-native-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="roku",
        nav_title="Roku SDK",
        article_title="Roku SDK repository guide",
        page_order=8,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-roku-sdk",
        branch="main",
    ),
    RepoGuide(
        slug="unity",
        nav_title="Unity SDK",
        article_title="Unity SDK repository guide",
        page_order=9,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-unity-sdk",
        branch="master",
    ),
    RepoGuide(
        slug="xamarin",
        nav_title=".NET MAUI (Xamarin) SDK",
        article_title=".NET MAUI (Xamarin) SDK repository guide",
        page_order=10,
        description="Braze Android SDK README",
        owner="braze-inc",
        repo="braze-xamarin-sdk",
        branch="master",
    ),
]


def fetch_readme(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "braze-docs-sync-bot/1.0",
            "Accept": "text/plain",
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def is_external_or_anchor(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme in {"http", "https", "mailto", "tel", "data"}:
        return True
    if url.startswith("//") or url.startswith("#"):
        return True
    return False


def normalize_relative_url(url: str, guide: RepoGuide, is_image: bool) -> str:
    if is_external_or_anchor(url):
        return url

    parsed = urlparse(url)
    path = parsed.path
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""
    query = f"?{parsed.query}" if parsed.query else ""

    # README is always in repository root.
    clean_path = path.lstrip("/")
    if path.startswith("./"):
        clean_path = path[2:]
    if clean_path == "":
        return url

    if is_image:
        return f"{guide.raw_base}/{clean_path}{query}{fragment}"
    return f"{guide.blob_base}/{clean_path}{query}{fragment}"


def normalize_markdown_links(content: str, guide: RepoGuide) -> str:
    # Markdown images: ![alt](url)
    def image_repl(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        link = match.group(2).strip()
        normalized = normalize_relative_url(link, guide, is_image=True)
        return f"![{alt_text}]({normalized})"

    # Markdown links: [text](url)
    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        link = match.group(2).strip()
        normalized = normalize_relative_url(link, guide, is_image=False)
        return f"[{label}]({normalized})"

    content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image_repl, content)
    content = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", link_repl, content)
    return content


def normalize_html_asset_urls(content: str, guide: RepoGuide) -> str:
    # HTML image/link tags occasionally appear in README files.
    def src_repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        url = match.group(2)
        normalized = normalize_relative_url(url, guide, is_image=True)
        return f'src={quote}{normalized}{quote}'

    def href_repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        url = match.group(2)
        normalized = normalize_relative_url(url, guide, is_image=False)
        return f'href={quote}{normalized}{quote}'

    content = re.sub(r'src=(["\'])([^"\']+)\1', src_repl, content)
    content = re.sub(r'href=(["\'])([^"\']+)\1', href_repl, content)
    return content


def strip_top_braze_logo_block(content: str) -> str:
    # Remove centered HTML logo blocks that many SDK READMEs place before H1.
    html_logo_pattern = re.compile(
        r"^\s*<p[^>]*align=['\"]center['\"][^>]*>[\s\S]*?</p>\s*",
        re.IGNORECASE,
    )
    while True:
        match = html_logo_pattern.match(content)
        if match is None:
            break
        block = match.group(0)
        if "braze logo" in block.lower() or "logo-light" in block.lower() or "braze-logo" in block.lower():
            content = content[match.end():]
            continue
        break

    # Remove top single-line markdown/html logo image lines if present.
    single_logo_line_pattern = re.compile(
        r"^\s*(?:!\[[^\]]*braze logo[^\]]*\]\([^)]+\)|<img[^>]*(?:braze-logo|braze logo|logo-light)[^>]*>)\s*\n?",
        re.IGNORECASE,
    )
    while True:
        match = single_logo_line_pattern.match(content)
        if match is None:
            break
        content = content[match.end():]

    return content.lstrip("\n")


def normalize_markdown_constructs(content: str) -> str:
    # Some upstream READMEs use invalid closing break tags that render as text.
    content = content.replace("</br>", "<br/>")

    # Convert Setext headings to ATX headings so parsing is stable after HTML comments.
    lines = content.split("\n")
    converted: List[str] = []
    i = 0
    while i < len(lines):
        if i + 1 < len(lines):
            title = lines[i].rstrip()
            underline = lines[i + 1].strip()
            is_setext_h1 = len(underline) >= 3 and all(ch == "=" for ch in underline)
            is_setext_h2 = len(underline) >= 3 and all(ch == "-" for ch in underline)
            if (is_setext_h1 or is_setext_h2) and title and "|" not in title:
                if is_setext_h1:
                    converted.append(f"# {title}")
                else:
                    converted.append(f"## {title}")
                i += 2
                continue
        converted.append(lines[i])
        i += 1

    return "\n".join(converted)


def normalize_content(content: str, guide: RepoGuide) -> str:
    normalized = content.replace("\r\n", "\n")
    normalized = strip_top_braze_logo_block(normalized)
    normalized = normalize_markdown_constructs(normalized)
    normalized = normalize_markdown_links(normalized, guide)
    normalized = normalize_html_asset_urls(normalized, guide)
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


def build_page_content(guide: RepoGuide, readme_body: str) -> str:
    front_matter = build_front_matter(guide)
    footer = REPO_FOOTER.format(repo_url=guide.repo_url)
    return (
        f"{front_matter}\n"
        f"{BEGIN_MARKER}\n"
        f"{readme_body}"
        f"{END_MARKER}\n\n"
        f"{footer}\n"
    )


def sync(repo_root: Path, write: bool) -> int:
    changed = 0

    for guide in REPO_GUIDES:
        readme = fetch_readme(guide.raw_readme_url)
        normalized = normalize_content(readme, guide)
        expected = build_page_content(guide, normalized)
        destination = output_path(repo_root, guide.slug)

        current = destination.read_text(encoding="utf-8") if destination.exists() else ""
        if current != expected:
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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    changed = sync(repo_root, write=args.write)

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
