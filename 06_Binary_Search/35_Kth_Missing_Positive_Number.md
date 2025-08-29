# Kth Missing Positive Number

## Problem Background

In data analysis and system monitoring, you often need to identify gaps in sequential data. This problem simulates finding missing elements in ordered datasets, which is crucial for data integrity checks, sequence validation, and identifying missing records in databases or logs.

## Problem Statement

You are given an ascending array of positive integers and an integer k. Your task is to find the kth positive integer that is missing from this array.

For example, if the array is [2, 3, 4, 7, 11] and k = 5, then the missing positive integers are 1, 5, 6, 8, 9, 10, 12, 13, ... The 5th missing positive integer is 9.

Can you solve this efficiently using binary search?

## Input Format

- The first line contains two integers n and k — the size of the array and the position of the missing number to find.
- The second line contains n integers representing the array elements in ascending order.

## Output Format

- Return a single integer — the kth missing positive integer.

## Example

**Input:**

```
5 5
2 3 4 7 11
```

**Output:**

```
9
```

**Explanation:**
The missing positive integers are 1, 5, 6, 8, 9, 10, 12, 13, ...
The 5th missing positive integer is 9.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ k ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5
- All array elements are distinct and in ascending order.

## Approach

1. Use binary search to find the position where kth missing number would be
2. For each position i, calculate missing numbers before arr[i] as: arr[i] - (i + 1)
3. Find the first position where missing count >= k
4. The answer is k + left (where left is count of array elements ≤ answer)
5. This achieves O(log n) time complexity instead of O(n)
