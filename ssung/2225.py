"""

dp[K][N]: K개의 정수를 더해 그 합이 N이 되는 경우의 수

0 ~ K까지의 정수가 있을 때 0 ~ (K-1)까지의 합과 K 두 개의 정수로 생각해서 문제를 풀 수 있음.
0 ~ (K-1)까지의 합을 A라고 하면 N = A+K이므로 dp[K][N] = dp[K-1][N-i] (0 <= i <= N)

"""
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip("\n").split(" "))
mod = 1_000_000_000

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for i in range(N + 1):  # 정수 1개로 i를 만드는 방법은 1가지 밖에 없다.
    dp[1][i] = 1

for i in range(1, K + 1):
    for j in range(N + 1):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][j - k]
            dp[i][j] %= mod

print(dp[K][N])
