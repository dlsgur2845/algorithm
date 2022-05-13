import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent=[i for i in range(N+1)]
stack=[list(map(int, input().split())) for _ in range(M)]
stack=[(c, a, b) for a, b, c in stack]
stack.sort(key=lambda x:(-x[0]))

def find(a):
    global parent
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

answer=0
last=0
while stack:
    c, a, b = stack.pop()

    if find(a) != find(b):
        union(a, b)
        answer+=c
        last=c

print(answer-last)