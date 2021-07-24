"""

bfs로 탐색을 하면서 벽을 부순 횟수를 최소화 하면 된다.
crash[i][j]: (i, j)에 도착할 때까지 벽을 부순 최소 횟수

"""
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip("\n").split(" "))
maze = [list(map(int, input().rstrip("\n"))) for _ in range(N)]
crash = [[sys.maxsize for _ in range(M)] for _ in range(N)]  # 벽을 부순 횟수 저장

dx = [0, 0, -1, 1]  # x좌표 이동
dy = [-1, 1, 0, 0]  # y좌표 이동


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    crash[y][x] = 0

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0 <= nx) and (nx < M) and (0 <= ny) and (ny < N):
                if maze[ny][nx] == 0:  # 벽이 없으면 부수지 않고 이동 가능
                    if crash[ny][nx] > crash[cur_y][cur_x]:
                        crash[ny][nx] = crash[cur_y][cur_x]
                        queue.append([nx, ny])
                else:  # 벽이라면 부수고 이동 가능
                    if crash[ny][nx] > crash[cur_y][cur_x] + 1:
                        crash[ny][nx] = crash[cur_y][cur_x] + 1
                        queue.append([nx, ny])


bfs(0, 0)
print(crash[N - 1][M - 1])
