import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[float('inf')]*N for _ in range(N)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a-1][b-1]=c
    graph[b-1][a-1]=c
for i in range(N):
    graph[i][i]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer=0
for i in range(N):
    total=0
    for j in range(N):
        if graph[i][j] <= M:
            total+=items[j]
    answer = max(answer, total)
print(answer)