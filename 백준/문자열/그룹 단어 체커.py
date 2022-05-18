import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

answer=0
for _ in range(N):
    s = list(input())
    visit=[]
    for prev, cur in zip(s, s[1:]):
        if cur in visit:
            break
        if prev!=cur:
            visit.append(prev)
    else:
        answer+=1

print(answer)