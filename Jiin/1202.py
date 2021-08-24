"""
가방이랑 보석 둘 다 무게 오름차순으로 정렬
가방에 들어갈 수 있는 보석 후보(최대 힙으로 만들어)를 추린다 < 이 때 한번 본 보석은 보석 목록에서 빼 버려 어차피 힙에 들어있을 테니까
가방 하나에 대해 보석 다 봤으면 후보 중에 가치가 가장 높은 보석을 골라 가방에 넣기
모든 가방에 반복
근데 이 때 보석 후보를 초기화하면 안 됨! 가방 무게 오름차순으로 정렬했으니까 이전 가방에 들어가는 보석이었으면 다음 가방에도 들어가거든
"""

import sys, heapq

N, K = map(int, sys.stdin.readline().split())

gems = []
for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gems.append((M, V))
gems = sorted(gems)

bags = []
for i in range(K):
    bags.append(int(sys.stdin.readline()))
bags = sorted(bags)

stolen = 0
heap = []
for bag in bags:
    while gems and bag >= gems[0][0]:
        m, v = heapq.heappop(gems)
        heapq.heappush(heap, -v)  # 최대 힙처럼 동작하게

    if heap:  # 보석을 못 훔치는 경우도 있음
        stolen += heapq.heappop(heap)
    elif not gems:
        break

print(-stolen)

