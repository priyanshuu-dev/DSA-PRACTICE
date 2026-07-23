# Merge Intervals

## Problem
Given an array of intervals where `intervals[i] = [start, end]`, merge all overlapping intervals and return a list of non-overlapping intervals covering all the intervals.

## Approach

1. Sort the intervals based on their starting value.
2. Initialize the first interval as the current interval.
3. Traverse the remaining intervals:
   - If the current interval overlaps with the previous one, merge them by updating the ending value.
   - Otherwise, add the previous interval to the result and move to the next interval.
4. Add the last merged interval to the result.

## Algorithm

- Sort the intervals by their start value.
- Keep track of the current merged interval.
- Merge overlapping intervals whenever possible.
- Store non-overlapping intervals in the result list.

## Time Complexity

- Sorting: **O(n log n)**
- Merging: **O(n)**

**Overall:** `O(n log n)`

## Space Complexity

- **O(n)** (for the output list)

## Concepts Used

- Sorting
- Arrays
- Interval Merging
- Greedy Traversal
