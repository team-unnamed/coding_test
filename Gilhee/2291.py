n, m, k = map(int, input().split())

dp = [[[-1 for _ in range(m+1)] for _ in range(m+1) ] for _ in range(n+1)]

for i in range(1, m+1):
    dp[n][m][i]=1

def solve(length, num, minnum):
    if length>n or num>m:
        return 0
    
    if dp[length][num][minnum] != -1:
        return dp[length][num][minnum]

    dp[length][num][minnum]=0

    for i in range(minnum, m+1):
        if i+num>m:
            break

        dp[length][num][minnum] += solve(length+1, num+i, i)

    return dp[length][num][minnum]

def findanswer(length, num, minnum, nth):
    if length==n:
        return

    for i in range(minnum, m+1):
        if dp[length+1][num+i][i]==-1:
            continue

        if dp[length+1][num+i][i] < nth:
            nth -= dp[length+1][num+i][i]
            continue

        print(i, end=' ')
        findanswer(length+1, num+i, i, nth)
        break

solve(0,0,1)

findanswer(0,0,1,k)