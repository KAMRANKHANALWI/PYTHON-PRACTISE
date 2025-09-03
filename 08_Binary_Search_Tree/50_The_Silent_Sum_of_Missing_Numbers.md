# The Silent Sum of Missing Numbers

## Problem Background
Computing sums of missing elements in datasets is fundamental to statistical analysis, data validation systems, and financial auditing. Banks use similar algorithms to calculate missing transaction amounts, while data analytics platforms employ this technique to identify data gaps and their cumulative impact on aggregate metrics. This approach is essential for maintaining data integrity in large-scale distributed systems.

## Problem Statement
Kamran, Shabab, and Asad are now exploring the hidden sum of missing numbers in a BST. Shabab has constructed a BST using unique integers. Kamran challenges Asad with a new puzzle:

"Hey Asad! Between two numbers L and R, can you find the sum of all numbers that should exist in this range but are missing from the BST?"

Asad, ever the problem-solver, agrees but insists on using his optimized approach.

## Input Format
* First line contains N (number of nodes in the BST)
* Second line contains N space-separated integers representing the BST in level-order format (-1 for null nodes)
* Third line contains two integers L and R

## Output Format
* Return the sum of all missing numbers in the range [L, R]
* If no numbers are missing, return 0

## Example
**Input:**
```
4
5 2 7 -1 -1 -1 10
1 10
```

**Output:**
```
31
```

**Explanation:**
BST contains: {2, 5, 7, 10}
Range [1, 10] should ideally have: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Missing numbers: {1, 3, 4, 6, 8, 9}
Sum of missing numbers: 1 + 3 + 4 + 6 + 8 + 9 = 31

## Constraints
* The number of nodes in the tree is in the range [0, 100]
* 0 <= Node.val <= 10^9
* 1 <= L <= R <= 10^5

## Approach
1. **BST Range Traversal**: Efficiently collect values within [L, R] using BST properties
2. **Mathematical Sum Formula**: Calculate sum of complete range [L, R] using arithmetic series
3. **Present Sum Calculation**: Sum all BST values within the range
4. **Difference Computation**: Subtract present sum from complete range sum
5. **Time Complexity**: O(N) for BST traversal in worst case
6. **Space Complexity**: O(H) for recursion stack where H is tree height