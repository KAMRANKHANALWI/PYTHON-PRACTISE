# Rat in a Maze

## Problem Background
You're developing a pathfinding algorithm for autonomous robots navigating through warehouse layouts, game AI for maze-solving puzzles, or route planning systems for emergency evacuation scenarios. This classic backtracking problem simulates finding all possible paths through obstacles, which is fundamental in robotics, game development, and logistics optimization.

## Problem Statement
A rat is placed at the top-left corner of a maze (0,0) and needs to reach the bottom-right corner (n-1,n-1). The rat can move in four directions: Down, Up, Left, Right (represented as D, U, L, R). Find all possible paths from source to destination.

The maze is represented by a binary matrix where:
- 1 represents a free cell (rat can move)
- 0 represents a blocked cell (rat cannot move)
- The rat cannot revisit a cell in the same path

## Input Format
* An n×n binary matrix representing the maze
* Source: (0,0) - top-left corner
* Destination: (n-1,n-1) - bottom-right corner

## Output Format
* A list of strings, each representing a valid path using characters D, U, L, R
* If no path exists, return an empty list

## Example
**Input:**
```
[
  [1, 0, 0, 0],
  [1, 1, 0, 1],
  [1, 1, 0, 0],
  [0, 1, 1, 1]
]
```

**Maze Visualization:**
```
S = Start (0,0), E = End (3,3), 1 = Free path, 0 = Blocked

    0   1   2   3
  ┌───┬───┬───┬───┐
0 │ S │ 0 │ 0 │ 0 │
  ├───┼───┼───┼───┤
1 │ 1 │ 1 │ 0 │ 1 │
  ├───┼───┼───┼───┤
2 │ 1 │ 1 │ 0 │ 0 │
  ├───┼───┼───┼───┤
3 │ 0 │ 1 │ 1 │ E │
  └───┴───┴───┴───┘

Path 1: DDRDRR
S → (1,0) → (2,0) → (2,1) → (1,1) → (3,1) → (3,2) → E

Path 2: DRDDRR  
S → (1,0) → (1,1) → (2,1) → (2,0) → (3,1) → (3,2) → E
```

**Output:**
```
["DDRDRR", "DRDDRR"]
```

**Explanation:**
The rat starts at (0,0) and needs to reach (3,3). There are two valid paths:
1. Down→Down→Right→Down→Right→Right
2. Down→Right→Down→Down→Right→Right

## Constraints
* 1 ≤ n ≤ 8
* Matrix contains only 0s and 1s
* Source (0,0) and destination (n-1,n-1) are always 1
* Rat cannot move diagonally
* Rat cannot revisit cells in the same path
* Output paths should be lexicographically sorted

## Step-by-Step Path Visualization

### Path 1: "DDRDRR"
```
Step 0: Start at (0,0)        Step 1: Move D to (1,0)       Step 2: Move D to (2,0)
    0   1   2   3                 0   1   2   3                 0   1   2   3
  ┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐
0 │ ★ │ 0 │ 0 │ 0 │           0 │ X │ 0 │ 0 │ 0 │           0 │ X │ 0 │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
1 │ 1 │ 1 │ 0 │ 1 │           1 │ ★ │ 1 │ 0 │ 1 │           1 │ X │ 1 │ 0 │ 1 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
2 │ 1 │ 1 │ 0 │ 0 │           2 │ 1 │ 1 │ 0 │ 0 │           2 │ ★ │ 1 │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
3 │ 0 │ 1 │ 1 │ 1 │           3 │ 0 │ 1 │ 1 │ 1 │           3 │ 0 │ 1 │ 1 │ 1 │
  └───┴───┴───┴───┘             └───┴───┴───┴───┘             └───┴───┴───┴───┘

Step 3: Move R to (2,1)       Step 4: Move D to (1,1)       Step 5: Move R to (3,1)
    0   1   2   3                 0   1   2   3                 0   1   2   3
  ┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐
0 │ X │ 0 │ 0 │ 0 │           0 │ X │ 0 │ 0 │ 0 │           0 │ X │ 0 │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
1 │ X │ 1 │ 0 │ 1 │           1 │ X │ ★ │ 0 │ 1 │           1 │ X │ X │ 0 │ 1 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
2 │ X │ ★ │ 0 │ 0 │           2 │ X │ X │ 0 │ 0 │           2 │ X │ X │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
3 │ 0 │ 1 │ 1 │ 1 │           3 │ 0 │ 1 │ 1 │ 1 │           3 │ 0 │ ★ │ 1 │ 1 │
  └───┴───┴───┴───┘             └───┴───┴───┴───┘             └───┴───┴───┴───┘

Step 6: Move R to (3,2)       Step 7: Move R to (3,3) - GOAL!
    0   1   2   3                 0   1   2   3
  ┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐
0 │ X │ 0 │ 0 │ 0 │           0 │ X │ 0 │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
1 │ X │ X │ 0 │ 1 │           1 │ X │ X │ 0 │ 1 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
2 │ X │ X │ 0 │ 0 │           2 │ X │ X │ 0 │ 0 │
  ├───┼───┼───┼───┤             ├───┼───┼───┼───┤
3 │ 0 │ X │ ★ │ 1 │           3 │ 0 │ X │ X │ ★ │
  └───┴───┴───┴───┘             └───┴───┴───┴───┘

Legend: ★ = Current position, X = Visited cell, 0 = Blocked, 1 = Free cell
```

## Approach
1. **Backtracking Strategy**: Explore all possible paths recursively
2. **Four Directions**: At each cell, try moving Down, Left, Right, Up (lexicographical order)
3. **Boundary Check**: Ensure the rat doesn't go out of maze boundaries
4. **Obstacle Check**: Verify the cell is not blocked (value = 1)
5. **Visited Check**: Ensure the cell hasn't been visited in current path
6. **Path Tracking**: Build path string and maintain visited matrix
7. **Base Case**: When rat reaches destination (n-1,n-1), add path to result
8. **Backtrack**: Mark cell as unvisited when returning from recursion

## Algorithm Steps
```
1. Start from (0,0) with empty path and visited matrix
2. Mark current cell as visited
3. If current cell is destination, add path to result
4. For each direction (D,L,R,U):
   a. Calculate new position
   b. Check if move is valid (within bounds, not blocked, not visited)
   c. If valid, recursively explore with updated path
5. Mark current cell as unvisited (backtrack)
6. Return all found paths
```