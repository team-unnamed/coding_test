"""

기본적인 투포인터 문제
1. 부분 합이 S보다 작다면 오른쪽 포인터가 가리키는 수를 더해주고 오른쪽 포인터를 하나 증가시킨다.
2. 부분 합이 S보다 크거나 같으면 왼쪽 포인터가 가리키는 수를 더하고 왼쪽 포인터를 하나 증가시킨다.
2-1. 최소길이를 갱신해준다.

"""
import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip("\n").split(" "))
arr = list(map(int, input().rstrip("\n").split(" ")))

min_length = sys.maxsize
left = right = part_sum = 0
while left <= right:
    if part_sum < S:
        if right == len(arr):
            break
        part_sum += arr[right]
        right += 1
    else:
        part_sum -= arr[left]
        left += 1
        min_length = right - left + 1 if right - left + 1 < min_length else min_length

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
