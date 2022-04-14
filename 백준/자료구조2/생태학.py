import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict
trees = defaultdict(int)
total=0
while True:
    tree = input()
    if not tree:
        break
    trees[tree]+=1
    total+=1

answer = sorted([f'{tree} {trees[tree] / total * 100:.4f}' for tree in trees.keys()])
print('\n'.join(answer))