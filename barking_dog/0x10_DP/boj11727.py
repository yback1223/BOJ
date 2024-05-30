# https://www.acmicpc.net/problem/11727
# 11727번 - 2xn 타일링2

from typing import List

n = int(input())
dp: List[int] = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = (dp[i - 1] * 2 + 1) % 10007
    else:
        dp[i] = (dp[i - 1] * 2 - 1) % 10007
print(dp[n])
