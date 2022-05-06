import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
parent = [i for i in range(N)]

def find(a):
    global parent
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(int(input())):
    a, b = map(lambda x:int(x)-1, input().split())
    union(a, b)

for i in range(N):
    parent[i] = find(i)

print(sum([1 for node in parent if node==0])-1)