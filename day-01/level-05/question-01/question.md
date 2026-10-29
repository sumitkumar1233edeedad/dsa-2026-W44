# Product of Array Except Self

- **Day:** `Day 01`
- **Level:** `Level 05`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Constraints:**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Example 3:**
```
Input: nums = [2,3,4,5]
Output: [60,40,30,24]
```

---

## 💻 Starter Function

```python
def productExceptSelf(nums: List[int]) -> List[int]:
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Levels 2-4) focused on sliding window techniques and hash maps for duplicate detection, two-sum variants, and subarray constraints with positive numbers. This problem introduces the canonical Prefix & Suffix Transform pattern: precomputing prefix products and suffix products in two linear passes to answer a per-index query in O(1) time. It reinforces linear traversal and direct indexing without division, hash maps, or window adjustments, making it the ideal logical next step for Level 5's core mechanics of prefix/suffix transforms.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
