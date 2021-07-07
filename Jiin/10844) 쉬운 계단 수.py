import sys

N = int(sys.stdin.readline())

memo = [[0]*10 for i in range(101)]
memo[1] = [0,1,1,1,1,1,1,1,1,1]


for i in range(2,N+1):
    for j in range(1,9):
        memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]
    memo[i][0] = memo[i-1][1]
    memo[i][9] = memo[i-1][8]

ans = 0
for n in memo[N]:
    ans += n
print(ans%1000000000)