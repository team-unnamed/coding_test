"""

회의가 빨리 끝나는 순으로 정렬할 때, 끝나는 시간이 같다면 먼저 시작하는 회의를 앞으로 오도록 정렬해야 한다.

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip("\n"))
conf = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
conf = sorted(conf, key=lambda x: (x[1], x[0]))  # 회의가 빨리 끝나는 순으로 정렬

prev_end = 0
answer = 0
for start, end in conf:
    if prev_end <= start:  # 이전 회의가 끝나고 다음 회의를 진행할 수 있을 때 +1
        answer += 1
        prev_end = end

print(answer)
