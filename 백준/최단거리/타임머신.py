# import sys
# sys.stdin = open('../input.txt', 'r')
#
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# from collections import defaultdict, deque
#
# N, M = map(int, input().split())
# graph = defaultdict(list)
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a-1].append((b-1, c))
#
# q = deque([0, 0])
# costList = [float('inf')]*N
# while q:
#     cost, From = q.pop()
#     if cost > costList[From]:
#         continue
#     for To, _cost in graph[From]:
#         