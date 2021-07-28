from heapq import heappush, heappop
m, n = map(int, input().split())

Map = [input() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0] * m for i in range(n)]

def bfs():
    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        c, a, b = heappop(heap)
        if a == n - 1 and b == m - 1:
            print(c)
            return
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
                heappush(heap, [c + 1 if int(Map[x][y]) == 1 else c, x, y])
                visit[x][y] = 1
bfs()