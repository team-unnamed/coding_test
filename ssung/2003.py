"""

구간 합이 M보다 작으면 오른쪽 포인터를 증가시키고
M보다 크거나 같으면 왼쪽 포인터를 증가시킨다.

오른쪽 포인터가 증가될 때 구간 합은 커지고 왼쪽 포인터가 증가될 때 구간 합은 줄어든다.

구간 합이 M과 같아지면 경우의수 +1

"""
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
arr = list(map(int, input().rstrip("\n").split(" ")))

answer = 0
left = right = part_sum = 0
while left <= right:
    if part_sum < M:  # M보다 작으면 오른쪽 포인터 증가
        if right == N:  # 범위를 벗어나면 종료
            break
        part_sum += arr[right]
        right += 1
    else:  # M보다 크거나 같으면 왼쪽 포인터 증가
        part_sum -= arr[left]
        left += 1

    if part_sum == M:  # 경우의수 +1
        answer += 1

print(answer)
