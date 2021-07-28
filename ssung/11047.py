import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip("\n").split(" "))
coin = [int(input().rstrip("\n")) for _ in range(N)]

answer = 0
for i in range(-1, -N - 1, -1):
    if K < coin[i]:  # 동전의 종류가 남은 금액보다 크면 넘어간다.
        continue

    coin_cnt = K // coin[i]  # 현재 동전의 종류로 최대한 많은 금액으로 만든다.
    K -= coin_cnt * coin[i]  # 남은 금액 업데이트

    answer += coin_cnt

print(answer)
