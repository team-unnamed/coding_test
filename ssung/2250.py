"""

중위 순회(in-order)를 하면서 레벨(깊이)에 따른 거리를 저장하는 것이 문제 해결의 키포인트

"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input().rstrip("\n"))
tree = [[] for _ in range(N + 1)]
isRoot = [True for _ in range(N + 1)]  # 루트 노드를 찾기 위한 list

for _ in range(N):
    node, left_child, right_child = map(int, input().rstrip("\n").split(" "))
    tree[node].append(left_child)
    tree[node].append(right_child)

    # 자식 노드가 있으면 루트가 아님
    if left_child != -1:
        isRoot[left_child] = False
    if right_child != -1:
        isRoot[right_child] = False

stats = [[] for _ in range(N + 1)]

global cols
cols = 1


# 중위 순회
def inOrder(cur_node, depth):
    global cols

    if tree[cur_node][0] != -1:
        inOrder(tree[cur_node][0], depth + 1)

    stats[depth].append(cols)  # 레벨에 따라 거리를 저장해준다. (가장 왼쪽 노드가 0, 가장 오른쪽 노드가 N)
    cols += 1

    if tree[cur_node][1] != -1:
        inOrder(tree[cur_node][1], depth + 1)


# 루트 노드를 찾아서 트리를 탐색한다.
root = 0
for i in range(1, N + 1):
    if isRoot[i]:
        root = i
        break

inOrder(root, 1)

level = 1
max_len = 1
for i in range(2, N + 1):  # level 1은 루트노드이므로 고려하지 않는다.
    if not stats[i]:
        break

    length = stats[i][-1] - stats[i][0] + 1  # level i에서 너비를 구한다.
    if max_len < length:
        max_len = length
        level = i

print(level, max_len)
