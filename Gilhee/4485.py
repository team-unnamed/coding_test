import sys
import heapq

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def Dijkstra(graph,x,y,n):
    costs = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    costs[y][x]=graph[y][x]
    queue = []
    heapq.heappush(queue, [costs[y][x], x, y])

    while queue:
        current_cost, cx, cy = heapq.heappop(queue)

        if costs[cy][cx]<current_cost:
            continue

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<n and 0<=ny<n and costs[ny][nx]>current_cost+graph[ny][nx] :
                costs[ny][nx] = current_cost+graph[ny][nx]
                heapq.heappush(queue, [costs[ny][nx], nx, ny])

    return costs[-1][-1]

counting = 1
while True:
    n = int(input())

    if n==0:
        break

    graph = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

    answer = Dijkstra(graph, 0,0, n)

    print(f'Problem {counting}: {answer}')

    counting +=1
