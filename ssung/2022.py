"""

빌딩 사이의 거리를 이분탐색으로 찾는다.
탐색마다 빌딩 사이의 거리를 구하고 c와 같다면 프로그램을 종료

코딩보다 수학 능력이 더 중요했던 문제.
식을 정리하고 정리하다 보면 빌딩의 거리가 주어졌을 때 교차지점의 높이를 구할 수 있다.

정수가 아니기 때문에 34, 39 line이 정수로 진행하는 이분탐색과 조금 다름
또한, while문의 조건도 구간 설정을 해주어야 무한루프에 빠지지 않는다

"""
import sys

input = sys.stdin.readline

x, y, c = map(float, input().rstrip("\n").split(" "))


# 교차하는 지점의 높이를 계산
def calc(dist):
    h1 = (x * x - dist * dist) ** 0.5
    h2 = (y * y - dist * dist) ** 0.5
    ret = (h1 * h2) / (h1 + h2)

    return round(ret, 3)


left = 1
right = min(x, y)
while abs(right-left) >= 1e-6:  # 소수점 여섯째 자리까지 주어지므로 구간 설정을 해야 함
    mid = (left + right) / 2
    height = calc(mid)

    if height < c:  # 주어진 높이보다 낮다면 빌딩 사이의 거리를 좁혀야 함
        right = mid
    else:  # 주어진 높이보다 높다면 빌딩 사이의 거리를 멀도록
        left = mid

print(f"{mid:0.3f}")