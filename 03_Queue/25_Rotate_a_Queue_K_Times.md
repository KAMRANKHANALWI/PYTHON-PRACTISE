# Rotate a Queue K Times

## Problem Background

Queue rotation is a fundamental operation in circular buffers, round-robin schedulers, and data stream processing. When you need to shift elements in a queue by k positions, you're essentially moving the front elements to the back. This operation is crucial in task scheduling systems, data preprocessing pipelines, and implementing circular data structures.

## Problem Statement

Rotate a queue k times.

- You are given a queue of integers and a number k
- You need to rotate the queue k times, meaning the front element should be moved to the rear k times
- For example, if queue = [1, 2, 3, 4, 5] and k = 2, after rotation it should be [3, 4, 5, 1, 2]
- For this problem, the queue is implemented as an array with these operations:
  - enqueue: Add an element at the end using "push()"
  - dequeue: Remove an element from the front using "shift()"
  - isEmpty: Check if the queue is empty by checking "length"
- The function should return the rotated queue

## Input Format

- A queue array and integer k separated by "|"

## Output Format

- An array representing the rotated queue

## Example

**Input:**

```
For input queue: [10, 20, 30, 40, 50] and k = 3 and they will be '|' separated in input, the output should be the queue that is [40, 50, 10, 20, 30]
```

**Explanation:**
After rotating 3 times:

- Original: [10, 20, 30, 40, 50]
- After 1 rotation: [20, 30, 40, 50, 10]
- After 2 rotations: [30, 40, 50, 10, 20]
- After 3 rotations: [40, 50, 10, 20, 30]

## Constraints

- Queue can contain 0 to 10^3 elements
- k can be any non-negative integer
- Handle k > queue length using modulo operation

## Approach

1. Handle edge cases: empty queue or k = 0
2. Use modulo to handle k > queue length
3. Split queue into two parts at position k
4. Concatenate second part + first part
5. Time complexity: O(n), Space complexity: O(n)
