def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Returns the 1-indexed indices of the two numbers in `numbers` that add up to `target`.
    The input array is sorted in non-decreasing order and exactly one solution exists.
    Uses two-pointer technique with constant extra space.
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    # According to problem constraints, a solution always exists.
    return []
