import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heapify, heapreplace
N = int(input())
q=list(map(int, input().split()))

heapify(q)
for _ in range(N-1):
    for num in input().split():
        num = int(num)

        if num > q[0]:
            heapreplace(q, num)

print(q[0])