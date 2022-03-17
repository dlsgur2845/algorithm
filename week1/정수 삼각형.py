"""
유형 : dp

각 행의 이웃한 값중 큰 값을 선택하여 위의 값에 더해주다보면 root에 남은 값이 가장 큰 값이 된다.
"""

def solution(triangle):
    for r in range(len(triangle)-2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])
    return triangle[0][0]
