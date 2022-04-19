import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))
dp = S[:]

for i in range(1, N):
    for j in range(i):
        if S[j] < S[i]:
            dp[i] = max(dp[i], dp[j] + S[i])
print(max(dp))