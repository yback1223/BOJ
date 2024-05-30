# https://www.acmicpc.net/problem/14501
# 14501번 - 퇴사

N = int(input())
costs: list[list[int]] = [list(map(int, input().split())) for _ in range(N)]
dp: list[int] = [0] * (N + 1)

for i in range(N):
    if costs[i][0] + i <= N:
        dp[i + costs[i][0]] = max(dp[i + costs[i][0]], dp[i] + costs[i][1])
    dp[i + 1] = max(dp[i + 1], dp[i])
# print(dp)
print(max(dp))