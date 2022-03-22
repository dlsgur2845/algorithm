"""
유형 : 구현

* binary_search 함수는 bisect의 bisect_right 함수 와 동작이 동일
  - (timetable의 최대 크기가 2000이라 굳이 안쓰고 순차적으로 index를 찾아도 무방)
  
1. 가장 핵심은 timetable이 아닌 다음 버스가 존재하는지에 대한 여부이다. 따라서 버스가 존재할때 까지만 loop 순회.
2. 현재 버스 시간에 탑승할 수 있는 인원을 모두 timetable에서 제거한다.
3. 현재 버스가 마지막 시간이라면 대기 인원보다 버스 자리가 많은지 확인.
  - 대기 인원을 알기 위해선 정렬된 timetable에서 인덱스를 구하면 됨.
  3-1. 버스 자리가 더 많다면 현재 버스 시간을 반환.
  3-2. 대기 인원이 더 많거나 같다면 m 번째 인원의 -1분 반환.

"""

from collections import deque

def toSecond(t):
    t = list(map(int, t.split(':')))
    return t[0]*60+t[1]

def toTime(n):
    return ':'.join([t.zfill(2) for t in list(map(str, divmod(n, 60)))])

def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l<=r:
        m = (l+r)//2
        
        if arr[m] <= x:
            l=m+1
        else:
            r=m-1
    return l

def solution(n, t, m, timetable):
    answer = ''
    bus = deque([9*60+t*i for i in range(n)])
    timetable = deque(sorted(list(map(toSecond, [t for t in timetable if t!='23:59']))))

    while bus:
        b = bus.popleft()
        pp=binary_search(timetable, b)
        
        cnt=min(pp, m)
        while timetable and cnt>0:
            lastP = timetable.popleft()
            cnt-=1
            
        if not bus:
            if m > pp:
                return toTime(b)
            return toTime(lastP-1)
