n = int(input())

dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    costs = input().split()
    if i>0:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + int(costs[0])
        dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + int(costs[1])
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + int(costs[2])
    else:
        dp[i] = list(map(int, costs))

print(min(dp[n-1]))