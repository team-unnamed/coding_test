"""
1. 문자열의 맨 뒤에 A를 추가
2. 문자열을 뒤집고 맨 뒤에 B를 추가

1을 알아보기 위해 끝이 A라면 A를 뗀다
2를 알아보기 위해 끝이 B라면 B를 떼고 뒤집는다
원래 문자열과 같은 길이가 될 때까지 반복

S = AB, T = AABAAB
> AABBA
> AABB
> BAA
> BA
> 불가능!
"""

import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

for i in range(len(T)-len(S)):
    if T[-1] == "A":
        T = T[:-1]

    elif T[-1] == "B":
        T = (T[:-1])[::-1]

if T==S:
    print(1)
else:
    print(0)

