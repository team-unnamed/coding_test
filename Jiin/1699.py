'''
D[n] = 제곱수를 최소로 모아 n을 만드는 경우의 수
D[n-k] = 제곱수를 최소로 모아 n-k를 만드는 경우의 수

D[n] = min(D[n-k]) + 1  * 이 때 k는 1부터 sqrt(n)의 제곱들까지 선택가능
(k는 제곱수)

f(n)을 이루는 첫 항으로 i^2를 넣었으면  그 다음에는 f(n - i^2)를 계산해야 함

'''
import sys, math


N = int(sys.stdin.readline())
D = [9 for _ in range(N+1)]
D[0], D[1] = 0, 1
if N>1: D[2] = 2

for i in range(3, N+1):  # D[3]부터 시작해서 D[N]까지 채우기
    ROOT = int(math.sqrt(i))
    '''
    if ROOT**2 == i:
        D[i] = 1
        continue
    '''

    for j in range(1, ROOT+1):  # 2~N을 제곱수 j들의 합으로 채울 건데 N이 j^2일 때가 j의 최대값, 값은 sqrt(N)
        if D[i] < D[i-j*j]+1:
            D[i] = D[i-j*j]+1  # 1을 골랐으면 D[N-1*1]의 항 수를 계산, 3을 골랐으면 D[N-3*3]의 항 수를 계산

print(D[N])
