import heapq as hq
from math import inf


n, m, x = map(int, input().split())
graph = {node: [] for node in range(1, n + 1)}

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])


def dijkstra(start_node):
    global n, m, x

    dist = {node: inf for node in range(1, n + 1)}
    dist[start_node] = 0

    pq = []
    hq.heappush(pq, [dist[start_node], start_node])

    # dijkstra
    while pq:
        cur_dist, cur_node = hq.heappop(pq)

        for connect_node, connect_dist in graph[cur_node]:
            candidate_dist = cur_dist + connect_dist
            if candidate_dist < dist[connect_node]:
                dist[connect_node] = candidate_dist
                hq.heappush(pq, [candidate_dist, connect_node])

    return dist


# calculate all node's shortes distance with dijkstra algorithm
dist_info = {node: dijkstra(node) for node in range(1, n + 1)}
max_dist = 0

for node in range(1, n + 1):
    # pass node held party
    if node == x:
        continue

    dist = dist_info[node][x] + dist_info[x][node]
    if dist > max_dist:
        max_dist = dist

print(max_dist)
