# 회의실 
# n개의 회의가 주어짐
# 각 회의 i 가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의 의 최대 개수를 찾는다
# 일찍 끝나는 회의들을 집중적으로 고른다.
# 짧은 회의를 집중적으로 고른다. 
# 즉, 일찍끝나면서 짧은 회의를 고르면 성공

import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

times = sorted( times, key = lambda x : (x[1],x[0]) )

s = 0
res = 0
for time in times:
    start, end = time
    if s <= start:
        s = time[1]
        res += 1
print(res)

        
