"""

기본적인 다익스트라 문제.
시작점에서 목적지까지 최소비용을 갱신하면서 진행한다.
최소 비용을 갱신하는 방법은 min heap을 이용해 비용이 적은 경로를 먼저 탐색하면서 갱신해준다.

"""
import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())
M = int(input())
city = [[] for _ in range(N + 1)]

# 그래프 정보 입력
for _ in range(M):
    u, v, w = map(int, input().rstrip("\n").split(" "))
    city[u].append([v, w])

start, end = map(int, input().rstrip("\n").split(" "))


def dijkstra(start):
    heap = []
    dist = [sys.maxsize for _ in range(N + 1)]  # dist[i] : 시작점에서 i node까지의 최단거리(최소비용)

    hq.heappush(heap, [0, start])
    dist[start] = 0

    while heap:
        cur_cost, cur_node = hq.heappop(heap)

        if cur_node == end:  # 목적지에 도달했다면 최소비용을 반환해준다.
            return dist[cur_node]

        for next_node, next_cost in city[cur_node]:
            if cur_cost + next_cost < dist[next_node]:  # 최소비용 갱신
                dist[next_node] = cur_cost + next_cost
                hq.heappush(heap, [dist[next_node], next_node])


answer = dijkstra(start)
print(answer)
