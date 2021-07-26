import sys

n = int(input())

Map = []

for _ in range(n):
    Map.append(list(map(int, input().split())))

def find(now, before):

    if dp[now][before]:
        return dp[now][before]

    if before == (1<<n) - 1:
        return Map[now][0] if Map[now][0] > 0 else sys.maxsize
 
    cost = sys.maxsize
    for i in range(1, n):
        if not (before>>i)%2 and Map[now][i]:
            tmp = find(i, before|(1<<i)) 
            cost = min(cost, tmp + Map[now][i])
 
    dp[now][before] = cost
    return cost

dp = [[0]*(1<<n) for _ in range(n)]
 
print(find(0, 1))