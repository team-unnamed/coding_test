def get_pos(d_i, d_e, d_q):
    step = 2 ** (d_e - d_i - 1)
    quadrant_step = [[0, step], [0, 0], [step, 0], [step, step]]

    return quadrant_step[d_q]


def solution(h_s, h_e, w_s, w_e, d_num):
    global h_pos, w_pos

    if h_s <= h_pos < h_e and w_s <= w_pos < w_e:
        if (h_e - h_s) == 1 and (w_e - w_s) == 1 and (h_s == h_pos) and (w_s == w_pos):
            print(d_num)
        else:
            h_m = (h_s + h_e) // 2
            w_m = (w_s + w_e) // 2
            solution(h_s, h_m, w_s, w_m, d_num + "2")
            solution(h_s, h_m, w_m, w_e, d_num + "1")
            solution(h_m, h_e, w_s, w_m, d_num + "3")
            solution(h_m, h_e, w_m, w_e, d_num + "4")


d, d_num = map(int, input().split())
m_w, m_h = map(int, input().split())

h_pos, w_pos = 0, 0
for i, q in enumerate(str(d_num)):
    q_h, q_w = get_pos(i, d, int(q) - 1)
    h_pos += q_h
    w_pos += q_w

h_pos -= m_h
w_pos += m_w

if 0 <= h_pos < 2 ** d and 0 <= w_pos < 2 ** d:
    solution(0, 2 ** d, 0, 2 ** d, "")
else:
    print(-1)
