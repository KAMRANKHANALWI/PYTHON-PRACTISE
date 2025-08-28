# Palindrome Linked List

## Problem Background
In data validation systems, you often need to verify if sequences maintain symmetry properties. Palindrome detection in linked lists is crucial for data integrity checks, pattern recognition algorithms, and validation systems where you need to determine if a sequence reads the same forward and backward.

## Problem Statement
Implement a function that determines if a linked list is a palindrome (reads the same forward and backward).

**Note:** Each node in the linked list has a value property containing the node's data and a next property pointing to the next node in the list. The function takes the head of the list as a parameter and should return true if the list is a palindrome, or false otherwise. The input format is an array representing the list values, and the output is a boolean value.

## Input Format
* An array representing the linked list values
* Each element becomes a node with value and next pointer

## Output Format
* Boolean value: true if palindrome, false otherwise

## Example
**Input:** `[1, 2, 2, 1]`
**Output:** `true`

**Input:** `[1, 2, 3]`
**Output:** `false`

**Explanation:**
* For the linked list 1 -> 2 -> 2 -> 1, the function should return true
* For the linked list 1 -> 2 -> 3, the function should return false

## Constraints
* Linked list can have 0 to 10^5 nodes
* Node values are integers
* Space complexity should be optimized

## Approach
1. Use slow/fast pointer technique to find the middle of the list
2. Reverse the second half of the linked list
3. Compare first half with reversed second half node by node
4. If all nodes match, the list is a palindrome
5. This achieves O(n) time complexity with O(1) space complexity