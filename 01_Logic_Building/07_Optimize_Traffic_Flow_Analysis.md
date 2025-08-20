# Optimize Traffic Flow Analysis

## Problem Background

As part of the Spring Smart City Initiative, you're developing a system to analyze traffic patterns. Traffic flow data is collected at regular intervals for multiple roads. Your task is to identify the maximum traffic flow recorded over any continuous k intervals to detect potential congestion trends.

## Problem Statement

Given a list of integers representing traffic flow at each interval and an integer k representing the window size, write a program to find the maximum sum of traffic flow recorded over any k consecutive intervals.

## Input Format

1. **trafficFlow**: An array of integers representing the traffic flow at each interval.
   - 1 ≤ length of trafficFlow ≤ 10^5
   - 0 ≤ trafficFlow[i] ≤ 10^3.
2. **k**: An integer representing the size of the window (1 <= k <= length of trafficFlow).

## Output Format

- An integer representing the maximum sum of traffic flow over any k consecutive intervals.

## Example

**Input:**

```json
[[10, 20, 30, 40, 50], 3]
```

**Output:**

```
120
```

## Explanation

The sum of each window of size 3 is:

- [10, 20, 30] = 60
- [20, 30, 40] = 90
- [30, 40, 50] = 120

The maximum sum is 120.

## Constraints

- 1 ≤ length of trafficFlow ≤ 10^5
- 0 ≤ trafficFlow[i] ≤ 10^3
- 1 ≤ k ≤ length of trafficFlow

## Approach

1. Use sliding window technique for efficient computation
2. Calculate sum of first k elements as initial window
3. Slide the window by removing leftmost element and adding rightmost element
4. Keep track of maximum sum encountered
5. This achieves O(n) time complexity instead of O(n\*k)
