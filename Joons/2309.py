# 일곱난쟁이 
# 9명의 난쟁이가와서 자신이 일곱난쟁이라 주장한다. 
# 하지만 주인공은 난쟁이 들의 키의 합이 100인것을 알고 있다.
# 9명의 키가 주어질때 7개의 합이 100일때의 키들을 출력
# dfs 기반으로 완전탐색
import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
select = [0]*7
res = []

def dfs(start, length):
    if length == 7:
        if sum(select) == 100:
            res.append(sorted(select))
        return None
    
    for i in range(start,len(heights)):
        select[length] = heights[i]
        dfs(i+1, length+1)

dfs(0,0)
for i in res[0]:
    print(i)