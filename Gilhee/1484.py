import sys
g = int(input())

limit = int(g/2+1/2)

s=1
e=1

answer = []

while s<=limit and e<=limit:
    res = e**2 - s**2

    if res<g:
        e +=1
    elif res==g:
        answer.append(e)
        s+=1
    else:
        s+=1

if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)