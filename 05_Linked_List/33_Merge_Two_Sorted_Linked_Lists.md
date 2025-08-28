# Merge Two Sorted Linked Lists

## Problem Background
Merging sorted data structures is fundamental in database operations, distributed systems, and data processing pipelines. This problem simulates merging two sorted datasets while maintaining order, which is essential for efficient data combination in real-world applications like merging user activity logs or combining sorted search results.

## Problem Statement
Implement a function that merges two sorted linked lists into a single sorted linked list. The new list should be made by splicing together the nodes of the first two lists.

## Input Format
* Two arrays separated by '|' representing the two sorted linked lists
* Example: `[1,3,5]|[2,4,6]` where first list is `[1,3,5]` and second is `[2,4,6]`

## Output Format
* An array representing the merged sorted linked list

## Example
**Input:** `[1,3,5]|[2,4,6]`
**Output:** `[1,2,3,4,5,6]`

**Explanation:**
For the linked lists 1 -> 3 -> 5 and 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6

**Note:** That list1 and list2 parameters are head nodes of already-sorted lists
* The structure of the nodes (value + next pointer)
* That the lists are pre-sorted by the value property
* That the merge should be done by reconnecting existing nodes, not creating new ones
* That the result should preserve the sorted order and return new head.

## Constraints
* Both lists can have 0 to 50 nodes
* Node values are integers (-100 ≤ value ≤ 100)
* Both input lists are sorted in non-decreasing order
* Must reuse existing nodes (no new node creation)

## Approach
1. Use a dummy node to simplify edge cases
2. Use two pointers to traverse both lists simultaneously
3. Compare values and attach smaller node to result
4. Move pointer of the selected list forward
5. Attach remaining nodes when one list is exhausted
6. Return dummy.next as new head
7. This achieves O(m+n) time complexity with O(1) space