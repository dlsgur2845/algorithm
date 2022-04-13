import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
mr = [0, -1, -1, -1, 0, 1, 1, 1]
mc = [-1, -1, 0, 1, 1, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    d-=1

    # Move & Rain
    for i, (r, c) in enumerate(clouds):
        r = (r + mr[d] * s) % N
        c = (c + mc[d] * s) % N

        board[r][c]+=1
        clouds[i] = (r, c)

    # Copy
    for r, c in clouds:
        water_cnt = 0
        for _d in [1, 3, 5, 7]:
            _r = r + mr[_d]
            _c = c + mc[_d]

            if _r < 0 or _c < 0 or _r >= N or _c >= N:
                continue
            if board[_r][_c] > 0:
                water_cnt += 1

        board[r][c] += water_cnt

    new_clouds=[]
    for r in range(N):
        for c in range(N):
            if (r, c) not in clouds and board[r][c]>=2:
                board[r][c]-=2
                new_clouds.append((r, c))
    clouds = new_clouds

answer=0
for r in range(N):
    for c in range(N):
        answer += board[r][c]
print(answer)