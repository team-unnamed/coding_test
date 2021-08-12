n, c = map(int, input().split())
x_pos = sorted([int(input()) for _ in range(n)])
dists = [x_pos[i + 1] - x_pos[i] for i in range(len(x_pos[:-1]))]

ans = 0


def check(cur_dist):
    global c

    count = 0
    cache = 0
    for dist in dists:
        cache += dist

        if cache >= cur_dist:
            count += 1
            cache = 0

    if count >= c - 1:
        return True
    else:
        return False


def solution(cur_dist, min_dist, max_dist):
    global ans

    ret = check(cur_dist)

    if ret and cur_dist > ans:
        ans = cur_dist

    if ret and (cur_dist + max_dist) // 2 > cur_dist:
        solution((cur_dist + max_dist) // 2, cur_dist, max_dist)
    if not ret and (cur_dist + min_dist) // 2 < cur_dist:
        solution((cur_dist + min_dist) // 2, min_dist, cur_dist)


solution(sum(dists) // 2, 1, sum(dists) + 1)
print(ans)
