n, m = map(int, input().split())
trees = list(map(int, input().split()))

ans = 0


def solution(cur_height, max_height, min_height):
    global n, m
    global trees
    global ans

    if cur_height == max_height or cur_height == min_height:
        return

    # calculate total acquired tree weights
    tree_value = 0
    for tree in trees:
        if tree > cur_height:
            tree_value += tree - cur_height

    # if total value higher than m and current height higher than previous cache
    if tree_value >= m and cur_height > ans:
        ans = cur_height

    # binary search
    if tree_value >= m:
        solution((cur_height + max_height) // 2, max_height, cur_height)
    else:
        solution((cur_height + min_height) // 2, cur_height, min_height)


solution(max(trees) // 2, max(trees), 0)
print(ans)
