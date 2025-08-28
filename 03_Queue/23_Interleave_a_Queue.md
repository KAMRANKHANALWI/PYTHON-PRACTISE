# Interleave a Queue

## Problem Background

In data stream processing and network packet management, you often need to merge two data streams in an alternating fashion. This problem simulates interleaving the first half of a queue with the second half, which is useful in round-robin scheduling, fair resource allocation, and load balancing algorithms.

## Problem Statement

Interleave the first half of a queue with the second half.

- You are given a queue with an even number of elements
- You need to interleave the first half with the second half
- For example, if queue = [1, 2, 3, 4, 5, 6], after interleaving it should be [1, 4, 2, 5, 3, 6]
- If queue = [11, 12, 13, 14], after interleaving it should be [11, 13, 12, 14]
- For this problem, the queue is implemented as an array with these operations:
  - enqueue: Add an element at the end using "push()"
  - dequeue: Remove an element from the front using "shift()"
  - isEmpty: Check if the queue is empty by checking "length"

## Input Format

- An array representing the queue elements (even number of elements)

## Output Format

- An array representing the interleaved queue

## Example

**Input:**

```
[1, 2, 3, 4]
```

**Output:**

```
[1, 3, 2, 4]
```

**Explanation:**
First half: [1, 2], Second half: [3, 4]
Interleaved: [1, 3, 2, 4] (alternating elements from each half)

## Constraints

- Queue has even number of elements
- Elements are integers
- Queue length ≥ 2

## Approach

1. Split queue into two halves
2. Store first half in temporary array
3. Alternate picking elements from first half and remaining queue
4. Build result by interleaving elements
5. Time complexity: O(n), Space complexity: O(n)
