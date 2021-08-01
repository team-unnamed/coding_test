"""

스위치를 누르는 순서에 관계없이 누른 스위치가 같다면 전구의 상태가 같기 때문에
1번 스위치부터 N번 스위치까지 차례대로 누른다고 가정하고 진행하였음.

현재 전구의 상태를 init, 목표 상태를 target이라고 하자.
이 때, init[i] != target[i]라면 i+1번째 스위치를 무조건 눌러야 함을 알 수 있다.

초기 상태를 1번 스위치를 눌렀을 경우와 그렇지 않은 경우로 나누어 생각했다.

"""
import sys
import copy

input = sys.stdin.readline

N = int(input().rstrip("\n"))
init = list(map(int, input().rstrip("\n")))
target = list(map(int, input().rstrip("\n")))
answer = []  # 각 case별 스위치 누른 횟수 저장 (target과 같을 경우)

# 1번 스위치를 눌렀을 경우
init1 = copy.deepcopy(init)
init1[0] = 0 if init1[0] + 1 == 2 else 1
init1[1] = 0 if init1[1] + 1 == 2 else 1
cnt1 = 1
for i in range(1, len(init)):
    if init1[i - 1] != target[i - 1]:  # 이전 전구의 상태가 목표와 다르다면 이번 스위치는 무조건 눌러야 한다.
        init1[i - 1] = 0 if init1[i - 1] + 1 == 2 else 1
        init1[i] = 0 if init1[i] + 1 == 2 else 1
        if i + 1 < len(init):
            init1[i + 1] = 0 if init1[i + 1] + 1 == 2 else 1
        cnt1 += 1

if init1 == target:  # 목표 상태와 같다면 누른 횟수를 저장해준다.
    answer.append(cnt1)

# 1번 스위치를 누르지 않은 경우
init2 = copy.deepcopy(init)
cnt2 = 0
for i in range(1, len(init)):
    if init2[i - 1] != target[i - 1]:
        init2[i - 1] = 0 if init2[i - 1] + 1 == 2 else 1
        init2[i] = 0 if init2[i] + 1 == 2 else 1
        if i + 1 < len(init):
            init2[i + 1] = 0 if init2[i + 1] + 1 == 2 else 1
        cnt2 += 1

if init2 == target:
    answer.append(cnt2)

# 위 두 가지 경우에도 목표 상태가 되지 않았으면 만들 수 없는 상태이므로 -1 출력
print(-1) if not answer else print(min(answer))
