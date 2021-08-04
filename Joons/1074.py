"""
Z 
Z 모양으로 2*2 행렬을 탐색
n 과, row, col 가 주어질때 
2**n * 2**n 의 행렬에서 row col 의 위치는 몇번째에 탐색하는지를 출력
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
                


