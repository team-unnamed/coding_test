"""

1. input 보다 sys.stdin.readline이 더 빠르다.
2. j*j 대신 j**2 쓰면 시간초과남
3. min 보다 if 문이 더 빠르다

"""

import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))

dp = [i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if dp[i] > dp[i - j * j] + 1:
            # 제곱수를 포함시켜 제곱항을 최대한 줄여준다.
            dp[i] = dp[i - j * j] + 1


print(dp[N])
