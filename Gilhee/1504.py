import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().rstrip('\n').split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().rstrip('\n').split())

    graph[a].append([b,c])
    graph[b].append([a,c])

v, w = map(int, input().rstrip('\n').split())

def Dijkstra(graph, start):
    distances = [sys.maxsize for _ in range(n+1)]
    distances[start]=0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance>distances[current_node]:
            continue

        for node, cost in graph[current_node]:
            if current_distance+cost <distances[node]:
                distances[node] = current_distance+cost 
                heapq.heappush(queue, [distances[node], node])

    return distances

start_route = Dijkstra(graph, 1)
v_route = Dijkstra(graph, v)
w_route = Dijkstra(graph, w)

case1 = start_route[v]+v_route[w]+w_route[n]
case2 = start_route[w]+w_route[v]+v_route[n]

if min(case1, case2)>=sys.maxsize:
    print(-1)
else:
    print(min(case1, case2))

