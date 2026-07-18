# Kadane's Algorithm

## Overview

Kadane's Algorithm is an efficient algorithm used to find the **maximum sum of a contiguous subarray** within a one-dimensional array.

Instead of checking every possible subarray, it processes the array in a single pass while maintaining the best sum found so far.

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

---

## Intuition

At every index, we have two choices:

1. Start a new subarray from the current element.
2. Extend the previous subarray.

If the previous sum becomes negative, it is better to discard it and start a new subarray.

---

## Algorithm

1. Initialize two variables:
   - `currentSum`
   - `maxSum`

2. Traverse the array.
3. Update the current sum:
   - Start a new subarray if the current element is larger.
   - Otherwise extend the previous subarray.
4. Update the maximum sum.
5. Return the maximum sum.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | O(n) |
| Space | O(1) |

---

## Common Problems

- Maximum Subarray (LeetCode 53)
- Maximum Circular Subarray
- Maximum Sum Rectangle (2D Kadane)
- Maximum Product Subarray (Different Variation)

---

## Key Learning

- Greedy Approach
- Dynamic Programming Optimization
- Contiguous Subarray Problems
- Running Sum Technique

---

## Notes

Kadane's Algorithm is one of the most important interview algorithms and is frequently asked in coding interviews. It serves as the foundation for many advanced array and dynamic programming problems.
