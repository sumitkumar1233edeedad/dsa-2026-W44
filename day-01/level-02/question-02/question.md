# Contains Nearby Duplicate

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`. Otherwise, return `false`.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: The value 1 appears at indices 0 and 3. The absolute difference is 3, which is <= k.
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: The value 1 appears at indices 2 and 3. The absolute difference is 1, which is <= k.
```

**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: All duplicate pairs (1, 2, 3) have index differences of 3, which exceeds k=2.
```

---

## 💻 Starter Function

```python
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'First Duplicate Value' (Level 02 Q01) introduced the Hash Set pattern for detecting duplicates globally by tracking seen elements. This problem provides the complementary 'dual-pointer variation' twist: instead of a global search, we constrain the duplicate search to a sliding window of size `k+1`. This reinforces Hash Set usage while introducing the sliding window (two-pointer) technique to maintain only the relevant recent elements, optimizing space to O(min(n, k)) and teaching boundary management (evicting elements that fall outside the window). It avoids duplicating the 'first duplicate' mechanic by changing the condition from 'any previous occurrence' to 'occurrence within distance k', a classic LeetCode 219 pattern that builds directly on the frequency/set foundation.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
