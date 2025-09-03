# Asad's Wedding Gift

## Problem Background
BST construction from preorder traversal is essential in compiler design and expression parsing systems. Database management systems use this technique when rebuilding indexes from serialized data, and distributed systems employ it for efficient data structure reconstruction across network partitions. Companies like Oracle and PostgreSQL implement similar algorithms for index recovery operations.

## Problem Statement
Kamran and Shabab are invited to their best friend Asad's wedding. They need to decide on a gift to bring. Kamran loves arrays, while Shabab prefers trees, especially binary search trees (BSTs). They begin to argue about what to choose. After some discussion, they remembered that Asad likes a BST created from an array that is the preorder traversal of that BST.

Properties of a BST:
- The left subtree contains nodes with keys less than the node's key
- The right subtree contains nodes with keys greater than the node's key
- Both subtrees are also binary search trees, ensuring all nodes have distinct keys

## Input Format
* First line contains N (number of elements in the preorder array)
* Second line contains N space-separated integers representing the preorder traversal of a BST

## Output Format
* Print "YES" if a valid BST can be constructed from the given preorder traversal, "NO" otherwise

## Example
**Input:**
```
5
8 5 1 7 10
```

**Output:**
```
YES
```

**Explanation:**
The preorder traversal [8, 5, 1, 7, 10] can construct a valid BST:
```
    8
   / \
  5   10
 / \
1   7
```

## Constraints
* 1 <= preorder.length <= 100
* 1 <= preorder[i] <= 10^9
* All the values of preorder are unique

## Approach
1. **Range-based Construction**: Use bounds to determine valid node placement
2. **Recursive Building**: For each element, check if it fits current range constraints
3. **Index Management**: Track current position in preorder array globally
4. **Left/Right Subtree Construction**: Recursively build subtrees with updated bounds
5. **Time Complexity**: O(N) - each element processed once
6. **Space Complexity**: O(H) - recursion depth where H is tree height