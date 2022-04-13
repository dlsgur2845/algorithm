import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

arr = input()
answer=0
stack=0

for i, a in enumerate(arr):
    if a == ')':
        stack-=1
        if arr[i-1] == ')':
            answer += 1
        else:
            answer += stack
    else:
        stack+=1
print(answer)