"""
유형 : 그래프, DP

1. 모든 최적 정로를 탐색하기 위해 floyd warshall 알고리즘 1회 수행.
2. k 지점까지 같이 탑승한 경우 k지점에서 각각 a, b 지점까지의 최소 비용을 answer에 저장

* floyd warshall
_min 함수를 재정의 했을 때 실행시간 : 2300 ms -> 1900 ms
기존 경로보다 비용이 작을 때만 update하는 조건문 추가시 : 1900 ms -> 1200 ms
  - 현재 n이 최대 200이지만 더 큰 n일 경우 조금이지만 더 유의미하다고 생각.
"""

def solution(n, s, a, b, fares):
    answer = float("inf")
    board = [[float("inf")]*n for _ in range(n)]
    _min = lambda a,b:a if a<b else b
    
    for i in range(n):
        board[i][i]=0
    for _a, _b, _c in fares:
        board[_a-1][_b-1] = _c
        board[_b-1][_a-1] = _c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                board[i][j] = min(board[i][j], board[i][k]+board[k][j])
    
    for k in range(n):
        answer = _min(answer, board[s-1][k]+board[k][a-1]+board[k][b-1])
    return answer
