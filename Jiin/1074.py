"""
크기가 2^N * 2^N인 배열을 z 모양으로 방문

시간을 줄이기 위해서 r,c의 범위를 체크하고 해당 범위가 아니면 스킵하도록
"""

import sys

def split(n, r, c):  # n은 지수 (가로 길이가 아님)
    global cnt
    if n == 0:
        if R==r and C==c:
            print(cnt)
            exit()
        cnt += 1
        return

    else:
        m = n-1
        # z 모양으로 방문
        for i in range(2):
            for j in range(2):
                LEN = 2**m
                sub_r = r+i*LEN
                sub_c = c+j*LEN

                if sub_r <= R <= sub_r + LEN and sub_c <= C <= sub_c + LEN:  
                    split(m, r+i*LEN, c+j*LEN)  # 4등분한 조각 범위 안에 R,C가 있을 때만 직접 계산
                else:  
                    cnt += LEN**2  # 없으면 칸 수만 더하기


N, R, C = map(int, sys.stdin.readline().split())
cnt = 0
split(N, 0, 0)
