#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens(board, row, N):
    if row == N:
        for i in range(N):
            print("".join(board[i]))
        print()
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, N)
            board[row][col] = '.'

def nqueens(N):
    """
    Solves the N-queens puzzle.

    Determines all possible solutions to placing N
    non-attacking queens on an NxN chessboard.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    nqueens(sys.argv[1])
