from itertools import combinations
from math import inf

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]


def get_synergy(nums: list):
    score_sum = 0
    for i in nums:
        for j in nums:
            score_sum += score[i][j]

    return score_sum


cases = combinations(range(n), n // 2)
score_diff = inf
for case in cases:
    start_team = case
    link_team = [i for i in range(n) if i not in start_team]

    start_score = get_synergy(start_team)
    link_score = get_synergy(link_team)

    diff = abs(start_score - link_score)
    if diff < score_diff:
        score_diff = diff

print(score_diff)
