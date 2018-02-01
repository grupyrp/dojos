#!/usr/bin/env python

import re
import unittest
from datetime import datetime


# [YYYY-mm-dd H:i:s] - Abertura da Porta OK


class DoorCheckTestCase(unittest.TestCase):
    def test_valid_entry(self):
        entry = "[2018-02-01 13:00:00] - Abertura da Porta OK"
        self.assertTrue(validate_entry(entry))

    def test_invalid_entry_string(self):
        entry = "Cebola"
        self.assertFalse(validate_entry(entry))

    def test_valid_entry_date_single_digit_month(self):
        entry = "[2018-2-03 13:00:00] - Abertura da Porta OK"
        self.assertTrue(validate_entry(entry))

    def test_invalid_entry_date(self):
        entry = "[2018-02-33 13:00:00] - Abertura da Porta OK"
        self.assertFalse(validate_entry(entry))

    def test_valid_entry_period(self):
        entry = "[2018-02-25 15:59:01] - Abertura da Porta OK"
        self.assertTrue(validate_entry(entry))

    def test_invalid_entry_period(self):
        entry = "[2018-02-25 16:00:00] - Abertura da Porta OK"
        self.assertFalse(validate_entry(entry))

    def test_invalid_entry_empty_braces(self):
        entry = "[] - Abertura da Porta OK"
        self.assertFalse(validate_entry(entry))

    def test_check_log_quantity(self):
        entries = [
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 19:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 20:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[2018-02-01 10:00:00] - Abertura da Porta OK',
            '[] - Abertura da Porta OK',
        ]
        self.assertEqual(qty_entries(entries), 8)


def qty_entries(entries):
    return len(list(filter(validate_entry, entries)))


def validate_entry(entry):
    zeit = re.findall(r'^\[(.*)\] - Abertura da Porta OK$', entry)

    try:
        d_time = datetime.strptime(zeit[0], '%Y-%m-%d %H:%M:%S')
    except (ValueError, IndexError):
        return False

    if d_time.hour in range(10, 16):
        return True

    return False


if __name__ == '__main__':
    unittest.main()
