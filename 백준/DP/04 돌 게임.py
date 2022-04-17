import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
if N%2==1:
    print('SK')
else:
    print('CY')