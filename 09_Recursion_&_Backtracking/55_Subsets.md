# Subsets

## Problem Background
Subset generation is fundamental in combinatorics, feature selection in machine learning, and power set operations in database systems. You need to generate all possible combinations of elements for tasks like selecting optimal features for ML models, creating test case combinations, configuration management, and analyzing all possible states in system design.

## Problem Statement
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Input Format
* An array of unique integers

## Output Format
* A list of lists containing all possible subsets including the empty subset

## Example
**Input:**
```
[1, 2, 3]
```

**Output:**
```
[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

**Explanation:**
All possible subsets of [1, 2, 3] including the empty set. Each element can either be included or excluded from each subset.

## Constraints
* 1 ≤ nums.length ≤ 10
* -10 ≤ nums[i] ≤ 10
* All the numbers of nums are unique

## Approach
1. Use backtracking to make binary choices for each element (include/exclude)
2. At each position, try both including and excluding current element
3. Base case: when all elements have been considered, add current subset
4. Use index parameter to avoid considering same element multiple times
5. This generates all 2^n subsets systematically
6. Alternative: Use bit manipulation where each bit represents include/exclude