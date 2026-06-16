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

    def test_allows_documented_example_name_pairs(self) -> None:
        text = 'Preview rows Alex Smith and Yuri Kim subscribed'
        violations = scan_text('assets/img/example.png', text)
        self.assertFalse(any(v.violation_type == 'person_name' for v in violations))

    def test_flags_external_id_header_and_numeric_ids(self) -> None:
        text = (
            'File preview Ext_Id Name Subscribe 42004428 Jordan opted_in '
            '42004430 Casey unsubscribed 42004437 Morgan subscribed'
        )
        violations = scan_text('assets/img/csv_import/preview.png', text)
        types = {v.violation_type for v in violations}
        self.assertIn('external_id_header', types)
        self.assertIn('numeric_user_id', types)

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
