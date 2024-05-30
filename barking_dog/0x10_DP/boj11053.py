# https://www.acmicpc.net/problem/11053
# 11053번 - 가장 긴 증가하는 부분 수열

from typing import List

N = int(input())
nums: List[int] = [int(i) for i in input().split()]
dp:List[int] = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + 1, dp[i])
# print(dp)
print(max(dp))