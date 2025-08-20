# Next Smaller Element to the Left

## Problem Background

This problem extends the pattern analysis to find previous smaller elements, which is essential for histogram analysis, building construction algorithms, and financial support level identification. Understanding both forward and backward element relationships is crucial for comprehensive data analysis.

## Problem Statement

Implement a function that finds the previous smaller element for each element in an array. The previous smaller element is the first smaller element that appears to the left. If no smaller element exists, use -1.

## Input Format

- An array of integers

## Output Format

- An array where each element represents the previous smaller element for the corresponding position in the input array

## Example

**Input:**

```
[4, 5, 2, 10, 8]
```

**Output:**

```
[-1, 4, -1, 2, 2]
```

**Explanation:**

- For 4: no previous smaller, so -1
- For 5: previous smaller is 4
- For 2: no previous smaller, so -1
- For 10: previous smaller is 2
- For 8: previous smaller is 2

## Constraints

- Array length can be 0 to 10^4
- Elements can be any integers
- Empty array returns empty array

## Approach

1. Use a stack to maintain elements in increasing order
2. Traverse array from left to right
3. For each element, pop greater/equal elements from stack
4. If stack not empty, top element is previous smaller
5. Push current element to stack
6. This achieves O(n) time complexity with O(n) space
