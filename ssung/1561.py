"""

3079 입국심사 문제랑 비슷한 느낌의 문제.
시간을 이분탐색으로 찾아가면서 해당 시간에 몇명까지 놀이기구에 태울 수 있는지 찾는다.

1. t초에 N명보다 많으면서 가장 근접하게 태울 수 있는 t를 이분탐색으로 구한다.
2. t-1초에 아이들을 몇명까지 태울 수 있는지 구한다.
3. 남은 아이들을 t초에 비어있는 놀이기구에 차례대로 탑승시키면 N번째 아이가 몇 번째 놀이기구에 타는지 알 수 있다.

"""
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
play = list(map(int, input().rstrip("\n").split(" ")))

if N <= M:  # 놀이기구가 더 많다면 모든 아이는 놀이기구에 차례대로 탑승가능.
    print(N)
    exit(0)


def binary_search():
    left = 1
    right = max(play) * N
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for p in play:  # 0초에는 모든 놀이기구가 비었으므로 +1씩 해주어 M을 더해준다.
            people += (mid // p) + 1

        if people < N:
            left = mid + 1
        else:
            right = mid - 1

    return left


def rest(time):
    people = 0
    for p in play:
        people += (time // p) + 1

    return N - people


time = binary_search()  # 모든 아이들이 탑승했을 때의 시간
rest_people = rest(time - 1)  # (time - 1)초에 최대 몇명까지 탑승가능한가 (time초에 탑승하지 못한 아이들의 수)

for i, p in enumerate(play):
    if time % p == 0:  # 놀이기구가 비었다면 한 명씩 태운다.
        rest_people -= 1
        if rest_people == 0:  # 마지막 아이가 타게 되는 놀이기구의 번호
            print(i + 1)
            exit(0)
