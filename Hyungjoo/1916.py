import sys

from math import inf
import heapq as hq

input = sys.stdin.readline


n = int(input())
m = int(input())
graph = {node: [] for node in range(1, n + 1)}
for _ in range(m):
    s, t, w = map(int, input().split())
    graph[s].append([t, w])
start, end = map(int, input().split())

dist = {node: inf for node in range(1, n + 1)}
dist[start] = 0

pq = []
hq.heappush(pq, [dist[start], start])

while pq:
    cur_dist, cur_node = hq.heappop(pq)

    if cur_dist > dist[cur_node]:
        continue

    for connect_node, connect_dist in graph[cur_node]:
        candidate_dist = dist[cur_node] + connect_dist
        if candidate_dist < dist[connect_node]:
            dist[connect_node] = candidate_dist
            hq.heappush(pq, [candidate_dist, connect_node])

print(dist[end])
