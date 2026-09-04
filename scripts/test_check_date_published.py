#!/usr/bin/env python3
"""Unit tests for date_published enforcement.

Run from the repository root:

    python3 scripts/test_check_date_published.py
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date, timedelta
from io import StringIO
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_date_published import (
    DiffEntry,
    HOMEPAGE_WINDOW_DAYS,
    SCOPE_PREFIXES,
    collect_findings,
    emit_github_annotations,
    evaluate_change,
    in_scope,
    main,
    parse_frontmatter,
    parse_iso_date,
    parse_name_status_line,
)

TODAY = date(2026, 8, 25)
TODAY_ISO = '2026-08-25'
YESTERDAY_ISO = '2026-08-24'
FUTURE_ISO = '2026-08-28'
OLD_ISO = '2026-01-01'
WINDOW_EDGE_ISO = (TODAY - timedelta(days=HOMEPAGE_WINDOW_DAYS)).isoformat()
OUTSIDE_WINDOW_ISO = (TODAY - timedelta(days=HOMEPAGE_WINDOW_DAYS + 1)).isoformat()

ARTICLE = """\
---
nav_title: Example
article_title: Example article
page_order: 1
page_type: reference
description: "An example article."
{extra}---

# Example
"""

LANDING = """\
---
nav_title: Example
article_title: Example
page_order: 1
layout: dev_guide
guide_featured_list:
  - name: One
    link: /docs/user_guide/one/
    image: /assets/img/one.png
---

# Example
"""

PATH = '_docs/_user_guide/example.md'


def article(**fields: str) -> str:
    extra = ''.join(f'{key}: {value}\n' for key, value in fields.items())
    return ARTICLE.format(extra=extra)


def evaluate(
    head: str,
    base: str | None = None,
    *,
    path: str = PATH,
    base_path: str | None = None,
) -> object:
    return evaluate_change(
        head_path=path,
        head_text=head,
        base_path=base_path if base_path is not None else (path if base is not None else None),
        base_text=base,
        today=TODAY,
    )


class ScopeTests(unittest.TestCase):
    def test_core_collections_are_in_scope(self) -> None:
        for prefix in SCOPE_PREFIXES:
            self.assertTrue(in_scope(f'{prefix}page.md'))

    def test_other_trees_are_out_of_scope(self) -> None:
        for path in (
            '_docs/_home/home.md',
            '_docs/_releases/2026/1.md',
            '_docs/_hidden/archived.md',
            '_includes/foo.md',
            '_lang/es/_user_guide/page.md',
            '_docs/_user_guide/page.html',
        ):
            self.assertFalse(in_scope(path), path)


class FrontmatterTests(unittest.TestCase):
    def test_reads_quoted_and_boolean_keys(self) -> None:
        fm = parse_frontmatter(
            article(hidden='true', date_published='"2026-07-10"')
        )
        self.assertTrue(fm.exists)
        self.assertEqual(fm.values['hidden'], 'true')
        self.assertEqual(fm.values['date_published'], '2026-07-10')
        self.assertEqual(fm.key_lines['date_published'], 8)

    def test_missing_frontmatter(self) -> None:
        fm = parse_frontmatter('# Just a heading\n')
        self.assertFalse(fm.exists)

    def test_invalid_calendar_date_is_not_parsed(self) -> None:
        self.assertIsNone(parse_iso_date('2026-02-30'))


class Check1NewFileTests(unittest.TestCase):
    def test_missing_field_fails(self) -> None:
        finding = evaluate(article())
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'missing')
        self.assertTrue((finding.suggested_replacement or '').startswith('---\n'))
        self.assertIn(TODAY_ISO, finding.suggested_replacement or '')

    def test_missing_field_inserts_after_opening_delimiter(self) -> None:
        finding = evaluate(LANDING)
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.suggested_original, '---')
        self.assertEqual(
            finding.suggested_replacement,
            f'---\ndate_published: "{TODAY_ISO}"',
        )
        self.assertNotIn('guide_featured_list', finding.suggested_replacement or '')

    def test_todays_date_passes(self) -> None:
        self.assertIsNone(evaluate(article(date_published=f'"{TODAY_ISO}"')))

    def test_future_date_passes(self) -> None:
        self.assertIsNone(evaluate(article(date_published=f'"{FUTURE_ISO}"')))

    def test_yesterdays_date_fails_as_stale(self) -> None:
        finding = evaluate(article(date_published=f'"{YESTERDAY_ISO}"'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'stale')
        self.assertEqual(finding.expected_date, TODAY_ISO)

    def test_malformed_date_fails(self) -> None:
        finding = evaluate(article(date_published='"August 25, 2026"'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'malformed')

    def test_invalid_calendar_date_fails_as_malformed(self) -> None:
        finding = evaluate(article(date_published='"2026-02-30"'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'malformed')

    def test_hidden_new_file_is_exempt(self) -> None:
        self.assertIsNone(evaluate(article(hidden='true')))

    def test_hidden_yes_is_exempt(self) -> None:
        self.assertIsNone(evaluate(article(hidden='yes')))

    def test_config_only_on_is_exempt(self) -> None:
        self.assertIsNone(evaluate(article(config_only='on')))

    def test_config_only_new_file_is_exempt(self) -> None:
        self.assertIsNone(evaluate(article(config_only='true')))

    def test_redirect_new_file_is_exempt(self) -> None:
        self.assertIsNone(evaluate(article(layout='redirect')))

    def test_out_of_scope_new_file_is_ignored(self) -> None:
        self.assertIsNone(
            evaluate(article(), path='_docs/_releases/2026/note.md')
        )


class Check1UnhideTests(unittest.TestCase):
    def test_unhide_without_date_fails(self) -> None:
        finding = evaluate(article(), base=article(hidden='true'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'missing')

    def test_unhide_with_today_passes(self) -> None:
        self.assertIsNone(
            evaluate(
                article(date_published=f'"{TODAY_ISO}"'),
                base=article(hidden='true'),
            )
        )

    def test_unhide_keeps_existing_date(self) -> None:
        self.assertIsNone(
            evaluate(
                article(date_published=f'"{OLD_ISO}"'),
                base=article(hidden='true', date_published=f'"{OLD_ISO}"'),
            )
        )

    def test_unhide_must_not_change_existing_date(self) -> None:
        finding = evaluate(
            article(date_published=f'"{TODAY_ISO}"'),
            base=article(hidden='true', date_published=f'"{OLD_ISO}"'),
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'modified')
        self.assertEqual(finding.expected_date, OLD_ISO)

    def test_leaving_config_only_requires_date(self) -> None:
        finding = evaluate(article(), base=article(config_only='true'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'missing')

    def test_leaving_config_only_keeps_existing_date(self) -> None:
        self.assertIsNone(
            evaluate(
                article(date_published=f'"{OLD_ISO}"'),
                base=article(config_only='true', date_published=f'"{OLD_ISO}"'),
            )
        )


class Check2ImmutabilityTests(unittest.TestCase):
    def test_existing_value_must_not_change(self) -> None:
        finding = evaluate(
            article(date_published='"2026-07-10"'),
            base=article(date_published='"2026-06-01"'),
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'modified')
        self.assertEqual(finding.expected_date, '2026-06-01')

    def test_existing_value_unchanged_passes(self) -> None:
        body = article(date_published='"2026-06-01"')
        self.assertIsNone(evaluate(body, base=body))

    def test_removing_existing_value_fails(self) -> None:
        finding = evaluate(article(), base=article(date_published='"2026-06-01"'))
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'modified')

    def test_rename_preserves_date(self) -> None:
        finding = evaluate(
            article(date_published='"2026-07-10"'),
            base=article(date_published='"2026-06-01"'),
            path='_docs/_user_guide/new_name.md',
            base_path='_docs/_user_guide/old_name.md',
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'modified')


class NoBackfillTests(unittest.TestCase):
    def test_existing_public_file_without_field_is_ignored(self) -> None:
        body = article()
        self.assertIsNone(evaluate(body, base=body))

    def test_adding_old_date_to_existing_public_is_allowed(self) -> None:
        self.assertIsNone(
            evaluate(
                article(date_published=f'"{OUTSIDE_WINDOW_ISO}"'),
                base=article(),
            )
        )

    def test_adding_today_to_existing_public_is_rejected(self) -> None:
        finding = evaluate(
            article(date_published=f'"{TODAY_ISO}"'),
            base=article(),
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'recency')

    def test_adding_future_date_to_existing_public_is_rejected(self) -> None:
        finding = evaluate(
            article(date_published=f'"{FUTURE_ISO}"'),
            base=article(),
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'recency')

    def test_adding_window_edge_date_to_existing_public_is_rejected(self) -> None:
        finding = evaluate(
            article(date_published=f'"{WINDOW_EDGE_ISO}"'),
            base=article(),
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'recency')

    def test_adding_empty_date_to_existing_public_is_rejected(self) -> None:
        finding = evaluate(article(date_published='""'), base=article())
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'malformed')

    def test_rename_of_old_file_without_field_is_ignored(self) -> None:
        self.assertIsNone(
            evaluate(
                article(),
                base=article(),
                path='_docs/_user_guide/new_name.md',
                base_path='_docs/_user_guide/old_name.md',
            )
        )

    def test_move_from_hidden_collection_is_first_ship(self) -> None:
        finding = evaluate(
            article(),
            base=article(),
            path='_docs/_user_guide/page.md',
            base_path='_docs/_hidden/page.md',
        )
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.code, 'missing')


class DiffParseTests(unittest.TestCase):
    def test_added(self) -> None:
        entry = parse_name_status_line('A\t_docs/_user_guide/new.md')
        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual(entry.status, 'A')
        self.assertIsNone(entry.base_path)

    def test_modified(self) -> None:
        entry = parse_name_status_line('M\t_docs/_user_guide/page.md')
        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual(entry.status, 'M')
        self.assertEqual(entry.base_path, '_docs/_user_guide/page.md')
        self.assertEqual(entry.head_path, '_docs/_user_guide/page.md')

    def test_renamed(self) -> None:
        entry = parse_name_status_line(
            'R100\t_docs/_user_guide/old.md\t_docs/_user_guide/new.md'
        )
        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual(entry.status, 'R')
        self.assertEqual(entry.base_path, '_docs/_user_guide/old.md')
        self.assertEqual(entry.head_path, '_docs/_user_guide/new.md')

    def test_copy_treated_as_add(self) -> None:
        entry = parse_name_status_line(
            'C80\t_docs/_user_guide/old.md\t_docs/_user_guide/copy.md'
        )
        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual(entry.status, 'A')
        self.assertIsNone(entry.base_path)


class CollectFindingsTests(unittest.TestCase):
    def test_added_file_missing_date(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = '_docs/_user_guide/example.md'
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(article(), encoding='utf-8')
            with (
                patch(
                    'check_date_published.git_merge_base',
                    return_value='abc123',
                ),
                patch(
                    'check_date_published.git_diff_entries',
                    return_value=[DiffEntry('A', rel, None)],
                ),
                patch('check_date_published.git_show') as show,
            ):
                findings = collect_findings(
                    root=root, base='origin/develop', today=TODAY
                )
            show.assert_not_called()
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, 'missing')

    def test_modified_file_uses_merge_base_blob(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = '_docs/_user_guide/example.md'
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(
                article(date_published='"2026-07-10"'), encoding='utf-8'
            )
            with (
                patch(
                    'check_date_published.git_merge_base',
                    return_value='mergebase',
                ),
                patch(
                    'check_date_published.git_diff_entries',
                    return_value=[DiffEntry('M', rel, rel)],
                ),
                patch(
                    'check_date_published.git_show',
                    return_value=article(date_published='"2026-06-01"'),
                ) as show,
            ):
                findings = collect_findings(
                    root=root, base='origin/develop', today=TODAY
                )
            show.assert_called_once_with(root, 'mergebase', rel)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, 'modified')

    def test_git_show_error_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = '_docs/_user_guide/example.md'
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(article(), encoding='utf-8')
            with (
                patch(
                    'check_date_published.git_merge_base',
                    return_value='mergebase',
                ),
                patch(
                    'check_date_published.git_diff_entries',
                    return_value=[DiffEntry('M', rel, rel)],
                ),
                patch(
                    'check_date_published.git_show',
                    side_effect=RuntimeError('git show failed'),
                ),
            ):
                with self.assertRaises(RuntimeError):
                    collect_findings(
                        root=root, base='origin/develop', today=TODAY
                    )


class MainTests(unittest.TestCase):
    def test_missing_base_returns_2(self) -> None:
        self.assertEqual(main([]), 2)

    def test_annotations_missing_file_returns_2(self) -> None:
        self.assertEqual(
            main(['--github-annotations', '/tmp/does-not-exist-date-published.json']),
            2,
        )

    def test_json_output_writes_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'findings.json'
            with patch(
                'check_date_published.collect_findings',
                return_value=[],
            ), patch('check_date_published.git_repo_root', return_value=Path(tmp)):
                self.assertEqual(
                    main(['--base', 'origin/develop', '--json', str(out), '--today', TODAY_ISO]),
                    0,
                )
            self.assertEqual(json.loads(out.read_text(encoding='utf-8')), [])


class AnnotationTests(unittest.TestCase):
    def test_emits_error_annotations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'findings.json'
            path.write_text(
                json.dumps(
                    [
                        {
                            'file': PATH,
                            'code': 'missing',
                            'message': 'Add date_published',
                            'line': 7,
                        }
                    ]
                ),
                encoding='utf-8',
            )
            with patch('sys.stdout', new=StringIO()) as stdout:
                self.assertEqual(emit_github_annotations(str(path)), 0)
                self.assertIn('::error file=_docs/_user_guide/example.md,line=7', stdout.getvalue())

    def test_malformed_json_returns_2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'findings.json'
            path.write_text('{not json', encoding='utf-8')
            self.assertEqual(emit_github_annotations(str(path)), 2)


if __name__ == '__main__':
    unittest.main()
