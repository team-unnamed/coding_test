n = int(input())
seq = list(map(int, input().split()))

upstream = [1 for _ in range(n)]
downstream = [1 for _ in range(n)]
ans = [-1 for _ in range(n)]

# calculate increasing subsequence.
for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j] and upstream[i] <= upstream[j]:
            upstream[i] = upstream[i] + 1

# calculate decreasing subsequence.
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if seq[i] > seq[j] and downstream[i] <= downstream[j]:
            downstream[i] = downstream[j] + 1

# calculate the longest bitonic subsequence length.
for i in range(n):
    ans[i] += upstream[i] + downstream[i]

print(max(ans))
