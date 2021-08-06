"""

중위 순회를 하면서 노드를 먼저 출력하면 pre-order가 된다.
root node의 index를 index()로 찾으면 시간 초과....

"""
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input().rstrip("\n"))
inorder = list(map(int, input().rstrip("\n").split(" ")))
postorder = list(map(int, input().rstrip("\n").split(" ")))
idx = [0 for _ in range(n+1)]
preorder = []

for i in range(n):  # 각 노드의 index를 저장해준다.
    idx[inorder[i]] = i


def dnc(in_start, in_end, post_start, post_end):
    if (in_end < in_start) or (post_end < post_start):  # 인덱스를 벗어나면 함수를 종료
        return

    root = postorder[post_end]  # root node
    index = idx[root]  # root node의 인덱스
    l_len = index - in_start  # inorder list에서 root node를 기준으로 왼쪽 (left sub tree)
    r_len = in_end - index  # right sub tree

    preorder.append(root)

    dnc(in_start, index - 1, post_start, post_end - r_len - 1)  # left sub tree 탐색
    dnc(index + 1, in_end, post_start + l_len, post_end - 1)  # right sub tree 탐색


dnc(0, n - 1, 0, n - 1)

print(" ".join(map(str, preorder)))
