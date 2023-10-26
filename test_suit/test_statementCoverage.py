import unittest
from isTriangle import Triangle  # Import triangle from isTriangle.py

class StatementCoverageTest(unittest.TestCase):

    def test_invalid(self):
        # Test invalid triangle
        # Invalid case: < 0
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)

    def test_scalene(self):
        # Test scalene triangle
        self.assertEqual(Triangle.classify(2, 3, 4), Triangle.Type.SCALENE)

    def test_equilateral(self):
        # Test equilateral triangle
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        # Test isosceles triangle
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
