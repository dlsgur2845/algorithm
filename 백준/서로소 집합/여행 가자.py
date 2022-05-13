import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find(a):
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a==b: return
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j]:
            union(i+1, j+1)

travel = set(map(lambda x:find(int(x)), input().split()))
print('YES' if len(travel)==1 else 'NO')