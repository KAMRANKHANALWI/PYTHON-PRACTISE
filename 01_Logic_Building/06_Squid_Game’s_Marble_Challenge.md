# Squid Game's Marble Challenge

## Problem Statement

In the Squid Game's infamous marble challenge, players are asked to gamble their marbles by placing them into different pits. Each pit contains a certain number of marbles, and a player can only take marbles from a contiguous range of pits in one move.

Your task is to determine the total number of marbles in any given range of pits efficiently. The Front Man has given you a list of n pits, where each pit has a certain number of marbles, and q queries. Each query provides a starting and ending pit, and you must calculate the total number of marbles in that range.

Can you calculate the results for all the queries quickly before time runs out?

## Input Format

- The first line contains two integers n and q:
  - **n**: the number of pits.
  - **q**: the number of queries.
- The second line contains n integers representing the number of marbles in each pit.
- The following q lines contain two integers each, l and r (1 <= l <= r <= n), representing the range of pits (inclusive).

## Output Format

- For each query, print a single integer representing the total number of marbles in the given range of pits.

## Example

**Input:**

```
5 3
1 2 3 4 5
1 3
2 5
1 5
```

**Output:**

```
6
14
15
```

## Explanation

- For the first query, the total number of marbles in the range [1, 3] is 1 + 2 + 3 = 6.
- For the second query, the total number of marbles in the range [2, 5] is 2 + 3 + 4 + 5 = 14.
- For the third query, the total number of marbles in the range [1, 5] is 1 + 2 + 3 + 4 + 5 = 15.

## Constraints

- 1 <= n, q <= 10^5
- 1 <= number of marbles in a pit <= 10^3
- 1 <= l <= r <= n

## Approach

1. Use prefix sum array to precompute cumulative sums
2. For each query [l, r], the sum is prefix[r] - prefix[l-1]
3. Handle edge case when l = 1 (use prefix[r] directly)
4. This achieves O(n + q) time complexity instead of O(n\*q)
