n = int(input())

print(2**n -1)

def hanoi(start, mid, end, size):
    if size==1:
        print(start, end)
        return 

    hanoi(start, end, mid, size-1)
    print(start, end)
    hanoi(mid, start, end, size-1)

hanoi(1, 2, 3, n)