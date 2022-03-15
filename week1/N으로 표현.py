"""
유형 : DP

1. 숫자끼리 이어 붙이는건 초기 숫자 N만 연결시 가능 따라서 처음에 빈 set에 추가
2. 1번만에 number가 찾아진다면 바로 return

3. ans 번 만에 찾아지는지를 탐색해야하는데 다음과 같은 규칙 존재
  - cases[2] = case[1] op case[1]
  - cases[3] = case[2] op case[1]
               case[1] op case[2]
  - ...
  - cases[8] = case[6] op case[2]
               case[7] op case[1]
               
  위와 같은 규칙을 메모라이징 기법으로 연산하면 시간내에 계산이 가능.
  
Line 28: for i in range(1, ans) 를 for i in range(1, ans//2+1) 로 변경 후 -, // 연산을 주의해주면 시간 단축가능하리라 예상.
"""


from itertools import product

def solution(N, number):
    cases={i:{int(str(N)*i)} for i in range(1, 9)}
    for k in cases.keys():
        if number in cases[k]:
            return k
    
    for ans in range(2, 9):
        for i in range(1, ans):
            A = cases[ans-i]
            B = cases[i]
            case = product(A, B)
            for a, b in case:
                for op in ['+', '-', '*', '//']:
                    try:
                        v = eval(f'{a}{op}{b}')
                        if v < 0: continue
                        if v == number:
                            return ans
                        cases[ans].add(v)
                    except:
                        pass
    return -1
