import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
S = [0]+list(map(lambda x: int(x) % 2, input().split()))
DP = [[0] * (N + 1) for _ in range(K+1)]

for k in range(1, K+1):
    for i in range(1, len(DP[0])):
        DP[k][i] = DP[k - 1][i - 1] if S[i] else DP[k - 1][i] + 1

print(max(DP[K]))