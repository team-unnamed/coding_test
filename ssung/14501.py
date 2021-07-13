"""

완전탐색
cons[i][0]: i번째 날의 상담 기간
cons[i][1]: i번째 날에 상담을 했을 때 받을 수 있는 비용

"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

global result

N = int(input().rstrip("\n"))
result = -1
cons = []

# 모든 경우의 수를 탐색하면서 가장 높은 비용을 result에 갱신해준다.
def bruteforce(init, money):
    global result

    if init > N:
        return

    result = money if result < money else result
    for i in range(init, N):
        # i번째 날에 일을 한다면 다음에 상담이 가능한 날짜(init)는 i + cons[i][0]
        # 비용(money)은 i번째 날까지의 비용 + i번째날 상담시 받을 수 있는 비용.
        bruteforce(i + cons[i][0], money + cons[i][1])


for _ in range(N):
    cons.append(list(map(int, input().rstrip("\n").split(" "))))

bruteforce(0, 0)
print(result)
