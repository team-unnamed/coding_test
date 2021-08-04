"""
종이의 갯수
N*N 크기의 행렬로 표현되는 종이가 있다.
규칙에 따라 자른다.
1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각 잘린 종이에 대해서 (1)의 
과정을 반복

# 분할 하면서 분할 된 종이가 1의 규칙에 맞는지 확인
일치하면 넘기고 그렇지 않으면 나누기
"""

import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int, input().split())) for _ in range(N)]
res = [0]*3

def check(row,col,length): # 받은 종이의 갑이 모두 일치 하는지 확인하는 함수
    v = paper[row][col]
    for r in range(row, row+length):
        for c in range(col, col+length):
            if v != paper[r][c]:
                return False
    return True

def divide(row, col, length): # 종이 나누기 + 받은 종이의 값 확인하기
    global res
    if check(row,col,length):
        res[paper[row][col]] += 1
    else:
        for r in range(row, row+length, length//3):
            for c in range(col, col+length, length//3):
                divide(r,c,length//3)
    
divide(0,0,N)
print(res[-1])
print(res[0])
print(res[1])

    


