import unittest
from isTriangle import Triangle

class mutationAdequateTest(unittest.TestCase):

    def test_mutation_1(self):
        # Test the mutated condition in Mutation #34
        # In this case, (a - b <= c) is True
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)

# if __name__ == '__main__':
#     unittest.main()
