# 합분해
# 정수 N 이 주어질때, 0 부터 N 사이의 정수를 K 번 사용해서 N 을 만드는 경우의수를 구하기
# 중복가능, 둘의 순서가 바뀌어도 허용
# 1+1+1... 가능 , 1+2, 2+1 허용

import sys
input = sys.stdin.readline

N,K = map(int, input().split())

dp = [[0]*(N+1) for _ in range(K+1)]
m = 1_000_000_000

for i in range(N+1):
    dp[1][i] = 1
for k in range(1,K+1):
    for n in range(N+1):
        for i in range(n+1):
            dp[k][n] += dp[k-1][n-i]
            dp[k][n] %= m
print(dp)
print(dp[K][N])

