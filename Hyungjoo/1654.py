n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

ans = 0


def solution(cur_length, min_length, max_length):
    global k, ans

    line_count = 0
    for line in lines:
        line_count += line // cur_length

    if line_count >= k and cur_length > ans:
        ans = cur_length

    if line_count >= k and (cur_length + max_length) // 2 > cur_length:
        solution((cur_length + max_length) // 2, cur_length, max_length)
    if line_count < k and (cur_length + min_length) // 2 < cur_length:
        solution((cur_length + min_length) // 2, min_length, cur_length)


solution(max(lines), 1, max(lines) + 1)
print(ans)
