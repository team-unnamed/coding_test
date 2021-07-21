"""

dfs 매개 변수

start_x, start_y : 시작지점
cur_x, cur_y : 현재 위치
direction : 상(0), 하(1), 좌(2), 우(3) 방향 체크
turn_cnr : 진행방향이 몇번 꺾였는지 체크. 
           사이클이 되려면 사각형이어야 하므로 turn_cnt >= 4 를 만족해야 하고
           direction이 바뀔 때마다 turn_cnt += 1 해주었다.

"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
game = [list(input().rstrip("\n")) for _ in range(N)]
dx = [0, 0, -1, 1]  # x방향 이동
dy = [-1, 1, 0, 0]  # y방향 이동
isVisited = [[False for _ in range(M)] for _ in range(N)]  # 방문했던 점인지 체크한다

global isCycle
isCycle = False  # 사이클 체크


def dfs(start_x, start_y, cur_x, cur_y, direction, turn_cnt):
    global isCycle
    if isCycle:
        return

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if (0 <= nx) and (nx < M) and (0 <= ny) and (ny < N):  # 다음 탐색 지점이 게임판 안에 위치해야 한다.
            if isVisited[ny][nx]:
                if (nx == start_x) and (ny == start_y) and (turn_cnt >= 4):  # 이미 방문했던 노드에 도착했고, 사이클이 존재하면 함수 종료
                    isCycle = True
                    return
            else:
                if game[cur_y][cur_x] == game[ny][nx]:  # 현재 점과 다음 점이 같아야 한다
                    isVisited[ny][nx] = True
                    if i == direction:  # 같은 방향으로 진행중이면 turn_cnt를 더해주지 않음
                        dfs(start_x, start_y, nx, ny, i, turn_cnt)
                    else:  # 방향이 꺾였다면 turn_cnt + 1
                        dfs(start_x, start_y, nx, ny, i, turn_cnt + 1)
                    isVisited[ny][nx] = False


for y in range(N):
    for x in range(M):
        isVisited[y][x] = True
        dfs(x, y, x, y, 0, 1)
        if isCycle:
            print("Yes")
            exit(0)

print("No")
