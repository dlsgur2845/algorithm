import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N=int(input())
dp=[0]*(N+1)
def pibo(n):
    assert n>=0
    if n<=1:
        return n
    if dp[n]>0:
        return dp[n]
    dp[n] = pibo(n-1) + pibo(n-2)
    return dp[n]
print(pibo(N))