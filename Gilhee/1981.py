import sys
input = sys.stdin.readline

n = int(input())

Map = []

boundary = [200,0]
for _ in range(n):
    Map.append(list(map(int, input().rstrip('\n').split())))
    boundary[0]= min(Map[-1]) if min(Map[-1])<boundary[0] else boundary[0]
    boundary[1]= max(Map[-1]) if max(Map[-1])>boundary[1] else boundary[1]

def bfs(mid):
    
    queue = [(0,0, Map[0][0], Map[0][0])]
    while queue:
        x, y, minimum, maximum = queue.pop(0)
        if x==n-1 and y==n-1:
            return True

        if x+1<n:
            mini = Map[y][x+1] if Map[y][x+1]<minimum else minimum
            maxi = Map[y][x+1] if Map[y][x+1]>maximum else maximum

            if maxi-mini<=mid:
                queue.append((x+1, y, mini, maxi ))

        if y+1<n :
            mini = Map[y+1][x] if Map[y+1][x]<minimum else minimum
            maxi = Map[y+1][x] if Map[y+1][x]>maximum else maximum

            if maxi-mini<=mid:
                queue.append((x, y+1, mini, maxi ))

    return False

start = 0
end = boundary[1]-boundary[0]
answer = boundary[1]-boundary[0]

while start<=end:
    mid = (start+end)//2

    if bfs(mid):
        answer = mid if answer>mid else answer
        end = mid-1
    else:
        start = mid+1

print(answer)