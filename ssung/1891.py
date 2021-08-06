"""

이동시키려는 사분면 조각의 좌표를 먼저 구해준 뒤 이동한 좌표를 dest_x, dest_y에 저장.
사분면의 오른쪽 아래 지점을 기준으로 (ex, ey) 분할정복을 진행.
목표지점 도달 시 사분면의 위치를 출력하고 프로그램 종료.

시간초과 방지를 위해 사분면에 속하지 않는 경우는 고려하지 않음.

"""
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

d, fr = map(int, input().rstrip("\n").split(" "))
dx, dy = map(int, input().rstrip("\n").split(" "))

# 시작 좌표 찾기
fr = list(str(fr))
init_x = init_y = 2 ** d  # 이동시키려는 사분면 조각의 좌표 저장
size = 2 ** (d - 1)
for num in fr:
    if num == "1":
        init_y -= size
    elif num == "2":
        init_x -= size
        init_y -= size
    elif num == "3":
        init_x -= size
    elif num == "4":
        pass

    size //= 2

# 목적지의 좌표
dest_x = init_x + dx
dest_y = init_y - dy


def dnc(sx, sy, ex, ey, size, quad):
    """
    이동시킨 사분면 조각을 찾는다.
    sx, sy, ex, ey를 이용해 사분면의 범위를 구한다.

    Args:
        sx (int): 사분면 조각의 좌상단 x좌표
        sy (int): 사분면 조각의 좌상단 y좌표
        ex (int): 사분면 조각의 우하단 x좌표
        ey (int): 사분면 조각의 우하단 y좌표
        size ([type]): 사분면 조각의 길이
        quad ([type]): 현재의 사분면 체크
    """
    # 목적지에 도착했으면 위치 출력
    if (dest_x == ex) and (dest_y == ey) and (len(quad) == d):
        print(quad)
        exit(0)

    # 해당 사분면에 존재하지 않으면 넘어간다.
    if not ((sx < dest_x) and (dest_x <= ex) and (sy < dest_y) and (dest_y <= ey)):
        return

    dnc(sx + size // 2, sy, ex, ey - size // 2, size // 2, quad + "1")  # 1사분면
    dnc(sx, sy, ex - size // 2, ey - size // 2, size // 2, quad + "2")  # 2사분면
    dnc(sx, sy + size // 2, ex - size // 2, ey, size // 2, quad + "3")  # 3사분면
    dnc(sx + size // 2, sy + size // 2, ex, ey, size // 2, quad + "4")  # 4사분면


dnc(0, 0, 2 ** d, 2 ** d, 2 ** d, "")
print(-1)  # 도달할 수 없으면 -1 출력
