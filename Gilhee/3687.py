k = int(input())

def min_num(n):
    match = [0,0,1,7,4,2,6,8,10, 18, 22, 20, 28, 68]
    
    if n<14:
        print(match[n], end=' ')
    else:
        ret = [8 for i in range((n+6)//7)]
        if n%7==1: ret[0]=1;ret[1]=0
        if n%7==2: ret[0]=1
        if n%7==3: ret[0]=2;ret[1]=0;ret[2]=0
        if n%7==4: ret[0]=2;ret[1]=0
        if n%7==5: ret[0]=2
        if n%7==6: ret[0]=6
        print(*ret,sep='',end=' ')

def max_num(n):
    if n%2==0:
        print('1'*(n//2))
    else:
        temp = '7'+'1'*((n-3)//2)
        print(temp)

for _ in range(k):
    n = int(input())

    min_num(n)
    max_num(n)

