# 로또
# k 개의 숫자들을 활용해서 나올수 있는 오름차순 형태의 6개 번호 출력하기
# DFS 방식으로 깊이가 6이 되었을때, 6자리수 출력

import sys
input = sys.stdin.readline


def dfs(start, depth):
    if depth == 6:
        print(' '.join(lotto))
        return None
    for i in range(start, k):
        lotto[depth] = str(arr[i])
        dfs(i+1, depth+1)

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    arr = arr[1:]
    lotto = [0]*6

    dfs(0,0)
    print()

