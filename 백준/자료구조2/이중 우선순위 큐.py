import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappush, heappop

for _ in range(int(input())):
    maxh = []
    minh = []
    alive= [False] * 1000001

    for i in range(int(input())):
        opor, oprnd = input().split()
        oprnd = int(oprnd)

        if opor == 'I':
            heappush(minh, (oprnd, i))
            heappush(maxh, (-oprnd, i))
            alive[i] = True
        elif minh:
            if oprnd == 1:
                alive[heappop(maxh)[1]]=False
            else:
                alive[heappop(minh)[1]]=False

            while minh and not alive[minh[0][1]]:
                heappop(minh)
            while maxh and not alive[maxh[0][1]]:
                heappop(maxh)

    if maxh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')