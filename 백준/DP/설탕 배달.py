import sys
sys.stdin = open("../input.txt", 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
R=N//5+1
C=N//3+1

answer=R*C

arr = [[3*c for c in range(C+1)] for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(C+1):
        arr[r][c] = arr[r-1][c] + 5

for r in range(R+1):
    for c in range(C+1):
        if arr[r][c]==N and answer > r+c:
            answer=r+c
print(answer if answer!=R*C else -1)