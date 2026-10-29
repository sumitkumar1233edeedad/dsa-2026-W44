def min_sub_array_len(target: int, nums: list[int]) -> int:
    """
    Returns the minimal length of a contiguous subarray of `nums` whose sum is
    greater than or equal to `target`. If no such subarray exists, returns 0.

    Uses a sliding window approach because all numbers are positive.
    Time Complexity: O(n), Space Complexity: O(1).
    """
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
