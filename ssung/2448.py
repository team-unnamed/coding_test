import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))

arr = [[" " for _ in range(N * 2)] for _ in range(N)]

# 별 그리기 함수
def star(y, x, size):
    if size == 0:
        return

    #   *
    #  * *
    # *****
    # size가 3의 배수이면 별을 저장해준다. (가장 작은 별이라고 생각)
    if size % 3 == 0:
        arr[y][x] = "*"

        arr[y + 1][x - 1] = "*"
        arr[y + 1][x + 1] = "*"
        
        arr[y + 2][x - 2] = "*"
        arr[y + 2][x - 1] = "*"
        arr[y + 2][x] = "*"
        arr[y + 2][x + 1] = "*"
        arr[y + 2][x + 2] = "*"

    next_size = size // 2

    # 큰 별을 만들기 위한 재귀함수. 가장 작은 별을 현재 위치 + 왼쪽 아래, 오른쪽 아래에 배치한다.
    star(y, x, next_size)
    star(y + next_size, x - next_size, next_size)
    star(y + next_size, x + next_size, next_size)


star(0, N - 1, N)

for i in range(N):
    print("".join(arr[i]))
