"""

물품들의 중량의 최댓값을 이분탐색으로 찾는다.

탐색마다 임의의 무게 m으로 시작점에서 목적지까지 이동할 수 있는지 bfs를 통해 판별하면 된다.
목적지에 도달할 수 없다면 중량을 낮추고 도달할 수 있었다면 중량을 높여가며 최댓값을 찾는다

"""
import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
bridge = [[] for _ in range(N + 1)]

left = 1  # 중량의 최솟값은 1
right = 0  # 중량의 최댓값은 모든 섬에서 가장 높은 중량제한
for _ in range(M):
    A, B, C = map(int, input().rstrip("\n").split(" "))
    bridge[A].append([B, C])
    bridge[B].append([A, C])
    right = C if right < C else right

start, end = map(int, input().rstrip("\n").split(" "))  # 시작점, 도착점


def bfs(start, end, weight):
    isVisited = [False for _ in range(N + 1)]
    q = deque()
    q.append(start)
    isVisited[start] = True

    while q:
        cur_node = q.popleft()

        if cur_node == end:  # 목적지에 도달했다면 종료한다
            return True

        for next_node, cost in bridge[cur_node]:
            if (not isVisited[next_node]) and (weight <= cost):  # 방문한 적이 없고 중량제한을 초과하지 않는다면 이동
                q.append(next_node)
                isVisited[next_node] = True

    return False


answer = 0
while left <= right:
    mid = (left + right) // 2

    if bfs(start, end, mid):  # 목적지에 도착했다면 중량의 최댓값을 갱신. 중량을 높여본다
        answer = mid if answer < mid else answer
        left = mid + 1
    else:  # 목적지에 도착할 수 없었다면 중량을 낮춤
        right = mid - 1

print(answer)
