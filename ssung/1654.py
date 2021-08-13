"""

잘라야 할 랜선의 길이를 이분탐색으로 찾는다.
탐색마다 몇 개의 랜선을 만들 수 있는지 찾고 N 이상으로 만들 수 있으면 최대 길이를 갱신한다.

"""
import sys

input = sys.stdin.readline

K, N = map(int, input().rstrip("\n").split(" "))
line = [int(input().rstrip("\n")) for _ in range(K)]
line = sorted(line, reverse=True)


def sum_of_lines(length):
    ret = 0  # 만들 수 있는 랜선의 길이
    for l in line:
        if l < length:  # 잘라야 하는 길이가 더 길다면 종료
            break
        ret += l // length

    return ret


answer = 0
left = 1
right = line[0]
while left <= right:
    mid = (left + right) // 2
    sum_line = sum_of_lines(mid)

    if sum_line < N:  # N개보다 적게 만들었다면 더 짧게 잘라야 함
        right = mid - 1
    else:  # N개보다 많이 만들었다면 더 길게 잘라볼 수 있음
        left = mid + 1
        answer = mid if answer < mid else answer

print(answer)
