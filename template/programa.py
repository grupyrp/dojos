#!/usr/bin/env python

import unittest


class ProgramaTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_False(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
