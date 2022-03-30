"""
유형 : 이진탐색

***난의도가 나에겐 너무 높은듯했다.
   접근은 입국심사랑 비슷한거같았는데 금, 은으로 두개가 존재하며
   금과 은을 동시에 나르는 방법을 떠올릴 수 없어 정답 코드 참조...

1. 우선 탐색 범위는 최소 시간:min(t) 부터 최악의 시간:(a+b)*max(t)*2 (곱하기 2는 왕복의 경우)로 설정
2. 이진 탐색 중 각 도시를 순회하며 m 시간 걸린다 가정했을때 옮길 수 있는 금과 은, 둘의 합을 각각 더해준다.
3. 모든 도시의 금, 은, 둘의 합이 필요로하는 금, 은, 둘의 합보다 크거나 같으면 탐색 범위를 줄여 최소 시간을 계산한다.

참조 코드랑 시간 비교하다 발견한점 : min 내장 함수의 구조가 tmp에 0번 째 파라미터 값을 할당 후 비교하는 것 같다.
                                    따라서 2개만 비교할때는 if-else 문이 최악 속도가 빠른듯하다.
"""

def solution(a, b, g, s, w, t):
    _min = lambda a,b:a if a<b else b
    
    l, r = min(t), (a+b) * 2 * max(t)
    while l <= r:
        m = (l+r)//2
        gold = 0
        silver = 0
        both = 0
        
        for _g, _s, _w, _t in zip(g,s,w,t):
            move, remain = divmod(m, (_t+_t))
            if remain >= _t:
                move+=1
            
            gold += _min(_w*move, _g)
            silver += _min(_w*move, _s)
            both += _min(_w*move, _g+_s)
            
        if gold >= a and silver >= b and both >= a+b:
            r = m-1
        else:
            l = m+1
    return l
