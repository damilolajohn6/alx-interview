import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve_util(col):
        if col == N:
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_util(col + 1)
                board[i][col] = 0

    solve_util(0)
    return solutions

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solutions = solve_nqueens(N)
for solution in solutions:
    print(solution)
