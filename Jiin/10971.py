"""
도시를 전부 여행하고 원래 도시로 돌아와야 함
어떤 도시에서 출발하든 상관없음
순열을 전부 구해서 경로 마지막에 출발 도시 붙여서 구하면 되겠지
"""

import sys, itertools

def sol():
    N = int(sys.stdin.readline())
    map_ = [list(map(int, sys.stdin.readline().split())) for __ in range(N)]

    for i in range(N):
        for j in range(N):
            if map_[i][j] == 0:  # 갈 수 없는 길 따로 처리하면 귀찮으니까 대신 엄청 큰 값으로 대체
                map_[i][j] = 10_000_000  # 주어지는 값은 항상 1_000_000 이하의 양수

    permu = itertools.permutations(range(N), N)
    cost_min = float('inf')

    for route in permu:
        start = route[0]
        route = route + (start,)
        cost = 0
        for i in range(N):
            cur = route[i]
            nxt = route[i + 1]
            cost += map_[cur][nxt]

        cost_min = min(cost_min, cost)
    return cost_min

print(sol())
