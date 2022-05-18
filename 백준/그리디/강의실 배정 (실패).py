import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappush, heapreplace

N = int(input())
visit = [False]*N
cls = [list(map(int, input().split())) for _ in range(N)]
cls.sort()

hq=[]
heappush(hq, cls[0][1])
for i in range(1, N):
    if cls[i][0] < hq[0]:
        heappush(hq, (cls[i][1]))
    else:
        heapreplace(hq, cls[i][1])
print(len(hq))