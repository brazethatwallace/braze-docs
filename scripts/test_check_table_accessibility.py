#!/usr/bin/env python3
"""
Tests for check_table_accessibility.py.

Run with:
    python3 -m pytest scripts/test_check_table_accessibility.py -v
"""

import textwrap
import pytest
from check_table_accessibility import (
    check_file,
    build_skip_mask,
    check_html_tables,
    check_markdown_tables,
    find_html_table_tag,
    INLINE_CODE_RE,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def violations_for(content: str) -> list:
    """Return violations for an in-memory markdown string (no file I/O)."""
    lines = content.splitlines(keepends=True)
    # ensure trailing newline so last-line edge cases work
    if lines and not lines[-1].endswith('\n'):
        lines[-1] += '\n'
    skip = build_skip_mask(lines)
    return check_html_tables(lines, skip, '<test>') + check_markdown_tables(lines, skip, '<test>')


# ---------------------------------------------------------------------------
# find_html_table_tag — unit tests for the inline-code guard
# ---------------------------------------------------------------------------

class TestFindHtmlTableTag:
    def test_bare_tag_outside_code_matches(self):
        assert find_html_table_tag('<table>') is not None

    def test_tag_with_attrs_outside_code_matches(self):
        assert find_html_table_tag('<table class="foo">') is not None

    def test_tag_in_single_backtick_span_ignored(self):
        assert find_html_table_tag('Use `<table>` for data.') is None

    def test_tag_with_attrs_in_single_backtick_span_ignored(self):
        line = 'Does not apply to `<table aria-label="x">` alone.'
        assert find_html_table_tag(line) is None

    def test_tag_in_double_backtick_span_ignored(self):
        assert find_html_table_tag('See ``<table>`` for details.') is None

    def test_tag_in_triple_backtick_span_ignored(self):
        assert find_html_table_tag('See ```<table>``` for details.') is None

    def test_real_tag_after_inline_code_ref_matches(self):
        line = 'Mention `<table>` here, real <table class="data"> follows.'
        m = find_html_table_tag(line)
        assert m is not None
        assert 'data' in m.group(0)

    def test_case_insensitive(self):
        assert find_html_table_tag('<TABLE>') is not None
        assert find_html_table_tag('`<TABLE>`') is None

    def test_mismatched_open_double_close_single_is_real_html(self):
        """``<table>` is not a valid CommonMark code span — must not be skipped."""
        assert find_html_table_tag('``<table>`') is not None

    def test_mismatched_open_single_close_double_is_real_html(self):
        """`<table>`` is not a valid CommonMark code span — must not be skipped."""
        assert find_html_table_tag('`<table>``') is not None

    def test_mismatched_open_triple_close_single_is_real_html(self):
        assert find_html_table_tag('```<table>`') is not None

    def test_matched_double_backtick_span_ignored(self):
        assert find_html_table_tag('See ``<table>`` for the pattern.') is None

    def test_matched_triple_backtick_span_ignored(self):
        assert find_html_table_tag('See ```<table>``` for the pattern.') is None


# ---------------------------------------------------------------------------
# HTML table violations
# ---------------------------------------------------------------------------

class TestHtmlTableViolations:
    def test_html_table_no_label_triggers(self):
        md = '<table>\n<tr><td>a</td></tr>\n</table>\n'
        assert len(violations_for(md)) == 1

    def test_html_table_with_aria_label_passes(self):
        md = '<table aria-label="My table">\n<tr><td>a</td></tr>\n</table>\n'
        assert violations_for(md) == []

    def test_html_table_with_aria_labelledby_passes(self):
        md = '<table aria-labelledby="heading-id">\n<tr><td>a</td></tr>\n</table>\n'
        assert violations_for(md) == []

    def test_html_table_with_role_presentation_passes(self):
        md = '<table role="presentation">\n<tr><td>a</td></tr>\n</table>\n'
        assert violations_for(md) == []

    def test_html_table_with_caption_passes(self):
        md = '<table>\n<caption>My caption</caption>\n<tr><td>a</td></tr>\n</table>\n'
        assert violations_for(md) == []

    def test_inline_code_table_name_does_not_trigger(self):
        """Prose mentioning `<table>` must never be a violation."""
        md = 'Set the gradient on the cell instead of only on the `<table>`.\n'
        assert violations_for(md) == []

    def test_inline_code_table_with_attrs_does_not_trigger(self):
        md = 'Does not apply to `<table aria-label="Gmail dark mode">` elements alone.\n'
        assert violations_for(md) == []

    def test_html_table_inside_fenced_code_block_passes(self):
        md = textwrap.dedent("""\
            ```html
            <table>
            <tr><td>a</td></tr>
            </table>
            ```
        """)
        assert violations_for(md) == []

    def test_violation_message_mentions_html_table(self):
        md = '<table>\n<tr><td>a</td></tr>\n</table>\n'
        v = violations_for(md)
        assert 'HTML' in v[0]['message'] or 'table' in v[0]['message'].lower()


# ---------------------------------------------------------------------------
# Markdown (GFM) table violations
# ---------------------------------------------------------------------------

class TestMarkdownTableViolations:
    def test_gfm_table_no_ial_triggers(self):
        md = textwrap.dedent("""\
            | A | B |
            |---|---|
            | 1 | 2 |
        """)
        assert len(violations_for(md)) == 1

    def test_gfm_table_with_aria_label_ial_passes(self):
        md = textwrap.dedent("""\
            | A | B |
            |---|---|
            | 1 | 2 |
            {: .reset-td-br-1 .reset-td-br-2 aria-label="My table" }
        """)
        assert violations_for(md) == []

    def test_gfm_table_with_role_presentation_ial_passes(self):
        md = textwrap.dedent("""\
            | A | B |
            |---|---|
            | 1 | 2 |
            {: role="presentation" }
        """)
        assert violations_for(md) == []

    def test_gfm_table_bare_ial_triggers(self):
        """IAL present but missing aria-label and no presentation role."""
        md = textwrap.dedent("""\
            | A | B |
            |---|---|
            | 1 | 2 |
            {: .reset-td-br-1 }
        """)
        assert len(violations_for(md)) == 1

    def test_gfm_table_inside_fenced_code_block_passes(self):
        md = textwrap.dedent("""\
            ```
            | A | B |
            |---|---|
            | 1 | 2 |
            ```
        """)
        assert violations_for(md) == []

    def test_gfm_table_inside_liquid_raw_block_passes(self):
        md = textwrap.dedent("""\
            {% raw %}
            | A | B |
            |---|---|
            | 1 | 2 |
            {% endraw %}
        """)
        assert violations_for(md) == []

    def test_no_false_positive_on_pipe_in_prose(self):
        """A lone pipe in prose must not be treated as a table."""
        md = 'Use `a | b` for union types.\n'
        assert violations_for(md) == []

    def test_suggestion_contains_aria_label(self):
        md = textwrap.dedent("""\
            | A | B |
            |---|---|
            | 1 | 2 |
        """)
        v = violations_for(md)
        assert 'aria-label' in v[0]['suggestion_content']
