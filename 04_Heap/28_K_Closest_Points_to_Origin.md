# K Closest Points to Origin

## Problem Background
You're developing a mapping application that needs to find the nearest points of interest to a user's location. This problem is fundamental in location-based services, GPS navigation systems, and spatial analysis where efficiently finding the closest geographical points is essential for user experience.

## Problem Statement
Given an array of points in a 2D plane, find the k closest points to the origin (0, 0). The distance between two points is measured using the Euclidean distance.

* You need to implement the `kClosest` function that returns the k closest points to the origin
* The distance formula is sqrt(x^2 + y^2)
* Return the answer in any order

## Input Format
* The function `kClosest(points, k)` takes two parameters:
  * **points**: An array of points where each point is an array [x, y] representing coordinates
  * **k**: An integer representing the number of closest points to return
* The function should return an array of the k closest points to the origin

## Output Format
* Return an array of the k closest points to the origin
* Each point should be in the format [x, y]

## Example
**Input:** `[[1,3],[-2,2]]|1`
**Output:** `[[-2,2]]`

**Explanation:** The distance from (1,3) to origin is sqrt(10) ≈ 3.16. The distance from (-2,2) to origin is sqrt(8) ≈ 2.83. Since sqrt(8) < sqrt(10), (-2,2) is closer to the origin.

## Constraints
* 1 ≤ points.length ≤ 10^4
* k is always valid (1 ≤ k ≤ points.length)
* Points can have negative coordinates
* -10^4 ≤ coordinates ≤ 10^4

## Approach
1. Use a max-heap of size k to maintain the k closest points
2. For each point, calculate squared distance (avoid sqrt for efficiency)
3. Push (-distance, x, y) to heap (negative for max-heap behavior)
4. If heap size exceeds k, pop the farthest point
5. Return the remaining k points from the heap
6. This achieves O(n log k) time complexity