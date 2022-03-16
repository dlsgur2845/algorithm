"""
유형 : 그래프 ( 다익스트라 )

그래프의 모든 가중치가 1이므로 1번 노드에서 가장 먼 거리에 있는 노드는 가장 cost가 높은 노드이다.
따라서 그래프의 대표적인 알고리즘인 다익스트라를 떠올릴 수만 있다면 문제는 이미 해결했다고 봐도 되는 문제이다.

Dijkstra 동작 설명
1. heap을 사용해도 되고 priority queue를 사용해도 무방하지만 선택할 수 있는 간선 중 가장 경로상 가중치의 합이 낮은 간선을 선택할 수 있어야한다.
  - heap을 사용하면 시간 복잡도 O(N * log2(V))
2. 1번노드 자신은 가중치가 0으로 queue의 처음에 삽입
3. 현재 노드에서 방문 할 수 있는 노드중 경로상의 cost 합이 가장 낮은 간선을 queue에 삽입
  3-1. 이 과정에서 costs 배열에 저장된 cost보다 삽입된 값이 적다면 costs 업데이트
4. queue가 빌 때까지 3번 반복

"""

from heapq import heappush, heappop

def solution(n, edge):
    graph = [list() for _ in range(n)]
                
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    def dijkstra(begin):
        q = [(0, begin)]
        costs = [float('inf')]*n
        costs[begin]=0
        
        while(q):
            pCost, pNode = heappop(q)
            if pCost > costs[pNode]:
                continue
            for cNode in graph[pNode]:
                cCost = pCost + 1
                if cCost < costs[cNode]:
                    costs[cNode] = cCost
                    heappush(q, (cCost, cNode))
        return costs
    
    costs = dijkstra(0)
    return costs.count(max(costs))
