# https://www.acmicpc.net/problem/1149
# 1149번 - RGB거리

from typing import List

home_num = int(input())
homes: List[List[int]] = [[cost for cost in map(int, input().split())] for _ in range(home_num)]


for i in range(1, home_num):
    for color_idx in range(3):
        if color_idx == 0:
            homes[i][color_idx] += min(homes[i - 1][1], homes[i - 1][2])
        elif color_idx == 1:
            homes[i][color_idx] += min(homes[i - 1][0], homes[i - 1][2])
        else:
            homes[i][color_idx] += min(homes[i - 1][0], homes[i - 1][1])

print(min(homes[home_num - 1]))
