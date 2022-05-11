import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
graph = [[float('inf')]*52 for _ in range(52)]

for i in range(52):
    graph[i][i]=0

toIdx = lambda x:ord(x)-ord('A') if x.isupper() else ord(x)-ord('a')+26
for _ in range(N):
    a, b = map(toIdx, input().split(' => '))
    graph[a][b]=1

for k in range(52):
    for i in range(52):
        for j in range(52):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

toAlpha = lambda x:chr(x+ord('A')) if x < 26 else chr(x+ord('a')-26)
answer=[]
for i in range(52):
    for j in range(52):
        if i==j: continue
        if graph[i][j] != float('inf'):
            answer.append((toAlpha(i), toAlpha(j)))

answer = sorted(answer)
print(len(answer))
for a, b in answer:
    print(f'{a} => {b}')