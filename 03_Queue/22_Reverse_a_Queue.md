# Reverse a Queue

## Problem Background

In data processing systems, you sometimes need to reverse the order of elements in a queue while maintaining the queue's FIFO nature. This is useful in undo operations, data stream processing, or when you need to process elements in reverse order. Since queues only allow access from front and rear, you'll need an auxiliary data structure to achieve this reversal.

## Problem Statement

Implement a function to reverse a queue.

- You are given a queue of integers implemented as an array
- The queue supports the following operations:
  - enqueue: Add an element at the end using push()
  - dequeue: Remove an element from the front using shift()
  - isEmpty: Check if the queue is empty by checking length
- You need to reverse the order of elements in the queue
- For example, if queue = [1, 2, 3, 4, 5], after reversing it should be [5, 4, 3, 2, 1]
- You may use a stack (or recursion) as an auxiliary data structure
- The function should return the reversed queue

## Input Format

- An array representing the queue elements

## Output Format

- An array representing the reversed queue

## Example

**Input:**

```
[10, 20, 30, 40, 50]
```

**Output:**

```
[50, 40, 30, 20, 10]
```

**Explanation:**
The queue elements are reversed: first element becomes last, last becomes first.

## Constraints

- Queue can contain 0 to 10^4 elements
- Elements are integers
- Must maintain queue operations

## Approach

1. Use a stack as auxiliary data structure
2. Dequeue all elements from queue and push to stack
3. Pop all elements from stack and enqueue back to queue
4. Stack's LIFO nature reverses the queue's FIFO order
5. Time complexity: O(n), Space complexity: O(n)
