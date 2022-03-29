"""
유형 : DP

n+1행 m+1열 배열을 만들어 현재 위치가 물 웅덩이거나 이전 위치가 물 웅덩이일 경우를 제외하고 아래와 같이 계산

puddles이 (열, 행)로 이루어져 있다는 것만 주의
"""

def solution(m, n, puddles):
    answer = 0
    board = [[0]*(m+1) for _ in range(n+1)]
    board[1][1]=1
    
    for c, r in puddles:
        board[r][c] = -1
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r==c==1 or board[r][c] == -1: continue
            
            up = 0 if 0 > board[r-1][c] else board[r-1][c]
            left = 0 if 0 > board[r][c-1] else board[r][c-1]
            board[r][c] = (up + left) % 1000000007
        
    return board[n][m]
