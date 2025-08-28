# Kth Smallest Element in a Sorted Matrix

## Problem Background
You're building a data analysis tool that needs to find particular values in large, pre-sorted 2D datasets efficiently. This problem is common in database query optimization, scientific computing, and data mining where you have structured data with multiple sorting dimensions and need to efficiently locate specific ranked elements.

## Problem Statement
Given an n x n matrix where each row and column is sorted in ascending order, find the kth smallest element in the matrix.

* The matrix has the property that elements are sorted in both rows and columns
* It's guaranteed that the matrix is non-empty and k is valid (1 ≤ k ≤ n²)
* You need to find the kth smallest element, not the kth distinct element

## Input Format
* The function `kthSmallest(matrix, k)` takes two parameters:
  * **matrix**: An n x n 2D array where both rows and columns are sorted in ascending order
  * **k**: An integer representing the position of the element to find
* The function should return the kth smallest element in the matrix

## Output Format
* Return the kth smallest element as an integer

## Example
**Input:** `[[1,5,9],[10,11,13],[12,13,15]]|8`
**Output:** `13`

**Explanation:** The elements in the matrix in sorted order are: 1, 5, 9, 10, 11, 12, 13, 13, 15. The 8th smallest element is 13.

## Constraints
* 1 ≤ n ≤ 300
* Matrix is guaranteed to be non-empty
* k is valid (1 ≤ k ≤ n²)
* Elements can be negative or positive integers

## Approach
1. Use a min-heap to efficiently traverse the matrix in sorted order
2. Initialize heap with the first element of each row
3. For each iteration, pop the smallest element from heap
4. Add the next element from the same row (if exists) to heap
5. Continue until we've popped k elements
6. This achieves O(k log n) time complexity with O(n) space