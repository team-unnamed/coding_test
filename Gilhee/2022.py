import sys
input = sys.stdin.readline

x, y, c = map(float, input().rstrip('\n').split())

def find(low, high):
    mid = (low+high)/2

    h1 = (x**2 - mid**2)**(1/2)
    h2 = (y**2 - mid**2)**(1/2)

    temp = (h1*h2)/(h1+h2)

    if abs(c-temp)<=0.001:
        print(mid)
        return

    if temp>c:
        find(mid, high)
    else:
        find(low, mid)

find(0, min(x,y))