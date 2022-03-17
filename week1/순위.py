"""
유형 : 그래프

1. A가 B를 이겼다는 정보가 주어진다. 이 정보에 따라서 그래프를 생성.
  - 주의할 점은 undirected edge로 연결해야하는 것이다.
2. floyd warshall 알고리즘을 수행 하면 어떤 선수가 다른 어떤 선수를 이겼는지에 대한 모든 정보가 업데이트 된다.
  - 시간 복잡도는 O(100**3)
3. 이 때 graph[a][b]를 행 기준에서 보면 이긴 경기, 열 기준에서 보면 진 경기 이다. 따라서 이긴 경기와 진 경기의 합이 n-1이라면 해당 선수의 순위를 매길 수 있다.
"""

def solution(n, results):
    answer = 0
    
    graph = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        graph[i][i]=0
    for a, b in results:
        graph[a-1][b-1]=1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = 1
        
    for i in range(n):
        if graph[i].count(1) + [list(g) for g in zip(*graph)][i].count(1) == n-1:
            answer+=1
    
    return answer
