# Kth Largest Element in an Array

## Problem Background
You're building a competition leaderboard system that needs to quickly identify top performers without sorting the entire dataset. This is a classic problem in competitive programming platforms, gaming leaderboards, and performance analytics where you need efficient access to the kth best result.

## Problem Statement
Implement a function that finds the kth largest element in an unsorted array. The function should efficiently find the element that would be at the kth position if the array was sorted in descending order.

* You need to implement the `findKthLargest` function that returns the kth largest element
* For example, in the array [3,2,1,5,6,4], the 1st largest element is 6, the 2nd largest element is 5, and so on
* The solution should be more efficient than sorting the entire array (which would be O(n log n))
* You may use a priority queue/heap for this implementation

## Input Format
* The function `findKthLargest(nums, k)` takes two parameters:
  * **nums**: An array of integers
  * **k**: An integer representing the position of the element to find
* The function should return the kth largest element as an integer

## Output Format
* Return the kth largest element as an integer

## Example
**Input:** `[3,2,1,5,6,4]|2`
**Output:** `5`

**Explanation:** After sorting, the array becomes [1,2,3,4,5,6], the 2nd largest element is 5.

## Constraints
* 1 ≤ array length ≤ 10^4
* k is always valid (1 ≤ k ≤ array length)
* Array elements can be any integers

## Approach
1. Use a min-heap of size k to maintain the k largest elements seen so far
2. For each element in the array, push it to the heap
3. If heap size exceeds k, pop the smallest element
4. After processing all elements, the root of the heap is the kth largest
5. This achieves O(n log k) time complexity with O(k) space