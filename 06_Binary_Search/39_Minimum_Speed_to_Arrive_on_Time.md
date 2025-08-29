# Minimum Speed to Arrive on Time

## Problem Background
You are planning a train journey that consists of n segments. The distances of each segment are given in an array distances, where distances[i] is the distance of the i-th segment.

The train journey has the following characteristics:
* The time taken to travel a segment is calculated as distances[i] / v, where v is the speed at which the train travels (in km/h)
* For every segment except the last, you must wait at an integer time point (e.g., 1:00, 2:00). If the time to travel a segment is not an integer, it must be rounded up to the next integer.
* For the last segment, you can arrive at a decimal time point.
* The journey must be completed within a given maximum time, hours.

## Problem Statement
You are planning a train journey that consists of n segments. The distances of each segment are given in an array distances, where distances[i] is the distance of the i-th segment.

The train journey has the following characteristics:
* The time taken to travel a segment is calculated as distances[i] / v, where v is the speed at which the train travels (in km/h)
* For every segment except the last, you must wait at an integer time point (e.g., 1:00, 2:00). If the time to travel a segment is not an integer, it must be rounded up to the next integer.
* For the last segment, you can arrive at a decimal time point.
* The journey must be completed within a given maximum time, hours.

Given the array distances representing the distances of the journey's segments, and a floating-point number hours representing the maximum total time available to complete the journey, you are tasked with finding the minimum integer speed v (in km/h) that allows you to finish the journey within hours. If it's impossible to finish the journey within the given time, return -1.

## Input Format
* The first line contains two values: n (the number of segments) and hours (the maximum time for the journey).
* The second line contains n integers, where each integer represents the distance for the corresponding segment.

## Output Format
* Return a single integer — the minimum speed required to finish the journey within the given time, or -1 if it's impossible to complete the journey within hours.

## Constraints
* 1 ≤ n ≤ 10^5
* 1 ≤ distances[i] ≤ 10^5
* 1 ≤ hours ≤ 10^9
* hours has at most two decimal places.

## Example
**Input:**
```
3 6.0
1 3 2
```

**Output:**
```
1
```

**Explanation:**
For a speed of 1 km/h:
* First segment: 1/1 = 1 hour
* Second segment: 3/1 = 3 hours  
* Third segment: 2/1 = 2 hours

The total time would be 1 + 3 + 2 = 6 hours, which meets the maximum allowed time (6.0 hours).

## Approach
1. Use binary search on the speed value
2. For each candidate speed, calculate total time needed
3. For non-last segments, use ceil(distance/speed) 
4. For last segment, use exact distance/speed
5. If total time ≤ hours, speed is feasible
6. Binary search finds minimum feasible speed
7. This achieves O(n * log(max_speed)) time complexity