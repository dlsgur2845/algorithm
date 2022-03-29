"""
유형 : BFS

1. 단어 차이가 1개인 경우만 True를 반환하는 compare 함수 작성
   (항상 같은 길이로 주어진다는 조건을 못봐서 단어 길이차도 고려되어있음)
2. bfs를 사용해 target 단어가 나왔을 때 바로 현재 depth를 반환
3. 모든 경로 탐색 후 target이 없었으면 0을 반환
"""

from collections import deque

def compare(A, B):
    cnt = abs(len(A)-len(B))
    length = len(A) if len(A) < len(B) else len(B)
    
    for i in range(length):
        if A[i] != B[i]:
            cnt+=1
        if cnt > 1:
            return False
    return True

def solution(begin, target, words):
    visit = [False]*len(words)
    
    q = deque([begin])
    depth=0
    
    while q:
        size = len(q)
        
        for _ in range(size):
            word = q.popleft()
            
            if word == target:
                return depth
            
            for i in range(len(words)):
                if not visit[i] and compare(word, words[i]):
                    visit[i] = True
                    q.append(words[i])
        depth+=1
    return 0
