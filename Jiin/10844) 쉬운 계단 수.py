'''
memo(i,j) > i자리의 계단수가 j로 끝나는 경우의 수
j로 끝나는 i자리의 계단수 = j-1이나 j+1로 끝나는 i-1자리의 계단수 가짓수의 합
'''


import sys

N = int(sys.stdin.readline())

memo = [[0]*10 for i in range(101)]
memo[1] = [0,1,1,1,1,1,1,1,1,1] # 한자리 계단수에서 0은 제외 (0으로 시작해버리니까)


for i in range(2,N+1):
    for j in range(1,9):
        memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]

    memo[i][0] = memo[i-1][1] # 0으로 끝나는 경우에는 다음에 올 수 있는 숫자가 하나뿐
    memo[i][9] = memo[i-1][8] # 9로 끝나는 경우 역시 다음에 올 수 있는 숫자가 하나뿐

ans = 0
for n in memo[N]:
    ans += n
print(ans%1000000000)
