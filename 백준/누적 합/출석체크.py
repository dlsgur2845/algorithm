import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, Q, M = map(int, input().split())
sleep = [False]*(N+3)
answer = [0]*3+[1]*N
for i in map(int, input().split()):
    sleep[i]=True
for i in map(int, input().split()):
    if not sleep[i]:
        for j in range(i, N+3, i):
            if not sleep[j]:
                answer[j]=0

for i in range(4, N+3):
    answer[i] += answer[i-1]
for _ in range(M):
    S, E = map(int, input().split())
    print(answer[E]-answer[S-1])