# Sudoku Solver

## Problem Background
Sudoku solving algorithms are essential in puzzle games, AI constraint satisfaction systems, and as benchmarks for algorithm efficiency. This problem demonstrates advanced backtracking with multiple constraints and is used in educational software, mobile gaming apps, and artificial intelligence research for constraint satisfaction problems.

## Problem Statement
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row
2. Each of the digits 1-9 must occur exactly once in each column  
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid

The '.' character indicates empty cells.

## Input Format
* A 9x9 2D array representing the Sudoku board
* Empty cells are represented by '.'
* Filled cells contain digits '1' to '9'

## Output Format
* Return True if the puzzle is solvable, False otherwise
* The input board should be modified in-place with the solution

## Example
**Input:**
```
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
```

**Output:**
```
True (and board is filled with solution)
```

## Constraints
* Board is always 9x9
* Given board is guaranteed to be valid
* There is exactly one solution for valid puzzles

## Approach
1. **Linear Cell Traversal**: Process cells sequentially from (0,0) to (8,8) using coordinate calculation
2. **Next Cell Calculation**: Compute next position as (row, col+1) wrapping to next row when needed
3. **Skip Filled Cells**: If current cell is not '.', move directly to next cell
4. **Try Digits 1-9**: For empty cells, attempt each digit and validate against constraints
5. **Constraint Validation**: Check row, column, and 3x3 subgrid for digit conflicts
6. **Recursive Solution**: If digit is valid, place it and recursively solve remaining board
7. **Backtracking**: If recursion fails, remove digit and try next possibility
8. **Base Case**: When row reaches 9, entire board is successfully filled

## Algorithm Steps
```
1. Start at position (0,0)
2. Base case: if row == 9, solution found, return True
3. Calculate next cell coordinates:
   - next_col = col + 1
   - If next_col == 9: next_row = row + 1, next_col = 0
4. If current cell is filled, skip to next cell
5. For each digit 1-9:
   a. Check if digit placement is safe (row, column, 3x3 box)
   b. If safe, place digit and recurse to next cell
   c. If recursion succeeds, return True
   d. If recursion fails, remove digit (backtrack)
6. If no digit works, return False
```

## Safety Check Details
- **Row Check**: Ensure digit doesn't exist in current row
- **Column Check**: Ensure digit doesn't exist in current column  
- **3x3 Subgrid Check**: Ensure digit doesn't exist in corresponding 3x3 box
- **Subgrid Calculation**: start_row = (row//3)*3, start_col = (col//3)*3

## Time and Space Complexity
- **Time Complexity**: O(9^(empty_cells)) in worst case, but pruning makes it much faster in practice
- **Space Complexity**: O(81) for recursion stack in worst case (all cells empty)
- **Recursion Depth**: O(81) maximum when all cells are empty