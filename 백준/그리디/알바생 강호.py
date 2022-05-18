import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

answer=0
for i in range(N):
    answer += max(0, arr[i]-(i+1)+1)
print(answer)