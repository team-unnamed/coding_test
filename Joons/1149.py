# RGB 거리
# 각 집을 색칠하는데, 인접하는 집 끼리는 색을 같게 하면 안된다.
# 각 집 마다의 RGB를 색칠함에 있어 비용이 나온다.
# 매 step (집) 을 돌때 RGB 마다의 비용을 남긴다.
# 다음 step 에서 이전 step 의 비용을 기준으로 다시 갱신한다.

import sys

n = int(sys.stdin.readline().split()[0])
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0,0,0]

for c in cost:
    rgb_cost = dp.copy()
    # 색상별 for문
    for i in range(len(c)):
        tmp = max(rgb_cost)
        # 이전 rgb_cost(dp) 에서 동일 색상이 아닌 비용최소 색상
        for j in range(len(dp)):
            if (i!=j) and (rgb_cost[j] < tmp):
                tmp = rgb_cost[j]
        dp[i] = c[i] + tmp

print(min(dp))