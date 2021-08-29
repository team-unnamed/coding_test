import sys
import heapq

def calculate(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**(0.5)

start = list(map(float, input().split()))
destination = list(map(float, input().split()))

n = int(input())

graph = [[] for _ in range(n+2)]
location = [start]

for i in range(1, n+1):
    x, y = map(float, input().split())
    location.append([x, y])
    graph[0].append([i, calculate(start[0], start[1], x, y)/5])

location.append(destination)
graph[0].append([n+1, calculate(start[0], start[1], destination[0], destination[1])/5])

for i in range(1, n+1):
    [x, y] = location[i]

    for j in range(n+2):
        [xx, yy] = location[j]

        if i!=j:
            graph[i].append([j, 2+abs(calculate(x,y,xx,yy)-50)/5])

def Dijkstra(s):
    costs=[sys.maxsize for _ in range(n+2)]
    costs[s]=0
    queue = []
    heapq.heappush(queue, [0, 0])

    while queue:
        current_cost, current_location = heapq.heappop(queue)

        for l, c in graph[current_location]:
            if c+current_cost<costs[l]:
                costs[l] = c+current_cost
                heapq.heappush(queue, [costs[l], l])

    print(costs[n+1])

Dijkstra(0)