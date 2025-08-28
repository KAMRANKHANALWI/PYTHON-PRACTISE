# Top K Frequent Elements

## Problem Background
As a data analyst, you need to identify the most common items in large datasets for trend analysis. This problem appears in recommendation systems, fraud detection, web analytics, and social media trend analysis where finding the most frequent patterns is crucial for business insights.

## Problem Statement
Given an integer array and an integer k, find the k most frequent elements in the array.

* You need to implement the `topKFrequent` function that returns the k most frequent elements
* The answer should be sorted by frequency from highest to lowest
* If two elements have the same frequency, they can be returned in any order
* You may assume that k is always valid, i.e., 1 ≤ k ≤ number of unique elements
* The solution should be better than O(n log n) time complexity

## Input Format
* The function `topKFrequent(nums, k)` takes two parameters:
  * **nums**: An array of integers
  * **k**: An integer representing how many top frequent elements to return
* The function should return an array of the k most frequent elements

## Output Format
* Return an array of the k most frequent elements sorted by frequency (highest to lowest)

## Example
**Input:** `[1,1,1,2,2,3]|2`
**Output:** `[1,2]`

**Explanation:** The elements 1 and 2 appear three times and two times respectively, making them the most frequent elements.

## Constraints
* 1 ≤ array length ≤ 10^5
* k is always valid (1 ≤ k ≤ number of unique elements)
* Elements can be any integers

## Approach
1. Count frequency of each element using a hash map
2. Use a min-heap of size k to maintain the k most frequent elements
3. For each element-frequency pair, push to heap
4. If heap size exceeds k, pop the least frequent element
5. Sort final result by frequency in descending order
6. This achieves O(n log k) time complexity