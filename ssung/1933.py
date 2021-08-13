"""

예제를 보면 3번째 스카이라인의 끝나는 지점이 9이고 해당 지점의 높이가 0인 것으로 보아
끝나는 지점은 스카이라인에 포함되지 않는 것을 알 수 있다.

처음엔 스카이라인의 시작 좌표 ~ 끝 좌표를 탐색하려 함.
좌표의 범위가 10억이라 시간초과가 발생할 것으로 예상하고 좌표마다 탐색하는 방법을 생각하고 아래와 같이 해결

1. 시작, 끝 점과 상관 없이 모두 rank라는 min_heap에 저장.
2. rank에서 좌표를 하나씩 pop(이하 현재 좌표)하면서 현재 좌표보다 먼저(혹은 동시에) 시작하는 스카이라인을 max_heap에 모두 저장
   => 높이를 기준으로 내림차순 정렬하기 위해 (-높이, 끝 좌표) 형식으로 push

3. 현재 좌표보다 먼저(혹은 동시에) 끝나는 스카이라인을 max_heap에서 모두 pop
   => 스카이라인이 끝나는 좌표에서는 높이가 0 이므로 pop 해주어야 함.

4. max_heap에 남아 있는 스카이라인이 있다면 현재 좌표에서의 최고 높이는 -max_heap[0][0]
   => 이 높이가 max_height와 다르다면 높이가 바뀐 것이므로 출력

"""
import sys
import heapq as hq

input = sys.stdin.readline

N = int(input().rstrip("\n"))

building = []  # 스카이라인 정보 저장
rank = []  # 시작 좌표, 끝 좌표 모두 저장 (오름차순)

for _ in range(N):
    left, height, right = map(int, input().rstrip("\n").split(" "))
    building.append([left, height, right])
    hq.heappush(rank, left)
    hq.heappush(rank, right)

building = sorted(building, key=lambda x: x[0])

idx = 0
max_height = 0  # 현재 위치에서의 최고 높이
max_heap = []  # 스카이라인 정보를 높이를 기준으로 내림차순 정렬하여 저장 (-높이, 끝나는 x좌표)
while rank:
    x = hq.heappop(rank)
    while (idx < N) and (building[idx][0] <= x):  # 현재 위치보다 먼저 시작되는 스카이라인 저장 (-높이, 끝나는 x좌표)
        hq.heappush(max_heap, (-building[idx][1], building[idx][2]))
        idx += 1

    new_height = 0
    while (max_heap) and (max_heap[0][1] <= x):  # 현재 위치보다 먼저 끝나는 스카이라인을 모두 pop
        hq.heappop(max_heap)

    if max_heap:  # 스카이라인이 존재한다면 높이를 갱신해주고
        new_height = -max_heap[0][0]

    if max_height != new_height:  # 현재 위치에서의 최대 높이가 달라졌다면 출력해준다.
        print(x, new_height, end=" ")
        max_height = new_height
