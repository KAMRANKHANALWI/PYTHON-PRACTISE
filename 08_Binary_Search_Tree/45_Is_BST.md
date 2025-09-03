# Can Kamran Drink a Cup of Chai?

## Problem Background
Binary Search Tree validation is a fundamental operation in database systems and search engines where maintaining sorted data structure integrity is crucial. Companies like Google and Amazon use BST validation in their indexing systems to ensure efficient data retrieval and maintain logarithmic search performance in their massive datasets.

## Problem Statement
Kamran loves chai a lot, but his grandfather believes that drinking too much chai is unhealthy. So, whenever Kamran asks for chai, his grandfather gives him a challenge. He hands Kamran a tree and asks him to determine if it is a binary search tree (BST). If Kamran answers correctly, he gets a cup of chai; if not, he ends up disappointed.

A binary search tree (BST) is a type of binary tree with these properties:
- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also be binary search trees

Note: From the above properties it naturally follows that each node has a distinct key

Please help Kamran's grandfather, as he is too old to decide if Kamran should get a cup of chai.

## Input Format
* First line contains N (number of nodes in the tree)
* Second line contains N space-separated integers representing the tree in level-order format (-1 for null nodes)

## Output Format
* Print "YES" if the tree is a valid BST, "NO" otherwise

## Example
**Input:**
```
7
8 3 10 1 6 14 4
```

**Output:**
```
YES
```

**Explanation:**
The given tree forms a valid BST where each node satisfies the BST property with respect to its ancestors.

## Constraints
* 0 <= Node.val <= 10^9

## Approach
1. **Range-based Validation**: For each node, maintain valid range bounds (min_val, max_val)
2. **Recursive Traversal**: Check if current node value lies within valid range
3. **Range Updates**: Update ranges for left (min_val to node.val) and right (node.val to max_val) subtrees
4. **Time Complexity**: O(N) - visit each node once
5. **Space Complexity**: O(H) - recursion stack depth where H is tree height