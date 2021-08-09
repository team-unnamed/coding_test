"""
버블 소트
버블 정렬 방식으로 진행 할때, 총 순서를 바꾸는 횟수는 몇번인지 출력

방법 1. 병합 정렬 방식을 이용해서 ++ 한다
방법 2. index tree 를 활용해서 구현이 가능하다. 
"""
import sys
input = sys.stdin.readline

length = int(input())
arr = list(map(int, input().split()))

def merge_sort(start,end):
    global swap, arr
    size = end - start
    mid = (start+end)//2
    if size <= 1:
        return
    
    merge_sort(start,mid)
    merge_sort(mid,end)

    n_arr = []
    idx1, idx2 = start,mid

    cnt = 0
    while idx1 < mid and idx2 < end:
        if arr[idx1] > arr[idx2]:
            n_arr.append(arr[idx2])
            idx2 += 1
            cnt += 1
        else:
            n_arr.append(arr[idx1])
            idx1 += 1
            swap += cnt
    while idx1 < mid:
        n_arr.append(arr[idx1])
        idx1 += 1
        swap += cnt
    while idx2 < mid:
        n_arr.append(arr[idx2])
        idx2 += 1

    for i in range(len(n_arr)):
        arr[start+i] = n_arr[i]

swap = 0
merge_sort(0, length)
print(swap)