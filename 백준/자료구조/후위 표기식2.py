import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
eq = input()
idx=0
stack=[]
d=dict()

for e in eq:
    if e.isalpha() and e not in d.keys():
        d[e]=input()

for e in eq:
    if e.isalpha():
        stack.append(d[e])
    else:
        b = stack.pop()
        a = stack.pop()
        c = eval(f'{a}{e}{b}')
        stack.append(c)

print(f'{stack[0]:.2f}')