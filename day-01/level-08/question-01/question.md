# Maximum Concurrent Weight of Intervals

- **Day:** `Day 01`
- **Level:** `Level 08`
- **Question:** `Question 01`
- **Difficulty:** `Hard`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

You are given a list of `n` intervals, where each interval is represented as a triplet `[start, end, weight]`. The interval includes all real numbers `x` such that `start <= x < end` (i.e., half-open interval). The weight is a positive integer.

Find the maximum total weight of intervals that overlap at any single point. In other words, find a point `x` on the real line such that the sum of weights of all intervals covering `x` is maximized, and return that maximum sum.

### Constraints
- `1 <= n <= 10^5`
- `0 <= start < end <= 10^9`
- `1 <= weight <= 10^4`
- The answer fits within a 32-bit signed integer.

### Example 1
**Input:** `intervals = [[1, 5, 10], [2, 3, 5], [4, 6, 7]]`
**Output:** `17`
**Explanation:**
- At point `2.5`, intervals `[1,5,10]` and `[2,3,5]` overlap. Total weight = 15.
- At point `4.5`, intervals `[1,5,10]` and `[4,6,7]` overlap. Total weight = 17.
- No point is covered by all three intervals simultaneously. Maximum concurrent weight is 17.

### Example 2
**Input:** `intervals = [[0, 10, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6]]`
**Output:** `7`
**Explanation:** The interval `[0,10,3]` overlaps with each of the small intervals. The maximum overlap occurs at any point inside `[1,2)`, `[2,3)`, or `[3,4)` where the base weight 3 adds with the respective small interval's weight (4, 5, or 6). The peak is 3 + 6 = 9? Wait, check: at [3,4) we have weight 3+6=9. But the example says output 7. Let's correct: Actually, the intervals are [0,10,3], [1,2,4], [2,3,5], [3,4,6]. At point 1.5: 3+4=7. At 2.5: 3+5=8. At 3.5: 3+6=9. So maximum is 9. Let's adjust example to avoid confusion. We'll provide a consistent example.

**Corrected Example 2:**
**Input:** `intervals = [[0, 10, 3], [1, 2, 4], [5, 6, 5]]`
**Output:** `7`
**Explanation:** Overlap at [1,2) gives 3+4=7. Overlap at [5,6) gives 3+5=8? Wait, 3+5=8. So max is 8. Let's make a simpler example.

**Example 2 (final):**
**Input:** `intervals = [[1, 3, 5], [2, 4, 3], [3, 5, 2]]`
**Output:** `8`
**Explanation:** At point 2.5, first two intervals overlap: 5+3=8. At point 3.5, last two overlap: 3+2=5. Maximum is 8.

### Example 3
**Input:** `intervals = [[10, 20, 100]]`
**Output:** `100`
**Explanation:** Only one interval, so maximum concurrent weight is its own weight.

---

## 💻 Starter Function

```python
from typing import List

def max_concurrent_weight(intervals: List[List[int]]) -> int:
    """
    Returns the maximum total weight of intervals overlapping at any point.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous Level 08 problem 'Maximum Weight of Non-Overlapping Intervals' focused on the classic Weighted Interval Scheduling problem, which is solved via Dynamic Programming with binary search (selecting a subset of non-overlapping intervals to maximize total weight). This new problem shifts the paradigm to the complementary 'overlap scheduling' mechanic: instead of selecting non-overlapping intervals, we need to find the peak concurrent weight at any point on the timeline. This is a canonical sweep-line / difference-array problem that requires coordinate compression (using hashing) to handle large coordinate ranges efficiently, fitting the 'Arrays & Hashing' topic perfectly. It reinforces core interval mechanics (event sorting, prefix sums, peak tracking) while avoiding duplication of the DP-based selection logic. The Hard difficulty arises from the need for O(n log n) event processing and coordinate compression with hash maps to manage up to 10^5 intervals and 10^9 coordinate bounds.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
