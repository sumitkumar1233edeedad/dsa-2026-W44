import unittest

class TestContainsNearbyDuplicate(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(contains_nearby_duplicate([1,2,3,1], 3))
    
    def test_example2(self):
        self.assertTrue(contains_nearby_duplicate([1,0,1,1], 1))
    
    def test_example3(self):
        self.assertFalse(contains_nearby_duplicate([1,2,3,1,2,3], 2))
    
    def test_single_element(self):
        self.assertFalse(contains_nearby_duplicate([1], 0))
        self.assertFalse(contains_nearby_duplicate([1], 5))
    
    def test_k_zero(self):
        self.assertFalse(contains_nearby_duplicate([1,1], 0))
        self.assertFalse(contains_nearby_duplicate([1,2,1], 0))
    
    def test_large_k(self):
        self.assertTrue(contains_nearby_duplicate([1,2,3,4,5,1], 10))
    
    def test_negative_numbers(self):
        self.assertTrue(contains_nearby_duplicate([-1,-1], 1))
    
    def test_duplicate_distance_exceeds_k(self):
        self.assertFalse(contains_nearby_duplicate([1,2,3,4,1], 3))

if __name__ == '__main__':
    unittest.main()