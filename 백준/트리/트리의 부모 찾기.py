import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

tree=defaultdict(list)
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)
tree[0]=[1]

parent=[-1]*(N+1)

# sys.setrecursionlimit(110000)
# def dfs(cur):
#     global parent
#     for next in tree[cur]:
#         if parent[next]==-1:
#             parent[next]=cur
#             dfs(next)
#
# dfs(0)
#
# for par in parent[2:]:
#     print(par)

def bfs(cur):
    global parent
    q = deque([cur])

    while q:
        cur = q.popleft()

        for next in tree[cur]:
            if parent[next]==-1:
                parent[next]=cur
                q.append(next)

bfs(0)
for par in parent[2:]:
    print(par)