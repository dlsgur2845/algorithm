import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

exp = list(input())
stack=[]
answer=set()

pair=[]
for idx, e in enumerate(exp):
    if e == '(':
        stack.append(idx)
    elif e == ')':
        pair.append([stack.pop(), idx])

for i in range(len(pair)):
    for cases in combinations(pair,i+1):
        tmp=exp[:]
        for begin, end in cases:
            tmp[begin]=''
            tmp[end]=''
        answer.add(''.join(tmp))

print('\n'.join(sorted(answer)))