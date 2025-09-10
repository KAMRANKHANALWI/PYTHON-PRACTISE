def solveSudoku(board):
    """
    Solves a Sudoku puzzle in-place using a linear backtracking approach.
    
    Args:
        board (list[list[str]]): The 9x9 Sudoku board, represented as a list
                                   of lists of characters.
    """
    helper(board, 0, 0)


def helper(board, row, col):
    """
    The recursive helper function for the backtracking algorithm.
    It attempts to fill the board by moving sequentially from cell to cell.
    
    Args:
        board (list[list[str]]): The current state of the board.
        row (int): The current row to check.
        col (int): The current column to check.
    
    Returns:
        bool: True if a solution is found, False otherwise.
    """
    # Base case: if we have successfully placed digits up to the end of the board,
    # it means we have found a solution.
    if row == 9:
        return True

    # Calculate the coordinates of the next cell to check.
    next_row = row
    next_col = col + 1
    if next_col == 9:
        next_row += 1
        next_col = 0
    
    # If the current cell is not empty (it's a given number),
    # we skip it and move to the next cell.
    if board[row][col] != '.':
        return helper(board, next_row, next_col)

    # Try to place digits from 1 to 9 in the empty cell.
    for digit in range(1, 10):
        char_digit = str(digit)
        # Check if the current digit is a safe placement.
        if isSafe(board, row, col, char_digit):
            # Place the digit on the board.
            board[row][col] = char_digit
            
            # Recurse to the next cell. If the recursive call finds a solution,
            # we can return True immediately.
            if helper(board, next_row, next_col):
                return True
            
            # Backtrack: if the recursive call fails, undo the move by resetting
            # the cell to empty and try the next digit.
            board[row][col] = '.'

    # If no digit from 1-9 worked for this cell, this path is invalid.
    return False


# def helper(board):
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == '.':
#                 # Try placing digits from 1 to 9
#                 for digit in range(1, 10):
#                     char_digit = str(digit)
#                     if isSafe(board, row, col, char_digit):
#                         board[row][col] = char_digit
#                         if helper(board):
#                             return True
#                         # Backtrack: if the recursive call fails, undo the move
#                         board[row][col] = '.'
#                 return False  
#     return True  

def isSafe(board, row, col, digit):
    """
    Checks if it's safe to place a given digit at the specified position.
    
    Args:
        board (list[list[str]]): The Sudoku board.
        row (int): The row index.
        col (int): The column index.
        digit (str): The digit to check for safety.
        
    Returns:
        bool: True if the placement is safe, False otherwise.
    """
    # Check if the digit already exists in the same row.
    for j in range(9):
        if board[row][j] == digit:
            return False

    # Check if the digit already exists in the same column.
    for i in range(9):
        if board[i][col] == digit:
            return False

    # Check if the digit already exists in the 3x3 subgrid.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == digit:
                return False
                
    return True

# Example Usage:
# A solvable board with empty cells represented by '.'
board = [
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

print("Before solving:")
for row in board:
    print("".join(row))

solveSudoku(board)

print("\nAfter solving:")
for row in board:
    print("".join(row))