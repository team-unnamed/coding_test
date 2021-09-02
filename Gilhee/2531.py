N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

MAX = 0
for i in range(N):
    arr = [0 for _ in range(d+1)]
    kind = 0
    set = []
    for j in range(k):
        arr[sushi[(i+j) % N]] = 1
        set.append(sushi[(i+j) % N])
    kind += arr.count(1)

    if c not in set: 
        kind += 1

    MAX = max(MAX, kind)

print(MAX)