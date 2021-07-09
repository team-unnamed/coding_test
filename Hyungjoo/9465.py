t = int(input())
for _ in range(t):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(2)]

    case = [[0, 0] for _ in range(n)]
    for i in range(n):
        if i == 0:
            case[i] = [cost[0][i], cost[1][i]]
        elif i == 1:
            case[i] = [cost[1][i - 1] + cost[0][i], cost[0][i - 1] + cost[1][i]]
        else:
            case[i][0] = max(case[i - 2][0] + cost[0][i], case[i - 2][1] + cost[0][i], case[i - 1][1] + cost[0][i])
            case[i][1] = max(case[i - 2][0] + cost[1][i], case[i - 2][1] + cost[1][i], case[i - 1][0] + cost[1][i])

    print(max(case[-1]))
