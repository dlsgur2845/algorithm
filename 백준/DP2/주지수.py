import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(2, M+1):
        board[r][c] += board[r][c-1]

for c in range(1, M+1):
    for r in range(2, N+1):
        board[r][c] += board[r-1][c]

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print(board[r2][c2]-board[r1-1][c2]-board[r2][c1-1]+board[r1-1][c1-1])