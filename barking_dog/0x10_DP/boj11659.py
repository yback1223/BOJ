# https://www.acmicpc.net/problem/11659
# 11659번 - 구간 합 구하기4

from typing import List

N, M = map(int, input().split())
nums: List[int] = [int(i) for i in input().split()]
sums: List[int] = [nums[0]]

for i in range(1, len(nums)):
    sums.append(sums[i - 1] + nums[i])

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sums[j - 1])
    else:
        print(sums[j - 1] - sums[i - 2])
