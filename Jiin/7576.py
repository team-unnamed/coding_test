import sys
from collections import deque

def bfs(q):
    global storage, days

    if not q: # 익은 토마토가 없어도 여기 들어올 수가 있다...!
        return -1

    front = q[0]
    row = front[0]
    col = front[1]
    days[row][col] = 0
    maxd = 0  # 여기까지 왔다는 건 익은 토마토가 하나 이상 있다는 것

    while q:
        front = q[0]
        row = front[0]
        col = front[1]
        q.popleft()

        for i in range(4):
            nextr = row + dr[i]
            nextc = col + dc[i]
            if nextr >= R or nextc >= C or nextr < 0 or nextc < 0: continue

            if storage[nextr][nextc] == 0:  # 안익은 토마토가 더 없으면 여기는 스킵됨
                days[nextr][nextc] = days[row][col] + 1
                if maxd < days[nextr][nextc]:
                    maxd = days[nextr][nextc]

                storage[nextr][nextc] = 1
                q.append((nextr, nextc))

    return maxd



dc = (-1, 0, +1, 0)
dr = (0, -1, 0, 1)

C, R = map(int, sys.stdin.readline().split())
storage = [[] for _ in range(R)]
days = [[0] * C for _ in range(R)]  # -1이면 아직 방문하지 않은 것
q = deque()
maxday = 0

tomato = [0, 0, 0]  # 순서대로 안익음 / 익음 / 토마토 없음
for i in range(R):
    storage[i] = list(map(int, sys.stdin.readline().split()))
    for tomat in storage[i]:
        tomato[tomat] += 1  # 토마토 저장

for i in range(R):
    for j in range(C):
        if storage[i][j] == 1 and days[i][j] == 0:
            q.append((i, j)) #익은 토마토를 큐에 넣기


maxday = bfs(q)

newtomato = [0, 0, 0]
for line in storage:  # 토마토 저장
    for tomat in line:
        newtomato[tomat] += 1  # 토마토 상태(0,1,-1)에 따라서 newtomato에 저장

if newtomato[0] == 0:  # 토마토가 무사히 익었다면
    print(maxday)

elif tomato[0] == 0 and tomato[1] != 0:  # 처음부터 다 익어있었다면
    print(0)

elif tomato[1] == 0 or newtomato[0] != 0:  # 익은 토마토가 한 개도 없었거나 안익은 토마토가 남아있다면
    print(-1)

 
