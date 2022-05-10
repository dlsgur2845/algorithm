import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

from collections import defaultdict, deque

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(begin):
    costList = [float('inf')]*(N+1)
    costList[begin] = 0
    dq = deque([(0, begin)])

    while dq:
        cur_cost, cur_node = dq.popleft()

        if cur_cost < costList[cur_node]:
            continue
        for next_node in graph[cur_node]:
            new_cost = cur_cost + 1
            if costList[next_node] > new_cost:
                costList[next_node] = new_cost
                dq.append((new_cost, next_node))

    return costList

answer = [str(i) for i, dist in enumerate(dijkstra(X)) if dist==K]
print('\n'.join(answer) if answer else -1)
