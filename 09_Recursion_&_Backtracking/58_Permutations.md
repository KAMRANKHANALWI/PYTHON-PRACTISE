# Permutations

## Problem Background
Permutation generation is fundamental in combinatorial optimization, cryptography, and scheduling systems. You need to generate all possible arrangements of elements for tasks like password generation, task scheduling optimization, tournament arrangements, and testing all possible configurations in system design.

## Problem Statement
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## Input Format
* An array of distinct integers

## Output Format
* A list of lists containing all possible permutations

## Example
**Input:**
```
[1, 2, 3]
```

**Output:**
```
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Explanation:**
All possible arrangements of [1, 2, 3] where each number appears exactly once in each permutation.

## Constraints
* 1 ≤ nums.length ≤ 6
* -10 ≤ nums[i] ≤ 10
* All the integers of nums are unique

## Approach
1. Use backtracking to build permutations element by element
2. At each position, try all unused elements from the original array
3. Track used elements to avoid duplicates within same permutation
4. When permutation length equals original array length, add to result
5. Backtrack by removing last element and marking it as unused
6. This generates all n! permutations systematically without duplicates