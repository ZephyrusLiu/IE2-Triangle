import unittest
from isTriangle import Triangle  # Import triangle from isTriangle.py

class DecisionCoverageTest(unittest.TestCase):

    def test_invalid(self):
        # Test invalid triangle
        # Invalid case: < 0
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        
        # Invalid case: a + b <= c or a + c <= b or b + c <= a
        self.assertEqual(Triangle.classify(1, 1, 2), Triangle.Type.INVALID)

    def test_scalene(self):
        # Test scalene triangle
        self.assertEqual(Triangle.classify(2, 3, 4), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(5, 6, 7), Triangle.Type.SCALENE)

    def test_equilateral(self):
        # Test equilateral triangle
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)
        
        
    def test_isosceles(self):
        # Test isosceles triangle
        # To test all cases, we need different case: a=b, a=c, b=c, once a time.
        # trian == 1 and a + b > c
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        # trian == 2 and a + c > b
        self.assertEqual(Triangle.classify(3, 4, 3), Triangle.Type.ISOSCELES)
        # trian == 3 and b + c > a
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)

if __name__ == '__main__':
    unittest.main()
