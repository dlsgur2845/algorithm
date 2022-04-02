"""
유형 : BFS

*보드를 출력해보려면 모든 주석 제거
*** 1번, 2번이 중요 포인트

1. 모든 좌표계에 2를 곱해줌
  - 2를 곱해야 2차원 보드에서 두 좌표가 선으로 연결되어 있는지 아닌지를 쉽게 구별할 수 있다.
2. 2중 for-loop을 2번 사용하여 모든 사각형의 테두리만 1로 남겨둠.
3. 테두리를 1로 남겨둘 수 있다면 그 다음은 간단한 BFS로 탐색. 좌표를 2로 곱한 후 거리를 탐색했으니 탐색 결과에 2를 나누어준다.
"""

# def test(board):
#     for b in board:
#         for _b in b:
#             if _b==0:
#                 print('.', end=' ')
#             else:
#                 print(_b, end=' ')
#         print()
#     print()
    
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    rectangle = [list(map(lambda x:x*2, rect)) for rect in rectangle]
    characterX, characterY, itemX, itemY = list(map(lambda x:x*2, [characterX, characterY, itemX, itemY]))
    n = max(map(max, rectangle))

    board = [[0]*(n+2) for _ in range(n+2)]
    visit = [[False]*(n+2) for _ in range(n+2)]
    my, mx = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for x0, y0, x1, y1 in rectangle:
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                board[x][y]=1
                
    for x0, y0, x1, y1 in rectangle:
        for x in range(x0+1, x1):
            for y in range(y0+1, y1):
                board[x][y]=0
            
#     test(board)
    
    def bfs(x, y):
        nonlocal visit
        q = deque([(x, y)])
        visit[x][y] = True
        depth=0
        
        while q:
            size = len(q)
            
            for _ in range(size):
                x, y = q.popleft()
                
                if x == itemX and y == itemY:
                    return depth//2
                
                for d in range(4):
                    _x = x + mx[d]
                    _y = y + my[d]
                    
                    if board[_x][_y] <= 0:
                        continue
                    if not visit[_x][_y]:
                        visit[_x][_y] = True
                        q.append((_x, _y))
            depth+=1
    
    return bfs(characterX, characterY)
