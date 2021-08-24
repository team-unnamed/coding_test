import sys
input = sys.stdin.readline

n = int(input())

weights = [0] + list(map(int, input().rstrip('\n').split()))

edges = [[] for _ in range(n+1)]

while True:
    try:
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    except:
        break

dp = [[0]*2 for _ in range(n+1)]
nums = [[[],[]] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

def dfs(node):
    visit[node]=1
    dp[node][0] += weights[node]
    nums[node][0].append(node)

    for i in edges[node]:
        if visit[i]==0:
            dfs(i)
            dp[node][0] += dp[i][1]
            for j in nums[i][1]:
                nums[node][0].append(j)

            if dp[i][1]>=dp[i][0]:
                dp[node][1] += dp[i][1]
                for j in nums[i][1]:
                    nums[node][1].append(j)
            else:
                dp[node][1] += dp[i][0]
                for j in nums[i][0]:
                    nums[node][1].append(j)

dfs(1)

if dp[1][0]>= dp[1][1]:
    print(dp[1][0])
    nums[1][0].sort()
    for i in nums[1][0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    nums[1][1].sort()
    for i in nums[1][1]:
        print(i, end=' ')
