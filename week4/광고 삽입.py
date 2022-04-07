"""
유형 : DP

1. 모든 시간을 정수형으로 바꾼다.
2. DP로 접근해야하는데 play_time 크기의 배열을 만든 후 각 시청 시간의 시작 인덱스를 +1 끝 인덱스를 -1 해준다.
  - 끝 인덱스는 포함되지 않기 때문에 해당 인덱스의 다음이 아닌 해당 인덱스에 -1을 해줌.
3. 가중합을 구하여 시청 구간을 구한다.
4. 가중합을 한번 더 하여 누적 시청자 수를 구한다.
5. 시점 A 부터 B 까지의 시청자 수는 dp[B-1]-dp[A-1]로 구할 수 있다.
  - A-1 : A도 포함되기 때문에 A가 아닌 A-1
  - B-1 : B는 포함되지 않기 때문에 B가 아닌 B-1
6. 광고를 시작해서 끝마칠 수 있는 모든 시간 중 최대 효율 시작 시간을 구한다.
7. 구한 정수형 시간을 다시 시간형태로 변경
"""

def TimetoInt(time):
    time = list(map(int, time.split(':')))
    return time[0]*3600 + time[1]*60 + time[2]

def InttoTime(n):
    hour, minute = divmod(n, 3600)
    minute, second = divmod(minute, 60)
    return ':'.join([str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)])

def solution(play_time, adv_time, logs):
    play_time, adv_time = map(TimetoInt, [play_time, adv_time])
    dp = [0]*(play_time+1)

    for log in logs:
        A, B = map(TimetoInt, log.split('-'))
        dp[A]+=1
        dp[B]-=1
        
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    
    max_watch=dp[adv_time]
    answer=0
    for A in range(1, play_time-adv_time+1):
        B = min(A+adv_time, play_time)
    
        watch = dp[B-1]-dp[A-1]
        if max_watch < watch:
            max_watch = watch
            answer = A
        
    return InttoTime(answer)
