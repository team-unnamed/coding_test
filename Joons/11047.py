import sys
input = sys.stdin.readline

n, target = map(int,input().split())
coins = sorted([int(input()) for _ in range(n)], reverse = True)

res = 0

for coin in coins:
    cnt = target // coin
    if cnt != 0:
        res += cnt
        target -= cnt * coin
print(res)