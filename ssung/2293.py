"""

반복문 부분을 예시로 이해해보자.
dp[0] = 1 (동전을 사용하지 않는 경우)

coin[i] = 2일 때, dp[k]를 구하려고 하면 k-2원을 만든 후 2원 동전을 추가하면 된다.
coin[i] = 5일 때도 마찬가지이다. dp[k]를 구하고 싶으면 k-5원을 만든 후 5원 동전을 추가.

일반화 해보면 k원을 만드는 방법은 k - coin[i]원을 만든 후 coin[i]원 동전을 추가하면 된다.
따라서 점화식은 dp[k] += dp[k - coin[i]]가 된다. (모든 종류의 동전을 고려해야 하기 때문에 결과를 계속 더해준다.)

"""
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip("\n").split(" "))
coin = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]  # dp[a] = b : a원을 만들 수 있는 경우의 수는 b이다.

dp[0] = 1
for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] += dp[j - coin[i]]  # 경우의 수 추가.

print(dp[k])
