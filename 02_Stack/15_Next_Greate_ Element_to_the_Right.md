# Next Greater Element to the Right

## Problem Background

You're working on a code optimization tool that analyzes array patterns. One common requirement is finding the next greater element for each position in an array. This pattern appears frequently in financial analysis, data processing, and algorithmic trading systems where you need to identify the next peak or threshold value.

## Problem Statement

Implement a function that finds the next greater element for each element in an array. The next greater element is the first greater element that appears to the right. If no greater element exists, use -1.

## Input Format

- An array of integers

## Output Format

- An array where each element represents the next greater element for the corresponding position in the input array

## Example

**Input:**

```
[4, 5, 2, 25]
```

**Output:**

```
[5, 25, 25, -1]
```

**Explanation:**

- For 4: next greater is 5
- For 5: next greater is 25
- For 2: next greater is 25
- For 25: no greater element, so -1

## Constraints

- Array length can be 0 to 10^4
- Elements can be any integers
- Empty array returns empty array

## Approach

1. Use a stack to store elements in decreasing order
2. Traverse array from right to left
3. For each element, pop smaller/equal elements from stack
4. If stack not empty, top element is next greater
5. Push current element to stack
6. This achieves O(n) time complexity with O(n) space
