import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

stack=[]
answer=[]
for i, a in enumerate(arr):
    while stack and stack[-1][0] < a:
        stack.pop()
    answer.append(stack[-1][1] if stack else 0)
    stack.append((a, i+1))

print(' '.join(str(i) for i in answer))