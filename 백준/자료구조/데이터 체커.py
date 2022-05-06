import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [map(int, input().split()) for _ in range(N)]
arr = sorted([(x-r, x+r) for x, r in arr])

stack=[]
for a in arr:
    while stack and stack[-1][1] < a[0]:
        stack.pop()
    if stack and a[0] <= stack[-1][1] <= a[1]:
        print('NO')
        break
    stack.append(a)
else:
    print('YES')