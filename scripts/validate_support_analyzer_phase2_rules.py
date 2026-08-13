#!/usr/bin/env python3
"""
Validate `.github/support_analyzer_phase2_rules.yml` for CI.

Checks rule structure, regex compilation, `_docs/` path allowlisting, target file
existence, and anchor substrings on the current checkout. Does not open PRs.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from support_analyzer_phase2 import (
    _RULE_ID_RE,
    _edit_already_applied,
    _ensure_case_pattern_cache,
    _load_rules,
    _validate_docs_relative_path,
    _validate_rule_edit_paths,
)

_VALID_MATCH_MODES = frozenset({"all_of", "any_of"})


def validate_rules_doc(*, root: Path, rules: list[dict[str, Any]]) -> list[str]:
    """Return human-readable validation errors (empty when valid)."""
    errors: list[str] = []
    seen_ids: set[str] = set()

    for index, rule in enumerate(rules):
        ctx = f"rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{ctx}: expected a mapping")
            continue

        rid = rule.get("id")
        if not isinstance(rid, str) or not rid.strip():
            errors.append(f"{ctx}: missing or empty id")
            continue
        rid = rid.strip()
        ctx = f"rule {rid!r}"
        if rid in seen_ids:
            errors.append(f"{ctx}: duplicate rule id")
        seen_ids.add(rid)

        if not _RULE_ID_RE.match(rid):
            errors.append(
                f"{ctx}: invalid id for git branch names "
                "(use letters, digits, hyphens, underscores; 1–128 chars)"
            )

        enabled = rule.get("enabled", True)
        if not isinstance(enabled, bool):
            errors.append(f"{ctx}: enabled must be a boolean when set")

        min_n = rule.get("min_matching_cases", 1)
        if not isinstance(min_n, int) or min_n < 1:
            errors.append(f"{ctx}: min_matching_cases must be a positive integer")

        case_cfg = rule.get("case_text")
        if not isinstance(case_cfg, dict):
            errors.append(f"{ctx}: case_text must be a mapping")
        else:
            fields = case_cfg.get("fields")
            if not isinstance(fields, list) or not fields:
                errors.append(f"{ctx}: case_text.fields must be a non-empty list")
            elif not all(isinstance(f, str) and f.strip() for f in fields):
                errors.append(f"{ctx}: case_text.fields must be non-empty strings")

            patterns = case_cfg.get("patterns")
            if not isinstance(patterns, list) or not patterns:
                errors.append(f"{ctx}: case_text.patterns must be a non-empty list")
            else:
                mode = (case_cfg.get("match_mode") or "all_of").lower()
                if mode not in _VALID_MATCH_MODES:
                    errors.append(
                        f"{ctx}: case_text.match_mode must be one of "
                        f"{sorted(_VALID_MATCH_MODES)} (got {mode!r})"
                    )
                for pi, pattern in enumerate(patterns):
                    if not isinstance(pattern, str) or not pattern.strip():
                        errors.append(f"{ctx}: case_text.patterns[{pi}] must be a non-empty string")
                try:
                    _ensure_case_pattern_cache(rule)
                except re.error as exc:
                    errors.append(f"{ctx}: invalid regex in case_text.patterns: {exc}")

        edits = rule.get("edits")
        if edits is None:
            errors.append(f"{ctx}: edits must be present")
        elif not isinstance(edits, list):
            errors.append(f"{ctx}: edits must be a list")
        elif enabled and not edits:
            errors.append(f"{ctx}: enabled rules must include at least one edit")
        else:
            try:
                _validate_rule_edit_paths(rule, rid)
            except SystemExit as exc:
                errors.append(str(exc))

            for ei, edit in enumerate(edits):
                if not isinstance(edit, dict):
                    errors.append(f"{ctx}: edits[{ei}] must be a mapping")
                    continue
                ectx = f"{ctx} edits[{ei}]"
                anchor = edit.get("anchor_substring")
                insert = edit.get("insert")
                rel = edit.get("file")
                if not rel:
                    errors.append(f"{ectx}: missing file")
                    continue
                if not isinstance(anchor, str) or not anchor.strip():
                    errors.append(f"{ectx}: missing anchor_substring")
                if not isinstance(insert, str) or not insert.strip():
                    errors.append(f"{ectx}: missing insert")

                try:
                    rel_norm = _validate_docs_relative_path(str(rel), context=ectx)
                except SystemExit as exc:
                    errors.append(str(exc))
                    continue

                path = root / rel_norm
                if not path.is_file():
                    errors.append(f"{ectx}: target file not found: {rel_norm}")
                    continue

                content = path.read_text(encoding="utf-8")
                if _edit_already_applied(content, edit, root=root):
                    continue
                anchor_text = (anchor or "").strip()
                if anchor_text and anchor_text not in content:
                    errors.append(
                        f"{ectx}: anchor_substring not found in {rel_norm} "
                        "(and edit is not already applied via skip_if_contains)"
                    )

        pr_cfg = rule.get("pr")
        if pr_cfg is not None and not isinstance(pr_cfg, dict):
            errors.append(f"{ctx}: pr must be a mapping when set")

        ver_cfg = rule.get("verification")
        if ver_cfg is not None:
            if not isinstance(ver_cfg, dict):
                errors.append(f"{ctx}: verification must be a mapping when set")
            else:
                checks = ver_cfg.get("checks")
                if checks is not None and not isinstance(checks, list):
                    errors.append(f"{ctx}: verification.checks must be a list when set")

    return errors


def main() -> None:
    p = argparse.ArgumentParser(description="Validate support_analyzer_phase2_rules.yml")
    p.add_argument(
        "--rules",
        default=".github/support_analyzer_phase2_rules.yml",
        help="Path to rules YAML",
    )
    p.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root (contains _docs)",
    )
    args = p.parse_args()

    root = args.root.resolve()
    rules_path = (root / args.rules).resolve() if not Path(args.rules).is_absolute() else Path(args.rules)
    if not rules_path.is_file():
        raise SystemExit(f"Rules not found: {rules_path}")

    rules_doc = _load_rules(rules_path)
    rules = rules_doc.get("rules")
    if not isinstance(rules, list):
        raise SystemExit("Rules file must include a top-level 'rules' list")

    errors = validate_rules_doc(root=root, rules=rules)
    if errors:
        print("Phase 2 rules validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        raise SystemExit(1)

    print(f"Phase 2 rules OK ({len(rules)} rule(s)) in {rules_path.relative_to(root)}")


if __name__ == "__main__":
    main()
