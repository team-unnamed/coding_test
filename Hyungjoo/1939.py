from collections import deque

n, m = map(int, input().split())

max_w = 0
min_w = 1_000_000_000
bridge_info = [[] for _ in range(n + 1)]
for _ in range(m):
    src, tgt, weight = map(int, input().split())
    bridge_info[src].append((tgt, weight))
    bridge_info[tgt].append((src, weight))
    if weight > max_w:
        max_w = weight
    if weight < min_w:
        min_w = weight

start, end = map(int, input().split())
ans = 0


def bfs_search(threshold):
    global n, m
    global start, end

    bfs_q = deque()
    bfs_q.append(start)

    is_visit = [False for _ in range(n + 1)]
    is_visit[start] = True

    while bfs_q:
        cur_node = bfs_q.popleft()

        for connected_node, connected_w in bridge_info[cur_node]:
            if not is_visit[connected_node] and connected_w >= threshold:
                is_visit[connected_node] = True
                bfs_q.append(connected_node)

    if is_visit[end]:
        return True
    else:
        return False


def solution(cur_w, min_w, max_w):
    global ans

    passed = bfs_search(cur_w)
    if passed and cur_w > ans:
        ans = cur_w

    if passed and (cur_w + max_w) // 2 > cur_w:
        solution((cur_w + max_w) // 2, cur_w, max_w)
    if not passed and (cur_w + min_w) // 2 < cur_w:
        solution((cur_w + min_w) // 2, min_w, cur_w)


solution((min_w + max_w) // 2, min_w, max_w + 1)
print(ans)
