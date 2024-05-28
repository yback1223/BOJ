# https://www.acmicpc.net/problem/2579
# 2579번 - 계단 오르기

from typing import List

MAX = 10000
total_stairs = int(input())
stairs: List[int] = [0] * MAX
for i in range(total_stairs):
    stairs[i] = int(input())

dp: List[int] = [0] * (MAX + 1)
dp[0] = 0
dp[1] = stairs[0]
dp[2] = stairs[0] + stairs[1]
dp[3] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(4, total_stairs + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i - 2], dp[i - 2] + stairs[i - 1])

print(dp[total_stairs])