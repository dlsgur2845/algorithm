import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
#
# answer=0
# i=0
# while i<N-1:
#     j=i+1
#     while j<N-1 and cities[i] < cities[j]: j+=1
#     for k in range(i, j):
#         answer += cities[i] * roads[k]
#     i=j
# print(answer)

answer=0
cost=10**10
for i in range(N-1):
    cost = min(cost, cities[i])
    answer += roads[i]*cost
print(answer)