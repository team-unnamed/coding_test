"""

N : 문자열 S의 길이
num_A : A의 개수
num_B : B의 개수 (N - num_A)

이해하는 데 오래걸렸던 문제...
num_A * num_B > K인 경우를 잘 처리 해주면 어렵지 않게 풀 수 있다.

1. num_A * num_B < K인 경우는 조건을 만족하는 문자열을 만들 수 없다.
2. num_A * num_B == K 이면 개수에 맞게 A, B를 넣어주기만 하면 된다.
3. num_A * num_B > K인 경우
   
   - 과정 1: line 52 ~ 56
   K보다 작은 쌍을 만들어서 먼저 S에 넣어준다.
   => A는 (num_A - 1)개, B는 num_B개, 문자열 S의 길이는 N-1이 된다.
   
   - 과정 2: line 59 ~ 61
   위에서 (num_A - 1) * num_B의 쌍이 만들어 졌으므로 나머지 쌍을 추가해야 한다.
   그 과정은 하나 남은 A의 자리를 정해주는 과정으로 생각하면 된다.
   A가 하나이므로 (만들 수 있는 쌍의 개수 = B의 개수) 이다. 
   남은 쌍의 개수가 left개 이므로 하나 남은 A 뒤에 left개의 B가 오도록 위치하면 S완성. 

   ex) 10 17인 경우
       num_A = 3, num_B = 7 일 때, num_A * num_B > K를 만족
       과정 1을 거쳐 문자열 S는 'AABBBBBBB'가 된다. 
       
       이제 14개의 쌍이 만들어졌으므로 남은 쌍은 3개이다. 오른쪽에 B가 3개만 오도록 A의 위치를 정해주자.
       과정 2를 거쳐 구하려는 문자열 S는 'AABBBBABBB'

"""
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip("\n").split(" "))

S = []
for num_A in range(N + 1):
    num_B = N - num_A
    if num_A * num_B < K:
        continue

    # 쌍이 맞다면 개수에 맞게 넣어주기만 하면 됨.
    if num_A * num_B == K:
        for _ in range(num_A):
            S.append("A")
        for _ in range(num_B):
            S.append("B")

    # K보다 크다면 우선 A의 개수를 하나 줄이고 쌍에 맞게 넣어준다. (num_A * num_B > K 이므로 A의 개수를 하나 줄여서 넣어준다.)
    elif num_A * num_B > K:
        for _ in range(num_A - 1):
            S.append("A")
        for _ in range(num_B):
            S.append("B")

        # 이제 하나 남은 A의 자리를 찾으면 된다. (A뒤에 left개의 B가 있어야 함)
        left = K % num_B
        S[-left] = "A"
        S.append("B")

    break

if S:  # 문자열을 만들 수 있으면 S 출력. 그렇지 않으면 -1 출력.
    print("".join(S))
else:
    print(-1)
