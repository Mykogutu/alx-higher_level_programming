#!/usr/bin/python3
import sys

def nqueens(n):
    if not isinstance(n, int) or n < 4:
        return "N must be a number >= 4"
    res = []
    def backtrack(board, row):
        if row == n:
            res.append(board)
            return
        for i in range(n):
            if is_valid(board, row, i):
                backtrack(board + [i], row + 1)

    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    backtrack([], 0)
    return res

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

result = nqueens(n)
if isinstance(result, str):
    print(result)
    sys.exit(1)

for i, board in enumerate(result):
    print("Solution {}:".format(i + 1))
    for j in range(n):
        row = ['Q' if k == board[j] else '.' for k in range(n)]
        print(" ".join(row))
    print("")

