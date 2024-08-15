#!/usr/bin/env python3
"""Factorial Module Tests"""

import unittest
from operations.factorial import factorial


class TestFactorial(unittest.TestCase):
    """Factorial Module Test Cases"""

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_performance_large_inputs(self):
        import time
        start_time = time.time()
        factorial(100)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1,
                        "Performance test failed: took too long.")


if __name__ == '__main__':
    unittest.main()
