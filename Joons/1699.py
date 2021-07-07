# 제곱수의 합 푸는중입니당.
# 최적의 마지막 항을 찾는 방식
# 찾아진 값들은 저장. 
import sys

N = int(sys.stdin.readline().split()[0])+1

dp = [0]*N

for n in range(N):
    dp[n] = n
    # 갱신 부분
    for i in range(n):
        i_ = i*i
        if i_ <= n:
            if dp[n-i_]+1 < dp[n]:
                dp[n] = dp[n-i_]+1
        else:
            break

print(dp[-1])