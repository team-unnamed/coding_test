  
import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split())) # 입력받은 수열
D = [x for x in seq] # dp 배열, 부분수열의 합 저장

# seq[i] > seq[j] (j는 i 앞에 있는 원소들)인 경우 부분수열의 합이 최대인 쪽에 seq[i]를 더한다
for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]: # 증가하는 부분수열
            D[i] = max(D[i], seq[i]+D[j])

print(max(D))
