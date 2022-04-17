import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    R, N = map(int, input().split())
    pascal = [[1]*(N+1) for _ in range(R+1)]

    for r in range(1, R+1):
        for n in range(r, N+1):
            if n==r:
                pascal[r][n]=1
            else:
                pascal[r][n] = pascal[r][n-1] + pascal[r-1][n-1]
    print(pascal[R][N])


