import heapq
from math import inf
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
start_node = int(input())

graph = {node: [] for node in range(1, v + 1)}
for _ in range(e):
    src, tgt, weight = map(int, input().split())
    graph[src].append([tgt, weight])

dist = {node: inf for node in range(1, v + 1)}
dist[start_node] = 0

# init prority queue
pq = []
heapq.heappush(pq, [dist[start_node], start_node])

# dijkstra
while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    for connect_node, connect_dist in graph[cur_node]:
        candidate_dist = cur_dist + connect_dist
        if candidate_dist < dist[connect_node]:
            dist[connect_node] = candidate_dist
            heapq.heappush(pq, [candidate_dist, connect_node])

for k, v in dist.items():
    if v == inf:
        print("INF")
    else:
        print(v)
