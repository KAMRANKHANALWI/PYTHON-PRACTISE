# Sort a Stack

## Problem Background

You're designing a document management system where files are processed in a specific order. The system has a constraint: it can only interact with documents at the top of the stack (like a physical pile of papers). You need to sort the entire stack of documents by their priority number, but you can only use the basic stack operations: push (add to top), pop (remove from top), and a temporary storage stack.

This mirrors how many real-world systems with limited access patterns (like network packet processing or hardware memory constraints) need to work!

## Problem Statement

You're designing a document management system where files are processed in a specific order. The system has a constraint: it can only interact with documents at the top of the stack (like a physical pile of papers). You need to sort the entire stack of documents by their priority number, but you can only use the basic stack operations: push (add to top), pop (remove from top), and a temporary storage stack.

## Input Format

- A stack with elements [5, 2, 9, 1, 5] (where 5 is at the top)

## Output Format

- Sorted stack [1, 2, 5, 5, 9] (where 1 is at the top and 9 is at the bottom)

## Example

**Input:**

```
[5, 2, 9, 1, 5]
```

**Output:**

```
[1, 2, 5, 5, 9]
```

**Explanation:**
The stack is sorted in ascending order with smallest element at top.

## Constraints

- Stack can contain 0 to 10^3 elements
- Elements are integers
- Only stack operations allowed: push, pop
- Can use one additional temporary stack

## Approach

1. Use a helper stack to maintain sorted order
2. Pop elements from original stack one by one
3. For each element, find correct position in helper stack
4. Move larger elements back to original stack temporarily
5. Insert current element at correct position
6. Reverse the final result to get ascending order
7. This achieves O(n²) time complexity with O(n) space
