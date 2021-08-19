import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

times = list(map(int, input().rstrip('\n').split()))

def calc_people(mid):

    re = 0
    for time in times:
        re += mid//time +1
    
    return re

if n<=m:
    print(n)
    exit(0)

s = 1
e = max(times)*n
need_time = max(times)*n

while s<=e:
    mid = (s+e)//2

    if calc_people(mid)>=n:
        need_time = need_time if mid>need_time else mid
        e = mid-1
    else:
        s = mid+1

rest_people = n-calc_people(need_time-1)
rest_time = [need_time%time for time in times]

for i in range(m):
    if rest_time[i]==0:
        rest_people -= 1
    
    if rest_people ==0:
        print(i+1)
        break
