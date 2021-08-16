"""
구간 나누기

input N, s
N : 배열의 길이, s : 분할해야 하는 배열의 수

input arr
arr 해당 배열

구간 만큼 배열을 나눴을때 구간 (해당 arr 에서 최대 - 최소) 의 값들중, 최대값이 가장 작을 경우를 찾기

목표 수(target) 보다 작은 구간을 만들어 내는 과정에서, 나눠진 구간들의 수(s) 보다 많이 나눠지게 된다면?
--> 이는 s 의 수만큼 구간을 만들어야 한다고 할때, 위 조건에 맞게 만들 수 없을을 의미함.
--> target의 수를 늘려야 한다. 

목표 수(target) 보다 작은 구간을 만들어 내는 과정에서, 나눠진 구간들의 수(s) 보다 적게 나눠지게 된다면?
--> 이는 target 값이 충분히 커서 아무렇게나 나눠도 조건에 맞게 나눌 수 있음을 의미
--> 이는 s 의 수만큼 구간을 만들어야 한다고 할때, 위 조건에 맞게 만들 수 있으며, 이중 최소 값을 가져야 함으로,
--> target의 수를 줄여야 한다.

## 탐색하는 방법
target (구간의 최대값) 을 설정하고 arr 선형 탐색을 하면서, 하나씩 구간을 늘려가며 구간의 최대와 최소의 차이가 
target 보다 크다면, 구간의 수를 ++, 
그렇지 않다면 그냥 pass
최종적으로 구간의 수를 출력
"""
import sys
input = sys.stdin.readline
N,s = map(int,input().split())
arr = list(map(int, input().split()))


left = 0
right = max(arr)

def check(target):
    s = 1
    MIN = arr[0]
    MAX = arr[0]
    for v in arr:
        MIN_t = min(MIN, v)
        MAX_t = max(MAX, v)
        if MAX_t - MIN_t > target:
            s += 1
            MAX = v
            MIN = v
        else:
            MIN = MIN_t
            MAX = MAX_t
    return s

res = 0
while left < right:
    mid = (left+right)//2
    if s < check(mid): # s 보다 많이 나눠야 한다면
        left = mid + 1 # target의 숫자를 키운다.
    else: # s 보다 적게 나눠진다면 target의 숫자가 크다는 뜻. 
        right = mid # target의 수를 줄인다. ( 최대에 도달하기 위해서 )
        res = mid
print(res)