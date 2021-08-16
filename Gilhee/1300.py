n = int(input())
k = int(input())

answer = 0
def find(s, e):
    global answer
    if s>e:
        print(answer)
        return

    m = (s+e)//2

    count =0
    for i in range(1, n+1):
        temp = m//i
        count += temp if temp<=n else n
    
    if count >=k:
        answer = m
        find(s, m-1)
    elif count <k:
        find(m+1, e)


find(1, n*n)
