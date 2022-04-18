import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 방법1. combination 공식 사용
fact=[i for i in range(N+1)]
for i in range(2, N+1):
    fact[i] = fact[i] * fact[i-1]
print(fact[N]//fact[N-M]//fact[M])

# 방법2. pascal triangle 사용
pascal = [[1]*(N+1) for _ in range(M+1)]
for m in range(1, M+1):
    for n in range(m+1, N+1):
        pascal[m][n] = pascal[m][n-1] + pascal[m-1][n-1]
print(pascal[M][N])