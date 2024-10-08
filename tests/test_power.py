#!/usr/bin/env python3
"""Multiplication Module Tests"""

import unittest

from operations.power import power


class TestPowerFunction(unittest.TestCase):
    def test_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(7, 0), 1)
    
    def test_zero_base(self):
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)
    
    def test_one_base(self):
        self.assertEqual(power(1, 100), 1)
    
    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(5, -3), 0.008, places=3)
        self.assertAlmostEqual(power(10, -1), 0.1)

if __name__ == "__main__":
    unittest.main()
