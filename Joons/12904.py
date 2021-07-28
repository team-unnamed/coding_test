# A 와 B 
# T를 S로 역행하는 방법을 사용하자.
# 마지막 문자열이 A이면, 제거하기
# 마지막 문자열이 B라면, 제고하고 문자열 뒤집기

import sys
input = sys.stdin.readline
S = input().split()[0]
T = input().split()[0]


while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[::-1][1:]

if T == S:
    print(1)
else:
    print(0)
