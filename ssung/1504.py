"""

반드시 거쳐야 하는 두 개의 서로 다른 정점을 v1, v2라고 할 때
(1번 정점 ~ v1 정점), (1번 정점 ~ v2 정점) 두 가지 경로 중 더 짧은 경로로 이동하면 된다.
v1에서 v2로 이동하는 경로는 같으므로 위에서 구한 더 짧은 경로에 더해주면 v1, v2 정점을 반드시 지나는 최단경로가 된다.

"""
import sys
import heapq as hq

input = sys.stdin.readline

N, E = map(int, input().rstrip("\n").split(" "))
road = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip("\n").split(" "))
    road[a].append([b, c])
    road[b].append([a, c])

v1, v2 = map(int, input().rstrip("\n").split(" "))


def dijkstra(start, end):
    heap = []
    dist = [sys.maxsize for _ in range(N + 1)]
    hq.heappush(heap, [0, start])
    dist[start] = 0

    while heap:
        cur_cost, cur_node = hq.heappop(heap)

        if cur_node == end:  # 목적지에 도달했다면 함수 종료
            return dist[cur_node]

        for next_node, next_cost in road[cur_node]:
            if cur_cost + next_cost < dist[next_node]:  # 최단 경로 갱신
                dist[next_node] = cur_cost + next_cost
                hq.heappush(heap, [dist[next_node], next_node])
    
    return dist[cur_node]


answer = sys.maxsize
start_to_v1 = dijkstra(1, v1)  # 1번 정점에서 v1정점으로 이동하는 최단경로
start_to_v2 = dijkstra(1, v2)  # 1번 정점에서 v2정점으로 이동하는 최단경로
v1_to_v2 = dijkstra(v1, v2)  # v1정점에서 v2정점으로 이동하는 최단경로
v1_to_end = dijkstra(v1, N)  # v1정점에서 N번 정점으로 이동하는 최단경로
v2_to_end = dijkstra(v2, N)  # v2정점에서 N번 정점으로 이동하는 최단경로

answer = min(start_to_v1 + v1_to_v2 + v2_to_end, start_to_v2 + v1_to_v2 + v1_to_end)  # 더 짧은 경로를 찾는다.
if answer == 0:
    print(-1)
else:
    print(answer)
