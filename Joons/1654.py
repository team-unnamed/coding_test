"""
랜선 자르기

길이를 탐색

해당 길이 (mid) 를 통헤서 자른 랜선의 종류가
N 보다 크다면 ( N < cnt ) 자를 랜선의 길이를 늘린다. 추가적으로 랜선 길이 저장
반대면 자를 랜선의 길이를 줄인다.
"""
import sys
input = sys.stdin.readline
def solution(n, arr):
    low = 1
    high = max(arr)
    res = 0

    while low <= high:
        mid = (low + high)//2
        cable_cnt = 0
        for i in arr:
            cable_cnt += i // mid
        if cable_cnt < n:
            high = mid-1
        else:
            if res < mid:
                res = mid 
            low = mid+1
    return res

iter_, n = map(int, input().split( ))
arr = [int(input()) for _ in range(iter_)]
print(solution(n,arr))