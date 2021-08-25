"""
최단 경로 알고리즘
Dijkstra!! 

sol 1
v by v 행렬 만들어서 (map) 해당 정점에서 시작하기

"""

### SOL 1
import sys
input = sys.stdin.readline

INF = 10000000

v,e = map(int, input().split())
START = int(input())-1
MAP = [[ INF for _ in range(v) ] for _ in range(v)]
for _ in range(e):
    u,d,w = map(lambda x : int(x)-1, input().split())
    MAP[u][d] = w + 1
visit = [False for _ in range(v)]

dist = MAP[START]
visit[START] = True

def get_smallest_index():
    global v,dist,visit
    m = INF
    index = 0
    for i in range(v):
        if (dist[i] < m) and not(visit[i]):
            m = dist[i]
            index = i
    return index

for _ in range(v):
    idx = get_smallest_index()
    visit[idx] = True
    for j in range(v):
        d = dist[idx] + MAP[idx][j]
        if not(visit[j]) and (d < dist[j]):
            dist[j] = d

# 값 출력
for i in range(v):
    if i == START:
        print(0)
    elif dist[i] == INF:
        print("INF")
    else:
        print(dist[i])


