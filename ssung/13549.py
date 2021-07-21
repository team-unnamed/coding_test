"""

2*X 위치로 순간이동 하는 경우는 이동 시간이 0초이기 때문에 가장 먼저 이동해보아야 함.

"""
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip("\n").split(" "))
queue = deque()
dist = [-1 for _ in range(100001)]


def bfs(start, end):
    queue.append(start)
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        if cur == end:
            return dist[cur]

        if (2 * cur <= 100000) and (dist[2 * cur] == -1):  # 2*X 순간이동은 0초이므로 먼저 계산해야 함
            dist[2 * cur] = dist[cur]
            queue.append(2 * cur)
        
        if (0 <= cur - 1) and (dist[cur - 1] == -1):  # X-1 위치로 1초 후 이동
            dist[cur - 1] = dist[cur] + 1
            queue.append(cur - 1)
        
        if (cur + 1 <= 100000) and (dist[cur + 1] == -1):  # X+1 위치로 1초 후 이동
            dist[cur + 1] = dist[cur] + 1
            queue.append(cur + 1)


print(bfs(N, K))
