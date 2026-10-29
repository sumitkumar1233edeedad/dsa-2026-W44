import unittest

class TestLongestSubarrayAtMostKDistinct(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([1, 2, 1, 2, 3], 2), 4)
    def test_example2(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([1, 2, 3, 4, 5], 1), 1)
    def test_example3(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([1, 1, 1, 1], 2), 4)
    def test_single_element(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([5], 1), 1)
    def test_k_larger_than_distinct(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([1, 2, 3], 5), 3)
    def test_negative_numbers(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([-1, -2, -1, -2], 2), 4)
    def test_all_same_k_one(self):
        self.assertEqual(longest_subarray_at_most_k_distinct([7, 7, 7, 7], 1), 4)

if __name__ == '__main__':
    unittest.main()
