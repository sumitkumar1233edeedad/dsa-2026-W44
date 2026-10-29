from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Returns an array where each element at index i is the product of all elements
    in nums except nums[i].
    Runs in O(n) time and O(1) extra space (excluding the output array).
    """
    n = len(nums)
    answer = [1] * n

    # Compute prefix products: answer[i] contains product of nums[0..i-1]
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    # Multiply by suffix products on the fly
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
