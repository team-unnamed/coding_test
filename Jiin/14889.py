"""
조합으로 N개 중에 N/2개를 뽑아서 나오는 조합들의 값을 다 더해봐
iterools.combination 쓰면 대칭적으로 구해진다!
맨 앞에 (1,2,3)/맨 뒤에 (4,5,6) 있고 두번째에는 (1,2,4)/뒤에서 두번째에는 (3,5,6)
"""

import sys, itertools

N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
combi_people = list(itertools.combinations(range(1, N+1), N//2))  # 팀을 나누는 조합
LEN = len(combi_people)
sub_min = float('inf')

for i in range(LEN//2):
    start = combi_people[i]  # 앞에서부터
    link = combi_people[-1-i]  # 뒤에서부터

    combi_status_start = list(itertools.combinations(start, 2))  # 팀이 되면 얻는 능력치를 구하기 위한 조합 (팀 내에서 두명씩 고르기)
    status_start = 0
    for r, c in combi_status_start:
        status_start += table[r-1][c-1]  # 사람 번호는 1부터 시작함
        status_start += table[c-1][r-1]  # table[i][j]랑 table[j][i]가 다르다

    combi_status_link = list(itertools.combinations(link, 2))
    status_link = 0
    for r, c in combi_status_link:
        status_link += table[r-1][c-1]
        status_link += table[c-1][r-1]

    sub = abs(status_start-status_link)
    sub_min = min(sub_min, sub)

print(sub_min)
