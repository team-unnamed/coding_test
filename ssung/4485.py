"""

1261 알고스팟 문제와 유사하다. (bfs + dijkstra)
시작점(0, 0)에서 목적지(n-1, n-1)까지 최소비용을 갱신하면서 bfs로 탐색을 하면 된다.

유의할 점은 목적지에 처음 도달 했을 때가 최소비용이 아닐 수도 있다는 것.
(n-1, n-2), (n-2, n-1) 두 지점을 경유하는 비용을 비교해야 한다.

"""
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]  # x 좌표 이동
dy = [-1, 1, 0, 0]  # y 좌표 이동


def dijkstra(x, y, cave):
    length = len(cave)
    q = deque()
    dist = [[sys.maxsize for _ in range(length)] for _ in range(length)]  # 최소비용 저장
    q.append([0, 0])
    dist[0][0] = cave[0][0]  # 시작점은 무조건 지나야 함

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0 <= nx) and (nx < length) and (0 <= ny) and (ny < length):  # 다음 이동 위치가 동굴을 벗어나지 않을 경우 탐색
                if dist[cur_y][cur_x] + cave[ny][nx] < dist[ny][nx]:  # 최소비용 갱신
                    dist[ny][nx] = dist[cur_y][cur_x] + cave[ny][nx]
                    q.append([nx, ny])

    return dist[length - 1][length - 1]


case = 1
while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
    print(f"Problem {case}: {dijkstra(0, 0, cave)}")  # case마다 출력

    case += 1
