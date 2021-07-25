import sys
from collections import deque

def bfs(r,c): # row, col
    q = deque()
    visited[r][c] = True
    q.append((r,c))

    while q:
        front = q[0]
        row = front[0]; col = front[1]
        q.popleft()

        for i in range(8):
            nextrow = row + drow[i]
            nextcol = col + dcol[i]

            if nextrow >= h or nextcol >= w or nextrow < 0 or nextcol < 0: continue

            if map_[nextrow][nextcol] and not visited[nextrow][nextcol]:
                visited[nextrow][nextcol] = True
                q.append((nextrow,nextcol))


drow = (1, 1, 0, -1, -1, -1, 0, 1)
dcol = (0, 1, 1, 1, 0, -1, -1, -1)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0: break
    map_ = [[] for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    island = 0

    for i in range(h):
        map_[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(h):
        for j in range(w):
            if map_[i][j] == 1 and not visited[i][j]:
                island += 1
                bfs(i,j)

    print(island)
