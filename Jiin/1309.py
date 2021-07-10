'''
사자를 왼쪽에 배치하는 경우 / 오른쪽에 배치하는 경우 / 배치하지 않는 경우로 나누면
RGB거리 문제처럼 풀 수 있다
'''

import sys

N = int(sys.stdin.readline())
d = [[0, 0, 0] for _ in range(N)]
d[0] = [1, 1, 1]
DENOM = 9901

for i in range(1, N):
    d[i][0] = (d[i-1][1] + d[i-1][2]) % DENOM
    d[i][1] = (d[i-1][0] + d[i-1][2]) % DENOM
    d[i][2] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % DENOM
    # 사자를 배치하지 않을 경우에는 n-1번째 칸에도 사자가 없을 가능성을 고려해야 함

print(sum(d[N-1]))
