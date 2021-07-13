'''
1일차부터 시작해서 N+1일째 되는 날 퇴사
income : 오늘까지 일했을 때 벌게 되는 돈의 최대값?

어떤 일이 하루 걸린다면 그건 그날 안에 끝나는 일인가?
꼭 상담을 맡아야 하는 건 아님... i일차의 상담을 넘기고 i+1일차 상담을 맡을 수도 있다
'''

import sys

N = int(sys.stdin.readline())
time = [0 for _ in range(20+1)]  # N이 15까지고 T가 5까지라서
pay = [0 for _ in range(20+1)]
income = [0 for _ in range(20+1)]

for i in range(1, N+1): # 1일부터 N일까지
    time[i], pay[i] = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    t = time[i]
    income[i] = max(income[i], income[i-1])  # 오늘 번 돈보다 어제까지 벌어둔 돈이 더 많으면 오늘 일하지 말기 (일을 맡으면 시간이 걸리니까)
    income[i+t-1] = max(income[i+t-1], income[i-1] + pay[i])  # 1일 걸리는 일은 오늘 안에 끝난다고 쳐서 t일 걸리는 일은 t-1에 끝남


print(max(income[:N+1]))
