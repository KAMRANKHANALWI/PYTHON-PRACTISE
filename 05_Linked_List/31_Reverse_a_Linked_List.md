# Reverse a Linked List

## Problem Background
Linked list reversal is a fundamental operation used in data processing, undo mechanisms, and algorithmic problem solving. This operation appears frequently in interview questions and real-world applications where you need to process data in reverse order while maintaining the original structure's integrity.

## Problem Statement
Implement a function that reverses a linked list in-place and returns the new head.

## Input Format
* An array representing the linked list values that will be converted to actual linked list nodes

## Output Format
* An array representing the reversed linked list

## Example
**Input:** `[1, 2, 3, 4, 5]`
**Output:** `[5, 4, 3, 2, 1]`

**Explanation:**
For the linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed list should be 5 -> 4 -> 3 -> 2 -> 1

**Note:** You only have to implement the function to reverse linked list, you will be getting head of the linked list. The linked list is made of Node objects with next pointers.

## Constraints
* Linked list can have 0 to 10^4 nodes
* Node values are integers
* Must reverse in-place (modify existing nodes, don't create new ones)

## Approach
1. Use three pointers: prev (initially null), curr (head), and next
2. For each node, store next node, reverse current's pointer to prev
3. Move prev and curr forward by one position
4. Continue until curr becomes null
5. Return prev as new head
6. This achieves O(n) time complexity with O(1) space complexity