import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().rstrip('\n').split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip('\n').split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distances = [[sys.maxsize]*(k+1) for _ in range(n+1)]

for i in range(1,k+1):
    distances[1][i]=0

queue = []
counting = 0
heapq.heappush(queue, [0, 1, counting])

while queue:
    current_distance, current_node, c = heapq.heappop(queue)

    if current_distance>distances[current_node][c]:
        continue

    for node, cost in graph[current_node]:

        if current_distance+cost <distances[node][c]:
            distances[node][c]=current_distance+cost
            heapq.heappush(queue, [distances[node][c], node, c])

        if  c<k and distances[node][c+1]>current_distance:
            distances[node][c+1] = current_distance
            heapq.heappush(queue, [distances[node][c+1], node, c+1])

print(min(distances[n]))