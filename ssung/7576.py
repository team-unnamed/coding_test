import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip("\n").split(" "))
tomato = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
dx = [0, 0, -1, 1]  # x좌표 이동
dy = [-1, 1, 0, 0]  # y좌표 이동
queue = deque()  # bfs를 위한 queue


def bfs():
    while queue:
        cur_x, cur_y = queue.popleft()
        cur_status = tomato[cur_y][cur_x]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (
                (0 <= nx)
                and (nx < M)
                and (0 <= ny)
                and (ny < N)
                and (tomato[ny][nx] == 0)
            ):
                tomato[ny][nx] = cur_status + 1
                queue.append([nx, ny])

    for y in range(N):
        for x in range(M):
            if tomato[y][x] == 0:  # 익지 않은 토마토가 존재하면 -1 출력
                return -1

    return max(map(max, tomato)) - 1


# 초기 토마토의 상태가 1이면 queue에 넣어준다. (해당 지점에서 bfs 진행)
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            queue.append([x, y])

init_tomato = N * M - tomato.count(-1)
if len(queue) == init_tomato:  # 모든 토마토가 이미 익어있는 상태면 0 출력
    print(0)
else:  # 그렇지 않은 경우 bfs로 토마토가 모두 익는 날짜를 찾아야 함
    print(bfs())
