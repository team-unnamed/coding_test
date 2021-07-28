"""
일찍 끝나는 순서대로 배정...
"""

import sys


N = int(sys.stdin.readline())
meeting = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting_endwise = sorted(meeting, key=lambda x: (x[1], x[0]))  # 끝나는 시간이 같으면 시작하는 시간이 더 빠른 순으로 정렬

start_chosen = meeting_endwise[0][0]
end_chosen = meeting_endwise[0][1]
cnt = 1
for i in range(1, N):
    start_current, end_current = meeting_endwise[i]
    if start_current >= end_chosen:  # 골라놓은 회의 끝나고 나서 이번 회의가 시작한다면
        cnt += 1
        start_chosen = start_current
        end_chosen = end_current
        # pick

print(cnt)
