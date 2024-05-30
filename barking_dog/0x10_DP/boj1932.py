# https://www.acmicpc.net/problem/1932
# 1932번 - 정수 삼각형

from typing import List

n = int(input())
triangle: List[List[int]] = [[int(i) for i in input().split()] for _ in range(n)]

idx = 0
for i in range(1, n):
    for j in range(len(triangle[i])):
        tmp: List[int] = []
        if j - 1 >= 0:
            tmp.append(triangle[i - 1][j - 1] + triangle[i][j])
        if j < len(triangle[i - 1]):
            tmp.append(triangle[i - 1][j] + triangle[i][j])
        triangle[i][j] = max(tmp)
print(max(triangle[n - 1]))