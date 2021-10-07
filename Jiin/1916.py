"""
다익스트라 하는 법

1. 그래프 구성하기 (인접 리스트에 비용도 같이 넣어)
2. 최단경로 리스트에서 시작점은 0으로, 나머지 노드는 sys.maxsize(무한대)로 초기화
3. 시작점에서 인접한 노드를 방문하면서 방문 체크
4. 방문 중인 노드에 인접한 노드들의 거리 최소값을 갱신
5. 아직 방문 안 한 노드 중에서 거리가 최소인 노드를 방문해서 3부터 반복
   이 때 최소값을 빠르게 찾기 위해 min heap을 사용하며 노드 방문 체크는 자동으로 된다
   (기록된 거리가 현재 노드에서 가는 것보다 더 클 때만 힙에 넣는데, 옛날에 방문했던 노드는 현재 노드에서 가는 것보다 거리가 작거나 같아서)
   
"""

import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]


# 그래프 구성
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])  # 양방향 그래프가 아니었네...


# 출발/도착점
start, end = map(int, input().split())
INF = sys.maxsize
dist = [INF for _ in range(N+1)]  # 최단경로를 저장할 리스트
min_cost = INF


dist[start] = 0  # 시작점은 거리가 0
heap = []
heapq.heappush(heap, [0, start])  # 힙에 넣을 때 거리, 노드 순으로 넣어야 최소 힙이 목적에 맞게 작동함

while heap:
    cost, node = heapq.heappop(heap)  # pop하면 방문 완료된 것

    if node == end:
        min_cost = cost
        break
        
    neighbor = graph[node]
    for node_next, c in neighbor:
        cost_next = cost + c  # 현재 노드까지 오는 최단거리 (cost에 들어 있음) + 현재 노드에 인접한 노드까지 가는 거리
        if dist[node_next] > cost_next:  # 현재 노드를 거쳐서 방문하는 게 더 빠를 때에만 갱신
            dist[node_next] = cost_next
            heapq.heappush(heap, [cost_next, node_next])  # 이렇게 하면 방문체크를 안해도 자동으로 된다
        
print(cost)
