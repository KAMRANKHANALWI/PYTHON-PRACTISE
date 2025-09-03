# Shadman and the Missing Median

## Problem Background
Finding medians of missing data points is crucial in statistical analysis, quality control systems, and anomaly detection in large datasets. Healthcare systems use similar algorithms to identify median gaps in patient data sequences, while financial institutions employ this technique for detecting median anomalies in transaction patterns, ensuring robust statistical analysis even with incomplete data.

## Problem Statement
Saad, Shadman, and Kamran are back with another BST brain-teaser! Kamran builds a BST with unique integers. Shadman, always the prankster, challenges Saad:

"Hey Saad! Between two numbers L and R, what's the median of all the numbers missing from your BST? If there are two medians, pick the smaller one!"

Saad, determined to outsmart Shadman, gets to work!

Help Saad outsmart Shadman.

## Input Format
* First line contains M (number of nodes in the BST)
* Second line contains M space-separated integers representing the BST in level-order format (-1 for null nodes)
* Third line contains two integers L and R

## Output Format
* Return the median of all missing numbers in the range [L, R]
* If there are no missing numbers, return -1
* If there are two medians (even count), return the smaller one

## Example
**Input:**
```
4
5 2 7 -1 -1 -1 10
1 10
```

**Output:**
```
4
```

**Explanation:**
BST contains: {2, 5, 7, 10}
Range [1, 10] should ideally have: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Missing numbers: {1, 3, 4, 6, 8, 9}
Count = 6 (even), so median is the smaller of the two middle values
Middle positions: 3rd and 4th elements = 4 and 6
Return smaller: 4

## Constraints
* The number of nodes in the tree is in the range [0, 100]
* 0 <= Node.val <= 10^9
* 1 <= L <= R <= 10^5

## Approach
1. **BST Inorder Traversal**: Extract values in sorted order
2. **Range Filtering**: Collect BST values within [L, R]
3. **Missing Numbers Collection**: Find all numbers in [L, R] not present in BST
4. **Median Calculation**: For odd count, return middle element; for even count, return smaller of two middle elements
5. **Time Complexity**: O(N + (R-L+1)) for traversal and range processing
6. **Space Complexity**: O(N) for storing BST values and missing numbers