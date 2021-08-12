# 자른 랜선 길이를 x라고 하면 k개의 랜선을 x길이로 잘라서 n개를 만들 수 있는가를 확인해야 함
# x를 임의로 정해서 돌려 보고 n개 넘게 만들 수 있으면 x가 더 길어도 됨
# n개를 못 만들면 x가 더 짧아야 함
import sys


def cut(lans, x):
    cnt = 0
    for cord in lans:
        cnt += cord//x
    return cnt


K, N = map(int, sys.stdin.readline().split())
LANS = [int(sys.stdin.readline()) for _ in range(K)]
left = 1
right = max(LANS)
maxCord = 0

while left <= right:
    mid = (left+right)//2
    piece = cut(LANS,mid)

    if piece < N: # N개 못만들었다는건 길이가 너무 길다는 것
        right = mid - 1
    elif piece >= N: # N개 넘었다는 건 짧다는 것
        left = mid + 1
        if maxCord < mid:
            maxCord = mid


print(maxCord)
