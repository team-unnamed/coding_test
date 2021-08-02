"""
문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.

조건을 만족하는 문자열을 만들어서 아무거나 출력
만들 수 없는 경우 -1 출력


A와 B의 합은 N, 곱은 K가 되도록 하면?
그럼 2차방정식인가? x^2 + Nx + K의 실근이 존재하면 되나?

와 이게 되네
"""

import sys, math

N, K = map(int, sys.stdin.readline().split())
D = N**2 - 4*K  # x^2 + Nx + K 판별식

if D < 0:
    print(-1)

else:
    ROOT = math.sqrt(D)
    x1 = -int((-N + ROOT) / 2)  # 문자를 0.3개 넣을 수는 없으니까 소수점 자르기
    x2 = -int((-N - ROOT) / 2)  # N,K는 모두 양수니까 무조건 해가 음수겠지
    s = 'A' * x1 + 'B' * x2  # 일단 A를 x1개, B를 x2개씩 집어넣는다 (ABBBBBBBB)

    lack = K - (x1*x2)  # AB가 K쌍 있어야 하는데 몇 쌍이 부족한지 체크
    if lack > 0:
        s = s[:-lack] + 'A' + s[-lack:]  # lack쌍만큼 부족하다면 뒤에서부터 세어서 AB가 lack쌍이 되는 위치에 A 집어넣기 (ABBBBABBBB)
    print(s)


