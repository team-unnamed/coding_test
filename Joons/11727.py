import sys

n = int(sys.stdin.readline().split()[0])
dp = [1,3]
dp += [0]*(n-2)
if n > 2:
    for i in range(2,n):
        dp[i] = 2*dp[i-2] + dp[i-1]    

print(dp[n-1]%10007)