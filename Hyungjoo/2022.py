x, y, c = map(float, input().split())


def calculate_c(width):
    global x, y

    h_1 = ((x * x) - (width * width)) ** 0.5
    h_2 = ((y * y) - (width * width)) ** 0.5

    return (h_1 * h_2) / (h_1 + h_2)


def solution(cur_width, min_width, max_width):
    global c

    cur_c = calculate_c(cur_width)

    if abs(c - cur_c) <= 0.000_000_1:
        print(cur_width)
    elif cur_c > c:
        solution((cur_width + max_width) / 2, cur_width, max_width)
    elif cur_c < c:
        solution((cur_width + min_width) / 2, min_width, cur_width)


solution(min(x, y) / 2, 0, min(x, y))
