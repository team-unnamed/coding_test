n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(n):
    cur = int(input())
    if i>1:
        dp[i+1] = max(max(dp[:i]), max(dp[:i-1])+prev)+cur
    elif i==0:
        dp[i+1]=cur
    elif i==1:
        dp[i+1] = dp[i]+cur

    prev = cur

print(max(dp))