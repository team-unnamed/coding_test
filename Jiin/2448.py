"""
  *   기본 단위
 * *
*****

각 줄마다 2n개의 문자가 출력되어야 함 (세모 뒤쪽 공백도 포함)
앞쪽 공백과 뒤쪽 공백 처리를 위해서 배열을 쓰는 듯

큰 삼각형(조각내기 전)의 높이랑 (밑변의 가운데 지점 좌표+1)랑 같다! 가운데+1이랑 같은 이유는 0부터 시작하니까
꼭지점 (r,c) 인 삼각형을 조각내면 (이 때 h를 2로 나눈다)
첫 번째 삼각형의 꼭지점은 (r, c)
두 번째 삼각형의 꼭지점은 (r+h, c-h)
세 번재 삼각형의 꼭지점은 (r+h, c+h)

오옷 엄청 큰 배열인 경우에는 for문 일일이 돌면서 출력하기보다 join 써서 각 줄을 string으로 만든 다음 한 줄씩 통으로 출력하는 게 더 빠르다!
"""

import sys
sys.setrecursionlimit(10**8)


def minStar(r, c):
    global arr

    arr[r][c] = '*'
    arr[r+1][c-1] = '*'
    arr[r+1][c+1] = '*'
    for i in range(-2, 3):
        arr[r+2][c+i] = '*'

def dnc(r, c, h):
    # 맨 위쪽 점의 좌표와 삼각형 조각의 높이를 받아서 배열에 별 집어넣기
    global arr

    if h == 3:
        minStar(r, c)
        return

    h //= 2
    dnc(r, c, h)
    dnc(r+h, c-h, h)
    dnc(r+h, c+h, h)



N = int(sys.stdin.readline())

arr = [[' ' for _ in range(N*2)] for __ in range(N)]

dnc(0, N-1, N) # 0부터 시작한다는 걸 잊지 마...

for row in arr:
    print(''.join(row))

