import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
mod = 1000000000

dp = [[0 for _ in range(11)] for _ in range(N + 1)]  # dp[i][j] : 길이 i, 일의 자리 숫자가 j인 숫자
for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:  # 일의 자리가 0이면 앞 숫자(십의 자리)는 무조건 1이어야 한다.
            dp[i][j] = dp[i - 1][1] % mod
        elif j == 9:  # 일의 자리가 9이면 앞 숫자(십의 자리)는 무조건 8이어야 한다.
            dp[i][j] = dp[i - 1][8] % mod
        else:  # 일의 자리가 j이면 앞 숫자(십의 자리)는 (j-1) or (j+1).
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod

answer = 0
for i in range(1, 10):
    # answer += dp[N][i]%mod 로 작성하면 원하는 결과가 나오지 않음.
    answer = (answer + dp[N][i]) % mod

print(answer)
