import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().rstrip('\n').split()))

answer = 0

def sorting(nums):
    global answer

    if len(nums)==1:
        return nums

    left = sorting(nums[:len(nums)//2])
    right = sorting(nums[len(nums)//2:])

    la,lb=len(left),len(right)
    i,j=0,0
    temp=[]
    while i<la and j<lb:
        if left[i]>right[j]:
            temp.append(right[j])
            j+=1
            answer+=la-i
        else:
            temp.append(left[i])
            i+=1
    if i==la:
        temp.extend(right[j:])
    else:
        temp.extend(left[i:])
    return temp

sorting(nums)

print(answer)