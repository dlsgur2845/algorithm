import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
graph = [[float('inf')]*V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1]=c

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = min([graph[i][i] for i in range(V)])
if ans == float('inf'):
    print(-1)
else:
    print(ans)