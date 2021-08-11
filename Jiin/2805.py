'''
높이 H를 임의로 정해서 나무 베고 더하기
잘린 부분의 합이 M보다 작으면 높이 떨구고 크면 높이 낮추기
'''
import sys


def isSatisfied(H):
    treeSum = 0
    for tree in trees:
        fragment = tree - H
        if fragment > 0:
            treeSum += fragment
    if treeSum >= M:
        return True
    else:
        return False


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)
mid = (left+right)//2


# 조건에 맞으면 right를 땡기는 게 아니라 left를 땡겨오는 거라서 문제가 생김
# left와 right가 1 차이 날 때 mid는 round(두개 합) 이라서 left=mid이고, left와 right가 같아질 수 없게 된다
# 그래서 탈출조건을 저렇게 주고 탈출한 다음에 left가 답인지 right가 답인지 확인해보기
# right를 땡겨올 때는 이런 문제 없음

while left+1 < right:
    mid = (left + right) // 2

    condition = isSatisfied(mid)

    if condition:  # 나무조각 합 >= M이면 톱의 높이를 더 높여볼 수 있다
        left = mid  # 톱을 mid보다 더 높이면 못 챙길 수도 있으니까 일단 mid만큼은 챙겨야.
    else:
        right = mid-1 # 톱 높이가 mid이면 못 챙기니까 mid보다 더 낮추기

if isSatisfied(right):
    print(right)
else:
    print(left)

