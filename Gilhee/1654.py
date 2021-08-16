import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip('\n').split())

lines = [int(input()) for _ in range(k)]

answer = 0

def find(start, end):
    global answer

    if end<start:
        print(answer)
        return

    s = 0
    mid = (end+start)//2
    for line in lines:
        if line>=mid:
            s+= line//mid
    
    if s>=n and max(mid, answer)==mid:
        answer = mid
        find(mid+1, end)
    else:
        find(start, mid-1)

find(1, max(lines))