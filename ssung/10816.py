import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
card = list(map(int, input().rstrip("\n").split(" ")))
check = {}

for c in card:  # 가지고 있는 카드 개수 체크 (dict)
    if c in check:
        check[c] += 1
    else:
        check[c] = 1

M = int(input().rstrip("\n"))
has = list(map(int, input().rstrip("\n").split(" ")))

answer = [check[c] if c in check else 0 for c in has]  # 가지고 있는 카드 개수 출력
print(" ".join(map(str, answer)))
