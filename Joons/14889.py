# 스타트와 링크
# 플레이어 간의 행렬이 존재, S_ij 는 i 와 j 가 같은 팀일때의 능력치
# 이는 반대 S_ji 와 다를 수 도 있으며 팀에게 추가되는 능력치는 S_ij + S_ji 가 된다.
# 두 팀의 능력치를 최소화 하는 방향으로 접근하자.
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

team_pair = list(combinations([i for i in range(n)], int(n/2)))
def get_diff(team_1, n):
    team_1_score = 0
    team_2_score = 0
    for p1 in range(n): 
        if p1 in team_1: # team_1 의 score 계산
            for p2 in range(n):
                if p2 in team_1:
                    team_1_score += matrix[p1][p2]
        else:
            for p2 in range(n): # team_2 의 score 계산 
                if not(p2 in team_1):
                    team_2_score += matrix[p1][p2]
    return abs(team_1_score - team_2_score)     
            

res = 1000000000
for i in team_pair:
    tmp = get_diff(i, n)
    if  tmp < res:
        res = tmp 
print(res)

