import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
graph = [[c if c==1 else float('inf') for c in list(map(int, input().split()))] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for g in graph:
    print(' '.join([str(int(c!=float('inf'))) for c in g]))