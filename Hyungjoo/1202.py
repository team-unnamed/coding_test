import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
juwelry_infos = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
bag_sizes = sorted([int(input()) for _ in range(k)])

ans = 0
candidates = []
for bag_size in bag_sizes:
    while juwelry_infos and juwelry_infos[0][0] <= bag_size:
        heapq.heappush(candidates, -juwelry_infos[0][1])
        heapq.heappop(juwelry_infos)

    # if a juwelry that has current maximum cost can be on current bag,
    if candidates:
        ans -= heapq.heappop(candidates)
    # if no candidates and no juwelry left,
    elif not juwelry_infos:
        break

print(ans)
