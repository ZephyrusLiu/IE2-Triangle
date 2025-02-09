import unittest
from isTriangle import Triangle

class mutationAdequateTest(unittest.TestCase):

    def test_invalid(self):
        # Test invalid triangle
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        
        self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, -1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, -1), Triangle.Type.INVALID)
        
        self.assertEqual(Triangle.classify(1, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 1), Triangle.Type.INVALID)
        
        self.assertEqual(Triangle.classify(3, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 3, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 3), Triangle.Type.INVALID)
        
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 3, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 2, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 3, 1), Triangle.Type.INVALID)

    def test_scalene(self):
        # Test scalene triangle
        self.assertEqual(Triangle.classify(2, 3, 4), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(5, 6, 7), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(5, 12, 13), Triangle.Type.SCALENE)

    def test_equilateral(self):
        # Test equilateral triangle
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)
        
    def test_isosceles(self):
        # Test isosceles triangle
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 4, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)
                
        self.assertEqual(Triangle.classify(3, 3, 1), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 1, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(1, 3, 3), Triangle.Type.ISOSCELES)

if __name__ == '__main__':
    unittest.main()