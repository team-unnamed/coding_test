import sys
import copy

input = sys.stdin.readline

N = int(input().rstrip("\n"))
A = list(map(int, input().rstrip("\n").split(" ")))

dp = copy.deepcopy(A)

for i in range(len(A)):
    for j in range(i):
        # 현재 위치에서 가장 큰 증가 부분 수열을 구하고 그 합의 최댓값을 구한다.
        if (A[j] < A[i]) and (dp[i] < dp[j] + A[i]):
            dp[i] = dp[j] + A[i]

print(max(dp))
