import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
K = int(input())

for r in range(1, N+1):
    for c in range(2, M+1):
        arr[r][c] += arr[r][c - 1]
for c in range(1, M+1):
    for r in range(2, N+1):
        arr[r][c] += arr[r - 1][c]

for _ in range(K):
    r1, c1, r2, c2 = map(lambda x:int(x), input().split())
    print(arr[r2][c2]-arr[r1-1][c2]-arr[r2][c1-1]+arr[r1-1][c1-1])