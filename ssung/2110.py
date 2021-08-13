"""

공유기 사이의 최소 거리를 이분탐색으로 찾는다.

탐색마다 설치할 수 있는 공유기 대수와 '가장 인접한 공유기 사이의 거리'를 계산
설치 가능한 공유기가 C 이상일 때 '가장 인접한 공유기 사이의 거리'를 업데이트 해준다.

"""
import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip("\n").split(" "))
wifi = [int(input().rstrip("\n")) for _ in range(N)]
wifi = sorted(wifi)


# 공유기 설치 대수, 가장 인접한 공유기 사이의 거리 계산
def calc(distance):
    prev = wifi[0]
    cnt = 1
    dist = wifi[-1]
    for point in wifi:
        if prev == point:
            continue

        if point - prev >= distance:
            cnt += 1
            dist = point - prev if point - prev < dist else dist
            prev = point

    return cnt, dist


answer = 0
left = 1
right = wifi[-1]
while left <= right:
    mid = (left + right) // 2
    cnt, dist = calc(mid)

    if cnt < C:  # C보다 적게 설치되었다면 공유기 사이의 거리를 줄여야 한다.
        right = mid - 1
    else:  # C보다 같거나 많에 설치되었다면 공유기 사이의 거리를 늘려본다.
        left = mid + 1
        answer = dist if answer < dist else dist

print(answer)
