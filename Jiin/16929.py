"""
배열의 각 칸에 대해 visited를 만들고, 각각 bfs 돌면서 방문 체크
방문한 적 있으면 그 칸을 시작지점으로 삼지 않음

사이클을 이루려면 언젠가 방문했던 지점으로 돌아와야 하는데 지금까지 거쳐온 경로의 길이를 따로 체크해서
방문한 적 있더라도 경로의 길이가 (어떤 값) 이상이면 그 지점을 방문함으로써 사이클이 완성되니까 방문 또 할 수 있게

근데 그럼 경로가 4일때 바로 직전 칸으로 돌아가 버린다...
좀 지저분하긴 한데 이전 칸이 어디었는지를 달고 다니게 하면 될 듯
"""

import sys, collections


def bfs(r, c):
    global visited
    dr = (0, 1, 0, -1)
    dc = (1, 0, -1, 0)

    q = collections.deque()
    q.append((r, c, 0, r, c)) # 현재 좌표, 경로 길이, 이전 좌표

    while q:
        front = q[0]
        q.popleft()

        row = front[0]
        col = front[1]
        length = front[2]
        old_r = front[3]
        old_c = front[4]

        visited[row][col] = True

        for i in range(4):
            next_r = row + dr[i]
            next_c = col + dc[i]

            if 0 <= next_r < N and 0 <= next_c < M and board[row][col] == board[next_r][next_c]:
                if not visited[next_r][next_c]:
                    q.append((next_r, next_c, length+1, row, col))

                if visited[next_r][next_c] and (next_r, next_c) != (old_r, old_c):
                    print("Yes")
                    exit()

N, M = map(int, sys.stdin.readline().split())

board = []
visited = [[False for _ in range(M)] for __ in range(N)]
for i in range(N):
    line = list(sys.stdin.readline().strip())
    board.append(line)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j)

print("No")
