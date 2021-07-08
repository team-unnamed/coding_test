"""

dp[i][0] = i번째 우리에 사자를 배치하지 않음
dp[i][1] = i번째 우리에서 사자를 왼쪽에 배치
dp[i][2] = i번쨰 우리에서 사자를 오른쪽에 배치

점화식을 구할 수도 있다.
dp[i] = 2*dp[i-1]+dp[i-2]

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
mod = 9901

dp = [[0 for _ in range(3)] for _ in range(N + 1)]
dp[1][0] = dp[1][1] = dp[1][2] = 1
for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % mod

print((dp[N][0] + dp[N][1] + dp[N][2]) % mod)
