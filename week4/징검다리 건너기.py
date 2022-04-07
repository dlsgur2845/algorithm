"""
유형 : 이진탐색

1. 건널 수 있는 사람 수를 m으로 두고 이진탐색 수행.
2. m 이하의 값을 가진 돌이 K를개이상 연속으로 있다면 사람 수를 줄여 재탐색, 반대의 경우 사람 수를 늘려 재탐색.
"""

def solution(stones, k):
    l, r = 0, max(stones)
    while l<=r:
        m = (l+r)//2

        cnt=0
        for s in stones:
            if s-m<=0:
                cnt+=1
            else:
                cnt=0
            if cnt >= k:
                break

        if cnt >= k:
            r=m-1
        else:
            l=m+1
    return l
