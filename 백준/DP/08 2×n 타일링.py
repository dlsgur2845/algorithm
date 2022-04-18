import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [1]*(N+1)
for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007
print(dp[N])