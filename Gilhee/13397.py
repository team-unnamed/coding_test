import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

nums = list(map(int, input().rstrip('\n').split()))

answer = 0

def find(low, high):
    global answer

    if low>high:
        print(answer)
        return

    mid = (low+high)//2

    max_x=min_x=nums[0]
    count =1
    for i in range(1,n):
        max_x=max(max_x,nums[i])
        min_x=min(min_x,nums[i])
        if max_x - min_x > mid:
            count +=1
            max_x=nums[i]
            min_x=nums[i]

    if count<=m:
        answer = mid
        find(low, mid-1)
    else:
        find(mid+1, high)


find(0, max(nums)-min(nums))