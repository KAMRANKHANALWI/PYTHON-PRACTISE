# Binary Bounty: The Sum Quest

## Problem Background

Finding maximum sum BSTs within binary trees is crucial for database optimization, financial portfolio analysis, and resource allocation systems. Investment firms use similar algorithms to identify optimal asset allocation subtrees that maximize returns while maintaining balanced risk profiles. This technique is also applied in network topology optimization where BST properties ensure efficient routing while maximizing throughput.

## Problem Statement

In the bustling city of Techville, friends Abdullah and Kamran loved tackling coding challenges at their favourite cafe, "The Code Nook."

One rainy day, Abdullah excitedly shared a LeetLab problem with Kamran. "We need to find the maximum sum of keys in a Binary Search Tree (BST) within a given binary tree", he explained. "The subtree must be a valid BST, with all left nodes having keys less than the root and all right nodes having keys greater".

Kamran nodded, "So we check each part of the tree, ensure it's a BST, and calculate the sum. We must also consider special cases, like negative values or single-node trees".

Help them to solve the problem.

## Input Format

- First line contains N (number of nodes in the binary tree)
- Second line contains N space-separated integers representing the tree in level-order format (-1 for null nodes)

## Output Format

- Return the maximum sum of keys found in any Binary Search Tree (BST) within the given binary tree

## Example

**Input:**

```
7
1 4 3 2 4 2 5
```

**Output:**

```
20
```

**Explanation:**
Among all the Binary Search Trees (BSTs) within the given binary tree, the highlighted BST yields the maximum sum of 20 (3 + 2 + 5 + 4 + 6).

## Constraints

- The number of nodes in the tree is in the range [1, 100]
- -10^9 <= Node.val <= 10^9

## Approach

1. **Post-order Traversal**: Process children before parent to validate BST property
2. **BST Validation**: Check if left subtree max < root < right subtree min
3. **Sum Calculation**: Maintain running sum for valid BST subtrees
4. **Global Maximum**: Track maximum BST sum found across all subtrees
5. **State Propagation**: Return (isBST, minVal, maxVal, sum) for each subtree
6. **Time Complexity**: O(N) - visit each node once
7. **Space Complexity**: O(H) - recursion depth where H is tree height
