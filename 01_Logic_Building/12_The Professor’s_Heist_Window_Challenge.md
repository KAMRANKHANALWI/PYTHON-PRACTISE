# The Professor's Heist Window Challenge

## Problem Background

During the meticulous planning of a heist at the Bank of Spain, the Professor must analyze cash transport timings to find the maximum cash transported in any fixed time window. Each hour, a certain amount of cash is moved, and the Professor needs to determine the maximum cash moved in any given window of (k) consecutive hours.

Your task is to help the Professor by solving this problem using an efficient sliding window technique. Given the cash transported during (n) hours and a fixed window size (k), determine the maximum total cash transported within any window of (k) hours.

Can you assist the Professor in ensuring the heist plan is flawless?

## Problem Statement

During the meticulous planning of a heist at the Bank of Spain, the Professor must analyze cash transport timings to find the maximum cash transported in any fixed time window. Each hour, a certain amount of cash is moved, and the Professor needs to determine the maximum cash moved in any given window of (k) consecutive hours.

Your task is to help the Professor by solving this problem using an efficient sliding window technique. Given the cash transported during (n) hours and a fixed window size (k), determine the maximum total cash transported within any window of (k) hours.

## Input Format

- The first line contains two integers (n) and (k) — the total number of hours and the window size.
- The second line contains (n) space-separated integers, where each integer represents the amount of cash transported in a specific hour.

## Output Format

- Return a single integer — the maximum cash transported in any window of (k) consecutive hours.

## Example

**Input:**

```
n = 6 k = 3
10 20 30 40 50 60
```

**Output:**

```
150
```

**Explanation:**
The maximum cash transported in any window of 3 consecutive hours is 150: 60 + 50 + 40 = 150.

## Constraints

- 1 <= n <= 10^5
- 1 <= k <= n
- 1 <= cash transported <= 10^4

## Approach

1. Use sliding window technique for efficient computation
2. Calculate sum of first k elements as initial window
3. Slide window by removing leftmost and adding rightmost element
4. Keep track of maximum sum encountered
5. This achieves O(n) time complexity instead of O(n\*k)
