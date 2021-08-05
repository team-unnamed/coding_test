import sys


n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# save where the number is on in_order array
post_to_in = [0] * (n + 1)
for i in range(n):
    post_to_in[in_order[i]] = i

# use first-in last-out queue
FILO_Q = [(0, n, 0, n)]
while FILO_Q:
    in_s, in_e, post_s, post_e = FILO_Q.pop()

    # print root node
    root_node = post_order[post_e - 1]
    root_in_idx = post_to_in[root_node]
    sys.stdout.write(f"{root_node} ")

    # calculate each sub-graph size
    left_size = root_in_idx - in_s
    right_size = in_e - root_in_idx - 1

    if right_size > 0:
        FILO_Q.append((in_e - right_size, in_e, post_e - right_size - 1, post_e - 1))
    if left_size > 0:
        FILO_Q.append((in_s, in_s + left_size, post_s, post_s + left_size))
