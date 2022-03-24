"""
유형 : DP

n=1 : 1개
 =2 : 2개
 =3 : 3개
 =4 : 5개
 
패턴을 보니 피보나치 수열이라 시도해봤는데 얻어 맞춘 느낌
"""

def solution(n):
    pibo = [1]*(n+1)
    for i in range(2, n+1):
        pibo[i] = (pibo[i-1] + pibo[i-2]) % 1000000007
    return pibo[n]
