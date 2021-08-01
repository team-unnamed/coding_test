# 전구의 스위치
# 주번의 전구가 동시에 작동 된다. 
# 해당 상태에 도달하기 위해서 최소 조건의 수를 계산하여라
# 경우의 수를 최소화 하는 방법 이 greedy의 주요 목적? 이 아닌가 싶다

# 각 버튼이 일어날 경우의 수는 4 자리의 경우
# 2332 가 된다. idx 0 은 0을 누를때, 1을 누를때 변하게 된다. (2개)
# 이러한 경우를 최소화 하는 방향으로 접근..
# 첫 스위치를 누른다고 했을때, 경우의 수는 1232
# 그다음 스위치를 누른다고 했을때 다음 경우의 수는 1122
# 즉 각 인덱스 마다 최선의 선택을 통해서 다음 번으로 진행 하는 방향으로 접근
"""
첫번째 스위치를 눌렀을때, 첫번쨰 스위치를 누르지 않았을때 로 나눠서 
이전 전구의 상태를 보고 일치하지 않으면 누르고 그렇지 않으면 넘기기 방식
"""

import sys
input = sys.stdin.readline

N = int(input().split()[0])
state = [int(i) for i in input().split()[0]]
target = [int(i) for i in input().split()[0]]
avaliable = False

def click(state,i):
    for d in [-1,0,1]: # 스위치 누르는 연산
        if 0<=i+d<len(state):
            if state[i+d]:
                state[i+d] = 0
            else:
                state[i+d] = 1
    return state

def f(state, target):
    global avaliable
    cnt = 0
    start = state.copy()

    for i in range(1,len(start)):
        if start[i-1] == target[i-1]:
            pass
        else: # 스위치 누르는 경우.
            start = click(start, i)
            cnt += 1
    if start[-1] == target[-1]:
        avaliable = True
        return cnt
    else:
        return len(start)


res = min(f(state, target), f(click(state,0), target)+1)
if avaliable:
    print(res)
else:
    print(-1)