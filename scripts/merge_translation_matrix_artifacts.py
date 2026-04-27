#!/usr/bin/env python3
"""Merge per-locale GitHub Actions matrix artifacts into the repo workspace.

Each matrix cell uploads ``translation_results.json``, ``qc_results.json``, and
``_lang/<locale_dir>/``. The workflow downloads them under one directory; this
script walks it (via ``rglob``), merges JSON, and overlays ``_lang/`` so a
single PR can ship all locales.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "usage: merge_translation_matrix_artifacts.py <artifact-root>",
            file=sys.stderr,
        )
        sys.exit(1)
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)

    combined: dict = {"translated": [], "failed": [], "skipped": []}
    chunked_by_src: dict[str, dict] = {}
    build_results: dict = {"passed": [], "fixed": [], "failed": []}
    findings: list = []

    seen_tr: set[Path] = set()
    for trp in sorted(root.rglob("translation_results.json")):
        key = trp.resolve()
        if key in seen_tr:
            continue
        seen_tr.add(key)

        data = json.loads(trp.read_text(encoding="utf-8"))
        combined["translated"].extend(data.get("translated", []))
        combined["failed"].extend(data.get("failed", []))
        combined["skipped"].extend(data.get("skipped", []))
        for c in data.get("chunked", []):
            src = c.get("source")
            if src:
                chunked_by_src[str(src)] = c
        br = data.get("build_results") or {}
        for k in ("passed", "fixed"):
            for lg in br.get(k, []):
                if lg not in build_results[k]:
                    build_results[k].append(lg)
        for item in br.get("failed", []):
            build_results["failed"].append(item)

    for qcp in sorted(root.rglob("qc_results.json")):
        data = json.loads(qcp.read_text(encoding="utf-8"))
        findings.extend(data.get("findings", []))

    for lang_root in sorted(root.rglob("_lang")):
        if not lang_root.is_dir() or lang_root.name != "_lang":
            continue
        dest_root = REPO_ROOT / "_lang"
        dest_root.mkdir(parents=True, exist_ok=True)
        try:
            children = list(lang_root.iterdir())
        except OSError:
            continue
        for lang_dir in children:
            if lang_dir.is_dir():
                shutil.copytree(
                    lang_dir, dest_root / lang_dir.name, dirs_exist_ok=True
                )

    if not seen_tr:
        print(
            "No translation_results.json found under artifact root.",
            file=sys.stderr,
        )
        sys.exit(1)

    combined["chunked"] = list(chunked_by_src.values())
    combined["build_results"] = build_results
    (REPO_ROOT / "translation_results.json").write_text(
        json.dumps(combined, indent=2),
        encoding="utf-8",
    )

    total_repairs = sum(len(f.get("repairs") or []) for f in findings)
    total_warnings = sum(len(f.get("warnings") or []) for f in findings)
    qc_out = {
        "total_files": len(combined["translated"]),
        "files_with_issues": len(findings),
        "total_repairs": total_repairs,
        "total_warnings": total_warnings,
        "findings": findings,
    }
    (REPO_ROOT / "qc_results.json").write_text(
        json.dumps(qc_out, indent=2),
        encoding="utf-8",
    )

    print(
        f"Merged {len(seen_tr)} locale result file(s): "
        f"{len(combined['translated'])} translated paths; "
        f"_lang written under {REPO_ROOT / '_lang'}",
    )


if __name__ == "__main__":
    main()
