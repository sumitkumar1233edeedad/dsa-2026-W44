def first_duplicate_value(arr: list[int]) -> int:
    """
    Returns the first duplicate value in the array, where the first duplicate is defined
    as the value whose second occurrence has the smallest index.
    If no duplicates exist, returns -1.

    Args:
        arr: List of integers (1 <= len(arr) <= 10^5, 1 <= arr[i] <= 10^5).

    Returns:
        The first duplicate value, or -1 if none.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1
