n = int(input())
src = list(map(int, list(input())))
tgt = list(map(int, list(input())))


def solution(size, start_with):
    switch_turned = [None] * size
    switch_turned[0] = start_with
    for n_i in range(n - 1):
        if n_i == 0:
            if src[0] == tgt[0]:
                switch_turned[1] = switch_turned[0]
            else:
                switch_turned[1] = not switch_turned[0]
        else:
            if src[n_i] == tgt[n_i]:
                switch_turned[n_i + 1] = not (switch_turned[n_i] == switch_turned[n_i - 1])
            else:
                switch_turned[n_i + 1] = (switch_turned[n_i] == switch_turned[n_i - 1])

    if (switch_turned[-1] == switch_turned[-2]) == (src[-1] == tgt[-1]):
        return True, sum(switch_turned)
    elif (switch_turned[-1] == switch_turned[-2]) != (src[-1] == tgt[-1]):
        return False, 0
    else:
        return None


succeed = False
for case, sum_switched in [solution(n, False), solution(n, True)]:
    if case:
        print(sum_switched)
        succeed = True
        break

if not succeed:
    print(-1)
