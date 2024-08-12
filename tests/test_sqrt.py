#!/usr/bin/env python3
""""tester module for the square root"""
import unittest
from operations.sqrt import sqrt


class TestSqrt(unittest.TestCase):
    """class with method testers"""
    def test_sqrt(self):
        """method to test square root outputs"""
        self.assertEqual(sqrt(25), 5, "should be 5")
        self.assertEqual(sqrt(144), 12, "should be 12")
    
    def test_sqrt_negatives(self):
        """method to test square root for negative input"""
        self.assertEqual(sqrt(-12), ValueError, "input should be positive")
    
    def test_invalid_inputs(self):
        self.assertRaises(ValueError, sqrt, ["Hello", "3"])


if __name__ == "__main__":
    unittest.main()
