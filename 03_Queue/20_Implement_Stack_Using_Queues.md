# Implement Stack Using Queues

## Problem Background

You're working on a system architecture where you need to simulate stack behavior but only have access to queue data structures. This scenario occurs in distributed systems, embedded programming, or when working with APIs that only provide queue operations. Your challenge is to implement a complete stack using only queue operations.

## Problem Statement

Implement a Stack using Queues.

- A stack is a LIFO (Last In First Out) data structure
- You need to implement a stack using only queue data structures
- In this problem, queues are implemented as arrays with these operations:
  - enqueue: Add an element at the end using push()
  - dequeue: Remove an element from the front using shift()
  - isEmpty: Check if the queue is empty by checking length
  - size: Get the number of elements by checking length
- You may use either one or two queues for your implementation
- The stack should support the following operations:
  - push(element): Adds element to the top of the stack
  - pop(): Removes and returns the element at the top of the stack
  - top(): Returns the element at the top without removing it
  - isEmpty(): Returns true if the stack is empty, false otherwise
  - size(): Returns the number of elements in the stack

## Input Format

- Operations and parameters as arrays: ["push", "push", "top", "pop", "size"] with parameters [[1], [2], [], [], []]

## Output Format

- Array of results for each operation (null for operations that don't return values)

## Example

**Input:**

```
For operations: ["push", "push", "top", "pop", "size"] with parameters [[1], [2], [], [], []], the output should be [null, null, 2, 2, 1]
```

## Constraints

- Stack can be empty
- All operations should maintain LIFO order
- Use only queue operations for implementation

## Approach

1. Use two queues: q1 (main) and q2 (auxiliary)
2. For push: Add to q2, move all elements from q1 to q2, then swap queues
3. For pop: Simply dequeue from q1 (front element is always the top)
4. This maintains LIFO order using FIFO queues
5. Time complexity: O(n) for push, O(1) for other operations
