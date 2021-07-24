from math import inf
from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
break_count = [[inf] * m for _ in range(n)]

bfs_q = deque([(0, 0)])
break_count[0][0] = 0

while bfs_q:
    cur_n, cur_m = bfs_q.popleft()

    for d_n, d_m in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        next_n, next_m = cur_n + d_n, cur_m + d_m

        if not (0 <= next_n < n and 0 <= next_m < m):
            continue

        if board[next_n][next_m] == 0:
            next_break_count = break_count[cur_n][cur_m]
        elif board[next_n][next_m] == 1:
            next_break_count = break_count[cur_n][cur_m] + 1

        if next_break_count < break_count[next_n][next_m]:
            break_count[next_n][next_m] = next_break_count
            bfs_q.append((next_n, next_m))

print(break_count[-1][-1])
