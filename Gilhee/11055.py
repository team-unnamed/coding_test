size = int(input())
numbers = list(map(int,input().split()))

dp = [0 for _ in range(size)]
dp[0]=numbers[0]

for i in range(1, size):
    for j in range(i):
        if numbers[j]<numbers[i] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=numbers[i]

print(max(dp))