"""
유형 : 그래프

최소 스패닝 트리를 생성하기 위해서 kruskal 또는 prime 알고리즘 수행

[kruskal]
1. 주어진 모든 간선들에 대해 union-find 를 통해 두 노드를 연결 했을 때 사이클이 발생하는지 확인.
2. 발생하지 않는다면 union을 통해 합친다 (= 같은 노드를 부모로 가짐)

모든 간선을 확인하고나면 생성되는 트리가 최소 스패닝 트리.
"""

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    def find(a):
        nonlocal parent
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    
    def union(a, b):
        nonlocal parent
        a = find(a)
        b = find(b)
        
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
            
    for a, b, c in sorted(costs, key=lambda x:x[2]):
        if find(a) != find(b):
            union(a, b)
            answer+=c
    return answer
