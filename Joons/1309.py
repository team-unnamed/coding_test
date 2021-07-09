# 동물원
# 1. 점화식 방법으로 접근 d[n] = d[n-1]*2 + d[n-2]
import sys
input_ = sys.stdin.readline
n = int(input_())

def solution_A(n):
    dp = [0]*(n + 1)
    for i in range(n+1):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 3
        else:
            dp[i] = dp[i-1]*2 + dp[i-2] % 9901
    print(dp[-1] % 9901)

def solution_B(n):
    m = 9901
    dp = [[0]*3 for _ in range(n+1)] # (N+1) * [L,R,None]
    dp[0][2] = 1
    for i in range(1,n+1):
        l,r,none = dp[i-1]
        dp[i][0] = (r + none)%m
        dp[i][1] = (l + none)%m
        dp[i][2] = (l + r + none)%m
    print(sum(dp[-1])%m)
solution_A(n)
solution_B(n)