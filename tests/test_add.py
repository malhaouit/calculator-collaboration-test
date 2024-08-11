#!/usr/bin/env python3
""" Add Module Tests
"""

import unittest

from operations.add import add


class TestAdd(unittest.TestCase):
    """ Add Module Test Cases
    """

    def test_add_positive_numbers(self):
        res = add(1, 2)
        self.assertEqual(res, 3)

    def test_add_negetive_numbers(self):
        res = add(-1, -2)
        self.assertEqual(res, -3)

    def test_add_positive_and_negetive_number(self):
        res = add(-1, 2)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
