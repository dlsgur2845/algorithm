import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [1] + ([0] * money)

    for c in coins:
        for i in range(c, money + 1):
            dp[i] += dp[i-c]
    print(dp[money])