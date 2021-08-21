a = input()
b = input()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1]==b[i-1]:
            dp[i][j]= dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

x= len(a)
y= len(b)
key = dp[-1][-1]
answer = ''

while key!=0:
    if dp[y-1][x]==key-1 and dp[y][x-1]==key-1:
        answer = a[x-1] + answer
        x -=1
        y -=1
        key -=1
    else:
        if dp[y-1][x]> dp[y][x-1]:
            y -=1
        else:
            x -=1

print(dp[-1][-1])
print(answer)

