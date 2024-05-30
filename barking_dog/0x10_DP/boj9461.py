# https://www.acmicpc.net/problem/9461
# 9461번 - 파도반 수열

from typing import List

T = int(input())
dp: List[int] = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, len(dp)):
    dp[i] = dp[i - 5] + dp[i - 1]

for i in range(T):
    print(dp[int(input())])