"""

9251 LCS 문제와 출력 방식만 다른 문제. LCS의 길이와 LCS를 출력하면 된다.
길이가 아닌 문자를 기준으로 LCS 알고리즘을 구현하면 된다.
9251번 문제와 line 20, 22만 다르다

"""
import sys

input = sys.stdin.readline

str_a = input().rstrip()
str_b = input().rstrip()

dp = [["" for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]

for i in range(1, len(str_a) + 1):
    for j in range(1, len(str_b) + 1):
        if str_a[i - 1] == str_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + str_a[i - 1]
        else:
            dp[i][j] = dp[i - 1][j] if len(dp[i][j - 1]) < len(dp[i - 1][j]) else dp[i][j - 1]

answer = dp[len(str_a)][len(str_b)]
print(len(answer))
print(answer)
