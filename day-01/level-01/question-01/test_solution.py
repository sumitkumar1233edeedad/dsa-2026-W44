import unittest

class TestFindTargetIndex(unittest.TestCase):
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(find_target_index(nums, target), 4)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(find_target_index(nums, target), -1)

    def test_example3(self):
        nums = [1]
        target = 1
        self.assertEqual(find_target_index(nums, target), 0)

    def test_multiple_occurrences(self):
        nums = [2, 3, 2, 4, 2]
        target = 2
        self.assertEqual(find_target_index(nums, target), 0)

    def test_target_at_end(self):
        nums = [5, 6, 7, 8]
        target = 8
        self.assertEqual(find_target_index(nums, target), 3)

    def test_negative_numbers(self):
        nums = [-5, -2, 0, 3]
        target = -2
        self.assertEqual(find_target_index(nums, target), 1)

if __name__ == '__main__':
    unittest.main()