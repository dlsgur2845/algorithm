import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

for cnt5 in range(n//5, -1, -1):
    five = cnt5*5
    cnt2, left = divmod(n-five, 2)
    if left==0:
        print(cnt5+cnt2)
        break
else:
    print(-1)