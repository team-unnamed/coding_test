import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().rstrip('\n').split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().rstrip('\n').split())
    graph[s].append([e,t])

def Dijkstra(graph, start):
    distances = [sys.maxsize for _ in range(n+1)]
    distances[start]=0
    queue =[]
    heapq.heappush(queue,[0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for node, cost in graph[current_node]:
            if current_distance+cost<distances[node]:
                distances[node]=current_distance+cost
                heapq.heappush(queue, [distances[node], node])

    return distances

back_distances = Dijkstra(graph, x)
max_time =0

for i in range(1, n+1):
    go_distances = Dijkstra(graph, i)
    if go_distances[x]+back_distances[i]>max_time:
        max_time=go_distances[x]+back_distances[i]

print(max_time)