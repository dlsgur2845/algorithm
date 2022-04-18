import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0]*(N+3)
dp[1]=0
dp[2]=1
dp[3]=1
for i in range(4, N+1):
    dp[i] = min(dp[i-1],
                dp[i//2] if i%2==0 else float('inf'),
                dp[i//3] if i%3==0 else float('inf')) + 1
print(dp[N])