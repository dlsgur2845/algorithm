import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [4]*(N+1)
dp[0]=0
dp[1]=1
for i in range(2, N+1):
    for j in range(1, int(i**0.5)+1):
        if dp[i] > dp[i-j*j]:
            dp[i] = dp[i-j*j]
    dp[i]+=1
print(dp[N])