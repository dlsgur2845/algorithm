"""
유형 : queue + stack

1. 진열장의 모든 보석을 basket에 stack의 push 연산.
2. basket에 모든 종류가 있다면 basket의 첫 번째가 중복되는지 확인.
  2-1. 중복된다면 제거 후 다시 2수행.
3. 가능한 모든 모든 구간을 answer에 넣는데 이때, heap 구조를 사용하여 정렬(n logn) 할필요 없이 삽입(log n).
  - 사실 이 문제에서는 정렬이나 힙이 큰 차이가 없음.
4. answer 힙 트리의 0번째 인덱스가 가장 짧은 구간이며 가장 앞에 있는 구간이므로 return한다.
"""

from collections import deque, defaultdict
from heapq import heappush

def solution(gems):
    basket=deque()
    kinds={gem for gem in gems}
    nums=defaultdict(int)
    
    answer=[]
    l, r = 1, 0
    for gem in gems:
        basket.append(gem)
        nums[gem]+=1
        r+=1
        
        if len(nums) >= len(kinds):
            while basket and nums[basket[0]]>1:
                nums[basket.popleft()]-=1
                l+=1
            heappush(answer, (r-l, l, r))

    return answer[0][1:]
