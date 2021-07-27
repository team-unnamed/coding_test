n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coin_counter = 0
for coin in reversed(coins):
    while k >= coin:
        coin_counter += k // coin
        k %= coin

print(coin_counter)
