import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
N = 11
dp = [1]*(N+1)
dp[2]=2
for i in range(3, N+1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(T):
    print(dp[int(input())])