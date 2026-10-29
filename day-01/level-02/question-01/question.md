# First Duplicate Value

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers, find the **first duplicate value** that occurs. The first duplicate is defined as the value whose **second occurrence** has the smallest index. If there are no duplicates, return `-1`.

**Constraints:**
- `1 <= len(arr) <= 10^5`
- `1 <= arr[i] <= 10^5`

**Examples:**

**Example 1:**
```
Input: [2, 1, 5, 2, 3, 3, 4]
Output: 2
Explanation: 2 appears at indices 0 and 3. 3 appears at indices 4 and 5. The second occurrence of 2 (index 3) comes before the second occurrence of 3 (index 5).
```

**Example 2:**
```
Input: [1, 2, 3, 4]
Output: -1
Explanation: No value appears more than once.
```

**Example 3:**
```
Input: [5, 5, 5, 5]
Output: 5
Explanation: The second occurrence of 5 is at index 1, which is the earliest possible.
```

---

## 💻 Starter Function

```python
def first_duplicate_value(arr: list[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems: 'Find Target Index in Array' (linear search) and 'Remove Duplicates from Sorted Array' (two-pointer on sorted array). The latter exploited sorted order to remove duplicates in-place. The logical next step is duplicate detection in **unsorted** arrays where ordering cannot be used. The canonical solution introduces a **Hash Set** to track seen elements during a single pass, achieving O(n) time and O(n) space. This problem ('First Duplicate Value') specifically reinforces the core mechanic of using a hash set for frequency/detection: we insert each element, and the moment we encounter an element already in the set, we have found the first duplicate by second-occurrence index. It avoids duplication by not asking for removal or mere existence check, but for the value with the earliest second occurrence, a slight twist that solidifies the traversal-and-hash pattern.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
