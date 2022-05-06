import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

eq = input()
stack=[]
answer=''
pri = {'*':2, '/':2, '+':1, '-':1}
for a in eq:
    if a.isalpha():
        answer+=a
    else:
        if a=='(':
            stack.append(a)
        elif a==')':
            while stack:
                op = stack.pop()
                if op == '(':
                    break
                answer+=op
        else:
            while stack and stack[-1]!='(' and pri[stack[-1]] >= pri[a]:
                answer+=stack.pop()
            stack.append(a)
while stack:
    answer+=stack.pop()

print(answer)