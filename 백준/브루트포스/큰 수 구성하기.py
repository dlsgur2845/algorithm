import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda : sys.stdin.readline().rstrip()

from itertools import product

N, K = map(int, input().split())
S = set(input().split())

answer=0
for i in range(1, len(str(N))+1):
    for p in [int(''.join(p)) for p in product(list(S), repeat=i)]:
        if p <= N:
            answer = answer if answer > p else p

print(answer)