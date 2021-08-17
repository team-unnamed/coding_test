"""
사분면

input
d num / d : 사분면 조각의 번호의 자릿수 (분할 하는 수) num : 해당 사분면의 번호
x y / x : x 축방향으로 이동 경로 (+r, -l) y 축방향 이동경로 (+u, -d)

output
num 에서 x,y 만큼 이동했을 시 사분면의 번호

num 의 좌표를 알아내고, x,y 만큼 이동했을시의 좌표도 구하기

1. 첫번째 input 관련하여 좌표 획득. 
2. 해당 좌표만큼 이동
3. 다시 해당 좌표만큼 탐색.( 분할 정복 활용 )
""" 

import sys
input = sys.stdin.readline
def int_str(arr):
    return int(arr[0]), str(arr[1])
N, spot = int_str(input().split())
dx, dy = map(int, input().split())

def get_spot(spot):
    x, y = 1,1
    quadrant = [[1,0],[0,0],[0,1],[1,1]]
    for i,s in enumerate(spot):
        mx, my = quadrant[int(s)-1]
        level = N - i - 1
        x += mx*(2**level)
        y += my*(2**level)
    return x,y


def divide(spot,length):
    # 가장 크게 사분면 분할 (해당 좌표에 맞는 위치 확득, 해당 level 만큼 - )
    # 각 좌표에서 표함되어 있다면, 다음으로 진행 그리고 결과 단에다 전달.
    global res
    x,y = spot
    quadrant = [[1,0],[0,0],[0,1],[1,1]]
    for i,q in enumerate(quadrant):
        q_x = q[0]*length//2
        q_y = q[1]*length//2
        if (q_x < x <= q_x + length//2) and (q_y < y <= q_y + length//2):
            res += str(i+1)
            spot = x - q_x, y - q_y
            divide(spot, length//2)



x, y = get_spot(spot)
x += dx
y -= dy

if (0<x<=2**N) and (0<y<=2**N):
    res = ''
    spot = x,y
    divide(spot,2**N)
    print(res) 
else:
    print(-1)
    