"""

빼는 수를 최대한 크게 만들면 되므로 '-'를 기준으로 괄호를 치면 된다.

"""
import sys

input = sys.stdin.readline

st = input().rstrip("\n").split("-")

answer = 0
for i, s in enumerate(st):
    if "+" in s:
        if i == 0:  # 첫 숫자라면 더하고 아니면 빼준다.
            answer += sum(map(int, s.split("+")))
        else:
            answer -= sum(map(int, s.split("+")))
    else:
        if i == 0:
            answer += int(s)
        else:
            answer -= int(s)

print(answer)
