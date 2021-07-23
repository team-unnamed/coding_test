import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]  # x좌표 이동
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]  # y좌표 이동


def dfs(x, y, width, height, island: list, isVisited: list):
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if ( # 섬이 연결 되어있고 방문하지 않았으면 방문.
            (0 <= nx)
            and (nx < width)
            and (0 <= ny)
            and (ny < height)
            and (not isVisited[ny][nx])
            and (island[ny][nx] == 1)
        ):
            isVisited[ny][nx] = True
            dfs(nx, ny, width, height, island, isVisited)


while True:
    w, h = map(int, input().rstrip("\n").split(" "))
    if (w == 0) and (h == 0):  # 둘 다 0이면 종료.
        break

    island = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(h)]
    isVisited = [[False for _ in range(w)] for _ in range(h)]

    island_cnt = 0
    for y in range(h):
        for x in range(w):
            if (island[y][x] == 1) and (not isVisited[y][x]): # 섬의 개수 체크
                isVisited[y][x] = True
                island_cnt += 1
                dfs(x, y, w, h, island, isVisited)

    print(island_cnt)
