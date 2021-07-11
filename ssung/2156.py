"""

wine[i]: i번째 포도주의 양.
dp[i]: i번째 위치에서 마실 수 있는 포도주의 최대 양

우선 현재 위치에서 포도주를 마시지 않거나(1) 마시는 경우가 있다.
(1): dp[i] = dp[i-1]

마시는 경우는 이전 포도주를 마셨는지(2) 마시지 않았는지(3) 두 가지로 나눌 수 있다.
(2): dp[i] = dp[i-3] + wine[i-1] + wine[i]
(3): dp[i] = dp[i-2] + wine[i]

3 가지 경우 중 가장 많이 마실 수 있는 경우를 고르면 된다.
dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

"""
import sys

input = sys.stdin.readline


def solution():
    n = int(input().rstrip("\n"))
    wine = [0]
    for _ in range(n):
        wine.append(int(input().rstrip("\n")))

    dp = [0 for _ in range(n + 1)]
    dp[1] = wine[1]
    if n != 1: # n = 1이면 IndexError가 발생하기 때문에 예외 처리.
        dp[2] = wine[1] + wine[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

    print(dp[n])


if __name__ == "__main__":
    solution()
