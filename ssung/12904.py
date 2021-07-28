"""

S를 T로 바꾸는 것이 아니라 T를 S로 바꾸어 보는 것이 핵심.

"""
import sys

input = sys.stdin.readline

S = input().rstrip("\n")
T = input().rstrip("\n")

# S와 T의 길이가 같아질 때까지 문자열을 변환한다
while len(S) != len(T):
    if T[-1] == "A": # 마지막 문자가 A라면 삭제
        T = T[:-1]
    elif T[-1] == "B": # 마지막 문자가 B라면 삭제하고 문자열을 뒤집는다.
        T = T[:-1]
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
