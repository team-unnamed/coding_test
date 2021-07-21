# 토마토
# MxN 의 행렬에 익은 토마토와 익지 않은 토마토 정보
# 하루가 경과할때 '익은' 토마토 주변의 토마토는 익는다.
# BFS 방법. 주변의 익은 토마토를 기준으로 day+=1
# queue 형식으로 접근하자. 익었으면 queue에 넣고 더이상 queue에 데이터가 없을시 멈춤
# 모든 토마토가 익었을때의 day을 return

from collections import deque
import sys
input = sys.stdin.readline

M,N = list(map(int,input().split()))
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

x = [0,0,-1,1] # 상 하 좌 우
y = [1,-1,0,0] # 상 하 좌 우


def bfs():
    while queue:
        idx_y,idx_x = queue.popleft()
        for i in range(4):
            dx,dy = idx_x+x[i], idx_y+y[i]
            if (-1< dx <M) and (-1< dy <N):
                if matrix[dy][dx] == 0 :
                    matrix[dy][dx] = matrix[idx_y][idx_x]+1
                    queue.append((dy,dx))

if __name__ == "__main__":
    queue = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue.append((i,j))
    bfs()
    res = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                res = -1
                break
            if res < matrix[i][j]:
                res = matrix[i][j]-1
        if res == -1:
            break
    print(res)
                