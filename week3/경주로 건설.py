"""
유형 : DFS, 메모

1. 최저 비용을 업데이트하는 2차원 배열 생성.
2. dfs 탐색하는데 이전 방향과 현재 가려는 방향이 같을때만 +100 그 외는 +100+500
3. 벽이거나, 보드를 넘으면 탐색하지 않음
4. 현재 코스트가 저장된 코스트보다 작거나 같을때만 탐색
  - 작은 경우만 했다가 테스트 케이스 3번을 통과하지 못했음 - memo[1][1]에서 위에서오나 밑에서 오나 cost는 700이지만,
  다음으로 이동시 코너를 만드냐 안만드냐가 나뉘기 때문.
"""

def solution(board):
    N = len(board)
    memo = [[float("inf")]*N for _ in range(N)]
    mr, mc = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    def dfs(r, c, prev_d, cost):
        nonlocal memo
        if r==c==N-1:
            return
        
        for d in range(4):
            _r = r+mr[d]
            _c = c+mc[d]
            
            if _r < 0 or _c < 0 or _r >= N or _c >= N or board[_r][_c]==1:
                continue
                
            _cost = cost+100 if prev_d==d or cost==0 else cost+600
            if _cost <= memo[_r][_c]:
                memo[_r][_c] = _cost
                dfs(_r, _c, d, _cost)

    dfs(0, 0, -1, 0)
    return memo[N-1][N-1]
