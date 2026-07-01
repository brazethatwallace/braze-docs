#!/usr/bin/env python3
"""
Tests for check_content_accessibility.py.

Run with:
    python3 -m pytest scripts/test_check_content_accessibility.py -v
"""

import textwrap

from check_content_accessibility import (
    build_skip_mask,
    check_spatial_directionals,
)


def spatial_violations_for(content: str) -> list:
    lines = content.splitlines(keepends=True)
    if lines and not lines[-1].endswith('\n'):
        lines[-1] += '\n'
    skip = build_skip_mask(lines)
    return check_spatial_directionals(lines, skip, '<test>')


class TestSpatialDirectionals:
    def test_flags_above_reference(self):
        v = spatial_violations_for('See the operators above for details.\n')
        assert len(v) == 1
        assert v[0]['violation_type'] == 'spatial_directional'
        assert v[0]['wcag_criterion'] == '1.3.3'

    def test_flags_below_reference(self):
        v = spatial_violations_for('Follow the steps below to configure filters.\n')
        assert len(v) == 1

    def test_flags_to_the_left(self):
        v = spatial_violations_for('Choose the option to the left of Save.\n')
        assert len(v) == 1

    def test_allows_below_input_field(self):
        v = spatial_violations_for(
            'Enter a value below the input field to filter results.\n'
        )
        assert v == []

    def test_allows_above_threshold(self):
        v = spatial_violations_for('Matches values above the threshold.\n')
        assert v == []

    def test_allows_below_threshold(self):
        v = spatial_violations_for('This selection returns items below the threshold.\n')
        assert v == []

    def test_flags_spatial_above_when_threshold_phrase_is_separate(self):
        v = spatial_violations_for(
            'values above the threshold; see the table above\n'
        )
        assert len(v) == 1
        assert 'above' in v[0]['message']

    def test_allows_left_to_right(self):
        v = spatial_violations_for(
            'Body alignment can follow left-to-right text on each line.\n'
        )
        assert v == []

    def test_allows_bi_directional(self):
        v = spatial_violations_for('Many users write bi-directional text.\n')
        assert v == []

    def test_skips_fenced_code_blocks(self):
        content = textwrap.dedent('''\
            ```text
            See the table below.
            ```
            Safe line without directionals.
        ''')
        v = spatial_violations_for(content)
        assert v == []

    def test_uses_section_name_fix_hint(self):
        v = spatial_violations_for('Use the table below.\n')
        assert 'section heading' in v[0]['fix_hint']
