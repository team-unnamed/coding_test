import sys

N = int(sys.stdin.readline())

# 11726번과 거의 같은데 이번에는 맨 끝에 2x2가 올 수 있다는 것이 추가됨
# 맨 끝에 2x1 두개 오는 경우와 2x2 하나가 오는 경우의 수가 같다

# 그럼 f(n) = f(n-1) + 2*f(n-2)가 되나?

memo = [1, 1]+[0]*(N+1-2)

for n in range(2, N+1):
    memo[n] = memo[n-1] + 2*memo[n-2]
    memo[n] %= 10007

print(memo[N])