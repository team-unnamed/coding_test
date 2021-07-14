n = int(input())
T = []
P = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if T[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + t[i]])
print(dp[0])