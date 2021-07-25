# 4963 섬의 갯수
# 주어진 데이터에서, 점의 갯수 구하기.
# DFS 방법으로 해당 시작점에서 연결된 곳 까지 탐색


import sys
input = sys.stdin.readline




def dfs(x,y):
    if MAP[y][x]:
        MAP[y][x] = 0
        for i in range(len(dx)):
            if (0<=x+dx[i]<W) and (0<=y+dy[i]<H):
                dfs(x+dx[i], y+dy[i])
    else:
        return None

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

while True:
    # w,h 받기
    W,H = list(map(int, input().split()))
    if not(W) and not(H):
        break
    # map 저장
    MAP = []
    for _ in range(H):
        MAP.append(list(map(int, input().split()))) 

    res = 0
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == 1:
                res += 1
                dfs(j,i)

    print(res)      
    
