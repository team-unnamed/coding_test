"""

특이한 이분탐색(?) 문제. 보통 구하려는 값을 이분탐색으로 범위를 좁혀가면서 구했는데
해당 문제는 최소, 최대 범위를 투 포인터 방식으로 풀었던 문제이다.

최소(left), 최대(right)의 범위 제한은 (0 ~ 배열의 원소의 최댓값)으로 두고 투 포인터 방식을 사용.

left <= x <= right를 만족하는 x에 대해서 bfs로 탐색하여 목적지에 도달할 수 있는지 체크한다.
즉, 방문해야 할 원소들의 최소, 최대값의 범위를 정해줌으로써 출력 결과인 (최대-최소)를 고정시킬 수 있다.

(line 57) 만약 목적지에 도달했더라도 해당하는 left, right 값이 실제 배열의 최소, 최대값이 아닐 수 있으므로 범위를 좁혀가면서 계속 탐색한다.
 
(line 60) 목적지에 도달하지 못했다면 현재 범위보다 큰 원소가 존재한다는 뜻이므로 right += 1 해주어서 범위를 확장시켜준다.


"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]

dx = [0, 0, -1, 1]  # x좌표 이동
dy = [-1, 1, 0, 0]  # y좌표 이동


def bfs(x, y, min_num, max_num):
    if (arr[y][x] < min_num) or (max_num < arr[y][x]):  # 시작 지점이 범위를 벗어나면 탐색 불가능
        return False

    isVisited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([x, y])
    isVisited[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()

        if (cur_x == n - 1) and (cur_y == n - 1):  # 목적지에 도달하면 종료
            return True

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0 <= nx) and (nx < n) and (0 <= ny) and (ny < n) and (not isVisited[ny][nx]) and (min_num <= arr[ny][nx]) and (arr[ny][nx] <= max_num):
                isVisited[ny][nx] = True
                q.append([nx, ny])

    return False


left = right = 0
limit = max(map(max, arr))  # 배열의 원소의 최댓값 (left, right는 이 이상 커질 수 없다)
answer = sys.maxsize
while (left <= limit) and (right <= limit):
    if bfs(0, 0, left, right):  # 목적지에 도착했다면 (최대-최소)를 줄여본다.
        answer = right - left if right - left < answer else answer
        left += 1
    else:  # 목적지에 도달하지 못했다면 범위를 늘려주어야 한다.
        right += 1

print(answer)
