import unittest

class TestPartitionByParity(unittest.TestCase):
    def test_example1(self):
        nums = [3,1,2,4]
        result = partition_by_parity(nums)
        seen_odd = False
        for x in result:
            if x % 2 == 1:
                seen_odd = True
            else:
                self.assertFalse(seen_odd, "Even found after odd")
        self.assertEqual(sorted(result), sorted([3,1,2,4]))

    def test_example2(self):
        nums = [0]
        result = partition_by_parity(nums)
        self.assertEqual(result, [0])

    def test_example3(self):
        nums = [1,3,5,7]
        result = partition_by_parity(nums)
        self.assertEqual(result, [1,3,5,7])

    def test_all_even(self):
        nums = [2,4,6,8]
        result = partition_by_parity(nums)
        self.assertEqual(result, [2,4,6,8])

    def test_mixed(self):
        nums = [1,2,3,4,5,6,7,8,9,10]
        result = partition_by_parity(nums)
        seen_odd = False
        for x in result:
            if x % 2 == 1:
                seen_odd = True
            else:
                self.assertFalse(seen_odd)
        self.assertEqual(sorted(result), sorted(nums))

    def test_empty(self):
        nums = []
        result = partition_by_parity(nums)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()