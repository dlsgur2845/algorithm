import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())
arr = list(map(int, input().split()))
arr = deque([(a, i+1) for i, a in enumerate(arr)])

answer=[]
while True:
    cur = arr.popleft()
    answer.append(cur[1])

    if not arr:
        break

    if cur[0] > 0:
        for i in range(cur[0]-1):
            arr.append(arr.popleft())
    else:
        for i in range(-cur[0]):
            arr.appendleft(arr.pop())

print(' '.join(list(map(str, answer))))