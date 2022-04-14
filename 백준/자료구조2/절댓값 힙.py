import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappush, heappop

q = []
N = int(input())

for _ in range(N):
    x = int(input())

    if x==0:
        if q:
            print(heappop(q)[1])
        else:
            print(0)
    else:
        heappush(q, (abs(x), x))