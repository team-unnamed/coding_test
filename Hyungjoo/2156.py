n = int(input())
cost = [int(input()) for _ in range(n)]
case = [0] * n

for i in range(n):
    if i == 0:
        case[i] = cost[i]
    elif i == 1:
        case[i] = cost[i - 1] + cost[i]
    else:
        case[i] = max(case[i - 3] + cost[i - 1] + cost[i], case[i - 2] + cost[i], case[i - 1])

print(case[-1])
