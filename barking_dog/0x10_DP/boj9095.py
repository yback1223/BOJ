# https://www.acmicpc.net/problem/9095
# 9095번 - 1, 2, 3 더하기

from typing import List

T = int(input())
inputs: List[int] = []

for i in range(T):
    inputs.append(int(input()))

max_num = max(inputs)

dp: List[int] = [0] * (max_num + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max_num + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for i in range(T):
    print(dp[inputs[i]])