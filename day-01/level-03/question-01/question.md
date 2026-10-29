# Two Sum II - Input Array Is Sorted

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only **constant extra space**.

---

### Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

---

### Example 1
**Input:** `numbers = [2,7,11,15], target = 9`
**Output:** `[1,2]`
**Explanation:** The sum of 2 and 7 is 9. Therefore `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

### Example 2
**Input:** `numbers = [2,3,4], target = 6`
**Output:** `[1,3]`
**Explanation:** The sum of 2 and 4 is 6. Therefore `index1 = 1`, `index2 = 3`. We return `[1, 3]`.

### Example 3
**Input:** `numbers = [-1,0], target = -1`
**Output:** `[1,2]`
**Explanation:** The sum of -1 and 0 is -1. Therefore `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

---

## 💻 Starter Function

```python
def two_sum(numbers: list[int], target: int) -> list[int]:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems covered linear search (Level 1 Q1), fast/slow pointer in-place duplicate removal on sorted array (Level 1 Q2), and hash-based duplicate detection (Level 2 Q1 & Q2). This problem introduces the classic two-pointer from ends technique on a sorted array, a fundamental pattern for pair-sum problems. It complements the fast/slow pointer by demonstrating how left/right pointers converge from opposite ends, reinforcing in-place logic without extra space. The sorted property allows deterministic movement: increase left pointer if sum is too small, decrease right if too large. This avoids duplication of mechanics (no hash set, no fast/slow) while building core two-pointer intuition.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
