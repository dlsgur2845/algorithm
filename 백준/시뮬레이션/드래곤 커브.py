import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [[False]*101 for _ in range(101)]
mr, mc = [0, -1, 0, 1], [1, 0, -1, 0]

def dfs(curve, depth):
    global init_r, init_c

    if depth >= g:
        for d in curve:
            init_r += mr[d]
            init_c += mc[d]
            board[init_r][init_c]=True
    else:
        for d in curve[::-1]:
            d = (d+1)%4
            curve.append(d)
        dfs(curve, depth+1)

for _ in range(N):
    init_c, init_r, d, g = map(int, input().split())
    board[init_r][init_c]=True
    dfs([d], 0)

answer=0
for r in range(100):
    for c in range(100):
        if board[r][c]==board[r+1][c]==board[r][c+1]==board[r+1][c+1]==True:
            answer+=1
print(answer)
