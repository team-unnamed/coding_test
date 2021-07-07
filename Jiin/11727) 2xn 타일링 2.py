'''
n번째 칸을 채우려면?
n-1번째 칸까지 채우고 남은 걸 1x2로 채우는 경우의 수
+ n-2번째 칸까지 채우고 남은 걸 2x2 1개나 1x2 2개로 채우는 경우의 수

그럼 f(n) = f(n-1) + 2*f(n-2)가 되나?
'''

import sys

N = int(sys.stdin.readline())

memo = [1, 1]+[0]*(N+1-2)

for n in range(2, N+1):
    memo[n] = memo[n-1] + 2*memo[n-2]
    memo[n] %= 10007

print(memo[N])
