def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Returns True if there exist two distinct indices i and j such that
    nums[i] == nums[j] and abs(i - j) <= k.
    Uses a sliding window set of size at most k to achieve O(n) time and O(min(n, k)) space.
    """
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        # Maintain window size <= k
        if len(window) > k:
            window.remove(nums[i - k])
    return False