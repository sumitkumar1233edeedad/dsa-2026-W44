def remove_duplicates(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted array in-place.

    Args:
        nums: A list of integers sorted in non-decreasing order.

    Returns:
        The number of unique elements (k). The first k elements of nums
        will contain the unique elements in their original relative order.
    """
    if not nums:
        return 0

    # slow pointer points to the position where the next unique element should be placed
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow