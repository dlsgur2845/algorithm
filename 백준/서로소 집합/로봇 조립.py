import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
parent = [i for i in range(10**6+1)]
rank = [1]*(10**6+1)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a==b: return
    if a>b: a,b = b,a
    parent[b]=a
    rank[a]+=rank[b]
    rank[b]=rank[a]

for _ in range(N):
    op = input().split()
    if len(op)==3:
        union(*map(int, op[1:]))
    else:
        print(rank[find(int(op[1]))])