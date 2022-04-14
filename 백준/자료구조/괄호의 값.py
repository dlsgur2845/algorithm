import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

arr = input()
stack=[]
cnt=1
answer=0

for i, a in enumerate(arr):
    if a=='(':
        cnt*=2
        stack.append(a)
    elif a=='[':
        cnt*=3
        stack.append(a)
    elif a==')':
        if not stack or stack[-1]!='(':
            answer=0
            break
        if arr[i-1]=='(':
            answer+=cnt
        cnt//=2
        stack.pop()
    elif a==']':
        if not stack or stack[-1]!='[':
            answer=0
            break
        if arr[i-1]=='[':
            answer+=cnt
        cnt//=3
        stack.pop()

print(answer if not stack else 0)