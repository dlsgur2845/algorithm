import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

from heapq import heappop, heappush

N, K = map(int, input().split())

# def dijkstra():
#     hq = [(0, N)]
#     costList = [float('inf')] * 100001
#     costList[N] = 0
#
#     while hq:
#         cur_cost, cur_node = heappop(hq)
#
#         if cur_cost > costList[cur_node]:
#             continue
#
#         for next_node, next_cost in [(cur_node*2, 0), (cur_node+1, 1), (cur_node-1, 1)]:
#             new_cost = cur_cost+next_cost
#             if 0 <= next_node <= 100000 and new_cost < costList[next_node]:
#                 costList[next_node] = new_cost
#                 heappush(hq, (new_cost, next_node))
#     return costList[K]
#
# print(dijkstra())

def dijkstra2():
    hq = [(0, N)]
    costList = [float('inf')] * 100001
    costList[N] = 0

    while hq:
        cur_cost, cur_node = heappop(hq)

        if cur_cost > costList[cur_node]:
            continue
        if cur_node == K:
            return costList[K]

        for next_node, next_cost in [(cur_node*2, 0), (cur_node+1, 1), (cur_node-1, 1)]:
            new_cost = cur_cost+next_cost
            if 0 <= next_node <= 100000 and new_cost < costList[next_node]:
                costList[next_node] = new_cost
                heappush(hq, (new_cost, next_node))

print(dijkstra2())