import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())

    memo = [[0]*(N+1) for n in range(3)] # 1부터 시작하려고
    arr = [[0]*(N+1) for n in range(3)]


    for i in range(1,3):
        arr[i] = [0]+list(map(int, sys.stdin.readline().split()))

    memo[1][1] = arr[1][1]
    memo[2][1] = arr[2][1]



    for j in range(2,N+1):
        for i in range(1,3):
            memo[i][j] = max( memo[3-i][j-1], memo[3-i][j-2] ) + arr[i][j]
            #                 i가 1 또는 2라서 3-i로 스위칭


    res = [memo[1][N], memo[2][N], memo[1][N-1], memo[2][N-1]]
    print(max(res))

