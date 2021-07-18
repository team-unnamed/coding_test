import sys
'''
1) 증가하는 부분수열의 길이를 싹 구한다
2) 감소하는 부분수열의 길이를 싹 구한다
     증가수열 구하는 방향 : ->
     감소수열 구하는 방향 : <- (dec에 기록하는 방향도 <-)
     그래야 두 수열을 연결할 수 있음
3) 위의 두 리스트에서 같은 인덱스끼리 더했을 때 가장 큰 것 -1이 답
   -1 하는 이유는 1)과 2)에 겹치는 원소가 하나 있으니까
'''

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
inc = [1 for _ in range(N)]  #수열의 길이
dec = [1 for _ in range(N)]
bitonic = [0 for _ in range(N)]

for i in range(N):  # 증가수열
    for j in range(i):
        if seq[i] > seq[j]:
            inc[i] = max(inc[i], inc[j]+1)

for i in range(N-1,-1,-1):  # 감소수열
    for j in range(N-1,i,-1):
        if seq[i] > seq[j]:
            dec[i] = max(dec[i], dec[j]+1)

for i in range(N):
    bitonic[i] = inc[i]+dec[i]-1

print(max(bitonic))
