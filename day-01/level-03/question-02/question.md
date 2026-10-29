# Partition Array by Parity

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, rearrange the array **in-place** such that all even integers appear before all odd integers.

Return the modified array. The relative order of the even and odd integers does **not** need to be preserved.

**Constraints:**
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^4`

**Example 1:**
```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The even numbers [2,4] are moved to the front. [4,2,3,1] is also accepted.
```

**Example 2:**
```
Input: nums = [0]
Output: [0]
```

**Example 3:**
```
Input: nums = [1,3,5,7]
Output: [1,3,5,7]
Explanation: There are no even numbers, so the array remains unchanged.
```

---

## 💻 Starter Function

```python
def partition_by_parity(nums: list[int]) -> list[int]:
    """
    Rearranges nums in-place so that all even integers come before odd integers.
    Returns the modified list.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Two Sum II) used the classic two-pointer technique on a sorted array to search for a target sum by moving pointers inward from both ends. This problem provides the complementary twist: instead of searching, we use the same left/right pointer structure to perform an in-place partition based on parity (even/odd). This reinforces the two-pointer boundary optimization pattern—moving pointers toward each other and swapping when they find misplaced elements—while introducing the concept of in-place rearrangement without extra space. It avoids duplication because it does not involve searching for a sum, checking duplicates, or finding indices; it purely focuses on partitioning via two-pointer boundary convergence.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
