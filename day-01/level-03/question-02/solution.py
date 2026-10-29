def partition_by_parity(nums: list[int]) -> list[int]:
    """
    Rearranges nums in-place so that all even integers come before odd integers.
    Returns the modified list.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums