"""

루트 노드를 기준으로 가장 멀리 떨어진 노드를 찾는다 (지름이 될 두 개의 node 중 하나)
찾은 node를 기준으로 가장 멀리 떨어진 노드를 찾으면 트리의 지름이 된다.

"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().rstrip("\n"))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, cost = map(int, input().rstrip("\n").split(" "))
    tree[u].append([v, cost])
    tree[v].append([u, cost])

global length, init_node
length = 0
init_node = 0
isVisited = [False for _ in range(n + 1)]


def dfs(cur_node, cost):
    global length, init_node

    isVisited[cur_node] = True
    if length < cost:
        length = cost
        init_node = cur_node

    for next_node, next_cost in tree[cur_node]:
        if not isVisited[next_node]:
            dfs(next_node, cost + next_cost)


dfs(1, 0)  # 루트에서 시작해서 가장 멀리있는 node를 하나 찾는다. (지름이 될 두 개의 node 중 하나)

length = 0
isVisited = [False for _ in range(n + 1)]

dfs(init_node, 0)  # 찾은 node에서 가장 멀리 떨어진 node를 찾는다 (지름)

print(length)
