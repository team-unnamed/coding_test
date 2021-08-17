"""
나무자르기

벌목을 한다.
벌목 규제 덕분에 나무의 일정길이 (H)만큼 보존해야 한다. 
따라서 일정길이 (H) 보다 길다면 남은 부분만큼 자를 수 았고,
짧다면 보존한다.
하지만 상근이는 챙겨야할 나무의 길이가 존재한다.
상근이가 챙겨야할 나무 길이에 맞추려면 최대높이(H)을 얼마로 설정해야 할까? 

input
N, target : 나무의 수, 챙겨야할 나무 길이
tree_info : 각각 나무의 길이

이진 탐색!
H에 따라서, 
잘려진 나무 길이의 총합 (length) 가  < target 일땐, H를 줄인다.
잘려진 나무 길이의 총합 (length) 가  > target 일땐, H를 늘린다.
"""

import sys
input = sys.stdin.readline
N, target = map(int, input().split())
tree_info = list(map(int, input().split()))

right = max(tree_info)
left = 0

def get_sum(cut): 
    ## ㅡㅡ max( value, 0 ) 으로 한다면 시간 초과 발생, 별도의 함수로 지정해서 계산하는 것이 더 빠름 왜 일까?
    l = 0
    for t in tree_info:
        if t > cut:
            l += t-cut
    return l
        

res = 0
while left < right:
    mid = (left+right)//2
    lenght = get_sum(mid)
    if lenght >= target:
        left = mid + 1
        res = mid
    else:
        right = mid
print(res)


