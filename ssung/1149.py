"""

 첫 번째 집의 색을 결정하고 greedy하게?? 다음 집의 색을 고른다.
 cost_r : 첫 번째 집의 색이 r일 때 최종 비용
 cost_g : 첫 번째 집의 색이 g일 때 최종 비용 
 cost_b : 첫 번째 집의 색이 b일 때 최종 비용

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
cost_r = cost_g = cost_b = 0
for _ in range(N):
    r, g, b = map(int, input().rstrip("\n").split(" "))

    # 인접한 집을 다른 색으로 칠하면서 비용을 최소화한다.
    r += min(cost_g, cost_b)
    g += min(cost_r, cost_b)
    b += min(cost_r, cost_g)

    # 최종 비용 업데이트
    cost_r = r
    cost_g = g
    cost_b = b

print(min(cost_r, cost_g, cost_b))
