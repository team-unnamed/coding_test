n = int(input())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    line = list(map(int, input().split()))
    graph[line[0]].append((line[1], line[2]))
    graph[line[1]].append((line[0], line[2]))


def bfs(node):
    queue = [node]

    visit = [0 for i in range(n+1)]
    length = [0 for i in range(n + 1)]
    visit[node]=1

    while queue:
        q = queue[0]

        for g, l in graph[q]:
            if visit[g]==0:
                queue.append(g)
                length[g] = length[q]+l
                visit[g]=1

        queue.pop(0)

    return length

result = bfs(1)


result = bfs(result.index(max(result)))

print(max(result))