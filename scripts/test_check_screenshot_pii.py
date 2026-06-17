#!/usr/bin/env python3
"""Unit tests for screenshot PII pattern matching (no OCR required)."""

import unittest

from check_screenshot_pii import active_violations, scan_text


class ScanTextTests(unittest.TestCase):
    def test_flags_single_names_when_name_column_present(self) -> None:
        text = (
            'File preview Ext_Id Name Name_Last Subscribe 42004428 Jordan opted_in '
            '42004430 Casey unsubscribed 42004437 Morgan subscribed'
        )
        violations = scan_text('assets/img/csv_import/preview.png', text)
        singles = {v.match for v in violations if v.violation_type == 'person_name_single'}
        self.assertIn('Jordan', singles)
        self.assertIn('Casey', singles)
        self.assertIn('Morgan', singles)

    def test_ignores_single_names_without_name_column(self) -> None:
        text = 'File preview Ext_Id Subscribe 42004428 Jordan opted_in 42004430 Casey'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name_single' for v in violations))

    def test_single_name_not_duplicated_when_part_of_pair(self) -> None:
        text = 'Name Name_Last Jordan Miller Casey Higgins'
        violations = scan_text('assets/img/example.png', text)
        pairs = {v.match for v in violations if v.violation_type == 'person_name'}
        singles = {v.match for v in violations if v.violation_type == 'person_name_single'}
        self.assertIn('Jordan Miller', pairs)
        self.assertNotIn('Jordan', singles)
        self.assertNotIn('Miller', singles)

    def test_ignores_create_ui_label_as_person_name(self) -> None:
        text = 'Name Name_Last Create targeting filter Create segment'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name_single' for v in violations))

    def test_flags_person_name_pairs(self) -> None:
        text = (
            'File preview Name Name_Last Subscribe a82415 Jordan Miller opted_in '
            'a71902 Casey Higgins unsubscribed a94328 Morgan Peterson'
        )
        violations = scan_text('assets/img/csv_import/preview.png', text)
        names = {v.match for v in violations if v.violation_type == 'person_name'}
        self.assertIn('Jordan Miller', names)
        self.assertIn('Casey Higgins', names)
        self.assertIn('Morgan Peterson', names)

    def test_ignores_ui_phrases_for_name_detection(self) -> None:
        text = 'File Preview Column Mapping Import Settings Browse Files Start Import'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name' for v in violations))

    def test_ignores_nav_labels_without_name_context(self) -> None:
        text = 'Help Center Dark Mode Feature Requests Shortcuts Changelog Connected Apps'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name' for v in violations))

    def test_ignores_ui_labels_near_external_id_without_name_column(self) -> None:
        text = 'Help Center Select Trigger Ext_Id Subscribe opted_in'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name' for v in violations))

    def test_still_flags_names_with_name_column_context(self) -> None:
        text = 'Help Center Name Name_Last Jordan Miller Casey Higgins'
        violations = scan_text('assets/img/csv_import/preview.png', text)
        names = {v.match for v in violations if v.violation_type == 'person_name'}
        self.assertIn('Jordan Miller', names)
        self.assertNotIn('Help Center', names)

    def test_ignores_komo_and_partner_ui_labels(self) -> None:
        ui_labels = [
            'Pages Publish',
            'Help Center',
            'Shortcuts Changelog',
            'Feature Requests',
            'Dark Mode',
            'Connected Apps',
            'Company Members',
            'Audit Log',
            'Vii Integrate',
            'Prize Awarded',
            'React Flow',
            'Steps Variables',
            'Saved Trigger',
            'Unified Contacts',
            'Pos Eshop',
            'Datawarehouse Identity',
            'Cleansing Computed',
        ]
        for label in ui_labels:
            with self.subTest(label=label):
                text = f'Name Name_Last Navigation {label} Settings'
                violations = scan_text('assets/img/example.png', text)
                flagged = {v.match for v in violations if v.violation_type == 'person_name'}
                self.assertNotIn(label, flagged)

    def test_ignores_ui_capitalized_words_in_name_columns(self) -> None:
        text = 'Name Name_Last Subscribe Status Segment Canvas Trigger Filter'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name_single' for v in violations))

    def test_allows_documented_example_name_pairs(self) -> None:
        text = 'Preview rows Alex Smith and Yuri Kim subscribed'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name' for v in violations))

    def test_ignores_example_pair_last_names_in_name_columns(self) -> None:
        text = 'Name Name_Last Alex Smith Yuri Kim subscribed'
        violations = scan_text('assets/img/example.png', text)
        singles = {v.match for v in violations if v.violation_type == 'person_name_single'}
        self.assertNotIn('Smith', singles)
        self.assertNotIn('Kim', singles)

    def test_flags_substring_example_domain_emails(self) -> None:
        text = 'Contact user@badexample.com or user@myexample.community for help'
        violations = scan_text('assets/img/example.png', text)
        flagged = {v.match for v in violations if v.violation_type == 'email_address'}
        self.assertIn('user@badexample.com', flagged)
        self.assertIn('user@myexample.community', flagged)

    def test_flags_emails_on_domains_that_prefix_example_placeholders(self) -> None:
        """Domains like example.community must not be skipped by naive example.* lookahead."""
        text = (
            'Reach user@example.community or user@example.com.br or '
            'user@example.org.uk for details'
        )
        violations = scan_text('assets/img/example.png', text)
        flagged = {v.match for v in violations if v.violation_type == 'email_address'}
        self.assertIn('user@example.community', flagged)
        self.assertIn('user@example.com.br', flagged)
        self.assertIn('user@example.org.uk', flagged)

    def test_allows_exact_example_domain_emails(self) -> None:
        text = 'Contact alex@example.com and lee@example.org for help'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'email_address' for v in violations))

    def test_flags_numeric_ids_when_external_id_column_present(self) -> None:
        text = (
            'File preview Ext_Id Name Subscribe 42004428 Jordan opted_in '
            '42004430 Casey unsubscribed 42004437 Morgan subscribed'
        )
        violations = scan_text('assets/img/csv_import/preview.png', text)
        types = {v.violation_type for v in violations}
        self.assertIn('numeric_user_id', types)

    def test_does_not_flag_external_id_labels_without_values(self) -> None:
        text = (
            'Destination mapping Source field external_id Target external id '
            'Ext Id column schema'
        )
        violations = scan_text('assets/img/mapping/example.png', text)
        types = {v.violation_type for v in violations}
        self.assertNotIn('numeric_user_id', types)
        self.assertNotIn('alphanumeric_external_id', types)

    def test_flags_alphanumeric_external_ids(self) -> None:
        text = 'Preview a82415 Jordan Miller opted_in a71902 Casey Higgins'
        violations = scan_text('assets/img/example.png', text)
        types = {v.violation_type for v in violations}
        self.assertIn('alphanumeric_external_id', types)

    def test_flags_customer_attribute_names(self) -> None:
        text = 'Marketing_Transactor_Flag OptIn_Email_Art_News OptIn_DM_Auction_Updates'
        violations = scan_text('assets/img/example.png', text)
        self.assertTrue(any(v.violation_type == 'customer_attribute_name' for v in violations))

    def test_flags_production_csv_filename(self) -> None:
        text = 'Upload completed user_updates_03_04.csv Total attributes detected 18'
        violations = scan_text('assets/img/example.png', text)
        self.assertTrue(any(v.violation_type == 'production_csv_filename' for v in violations))

    def test_allows_example_email(self) -> None:
        text = 'Contact alex@example.com for help'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'email_address' for v in violations))

    def test_flags_real_email(self) -> None:
        text = 'Contact wallace.lee@braze.com for help'
        violations = scan_text('assets/img/example.png', text)
        self.assertTrue(any(v.violation_type == 'email_address' for v in violations))

    def test_dismissed_violations_are_inactive(self) -> None:
        text = 'Marketing_Transactor_Flag OptIn_Email_Art_News'
        violations = scan_text('assets/img/example.png', text)
        for v in violations:
            v.dismissed = True
        self.assertEqual(active_violations(violations), [])


if __name__ == '__main__':
    unittest.main()
