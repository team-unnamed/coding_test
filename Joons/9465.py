# 스티커
# 이놈의 주인공은 한장을 때면 주변의 스티커가(이웃한 스티커들) 훼손되어서 사용 할 수 없다고한다.
# 각 스티커 별로 점수가 부여 되어 있으며 위 규칙에 맞게 뜯었을떄, 최고 점수를 출력해라

# dp --> 1차원 arr
# dp[i] = max(dp[j]) + stciker[i%2][i// 2]
# i 가 짝수 일때, i-1, i-2 를 제외한 최댓값 (j != i-1, i-2)
# i 가 홀수 일때, i-2 를 제외한 최댓값 (j!=i-2)
"""
ex)
1
5
50 10 100 20 40
30 50 70 10 60
"""

import sys
input = sys.stdin.readline

problem = int(input())
for _ in range(problem):
    n = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]

    dp = [0] * (2*n)
    dp[0], dp[1] = stickers[0][0], stickers[1][0]

    for i in range(2, len(dp)):
        if i%2 == 0: # 홀수번 (맨 우측상단)
            m = max(dp[i-1], dp[i-3])
        else: # 짝수번 (맨 우측 아랫단)
            m = max(dp[i-3],dp[i-5])
        dp[i] = stickers[i%2][i//2] + m
    print(max(dp))
    
    

