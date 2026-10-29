import unittest

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2])
    
    def test_example2(self):
        self.assertEqual(two_sum([2, 3, 4], 6), [1, 3])
    
    def test_example3(self):
        self.assertEqual(two_sum([-1, 0], -1), [1, 2])
    
    def test_duplicates(self):
        # numbers = [1, 2, 2, 4], target = 4 -> indices 2 and 3 (1-indexed)
        # Only pair is 2+2=4 (the two 2's). This input has exactly one solution.
        self.assertEqual(two_sum([1, 2, 2, 4], 4), [2, 3])
    
    def test_large_array(self):
        numbers = list(range(1, 10001))
        target = 19999  # 9999 + 10000
        self.assertEqual(two_sum(numbers, target), [9999, 10000])
    
    def test_negative_numbers(self):
        numbers = [-5, -3, -1, 0, 1, 3, 5]
        target = -4  # -5 + 1 = -4
        self.assertEqual(two_sum(numbers, target), [1, 5])

if __name__ == '__main__':
    unittest.main()
