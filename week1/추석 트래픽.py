"""
유형 : 구현

1. TIME과 COLAPSED를 계산의 편이상 int로 변경후 각 작업의 시작, 끝 시간을 저장
2. lines은 끝나는 시간 기준으로 오름차순 정렬되어있다.
  2-1. 따라서 현재 끝나는 시간과 다음 작업들의 시작시간을 비교하면 0.001초 동안 동시에 진행 중인 작업 수를 알 수 있음.
3. 그렇다면 현재 끝나는 시간에 999ms 를 더한 후 비교하면 1초 동안의 최대 작업 수를 구할 수 있음.
"""

def solution(lines):
    answer = 0
    
    for i, line in enumerate(lines):
        DATE, TIME, COLAPSED = line.split(' ')
        h, m, s = list(map(lambda x:int(float(x)*1000), TIME.split(':')))
        end_t = h*3600 + m*60 + s
        beg_t = end_t - int(float(COLAPSED[:-1])*1000) + 1
        
        lines[i] = (beg_t, end_t)
        
    for i in range(len(lines)):
        end_t = lines[i][1]
        cnt=0
        for j in range(i, len(lines)):
            beg_t = lines[j][0]
            if end_t+999 >= beg_t:
                cnt+=1
        answer = max(answer, cnt)
        
    return answer
