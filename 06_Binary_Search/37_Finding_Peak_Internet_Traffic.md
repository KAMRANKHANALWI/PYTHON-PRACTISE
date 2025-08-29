# Finding Peak Internet Traffic

## Problem Background
As a network analyst at a major tech company, you're monitoring internet traffic patterns across your data centers. The traffic pattern follows an interesting trend: it first increases, reaches a peak, and then starts decreasing.

You've collected samples of traffic volume at different time points during a 24-hour period. Each sample is greater than or equal to its neighbors as you approach the peak, and less than or equal to its neighbors as you move away from the peak.

Your task is to find the peak traffic volume - the point where the traffic stops increasing and starts decreasing. This will help you understand when your network is under the most stress.

## Problem Statement
As a network analyst at a major tech company, you're monitoring internet traffic patterns across your data centers. The traffic pattern follows an interesting trend: it first increases, reaches a peak, and then starts decreasing.

You've collected samples of traffic volume at different time points during a 24-hour period. Each sample is greater than or equal to its neighbors as you approach the peak, and less than or equal to its neighbors as you move away from the peak.

Your task is to find the peak traffic volume - the point where the traffic stops increasing and starts decreasing. This will help you understand when your network is under the most stress.

## Input Format
* A list of integers representing traffic volume at different time points
* Each element represents the traffic volume (in Gbps) at a certain time
* The array is guaranteed to have a single peak (mountain shape)

## Output Format
* The index of the peak element in the array

## Example
**Input:**
```
7
1 3 5 7 6 4 2
```

**Output:**
```
3
```

**Explanation:**
* For traffic volumes [1, 3, 5, 7, 6, 4, 2], the peak is at index 3 (with value 7)
* For traffic volumes [10, 20, 30, 40, 50], the peak is at index 4 (with value 50)
* For traffic volumes [50, 40, 30, 20, 10], the peak is at index 0 (with value 50)

## Constraints
* The array will have at least 1 element
* If there are multiple equal peaks, return the index of any one of them
* Your solution must run in O(log n) time complexity, where n is the number of elements in the array

## Approach
1. Use binary search to efficiently find the peak
2. Compare middle element with its right neighbor
3. If arr[mid] < arr[mid+1], peak is on the right side
4. Otherwise, peak is at mid or on the left side
5. This achieves O(log n) time complexity instead of O(n) linear search