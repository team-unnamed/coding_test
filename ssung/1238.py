"""

각 학생마다 (X로 가는 시간 + 돌아오는 시간)을 구해서 그 최댓값을 구하면 된다.

"""
import sys
import heapq as hq

input = sys.stdin.readline


# 다익스트라 알고리즘
def dijkstra(start, end, road):
    heap = []
    dist = [sys.maxsize for _ in range(len(road))]
    hq.heappush(heap, [0, start])
    dist[start] = 0

    while heap:
        cur_cost, cur_node = hq.heappop(heap)

        if cur_node == end:  # 목적지에 도착했다면 이동 시간을 반환해준다.
            return dist[cur_node]

        for next_node, next_cost in road[cur_node]:
            if cur_cost + next_cost < dist[next_node]:
                dist[next_node] = cur_cost + next_cost
                hq.heappush(heap, [dist[next_node], next_node])


def solution():
    answer = 0
    
    N, M, X = map(int, input().rstrip("\n").split(" "))
    road = [[] for _ in range(N + 1)]

    for _ in range(M):  # 단방향 도로이므로 u -> v 경로만 업데이트
        u, v, w = map(int, input().rstrip("\n").split(" "))
        road[u].append([v, w])

    # 1번 학생부터 N번 학생까지 왕복 시간을 구한다.
    for start in range(1, N + 1):
        go = dijkstra(start, X, road)  # 목적지(X)로 이동할 때의 최단시간
        back = dijkstra(X, start, road)  # 집으로 돌아올 떄의 최단시간
        answer = go + back if answer < go + back else answer

    print(answer)


if __name__ == "__main__":
    solution()
