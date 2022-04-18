import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)] + [0]
dp = [0]*(N+2)
dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-3] + stairs[i - 1], dp[i - 2]) + stairs[i]
print(dp[N])