# https://www.acmicpc.net/problem/1912
# 1912번 - 연속합

from typing import List

n = int(input().strip())
nums: List[int] = [int(i) for i in input().split()]
dp: List[int] = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))