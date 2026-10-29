import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_example1(self):
        nums = [1, 1, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_single_element(self):
        nums = [5]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [2])

    def test_no_duplicates(self):
        nums = [-3, -1, 0, 5, 9]
        k = remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-3, -1, 0, 5, 9])

    def test_empty_list(self):
        nums = []
        k = remove_duplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

if __name__ == '__main__':
    unittest.main()