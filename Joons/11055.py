# 가장 큰 부분 증가 수열
# arr 를 돌면서 매 번 값에 따른 증가 여부 파악하기
import sys

n = int(sys.stdin.readline().split()[0])
arr = list(map(int, sys.stdin.readline().split()))

d = [0]*n
for i in range(n):
    d[i] = arr[i]
    for j in range(i):
        tmp = d[j] + arr[i]
        if (arr[j] < arr[i]) and (tmp > d[i]):
            d[i] = tmp
print(max(d))
            