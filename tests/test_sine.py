#!/usr/bin/env python3
"""
Unit tests for the sine function in the operations module.
"""
import unittest
from operations.sine import sine


class TestSineFunction(unittest.TestCase):
    """
    Unit tests for the sine function in the operations module.
    """
    def test_sine(self):
        """
        Test the sine function with various angles in degrees to ensure
        that the sine function returns the correct results
        """
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(90), 1)
        self.assertAlmostEqual(sine(180), 0)
        self.assertAlmostEqual(sine(270), -1)
        self.assertAlmostEqual(sine(30), 0.5)
        self.assertAlmostEqual(sine(45), 0.7071, places=4)


if __name__ == '__main__':
    unittest.main()
