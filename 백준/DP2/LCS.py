import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

str1 = input()
str2 = input()
R, C = len(str1), len(str2)
board = [[0]*(C+1) for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        if str1[r - 1] == str2[c - 1]:
            board[r][c] = board[r-1][c-1] + 1
        else:
            board[r][c] = max(board[r-1][c], board[r][c-1])
print(board[-1][-1])