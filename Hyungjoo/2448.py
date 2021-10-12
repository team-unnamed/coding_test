from math import log2

n = int(input())
k = int(log2(n // 3))

star_map = [
    "*",
    "* *",
    "*****",
]


def append_star(count: int):
    global star_map

    if count == 0:
        return
    else:
        empty_space = len(star_map[-1])
        for idx in range(len(star_map)):
            new_row = (" " * empty_space).join([star_map[idx]] * 2)
            star_map.append(new_row)
            empty_space -= 2
        append_star(count - 1)


append_star(k)

line_width = len(star_map[-1])
for idx in range(len(star_map)):
    star_map[idx] = star_map[idx].center(line_width, " ")

print("\n".join(star_map), end="")
