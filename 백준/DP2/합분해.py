import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = [[1]*(N+1) for _ in range(K)]
#
# for k in range(1, K):
#     for n in range(1, N+1):
#         arr[k][n] = (arr[k-1][n] + arr[k][n-1])%1000000000
# print(arr[-1][-1])

fact = [1]*(N+K)
for i in range(2, N+K):
    fact[i] = fact[i-1]*i
A = N+K-1
B = N
print((fact[A]//fact[A-B]//fact[B])%1000000000)