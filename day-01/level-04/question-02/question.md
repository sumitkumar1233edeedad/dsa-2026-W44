# Longest Subarray with At Most K Distinct Integers

- **Day:** `Day 01`
- **Level:** `Level 04`
- **Question:** `Question 02`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return the length of the longest contiguous subarray that contains **at most** `k` distinct integers.

A subarray is a contiguous part of the array.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

**Example 1:**
```
Input: nums = [1,2,1,2,3], k = 2
Output: 4
Explanation: The longest subarray with at most 2 distinct integers is [1,2,1,2] (length 4).
```

**Example 2:**
```
Input: nums = [1,2,3,4,5], k = 1
Output: 1
Explanation: Any subarray of length 1 has exactly 1 distinct integer.
```

**Example 3:**
```
Input: nums = [1,1,1,1], k = 2
Output: 4
Explanation: The entire array has only 1 distinct integer, which is <= 2.
```

---

## 💻 Starter Function

```python
from typing import List

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Minimum Size Subarray Sum) practiced the classic variable-size sliding window to find a *minimum* length satisfying a *sum* condition (sum >= target) using only a running sum and two pointers. This problem is the logical complementary twist for Level 04 Q02: it keeps the sliding window bounds pattern but shifts the objective to *maximizing* the window length (edge boundary optimization) and changes the window validity condition from a numeric sum to a *distinct count* constraint (at most k distinct). This forces the introduction of a Hash Map (dictionary) to track frequencies of elements in the current window, a core technique in the 'Arrays & Hashing' topic. It avoids duplication by replacing the arithmetic condition with a cardinality condition and the minimization goal with maximization, while reinforcing the dual-pointer (left/right) expansion/shrinking mechanics.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
