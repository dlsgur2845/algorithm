import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
rank = [1]*(N+1)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if rank[a] > rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a]+=1

for _ in range(M):
    op, a, b = map(int, input().split())

    if op==0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')