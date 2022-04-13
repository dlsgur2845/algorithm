import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack=[]
arr = [int(input()) for _ in range(n)]
i=1
answer=[]
for a in arr:
    while i <= a:
        answer.append('+')
        stack.append(i)
        i+=1
    if a==stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        answer=['NO']
        break

print('\n'.join(answer))