import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappop, heapify

N = int(input())
M = int(input())
hq = [list(map(int, input().split())) for _ in range(M)]
hq = [(c, a, b) for a, b, c in hq]
heapify(hq)
parent = [i for i in range(N+1)]

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

answer=0
while hq:
    c, a, b = heappop(hq)
    if find(a) != find(b):
        union(a, b)
        answer+=c
print(answer)