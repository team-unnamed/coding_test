k = int(input())
paper = [list(map(int, input().split())) for _ in range(k)]

# counter for [-1, 0, 1]
counter = [0, 0, 0]


def solution(h_s, h_e, w_s, w_e):
    global counter

    cur_symbol = paper[h_s][w_s]
    for h_i in range(h_s, h_e):
        for w_i in range(w_s, w_e):
            if paper[h_i][w_i] != cur_symbol:
                step = (h_e - h_s) // 3
                for h_step in range(h_s, h_e, step):
                    for w_step in range(w_s, w_e, step):
                        solution(h_step, h_step + step, w_step, w_step + step)
                return

    if cur_symbol == -1:
        counter[0] += 1
    elif cur_symbol == 0:
        counter[1] += 1
    elif cur_symbol == 1:
        counter[2] += 1


solution(0, k, 0, k)
for count in counter:
    print(count)
