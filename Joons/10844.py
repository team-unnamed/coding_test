import sys

n = int(sys.stdin.readline().split()[0])
mod = 1000000000

d = [[0]*10 for i in range(n)]

for i in range(1,10):
    d[0][i] = 1


for i in range(1,n):
    for j in range(10):
        if j-1 >= 0:
            d[i][j] += d[i-1][j-1]
        if j+1 <= 9:
            d[i][j] += d[i-1][j+1]

ans = 0
for i in range(10):
    ans += d[n-1][i]
print(ans%mod)