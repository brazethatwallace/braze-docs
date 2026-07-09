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


def spatial_violations_for_path(content: str, path: str) -> list:
    lines = content.splitlines(keepends=True)
    if lines and not lines[-1].endswith('\n'):
        lines[-1] += '\n'
    skip = build_skip_mask(lines)
    return check_spatial_directionals(lines, skip, path)


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

    def test_allows_above_allotment_numeric_comparison(self):
        v = spatial_violations_for(
            'Requests above that allotment still send but are not covered by SLA.\n'
        )
        assert v == []

    def test_allows_below_campaign_subgrouping(self):
        v = spatial_violations_for(
            'Identifier for an optional sub-grouping below campaign and ad group.\n'
        )
        assert v == []

    def test_allows_directional_language_inside_image_alt_text(self):
        v = spatial_violations_for(
            '![The chart on the left shows baseline and the chart on the right shows treatment.](/img/chart.png)\n'
        )
        assert v == []

    def test_allows_standalone_css_declaration_line(self):
        v = spatial_violations_for('transform-origin: top right;\n')
        assert v == []

    def test_allows_left_and_right_side_of_string(self):
        v = spatial_violations_for(
            'Strips tabs, spaces, and newlines from the left and right side of a string.\n'
        )
        assert v == []

    def test_allows_left_side_of_string(self):
        v = spatial_violations_for(
            'Strips tabs and spaces from the left side of a string.\n'
        )
        assert v == []

    def test_allows_right_side_of_string(self):
        v = spatial_violations_for(
            'Strips tabs and spaces from the right side of a string.\n'
        )
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
        assert v[0]['auto_fix_eligible'] is True

    def test_marks_cla_spatial_violations_as_manual_review_only(self):
        v = spatial_violations_for_path(
            'Select one of the options below and sign as indicated.\n',
            '_docs/_docs_pages/cla.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is False

    def test_marks_legal_segment_paths_as_manual_review_only(self):
        v = spatial_violations_for_path(
            'Read the terms below before continuing.\n',
            '_docs/legal/terms_of_service.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is False

    def test_marks_docs_pages_legal_filenames_as_manual_review_only(self):
        v = spatial_violations_for_path(
            'The details are listed below.\n',
            '_docs/_docs_pages/privacy_policy.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is False

    def test_marks_docs_pages_tokenized_legal_stem_as_manual_review_only(self):
        v = spatial_violations_for_path(
            'The details are listed below.\n',
            '_docs/_docs_pages/privacy-overview.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is False

    def test_marks_api_data_retention_as_manual_review_only(self):
        v = spatial_violations_for_path(
            'The details are listed below.\n',
            '_docs/_api/data_retention.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is False

    def test_does_not_treat_terms_to_know_as_legal_sensitive(self):
        v = spatial_violations_for_path(
            'Review the list below before setup.\n',
            '_docs/_user_guide/get_started/terms_to_know.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is True

    def test_does_not_treat_docs_pages_classification_as_legal_sensitive(self):
        v = spatial_violations_for_path(
            'See details below.\n',
            '_docs/_docs_pages/classification.md',
        )
        assert len(v) == 1
        assert v[0]['auto_fix_eligible'] is True

    def test_allows_below_a_certain_threshold_numeric_comparison(self):
        v = spatial_violations_for(
            'If the value drops below a certain threshold, throttle requests.\n'
        )
        assert v == []

    def test_allows_at_or_below_variant_limit(self):
        v = spatial_violations_for(
            'Re-activate variants as long as this keeps the component at or below the five-variant limit.\n'
        )
        assert v == []

    def test_allows_above_average_phrase(self):
        v = spatial_violations_for(
            'Users with above-average recency are grouped in this segment.\n'
        )
        assert v == []

    def test_allows_above_and_beyond_idiom(self):
        v = spatial_violations_for(
            'Our support team goes above and beyond for onboarding.\n'
        )
        assert v == []

    def test_allows_left_center_right_alignment_options(self):
        v = spatial_violations_for(
            'Orients the image to either the left, center, or right of the block.\n'
        )
        assert v == []

    # ------------------------------------------------------------------
    # False-positive guard: "right" / "left" meaning "correct" or other
    # non-directional uses that the old bare-word regex incorrectly flagged
    # ------------------------------------------------------------------

    def test_allows_right_users(self):
        """'right users' means 'correct users', not a spatial reference."""
        v = spatial_violations_for('Make sure you target the right users.\n')
        assert v == []

    def test_allows_right_approach(self):
        v = spatial_violations_for('Choose the right approach for your use case.\n')
        assert v == []

    def test_allows_right_api_key(self):
        v = spatial_violations_for('Verify the SDK is configured with the right API key and endpoint.\n')
        assert v == []

    def test_allows_right_message_right_person(self):
        v = spatial_violations_for(
            'Send the right message to the right person at the right time.\n'
        )
        assert v == []

    def test_allows_right_now(self):
        v = spatial_violations_for('Refresh the page right now to apply changes.\n')
        assert v == []

    def test_allows_css_float_right(self):
        """'float:right' in an inline style attribute is CSS, not a spatial instruction."""
        v = spatial_violations_for(
            '{: style="float:right;max-width:30%;margin-left:15px;"}\n'
        )
        assert v == []

    def test_allows_margin_left_css(self):
        v = spatial_violations_for(
            '![SDK overview]({% image_buster /assets/img/sdk_overview.png %})'
            '{: style="max-width:40%;float:right;margin-left:15px;"}\n'
        )
        assert v == []

    def test_allows_left_as_past_tense(self):
        """'left' as past tense of 'leave' (e.g. cart abandonment) is not directional."""
        v = spatial_violations_for(
            'Users who abandoned their cart and left the cart value at more than $50.\n'
        )
        assert v == []

    def test_allows_right_to_left_text_direction(self):
        v = spatial_violations_for(
            'For right-to-left languages, use the RTL configuration option.\n'
        )
        assert v == []

    # ------------------------------------------------------------------
    # True-positive coverage: spatial UI references that must still flag
    # ------------------------------------------------------------------

    def test_flags_right_side(self):
        v = spatial_violations_for('Select the option on the right side of the screen.\n')
        assert len(v) == 1

    def test_flags_left_panel(self):
        v = spatial_violations_for('In the left panel, select Settings.\n')
        assert len(v) == 1

    def test_flags_left_sidebar(self):
        v = spatial_violations_for('Click the icon in the left sidebar.\n')
        assert len(v) == 1

    def test_flags_upper_right(self):
        v = spatial_violations_for('Click the icon in the upper right corner.\n')
        assert len(v) == 1

    def test_flags_top_left_hyphenated(self):
        """Hyphenated 'top-left' is a UI position reference and must be flagged."""
        v = spatial_violations_for("Click the icon at the top-left of the panel.\n")
        assert len(v) == 1

    def test_flags_top_right_of(self):
        v = spatial_violations_for('Select the indicator at the top right of the app.\n')
        assert len(v) == 1

    def test_flags_bottom_left(self):
        v = spatial_violations_for('The button appears at the bottom-left of the modal.\n')
        assert len(v) == 1

    def test_flags_left_of(self):
        v = spatial_violations_for('Select the icon to the left of the title.\n')
        assert len(v) == 1

    def test_flags_right_of_button(self):
        v = spatial_violations_for('Choose the icon to the right of the button.\n')
        assert len(v) == 1

    def test_flags_right_hand_side(self):
        v = spatial_violations_for('The settings appear on the right-hand side.\n')
        assert len(v) == 1
