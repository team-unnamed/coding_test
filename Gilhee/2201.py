import sys
k = int(input())

dp = [[0 for _ in range(101)], [0 for _ in range(101)]]

dp[0][1]=1
dp[0][2]=1
dp[1][1]=1
dp[1][2]=2

if k==1:
    print(1)
    sys.exit()
elif k==2:
    print(10)
    sys.exit()


for i in range(3, 101):
    dp[0][i] = dp[0][i-1] + dp[0][i-2]
    dp[1][i] = dp[1][i-1] + dp[0][i]
    if dp[1][i]>=k:
        break


print(10, end='')
k -= dp[1][i-1]
i -=2

while i>0:
    if k>dp[0][i+1]:
        if i==1:
            print(1)
        else:
            print(10, end='')
        k -= dp[0][i+1]
        i -=2
    else:
        print(0, end='')
        i -=1

