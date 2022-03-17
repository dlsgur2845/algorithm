"""
유형 : 힙, 큐, 정렬

평균 턴어라운드 타임이 가장 짧은 job scheduling 방법은 SJF이다.

1. jobs을 작업 생성 시간을 기준으로 오름차순 정렬
2. time(현재 시간)을 0초로 초기화
3. jobs에 time과 같거나 작은 작업 생성 시간이 있으면 waitq에 모두 삽입
4. waitq에 작업이 존재하는지 확인
  4-1. 존재한다면 시간 업데이트 및 경과시간 기록
  4-2. 없다면 시간 +1초
5. 남은 작업 또는 대기중인 작업이 있다면 다시 3으로 이동
"""

from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs = deque(sorted(jobs))
    waitq = []
    
    time=0
    while jobs or waitq:
        while jobs and jobs[0][0] <= time:
            created, runtime  = jobs.popleft()
            heappush(waitq, (runtime, created))
        
        if waitq:
            runtime, created = heappop(waitq)
            time += runtime
            answer+=time-created
        else: time+=1
    return answer//n
