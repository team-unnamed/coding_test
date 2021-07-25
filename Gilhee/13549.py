from collections import deque

def bfs(x):
    q = deque([x])	
    time = [-1] * MAX	
    time[x] = 0

    while q:
        cx = q.popleft()
        if cx == k:
            return time[cx]

        for i in range(3):
            if i == 0:
                nx = cx - 1
            elif i == 1:
                nx = cx + 1
            else:
                nx = cx * 2

            if not 0 <= nx < MAX:	
                continue
            if time[nx] != -1 and time[nx] <= time[cx]:
                continue

            if i < 2:	
                q.append(nx)
                time[nx] = time[cx] + 1
            else:	
                q.appendleft(nx)
                time[nx] = time[cx]


n, k = map(int, input().split())
MAX = 100001
print(bfs(n))