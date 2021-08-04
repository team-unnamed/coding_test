"""
Z 
Z 모양으로 2*2 행렬을 탐색
n 과, row, col 가 주어질때 
2**n * 2**n 의 행렬에서 row col 의 위치는 몇번째에 탐색하는지를 출력

분할 정복 방법으로 2**n * 2**n --> 2**n//2 by 2**n//2 이런식으로 접근
분할 방식은 col --> row
row col 이 일치하는지를 찾아 다니며 탐색하는 방법 수행

point!! 해당 목표 (row, col) 좌표가 분할된 행렬에 존재하지 않고 방향 이전이라면
분할 탐색을 수행하지 않고 해당 행렬의 칸 수만큼 넘기기

"""
cnt = 0
import sys
input = sys.stdin.readline
exit = sys.exit

N, R, C = map(int,input().split())


def divide(row,col,length):
    global cnt, R, C
    for r in range(row,length+row,length//2):
        for c in range(col, length+col, length//2):
            if (r <= R < r+length//2) and (c <= C < c+length//2): # R,C 가 해당 영역안에 있다면 divide | 탐색 
                if (r == R) and (c == C):
                    print(cnt)
                    exit(0)
                else:
                    divide(r,c,length//2)
            else:
                cnt += (length//2)**2
                
            

divide(0,0,2**N)
                


