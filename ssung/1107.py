"""

이동하려는 채널의 최댓값이 999999이므로 O(n)의 시간복잡도를 가질 수 있음.
누를 수 있는 채널을 0~999999까지 모두 눌러보고 가장 버튼을 적게 누른 경우를 찾으면 된다.

채널을 이동할 경우는 다음과 같다.
1. 이동하려는 채널의 숫자 버튼이 고장나지 않은 경우
2. 이동하려는 채널의 숫자 버튼이 하나라도 고장난 경우

1. 채널의 자릿수만큼 버튼을 누르면 된다. ex) 5457 -> 4번
2. 가장 가까운 채널로 이동한 뒤, (+, -)를 이용해 채널을 옮기면 된다.

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
M = int(input().rstrip("\n"))
is_crash = [False for _ in range(10)]  # 고장난 버튼 check
button = []
if M != 0:
    button = list(map(int, input().rstrip("\n").split(" ")))

for b in button:
    is_crash[b] = True

# 고장난 버튼이 있는지 찾는다.
def isBroken(channel):
    if channel == 0:
        if is_crash[0]:
            return True
        else:
            return False

    while channel:
        if is_crash[channel % 10]:
            return True
        channel //= 10

    return False


shortest = abs(N - 100)
for channel in range(1000000):  # 누를 수 있는 채널의 최댓값이 999999
    if isBroken(channel):
        continue

    length = len(str(channel))  # 숫자로 채널을 눌렀을 때 버튼을 누른 횟수는 그 길이가 된다.
    tmp = abs(N - channel)  # 이동한 채널과 목표 채널과의 거리 (+, -를 이용해 이동해야 함)
    shortest = min(shortest, tmp + length)

print(shortest)
