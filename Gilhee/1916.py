import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().rstrip('\n').split())
    graph[s].append([e,c])

x, y = map(int, input().rstrip('\n').split())

def Dijkstra(graph, start):
    costs = [sys.maxsize for _ in range(len(graph))]
    costs[start]=0
    queue =[]
    heapq.heappush(queue, [0, start])

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if costs[current_node]<current_cost:
            continue

        for n, c in graph[current_node]:
            if costs[n]>current_cost+c:
                costs[n] = current_cost+c
                heapq.heappush(queue, [costs[n], n])

    return costs

costs = Dijkstra(graph, x)

print(costs[y])