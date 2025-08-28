# Find Kth Element from End

## Problem Background
Finding elements from the end of a data structure is common in systems where you need recent or last few items efficiently. This problem appears in log analysis, recent activity tracking, and data streaming applications where accessing the kth most recent item without knowing the total length beforehand is essential.

## Problem Statement
Implement a function that finds the value of the kth element from the end of a linked list in a single pass. If k is greater than the length of the list, return -1.

## Input Format
* An array representing the linked list values, followed by a pipe character '|' and the value of k
* Example: `[1, 2, 3, 4, 5]|1` where `[1, 2, 3, 4, 5]` is linked list, and `1` is k.

## Output Format
* Integer value of the kth element from the end, or -1 if k is invalid

## Example
**Input:** `[1, 2, 3, 4, 5]|2`
**Output:** `4`

**Explanation:**
For the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the function should return 4 (the 2nd element from the end)

**Note:** The linked list will consist of Node objects, each containing a value and a next pointer to the following node.

## Constraints
* Linked list can have 0 to 10^4 nodes
* k is a positive integer
* Must find element in single pass (O(n) time)
* 1-based indexing from the end

## Approach
1. Use two pointers technique with k-gap distance
2. Move first pointer k steps ahead from head
3. Move both pointers simultaneously until first reaches end
4. Second pointer will be at kth position from end
5. Return the value at second pointer
6. This achieves O(n) time complexity with O(1) space complexity