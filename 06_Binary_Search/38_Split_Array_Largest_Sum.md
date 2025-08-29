# Split Array Largest Sum

## Problem Background
You are working on a data processing system that needs to distribute workload across multiple servers efficiently. You have an array representing processing tasks, and you need to split these tasks into groups such that the maximum workload on any single server is minimized.

## Problem Statement
You are given an integer array nums and an integer m. Your task is to split the array into m non-empty continuous subarrays.

Your goal is to minimize the largest sum among these m subarrays.

## Input Format
* The first line contains two integers n and m — the size of the array and the number of subarrays to split the array into.
* The second line contains n integers representing the array elements.

## Output Format
* Return a single integer — the minimized largest sum among the subarrays after splitting.

## Example
**Input:**
```
5 3
7 2 5 10 8
```

**Output:**
```
14
```

**Explanation:**
You need to split the array into 3 subarrays. One possible way to split it is:

* First subarray: [7, 2, 5] (sum = 14)
* Second subarray: [10] (sum = 10)  
* Third subarray: [8] (sum = 8)

The largest sum among the subarrays is 14, which is the minimum possible value for the largest sum among any valid split.

## Constraints
* 1 ≤ n ≤ 1000 (Size of the array)
* 1 ≤ m ≤ min(50, n) (Number of subarrays)
* 0 ≤ nums[i] ≤ 10^6 (Values in the array)

## Approach
1. Use binary search on the answer (maximum sum of any subarray)
2. Search range: [max(nums), sum(nums)]
3. For each candidate maximum sum, check if array can be split into ≤ m subarrays
4. Use greedy approach: keep adding elements to current subarray until sum exceeds target
5. If total subarrays needed ≤ m, the target sum is feasible
6. This achieves O(n * log(sum)) time complexity