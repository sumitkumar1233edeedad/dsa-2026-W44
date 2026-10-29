from typing import List

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    """
    Returns the length of the longest contiguous subarray with at most k distinct integers.
    Uses a sliding window with a hash map to track counts of elements in the current window.
    Time Complexity: O(n), Space Complexity: O(k) (or O(n) in worst case).
    """
    if k == 0:
        return 0
    left = 0
    max_len = 0
    count = {}
    for right, num in enumerate(nums):
        count[num] = count.get(num, 0) + 1
        while len(count) > k:
            left_num = nums[left]
            count[left_num] -= 1
            if count[left_num] == 0:
                del count[left_num]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
