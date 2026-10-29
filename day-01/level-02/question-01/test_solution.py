import unittest

class TestFirstDuplicateValue(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]), 2)

    def test_example2(self):
        self.assertEqual(first_duplicate_value([1, 2, 3, 4]), -1)

    def test_example3(self):
        self.assertEqual(first_duplicate_value([5, 5, 5, 5]), 5)

    def test_single_element(self):
        self.assertEqual(first_duplicate_value([1]), -1)

    def test_duplicate_at_end(self):
        self.assertEqual(first_duplicate_value([1, 2, 3, 4, 5, 3]), 3)

    def test_multiple_duplicates_earliest_second(self):
        # 2 appears at indices 1 and 4, 3 appears at indices 2 and 3 -> second occurrence of 3 is earlier
        self.assertEqual(first_duplicate_value([1, 2, 3, 3, 2]), 3)

    def test_large_input(self):
        # generate a large array with a duplicate early
        arr = list(range(1, 100001))
        arr[50000] = 1  # duplicate of 1 at index 50000
        self.assertEqual(first_duplicate_value(arr), 1)

if __name__ == "__main__":
    unittest.main()
