# Next Smaller Element to the Right

## Problem Background

Building on array analysis patterns, this problem focuses on finding the next smaller element for each position. This is commonly used in stock market analysis for finding support levels, in data compression algorithms, and in various optimization problems where you need to identify the next minimum threshold.

## Problem Statement

Implement a function that finds the next smaller element for each element in an array. The next smaller element is the first smaller element that appears to the right. If no smaller element exists, use -1.

## Input Format

- An array of integers

## Output Format

- An array where each element represents the next smaller element for the corresponding position in the input array

## Example

**Input:**

```
[4, 5, 2, 10, 8]
```

**Output:**

```
[2, 2, -1, 8, -1]
```

**Explanation:**

- For 4: next smaller is 2
- For 5: next smaller is 2
- For 2: no smaller element, so -1
- For 10: next smaller is 8
- For 8: no smaller element, so -1

## Constraints

- Array length can be 0 to 10^4
- Elements can be any integers
- Empty array returns empty array

## Approach

1. Use a stack to store elements in increasing order
2. Traverse array from right to left
3. For each element, pop greater/equal elements from stack
4. If stack not empty, top element is next smaller
5. Push current element to stack
6. This achieves O(n) time complexity with O(n) space
