T = int(input())

for _ in range(T):
    n = int(input())

    stickers = []
    stickers.append(list(map(int,input().split())))
    stickers.append(list(map(int,input().split())))

    dp = [[0,0,0] for _ in range(n)]

    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + stickers[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[1][i]
        dp[i][2] = max(dp[i-1])

    print(max(dp[n-1]))