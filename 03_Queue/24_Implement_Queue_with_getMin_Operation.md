# Implement Queue with getMin Operation

## Problem Background

You're building a real-time monitoring system that needs to track data streams efficiently. The system requires quick access to both the standard queue operations and the ability to retrieve minimum values in constant time. This pattern is common in financial systems for tracking minimum stock prices, server monitoring for minimum response times, and data analytics for streaming minimums.

## Problem Statement

Implement a Queue with getMin operation.

- You need to implement a queue that supports all standard operations plus getMin
- The queue should support the following operations:
  - enqueue(element): Add element to the rear of the queue
  - dequeue(): Remove and return element from the front of the queue
  - peek(): Return the front element without removing it
  - getMin(): Return the minimum element in the queue in O(1) time
  - isEmpty(): Check if the queue is empty
- The key challenge is to implement getMin() efficiently (in O(1) time)

## Input Format

- A series of operations as arrays with their parameters

## Output Format

- Array of results for each operation (null for operations that don't return values)

## Example

**Input:**

```
For operations: ["MinQueue", "enqueue", "enqueue", "enqueue", "getMin", "dequeue", "getMin", "peek"] with parameters [[], [3], [1], [5], [], [], [], []], the output should be [null, null, null, null, 1, 3, 1, 1]
```

**Explanation:**

- Create MinQueue, enqueue 3, 1, 5
- getMin() → 1 (minimum in queue)
- dequeue() → 3 (removed front element)
- getMin() → 1, peek() → 1

## Constraints

- All operations must be efficient
- getMin() must be O(1) time complexity
- Queue can be empty
- Values can be any integers

## Approach

1. Use main queue for standard operations
2. Use auxiliary deque to maintain minimums in increasing order
3. For enqueue: add to main queue, maintain min_deque order
4. For dequeue: remove from main queue, check if minimum needs removal
5. getMin() simply returns front of min_deque
6. This achieves O(1) amortized for all operations
