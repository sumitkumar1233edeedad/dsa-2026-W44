import unittest
from typing import List

# The function productExceptSelf is defined in the solution_code above.

class TestProductExceptSelf(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_example3(self):
        nums = [2, 3, 4, 5]
        expected = [60, 40, 30, 24]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_two_elements(self):
        nums = [5, 7]
        expected = [7, 5]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_with_zeros(self):
        nums = [0, 0, 1, 2]
        expected = [0, 0, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_negative_numbers(self):
        nums = [-2, -3, -4]
        expected = [12, 8, 6]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_large_array(self):
        # Use an array where product fits in 32-bit integer (all 1s)
        nums = [1] * 100000
        expected = [1] * 100000
        self.assertEqual(productExceptSelf(nums), expected)

if __name__ == '__main__':
    unittest.main()
