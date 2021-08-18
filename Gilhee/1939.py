import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().rstrip('\n').split())

Map = [[] for _ in range(n)]

boundary = 0

for _ in range(m):
    a, b, c, = map(int, input().rstrip('\n').split())

    Map[a-1].append([b-1, c])
    Map[b-1].append([a-1, c])
    boundary = max(boundary,c)

x, y = map(int, input().rstrip('\n').split())

def bfs(mid):
    visit = [0 for _ in range(n)]

    queue = [x-1]
    visit[x-1] =1

    while queue:
        q = queue.pop(0)

        if q==y-1:
            return True

        for i, c in Map[q]:
            
            if c>= mid and visit[i]==0:
                queue.append(i)
                visit[i]=1
    
    return False

s=1
e=boundary
answer = 0
while s<=e:
    mid = (s+e)//2

    if bfs(mid):
        answer = max(answer, mid)
        s = mid +1
    else:
        e = mid -1

print(answer)
