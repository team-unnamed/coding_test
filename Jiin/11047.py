"""
쭉 돌면서 몫 구하면 되는 것 같은데
"""

import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
quotient = 0
coins = []

for i in range(N):
    coins.append( int(sys.stdin.readline()) )

for i in range(N-1, -1, -1):
    quotient = K // coins[i]
    if quotient > 0:
        K -= quotient*coins[i]
        cnt += quotient

    if K == 0: break

print(cnt)
