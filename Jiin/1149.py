'''
집들은 각자 이웃한 집들과 다른 색이어야 함
n x 3 배열로 만들어서 어떤 집을 R로 칠했다면 그 다음 집은 G/B로 칠하도록
'''

import sys


N = int(sys.stdin.readline())
cost = []
for i in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    cost.append([r, g, b])

D = [[0, 0, 0] for _ in range(N)]
D[0] = cost[0]

for i in range(1, N):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + cost[i][0] # R로 칠할 거라면 앞집을 G 또는 B로 칠한 경우 중 더 저렴한 루트를 타기
    D[i][1] = min(D[i-1][0], D[i-1][2]) + cost[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + cost[i][2]

print(min(D[N-1]))
