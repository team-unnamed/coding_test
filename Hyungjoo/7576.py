from collections import deque


m, n = map(int, input().split())
board = []
visit = []
bfs_q = deque()

# init
for n_i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

    visit_row = []
    for m_i in range(m):
        if row[m_i] == 1:
            bfs_q.append((n_i, m_i, 0))
        if row[m_i] == 0:
            visit_row.append(False)
        else:
            visit_row.append(True)
    visit.append(visit_row)

# run bfs
ans = 0
while bfs_q:
    cur_n, cur_m, cur_day = bfs_q.popleft()
    for d_m, d_n in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        next_n = cur_n + d_n
        next_m = cur_m + d_m
        if 0 <= next_m < m and 0 <= next_n < n and not visit[next_n][next_m]:
            visit[next_n][next_m] = True
            bfs_q.append((next_n, next_m, cur_day + 1))
            if cur_day + 1 > ans:
                ans = cur_day + 1

flag = True
for row in visit:
    if sum(row) < m:
        flag = False
        break

if flag:
    print(ans)
else:
    print(-1)
