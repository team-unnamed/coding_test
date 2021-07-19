"""

그래프로 표현하면 cycle이 생기기 때문에 어느 위치에서 시작하더라도 비용이 같다는 것을 생각해야 한다.
각 섬에서 출발했을 때의 비용을 모두 구하면 시간초과 발생

"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input().rstrip("\n"))
weight = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
check = [False for _ in range(N)]

global result
result = sys.maxsize


def cycle(cur, sum, cnt):
    global result
    if (check[0]) and (cnt != N): # 모든 섬을 방문하지 않은 경우는 제외한다.
        return

    if (cur == 0) and (cnt == N): # 모든 섬을 방문한 경우 result값을 업데이트 해준다.
        result = sum if sum < result else result
        return

    for i in range(N):
        if (weight[cur][i] != 0) and (not check[i]): # 갈 수 있는 섬을 모두 방문해본다.
            check[i] = True
            cycle(i, sum + weight[cur][i], cnt + 1)
            check[i] = False


cycle(0, 0, 0) # 순회할 수 있기 떄문에 시작점을 어떤 위치로 잡더라도 비용이 똑같다.
print(result)
