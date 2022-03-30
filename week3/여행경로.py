"""
유형 : 완탐(DFS)

1. 탐색할 때 빠른 인덱싱을 위해 출발지로부터 갈 수 있는 도착지들을 모두 dictionary에 넣어둠
2. visit 도 똑같은 구조로 생성
3. DFS 탐색. 이미 갈 수 있는 여행지를 dict에서 정렬했기 때문에 가장 처음 나온 NULL이 아닌 return 값이 정답.
"""

from collections import defaultdict

def solution(tickets):
    answer = []
    d = defaultdict(list)
    visit = defaultdict(list)
    for dep, arr in tickets:
        visit[dep].append(False)
        d[dep].append(arr)
        d[dep].sort()

    def dfs(trace):
        if len(trace) >= len(tickets)+1:
            return trace
        
        dep = trace[-1]
        for i, arr in enumerate(d[dep]):
            if not visit[dep][i]:
                visit[dep][i] = True
                ret = dfs(trace+[arr])
                visit[dep][i] = False
                
                if ret:
                    return ret

    return dfs(['ICN'])
