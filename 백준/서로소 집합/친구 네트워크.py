import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a==b: return
    if rank[a] > rank[b]: a,b = b,a
    parent[b]=a
    rank[a]+=rank[b]
    rank[b]=rank[a]

T = int(input())
for _ in range(T):
    N = int(input())
    parent = dict()
    rank = defaultdict(lambda:1)

    for _ in range(N):
        a, b = input().split()
        if a not in parent: parent[a]=a
        if b not in parent: parent[b]=b

        union(a, b)
        print(rank[find(a)])