"""
0~N까지의 정수 k개를 더해서 N이 되는 경우의 수 구하기
같은 수 중복 사용 가능 -> 자기 자신+0+0 이런것도 포함

d[k][i] = 숫자 k개 사용해서 i 만들기
숫자 2개 사용해서 i 만들기
숫자 k개 사용해서 i 만들기?

모르겠다너무어려운데
"""
import sys

N, K = map(int, sys.stdin.readline().split())

d = [[0]*(N+1) for _ in range(K+1)]

d[0][0] = 1
mod = 1_000_000_000

for i in range(1, K+1):
    for j in range(N+1):
        for k in range(j+1):
            d[i][j] += d[i-1][j-k]
            d[i][j] %= mod

print(d[K][N])
