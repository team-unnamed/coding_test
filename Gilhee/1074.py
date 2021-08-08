n, r, c = map(int, input().split())

size = 2**n

total = size**2

answer =0

while True:

    if size==1:
        break

    if r>=size//2:
        answer += total//2
        r -= size//2
    
    if c>=size//2:
        answer += total//4
        c -= size//2
    
    size /= 2
    total = total//4

print(int(answer))