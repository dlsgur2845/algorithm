import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    q = deque([(a, i) for i, a in enumerate(q)])

    cnt=0
    while q:
        max_item = max(q, key=lambda x:x[0])
        item = q.popleft()

        if item[0] < max_item[0]:
            q.append(item)
        else:
            cnt+=1
            if item[1] == M:
                print(cnt)
                break