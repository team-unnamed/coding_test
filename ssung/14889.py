import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().rstrip("\n"))
stats = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]

all_cases = list(combinations([i for i in range(N)], N // 2))  # 팀이 될 수 있는 모든 경우의 수

stat_gap = sys.maxsize
for i in range(len(all_cases) // 2):
    # 첫 번째 팀
    a_team = all_cases[i]
    a_stat = 0
    for member1 in a_team:
        for member2 in a_team:
            a_stat += stats[member1][member2]

    # 두 번째 팀
    b_team = all_cases[-(i + 1)]  # combinations list에서 대칭으로 팀을 나눌 수 있음
    b_stat = 0
    for member1 in b_team:
        for member2 in b_team:
            b_stat += stats[member1][member2]

    stat_gap = min(stat_gap, abs(a_stat - b_stat))

print(stat_gap)
