import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = list(map(int, input().split()))

for i in range(1, N):
    if dp[i-1] > 0:
        dp[i] = dp[i] + dp[i-1]
print(max(dp))