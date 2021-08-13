"""

B[k]를 구해야 하기 때문에 B[k]를 이분탐색으로 찾으면 된다.
문제의 예시에서 B[7], B[8]의 값이 같은 것처럼 B[k]의 값이 같은 경우가 생기기 때문에
원하는 k를 찾을 때까지 이분탐색을 계속 수행해야 한다.

행마다 임의의 숫자 m과 같거나 작은 수의 개수를 찾는다.
A에서 m보다 작거나 같은 수의 개수를 sum이라 했을 때

sum < k라면 m은 k번째 수가 될 수 없고
sum >= k라면 m은 k번째 수가 될 가능성이 있으므로 계속 값을 찾는다

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
k = int(input().rstrip("\n"))


# num보다 작은 수의 개수를 찾는다.
def partsum(num):
    ret = 0
    for i in range(1, N + 1):
        ret += num // i if num // i < N else N  # (num // i): i번째 행에서 num보다 작은 수의 개수

    return ret


left = 0
right = min(10000000000, k)
while left <= right:
    mid = (left + right) // 2
    psum = partsum(mid)

    if psum < k:  # k번째 수보다 작다면 값을 키워준다.
        left = mid + 1
    else:  # k번째 수보다 크거나 같다면 k번째 수가 될 수 있으므로 수를 줄여가며 계속 탐색
        right = mid - 1

print(left)
