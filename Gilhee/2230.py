import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip('\n').split())

nums= [int(input()) for _ in range(n)]

nums.sort()

mini = sys.maxsize

s=0
e=0

while s<n and e<n:
    dis = nums[e]-nums[s]

    if dis<m:
        e+=1
    else:
        if dis<mini:
            mini = dis
        s+=1

print(mini)