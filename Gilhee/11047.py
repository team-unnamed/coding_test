n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

answer = 0

while coin:
    if coin[-1]>k:
        coin.pop(-1)
    else:
        i = k//coin[-1]

        k -=coin[-1]*i
        answer +=i

print(answer)