import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip('\n').split())

location = [int(input()) for _ in range(n)]

location.sort()

distance = [location[i+1]-location[i] for i in range(n-1)]

answer = 0
def find(s, e):
    global answer
    if s>e:
        print(answer)
        return

    m = (s+e)//2

    count = 1
    summation = 0
    minimum =1000000000

    for d in distance:
        if summation+d>=m:
            count +=1
            minimum = min(minimum, summation+d)
            summation =0
        else:
            summation += d
    
    if count >= c:
        answer = max(answer, minimum)
        find(m+1, e)
    elif count < c:
        find(s, m-1)
        
find(1, location[-1]-1)