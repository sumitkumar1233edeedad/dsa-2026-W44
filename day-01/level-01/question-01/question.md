# Find Target Index in Array

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the index of the **first occurrence** of `target` in `nums`. If `target` does not exist in the array, return `-1`.

You must write an algorithm with `O(n)` runtime complexity.

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

**Example 1:**
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Explanation: 0 is found at index 4.
```

**Example 2:**
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
Explanation: 3 does not exist in nums.
```

**Example 3:**
```
Input: nums = [1], target = 1
Output: 0
```

---

## 💻 Starter Function

```python
def find_target_index(nums: list[int], target: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> This is the inaugural problem (Question 01, Level 01, Day 01) for the 'Arrays & Hashing' topic with a focus on 'Linear Traversal & Search'. Since there are no previously solved questions, the pedagogical goal is to establish the absolute canonical algorithmic primitive: the Linear Scan. This problem enforces the core mechanics of iterating 0 to N-1, direct indexing (`nums[i]`), conditional comparison (`==`), and early exit via `return`. It avoids duplication by being the foundational entry point. It prepares the learner for immediately subsequent patterns (Two Pointers, Sliding Window, Prefix Sums) which all rely on mastering the single-pass loop structure and index manipulation first.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
