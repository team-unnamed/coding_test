import sys
n = int(input())

input = sys.stdin.readline

mem = [ list(map(int,input().rstrip('\n').split())) for _ in range(n)]

answer = [0,0,0]

def solve(x, y, size):
    c = mem[x][y]

    check = False

    for i in range(x, x+size):
        for j in range(y, y+size):
            if mem[i][j] != c:
                check = True
                break
        
        if check:
            break
    
    if check:
        if size %3==0:
            l = size//3
            solve(x, y, l)
            solve(x, y+l, l)
            solve(x, y+2*l, l)
            solve(x+l, y, l)
            solve(x+l, y+l, l)
            solve(x+l, y+2*l, l)
            solve(x+2*l, y, l)
            solve(x+2*l, y+l, l)
            solve(x+2*l, y+2*l, l)
        else:
            for i in range(x, x+size):
                for j in range(y, y+size):
                    answer[mem[i][j]+1] +=1
    else:
        answer[c+1] +=1
        

solve(0,0,n)

for a in answer:
    print(a)