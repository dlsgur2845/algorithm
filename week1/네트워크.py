"""
유형 : 그래프 (BFS/DFS, union-find)

A. DFS
  1. answer의 범위는 1 <= answer <= n 이다 따라서 n번의 시작점을 기준으로 dfs를 실행.
  2. 이웃한 노드를 방문하면 visit을 true로 변경.
  3. 1번, 2번을 반복하는데 False로 남아있는 시작점만 dfs를 시작하게 되므로 answer 역시 해당 경우만 +1
  
B. union-find
  1. union-find 알고리즘은 그래프에서 cycle이 발생하는지 여부를 찾을 때 사용되는 알고리즘.
  2. 따라서 알고리즘 수행 후 root 노드 종류의 갯수가 정답이 된다.
    - 주의할 점은 union을 수행하다보면 dangling이 발생하는데 find 함수를 n번(모든노드)에 대해 수행하면 해결.
"""

def solution_DFS(n, computers):
    answer = 0
    visit=[False]*n
    
    def dfs(cNode):
        visit[cNode] = True
        
        for nNode in range(n):
            if computers[cNode][nNode] and not visit[nNode]:
                dfs(nNode)
                
    for begin in range(n):
        if not visit[begin]:
            dfs(begin)
            answer+=1
    return answer




def solution_UNION_FIND(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    
    def find(a):
        if a != parents[a]:
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a < b:
            parents[b]=a
        else:
            parents[a]=b
            
    for r in range(n):
        for c in range(n):
            if computers[r][c]:
                union(r,c)
                
    for i in range(n):
        find(i)
    return len(set(parents))
