import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

board = input()

answer=[]
for b in board.split('.'):
    n = len(b)
    if n==0:
        answer.append('')
        continue

    cnt4, n = divmod(n, 4)
    cnt2, n = divmod(n, 2)

    if n==0:
        answer.append('AAAA'*cnt4 + 'BB'*cnt2)
answer = '.'.join(answer)

if len(answer) == len(board):
    print(answer)
else:
    print(-1)