"""
LCS2

부분 최장수열 구하기

input : 문자열 2개
output : 부분 최장 수열, 해당 수열의 크기

dp방식으로 저장.
dp 에 담아야 할것. 
각 idx당 길이, 
"""
import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()


dp = [[[0,''] for _ in range(len(a)+1)] for _ in range(len(b)+1)]
# print(dp)
MAX = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[j+1][i+1][0] += dp[j][i][0]+1
            dp[j+1][i+1][1] += dp[j][i][1]+b[j]
        else:
            if dp[j][i+1][0] <= dp[j+1][i][0]:
                dp[j+1][i+1][0] = dp[j+1][i][0]
                dp[j+1][i+1][1] = dp[j+1][i][1]

            else:
                dp[j+1][i+1][0] = dp[j][i+1][0]
                dp[j+1][i+1][1] = dp[j][i+1][1]
        if MAX < dp[j+1][i+1][0]:
            MAX = dp[j+1][i+1][0]
            STR = dp[j+1][i+1][1]

for d in dp:
    print(d)
if MAX:
    print(MAX)
    print(STR)
else:
    print(MAX)
    