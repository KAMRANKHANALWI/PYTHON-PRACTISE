def solveNQueens(n):
    """
    Solves the N-Queens problem using a backtracking approach.
    
    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all unique solutions, where each solution is a list
              of strings representing the board configuration.
    """
    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    nQueens(board, 0, n, ans)
    
    # Convert the list of lists of characters into a list of strings for output
    result = []
    for solution in ans:
        result.append([''.join(row) for row in solution])
    return result


def isSafe(board, row, col, n):
    """
    Checks if it's safe to place a queen at the given position (row, col).
    
    Args:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check vertical
    # We only need to check the rows above the current row.
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        
    # Horizontal check is not needed.
    # The `nQueens` function places only one queen per row, so a horizontal conflict is impossible.
    # for j in range(n):
    #     if board[row][j] == 'Q':
    #         return False

    # Check left diagonal (upper-left)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal (upper-right)
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
        
    return True


def nQueens(board, row, n, ans):
    """
    Recursive backtracking function to find all solutions.
    
    Args:
        board (list): The current board configuration.
        row (int): The current row to place a queen.
        n (int): The size of the board.
        ans (list): The list to store all valid solutions.
    """
    # Base case: All queens are placed successfully
    if row == n:
        ans.append([r[:] for r in board])
        return

    # Iterate through each column to place a queen in the current row
    for j in range(n):
        if isSafe(board, row, j, n):
            # Place queen
            board[row][j] = 'Q'
            
            # Recurse to the next row
            nQueens(board, row + 1, n, ans)
            
            # Backtrack: remove the queen to explore other possibilities
            board[row][j] = '.'

# Example usage:
solutions = solveNQueens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()