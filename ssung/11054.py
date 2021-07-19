"""

각 위치에서 구성할 수 있는 증가, 감소 수열의 최대 길이를 구하면 되는 문제.

inc_list[i]: 인덱스가 i보다 작거나 같은 원소로 구성할 수 있는 증가 수열의 최대 길이
dec_list[i]: 인덱스가 i보다 크거나 같은 원소로 구성할 수 있는 감소 수열의 최대 길이

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
arr = list(map(int, input().rstrip("\n").split(" ")))

inc_list = [0 for _ in range(N)]  # 현재 위치에서 증가 수열의 길이를 저장
dec_list = [0 for _ in range(N)]  # 현재 위치에서 감소 수열의 길이를 저장 (역순으로 저장)

# 증가 수열(inc_list)을 채워준다.
for i in range(N):
    inc_list[i] = 1
    for j in range(i):
        if (arr[i] > arr[j]) and (inc_list[i] < inc_list[j] + 1):
            inc_list[i] = inc_list[j] + 1

# 감소 수열(dec_list)을 채워준다.
for i in range(N - 1, -1, -1):
    dec_list[i] = 1
    for j in range(N - 1, i - 1, -1):
        if (arr[i] > arr[j]) and (dec_list[i] < dec_list[j] + 1):
            dec_list[i] = dec_list[j] + 1

answer = 0
for inc, dec in zip(inc_list, dec_list):
    answer = max(answer, inc + dec)  # 현재 위치에서의 바이토닉 수열의 최대 길이를 저장

print(answer - 1)  # 중복으로 더해진 원소 제거
