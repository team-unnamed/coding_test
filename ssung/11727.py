import sys

input = sys.stdin.readline

n = int(input().rstrip("\n"))

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    # 1. f(n-1)에서 2x1 블록 추가 (1가지)
    # 2. f(n-2)에서 2x2 블록 추가 or 1x2블록 2개 추가 (2가지)
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

print(dp[n])