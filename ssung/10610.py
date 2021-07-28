"""

30으로 나눌 수 있는 수는 각 자리수의 합이 3의 배수이고 마지막 자리가 0이어야 한다.

"""
import sys

input = sys.stdin.readline

N = list(map(int, input().rstrip("\n")))
N.sort(reverse=True)

if (sum(N) % 3 == 0) and (N.count(0) != 0):  # 3의 배수이고 0이 존재하면 30으로 나눌 수 있는 수
    print("".join(map(str, N)))
else:
    print(-1)
