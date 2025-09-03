# The Curious Case of the Missing Numbers

## Problem Background
Finding missing elements in ordered datasets is crucial for data integrity systems in banking, inventory management, and sequence analysis in bioinformatics. Financial institutions use similar algorithms to detect missing transaction IDs, while e-commerce platforms employ this concept to identify gaps in product catalogs or order sequences, ensuring system reliability and audit compliance.

## Problem Statement
Saad, Shadman, and Asad are preparing for a coding competition, and they stumble upon an interesting puzzle while building a Binary Search Tree (BST) from a set of unique numbers. Shadman, the curious one, has inserted several numbers into the BST. Now, Saad challenges Asad with a question:

"Hey Asad! Between two given numbers L and R, can you find the K-th smallest number that's missing from the BST?"

Asad, being the problem-solver of the group, agrees but with a condition: Saad must allow him to use his own logic.

## Input Format
* First line contains N (number of nodes in the BST)
* Second line contains N space-separated integers representing the BST in level-order format (-1 for null nodes)
* Third line contains three integers L, R, and K

## Output Format
* Return the K-th smallest missing number in the range [L, R]
* If there aren't K missing numbers in the range, return -1

## Example
**Input:**
```
7
5 2 7 -1 -1 -1 10
1 10
3
```

**Output:**
```
4
```

**Explanation:**
BST contains: {2, 5, 7, 10}
Range [1, 10] should ideally have: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Missing numbers in range: {1, 3, 4, 6, 8, 9}
The 3rd smallest missing number is 4.

## Constraints
* The number of nodes in the tree is in the range [0, 100]
* 0 <= Node.val <= 10^9
* 1 <= L <= R <= 10^5
* 1 <= K <= 10^5

## Approach
1. **Inorder Traversal**: Extract BST values in sorted order
2. **Range Filtering**: Collect only values within [L, R] range
3. **Missing Number Detection**: Iterate through range and identify absent numbers
4. **K-th Element Selection**: Return the K-th missing number or -1 if insufficient
5. **Time Complexity**: O(N + (R-L+1)) for traversal and range checking
6. **Space Complexity**: O(N) for storing BST values and missing numbers