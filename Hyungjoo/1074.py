n, r, c = map(int, input().split())

counter = 0


def solution(r_s, r_e, c_s, c_e, cur_value):
    global r, c
    global counter

    if r_s <= r < r_e and c_s <= c < c_e:
        if r_s + 1 == r_e and c_s + 1 == c_e:
            if r_s == r and c_s == c:
                print(cur_value)
            counter += 1
        else:
            r_m = (r_s + r_e) // 2
            c_m = (c_s + c_e) // 2
            value_step = (r_m - r_s) * (c_m - c_s)

            solution(r_s, r_m, c_s, c_m, cur_value + value_step * 0)
            solution(r_s, r_m, c_m, c_e, cur_value + value_step * 1)
            solution(r_m, r_e, c_s, c_m, cur_value + value_step * 2)
            solution(r_m, r_e, c_m, c_e, cur_value + value_step * 3)


solution(0, 2 ** n, 0, 2 ** n, 0)
