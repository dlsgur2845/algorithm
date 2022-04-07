"""
유형 : DFS

1. 후위순회 방법으로 트리를 탐색. 방문한 노드 재탐색 방지를 위해 visit 사용
2. 현재 탐색 중인 노드의 값을 부모 노드로 전달하며 root 노드까지 전달. 이때, 각 노드의 절대 값을 answer에 추가.
3. root 노드에서 모든 child와 자기 자신의 합이 0이 된다면 가능한 경우이기 때문에 return answer, 0이 아니라면 return -1
"""

import sys
sys.setrecursionlimit(300000)

from collections import defaultdict

def solution(a, edges):
    answer = 0
    tree = defaultdict(list)
    visit = [False] * len(a)
    
    for _a, _b in edges:
        tree[_a].append(_b)
        tree[_b].append(_a)
    
    def dfs(cur):
        nonlocal visit, answer
        
        for next in tree[cur]:
            if not visit[next]:
                visit[next]=True
                a[cur] += dfs(next)
        
        answer += abs(a[cur])
        return a[cur]
    
    visit[0]=True
    if dfs(0)==0:
        return answer
    else:
        return -1
