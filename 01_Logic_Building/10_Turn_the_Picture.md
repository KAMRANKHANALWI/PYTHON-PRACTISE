# Turn the Picture

## Problem Background

You're a developer at Instagram building a new profile picture editor. When users upload square photos, they often need to be rotated to the correct orientation. Implement a feature that rotates a square photo by 90 degrees clockwise.

## Problem Statement

You're a developer at Instagram building a new profile picture editor. When users upload square photos, they often need to be rotated to the correct orientation. Implement a feature that rotates a square photo by 90 degrees clockwise.

## Input Format

- An integer (n) representing the size of the matrix.
- A 2D array (matrix) representing a square photo. Each element of the array contains an integer (for simplicity, think of it as a pixel value).
  - The size of the matrix is (n x n) where (1 <= n <= 10^3).
  - The matrix contains only integers between 0 and 255, inclusive (simulating RGB pixel values).

## Output Format

- Return the rotated matrix after rotating it 90 degrees clockwise.
- Your task is to just write a function to rotate the image.

## Example

**Input:**

```
3
1 2 3
4 5 6
7 8 9
```

**Output:**

```
7 4 1
8 5 2
9 6 3
```

## Constraints

- 1 ≤ n ≤ 10^3
- 0 ≤ matrix[i][j] ≤ 255

## Approach

1. First transpose the matrix (swap elements across diagonal)
2. Then reverse each row to complete 90-degree clockwise rotation
3. This achieves in-place rotation with O(n²) time complexity
4. Alternative: Create new matrix and map positions directly
