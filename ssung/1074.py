import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, r, c = map(int, input().rstrip("\n").split(" "))

global cnt
cnt = 0


def dnc(x, y, size):
    global cnt

    if (y == r) and (x == c): # 방문 위치를 찾았으면 방문 순서를 출력 후 종료한다.
        print(cnt)
        exit(0)

    # 1 2
    # 3 4
    # 위와 같은 모양으로 분할정복 (현재 사분면(?)과 같은 위치에 있을 경우)
    if (y <= r) and (r < y + size) and (x <= c) and (c < x + size):
        nsize = size // 2
        dnc(x, y, nsize)  # 1
        dnc(x + nsize, y, nsize)  # 2
        dnc(x, y + nsize, nsize)  # 3
        dnc(x + nsize, y + nsize, nsize)  # 4

    # 위치가 다르면 탐색할 필요가 없다. (현재 사분면의 크기만큼 더해줌)
    else:
        cnt += size * size
        return


dnc(0, 0, 2 ** N)
