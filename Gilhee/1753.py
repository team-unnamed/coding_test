import sys
import heapq
input = sys.stdin.readline

V, e = map(int, input().rstrip('\n').split())

start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(e):
    u, v, w = map(int, input().rstrip('\n').split())
    graph[u].append([v, w])

def Dijkstra(graph, start):
    distances = [sys.maxsize for _ in range(V+1)]
    distances[start]=0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for n, d in graph[current_node]:
            distance = d+current_distance

            if distance< distances[n] :
                distances[n]=distance
                heapq.heappush(queue, [distance, n])

    for i in range(1, V+1):
        if distances[i] == sys.maxsize:
            print('INF')
        else:
            print(distances[i])

Dijkstra(graph, start)
