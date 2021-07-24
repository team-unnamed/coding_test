from itertools import permutations
from math import inf

n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]

ans = inf
for case in permutations(range(n)):
    case += (case[0],)
    circular = True
    cost = 0
    for i in range(len(case) - 1):
        cost += weight[case[i]][case[i + 1]]

        if cost > ans or weight[case[i]][case[i + 1]] == 0:
            circular = False
            break

    if circular and cost < ans:
        ans = cost

print(ans)
