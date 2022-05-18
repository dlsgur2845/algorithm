import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict

N, M, K = map(int, input().split())
costList = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a>b: a, b = b,a
    parent[b]=a

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

minCost = defaultdict(lambda:10000000)
for i in range(1, N+1):
    if minCost[find(i)] > costList[i]:
        minCost[find(i)] = costList[i]
total = sum(minCost.values())
print(total if total <= K else 'Oh no')