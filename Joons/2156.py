# 포도주
# 연속 3번 마시기 불가능 
# 최대한 많은 양을 마셔야 한다. 
# 각 idx 마다 마신 양을 정의하고, 연속으로 마신 여부까지 기록
# dp 에 이전에 한번, 두번, 안마셨을때를 고려하여 계산.

import sys
input = sys.stdin.readline
n = int(input())

dp = [[0,0,0,0,0]] #  skip,sskip, none, once, twice


for i in range(n):
    wine = int(input())
    skip, sskip, none, once, twice = dp[-1]
    dp.append([ once, none ,twice, max(none+wine, skip+wine, sskip+wine), once+wine])

print(max(dp[-1]))

    