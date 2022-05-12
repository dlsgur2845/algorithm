import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**6+10)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
#
# def find_recur(a):
#     if parent[a] != a:
#         parent[a] = find_recur(parent[a])
#     return parent[a]

def find(a):
    while parent[a] != a:
        a = parent[a]
    return a

def union(a, b):
    a, b = find(a), find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(M):
    op, a, b = map(int, input().split())

    if op==0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')