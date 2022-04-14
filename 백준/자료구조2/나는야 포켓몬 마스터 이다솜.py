import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

pokemon = dict()
N, M = map(int, input().split())

for i in range(1, N+1):
    name = input()
    pokemon[name] = str(i)
    pokemon[str(i)] = name

for _ in range(M):
    print(pokemon[input()])