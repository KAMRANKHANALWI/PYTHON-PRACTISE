# Don't Let Them Lose

## Problem Background
Greater Sum Tree transformation is used in financial systems for calculating cumulative wealth distributions and in game development for score aggregation systems. Companies like Bloomberg use similar tree transformations to compute running totals of financial instruments, while gaming companies apply this concept to leaderboard calculations and progressive reward systems.

## Problem Statement
Saad and Shadman are participating in a coding contest where Asad is the problem setter. Asad is known for presenting challenging problems to the participants, which made Saad and Shadman feel nervous and worried about losing the contest.

The problem assigned to Saad and Shadman is as follows:

Given the root of a Binary Search Tree (BST), convert it into a Greater Sum Tree (GST). In this transformation, each key in the original BST should be replaced with the sum of the original key and all keys greater than it in the BST.

To clarify, a Binary Search Tree (BST) is a tree that adheres to the following constraints:
- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key  
- Both the left and right subtrees must also be binary search trees

Help Saad and Shadman win the contest by solving this problem.

## Input Format
* First line contains N (number of nodes in the tree)
* Second line contains N space-separated integers representing the BST in level-order format (-1 for null nodes)

## Output Format
* Print "YES" if the transformation is successful and matches expected result, "NO" otherwise

## Example
**Input:**
```
9
4 1 6 0 2 5 7 -1 3 -1 -1 -1 -1 -1 8
```

**Output:**
```
YES
```

**Explanation:**
Original BST: [4, 1, 6, 0, 2, 5, 7, null, 3, null, null, null, null, null, 8]
After GST transformation: [30, 36, 21, 36, 35, 26, 15, null, 33, null, null, null, null, null, 8]

Each node's value becomes the sum of its original value and all greater values in the tree.

## Constraints
* The number of nodes in the tree is in the range [1, 100]
* 0 <= Node.val <= 10^5
* All the values in the tree are unique

## Approach
1. **Reverse Inorder Traversal**: Visit nodes in descending order (right → root → left)
2. **Running Sum Calculation**: Maintain a running total of all visited nodes
3. **Node Value Update**: Replace each node's value with the accumulated sum
4. **Time Complexity**: O(N) - visit each node exactly once
5. **Space Complexity**: O(H) - recursion stack depth where H is tree height