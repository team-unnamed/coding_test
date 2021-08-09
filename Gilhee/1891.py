import sys
input = sys.stdin.readline

n, d = map(int, input().rstrip('\n').split())
dx, dy = map(int, input().rstrip('\n').split())

x=0
y=0
size = (2**n)//2

for i in str(d):
    if i=='1' or i=='4':
        x += size
    
    if i=='3' or i=='4':
        y += size

    size = (size//2)

if x+dx<0 or x+dx>=2**n:
    print(-1)
elif y-dy<0 or y-dy>=2**n:
    print(-1)
else:
    x = x+dx
    y = y-dy
    size = (2**n)//2
    answer =''
    for i in range(n):
        if x>=size:
            if y>=size:
                answer +='4'
            else:
                answer +='1'
            x -= size
        else:
            if y>=size:
                answer +='3'
            else:
                answer +='2'

        if y>=size:
            y -=size

        size = size//2

    print(answer)