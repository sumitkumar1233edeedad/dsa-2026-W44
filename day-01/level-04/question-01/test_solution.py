import unittest

class TestMinSubArrayLen(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_sub_array_len(7, [2,3,1,2,4,3]), 2)

    def test_example2(self):
        self.assertEqual(min_sub_array_len(4, [1,4,4]), 1)

    def test_example3(self):
        self.assertEqual(min_sub_array_len(11, [1,1,1,1,1,1,1,1]), 0)

    def test_single_element_meets_target(self):
        self.assertEqual(min_sub_array_len(5, [5]), 1)
        self.assertEqual(min_sub_array_len(3, [10]), 1)

    def test_single_element_below_target(self):
        self.assertEqual(min_sub_array_len(10, [5]), 0)

    def test_all_elements_sum_exactly_target(self):
        self.assertEqual(min_sub_array_len(6, [1,2,3]), 3)

    def test_large_target_no_subarray(self):
        self.assertEqual(min_sub_array_len(100, [1,2,3,4,5]), 0)

    def test_minimal_length_at_end(self):
        self.assertEqual(min_sub_array_len(15, [1,2,3,4,5,6]), 3)  # [4,5,6] sum=15

if __name__ == '__main__':
    unittest.main()
