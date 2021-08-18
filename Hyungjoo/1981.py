import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d_set = [[-1, 0], [0, -1], [1, 0], [0, 1]]
min_v, max_v = 200, 0
for row in board:
    min_row, max_row = min(row), max(row)
    if min_row < min_v:
        min_v = min_row
    if max_row > max_v:
        max_v = max_row


def bfs_search(min_threshold, max_threshold):
    global n

    if board[0][0] < min_threshold or board[0][0] > max_threshold:
        return False

    bfs_q = deque([(0, 0)])

    is_visit = [[False] * n for _ in range(n)]
    is_visit[0][0] = True

    while bfs_q:
        cur_h, cur_w = bfs_q.popleft()

        for d_h, d_w in d_set:
            next_h = cur_h + d_h
            next_w = cur_w + d_w
            if 0 <= next_h < n and 0 <= next_w < n and not is_visit[next_h][next_w]:
                if min_threshold <= board[next_h][next_w] <= max_threshold:
                    is_visit[next_h][next_w] = True
                    bfs_q.append((next_h, next_w))
                    if next_h == n - 1 and next_w == n - 1:
                        return True

    return False


left, right = 0, 0
max_v = max(map(max, board))
ans = 200
while left <= right <= max_v:
    if bfs_search(left, right):
        if right - left < ans:
            ans = right - left
        left += 1
    else:
        right += 1

print(ans)
