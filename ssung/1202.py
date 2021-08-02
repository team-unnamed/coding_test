"""

보석, 가방의 무게 순으로 오름차순 정렬.
현재 가방에 넣을 수 있는 보석을 heap에 넣고 가격을 기준으로 최대 힙 구성.
가방에 보석 하나만 담을 수 있으므로 heap에서 보석을 하나 씩 빼서 최종 가격을 구해준다.

"""
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().rstrip("\n").split(" "))
jewel = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
bags = [int(input().rstrip("\n")) for _ in range(K)]

jewel = sorted(jewel)
bags = sorted(bags)

cost = 0
heap = []
for weight in bags:
    while (jewel) and (jewel[0][0] <= weight):  # 현재 가방에 넣을 수 있는 보석을 모두 heap에 넣음
        heapq.heappush(heap, -jewel[0][1])  # 보석의 가격이 큰 순으로 정렬(최대 힙)
        heapq.heappop(jewel)

    if heap:
        cost += heapq.heappop(heap)
    elif not jewel:  # 남은 보석이 없으면 종료한다.
        break

print(-cost)
