# 퇴사
# 퇴사 일이 정해저 있고 각 일마다 상담 소요 기간, 받을 수 있는 금액 을 받는다.
# 퇴사 일 전까지 최대한의 금액을 받을때 얼마를 받을 수 있는지 남기시오
# dp로 접근 dp[i] = Max(p[i]+dp[j], dp[i]) i는 기준일 j < i

import sys
input = sys.stdin.readline

retire_day = int(input())
table = [list(map(int, input().split())) for _ in range(retire_day)]
dp = [table[i][1] for i in range(retire_day)]

for i in range(2,retire_day):
    for j in range(i):
        if (i-j) >= table[j][0]:
            dp[i] = max(table[i][1]+dp[j] , dp[i])

m = 0
for i in range(retire_day):
    if (i + table[i][0] <= retire_day):
        if m < dp[i]:
            m = dp[i]

print(m)



        


