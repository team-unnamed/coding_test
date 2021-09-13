g = int(input())

cur_p, pre_p = 1, 1
ans = []

while 2 * cur_p - 1 <= g:
    if (cur_p + pre_p) * (cur_p - pre_p) < g:
        cur_p += 1
    elif (cur_p + pre_p) * (cur_p - pre_p) > g:
        pre_p += 1
    else:
        ans.append(cur_p)
        cur_p += 1
        pre_p += 1

if ans:
    for ans_ in ans:
        print(ans_)
else:
    print(-1)
