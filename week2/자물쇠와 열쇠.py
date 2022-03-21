"""
유형 : 브루트포스

열쇠를 돌리면서 M+N+N-2 크기의 맵에서 가능한 시작점(M+N-1 이상의 좌표는 볼 필요x)으로부터 열쇠를 맞춰봄.
맞추는 방식은 lock 과 key를 더해 합이 2이면 충돌, 0이면 자물쇠가 매꿔지지 않은 경우.
"""


def rotL(arr):
    return [list(a) for a in zip(*[a[::-1] for a in arr])]

def solution(key, lock):
    N, M = len(key), len(lock)
    
    for _ in range(4):
        # 시작점 설정
        for r0 in range(M+N+N-2): # 4*58*58
            for c0 in range(M+N+N-2):
                if r0 >= M+N-1 or c0 >= M+N-1:
                    continue

                # 보드 초기화
                board = [[0]*(M+N+N-2) for _ in range(M+N+N-2)] # 4 * 58**4
                for r in range(M): # 4 * 58**4
                    for c in range(M):
                        board[r+N-1][c+N-1] = lock[r][c]

                # 열쇠 삽입
                for r in range(N): # 4 * 58**2 * 20**2
                    for c in range(N):
                        board[r0+r][c0+c] += key[r][c]
                
                # 확인
                flag=True
                for r in range(N-1, N-1+M):
                    for c in range(N-1, N-1+M):
                        if board[r][c] != 1:
                            flag=False
                            break
                    if not flag: break
                if not flag: continue

                return True
        key = rotL(key)
    return False
