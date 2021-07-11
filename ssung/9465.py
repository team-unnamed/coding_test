"""

sticker[i][j]: i행 j열에서 얻을 수 있는 점수의 최댓값

j열을 기준으로 점수를 얻을 수 있는 경우의 수는
j-1열에서 스티커를 뗀 경우(1)와 
j-1열에서 스티커를 떼지 않은 경우(2) 두 가지 이다.
(1) sticker[0][j] = sticker[1][j-1],
    sticker[1][j] = sticker[0][j-1]

(2) sticker[0][j] = sticker[1][j-2], (sticker[0][j-2]는 (1)에 포함된다)
    sticker[1][j] = sticker[0][j-2]  (sticker[1][j-2]는 (1)에 포함된다)

두 가지 경우를 고려하여 최댓값을 구하면 됨.
sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

"""
import sys

input = sys.stdin.readline


def dp(sticker, n):
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]

    for i in range(2, n):
        sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])

    print(max(map(max, sticker)))


def solution():
    # input
    tc = int(input().rstrip("\n"))
    for _ in range(tc):
        sticker = []  # case마다 list 초기화
        n = int(input().rstrip("\n"))
        for _ in range(2):
            sticker.append(list(map(int, input().rstrip("\n").split(" "))))

        # dynamic programming
        dp(sticker, n)


if __name__ == "__main__":
    solution()
