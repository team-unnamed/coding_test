import sys
input = sys.stdin.readline

n = int(input())

Map = []

for _ in range(n):
    Map.append(list(map(int, input().rstrip('\n').split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(min_num, max_num):
    if Map[0][0]<min_num or Map[0][0]>max_num:
        return False
    visit = [[0 for _ in range(n)] for _ in range(n)]

    queue = [(0,0)]
    visit[0][0]=1

    while queue:
        x, y= queue.pop(0)
        if x==n-1 and y==n-1:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and Map[ny][nx]>=min_num and Map[ny][nx]<=max_num and visit[ny][nx]==0:
                queue.append((nx, ny))
                visit[ny][nx]=1

    return False

min_num = max_num = 0
limit = max(map(max, Map))
answer = max(map(max, Map))

while min_num<=limit and max_num<=limit:

    if bfs(min_num, max_num):
        answer = answer if (max_num-min_num)>answer else (max_num-min_num)
        min_num += 1
    else:
        max_num += 1

print(answer)