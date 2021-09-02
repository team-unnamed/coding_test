import sys
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
num_len = len(nums)

ans = inf
i, j = 0, 0
while i < num_len and j < num_len:
    cur_diff = nums[j] - nums[i]

    if m <= cur_diff < ans:
        ans = cur_diff

    if cur_diff < m:
        j += 1
    else:
        i += 1

print(ans)
