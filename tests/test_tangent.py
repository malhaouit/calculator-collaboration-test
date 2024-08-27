import unittest
import math
from operations.tangent import tangent

class TestCalculateTangent(unittest.TestCase):
    def test_positive_number(self):
        result = tangent(math.pi/4)
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_negative_number(self):
        result = tangent(-math.pi/3)
        self.assertAlmostEqual(result, -math.sqrt(3), places=2)

    def test_zero(self):
        result = tangent(0)
        self.assertAlmostEqual(result, 0.0, places=2)

if __name__ == '__main__':
    unittest.main()