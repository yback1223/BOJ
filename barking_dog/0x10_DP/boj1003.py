# https://www.acmicpc.net/problem/1003
# 1003번 - 피보나치 함수

from typing import List

T = int(input())
nums: List[int] = [int(input()) for _ in range(T)]
max_num = max(nums)
dp: List[List[int]] = [[0, 0] for _ in range(max_num + 1)]
dp[0] = [1, 0]
if max_num >= 1:
    dp[1] = [0, 1]

for i in range(2, max_num + 1):
    dp[i] = [dp[i - 1][1], dp[i - 2][1] + dp[i - 1][1]]

for num in nums:
    print(f'{dp[num][0]} {dp[num][1]}')