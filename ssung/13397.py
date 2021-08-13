"""

구간 점수의 최댓값의 최솟값(m)을 이분탐색으로 찾으면 된다.

divide_section 함수를 이용하여 m을 기준으로 구간을 나눈다.
인덱스마다 구간 점수를 구하고 m보다 구간 점수가 크다면
현재 위치까지의 최댓값, 최솟값은 다른 구간에 위치해야 하므로 구간을 나눠준다.

"""
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
arr = list(map(int, input().rstrip("\n").split(" ")))


# m을 기준으로 구간 나누기
def divide_section(m):
    section_max = section_min = arr[0]
    num_of_section = 1
    for i, num in enumerate(arr):
        section_max = num if section_max < num else section_max
        section_min = num if num < section_min else section_min
        if m < section_max - section_min:  # 구간 점수가 m보다 크다면
            num_of_section += 1  # 구간을 나누고
            section_max = section_min = num  # 다음 구간 탐색

    return num_of_section


answer = sys.maxsize
left = 0
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    num_of_section = divide_section(mid)

    if num_of_section <= M:  # 구간이 M개 이하이면 '구간 점수의 최댓값의 최솟값'을 갱신해준다.
        right = mid - 1
        answer = mid if mid < answer else answer
    else:  # 구간이 M개보다 많다면 '구간 점수의 최댓값의 최솟값'을 더 크게 해주어야 한다.
        left = mid + 1

print(answer)
