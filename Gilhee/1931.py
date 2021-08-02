n = int(input())

time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort()

answer = 1
end = time[0][1]

for i in range(1,n):
    if time[i][0]>=end:
        answer +=1
        end = time[i][1]
    else:
        end = min(end, time[i][1])

print(answer)