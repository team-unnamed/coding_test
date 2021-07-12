'''
어떤 잔을 0연속으로 고르는 경우 > 이전 잔 선택 여부에 관계없이 현재 잔을 고르지 않음
 현재 최대값은 이전 잔까지의 최대값

어떤 잔을 1연속(첫번째)로 고르는 경우 > 이전 잔을 고르지 않음
 현재 최대값은 이전 잔을 안 고른 경우(0번)의 값 + 고른 잔의 값

어떤 잔을 2연속으로 고르는 경우 > 이전 잔을 골랐으며 다음 잔을 고르지 않음
 현재 최대값은 이전 잔을 1연속으로 고른 경우 + 고른 잔의 값
'''
import sys

N = int(sys.stdin.readline())
wine = [0 for _ in range(N + 1)]  # 1부터 시작
choose = [[0] * 3 for _ in range(N + 1)]  # choose[i][j] : i번째 포도주잔을 j연속으로 선택

for i in range(1, N + 1):
    wine[i] = int(sys.stdin.readline())

choose[1][0] = 0
choose[1][1] = wine[1]
choose[1][2] = 0  # 불가능

for i in range(2, N + 1):
    choose[i][0] = max(choose[i - 1])
    choose[i][1] = choose[i - 1][0] + wine[i]
    choose[i][2] = choose[i - 1][1] + wine[i]

print(max(choose[N]))
