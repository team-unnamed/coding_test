import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def hanoi(N, fr, by, to):
    """
    하노이의 탑 구현

    Args:
        N (int): 전체 원판 개수
        fr (int): 하노이 탑 시작 위치.(문제에서 1)
        by (int): 최종 목적지에 도착하기 위해 거쳐가는 위치(문제에서 2)
        to (int): 최종 목적지.(문제에서 3)
    """
    if N == 1:
        print(fr, to)
        return

    hanoi(N - 1, fr, to, by)  # 시작위치(fr)에서 to를 거쳐 최종 목적지 by로 이동한다.
    print(fr, to)
    hanoi(N - 1, by, fr, to)  # 시작위치(by)에서 fr을 거쳐 최종 목적지 to로 이동한다.


N = int(input().rstrip('\n'))

print(2 ** N - 1)  # 하노이의 탑 이동 횟수
hanoi(N, 1, 2, 3)
