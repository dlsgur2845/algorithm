import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visit=[False]*N
answer=[]
def dfs(cur):
    global answer
    answer.append(cur+1)
    for next in graph[cur]:
        if not visit[next]:
            visit[next]=True
            dfs(next)
visit[V-1]=True
dfs(V-1)
print(' '.join(map(str,answer)))

def bfs(cur):
    from collections import deque
    visit = [False] * N
    visit[cur]=True
    q = deque([cur])
    answer=[]

    while q:
        cur = q.popleft()
        answer.append(cur+1)

        for next in graph[cur]:
            if not visit[next]:
                visit[next]=True
                q.append(next)
    return answer
print(' '.join(map(str, bfs(V-1))))