import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

from collections import defaultdict
from heapq import heappush, heappop

V, E = map(int, input().split())
begin = int(input())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra():
    costList=[float('inf')]*(V+1)
    costList[begin]=0
    hq = [(0, begin)]

    while hq:
        cur_cost, cur_node = heappop(hq)

        if costList[cur_node] < cur_cost:
            continue

        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost
            if costList[next_node] > new_cost:
                costList[next_node] = new_cost
                heappush(hq, (new_cost, next_node))

    return costList[1:]

for i in dijkstra():
    if i == float('inf'):
        print('INF')
    else:
        print(i)