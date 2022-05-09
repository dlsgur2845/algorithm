import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x = list(map(int, input().split()))

sum_x = x[:]
answer=0
for i in range(1, n):
    sum_x[i] += sum_x[i-1]
for i in range(n):
    answer += x[i] * (sum_x[n-1]-sum_x[i])
print(answer)

# answer=0
# sum_x=0
# for _x in x:
#     answer += _x * sum_x
#     sum_x += _x
# print(answer)