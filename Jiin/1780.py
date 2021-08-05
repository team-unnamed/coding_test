"""
종이에 적힌 숫자가 전부 같은지 체크
다르면 9장으로 쪼개기
또 체크

재귀함수로...?
split(r, c, n) : paper[r][c]에서 시작해서 가로세로 n인 종이를 체크하고 쪼개는 함수
"""

import sys


def isSame(r, c, n):
    if n==1:
        return True

    before = paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if before != paper[i][j]:
                return False
            before = paper[i][j]
    return True


def split(r, c, n):  # r, c는 종이조각의 왼쪽 위 지점
    global cnt
    if isSame(r, c, n):
        val = paper[r][c]
        cnt[val] += 1  # [0, 1, -1] 이니까 그 값에 해당하는 인덱스 증가

    else:
        sub_n = n//3
        for i in range(3):
            for j in range(3):
                split(r+sub_n*i, c+sub_n*j, sub_n)



N = int(sys.stdin.readline())
cnt = [0,0,0]
paper = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    paper.append(line)

split(0, 0, N)
print(cnt[-1])
print(cnt[0])
print(cnt[1])

