import sys
import heapq

input = sys.stdin.readline


def dijkstra(start, node):
    dist = [sys.maxsize for _ in range(len(node))]  # 시작 노드로부터의 거리를 나타내는 list
    min_heap = []  # 최단 거리(비용이 적음)를 고려하기 위한 min heap
    heapq.heappush(min_heap, [0, start])
    dist[start] = 0  # 시작 노드는 거리가 0

    while min_heap:
        cur_cost, cur_node = heapq.heappop(min_heap)
        for next_node, next_cost in node[cur_node]:  # 현재 노드와 연결 된 노드를 탐색한다.
            if dist[next_node] > cur_cost + next_cost:  # 다음 노드까지의 비용이 기존보다 적으면 update.
                dist[next_node] = cur_cost + next_cost
                heapq.heappush(min_heap, [dist[next_node], next_node])

    return dist


def solution():
    V, E = map(int, input().rstrip("\n").split(" "))
    K = int(input().rstrip("\n"))

    node = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().rstrip("\n").split(" "))
        node[u].append([v, w])

    dist = dijkstra(K, node)

    for i in range(1, V + 1):
        print("INF" if dist[i] == sys.maxsize else dist[i])


if __name__ == "__main__":
    solution()