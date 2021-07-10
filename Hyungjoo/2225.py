n, k = list(map(int, input().split()))

case = [[1] * (n + 1) for _ in range(k)]

for i in range(1, k):
    for j in range(1, n + 1):
        case[i][j] = sum(case[i - 1][: j + 1])

print(case[-1][-1] % 1_000_000_000)
