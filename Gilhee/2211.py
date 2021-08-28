import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip('\n').split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distances = [sys.maxsize for _ in range(n+1)]
distances[1]=0
save = [[] for _ in range(n+1)]
queue = []
heapq.heappush(queue,[0, 1, []])

while queue:
    current_distance, current_node, current_routes = heapq.heappop(queue)

    if current_distance>distances[current_node]:
        continue

    for node, cost in graph[current_node]:
        temp = [c for c in current_routes]
        if current_distance+cost < distances[node]:
            distances[node]= current_distance+cost
            if current_node<node:
                temp.append([current_node, node])
            else:
                temp.append([node, current_node])

            save[node] = temp
            heapq.heappush(queue, [distances[node], node, save[node]])

answer = []
for s in save:
    for g in s:
        if not g in answer:
            answer.append(g)

print(len(answer))

for a in answer:
    [x, y] = a
    print(f'{x} {y}')

