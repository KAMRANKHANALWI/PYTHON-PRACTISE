# Min Stack

## Problem Background

You're building a financial trading platform that needs to track stock prices over time. For regulatory compliance, you need to quickly identify the minimum price seen at any point during a trading session. Design a special stack data structure that supports standard stack operations (push, pop, top) AND an additional operation getMin() that retrieves the minimum element in the stack, all in O(1) time complexity.

Your MinStack will help traders analyze price movements and comply with financial regulations that require real-time access to minimum prices!

## Problem Statement

You're building a financial trading platform that needs to track stock prices over time. For regulatory compliance, you need to quickly identify the minimum price seen at any point during a trading session. Design a special stack data structure that supports standard stack operations (push, pop, top) AND an additional operation getMin() that retrieves the minimum element in the stack, all in O(1) time complexity.

## Input Format

- A series of operations as arrays: ["push", value], ["pop"], ["top"], ["getMin"]

## Output Format

- Array of results for each operation (-1 for operations that don't return values)

## Example

**Input:**

```
[["push", 5], ["push", 2], ["push", 4], ["getMin"], ["pop"], ["getMin"]]
```

**Output:**

```
[-1, -1, -1, 2, 4, 2]
```

**Explanation:**

- Push 5, push 2, push 4, getMin → 2 (minimum value in stack)
- Pop → 4 (removed element), getMin → 2 (after -1 is popped)

## Methods Required

1. **push(val)**: Add an element to the top of the stack
2. **pop()**: Remove the element on top of the stack and return it. If the stack is empty, return null.
3. **top()**: Get the top element without removing it. If the stack is empty, return null.
4. **getMin()**: Retrieve the minimum element in the stack without removing it. If the stack is empty, return null.

## Constraints

- All operations must be O(1) time complexity
- Stack can be empty
- Values can be any integers

## Approach

1. Use two stacks: one for actual values, one for tracking minimums
2. When pushing, also push current minimum to min_stack
3. When popping, pop from both stacks simultaneously
4. getMin() simply returns top of min_stack
5. This achieves O(1) for all operations with O(n) space
