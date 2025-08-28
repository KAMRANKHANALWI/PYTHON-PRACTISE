# Detect Cycle in a Linked List

## Problem Background
Cycle detection in data structures is critical for preventing infinite loops, memory leaks, and ensuring system stability. This problem appears in garbage collection algorithms, distributed systems validation, and data integrity checks where circular references must be identified to prevent system failures.

## Problem Statement
Implement a function that detects if a linked list contains a cycle. A cycle occurs when a node's next pointer points to a node that was previously visited. Your function should return true if a cycle is detected, and false otherwise. Your function return data type should be boolean.

## Input Format
* An array representing the linked list values, followed by a pipe character '|' and a number indicating the position (0-indexed) to which the last node connects, or -1 if there is no cycle
* Example: `[1, 2, 3, 4, 5]|1` means the last node with value 5 connects back to the node at index 1 (value 2), creating a cycle

## Output Format
* Boolean value: "true" if cycle exists, "false" otherwise

## Example
**Input:** `[1, 2, 3, 4, 5]|1`
**Output:** `"true"`

**Explanation:**
For a linked list with nodes 1 -> 2 -> 3 -> 4 -> 5 that loops back to node 2, the function should return true (the last node with value 5 connects back to the node at index 1, which has value 2, creating a cycle)

**Note:** The linked list is made of Node objects with next pointers, potentially forming a cycle where a node points back to a previous node.

## Constraints
* Linked list can have 0 to 10^4 nodes
* Node values can be any integers
* Cycle position can be -1 (no cycle) or valid index
* Must detect cycle efficiently without modifying the list

## Approach
1. Use Floyd's Cycle Detection Algorithm (Tortoise and Hare)
2. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
3. If there's a cycle, fast will eventually meet slow
4. If fast reaches null, there's no cycle
5. This achieves O(n) time complexity with O(1) space complexity