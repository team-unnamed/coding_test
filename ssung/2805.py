"""

이분탐색으로 문제를 풀 때는 '어떤 것을 변수로 이분탐색을 할 것인가'가 중요한 것 같다.
이 문제에서는 절단기에 설정할 수 있는 높이를 변수로 두고 이분탐색을 진행하면 쉽게 풀 수 있다.

신기했던 점은 가져갈 수 있는 나무의 길이를 구할 때 반복문으로 직접 구하면 시간초과 발생, 함수를 이용해 연산하니 시간초과가 뜨지 않음

"""
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split(" "))
tree = list(map(int, input().rstrip("\n").split(" ")))
tree = sorted(tree, reverse=True)
answer = 0


# 함수를 이용해 구하지 않았을 시 시간초과 발생
def sum_of_tree(cut):
    ret = 0
    for h in tree:
        if h <= cut:
            break
        ret += h - cut

    return ret


left = 0
right = max(tree)
while left <= right:
    mid = (left + right) // 2

    sum_tree = sum_of_tree(mid)  # 가져갈 수 있는 나무의 길이를 구해본다.

    if sum_tree < M:  # M보다 작으면 절단기의 높이를 내려야 함
        right = mid - 1
    elif sum_tree == M:  # 가져갈 수 있는 나무의 길이가 딱 M이라면 그것이 최댓값
        print(mid)
        exit(0)
    else:  # M보다 크면 절단기의 높이를 높일 수 있다
        answer = mid if answer < mid else answer
        left = mid + 1

print(answer)
