import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

tree = defaultdict(list)
N = int(input())

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
Q = int(input())

for _ in range(Q):
    tp, node = map(int, input().split())
    if tp==2:
        print('yes')
    else:
        if len(tree[node])<=1:
            print('no')
        else:
            print('yes')