import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())
trees = list(map(int, input().rstrip('\n').split()))

def find(start, height, end):
    if end-start==1:
        a = sum([t-start if t>=start else 0 for t in trees])
        b = sum([t-end if t>=end else 0 for t in trees])
        if min(m-a, m-b)==m-a and m-a<=0:
            print(start)
        else:
            print(end)
        return


    s = sum([t-height if t>=height else 0 for t in trees])

    if s==m:
        print(height)
    elif s<m:
        find(start, (start+height)//2, height)
    else:
        find(height, (end+height)//2, end)

find(0,max(trees)//2, max(trees))