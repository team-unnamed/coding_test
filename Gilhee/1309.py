n = int(input())

left = 1
right = 1
blank = 1

for i in range(1,n):
    new_left = right+blank
    new_right = left+blank
    new_blank = left+right+blank
    
    left = new_left
    right =new_right
    blank = new_blank

print((left+right+blank)%9901)