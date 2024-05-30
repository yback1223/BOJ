# https://www.acmicpc.net/problem/11055
# 11055번 - 가장 큰 증가하는 부분 수열

from typing import List

N = int(input())
nums: List[int] = [int(i) for i in input().split()]
dp: List[int] = nums.copy()

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))