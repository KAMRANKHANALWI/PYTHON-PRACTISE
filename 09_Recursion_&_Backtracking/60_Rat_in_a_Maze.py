def helper(mat, r, c, path, ans):
    n = len(mat)
    
    # Boundary conditions and checks
    if r < 0 or c < 0 or r >= n or c >= n or mat[r][c] == 0 or mat[r][c] == -1:
        return
    
    # If destination is reached
    if r == n - 1 and c == n - 1:
        ans.append(path)
        return
    
    # Mark the cell as visited by changing its value
    mat[r][c] = -1
    
    # Explore all four directions
    helper(mat, r + 1, c, path + "D", ans)  # down
    helper(mat, r - 1, c, path + "U", ans)  # up
    helper(mat, r, c - 1, path + "L", ans)  # left
    helper(mat, r, c + 1, path + "R", ans)  # right
    
    # Unmark the cell (backtrack)
    mat[r][c] = 1

def findPath(mat):
    ans = []
    path = ""
    helper(mat, 0, 0, path, ans)
    return ans

# Example usage
mat = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

paths = findPath(mat)
print(paths)
