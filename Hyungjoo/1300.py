from math import inf


n = int(input())
k = int(input())

ans = inf


def solution(cur_num, min_num, max_num):
    global n, k, ans

    count = 0
    for i in range(1, n + 1):
        count += min(cur_num // i, n)

    if count >= k and cur_num < ans:
        ans = cur_num

    if count >= k and (cur_num + min_num) // 2 < cur_num:
        solution((cur_num + min_num) // 2, min_num, cur_num)
    if count < k and (cur_num + max_num) // 2 > cur_num:
        solution((cur_num + max_num) // 2, cur_num, max_num)


solution((n * n) // 2, 1, (n * n) + 1)
print(ans)
