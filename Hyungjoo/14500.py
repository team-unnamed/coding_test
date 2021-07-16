n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


poly_pos = [
    # case 1
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # case 2
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # case 3
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 1], [1, 1], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[1, 0], [1, 1], [0, 2], [1, 2]],
    # case 4
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 0]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # case 5
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
]


def check(board, h_size, w_size):
    ans = 0
    for h in range(h_size):
        for w in range(w_size):
            for pos_case in poly_pos:
                score = 0
                for h_pos, w_pos in pos_case:
                    if h + h_pos < h_size and w + w_pos < w_size:
                        score += board[h + h_pos][w + w_pos]
                    else:
                        score = 0
                        break
                if score > ans:
                    ans = score

    return ans


print(check(board, n, m))
