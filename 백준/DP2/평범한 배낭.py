import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
items = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, K+1):
        w, v = items[r-1]
        if c >= w:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-w]+v)
        else:
            dp[r][c] = dp[r-1][c]

print(dp[-1][-1])