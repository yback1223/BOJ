# https://www.acmicpc.net/problem/11726
# 11726번 - 2xn 타일링

from typing import List

n = int(input())
dp: List[int] = []
dp.append(0)
dp.append(1)
dp.append(2)
for i in range(3, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 10007)
print(dp[n])2