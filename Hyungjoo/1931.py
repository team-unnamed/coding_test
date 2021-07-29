n = int(input())

meetings = [list(map(int, input().split())) for _ in range(n)]
meetings = sorted(meetings, key=lambda x: x[0])
meetings = sorted(meetings, key=lambda x: x[1])

ans = 1
last_meeting = meetings[0]
for meeting in meetings[1:]:
    if meeting[0] >= last_meeting[1]:
        ans += 1
        last_meeting = meeting

print(ans)
