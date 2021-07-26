"""

방문 순서가 주어지므로 방문 순서에 맞게 트리를 재정렬해준다. 그 후, bfs로 재정렬 된 트리를 순회한다. 
순회 결과와 주어진 방문 순서가 같으면 올바른 순서이고 다르다면 틀린 순서이다.

"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip("\n"))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().rstrip("\n").split(" "))
    graph[u].append(v)
    graph[v].append(u)

target = list(map(int, input().rstrip("\n").split(" ")))
order = [-1 for _ in range(len(target) + 1)]

for i, num in enumerate(target):  # 우선순위 설정
    order[num] = i

for i in range(1, N + 1):  # 우선순위에 맞게 다시 정렬해준다.
    graph[i].sort(key=lambda x: order[x])


def bfs(start):
    ret = [start]  # 방문한 정점의 순서를 저장한다.
    if target[0] != start:
        return 0

    isVisited = [False for _ in range(N + 1)]

    queue = deque()
    queue.append(start)

    isVisited[start] = True
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not isVisited[next_node]:
                isVisited[next_node] = True
                queue.append(next_node)
                ret.append(next_node)

    return ret


ret = bfs(1)
if ret == target:  # 재정렬 된 트리를 순회한 순서와 주어진 방문 순서가 같다면 올바른 순회
    print(1)
else:
    print(0)
