#!/usr/bin/env python3
"""
Test division module
"""

import unittest
from operations.divide import division


class TestDivision(unittest.TestCase):
    def test_float_division(self):
        # Test floating-point division
        self.assertAlmostEqual(division(10, 2), 5.0)
        self.assertAlmostEqual(division(7, 3), 7/3)
        self.assertAlmostEqual(division(10.5, 2), 5.25)

    def test_integer_division(self):
        # Test integer division
        self.assertEqual(division(10, 3, 'integer'), 10 // 3)
        self.assertEqual(division(7, 2, 'integer'), 7 // 2)

    def test_division_by_zero(self):
        # Test division by zero for all operations
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)
        with self.assertRaises(ZeroDivisionError):
            division(10, 0, 'integer')

    def test_invalid_operation(self):
        # Test with an invalid operation type
        with self.assertRaises(ValueError):
            division(10, 3, 'invalid')


if __name__ == '__main__':
    unittest.main()