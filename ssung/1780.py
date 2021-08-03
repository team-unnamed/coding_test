import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input().rstrip("\n"))
paper = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
answer = [0, 0, 0]  # 종이의 개수 저장 (-1, 0, 1)


def dnc(x, y, size):
    flag = False
    cat = paper[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != cat:  # 다른 수가 있다면 종이를 다시 잘라야 한다.
                flag = True
                break
        if flag:
            break

    if not flag:  # 종이가 모두 같은 수이면 개수를 +1 하고 다음 종이로 넘어감
        answer[cat + 1] += 1
        return

    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 위와 같은 모양으로 분할정복
    nsize = size // 3

    dnc(x, y, nsize)  # 1
    dnc(x + nsize, y, nsize)  # 2
    dnc(x + 2 * nsize, y, nsize)  # 3

    dnc(x, y + nsize, nsize)  # 4
    dnc(x + nsize, y + nsize, nsize)  # 5
    dnc(x + 2 * nsize, y + nsize, nsize)  # 6

    dnc(x, y + 2 * nsize, nsize)  # 7
    dnc(x + nsize, y + 2 * nsize, nsize)  # 8
    dnc(x + 2 * nsize, y + 2 * nsize, nsize)  # 9


dnc(0, 0, N)

for cnt in answer:
    print(cnt)
