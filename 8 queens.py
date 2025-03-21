def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve(board, row):
    if row == len(board):
        return True
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row] = col  
            if solve(board, row + 1): 
                return True
            board[row] = -1 
    return False 
def printSolution(board):
    for row in board:
        print(" ".join("Q" if i == row else "." for i in range(len(board))))
def solve8Queens():
    board = [-1] * 8  
    if solve(board, 0):
        printSolution(board)
    else:
        print("No solution exists.")
solve8Queens()

