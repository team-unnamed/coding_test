from collections import deque


while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    land_pos = deque()
    board = []
    for h_i in range(h):
        board.append(list(map(int, input().split())))
        for w_i in range(w):
            if board[h_i][w_i] == 1:
                land_pos.append((h_i, w_i))

    visit = [[False] * w for _ in range(h)]

    land_count = 0
    while land_pos:
        land_count += 1

        init_h, init_w = land_pos.popleft()
        visit[init_h][init_w] = True

        bfs_q = deque()
        bfs_q.append((init_h, init_w))

        while bfs_q:
            cur_h, cur_w = bfs_q.popleft()

            for d_h in [-1, 0, 1]:
                for d_w in [-1, 0, 1]:
                    if d_h == d_w == 0:
                        continue

                    next_h = cur_h + d_h
                    next_w = cur_w + d_w

                    if 0 <= next_h < h and 0 <= next_w < w and board[next_h][next_w] == 1 and not visit[next_h][next_w]:
                        visit[next_h][next_w] = True
                        bfs_q.append((next_h, next_w))

                        if (next_h, next_w) in land_pos:
                            land_pos.remove((next_h, next_w))

    print(land_count)
