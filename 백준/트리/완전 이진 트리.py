import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))

tree=defaultdict(list)
def dfs(l, r, depth):
    global tree
    if r<l:
        return
    m = (l+r)//2
    tree[depth].append(arr[m])
    dfs(l, m-1, depth+1)
    dfs(m+1, r, depth+1)

dfs(0, len(arr)-1, 1)
for _, node in tree.items():
    print(' '.join(map(str, node)))