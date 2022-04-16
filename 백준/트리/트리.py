import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
rem = int(input())
tree = defaultdict(list)

for i, a in enumerate(arr):
    if i==rem or a==rem:
        continue
    tree[a].append(i)

def dfs(cur):
    if cur not in tree:
        return 1
    else:
        cnt=0
        for next in tree[cur]:
            cnt+=dfs(next)
        return cnt

print(dfs(-1) if -1 in tree else 0)