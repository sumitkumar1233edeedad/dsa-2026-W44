# Remove Duplicates from Sorted Array

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

1.  Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
2.  Return `k`.

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k.
```

**Example 3:**
```
Input: nums = [5]
Output: 1, nums = [5]
Explanation: Single element array has no duplicates.
```

---

## 💻 Starter Function

```python
def remove_duplicates(nums: list[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Q01) practiced basic linear traversal for a read-only search operation (finding a target index). This problem (Q02) serves as the complementary twist by introducing the **dual-pointer (slow/fast) pattern** for **in-place array modification**. While Q01 moved a single pointer to *find* a value, this problem requires maintaining a 'write' boundary (slow pointer) separate from the 'read' boundary (fast pointer) to overwrite duplicates. This reinforces linear traversal mechanics (O(N) time, O(1) space) but shifts the cognitive load from 'search logic' to 'state maintenance and boundary management', which is the foundational skill for the 'Two Pointers' pattern often categorized under Arrays & Hashing.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
