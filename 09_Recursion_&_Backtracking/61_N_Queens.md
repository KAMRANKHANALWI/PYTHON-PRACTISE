# N-Queens

## Problem Background
The N-Queens problem is a classic constraint satisfaction problem used in AI and algorithm design. You need to place N chess queens on an N×N chessboard so that no two queens can attack each other. This problem demonstrates backtracking algorithms and is fundamental in understanding constraint satisfaction in computer science and game theory.

## Problem Statement
The N-Queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

## Input Format
* An integer n representing the size of the chessboard and number of queens

## Output Format
* An integer representing the number of distinct solutions

## Example
**Input:**
```
4
```

**Output:**
```
2
```

**Explanation:**
For a 4×4 board, there are exactly 2 distinct solutions where 4 queens can be placed without attacking each other.

## Constraints
* 1 ≤ n ≤ 9
* Queens attack horizontally, vertically, and diagonally
* All solutions must be distinct

## Approach
1. Use backtracking to try placing queens row by row
2. For each row, try placing queen in each column
3. Check if current placement conflicts with previous queens
4. If valid, recursively try next row
5. If all n queens placed successfully, increment solution count
6. Backtrack when no valid placement found in current row
7. This explores all possible configurations systematically