import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input().rstrip("\n"))
A = list(map(int, input().rstrip("\n").split(" ")))
merge_list = [0 for _ in range(len(A))]  # merge sort를 이용해 오름차순정렬


# merge sort 구현
def merge_sort(start, mid, end):
    idx = start
    left = start
    right = mid + 1
    inv_cnt = 0  # inversion(swap) 횟수

    # 원래 list를 반으로 나누어서 진행
    while (left <= mid) and (right <= end):
        # 왼쪽 원소가 오른쪽 원소보다 작다면 그냥 넣어주면 된다. (swap 일어나지 않음)
        if A[left] <= A[right]:
            merge_list[idx] = A[left]
            idx += 1
            left += 1

        # 왼쪽 원소가 오른쪽 원소보다 크다면 inversion의 개수만큼 swap이 일어난다
        else:
            merge_list[idx] = A[right]
            inv_cnt += mid - left + 1
            idx += 1
            right += 1

    # 남은 list를 모두 넣어준다.
    while left <= mid:
        merge_list[idx] = A[left]
        idx += 1
        left += 1
    while right <= end:
        merge_list[idx] = A[right]
        idx += 1
        right += 1

    # 계속 merge sort하기 위해 list를 갱신해준다.
    for i in range(start, end + 1):
        A[i] = merge_list[i]

    return inv_cnt


# merge sort를 활용해 swap 횟수를 세자
def swap_cnt(start, end):
    if start == end:
        return 0

    mid = (start + end) // 2
    answer = (
        swap_cnt(start, mid) + swap_cnt(mid + 1, end) + merge_sort(start, mid, end)
    )  # list를 계속 반으로 쪼개가면서 swap 횟수를 구함

    return answer


print(swap_cnt(0, N - 1))
